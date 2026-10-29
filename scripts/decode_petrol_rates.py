import json, base64, sys
sys.stdout.reconfigure(encoding='utf-8')

SECRET = 'NK_SECURE_KEY_2026_KARNATA'
with open('data/petrol_rates.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

payload = base64.b64decode(raw['payload'])
decoded = bytearray(len(payload))
for i in range(len(payload)):
    decoded[i] = payload[i] ^ ord(SECRET[i % len(SECRET)])

data = json.loads(decoded.decode('utf-8'))
for d, info in data.get('districts', {}).items():
    t_first = list(info.get('taluks', {}).values())[0] if info.get('taluks') else {}
    print(f"{d}: petrol={t_first.get('petrol')}, diesel={t_first.get('diesel')}")

