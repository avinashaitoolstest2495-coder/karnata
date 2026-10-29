import json, base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/dam_levels.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

SECRET = "NK_SECURE_KEY_2026_KARNATA"
if 'payload' in raw:
    binary = base64.b64decode(raw['payload'])
    bytes_arr = bytearray(len(binary))
    for i in range(len(binary)):
        bytes_arr[i] = binary[i] ^ ord(SECRET[i % len(SECRET)])
    data = json.loads(bytes_arr.decode('utf-8'))
else:
    data = raw

print("Dams in live data/dam_levels.json:")
for k, v in data.get('dams', {}).items():
    print(f"  {k:15}: {v.get('storage_pct'):5.1f}% | {v.get('present_storage_tmc'):7.3f} / {v.get('max_storage_tmc'):7.3f} TMC | in={v.get('inflow_cusecs'):7.0f} out={v.get('outflow_cusecs'):7.0f} | date={v.get('date')}")
