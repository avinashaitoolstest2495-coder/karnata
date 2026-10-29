import json, base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check what the cards have in HTML:
for dam in ['krs', 'bhadra', 'malaprabha']:
    idx = html.find(f'data-dam-id="{dam}"')
    if idx == -1:
        # search by name
        pass
    print(f"--- CARD SEARCH FOR {dam} ---")

# Let's inspect data/dam_levels.json
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
if isinstance(dams, list):
    dam_dict = {d.get('id') or d.get('key') or d.get('name_en'): d for d in dams}
else:
    dam_dict = dams

for k in ['krs', 'bhadra', 'malaprabha']:
    # find matching dam
    match = None
    for dk, dv in dam_dict.items():
        if k in dk.lower() or (isinstance(dv, dict) and k in dv.get('name_en', '').lower()):
            match = dv
            break
    print(f"data/dam_levels.json for {k}:", match)

