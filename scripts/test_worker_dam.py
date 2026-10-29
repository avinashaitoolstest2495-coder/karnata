import urllib.request

url = 'https://karnata-scraper.avinashaitoolstest2495.workers.dev/dam'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        print("Response:", resp.read().decode('utf-8')[:500])
except Exception as e:
    print("Error:", e)
