import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "x-api-key": "tYTy5eEhlu9rFjyxuCr7ra7ACp4dv1RH8gWuHTDc",
    "Origin": "https://www.myscheme.gov.in",
    "Referer": "https://www.myscheme.gov.in/"
}

d = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.myscheme.gov.in/schemes/v6/public/schemes?slug=iss&lang=kn", headers=HEADERS), timeout=10).read().decode("utf-8", "ignore"))["data"]

print("=== kn.schemeContent.benefits FULL ===")
print(json.dumps(d["kn"]["schemeContent"].get("benefits"), indent=2, ensure_ascii=False))
