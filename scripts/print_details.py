import sys, re, os, json, xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

tree = ET.parse('sitemap.xml')
root = tree.getroot()
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap_urls = [elem.text.strip() for elem in root.findall('ns:url/ns:loc', ns)]

print("--- 1. MISMATCHED CANONICALS ---")
for u in sitemap_urls:
    path_part = u.replace('https://karnata.in', '').strip('/')
    fpath = 'index.html' if not path_part else (f"{path_part}.html" if os.path.exists(f"{path_part}.html") else (f"{path_part}/index.html" if os.path.exists(f"{path_part}/index.html") else path_part))
    if not fpath or not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    c_el = soup.find('link', attrs={'rel': 'canonical'})
    canon = c_el.get('href', '').strip() if c_el else ''
    if canon and canon.rstrip('/') != u.rstrip('/'):
        print(f"  Sitemap: {u}  vs  Canonical: {canon}")

print("\n--- 2. MISSING JSON-LD SCHEMA ---")
for u in sitemap_urls:
    path_part = u.replace('https://karnata.in', '').strip('/')
    fpath = 'index.html' if not path_part else (f"{path_part}.html" if os.path.exists(f"{path_part}.html") else (f"{path_part}/index.html" if os.path.exists(f"{path_part}/index.html") else path_part))
    if not fpath or not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    if not soup.find('script', attrs={'type': 'application/ld+json'}):
        print(f"  Missing schema: {u} ({fpath})")

print("\n--- 3. THIN CONTENT (< 300 words) ---")
for u in sitemap_urls:
    path_part = u.replace('https://karnata.in', '').strip('/')
    fpath = 'index.html' if not path_part else (f"{path_part}.html" if os.path.exists(f"{path_part}.html") else (f"{path_part}/index.html" if os.path.exists(f"{path_part}/index.html") else path_part))
    if not fpath or not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    body = soup.find('body')
    text = body.get_text() if body else ''
    words = len(text.split())
    if words < 300:
        print(f"  {u} ({fpath}): {words} words")

print("\n--- 4. ROBOTS.TXT CHECK FOR AI CRAWLERS ---")
if os.path.exists('robots.txt'):
    with open('robots.txt', 'r', encoding='utf-8') as fp:
        print(fp.read())
