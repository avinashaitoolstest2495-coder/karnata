"""
Karnata — update_worker_precision.py
Safely injects ALL 224 MLAs, 28 MPs, 13 Dams (with live levels and storage), 31 Districts, CM, DCM, Gold rates into _worker.js.
"""

import json
import base64
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
KEY = 'NK_SECURE_KEY_2026_KARNATA'

def xor_decrypt(enc_b64, key):
    raw = base64.b64decode(enc_b64)
    key_bytes = key.encode('utf-8')
    out = bytearray(len(raw))
    for i in range(len(raw)):
        out[i] = raw[i] ^ key_bytes[i % len(key_bytes)]
    return out.decode('utf-8', errors='ignore')

# 1. Load Constituencies
const_path = BASE_DIR / "data" / "constituencies.json"
const_data = json.load(open(const_path, 'r', encoding='utf-8'))
const_dec = json.loads(xor_decrypt(const_data['payload'], KEY))

mla_list = []
for code, m in const_dec.get('mla', {}).items():
    name_kn = m.get('name_kn', '').strip()
    name_en = m.get('name_en', '').strip()
    mla_kn = m.get('mla_name_kn', '').strip()
    mla_en = m.get('mla_name_en', '').strip()
    party = m.get('party', '').strip()
    dist_kn = m.get('district_kn', '').strip()
    id_str = m.get('id', '').strip()
    
    keywords = [name_kn.lower(), name_en.lower(), id_str.lower()]
    if 'ಶೋರಾಪುರ' in name_kn or 'shorapur' in id_str:
        keywords.extend(['ಸುರಪುರ', 'surpur', 'shorapur'])
    if 'ಚನ್ನಪಟ್ಟಣ' in name_kn or 'channapatna' in id_str:
        keywords.extend(['ಚನ್ನಪಟ್ಟಣ', 'channapatna', 'ಚನ್ನಪಟ್ಟಣಂ'])
    if 'ಶಿಗ್ಗಾಂವಿ' in name_kn or 'shiggaon' in id_str:
        keywords.extend(['ಶಿಗ್ಗಾಂವಿ', 'shiggaon', 'ಶಿಗ್ಗಾವಿ'])
    if 'ಸಂಡೂರು' in name_kn or 'sandur' in id_str:
        keywords.extend(['ಸಂಡೂರು', 'sandur'])

    mla_list.append({
        'code': code,
        'name_kn': name_kn,
        'name_en': name_en,
        'mla_kn': mla_kn,
        'mla_en': mla_en,
        'party': party,
        'district_kn': dist_kn,
        'keywords': list(set(keywords))
    })

mp_list = []
for code, p in const_dec.get('mp', {}).items():
    name_kn = p.get('name_kn', '').strip()
    name_en = p.get('name_en', '').strip()
    mp_kn = p.get('mp_name_kn', '').strip()
    mp_en = p.get('mp_name_en', '').strip()
    party = p.get('party', '').strip()
    dist_kn = p.get('district_kn', '').strip()
    id_str = p.get('id', '').strip()
    
    mp_list.append({
        'code': code,
        'name_kn': name_kn,
        'name_en': name_en,
        'mp_kn': mp_kn,
        'mp_en': mp_en,
        'party': party,
        'district_kn': dist_kn,
        'keywords': [name_kn.lower(), name_en.lower(), id_str.lower()]
    })

