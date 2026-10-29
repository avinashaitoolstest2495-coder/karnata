import requests, json

url = "https://water.karnataka.gov.in/CommonXyZABC.aspx/GetReservoirLocs"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://water.karnataka.gov.in",
    "Referer": "https://water.karnataka.gov.in/ReservoirPublic",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

try:
    resp = requests.post(url, json={}, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    data = resp.json()
    print("Keys:", list(data.keys()))
    if 'd' in data:
        raw_d = data['d']
        print("d snippet:", str(raw_d)[:300])
except Exception as e:
    print("API error:", e)
