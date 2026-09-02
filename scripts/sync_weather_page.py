import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, base64, re, time
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup

ROOT_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")
SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

DISTRICT_REGIONS = {
    'bengaluru_urban': 'south', 'bengaluru_rural': 'south', 'ramanagara': 'south', 'kolar': 'south',
    'chikkaballapura': 'south', 'mandya': 'south', 'mysuru': 'south', 'chamarajanagara': 'south',
    'tumakuru': 'south', 'dakshina_kannada': 'coastal', 'udupi': 'coastal', 'uttara_kannada': 'coastal',
    'kodagu': 'malnad', 'hassan': 'malnad', 'chikkamagaluru': 'malnad', 'shivamogga': 'malnad',
    'chitradurga': 'central', 'davanagere': 'central', 'haveri': 'central', 'ballari': 'central',
    'vijayanagara': 'central', 'belagavi': 'north', 'dharwad': 'north', 'gadag': 'north',
    'bagalkote': 'north', 'vijayapura': 'north', 'koppal': 'north', 'raichur': 'north',
    'kalaburagi': 'north', 'yadgir': 'north', 'bidar': 'north'
}

REGION_NAMES_KN = {
    'coastal': 'ಕರಾವಳಿ', 'malnad': 'ಮಲೆನಾಡು', 'south': 'ದಕ್ಷಿಣ ಒಳನಾಡು',
    'central': 'ಮಧ್ಯ ಕರ್ನಾಟಕ', 'north': 'ಉತ್ತರ ಒಳನಾಡು'
}

def decrypt_payload(raw_json):
    if isinstance(raw_json, dict) and "payload" in raw_json:
        payload_b64 = raw_json["payload"]
        raw_bytes = base64.b64decode(payload_b64)
        key_bytes = SECRET_KEY.encode('utf-8')
        decrypted = bytearray()
        for i, b in enumerate(raw_bytes):
            decrypted.append(b ^ key_bytes[i % len(key_bytes)])
        return json.loads(decrypted.decode('utf-8'))
    return raw_json