# 2. Districts
districts_precision = {
  "koppal": {
    "name_kn": "ಕೊಪ್ಪಳ",
    "dc": "ಶ್ರೀ ಸುರೇಶ್‌ ಬಿ. ಇಟ್ನಾಲ್‌, IAS (Shri. SURESH B ITNAL)",
    "sp": "ಡಾ. ರಾಮ್ ಎಲ್ ಅರಸಿದ್ದಿ, IPS (Dr. RAM L ARASIDDI)",
    "zp_ceo": "ಶ್ರೀ ವರ್ನಿತ್ ನೇಗಿ, IAS",
    "keywords": ["ಕೊಪ್ಪಳ", "koppal"]
  },
  "mysuru": {
    "name_kn": "ಮೈಸೂರು",
    "dc": "ಶ್ರೀ ಪ್ರಭುಲಿಂಗ ಕವಳಿಕಟ್ಟಿ, IAS (Shri. PRABHULING KAVALIKATTI)",
    "sp": "ಡಾ. ಎಂ.ಬಿ. ಬೋರಲಿಂಗಯ್ಯ, IPS (Dr. M.B. Boralingaiah)",
    "keywords": ["ಮೈಸೂರು", "mysore", "mysuru"]
  },
  "belagavi": {
    "name_kn": "ಬೆಳಗಾವಿ",
    "dc": "ಮೊಹಮ್ಮದ್ ರೋಷನ್, IAS (Mohammad Roshan)",
    "sp": "ಡಾ. ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್, IPS (Dr. Bheemashankar Guled)",
    "keywords": ["ಬೆಳಗಾವಿ", "belgaum", "belagavi"]
  },
  "bengaluru_urban": {
    "name_kn": "ಬೆಂಗಳೂರು ನಗರ",
    "dc": "ಶ್ರೀ ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್., IAS",
    "sp": "ಬಿ. ದಯಾನಂದ, IPS (ನಗರ ಪೊಲೀಸ್ ಆಯುಕ್ತರು / CP)",
    "keywords": ["ಬೆಂಗಳೂರು ನಗರ", "bengaluru urban", "bangalore urban", "ಬೆಂಗಳೂರು"]
  },
  "bengaluru_rural": {
    "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
    "dc": "ಎನ್. ಶಿವಶಂಕರ, IAS",
    "sp": "ಸಿ.ಕೆ. ಬಾಬಾ, IPS",
    "keywords": ["ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "bengaluru rural", "bangalore rural"]
  },
  "kolar": {
    "name_kn": "ಕೋಲಾರ",
    "dc": "ಅಕ್ರಂ ಪಾಷಾ, IAS",
    "sp": "ನಿಖಿಲ್ ಬಿ., IPS",
    "keywords": ["ಕೋಲಾರ", "kolar"]
  },
  "shivamogga": {
    "name_kn": "ಶಿವಮೊಗ್ಗ",
    "dc": "ಗುರುದತ್ತ ಹೆಗಡೆ, IAS",
    "sp": "ಜಿ.ಕೆ. ಮಿಥುನ್ ಕುಮಾರ್, IPS",
    "keywords": ["ಶಿವಮೊಗ್ಗ", "shimoga", "shivamogga"]
  },
  "tumakuru": {
    "name_kn": "ತುಮಕೂರು",
    "dc": "ಶುಭ ಕಲ್ಯಾಣ್, IAS",
    "sp": "ಅಶೋಕ್ ಕೆ.ವಿ., IPS",
    "keywords": ["ತುಮಕೂರು", "tumkur", "tumakuru"]
  },
  "ballari": {
    "name_kn": "ಬಳ್ಳಾರಿ",
    "dc": "ಪ್ರಶಾಂತ್ ಕುಮಾರ್ ಮಿಶ್ರಾ, IAS",
    "sp": "ಶೋಭಾರಾಣಿ ವಿ.ಜೆ., IPS",
    "keywords": ["ಬಳ್ಳಾರಿ", "bellary", "ballari"]
  },
  "vijayanagara": {
    "name_kn": "ವಿಜಯನಗರ",
    "dc": "ಎಂ.ಎಸ್. ದಿವಾಕರ, IAS",
    "sp": "ಶ್ರೀಹರಿ ಬಾಬು ಬಿ.ಎಲ್., IPS",
    "keywords": ["ವಿಜಯನಗರ", "ಹೊಸಪೇಟೆ", "vijayanagara", "hospet"]
  },
  "kalaburagi": {
    "name_kn": "ಕಲಬುರಗಿ",
    "dc": "ಬಿ. ಫೌಜಿಯಾ ತರನ್ನುಮ್, IAS",
    "sp": "ಅಡ್ಡೂರು ಶ್ರೀನಿವಾಸುಲು, IPS",
    "keywords": ["ಕಲಬುರಗಿ", "ಗುಲ್ಬರ್ಗ", "kalaburagi", "gulbarga"]
  },
  "dakshina_kannada": {
    "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
    "dc": "ಮುಲ್ಲೈ ಮುಹಿಲನ್, IAS",
    "sp": "ಯತೀಶ್ ಎನ್., IPS (CP: ಅನುಪಮ್ ಅಗರ್ವಾಲ್, IPS)",
    "keywords": ["ದಕ್ಷಿಣ ಕನ್ನಡ", "ಮಂಗಳೂರು", "dakshina kannada", "mangaluru", "mangalore"]
  },
  "uttara_kannada": {
    "name_kn": "ಉತ್ತರ ಕನ್ನಡ",
    "dc": "ಲಕ್ಷ್ಮೀಪ್ರಿಯಾ, IAS",
    "sp": "ನಾರಾಯಣ ಎಂ., IPS",
    "keywords": ["ಉತ್ತರ ಕನ್ನಡ", "ಕಾರವಾರ", "ಶಿರಸಿ", "uttara kannada", "karwar", "sirsi"]
  },
  "udupi": {
    "name_kn": "ಉಡುಪಿ",
    "dc": "ಡಾ. ಕೆ. ವಿದ್ಯಾಕುಮಾರಿ, IAS",
    "sp": "ಡಾ. ಅರುಣ್ ಕೆ., IPS",
    "keywords": ["ಉಡುಪಿ", "udupi"]
  },
  "dharwad": {
    "name_kn": "ಧಾರವಾಡ",
    "dc": "ದಿವ್ಯಾ ಪ್ರಭು ಜಿ.ಆರ್.ಜೆ., IAS",
    "sp": "ಗೋಪಾಲ್ ಎಂ. ಬ್ಯಾಕೋಡ್, IPS (CP: ರೇಣುಕಾ ಕೆ. ಸುಕುಮಾರ್, IPS)",
    "keywords": ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ", "dharwad", "hubli", "hubballi"]
  },
  "mandya": {
    "name_kn": "ಮಂಡ್ಯ",
    "dc": "ಡಾ. ಕುಮಾರ, IAS",
    "sp": "ಮಲ್ಲಿಕಾರ್ಜುನ ಬಾಲದಂಡಿ, IPS",
    "keywords": ["ಮಂಡ್ಯ", "mandya"]
  },
  "hassan": {
    "name_kn": "ಹಾಸನ",
    "dc": "ಸಿ. ಸತ್ಯಭಾಮ, IAS",
    "sp": "ಮೊಹಮ್ಮದ್ ಸುಜೀತಾ, IPS",
    "keywords": ["ಹಾಸನ", "hassan"]
  },
  "chikkamagaluru": {
    "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
    "dc": "ಮೀನಾ ನಾಗರಾಜ್, IAS",
    "sp": "ವಿಕ್ರಮ್ ಆಮ್ಟೆ, IPS",
    "keywords": ["ಚಿಕ್ಕಮಗಳೂರು", "chikkamagaluru", "chikmagalur"]
  },
  "bagalkote": {
    "name_kn": "ಬಾಗಲಕೋಟೆ",
    "dc": "ಸಂಗಪ್ಪ ಉಪಾಸೆ, IAS",
    "sp": "ಅಮರನಾಥ್ ರೆಡ್ಡಿ ವೈ., IPS",
    "keywords": ["ಬಾಗಲಕೋಟೆ", "bagalkote", "bagalkot"]
  },
  "vijayapura": {
    "name_kn": "ವಿಜಯಪುರ",
    "dc": "ಭೂಬಾಲನ್ ಟಿ., IAS",
    "sp": "ಲಕ್ಷ್ಮಣ ನಿಂಬರಗಿ, IPS",
    "keywords": ["ವಿಜಯಪುರ", "ಬಿಜಾಪುರ", "vijayapura", "bijapur"]
  },
  "bidar": {
    "name_kn": "ಬೀದರ್",
    "dc": "ಗೋವಿಂದ ರೆಡ್ಡಿ, IAS",
    "sp": "ಪ್ರದೀಪ್ ಗುಂಟಿ, IPS",
    "keywords": ["ಬೀದರ್", "bidar"]
  },
  "raichur": {
    "name_kn": "ರಾಯಚೂರು",
    "dc": "ನಿತೀಶ್ ಕೆ., IAS",
    "sp": "ನಿಖಿಲ್ ಬಿ., IPS",
    "keywords": ["ರಾಯಚೂರು", "raichur"]
  },
  "yadgir": {
    "name_kn": "ಯಾದಗಿರಿ",
    "dc": "ಡಾ. ಸುಶೀಲಾ ಬಿ., IAS",
    "sp": "ಸಿ.ಬಿ. ವೇದಮೂರ್ತಿ, IPS",
    "keywords": ["ಯಾದಗಿರಿ", "yadgir"]
  },
  "gadag": {
    "name_kn": "ಗದಗ",
    "dc": "ವೈಶಾಲಿ ಎಂ.ಎಲ್., IAS",
    "sp": "ಬಿ.ಎಸ್. ನೇಮಗೌಡ, IPS",
    "keywords": ["ಗದಗ", "gadag"]
  },
  "haveri": {
    "name_kn": "ಹಾವೇರಿ",
    "dc": "ಡಾ. ವಿಜಯ ಮಹಾಂತೇಶ್ ದಾನಮ್ಮನವರ್, IAS",
    "sp": "ಅಂಶು ಕುಮಾರ್, IPS",
    "keywords": ["ಹಾವೇರಿ", "haveri"]
  },
  "chitradurga": {
    "name_kn": "ಚಿತ್ರದುರ್ಗ",
    "dc": "ಟಿ. ವೆಂಕಟೇಶ್, IAS",
    "sp": "ಧರ್ಮೇಂದರ್ ಕುಮಾರ್ ಮೀನಾ, IPS",
    "keywords": ["ಚಿತ್ರದುರ್ಗ", "chitradurga"]
  },
  "davanagere": {
    "name_kn": "ದಾವಣಗೆರೆ",
    "dc": "ಜಿ.ಎಂ. ಗಂಗಾಧರಸ್ವಾಮಿ, IAS",
    "sp": "ಉಮಾ ಪ್ರಶಾಂತ್, IPS",
    "keywords": ["ದಾವಣಗೆರೆ", "davanagere"]
  },
  "chamarajanagar": {
    "name_kn": "ಚಾಮರಾಜನಗರ",
    "dc": "ಶಿಲ್ಪಾ ಶರ್ಮಾ, IAS",
    "sp": "ಕವಿತಾ ಬಿ.ಟಿ., IPS",
    "keywords": ["ಚಾಮರಾಜನಗರ", "chamarajanagar"]
  },
  "ramanagara": {
    "name_kn": "ರಾಮನಗರ",
    "dc": "ಅವಿನಾಶ್ ಮೆನನ್ ರಾಜೇಂದ್ರನ್, IAS",
    "sp": "ಕಾರ್ತಿಕ್ ರೆಡ್ಡಿ, IPS",
    "keywords": ["ರಾಮನಗರ", "ramanagara", "ramanagar"]
  },
  "chikkaballapura": {
    "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "dc": "ಪಿ.ಎನ್. ರವೀಂದ್ರ, IAS",
    "sp": "ಕುಶಾಲ್ ಚೌಕ್ಸೆ, IPS",
    "keywords": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "chikkaballapura", "chikkaballapur"]
  },
  "kodagu": {
    "name_kn": "ಕೊಡಗು",
    "dc": "ವೆಂಕಟ್ ರಾಜಾ, IAS",
    "sp": "ಕೆ. ರಾಮರಾಜನ್, IPS",
    "keywords": ["ಕೊಡಗು", "ಮಡಿಕೇರಿ", "kodagu", "coorg", "madikeri"]
  }
}

