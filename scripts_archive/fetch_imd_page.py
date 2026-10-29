import urllib.request
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, timeout=10) as res:
        html = res.read().decode('utf-8', errors='ignore')
        print(f"HTML Length: {len(html)}")
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Look for images
        for img in soup.find_all('img'):
            print("IMG:", img.get('src'))
            
        # Look for svg
        svgs = soup.find_all('svg')
        print(f"SVGs found: {len(svgs)}")
        
        # Look for script or canvas or map
        for s in soup.find_all('script'):
            txt = s.string or ''
            if 'geojson' in txt.lower() or 'district' in txt.lower() or 'warning' in txt.lower():
                print("SCRIPT snippet:", txt[:200])

except Exception as e:
    print("Error:", e)