def sync_weather():
    print("=== SYNCING LATEST WEATHER DATA INTO WEATHER.HTML & GEO PUSH ALERTS ===")
    weather_file = ROOT_DIR / "data" / "weather.json"
    if not weather_file.exists():
        print("[ERROR] data/weather.json not found!")
        return

    weather_data = decrypt_payload(json.load(open(weather_file, 'r', encoding='utf-8')))
    nowcast_dists = weather_data.get('nowcast', {}).get('districts', {})
    forecast_5d = weather_data.get('forecast_5days', {})
    districts = weather_data.get('districts', {})
    bengaluru = districts.get('bengaluru_urban', list(districts.values())[0])

    # 1. Build master_d5
    master_d5 = {}
    nc_dist_dict = {}
    nc_summary = {"red": 0, "orange": 0, "yellow": 0, "green": 0, "total_alerts": 0}
    geo_weather_alerts = []

    for k, d in nowcast_dists.items():
        region = DISTRICT_REGIONS.get(k, 'south')
        lvl = (d.get('alert_level') or d.get('level') or 'green').lower()
        d_name_kn = d.get('district_kn') or d.get('name_kn') or k
        d_name_en = d.get('district_en') or d.get('name_en') or ''
        raw_wi = d.get('warning_info', '')

        if lvl == 'red':
            nc_summary['red'] += 1
            level_label = '🔴 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'
            hazard = d.get('hazard_kn') or 'ಅತಿ ಭಾರೀ ಮಳೆ & ಬಿರುಗಾಳಿ'
            advice = d.get('warning_info') or 'ತಕ್ಷಣದ ಸುರಕ್ಷತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
            accent = '#E11D48'; bg = '#FFF1F2'
            # Geo Push Notification for Red Alert
            geo_weather_alerts.append({
                "id": f"WEATHER-RED-{k}-{datetime.now().strftime('%Y%m%d%H')}",
                "alert_level": "red",
                "target_district": k,
                "target_district_kn": d_name_kn,
                "title": f"🔴 ಕೆಂಪು ಕಟ್ಟೆಚ್ಚರ (Red Alert) — {d_name_kn}",
                "body": f"IMD ತುರ್ತು ಎಚ್ಚರಿಕೆ: {d_name_kn} ಜಿಲ್ಲೆಯಲ್ಲಿ ಅತಿ ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ! ತಕ್ಷಣದ ಸುರಕ್ಷತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ.",
                "url": f"https://karnata.in/weather?district={k}",
                "icon": "https://karnata.in/assets/icons/icon-512x512.png",
                "topic": "weather_alert",
                "created_at": datetime.now().isoformat()
            })
        elif lvl == 'orange':
            nc_summary['orange'] += 1
            level_label = '🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'
            hazard = d.get('hazard_kn') or 'ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ'
            advice = d.get('warning_info') or 'ಮುಂಜಾಗ್ರತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
            accent = '#D97706'; bg = '#FFFBEB'
            # Geo Push Notification for Orange Alert
            geo_weather_alerts.append({
                "id": f"WEATHER-ORANGE-{k}-{datetime.now().strftime('%Y%m%d%H')}",
                "alert_level": "orange",
                "target_district": k,
                "target_district_kn": d_name_kn,
                "title": f"🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert) — {d_name_kn}",
                "body": f"IMD ಅಧಿಕೃತ ಎಚ್ಚರಿಕೆ: {d_name_kn} ಜಿಲ್ಲೆಯಲ್ಲಿ ಭಾರೀ ಮಳೆ ಹಾಗೂ ಬಿರುಗಾಳಿ ಸಾಧ್ಯತೆ. ಸುರಕ್ಷಿತವಾಗಿರಿ.",
                "url": f"https://karnata.in/weather?district={k}",
                "icon": "https://karnata.in/assets/icons/icon-512x512.png",
                "topic": "weather_alert",
                "created_at": datetime.now().isoformat()
            })
        elif lvl == 'yellow':
            nc_summary['yellow'] += 1
            level_label = '🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)'
            hazard = 'ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️'
            if 'Valid upto:' in raw_wi:
                v_time = raw_wi.split('Valid upto:').pop().strip()
                advice = f"ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: {v_time})"
            else:
                advice = 'ತುಂತುರು ಅಥವಾ ಸಾಧಾರಣ ಮಳೆ ಸಾಧ್ಯತೆ'
            accent = '#CA8A04'; bg = '#FEFCE8'
            # Geo Push Notification for Yellow Alert
            geo_weather_alerts.append({
                "id": f"WEATHER-YELLOW-{k}-{datetime.now().strftime('%Y%m%d%H')}",
                "alert_level": "yellow",
                "target_district": k,
                "target_district_kn": d_name_kn,
                "title": f"🟡 ಹಳದಿ ಮುನ್ನೆಚ್ಚರಿಕೆ (Yellow Watch) — {d_name_kn}",
                "body": f"IMD ಲೈವ್ ನೌಕಾಸ್ಟ್: {d_name_kn} ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಲಘು / ಸಾಧಾರಣ ಮಳೆ ಸಾಧ್ಯತೆ ({advice}).",
                "url": f"https://karnata.in/weather?district={k}",
                "icon": "https://karnata.in/assets/icons/icon-512x512.png",
                "topic": "weather_alert",
                "created_at": datetime.now().isoformat()
            })
        else:
            nc_summary['green'] += 1
            level_label = '🟢 ಸಾಮಾನ್ಯ (No Warning)'
            hazard = 'ಶಾಂತ ವಾತಾವರಣ 🌤️'
            advice = 'ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ'
            accent = '#16A34A'; bg = '#F0FDF4'

        nc_dist_dict[k] = {
            "district_key": k,
            "name_kn": d_name_kn,
            "name_en": d_name_en,
            "region": region,
            "level": lvl,
            "level_label_kn": level_label,
            "accent_color": accent,
            "bg_color": bg,
            "raw_warning": raw_wi,
            "hazard_kn": hazard,
            "advice_kn": advice
        }

    nc_summary['total_alerts'] = nc_summary['red'] + nc_summary['orange'] + nc_summary['yellow']
    master_d5['Nowcast'] = {
        "day_code": "Nowcast",
        "tab_label_kn": "⚡ 3-ಗಂಟೆ ಲೈವ್ ನೌಕಾಸ್ಟ್",
        "summary": nc_summary,
        "districts": nc_dist_dict
    }

    # Also check 5-day forecast Day 1 alerts and add if any orange/red
    day1_raw = forecast_5d.get('Day_1', {}).get('districts', {})
    for k, d in day1_raw.items():
        lvl = (d.get('alert_level') or d.get('level') or 'green').lower()
        if lvl in ['orange', 'red']:
            d_name_kn = d.get('district_kn') or d.get('name_kn') or k
            existing = [a for a in geo_weather_alerts if a['target_district'] == k]
            if not existing:
                geo_weather_alerts.append({
                    "id": f"FORECAST-{lvl.upper()}-{k}-{datetime.now().strftime('%Y%m%d')}",
                    "alert_level": lvl,
                    "target_district": k,
                    "target_district_kn": d_name_kn,
                    "title": f"🚨 {lvl.upper()} ALERT — {d_name_kn}",
                    "body": f"IMD ಅಧಿಕೃತ 24-ಗಂಟೆ ಮುನ್ಸೂಚನೆ: {d_name_kn} ಜಿಲ್ಲೆಯಲ್ಲಿ ಭಾರೀ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ.",
                    "url": f"https://karnata.in/weather?district={k}",
                    "icon": "https://karnata.in/assets/icons/icon-512x512.png",
                    "topic": "weather_alert",
                    "created_at": datetime.now().isoformat()
                })

    # Save live_push_feed.json for instant client fetching and edge sync
    push_feed_obj = {
        "updated_at": datetime.now().isoformat(),
        "total_active_alerts": len(geo_weather_alerts),
        "feed": geo_weather_alerts
    }
    feed_path = ROOT_DIR / "data" / "live_push_feed.json"
    feed_path.write_text(json.dumps(push_feed_obj, ensure_ascii=False, indent=2), encoding='utf-8')
    
    nk_feed_path = ROOT_DIR / "namma-karnataka" / "data" / "live_push_feed.json"
    if nk_feed_path.parent.exists():
        nk_feed_path.write_text(json.dumps(push_feed_obj, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Generated {len(geo_weather_alerts)} geo-targeted weather push alerts into data/live_push_feed.json!")

    # Build Day_1 to Day_5
    day_kn_labels = {
        'Day_1': '📅 ಇಂದು (Day 1)',
        'Day_2': '📅 ನಾಳೆ (Day 2)',
        'Day_3': '📅 ದಿನ 3 (Day 3)',
        'Day_4': '📅 ದಿನ 4 (Day 4)',
        'Day_5': '📅 ದಿನ 5 (Day 5)'
    }

    for d_code in ['Day_1', 'Day_2', 'Day_3', 'Day_4', 'Day_5']:
        day_raw = forecast_5d.get(d_code, {}).get('districts', {})
        d_summary = {"red": 0, "orange": 0, "yellow": 0, "green": 0, "total_alerts": 0}
        d_dict = {}

        for k in DISTRICT_REGIONS.keys():
            d = day_raw.get(k, {})
            region = DISTRICT_REGIONS[k]
            lvl = (d.get('alert_level') or d.get('level') or 'green').lower()

            if lvl == 'red':
                d_summary['red'] += 1
                level_label = '🔴 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'
                hazard = d.get('hazard_kn') or 'ಅತಿ ಭಾರೀ ಮಳೆ'
                advice = 'ಮುಂಜಾಗ್ರತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
                accent = '#E11D48'; bg = '#FFF1F2'
            elif lvl == 'orange':
                d_summary['orange'] += 1
                level_label = '🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'
                hazard = d.get('hazard_kn') or 'ಭಾರೀ ಮಳೆ'
                advice = 'ಮುಂಜಾಗ್ರತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
                accent = '#D97706'; bg = '#FFFBEB'
            elif lvl == 'yellow':
                d_summary['yellow'] += 1
                level_label = '🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)'
                hazard = d.get('hazard_kn') or 'ಸಾಧಾರಣ ಮಳೆ'
                advice = 'ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಗಮನಿಸಿ'
                accent = '#CA8A04'; bg = '#FEFCE8'
            else:
                d_summary['green'] += 1
                level_label = '🟢 ಸಾಮಾನ್ಯ (No Warning)'
                hazard = 'ಶಾಂತ ವಾತಾವರಣ 🌤️'
                advice = 'ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ'
                accent = '#16A34A'; bg = '#F0FDF4'

            d_name_kn = d.get('district_kn') or d.get('name_kn')
            d_name_en = d.get('district_en') or d.get('name_en')
            if not d_name_kn:
                match_dist = districts.get(k, {})
                d_name_kn = match_dist.get('name_kn', k)
                d_name_en = match_dist.get('name_en', '')

            d_dict[k] = {
                "district_key": k,
                "name_kn": d_name_kn,
                "name_en": d_name_en,
                "region": region,
                "level": lvl,
                "level_label_kn": level_label,
                "accent_color": accent,
                "bg_color": bg,
                "raw_warning": d.get('warning_info', ''),
                "hazard_kn": hazard,
                "advice_kn": advice
            }

        d_summary['total_alerts'] = d_summary['red'] + d_summary['orange'] + d_summary['yellow']
        master_d5[d_code] = {
            "day_code": d_code,
            "tab_label_kn": day_kn_labels[d_code],
            "summary": d_summary,
            "districts": d_dict
        }

    # 2. Read weather.html
    wpath = ROOT_DIR / "weather.html"
    wcontent = wpath.read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(wcontent, 'html.parser')

    # Update Warnings Summary Pills
    r_el = soup.find(id='ws-count-red')
    if r_el: r_el.string = str(nc_summary['red'])
    o_el = soup.find(id='ws-count-orange')
    if o_el: o_el.string = str(nc_summary['orange'])
    y_el = soup.find(id='ws-count-yellow')
    if y_el: y_el.string = str(nc_summary['yellow'])
    g_el = soup.find(id='ws-count-green')
    if g_el: g_el.string = str(nc_summary['green'])
    a_el = soup.find(id='ws-count-all')
    if a_el: a_el.string = "31"

    # Pre-render 31 cards for Nowcast into #district-warnings-grid
    grid_cards_html = ""
    for d in master_d5['Nowcast']['districts'].values():
        reg_kn = REGION_NAMES_KN.get(d['region'], 'ಕರ್ನಾಟಕ')
        grid_cards_html += f"""
      <div class="dw-card {d['level']}" data-district="{d['district_key']}" data-level="{d['level']}" data-region="{d['region']}">
        <div>
          <div class="dw-header">
            <span class="dw-level-pill">{d['level_label_kn']}</span>
            <span class="dw-region-tag">{reg_kn}</span>
          </div>
          <div class="dw-name-row">
            <div class="dw-name-kn">{d['name_kn']}</div>
            <div class="dw-name-en">{d['name_en']}</div>
          </div>
          <div class="dw-hazard-tag">{d['hazard_kn']}</div>
        </div>
        <div class="dw-advice">ℹ️ {d['advice_kn']}</div>
      </div>"""

    warn_grid = soup.find(id='district-warnings-grid')
    if warn_grid:
        warn_grid.clear()
        warn_grid.append(BeautifulSoup(grid_cards_html, 'html.parser'))

    # Update window.districtWarnings5D in script
    for s in soup.find_all('script'):
        if s.string and 'window.districtWarnings5D =' in s.string:
            sc = s.string
            idx1 = sc.find('window.districtWarnings5D =')
            idx2 = sc.find(';\n', idx1)
            new_json = json.dumps(master_d5, ensure_ascii=False)
            s.string = sc[:idx1] + f'window.districtWarnings5D = {new_json}' + sc[idx2:]
            break

    # Ensure push client script is loaded in weather.html without touching anything else
    push_script = soup.find('script', src='/assets/js/karnata-push-client.js')
    if not push_script:
        new_push_tag = soup.new_tag('script', src='/assets/js/karnata-push-client.js')
        soup.body.append(new_push_tag)
        print("Included karnata-push-client.js in weather.html")

    # Save to both locations
    final_html = str(soup)
    ROOT_DIR.joinpath("weather.html").write_text(final_html, encoding='utf-8')
    ROOT_DIR.joinpath("namma-karnataka", "weather.html").write_text(final_html, encoding='utf-8')
    print("=== SUCCESS: weather.html synced with latest IMD Nowcast & Geo-Push Alerts ===")

if __name__ == "__main__":
    sync_weather()
