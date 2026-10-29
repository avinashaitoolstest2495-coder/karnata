import urllib.request, json

url = 'https://karnata.in/api/voter-search'
payload = {
    'searchType': 'epic',
    'epicNumber': 'ABC1234567',
    'captchaId': 'TEST',
    'captchaData': '1234'
}
data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        print("Response:", resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