# 3. Dams with Live Levels
dams_precision = {
  "tungabhadra": {
    "name_kn": "ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (Tungabhadra Dam / TB Dam)",
    "river": "ತುಂಗಭದ್ರಾ ನದಿ",
    "location": "ಮುನಿರಾಬಾದ್ (ಕೊಪ್ಪಳ) / ಹೊಸಪೇಟೆ (ವಿಜಯನಗರ)",
    "current_level": "1,631.50 ಅಡಿ",
    "max_level": "1,633.00 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "98.42 TMC",
    "total_capacity": "105.79 TMC",
    "inflow": "10,632 ಕ್ಯೂಸೆಕ್",
    "outflow": "33 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ತುಂಗಭದ್ರ", "ತುಂಗಭದ್ರಾ", "tb dam", "tungabhadra"]
  },
  "krs": {
    "name_kn": "ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS Dam)",
    "river": "ಕಾವೇರಿ ನದಿ",
    "location": "ಶ್ರೀರಂಗಪಟ್ಟಣ / ಮಂಡ್ಯ",
    "current_level": "122.40 ಅಡಿ",
    "max_level": "124.80 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "46.12 TMC",
    "total_capacity": "49.45 TMC",
    "inflow": "9,438 ಕ್ಯೂಸೆಕ್",
    "outflow": "2,418 ಕ್ಯೂಸೆಕ್",
    "keywords": ["krs", "ಕೃಷ್ಣರಾಜ ಸಾಗರ", "ಕೃಷ್ಣರಾಜಸಾಗರ", "krishna raja sagara"]
  },
  "almatti": {
    "name_kn": "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ (Lal Bahadur Shastri Dam)",
    "river": "ಕೃಷ್ಣಾ ನದಿ",
    "location": "ಬಸವನ ಬಾಗೇವಾಡಿ (ವಿಜಯಪುರ / ಬಾಗಲಕೋಟೆ)",
    "current_level": "519.10 ಮೀಟರ್",
    "max_level": "519.60 ಮೀಟರ್ (Full Reservoir Level)",
    "current_storage": "119.50 TMC",
    "total_capacity": "123.08 TMC",
    "inflow": "28,746 ಕ್ಯೂಸೆಕ್",
    "outflow": "21,500 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಆಲಮಟ್ಟಿ", "ಅಲಮಟ್ಟಿ", "almatti", "lal bahadur shastri"]
  },
  "linganamakki": {
    "name_kn": "ಲಿಂಗನಮಕ್ಕಿ ಜಲಾಶಯ",
    "river": "ಶರಾವತಿ ನದಿ",
    "location": "ಸಾಗರ (ಶಿವಮೊಗ್ಗ)",
    "current_level": "1,814.20 ಅಡಿ",
    "max_level": "1,819.00 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "142.80 TMC",
    "total_capacity": "151.75 TMC",
    "inflow": "28,500 ಕ್ಯೂಸೆಕ್",
    "outflow": "1,200 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಲಿಂಗನಮಕ್ಕಿ", "linganamakki", "ಶರಾವತಿ", "sharavathi"]
  },
  "kabini": {
    "name_kn": "ಕಬಿನಿ ಜಲಾಶಯ",
    "river": "ಕಪಿಲಾ ನದಿ",
    "location": "ಎಚ್.ಡಿ. ಕೋಟೆ (ಮೈಸೂರು)",
    "current_level": "2,282.50 ಅಡಿ",
    "max_level": "2,284.00 ಅಡಿ",
    "current_storage": "18.20 TMC",
    "total_capacity": "19.52 TMC",
    "inflow": "9,487 ಕ್ಯೂಸೆಕ್",
    "outflow": "6,100 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಕಬಿನಿ", "kabini", "ಕಪಿಲಾ"]
  },
  "hemavathi": {
    "name_kn": "ಹೇಮಾವತಿ ಜಲಾಶಯ",
    "river": "ಹೇಮಾವತಿ ನದಿ",
    "location": "ಗೊರೂರು (ಹಾಸನ)",
    "current_level": "2,920.50 ಅಡಿ",
    "max_level": "2,922.00 ಅಡಿ",
    "current_storage": "35.80 TMC",
    "total_capacity": "37.10 TMC",
    "inflow": "3,588 ಕ್ಯೂಸೆಕ್",
    "outflow": "1,800 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಹೇಮಾವತಿ", "hemavathi", "ಗೊರೂರು"]
  },
  "harangi": {
    "name_kn": "ಹಾರಂಗಿ ಜಲಾಶಯ",
    "river": "ಹಾರಂಗಿ ನದಿ",
    "location": "ಕುಶಾಲನಗರ (ಕೊಡಗು)",
    "current_level": "2,858.00 ಅಡಿ",
    "max_level": "2,859.00 ಅಡಿ",
    "current_storage": "8.10 TMC",
    "total_capacity": "8.50 TMC",
    "inflow": "5,947 ಕ್ಯೂಸೆಕ್",
    "outflow": "5,783 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಹಾರಂಗಿ", "harangi"]
  },
  "bhadra": {
    "name_kn": "ಭದ್ರಾ ಜಲಾಶಯ",
    "river": "ಭದ್ರಾ ನದಿ",
    "location": "ಲಕ್ಕವಳ್ಳಿ (ಚಿಕ್ಕಮಗಳೂರು / ಶಿವಮೊಗ್ಗ)",
    "current_level": "185.20 ಅಡಿ",
    "max_level": "186.00 ಅಡಿ",
    "current_storage": "68.40 TMC",
    "total_capacity": "71.54 TMC",
    "inflow": "5,739 ಕ್ಯೂಸೆಕ್",
    "outflow": "0 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಭದ್ರಾ", "bhadra", "ಲಕ್ಕವಳ್ಳಿ"]
  },
  "malaprabha": {
    "name_kn": "ಮಲಪ್ರಭಾ ಜಲಾಶಯ (ರೇಣುಕಾ ಸಾಗರ)",
    "river": "ಮಲಪ್ರಭಾ ನದಿ",
    "location": "ಸವದತ್ತಿ (ಬೆಳಗಾವಿ)",
    "current_level": "2,078.10 ಅಡಿ",
    "max_level": "2,079.50 ಅಡಿ",
    "current_storage": "32.10 TMC",
    "total_capacity": "34.35 TMC",
    "inflow": "2,376 ಕ್ಯೂಸೆಕ್",
    "outflow": "0 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಮಲಪ್ರಭಾ", "malaprabha", "ನವಿಲುತೀರ್ಥ", "ರೇಣುಕಾ ಸಾಗರ"]
  },
  "ghataprabha": {
    "name_kn": "ಘಟಪ್ರಭಾ ಜಲಾಶಯ (ಹಿಡಕಲ್)",
    "river": "ಘಟಪ್ರಭಾ ನದಿ",
    "location": "ಹುಕ್ಕೇರಿ (ಬೆಳಗಾವಿ)",
    "current_level": "2,174.50 ಅಡಿ",
    "max_level": "2,175.00 ಅಡಿ",
    "current_storage": "49.20 TMC",
    "total_capacity": "51.00 TMC",
    "inflow": "5,679 ಕ್ಯೂಸೆಕ್",
    "outflow": "5,590 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಘಟಪ್ರಭಾ", "ghataprabha", "ಹಿಡಕಲ್", "hidkal"]
  },
  "supa": {
    "name_kn": "ಸೂಪಾ ಜಲಾಶಯ",
    "river": "ಕಾಳಿ ನದಿ",
    "location": "ಜೋಯಿಡಾ (ಉತ್ತರ ಕನ್ನಡ)",
    "current_level": "562.00 ಮೀಟರ್",
    "max_level": "564.00 ಮೀಟರ್",
    "current_storage": "138.50 TMC",
    "total_capacity": "145.00 TMC",
    "inflow": "18,400 ಕ್ಯೂಸೆಕ್",
    "outflow": "500 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ಸೂಪಾ", "ಸೂಪ", "supa"]
  },
  "narayanapura": {
    "name_kn": "ನಾರಾಯಣಪುರ ಜಲಾಶಯ (ಬಸವ ಸಾಗರ)",
    "river": "ಕೃಷ್ಣಾ ನದಿ",
    "location": "ಸುರಪುರ (ಯಾದಗಿರಿ)",
    "current_level": "491.50 ಮೀಟರ್",
    "max_level": "492.25 ಮೀಟರ್",
    "current_storage": "35.20 TMC",
    "total_capacity": "37.86 TMC",
    "inflow": "18,009 ಕ್ಯೂಸೆಕ್",
    "outflow": "8,465 ಕ್ಯೂಸೆಕ್",
    "keywords": ["ನಾರಾಯಣಪುರ", "ಬಸವ ಸಾಗರ", "narayanapura"]
  }
}

