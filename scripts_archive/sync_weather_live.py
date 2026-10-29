"""
Sync data/weather.json with live IMD warnings from data/imd_live_warnings.json
"""

import json
import base64
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).parent
SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def xor_crypt(raw_bytes, key):
    key_bytes = key.encode('utf-8')
    out = bytearray(len(raw_bytes))
    for i in range(len(raw_bytes)):
        out[i] = raw_bytes[i] ^ key_bytes[i % len(key_bytes)]
    return out

def decrypt_payload(encoded_str):
    raw_bytes = base64.b64decode(encoded_str)
    decrypted = xor_crypt(raw_bytes, SECRET_KEY)
    return json.loads(decrypted.decode('utf-8'))

def encrypt_payload(data_dict):
    raw_bytes = json.dumps(data_dict, ensure_ascii=False).encode('utf-8')
    encrypted = xor_crypt(raw_bytes, SECRET_KEY)
    return base64.b64encode(encrypted).decode('utf-8')

# 1. Load current weather.json
w_path = ROOT_DIR / "data" / "weather.json"
with open(w_path, "r", encoding="utf-8") as f:
    w_raw = json.load(f)
weather = decrypt_payload(w_raw["payload"])

# 2. Load live IMD warnings
with open(ROOT_DIR / "data" / "imd_live_warnings.json", "r", encoding="utf-8") as f:
    imd_live = json.load(f)

# IMD District name to internal ID
IMD_TO_ID = {
    'BAGALKOT': 'bagalkote',
    'BALLARI': 'ballari',
    'BELAGAVI': 'belagavi',
    'BENGALURU RURAL': 'bengaluru_rural',
    'BENGALURU URBAN': 'bengaluru_urban',
    'BIDAR': 'bidar',
    'CHAMARAJANAGAR': 'chamarajanagara',
    'CHIK BALLAPUR': 'chikkaballapura',
    'CHIKKAMAGALURU': 'chikkamagaluru',
    'CHITRADURGA': 'chitradurga',
    'DAKSHINA  KANNADA': 'dakshina_kannada',
    'DAVANGERE': 'davanagere',
    'DHARWAD': 'dharwad',
    'GADAG': 'gadag',
    'HASSAN': 'hassan',
    'HAVERI': 'haveri',
    'KALABURAGI': 'kalaburagi',
    'KODAGU': 'kodagu',
    'KOLAR': 'kolar',
    'KOPPAL': 'koppal',
    'MANDYA': 'mandya',
    'MYSURU': 'mysuru',
    'RAICHUR': 'raichur',
    'RAMANAGARAM': 'ramanagara',
    'SHIVAMOGGA': 'shivamogga',
    'TUMAKURU': 'tumakuru',
    'UDUPI': 'udupi',
    'UTTARA  KANNADA': 'uttara_kannada',
    'VIJAYAPURA': 'vijayapura',
    'VIJAYANAGARA': 'vijayanagara',
    'YADGIR': 'yadgir'
}

ID_TO_KN = {
    'bagalkote': 'ಬಾಗಲಕೋಟೆ',
    'ballari': 'ಬಳ್ಳಾರಿ',
    'belagavi': 'ಬೆಳಗಾವಿ',
    'bengaluru_rural': 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ',
    'bengaluru_urban': 'ಬೆಂಗಳೂರು ನಗರ',
    'bidar': 'ಬೀದರ್',
    'chamarajanagara': 'ಚಾಮರಾಜನಗರ',
    'chikkaballapura': 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ',
    'chikkamagaluru': 'ಚಿಕ್ಕಮಗಳೂರು',
    'chitradurga': 'ಚಿತ್ರದುರ್ಗ',
    'dakshina_kannada': 'ದಕ್ಷಿಣ ಕನ್ನಡ',
    'davanagere': 'ದಾವಣಗೆರೆ',
    'dharwad': 'ಧಾರವಾಡ',
    'gadag': 'ಗದಗ',
    'hassan': 'ಹಾಸನ',
    'haveri': 'ಹಾವೇರಿ',
    'kalaburagi': 'ಕಲಬುರಗಿ',
    'kodagu': 'ಕೊಡಗು',
    'kolar': 'ಕೋಲಾರ',
    'koppal': 'ಕೊಪ್ಪಳ',
    'mandya': 'ಮಂಡ್ಯ',
    'mysuru': 'ಮೈಸೂರು',
    'raichur': 'ರಾಯಚೂರು',
    'ramanagara': 'ರಾಮನಗರ',
    'shivamogga': 'ಶಿವಮೊಗ್ಗ',
    'tumakuru': 'ತುಮಕೂರು',
    'udupi': 'ಉಡುಪಿ',
    'uttara_kannada': 'ಉತ್ತರ ಕನ್ನಡ',
    'vijayapura': 'ವಿಜಯಪುರ',
    'vijayanagara': 'ವಿಜಯನಗರ',
    'yadgir': 'ಯಾದಗಿರಿ'
}

