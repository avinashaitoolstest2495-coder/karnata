import json, base64, sys
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
for k, v in dams.items():
    if 'bhadra' in k.lower():
        print(k, "=> storage_pct:", v.get('storage_pct'), "storage_tmc:", v.get('storage_tmc'), "gross:", v.get('gross_storage_tmc'), "live:", v.get('live_storage_tmc'))
