import urllib.request
import json
import os

urls = [
    "https://karnata.in/data/news.json",
    "https://karnata.in/data/articles.json",
    "https://karnata.in/data/stories.json",
    "https://karnata.in/data/districts.json",
    "https://karnata.in/api/news",
    "https://karnata.in/karnataka-local-news.html",
    "https://karnata.in/karnataka-stories.html"
]

print("=== REMOTE CHECKS ===")
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as res:
            raw = res.read().decode("utf-8", errors="ignore")
            print(f"{u} -> HTTP {res.status}, length: {len(raw)}")
            if u.endswith(".json"):
                try:
                    d = json.loads(raw)
                    print(f"   Keys: {list(d.keys())[:5]}")
                    if "items" in d:
                        print(f"   items count: {len(d['items'])}")
                    if "articles" in d:
                        print(f"   articles count: {len(d['articles'])}")
                    if "payload" in d:
                        print("   has payload")
                except Exception as je:
                    print(f"   JSON parse error: {je}")
    except Exception as e:
        print(f"{u} -> ERROR: {e}")

print("\n=== LOCAL DATA FILES ===")
data_dir = "data"
if os.path.exists(data_dir):
    for f in os.listdir(data_dir):
        if f.endswith(".json"):
            fp = os.path.join(data_dir, f)
            size = os.path.getsize(fp)
            print(f"{f}: {size} bytes")
