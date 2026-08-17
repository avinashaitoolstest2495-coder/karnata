import requests, sys, re, json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = 'https://www.josalukkasonline.com/gold-rate-today/Karnataka/'
r = requests.get(url, headers=headers, timeout=12)
soup = BeautifulSoup(r.text, 'html.parser')

print('Status:', r.status_code)
print('Title:', repr(soup.title.string if soup.title else ''))

print('\n=== SCRIPTS ===')
for idx, s in enumerate(soup.find_all('script')):
    txt = s.string or ''
    if any(k in txt.lower() for k in ['rate', 'gold', 'price', '18k', '22k', '24k', 'silver', 'api', 'state']):
        print(f'\n--- Script {idx} (len={len(txt)}) ---')
        print(txt[:1000])

print('\n=== TEXT DUMP OF ALL RATE SECTIONS ===')
for el in soup.find_all(class_=lambda c: c and any(k in str(c).lower() for k in ['rate', 'price', 'history', 'gold', 'table'])):
    txt = el.get_text(' | ', strip=True)
    if any(k in txt for k in ['22K', '24K', '18K', 'Silver', 'Rate', 'Gram']) and len(txt) < 500:
        print(f'<{el.name} class="{el.get("class")}">: {txt}\n')

# Check if there are API URLs in the JavaScript
js_apis = re.findall(r'https?://[^\s"\'<>]*(?:api|rate|gold)[^\s"\'<>]*', r.text, re.I)
print('\n=== POTENTIAL APIS IN JS ===')
for a in set(js_apis):
    print(' ', a)