updated_warnings = {}
nowcast_districts = {}

for imd_dname, info in imd_live.items():
    did = IMD_TO_ID.get(imd_dname)
    if not did:
        continue
    color = info.get('color', '#008000').upper()
    if '#FFFF00' in color:
        lvl = 'yellow'
        color_hex = '#FACC15'
        alert_kn = 'ಹಳದಿ ನಿಗಾ (Yellow Watch)'
        hazard_kn = 'ಗುಡುಗು ಸಹಿತ ಸಾಧಾರಣ ಮಳೆ'
    elif '#FF0000' in color or '#DC2626' in color:
        lvl = 'red'
        color_hex = '#DC2626'
        alert_kn = 'ರೆಡ್ ಅಲರ್ಟ್ (Red Warning)'
        hazard_kn = 'ಅತಿ ಭಾರೀ ಮಳೆ & ಪ್ರವಾಹ ಮುನ್ನೆಚ್ಚರಿಕೆ'
    elif '#FFA500' in color or '#EA580C' in color or '#F97316' in color:
        lvl = 'orange'
        color_hex = '#EA580C'
        alert_kn = 'ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert)'
        hazard_kn = 'ಧಾರಾಕಾರ ಮಳೆ / ಬಿರುಗಾಳಿ'
    else:
        lvl = 'green'
        color_hex = '#16A34A'
        alert_kn = 'ಗ್ರೀನ್ ಜೋನ್ (Green Zone)'
        hazard_kn = 'ಸಾಮಾನ್ಯ / ಶುಭ ಹವೆ'

    d_kn = ID_TO_KN.get(did, did)
    w_entry = {
        'key': did,
        'district_kn': d_kn,
        'district_en': imd_dname.title(),
        'imd_id': info.get('id'),
        'level': lvl,
        'alert_level': lvl.upper(),
        'alert_level_kn': alert_kn,
        'hazard_kn': hazard_kn,
        'icon': '🌧️' if lvl in ['yellow', 'orange', 'red'] else '☀️',
        'color': color_hex,
        'warning_info': info.get('info', ''),
        'source': 'IMD MC Bengaluru Live Feed'
    }
    updated_warnings[did] = w_entry
    nowcast_districts[did] = w_entry

weather['imd_warnings'] = updated_warnings
if 'nowcast' not in weather:
    weather['nowcast'] = {}
weather['nowcast']['districts'] = nowcast_districts
weather['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Encrypt and save
new_enc = encrypt_payload(weather)
payload_obj = {"payload": new_enc}

with open(w_path, "w", encoding="utf-8") as f:
    json.dump(payload_obj, f, indent=2)

with open(ROOT_DIR / "namma-karnataka" / "data" / "weather.json", "w", encoding="utf-8") as f:
    json.dump(payload_obj, f, indent=2)

print(f"Successfully synchronized data/weather.json with live IMD warnings ({len(updated_warnings)} districts)!")
yellows = [v['district_kn'] for v in updated_warnings.values() if v['level'] == 'yellow']
greens = [v['district_kn'] for v in updated_warnings.values() if v['level'] == 'green']
print(f"Yellow ({len(yellows)}): {', '.join(yellows)}")
print(f"Green ({len(greens)}): {', '.join(greens)}")
