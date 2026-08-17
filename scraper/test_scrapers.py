import requests
import xml.etree.ElementTree as ET
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

test_queries = [
    'https://news.google.com/rss/search?q=vijaykarnataka&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=vijaykarnataka+news&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=%22Vijaya+Karnataka%22&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=%22Vijay+Karnataka%22&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=%E0%B2%B5%E0%B2%BF%E0%B2%9C%E0%B2%AF+%E0%B2%95%E0%B2%B0%E0%B3%8D%E0%B2%A8%E0%B2%BE%E0%B2%9F%E0%B2%95&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=vijaykarnataka+karnataka&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=vijaykarnataka+bengaluru&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=vijaykarnataka+mysuru&hl=kn&gl=IN&ceid=IN:kn',
    'https://news.google.com/rss/search?q=vijaykarnataka+district&hl=kn&gl=IN&ceid=IN:kn'
]

articles = []
seen = set()

for q in test_queries:
    try:
        r = requests.get(q, headers=HEADERS, timeout=5)
        root = ET.fromstring(r.content)
        items = root.findall('.//item')
        print(f"Query: {q.split('q=')[1].split('&')[0]} -> {len(items)} items")
        for it in items:
            t = it.find('title').text if it.find('title') is not None else ''
            l = it.find('link').text if it.find('link') is not None else ''
            source_el = it.find('source')
            src = source_el.text if source_el is not None else ''
            t_clean = re.sub(r'\s*[-–—]\s*(Vijaya Karnataka|Vijay Karnataka|ವಿಜಯ ಕರ್ನಾಟಕ).*$', '', t, flags=re.I).strip()
            if ('vijay' in src.lower() or 'ವಿಜಯ' in src or 'vijaykarnataka' in l or 'vijay' in t.lower() or 'ವಿಜಯ' in t) and len(t_clean) >= 12:
                if t_clean not in seen:
                    seen.add(t_clean)
                    articles.append({'title': t_clean, 'url': l, 'source': 'ವಿಜಯ ಕರ್ನಾಟಕ (Vijay Karnataka)'})
    except Exception as e:
        print("Err:", e)

print(f"\nTotal Unique Vijaya Karnataka Articles Extracted: {len(articles)}")
