import urllib.request, json

url = 'https://karnata.in/data/dam_levels.json'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        raw = json.loads(resp.read().decode('utf-8'))
        print("Keys in /data/dam_levels.json:", list(raw.keys()))
        print("Has payload?", 'payload' in raw)
        print("Has dams?", 'dams' in raw)
except Exception as e:
    print("Error:", e)
