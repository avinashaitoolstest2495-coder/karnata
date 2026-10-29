import json, base64

SECRET = 'NK_SECURE_KEY_2026_KARNATA'
with open('data/petrol_rates.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

payload = base64.b64decode(raw['payload'])
decoded = bytearray(len(payload))
for i in range(len(payload)):
    decoded[i] = payload[i] ^ ord(SECRET[i % len(SECRET)])

data = json.loads(decoded.decode('utf-8'))
if 'dharwad' not in data.get('districts', {}):
    data['districts']['dharwad'] = {
        "name_en": "Dharwad",
        "name_kn": "ಧಾರವಾಡ",
        "taluks": {
            "hubballi": { "name_en": "Hubballi", "name_kn": "ಹುಬ್ಬಳ್ಳಿ", "latitude": 15.3647, "longitude": 75.124, "petrol": 111.2, "diesel": 99.12 },
            "dharwad": { "name_en": "Dharwad", "name_kn": "ಧಾರವಾಡ", "latitude": 15.4589, "longitude": 75.0078, "petrol": 111.2, "diesel": 99.12 }
        }
    }
    encoded_bytes = json.dumps(data, ensure_ascii=False).encode('utf-8')
    obf = bytearray(len(encoded_bytes))
    for i in range(len(encoded_bytes)):
        obf[i] = encoded_bytes[i] ^ ord(SECRET[i % len(SECRET)])
    raw['payload'] = base64.b64encode(obf).decode('ascii')
    with open('data/petrol_rates.json', 'w', encoding='utf-8') as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print("Added dharwad to data/petrol_rates.json successfully.")
else:
    print("Dharwad already in data/petrol_rates.json")
