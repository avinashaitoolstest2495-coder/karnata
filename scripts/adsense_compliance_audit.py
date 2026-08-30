# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_xml = f.read()

urls = re.findall(r'<loc>(https://karnata\.in/[^<]*)</loc>', sitemap_xml)
print(f"Total URLs in sitemap: {len(urls)}")

report = {
    'total_pages_scanned': 0,
    'pages_with_adsense_script': 0,
    'pages_missing_adsense_script': [],
    'thin_pages': [],
    'rich_pages': [],
    'ads_txt_exists': False
}

ads_txt_path = os.path.join(ROOT_DIR, 'ads.txt')
if os.path.exists(ads_txt_path):
    with open(ads_txt_path, 'r', encoding='utf-8') as f:
        ads_content = f.read()
    report['ads_txt_exists'] = 'ca-pub-4907996917420478' in ads_content or 'google.com' in ads_content

for u in urls:
    rel_path = u.replace('https://karnata.in/', '').strip()
    if not rel_path:
        rel_file = 'index.html'
    elif rel_path.endswith('/'):
        rel_file = os.path.join(rel_path, 'index.html')
    elif os.path.exists(os.path.join(ROOT_DIR, rel_path + '.html')):
        rel_file = rel_path + '.html'
    elif os.path.exists(os.path.join(ROOT_DIR, rel_path, 'index.html')):
        rel_file = os.path.join(rel_path, 'index.html')
    elif os.path.exists(os.path.join(ROOT_DIR, rel_path)):
        rel_file = rel_path
    else:
        continue

    full_path = os.path.join(ROOT_DIR, rel_file)
    if not os.path.exists(full_path):
        continue

    report['total_pages_scanned'] += 1
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    has_adsense = 'ca-pub-4907996917420478' in html or 'pagead2.googlesyndication.com' in html
    if has_adsense:
        report['pages_with_adsense_script'] += 1
    else:
        report['pages_missing_adsense_script'].append(rel_file)

    soup = BeautifulSoup(html, 'html.parser')
    for elem in soup(['script', 'style', 'svg', 'noscript']):
        elem.extract()
    text = soup.get_text(separator=' ')
    words = text.split()
    word_count = len(words)

    page_summary = {
        'file': rel_file,
        'url': u,
        'words': word_count,
        'has_adsense': has_adsense
    }

    if word_count < 250:
        report['thin_pages'].append(page_summary)
    else:
        report['rich_pages'].append(page_summary)

print("\n============================================================")
print("GOOGLE ADSENSE READINESS AUDIT REPORT")
print("============================================================")
print(f"Total Public Pages Audited: {report['total_pages_scanned']}")
print(f"Pages with AdSense Tag: {report['pages_with_adsense_script']} / {report['total_pages_scanned']}")
print(f"ads.txt Status: {'[PASS] Valid & Active' if report['ads_txt_exists'] else '[FAIL] Missing or Invalid'}")

print(f"\nSubstantial / Rich Content Pages (>= 250 words): {len(report['rich_pages'])}")
print(f"Thin Content Pages (< 250 words): {len(report['thin_pages'])}")

if report['thin_pages']:
    print("\n--- THIN PAGES DETECTED ---")
    for tp in report['thin_pages']:
        print(f"  * {tp['file']} ({tp['words']} words) -> {tp['url']}")

if report['pages_missing_adsense_script']:
    print("\n--- PAGES MISSING ADSENSE TAG ---")
    for mp in report['pages_missing_adsense_script'][:10]:
        print(f"  * {mp}")

print("\n============================================================")