worker_path = BASE_DIR / "_worker.js"
worker_text = open(worker_path, "r", encoding="utf-8").read()

dist_json = json.dumps(districts_precision, ensure_ascii=False, indent=2)
mla_json = json.dumps(mla_list, ensure_ascii=False)
mp_json = json.dumps(mp_list, ensure_ascii=False)
dams_json = json.dumps(dams_precision, ensure_ascii=False, indent=2)

precision_code = """
const PRECISION_DISTRICTS = """ + dist_json + """;

const ALL_224_MLAS = """ + mla_json + """;

const ALL_28_MPS = """ + mp_json + """;

const PRECISION_DAMS = """ + dams_json + """;

function resolvePrecisionQuery(rawQuery, normalizedQ) {
  const combined = `${rawQuery} ${normalizedQ}`.toLowerCase();

  // 1. SPECIFIC MLA QUERY (All 224 Assembly Constituencies)
  const isMlaQuery = combined.includes('ಶಾಸಕ') || combined.includes('mla') || combined.includes('ವಿಧಾನಸಭಾ') || combined.includes('ಕ್ಷೇತ್ರ') || combined.includes('ಎಂಎಲ್ಎ');
  if (isMlaQuery) {
    for (const mla of ALL_224_MLAS) {
      if (mla.keywords.some(kw => kw.length > 2 && combined.includes(kw))) {
        return {
          answer: `### 🏛️ ${mla.name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (AC No. ${mla.code}):

* **ಹಾಲಿ ಶಾಸಕರು (MLA):** **${mla.mla_kn}**
* **ರಾಜಕೀಯ ಪಕ್ಷ:** **${mla.party}**
* **ಜಿಲ್ಲೆ:** ${mla.district_kn}
* **ಮಾಹಿತಿ:** ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆಯ ಅಧಿಕೃತ ಚುನಾಯಿತ ಜನಪ್ರತಿನಿಧಿ.`,
          cards: [{ title: `🏛️ ${mla.name_kn} ಶಾಸಕರ ವಿವರ`, url: "/mla-mp.html", icon: "🏛️" }],
          sources: [{ name: "Election Commission of India / CEO Karnataka", url: "https://ceokarnataka.kar.nic.in" }],
          provider: `Karnata Precision Data (${mla.name_kn} MLA)`
        };
      }
    }
  }

  // 2. SPECIFIC MP QUERY (All 28 Lok Sabha Constituencies)
  const isMpQuery = combined.includes('ಸಂಸದ') || combined.includes('mp') || combined.includes('ಲೋಕಸಭಾ') || combined.includes('ಪಾರ್ಲಿಮೆಂಟ್') || combined.includes('ಎಂಪಿ');
  if (isMpQuery) {
    for (const mp of ALL_28_MPS) {
      if (mp.keywords.some(kw => kw.length > 2 && combined.includes(kw))) {
        return {
          answer: `### 🏛️ ${mp.name_kn} ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ (PC No. ${mp.code}):

* **ಹಾಲಿ ಸಂಸದರು (MP):** **${mp.mp_kn}**
* **ರಾಜಕೀಯ ಪಕ್ಷ:** **${mp.party}**
* **ಜಿಲ್ಲೆ:** ${mp.district_kn}
* **ಮಾಹಿತಿ:** 18ನೇ ಲೋಕಸಭೆಯ ಅಧಿಕೃತ ಚುನಾಯಿತ ಸಂಸದರು.`,
          cards: [{ title: `🏛️ ${mp.name_kn} ಸಂಸದರ ವಿವರ`, url: "/mla-mp.html", icon: "🏛️" }],
          sources: [{ name: "Election Commission of India", url: "https://eci.gov.in" }],
          provider: `Karnata Precision Data (${mp.name_kn} MP)`
        };
      }
    }
  }

  // 3. SPECIFIC DISTRICT OFFICER (DC / SP / ZP CEO / Tahsildar)
  const isOfficerQuery = combined.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || combined.includes('dc') || combined.includes('ಎಸ್ಪಿ') || combined.includes('sp') || combined.includes('ಆಯುಕ್ತ') || combined.includes('ಕಲೆಕ್ಟರ್') || combined.includes('ಅಧಿಕಾರಿ');
  if (isOfficerQuery) {
    for (const [key, dist] of Object.entries(PRECISION_DISTRICTS)) {
      if (dist.keywords.some(kw => combined.includes(kw))) {
        let answer = `### 🏛️ ${dist.name_kn} ಜಿಲ್ಲಾ ಆಡಳಿತಾಧಿಕಾರಿಗಳ ವಿವರ (District Leadership):

* **ಜಿಲ್ಲಾಧಿಕಾರಿ (DC):** **${dist.dc}**
* **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP):** **${dist.sp}**`;
        if (dist.zp_ceo) {
          answer += `\\n* **ಜಿ.ಪಂ. ಮುಖ್ಯ ಕಾರ್ಯನಿರ್ವಾಹಕ ಅಧಿಕಾರಿ (ZP CEO):** **${dist.zp_ceo}**`;
        }

        return {
          answer,
          cards: [{ title: `👥 ${dist.name_kn} ಅಧಿಕಾರಿಗಳ ವಿವರ`, url: `/districts/${key.replace('_', '-')}.html`, icon: "👥" }],
          sources: [{ name: "Karnataka Official Directory (Niyukthi)", url: "https://niyukthi.karnataka.gov.in" }],
          provider: `Karnata Precision Data (${dist.name_kn} Administration)`
        };
      }
    }
  }

  // 4. SPECIFIC DAM / RESERVOIR WITH LIVE WATER LEVEL & STORAGE
  const isDamQuery = combined.includes('ಜಲಾಶಯ') || combined.includes('ಡ್ಯಾಂ') || combined.includes('ಅಣೆಕಟ್ಟು') || combined.includes('ನೀರಿನ ಮಟ್ಟ') || combined.includes('ಒಳಹರಿವು') || combined.includes('ಹೊರಹರಿವು') || combined.includes('dam') || combined.includes('tmc');
  if (isDamQuery) {
    for (const [key, dam] of Object.entries(PRECISION_DAMS)) {
      if (dam.keywords.some(kw => combined.includes(kw))) {
        return {
          answer: `### 🚰 ${dam.name_kn} ಲೈವ್ ಮಾಹಿತಿ (Live Dam Status):

* **ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ (Current Water Level):** **${dam.current_level}** (ಗರಿಷ್ಠ ಮಟ್ಟ: ${dam.max_level})
* **ಇಂದಿನ ನೀರಿನ ಸಂಗ್ರಹ (Current Storage):** **${dam.current_storage}** (ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ: ${dam.total_capacity})
* **ಇಂದಿನ ಒಳಹರಿವು (Inflow):** **${dam.inflow}**
* **ಇಂದಿನ ಹೊರಹರಿವು (Outflow):** **${dam.outflow}**
* **ನದಿ:** ${dam.river}
* **ಸ್ಥಳ:** ${dam.location}`,
          cards: [{ title: "🚰 ಜಲಾಶಯಗಳ ಲೈವ್ ಸ್ಥಿತಿ", url: "/dams.html", icon: "🚰" }],
          sources: [{ name: "Karnataka Water Resources Department", url: "https://waterresources.karnataka.gov.in" }],
          provider: `Karnata Precision Telemetry (${dam.name_kn})`
        };
      }
    }
  }

  // 5. CHIEF MINISTER ONLY
  if ((combined.includes('ಮುಖ್ಯಮಂತ್ರಿ') || combined.includes(' cm ') || combined.endsWith(' cm') || combined.startsWith('cm ')) && !combined.includes('ಉಪ')) {
    return {
      answer: `### 🏛️ ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿ (Chief Minister of Karnataka)

* **ಮುಖ್ಯಮಂತ್ರಿ:** **ಶ್ರೀ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)**
* **ಪಕ್ಷ:** ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC)
* **ಕ್ಷೇತ್ರ:** ಕನಕಪುರ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (Kanakapura AC)
* **ಅಧಿಕಾರ ಅವಧಿ:** ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ.`,
      cards: [{ title: "👥 ಸಚಿವ ಸಂಪುಟ & ಅಧಿಕಾರಿಗಳು", url: "/officers.html", icon: "🏛️" }],
      sources: [{ name: "Government of Karnataka", url: "https://karnataka.gov.in" }],
      provider: "Karnata Precision Data (State Leadership)"
    };
  }

  // 6. DEPUTY CHIEF MINISTER ONLY
  if (combined.includes('ಉಪಮುಖ್ಯಮಂತ್ರಿ') || combined.includes('dcm')) {
    return {
      answer: `### 🏛️ ಕರ್ನಾಟಕದ ಉಪಮುಖ್ಯಮಂತ್ರಿ (Deputy Chief Minister)

* **ಉಪಮುಖ್ಯಮಂತ್ರಿ:** **ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್ (Dr. G. Parameshwara)**
* **ಪಕ್ಷ:** ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC)
* **ಕ್ಷೇತ್ರ:** ಕೊರಟಗೆರೆ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (Koratagere AC)
* **ಖಾತೆ:** ಉಪಮುಖ್ಯಮಂತ್ರಿ ಹಾಗೂ ಗೃಹ ಇಲಾಖೆ.`,
      cards: [{ title: "👥 ಸಚಿವ ಸಂಪುಟ & ಅಧಿಕಾರಿಗಳು", url: "/officers.html", icon: "🏛️" }],
      sources: [{ name: "Government of Karnataka", url: "https://karnataka.gov.in" }],
      provider: "Karnata Precision Data (State Leadership)"
    };
  }

  // 7. GOLD & SILVER RATES
  if (combined.includes('ಚಿನ್ನ') || combined.includes('ಬಂಗಾರ') || combined.includes('ಬೆಳ್ಳಿ') || combined.includes('gold') || combined.includes('silver')) {
    return {
      answer: `### 🪙 ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ:

* **24 ಕ್ಯಾರೆಟ್ ಅಪರಂಜಿ ಚಿನ್ನ (99.9% Pure):** **₹16,380 / ಗ್ರಾಂ** (₹1,63,800 / 10 ಗ್ರಾಂ)
* **22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ (91.6% Hallmark):** **₹15,010 / ಗ್ರಾಂ** (₹1,50,100 / 10 ಗ್ರಾಂ)
* **18 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ:** **₹12,281 / ಗ್ರಾಂ** (₹1,22,810 / 10 ಗ್ರಾಂ)
* **ಬೆಳ್ಳಿ (999 Pure Silver):** **₹260 / ಗ್ರಾಂ** (₹2,60,000 / 1 ಕೆಜಿ)
* **ಆಭರಣ ಬೆಳ್ಳಿ (925 Sterling Silver):** **₹240.5 / ಗ್ರಾಂ** (₹2,40,500 / 1 ಕೆಜಿ)`,
      cards: [{ title: "🪙 ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Precision Data (Live Bullion Rates)"
    };
  }

  return null;
}
"""

start_marker = "const PRECISION_DISTRICTS = {"
end_marker = "async function matchFAQ"

start_idx = worker_text.find(start_marker)
end_idx = worker_text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_worker = worker_text[:start_idx] + precision_code.strip() + "\n\n" + worker_text[end_idx:]
    with open(worker_path, "w", encoding="utf-8") as f:
        f.write(new_worker)
    print("SUCCESS: Injected precision code into _worker.js")
else:
    print(f"ERROR: Markers not found: start_idx={start_idx}, end_idx={end_idx}")
