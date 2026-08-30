import requests
import json
import re
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
url = 'https://ksndmc.org/en/WebDashboard'

try:
    res = requests.get(url, headers=headers, verify=False, timeout=15)
    print(f"Status: {res.status_code}")
    print(f"Length: {len(res.text)}")
    
    # Check if there are iframes or embedded dashboard urls
    iframes = re.findall(r'<iframe[^>]+src=["\']([^"\']+)["\']', res.text, re.IGNORECASE)
    print("Iframes:", iframes)
    
    # Check for keywords like highest rain, maximum temperature, minimum temperature, etc.
    with open('scratch_ksndmc.html', 'w', encoding='utf-8') as f:
        f.write(res.text)
    print("Saved scratch_ksndmc.html")

except Exception as e:
    print(f"Error fetching {url}: {e}")
