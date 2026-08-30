from bs4 import BeautifulSoup
import re
import json

with open('scratch_ksndmc_804.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Page title:", soup.title.string if soup.title else "No title")

# Find tables, cards, spans, ids
spans_with_id = soup.find_all(attrs={"id": True})
for s in spans_with_id[:25]:
    val = s.get_text(strip=True)
    if val:
        print(f"ID [{s['id']}]: {val[:60]}")

# Look for JavaScript data variables (e.g. rain data, high temp, low temp, gauge data)
scripts = soup.find_all('script')
for idx, sc in enumerate(scripts):
    s_text = sc.string or sc.get_text() or ''
    if any(k in s_text.lower() for k in ['rainfall', 'maxtemp', 'mintemp', 'heavy', 'extremes', 'highest', 'sampaje', 'gauge', 'var ']):
        print(f"\n--- SCRIPT {idx} snippet (len {len(s_text)}) ---")
        lines = [l.strip() for l in s_text.split('\n') if any(w in l.lower() for w in ['http', 'ajax', 'json', 'data', 'temp', 'rain', 'extreme', 'var '])]
        for l in lines[:15]:
            print("  ", l[:120])
