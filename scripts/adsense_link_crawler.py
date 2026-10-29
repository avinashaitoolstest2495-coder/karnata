import os, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Read redirects
redirects = {}
if os.path.exists('_redirects'):
    with open('_redirects', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 2:
                    redirects[parts[0]] = parts[1]

# Crawl all public pages
public_html_files = sorted(glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html'))

all_internal_links = set()
broken_links = []
forbidden_links = []

FORBIDDEN_PATTERNS = ['/admin', '/scratch', '/studio', '/cms', '/imd_hub', '/test_', '/gold_edit', '/temp-cards', 'exact_yesterday']

for filepath in public_html_files:
    if any(k in filepath for k in ['admin', 'officers-admin', 'push-admin']):
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all hrefs
    hrefs = re.findall(r'href=[\"\x27]([^\#\?\"\x27]+)[\"\x27]', content)
    for href in hrefs:
        href = href.strip()
        if not href or href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:')):
            continue

        # Normalize href
        norm_href = href if href.startswith('/') else '/' + href
        all_internal_links.add((norm_href, filepath))

        # Check for forbidden paths
        for pat in FORBIDDEN_PATTERNS:
            if pat in norm_href:
                # Exclude false positives like /former-cms
                if pat == '/cms' and 'former-cms' in norm_href:
                    continue
                forbidden_links.append((norm_href, filepath, pat))

        # Check for broken links (does destination file or redirect exist?)
        # 1. Direct file check
        candidate_file = norm_href.lstrip('/')
        if candidate_file == '':
            candidate_file = 'index.html'
        
        exists = (
            os.path.exists(candidate_file) or
            os.path.exists(candidate_file + '.html') or
            os.path.exists(os.path.join(candidate_file, 'index.html')) or
            norm_href in redirects or
            (norm_href + '.html') in redirects or
            (norm_href.rstrip('/') + '.html') in redirects
        )

        if not exists:
            broken_links.append((norm_href, filepath))

print(f"=== ADSENSE COMPLIANCE LINK AUDIT ===")
print(f"Total distinct internal links scanned: {len(all_internal_links)}")
print(f"Forbidden / Admin / Test / Scratch links found: {len(forbidden_links)}")
if forbidden_links:
    for href, source, pat in forbidden_links:
        print(f"  ❌ FORBIDDEN: {href} (found in {source}, matched {pat})")
else:
    print("  ✅ ZERO forbidden admin/scratch/test links found across any public page!")

print(f"Broken internal links found: {len(broken_links)}")
if broken_links:
    for href, source in broken_links:
        print(f"  ❌ BROKEN: {href} (found in {source})")
else:
    print("  ✅ ZERO broken internal links found across all public pages!")

# Check for stub / under construction markers
stub_markers = ['under construction', 'coming soon', 'page not found', 'work in progress', 'placeholder text']
stub_pages = []
for filepath in public_html_files:
    if any(k in filepath for k in ['admin', 'officers-admin', 'push-admin']): continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read().lower()
    for marker in stub_markers:
        if marker in c:
            # Check context
            stub_pages.append((filepath, marker))

print(f"Stub / Under-construction pages found: {len(stub_pages)}")
if stub_pages:
    for p, m in stub_pages:
        print(f"  ⚠️ STUB WARNING: {p} matched '{m}'")
else:
    print("  ✅ ZERO stub / under construction pages detected!")

