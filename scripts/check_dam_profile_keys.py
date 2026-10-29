import json, base64, sys, re
sys.stdout.reconfigure(encoding='utf-8')

SECRET = 'NK_SECURE_KEY_2026_KARNATA'
with open('data/dam_levels.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

if 'payload' in raw:
    payload = base64.b64decode(raw['payload'])
    decoded = bytearray(len(payload))
    for i in range(len(payload)):
        decoded[i] = payload[i] ^ ord(SECRET[i % len(SECRET)])
    data = json.loads(decoded.decode('utf-8'))
else:
    data = raw

dams = data.get('dams', {})
print("Dams in JSON:", list(dams.keys()))

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    html = f.read()

tbody_match = re.search(r'<tbody id="dam-profile-tbody">([\s\S]*?)</tbody>', html)
if tbody_match:
    rows = re.findall(r'<tr data-dam-key="([^"]+)">([\s\S]*?)</tr>', tbody_match.group(1))
    for k, r in rows:
        print(f"Table row key: {k}")
