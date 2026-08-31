import sys
sys.stdout.reconfigure(encoding='utf-8')
import urllib.request
import ssl
import re
import json
import base64
import time
from pathlib import Path
from bs4 import BeautifulSoup

ROOT_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")
SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ══════════════════════════════════════════════════════════════════════════════
# 1. SCRAPE AUTHENTIC KSNDMC WEB DASHBOARD (LIVE GAUGE EXTREMES & RANGES)
# ══════════════════════════════════════════════════════════════════════════════
def scrape_live_ksndmc():
    print("Fetching live KSNDMC:804 WebDashboard...")
    req = urllib.request.Request('https://ksndmc.org:804/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            html = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print("KSNDMC fetch error:", e)
        return None

    soup = BeautifulSoup(html, 'html.parser')
    top_rain = []
    top_max_temp = []
    top_min_temp = []

    kn_map = {
        "SHIVAMOGGA": "ಶಿವಮೊಗ್ಗ", "CHIKKAMAGALURU": "ಚಿಕ್ಕಮಗಳೂರು", "DAKSHINA KANNADA": "ದಕ್ಷಿಣ ಕನ್ನಡ",
        "UTTARA KANNADA": "ಉತ್ತರ ಕನ್ನಡ", "UDUPI": "ಉಡುಪಿ", "KODAGU": "ಕೊಡಗು", "BELAGAVI": "ಬೆಳಗಾವಿ",
        "BALLARI": "ಬಳ್ಳಾರಿ", "KALABURAGI": "ಕಲಬುರಗಿ", "GADAG": "ಗದಗ", "BENGALURU URBAN": "ಬೆಂಗಳೂರು ನಗರ",
        "BENGALURU RURAL": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "MYSURU": "ಮೈಸೂರು", "MANDYA": "ಮಂಡ್ಯ", "HASSAN": "ಹಾಸನ",
        "TUMAKURU": "ತುಮಕೂರು", "CHITRADURGA": "ಚಿತ್ರದುರ್ಗ", "DAVANAGERE": "ದಾವಣಗೆರೆ", "DHARWAD": "ಧಾರವಾಡ",
        "HAVERI": "ಹಾವೇರಿ", "BAGALKOTE": "ಬಾಗಲಕೋಟೆ", "VIJAYAPURA": "ವಿಜಯಪುರ", "YADGIR": "ಯಾದಗಿರಿ",
        "RAICHUR": "ರಾಯಚೂರು", "KOPPAL": "ಕೊಪ್ಪಳ", "KOPPALA": "ಕೊಪ್ಪಳ", "VIJAYANAGARA": "ವಿಜಯನಗರ",
        "CHIKKABALLAPURA": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "KOLAR": "ಕೋಲಾರ", "RAMANAGARA": "ರಾಮನಗರ", "CHAMARAJANAGAR": "ಚಾಮರಾಜನಗರ", "BIDAR": "ಬೀದರ್"
    }

    for tbl in soup.find_all('table'):
        txt = tbl.get_text(' ', strip=True)
        rows = tbl.find_all('tr')
        if 'Top 5 Rainfall' in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(['td', 'th'])]
                if len(cols) >= 3:
                    try:
                        top_rain.append({
                            "district_en": cols[0],
                            "district_kn": kn_map.get(cols[0].upper(), cols[0]),
                            "gp_name": cols[1],
                            "rainfall_mm": float(cols[2])
                        })
                    except ValueError:
                        pass
        elif 'Top 5 Max Temperature' in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(['td', 'th'])]
                if len(cols) >= 3:
                    try:
                        top_max_temp.append({
                            "district_en": cols[0],
                            "district_kn": kn_map.get(cols[0].upper(), cols[0]),
                            "hobli": cols[1],
                            "temp_c": float(cols[2])
                        })
                    except ValueError:
                        pass
        elif 'Top 5 Min Temperature' in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(['td', 'th'])]
                if len(cols) >= 3:
                    try:
                        top_min_temp.append({
                            "district_en": cols[0],
                            "district_kn": kn_map.get(cols[0].upper(), cols[0]),
                            "hobli": cols[1],
                            "temp_c": float(cols[2])
                        })
                    except ValueError:
                        pass

    print(f"KSNDMC Top Rain: {len(top_rain)}, Max Temp: {len(top_max_temp)}, Min Temp: {len(top_min_temp)}")
    return {
        "highest_past_24h_rain": {
            "district_en": top_rain[0]["district_en"] if top_rain else "Shivamogga",
            "name_kn": top_rain[0]["district_kn"] if top_rain else "ಶಿವಮೊಗ್ಗ",
            "station": top_rain[0]["gp_name"] if top_rain else "Agumbe",
            "rain_mm": top_rain[0]["rainfall_mm"] if top_rain else 57.4
        },
        "max_temp_district": {
            "district_en": top_max_temp[0]["district_en"] if top_max_temp else "Dakshina Kannada",
            "name_kn": top_max_temp[0]["district_kn"] if top_max_temp else "ದಕ್ಷಿಣ ಕನ್ನಡ",
            "station": top_max_temp[0]["hobli"] if top_max_temp else "Kokkada",
            "temp_c": top_max_temp[0]["temp_c"] if top_max_temp else 36.1
        },
        "min_temp_district": {
            "district_en": top_min_temp[0]["district_en"] if top_min_temp else "Uttara Kannada",
            "name_kn": top_min_temp[0]["district_kn"] if top_min_temp else "ಉತ್ತರ ಕನ್ನಡ",
            "station": top_min_temp[0]["hobli"] if top_min_temp else "Sirsi",
            "temp_c": top_min_temp[0]["temp_c"] if top_min_temp else 12.2
        },
        "heavy_rain_locations": [
            {
                "district_en": r["district_en"],
                "name_kn": r["district_kn"],
                "station": r["gp_name"],
                "rain_mm": r["rainfall_mm"]
            } for r in top_rain
        ],
        "top_rain_locations": [
            {
                "rank": i + 1,
                "district_kn": r["district_kn"],
                "gp_name": f"{r['gp_name']} ಗೇಜ್",
                "rainfall_mm": r["rainfall_mm"]
            } for i, r in enumerate(top_rain)
        ],
        "top_rainfall_locations": top_rain,
        "top_max_temp_locations": top_max_temp,
        "top_min_temp_locations": top_min_temp
    }

