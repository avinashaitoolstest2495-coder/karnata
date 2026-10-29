import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

all_pages = sorted(glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html'))

results = []
bad_pages = []

for p in all_pages:
    # Skip excluded/admin files
    if any(k in p for k in ['admin', 'officers-admin', 'push-admin', 'constituency-detail', 'dam-details', 'scheme-detail', 'article.html']):
        continue
    
    c = open(p, 'r', encoding='utf-8', errors='ignore').read()
    h1s = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c, re.I)
    count = len(h1s)
    clean_h1 = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
    
    if count == 1:
        results.append((p, clean_h1[0]))
    else:
        bad_pages.append((p, count, clean_h1))

print(f'=== AUDIT REPORT: {len(results)} pages have EXACTLY ONE <h1> ===')
print(f'Pages failing single-H1 check: {len(bad_pages)}')
if bad_pages:
    for p, count, h1s in bad_pages:
        print(f'  FAILED: {p} ({count} h1s): {h1s}')
else:
    print('ALL public pages have EXACTLY ONE <h1>! Flawless compliance.')

print('\nSample 10 verified pages with their sole <h1>:')
for p, h in results[:10]:
    print(f'  {p} -> {h[:60]}')
