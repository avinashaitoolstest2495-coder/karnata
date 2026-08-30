import requests
import json
import re
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
url = 'https://ksndmc.org:804/'

try:
    res = requests.get(url, headers=headers, verify=False, timeout=15)
    print(f"Status: {res.status_code}")
    print(f"Length: {len(res.text)}")
    
    with open('scratch_ksndmc_804.html', 'w', encoding='utf-8') as f:
        f.write(res.text)
    print("Saved scratch_ksndmc_804.html")
    
    # Find script tags, ajax calls, api endpoints
    apis = re.findall(r'["\'](/?api/[^"\']+|/[^"\']+\.json|[^"\']+\.ashx|[^"\']+\.asmx|[^"\']+\.aspx/[^"\']+)["\']', res.text)
    print("APIs / Endpoints:", set(apis))

except Exception as e:
    print(f"Error fetching {url}: {e}")
