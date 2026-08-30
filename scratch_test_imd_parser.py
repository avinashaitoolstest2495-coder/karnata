import requests, json, re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

url = 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False, timeout=15)

karnataka_districts_map = {
    "BENGALURU URBAN": {"kn": "ಬೆಂಗಳೂರು ನಗರ", "key": "bengaluru_urban"},
    "BENGALURU RURAL": {"kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "key": "bengaluru_rural"},
    "MYSURU": {"kn": "ಮೈಸೂರು", "key": "mysuru"},
    "MANDYA": {"kn": "ಮಂಡ್ಯ", "key": "mandya"},
    "HASSAN": {"kn": "ಹಾಸನ", "key": "hassan"},
    "KODAGU": {"kn": "ಕೊಡಗು", "key": "kodagu"},
    "DAKSHINA KANNADA": {"kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "key": "dakshina_kannada"},
    "UDUPI": {"kn": "ಉಡುಪಿ", "key": "udupi"},
    "UTTARA KANNADA": {"kn": "ಉತ್ತರ ಕನ್ನಡ", "key": "uttara_kannada"},
    "SHIVAMOGGA": {"kn": "ಶಿವಮೊಗ್ಗ", "key": "shivamogga"},
    "CHIKKAMAGALURU": {"kn": "ಚಿಕ್ಕಮಗಳೂರು", "key": "chikkamagaluru"},
    "TUMAKURU": {"kn": "ತುಮಕೂರು", "key": "tumakuru"},
    "CHITRADURGA": {"kn": "ಚಿತ್ರದುರ್ಗ", "key": "chitradurga"},
    "DAVANAGERE": {"kn": "ದಾವಣಗೆರೆ", "key": "davanagere"},
    "BELAGAVI": {"kn": "ಬೆಳಗಾವಿ", "key": "belagavi"},
    "DHARWAD": {"kn": "ಧಾರವಾಡ", "key": "dharwad"},
    "GADAG": {"kn": "ಗದಗ", "key": "gadag"},
    "HAVERI": {"kn": "ಹಾವೇರಿ", "key": "haveri"},
    "BAGALKOTE": {"kn": "ಬಾಗಲಕೋಟೆ", "key": "bagalkote"},
    "VIJAYAPURA": {"kn": "ವಿಜಯಪುರ", "key": "vijayapura"},
    "KALABURAGI": {"kn": "ಕಲಬುರಗಿ", "key": "kalaburagi"},
    "YADGIR": {"kn": "ಯಾದಗಿರಿ", "key": "yadgir"},
    "RAICHUR": {"kn": "ರಾಯಚೂರು", "key": "raichur"},
    "KOPPAL": {"kn": "ಕೊಪ್ಪಳ", "key": "koppal"},
    "BALLARI": {"kn": "ಬಳ್ಳಾರಿ", "key": "ballari"},
    "VIJAYANAGARA": {"kn": "ವಿಜಯನಗರ", "key": "vijayanagara"},
    "CHIKKABALLAPURA": {"kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "key": "chikkaballapura"},
    "KOLAR": {"kn": "ಕೋಲಾರ", "key": "kolar"},
    "RAMANAGARA": {"kn": "ರಾಮನಗರ", "key": "ramanagara"},
    "CHAMARAJANAGAR": {"kn": "ಚಾಮರಾಜನಗರ", "key": "chamarajanagar"}
}

areas_idx = res.text.find('"areas": [')
if areas_idx != -1:
    end_idx = res.text.find(']', areas_idx)
    raw_areas_json = res.text[areas_idx+9:end_idx+1]
    areas = json.loads(raw_areas_json)
    print(f"Parsed {len(areas)} total areas from IMD.")

    parsed_karnataka = {}
    for a in areas:
        title = (a.get('title') or '').upper().strip()
        info_html = a.get('info', '')
        color = a.get('color', '#00FF00').upper()

        # Determine alert level
        alert_level = "GREEN"
        alert_level_kn = "ಹಸಿರು (ಸುರಕ್ಷಿತ)"
        if "#FF0000" in color:
            alert_level = "RED"
            alert_level_kn = "ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)"
        elif "#FFA500" in color or "#FF8C00" in color or "#FF7F00" in color:
            alert_level = "ORANGE"
            alert_level_kn = "ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)"
        elif "#FFFF00" in color or "#FFD700" in color:
            alert_level = "YELLOW"
            alert_level_kn = "ಹಳದಿ ಎಚ್ಚರಿಕೆ (Yellow Watch)"

        clean_info = re.sub(r'<[^>]+>', ' ', info_html).strip()

        for kd_en, kd_meta in karnataka_districts_map.items():
            if kd_en in title or title in kd_en:
                parsed_karnataka[kd_meta["key"]] = {
                    "district_en": kd_en,
                    "district_kn": kd_meta["kn"],
                    "district_key": kd_meta["key"],
                    "alert_level": alert_level,
                    "alert_level_kn": alert_level_kn,
                    "color": color,
                    "info_raw": clean_info,
                    "valid_time": clean_info.split('Valid upto:')[-1].strip() if 'Valid upto:' in clean_info else 'ಇಂದಿನ ಮುನ್ಸೂಚನೆ'
                }
                break

    print(f"Extracted {len(parsed_karnataka)} Karnataka districts:")
    for k, v in list(parsed_karnataka.items())[:5]:
        print(f"  {v['district_kn']}: {v['alert_level_kn']} -> {v['info_raw'][:70]}")
