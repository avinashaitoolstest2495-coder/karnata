import urllib.request, json

url = 'https://karnata.in/api/voter-search?action=captcha'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Status:", resp.status)
        data = resp.read().decode('utf-8')
        print("Response:", data[:500])
except Exception as e:
    print("Error calling voter-search captcha:", e)
    if hasattr(e, 'read'):
        print("Error body:", e.read().decode('utf-8'))
