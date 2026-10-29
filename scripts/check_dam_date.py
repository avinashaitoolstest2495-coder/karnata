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

print("last_updated:", data.get('last_updated'))
print("updated_at:", data.get('updated_at'))
print("source:", data.get('source'))
dams = data.get('dams', {})
print("Sample dam date:")
for k, v in list(dams.items())[:3]:
    print(f"  {k}: date={v.get('date')}, storage_pct={v.get('storage_pct')}, present_storage_tmc={v.get('present_storage_tmc')}, inflow={v.get('inflow_cusecs')}, outflow={v.get('outflow_cusecs')}")