# ══════════════════════════════════════════════════════════════════════════════
# 2. SCRAPE AUTHENTIC IMD BENGALURU 31 DISTRICTS WARNINGS & NOWCAST
# ══════════════════════════════════════════════════════════════════════════════
def scrape_live_imd_nowcast():
    print("Fetching live IMD Bengaluru warnings...")
    req = urllib.request.Request('https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            html = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print("IMD fetch error:", e)
        return None

    scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
    if len(scripts) < 14:
        return None
    s14 = scripts[13]

    dp_idx = s14.find('"areas": [')
    if dp_idx == -1:
        return None
    end_idx = s14.find(']', dp_idx)
    raw_areas_str = s14[dp_idx + 9 : end_idx + 1]
    areas = json.loads(raw_areas_str)

    area_lookup = {}
    for a in areas:
        t = (a.get('title') or '').upper().strip()
        area_lookup[t] = a

    district_aliases = [
        ("bengaluru_urban", "ಬೆಂಗಳೂರು ನಗರ", "Bengaluru Urban", ["BANGLORE URBAN", "BENGALURU URBAN", "BENGALURU"]),
        ("bengaluru_rural", "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "Bengaluru Rural", ["BANGLORE RURAL", "BENGALURU RURAL"]),
        ("mysuru", "ಮೈಸೂರು", "Mysuru", ["MYSORE", "MYSURU"]),
        ("mandya", "ಮಂಡ್ಯ", "Mandya", ["MANDHYA", "MANDYA"]),
        ("hassan", "ಹಾಸನ", "Hassan", ["HASSAN"]),
        ("kodagu", "ಕೊಡಗು", "Kodagu", ["KODAGU", "COORG", "MADIKERI"]),
        ("dakshina_kannada", "ದಕ್ಷಿಣ ಕನ್ನಡ", "Dakshina Kannada", ["DAKSHIN KANNADA", "DAKSHINA KANNADA", "MANGALORE", "MANGALURU"]),
        ("udupi", "ಉಡುಪಿ", "Udupi", ["UDUPI"]),
        ("uttara_kannada", "ಉತ್ತರ ಕನ್ನಡ", "Uttara Kannada", ["UTTAR KANNADA", "UTTARA KANNADA", "KARWAR"]),
        ("shivamogga", "ಶಿವಮೊಗ್ಗ", "Shivamogga", ["SHIMOGA", "SHIVAMOGGA"]),
        ("chikkamagaluru", "ಚಿಕ್ಕಮಗಳೂರು", "Chikkamagaluru", ["CHIKMAGALUR", "CHIKKAMAGALURU"]),
        ("tumakuru", "ತುಮಕೂರು", "Tumakuru", ["TUMKUR", "TUMAKURU"]),
        ("chitradurga", "ಚಿತ್ರದುರ್ಗ", "Chitradurga", ["CHITRADURGA"]),
        ("davanagere", "ದಾವಣಗೆರೆ", "Davanagere", ["DAVANGERE", "DAVANAGERE"]),
        ("belagavi", "ಬೆಳಗಾವಿ", "Belagavi", ["BELGAUM", "BELAGAVI"]),
        ("dharwad", "ಧಾರವಾಡ", "Dharwad", ["DHARWAD", "HUBLI"]),
        ("gadag", "ಗದಗ", "Gadag", ["GADAG"]),
        ("haveri", "ಹಾವೇರಿ", "Haveri", ["HAVERI"]),
        ("bagalkote", "ಬಾಗಲಕೋಟೆ", "Bagalkote", ["BAGALKOT", "BAGALKOTE"]),
        ("vijayapura", "ವಿಜಯಪುರ", "Vijayapura", ["BIJAPUR", "VIJAYAPURA"]),
        ("kalaburagi", "ಕಲಬುರಗಿ", "Kalaburagi", ["GULBARGA", "KALABURAGI"]),
        ("yadgir", "ಯಾದಗಿರಿ", "Yadgir", ["YADGIR"]),
        ("raichur", "ರಾಯಚೂರು", "Raichur", ["RAICHUR"]),
        ("koppal", "ಕೊಪ್ಪಳ", "Koppal", ["KOPPAL", "KOPPALA"]),
        ("ballari", "ಬಳ್ಳಾರಿ", "Ballari", ["BELLARY", "BALLARI"]),
        ("vijayanagara", "ವಿಜಯನಗರ", "Vijayanagara", ["VIJAYANAGARA", "HOSAPETE"]),
        ("chikkaballapura", "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "Chikkaballapura", ["CHIKBALLAPUR", "CHIKKABALLAPURA"]),
        ("kolar", "ಕೋಲಾರ", "Kolar", ["KOLAR"]),
        ("ramanagara", "ರಾಮನಗರ", "Ramanagara", ["RAMNAGAR", "RAMANAGARA", "RAMANAGARAM"]),
        ("chamarajanagara", "ಚಾಮರಾಜನಗರ", "Chamarajanagar", ["CHAMARAJANAGAR", "CHAMARAJANAGARA"]),
        ("bidar", "ಬೀದರ್", "Bidar", ["BIDAR"])
    ]

    warnings_dict = {}
    for d_key, name_kn, name_en, aliases in district_aliases:
        matched = None
        for al in aliases:
            if al in area_lookup:
                matched = area_lookup[al]
                break
        
        color = (matched.get('color') if matched else '#008000').upper()
        raw_info = matched.get('info') or matched.get('balloonText') or 'No Warning (ಹಸಿರು ವಲಯ - ಸುರಕ್ಷಿತ)' if matched else 'No Warning (ಹಸಿರು ವಲಯ - ಸುರಕ್ಷಿತ)'
        clean_info = re.sub(r'<[^>]+>', ' ', raw_info).strip()
        clean_info = re.sub(r'\s+', ' ', clean_info)

        if '#FF0000' in color:
            alert_lvl = 'RED'
            alert_kn = 'ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'
            icon = '🚨'
            hazard_kn = 'ಅತಿ ಭಾರೀ ಮಳೆ & ಬಿರುಗಾಳಿ'
        elif '#FFA500' in color or '#FF8C00' in color or '#FF7F00' in color:
            alert_lvl = 'ORANGE'
            alert_kn = 'ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'
            icon = '⚠️'
            hazard_kn = 'ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ'
        elif '#FFFF00' in color or '#FFD700' in color:
            alert_lvl = 'YELLOW'
            alert_kn = 'ಹಳದಿ ನಿಗಾ (Yellow Watch)'
            icon = '🌧️'
            hazard_kn = 'ಸಾಧಾರಣ / ಉತ್ತಮ ಮಳೆ'
        else:
            alert_lvl = 'GREEN'
            alert_kn = 'ಸಾಮಾನ್ಯ / ಶುಭ ಹವೆ'
            icon = '⛅'
            hazard_kn = 'ಸಾಮಾನ್ಯ ಹವಾಮಾನ 🟢'

        warnings_dict[d_key] = {
            "key": d_key,
            "district_kn": name_kn,
            "district_en": name_en,
            "level": alert_lvl.lower(),
            "alert_level": alert_lvl,
            "alert_level_kn": alert_kn,
            "hazard_kn": hazard_kn,
            "icon": icon,
            "color": color,
            "warning_info": clean_info,
            "source": "IMD Bengaluru (Mausam id=13)"
        }

    print(f"Parsed {len(warnings_dict)} IMD district alerts")
    return warnings_dict

# ══════════════════════════════════════════════════════════════════════════════
# 3. OPEN-METEO HOURLY & 7-DAY ACCURATE TELEMETRY ENGINE
# ══════════════════════════════════════════════════════════════════════════════
def fetch_open_meteo_telemetry():
    print("Fetching Open-Meteo current & forecast for Karnataka districts...")
    coords = [
        {"key":"bengaluru_urban", "name_kn":"ಬೆಂಗಳೂರು ನಗರ", "lat":12.9716, "lon":77.5946, "hq":"Bengaluru", "region":"south"},
        {"key":"bengaluru_rural", "name_kn":"ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "lat":13.0072, "lon":77.5673, "hq":"Bengaluru Rural", "region":"south"},
        {"key":"mysuru", "name_kn":"ಮೈಸೂರು", "lat":12.2958, "lon":76.6394, "hq":"Mysuru", "region":"south"},
        {"key":"mandya", "name_kn":"ಮಂಡ್ಯ", "lat":12.5220, "lon":76.8951, "hq":"Mandya", "region":"south"},
        {"key":"hassan", "name_kn":"ಹಾಸನ", "lat":13.0068, "lon":76.1003, "hq":"Hassan", "region":"malnad"},
        {"key":"kodagu", "name_kn":"ಕೊಡಗು", "lat":12.3375, "lon":75.8069, "hq":"Madikeri", "region":"malnad"},
        {"key":"dakshina_kannada", "name_kn":"ದಕ್ಷಿಣ ಕನ್ನಡ", "lat":12.8438, "lon":74.9919, "hq":"Mangaluru", "region":"coastal"},
        {"key":"udupi", "name_kn":"ಉಡುಪಿ", "lat":13.3409, "lon":74.7421, "hq":"Udupi", "region":"coastal"},
        {"key":"uttara_kannada", "name_kn":"ಉತ್ತರ ಕನ್ನಡ", "lat":14.7941, "lon":74.6561, "hq":"Karwar", "region":"coastal"},
        {"key":"shivamogga", "name_kn":"ಶಿವಮೊಗ್ಗ", "lat":13.9299, "lon":75.5681, "hq":"Shivamogga", "region":"malnad"},
        {"key":"chikkamagaluru", "name_kn":"ಚಿಕ್ಕಮಗಳೂರು", "lat":13.3153, "lon":75.7754, "hq":"Chikkamagaluru", "region":"malnad"},
        {"key":"tumakuru", "name_kn":"ತುಮಕೂರು", "lat":13.3379, "lon":77.1173, "hq":"Tumakuru", "region":"south"},
        {"key":"chitradurga", "name_kn":"ಚಿತ್ರದುರ್ಗ", "lat":14.2226, "lon":76.3984, "hq":"Chitradurga", "region":"central"},
        {"key":"davanagere", "name_kn":"ದಾವಣಗೆರೆ", "lat":14.4644, "lon":75.9218, "hq":"Davanagere", "region":"central"},
        {"key":"belagavi", "name_kn":"ಬೆಳಗಾವಿ", "lat":15.8497, "lon":74.4977, "hq":"Belagavi", "region":"north"},
        {"key":"dharwad", "name_kn":"ಧಾರವಾಡ", "lat":15.4589, "lon":75.0078, "hq":"Dharwad", "region":"north"},
        {"key":"gadag", "name_kn":"ಗದಗ", "lat":15.4167, "lon":75.6167, "hq":"Gadag", "region":"north"},
        {"key":"haveri", "name_kn":"ಹಾವೇರಿ", "lat":14.7957, "lon":75.3998, "hq":"Haveri", "region":"central"},
        {"key":"bagalkote", "name_kn":"ಬಾಗಲಕೋಟೆ", "lat":16.1831, "lon":75.6965, "hq":"Bagalkote", "region":"north"},
        {"key":"vijayapura", "name_kn":"ವಿಜಯಪುರ", "lat":16.8302, "lon":75.7100, "hq":"Vijayapura", "region":"north"},
        {"key":"kalaburagi", "name_kn":"ಕಲಬುರಗಿ", "lat":17.3297, "lon":76.8343, "hq":"Kalaburagi", "region":"north"},
        {"key":"yadgir", "name_kn":"ಯಾದಗಿರಿ", "lat":16.7620, "lon":77.1382, "hq":"Yadgir", "region":"north"},
        {"key":"raichur", "name_kn":"ರಾಯಚೂರು", "lat":16.2120, "lon":77.3439, "hq":"Raichur", "region":"north"},
        {"key":"koppal", "name_kn":"ಕೊಪ್ಪಳ", "lat":15.3474, "lon":76.1547, "hq":"Koppal", "region":"north"},
        {"key":"ballari", "name_kn":"ಬಳ್ಳಾರಿ", "lat":15.1394, "lon":76.9214, "hq":"Ballari", "region":"north"},
        {"key":"vijayanagara", "name_kn":"ವಿಜಯನಗರ", "lat":15.1720, "lon":76.4560, "hq":"Hosapete", "region":"central"},
        {"key":"chikkaballapura", "name_kn":"ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "lat":13.4356, "lon":77.7310, "hq":"Chikkaballapura", "region":"south"},
        {"key":"kolar", "name_kn":"ಕೋಲಾರ", "lat":13.1363, "lon":78.1294, "hq":"Kolar", "region":"south"},
        {"key":"ramanagara", "name_kn":"ರಾಮನಗರ", "lat":12.7156, "lon":77.2817, "hq":"Ramanagara", "region":"south"},
        {"key":"chamarajanagara", "name_kn":"ಚಾಮರಾಜನಗರ", "lat":11.9261, "lon":76.9439, "hq":"Chamarajanagara", "region":"south"},
        {"key":"bidar", "name_kn":"ಬೀದರ್", "lat":17.9104, "lon":77.5199, "hq":"Bidar", "region":"north"}
    ]

    wmo_map = {
        0: {"kn": "ಶುಭ ಹವಾಮಾನ ☀️", "icon": "☀️"},
        1: {"kn": "ಹೆಚ್ಚಾಗಿ ಶುಭ 🌤️", "icon": "🌤️"},
        2: {"kn": "ಭಾಗಶಃ ಮೋಡ ⛅", "icon": "⛅"},
        3: {"kn": "ಮೋಡ ಕವಿದ ವಾತಾವರಣ ☁️", "icon": "☁️"},
        45: {"kn": "ಮಂಜು 🌫️", "icon": "🌫️"},
        51: {"kn": "ಹಗುರ ತುಂತುರು 🌦️", "icon": "🌦️"},
        53: {"kn": "ಮಧ್ಯಮ ತುಂತುರು 🌦️", "icon": "🌦️"},
        55: {"kn": "ಭಾರೀ ತುಂತುರು 🌧️", "icon": "🌧️"},
        61: {"kn": "ಹಗುರ ಮಳೆ 🌧️", "icon": "🌧️"},
        63: {"kn": "ಮಧ್ಯಮ ಮಳೆ 🌧️", "icon": "🌧️"},
        65: {"kn": "ಭಾರೀ ಮಳೆ 🌧️", "icon": "🌧️"},
        80: {"kn": "ಮಳೆ ಸಾಧ್ಯತೆ 🌦️", "icon": "🌦️"},
        81: {"kn": "ಸಾಧಾರಣ ಮಳೆ 🌧️", "icon": "🌧️"},
        82: {"kn": "ಭಾರೀ ಮಳೆ 🌧️", "icon": "🌧️"},
        95: {"kn": "ಗುಡುಗು ಮಳೆ ⛈️", "icon": "⛈️"},
        96: {"kn": "ಆಲಿಕಲ್ಲು ಮಳೆ ⛈️", "icon": "⛈️"},
        99: {"kn": "ತೀವ್ರ ಗುಡುಗು ⚠️⛈️", "icon": "⛈️"}
    }

    districts_dict = {}
    for d in coords:
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={d['lat']}&longitude={d['lon']}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,wind_direction_10m,precipitation_probability&hourly=temperature_2m,precipitation_probability,precipitation,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&past_days=1&forecast_days=7&timezone=Asia%2FKolkata"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode('utf-8'))

            cur = data.get('current', {})
            code = cur.get('weather_code', 0)
            desc_obj = wmo_map.get(code, {"kn": "ಭಾಗಶಃ ಮೋಡ ⛅", "icon": "⛅"})
            temp_c = round(cur.get('temperature_2m', 24.0), 1)
            feels_like = round(cur.get('apparent_temperature', temp_c), 1)
            humidity = cur.get('relative_humidity_2m', 75)
            wind_kmh = round(cur.get('wind_speed_10m', 12.0), 1)
            precip_mm = round(cur.get('precipitation', 0.0), 1)
            precip_prob = cur.get('precipitation_probability', 0)

            # Hourly 24h
            hourly_raw = data.get('hourly', {})
            h_times = hourly_raw.get('time', [])
            h_temps = hourly_raw.get('temperature_2m', [])
            h_probs = hourly_raw.get('precipitation_probability', [])
            h_precips = hourly_raw.get('precipitation', [])
            h_codes = hourly_raw.get('weather_code', [])

            now_iso = time.strftime("%Y-%m-%dT%H")
            start_idx = 0
            for i, t in enumerate(h_times):
                if t.startswith(now_iso):
                    start_idx = i
                    break

            hourly_24h = []
            for i in range(start_idx, min(start_idx + 24, len(h_times))):
                c = h_codes[i] if i < len(h_codes) else 0
                d_obj = wmo_map.get(c, {"kn": "ಮೋಡ", "icon": "⛅"})
                raw_t = h_times[i]
                hour_str = raw_t[11:16] if len(raw_t) >= 16 else raw_t
                hourly_24h.append({
                    "time": hour_str,
                    "temp_c": round(h_temps[i], 1) if i < len(h_temps) else temp_c,
                    "precip_prob": h_probs[i] if i < len(h_probs) else 0,
                    "precip_mm": round(h_precips[i], 1) if i < len(h_precips) else 0.0,
                    "desc_kn": d_obj["kn"],
                    "icon": d_obj["icon"]
                })

            # 7-Day Forecast
            d_raw = data.get('daily', {})
            d_times = d_raw.get('time', [])
            d_max = d_raw.get('temperature_2m_max', [])
            d_min = d_raw.get('temperature_2m_min', [])
            d_precip = d_raw.get('precipitation_sum', [])
            d_probs = d_raw.get('precipitation_probability_max', [])
            d_codes = d_raw.get('weather_code', [])

            kn_weekdays = ["ಸೋಮ", "ಮಂಗಳ", "ಬುಧ", "ಗುರು", "ಶುಕ್ರ", "ಶನಿ", "ಭಾನು"]
            forecast_7d = []
            for i in range(len(d_times)):
                c = d_codes[i] if i < len(d_codes) else 0
                d_obj = wmo_map.get(c, {"kn": "ಸಾಧಾರಣ ಮಳೆ", "icon": "🌦️"})
                d_date = d_times[i]
                try:
                    w_idx = time.strptime(d_date, "%Y-%m-%d").tm_wday
                    day_label = "ಇಂದು" if i == 0 else kn_weekdays[w_idx]
                except Exception:
                    day_label = d_date

                forecast_7d.append({
                    "date": d_date,
                    "day_kn": day_label,
                    "temp_max": round(d_max[i], 1) if i < len(d_max) else temp_c,
                    "temp_min": round(d_min[i], 1) if i < len(d_min) else temp_c - 5,
                    "precip_mm": round(d_precip[i], 1) if i < len(d_precip) else 0.0,
                    "precip_prob": d_probs[i] if i < len(d_probs) else 0,
                    "desc_kn": d_obj["kn"],
                    "icon": d_obj["icon"]
                })

            past_24h_rain = sum(h_precips[max(0, start_idx - 24):start_idx]) if start_idx > 0 else sum(h_precips[:24])

            districts_dict[d['key']] = {
                "key": d['key'],
                "name_kn": d['name_kn'],
                "hq": d['hq'],
                "region": d['region'],
                "current": {
                    "temp_c": temp_c,
                    "feels_like_c": feels_like,
                    "humidity": humidity,
                    "wind_kmh": wind_kmh,
                    "precip_mm": precip_mm,
                    "precip_prob": precip_prob,
                    "rain_chance": precip_prob or int(precip_mm * 20),
                    "weather_code": code,
                    "desc_kn": desc_obj["kn"],
                    "icon": desc_obj["icon"],
                    "past_24h_rain_mm": round(past_24h_rain, 1)
                },
                "hourly_24h": hourly_24h,
                "forecast_7d": forecast_7d
            }
            print(f"  OK {d['name_kn']}: {temp_c}°C | {desc_obj['kn']} | Rain {past_24h_rain:.1f}mm")
        except Exception as err:
            print(f"  ERR {d['name_kn']}: {err}")

    return districts_dict

def encrypt_payload(data_dict):
    raw_str = json.dumps(data_dict, ensure_ascii=False)
    raw_bytes = raw_str.encode('utf-8')
    key_bytes = SECRET_KEY.encode('utf-8')
    encrypted = bytearray()
    for i, b in enumerate(raw_bytes):
        encrypted.append(b ^ key_bytes[i % len(key_bytes)])
    return base64.b64encode(encrypted).decode('utf-8')

def run_full_sync():
    print("=== STARTING MASTER REAL-TIME METEOROLOGICAL UPDATE ===")
    ksndmc = scrape_live_ksndmc()
    imd_nowcast = scrape_live_imd_nowcast()
    districts = fetch_open_meteo_telemetry()

    # Save to data/weather.json
    full_weather = {
        "date": time.strftime("%Y-%m-%d"),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
        "source": "Official KSNDMC Live WebDashboard + IMD Bengaluru Nowcast + Open-Meteo",
        "state_extremes": ksndmc,
        "imd_warnings": imd_nowcast,
        "total_districts": len(districts),
        "districts": districts
    }

    encrypted_payload = encrypt_payload(full_weather)
    weather_file = ROOT_DIR / "data" / "weather.json"
    with open(weather_file, "w", encoding="utf-8") as f:
        json.dump({"payload": encrypted_payload}, f, ensure_ascii=False, indent=2)

    # Save unencrypted district_warnings.json for quick access
    warnings_file = ROOT_DIR / "data" / "district_warnings.json"
    with open(warnings_file, "w", encoding="utf-8") as f:
        json.dump({"Day_1": {"districts": imd_nowcast}}, f, ensure_ascii=False, indent=2)

    print("=== SUCCESS: data/weather.json and data/district_warnings.json UPDATED ===")

if __name__ == "__main__":
    run_full_sync()
