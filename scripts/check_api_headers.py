import urllib.request

url = 'https://karnata.in/api/voter-search?action=captcha'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
print("Headers:")
for k, v in resp.headers.items():
    print(f"  {k}: {v}")
