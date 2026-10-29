import os, sys, re, json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Comprehensive SEO & AI GEO Audit across all pages...\n")

pages_dir = '.'
html_files = []
for root, dirs, files in os.walk(pages_dir):
    if any(p in root for p in ['.git', 'node_modules', 'scratch', 'namma-karnataka', 'cms', 'studio', 'admin']):
        continue
    for f in files:
        if f.endswith('.html') and not f.startswith(('scratch_', 'test_', 'gold_edit_')):
            html_files.append(os.path.join(root, f))

html_files.sort()
print(f"Auditing {len(html_files)} production HTML pages...")

issues = {
    'missing_title': [],
    'long_title': [],
    'short_title': [],
    'missing_desc': [],
    'long_desc': [],
    'short_desc': [],
    'missing_canonical': [],
    'invalid_canonical': [],
    'missing_og': [],
    'missing_jsonld': [],
    'jsonld_types': {},
    'invalid_h1': [],
    'low_word_count': [],
    'missing_robots_meta': [],
}

page_reports = []

for path in html_files:
    rel_path = os.path.relpath(path, '.').replace('\\', '/')
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Title
    title_el = soup.find('title')
    title_text = title_el.get_text().strip() if title_el else ''
    if not title_text:
        issues['missing_title'].append(rel_path)
    elif len(title_text) > 75:
        issues['long_title'].append((rel_path, len(title_text), title_text[:60]))
    elif len(title_text) < 25:
        issues['short_title'].append((rel_path, len(title_text), title_text))

    # 2. Meta Description
    desc_el = soup.find('meta', attrs={'name': 'description'})
    desc_text = desc_el.get('content', '').strip() if desc_el else ''
    if not desc_text:
        issues['missing_desc'].append(rel_path)
    elif len(desc_text) > 165:
        issues['long_desc'].append((rel_path, len(desc_text), desc_text[:60]))
    elif len(desc_text) < 50:
        issues['short_desc'].append((rel_path, len(desc_text), desc_text))

    # 3. Canonical
    canon_el = soup.find('link', attrs={'rel': 'canonical'})
    canon_href = canon_el.get('href', '').strip() if canon_el else ''
    if not canon_href:
        issues['missing_canonical'].append(rel_path)
    elif not canon_href.startswith('https://karnata.in/'):
        issues['invalid_canonical'].append((rel_path, canon_href))

    # 4. OpenGraph
    og_title = soup.find('meta', attrs={'property': 'og:title'})
    og_img = soup.find('meta', attrs={'property': 'og:image'})
    if not og_title or not og_img:
        issues['missing_og'].append(rel_path)

    # 5. JSON-LD Schema
    scripts = soup.find_all('script', attrs={'type': 'application/ld+json'})
    if not scripts:
        issues['missing_jsonld'].append(rel_path)
    else:
        for s in scripts:
            try:
                js_data = json.loads(s.string or '{}')
                stype = js_data.get('@type', 'Unknown')
                if isinstance(stype, list): stype = ",".join(stype)
                issues['jsonld_types'][stype] = issues['jsonld_types'].get(stype, 0) + 1
            except:
                pass

    # 6. H1 tag
    h1s = soup.find_all('h1')
    if len(h1s) != 1:
        issues['invalid_h1'].append((rel_path, len(h1s)))

    # 7. Word Count
    # extract body text
    body = soup.find('body')
    text = body.get_text() if body else ''
    words = len(text.split())
    if words < 250:
        issues['low_word_count'].append((rel_path, words))

print("\n=== AUDIT RESULTS SUMMARY ===")
print(f"Total Pages Audited: {len(html_files)}")
print(f"Missing Title: {len(issues['missing_title'])}")
print(f"Long Title (>75 chars): {len(issues['long_title'])}")
print(f"Short Title (<25 chars): {len(issues['short_title'])}")
print(f"Missing Description: {len(issues['missing_desc'])}")
print(f"Long Description (>165 chars): {len(issues['long_desc'])}")
print(f"Short Description (<50 chars): {len(issues['short_desc'])}")
print(f"Missing Canonical: {len(issues['missing_canonical'])}")
print(f"Invalid Canonical (not https://karnata.in/...): {len(issues['invalid_canonical'])}")
print(f"Missing OG Title/Image: {len(issues['missing_og'])}")
print(f"Missing JSON-LD Schema: {len(issues['missing_jsonld'])}")
print(f"Invalid H1 Count (!= 1): {len(issues['invalid_h1'])}")
print(f"Low Word Count (<250 words): {len(issues['low_word_count'])}")

print("\nJSON-LD Types Found across pages:")
for t, c in sorted(issues['jsonld_types'].items(), key=lambda x: -x[1]):
    print(f"  {t}: {c} pages")

if issues['missing_jsonld']:
    print(f"\nPages missing JSON-LD Schema ({len(issues['missing_jsonld'])}):")
    for p in issues['missing_jsonld'][:15]:
        print(f"  - {p}")

if issues['missing_canonical']:
    print(f"\nPages missing Canonical ({len(issues['missing_canonical'])}):")
    for p in issues['missing_canonical'][:15]:
        print(f"  - {p}")

if issues['missing_og']:
    print(f"\nPages missing OG tags ({len(issues['missing_og'])}):")
    for p in issues['missing_og'][:15]:
        print(f"  - {p}")

