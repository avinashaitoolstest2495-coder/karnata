import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

all_pages = sorted(glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html'))

long_desc = []
for p in all_pages:
    if any(k in p for k in ['admin', 'officers-admin', 'push-admin', 'constituency-detail', 'dam-details', 'scheme-detail', 'article.html']):
        continue
    c = open(p, 'r', encoding='utf-8', errors='ignore').read()
    m = re.search(r'<meta\s+name=[\x22\x27]description[\x22\x27]\s+content=[\x22\x27]([\s\S]*?)[\x22\x27]', c, re.I)
    if m:
        desc = m.group(1).strip()
        if len(desc) > 160:
            long_desc.append((p, len(desc), desc))

print(f'Total pages with meta-description > 160 characters: {len(long_desc)}')
for p, length, desc in sorted(long_desc, key=lambda x: -x[1]):
    print(f'\n📄 {p} ({length} chars):')
    print(f'   Current:  \"{desc}\"')
