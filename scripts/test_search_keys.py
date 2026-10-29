import urllib.request, json

url = 'https://karnata.in/api/voter-search'

test_payloads = [
    {'epic': 'ABC1234567', 'captchaId': 'TEST', 'captcha': '1234'},
    {'epic': 'ABC1234567', 'captchaId': 'TEST', 'captchaValue': '1234'},
    {'epic': 'ABC1234567', 'captcha_id': 'TEST', 'captcha_val': '1234'},
    {'searchType': 'epic', 'epicNumber': 'ABC1234567', 'captchaId': 'TEST', 'captcha': '1234'},
    {'searchType': 'epic', 'epicNumber': 'ABC1234567', 'captchaId': 'TEST', 'captchaData': '1234'},
    {'epic': 'ABC1234567', 'captchaId': 'TEST', 'captchaData': '1234'},
]

for p in test_payloads:
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            print(p, "=> Success:", resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(list(p.keys()), "=> HTTP", e.code, body)
