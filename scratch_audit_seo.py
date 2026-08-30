import os
import re
from bs4 import BeautifulSoup

public_pages = [
    'index.html',
    'weather.html',
    'gold.html',
    'dam-levels.html',
    'karnataka-stories.html',
    'apmc-prices.html',
    'transfers.html',
    'schemes.html',
    'cabinet-ministers.html',
    'mlas.html',
    'mps.html',
    'officers.html',
    'governor.html',
    'districts.html',
    'ask.html',
    'about.html',
    'contact.html',
    'privacy.html',
    'terms.html',
    'disclaimer.html'
]

results = []

for page in public_pages:
    if not os.path.exists(page):
        results.append(f"[MISSING] {page}")
        continue
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip() if soup.title and soup.title.string else 'NO_TITLE'
    desc = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
    desc_val = desc.get('content', '').strip() if desc else 'NO_DESC'
    
    canonical = soup.find('link', rel=re.compile(r'^canonical$', re.I))
    canonical_val = canonical.get('href', '').strip() if canonical else 'NO_CANONICAL'
    
    og_title = soup.find('meta', property=re.compile(r'^og:title$', re.I))
    og_desc = soup.find('meta', property=re.compile(r'^og:description$', re.I))
    og_locale = soup.find('meta', property=re.compile(r'^og:locale$', re.I))
    
    geo_region = soup.find('meta', attrs={'name': re.compile(r'^geo\.region$', re.I)})
    geo_place = soup.find('meta', attrs={'name': re.compile(r'^geo\.placename$', re.I)})
    
    json_ld = soup.find_all('script', type='application/ld+json')
    
    has_kannada_title = bool(re.search(r'[\u0C80-\u0CFF]', title))
    has_kannada_desc = bool(re.search(r'[\u0C80-\u0CFF]', desc_val))
    
    results.append({
        'page': page,
        'title': title[:60],
        'has_kn_title': has_kannada_title,
        'has_kn_desc': has_kannada_desc,
        'canonical': canonical_val,
        'og_locale': og_locale.get('content', '') if og_locale else 'NONE',
        'geo_region': geo_region.get('content', '') if geo_region else 'NONE',
        'json_ld_count': len(json_ld)
    })

for r in results:
    if isinstance(r, str):
        print(r)
    else:
        print(f"{r['page']:<22} | KN_Title: {str(r['has_kn_title']):<5} | KN_Desc: {str(r['has_kn_desc']):<5} | Can: {bool(r['canonical'] != 'NO_CANONICAL'):<5} | OG_Loc: {r['og_locale']:<7} | GEO: {r['geo_region']:<7} | JSON-LD: {r['json_ld_count']}")
