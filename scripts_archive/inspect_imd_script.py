import urllib.request
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req, timeout=15) as res:
    html = res.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
for i, s in enumerate(soup.find_all('script')):
    txt = s.string or ''
    if 'district_shapefiles' in txt or 'Karnataka.json' in txt or 'warning' in txt.lower():
        print(f"=== SCRIPT {i} ===")
        print(txt[:3000])
        print("...")
