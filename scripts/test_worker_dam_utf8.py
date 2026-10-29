import urllib.request, sys, json
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://karnata-scraper.avinashaitoolstest2495.workers.dev/dam'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Updated at:", data.get('updated_at'))
        print("Dams count:", len(data.get('dams', {})))
        for k, v in list(data.get('dams', {}).items())[:3]:
            print(k, ":", v.get('date'), "storage_pct:", v.get('storage_pct'))
except Exception as e:
    print("Error:", e)
