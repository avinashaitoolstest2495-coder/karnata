import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, base64, re
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
    print("=== SYNCING LATEST WEATHER DATA INTO WEATHER.HTML ===")
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

    for k, d in nowcast_dists.items():
        region = DISTRICT_REGIONS.get(k, 'south')
        lvl = (d.get('alert_level') or d.get('level') or 'green').lower()
        if lvl == 'red':
            nc_summary['red'] += 1
            level_label = '🔴 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'
            hazard = d.get('hazard_kn') or 'ಅತಿ ಭಾರೀ ಮಳೆ & ಬಿರುಗಾಳಿ'
            advice = d.get('warning_info') or 'ತಕ್ಷಣದ ಸುರಕ್ಷತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
            accent = '#E11D48'; bg = '#FFF1F2'
        elif lvl == 'orange':
            nc_summary['orange'] += 1
            level_label = '🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'
            hazard = d.get('hazard_kn') or 'ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ'
            advice = d.get('warning_info') or 'ಮುಂಜಾಗ್ರತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'
            accent = '#D97706'; bg = '#FFFBEB'
        elif lvl == 'yellow':
            nc_summary['yellow'] += 1
            level_label = '🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)'
            hazard = 'ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️'
            raw_wi = d.get('warning_info', '')
            if 'Valid upto:' in raw_wi:
                v_time = raw_wi.split('Valid upto:').pop().strip()
                advice = f"ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: {v_time})"
            else:
                advice = 'ತುಂತುರು ಅಥವಾ ಸಾಧಾರಣ ಮಳೆ ಸಾಧ್ಯತೆ'
            accent = '#CA8A04'; bg = '#FEFCE8'
        else:
            nc_summary['green'] += 1
            level_label = '🟢 ಸಾಮಾನ್ಯ (No Warning)'
            hazard = 'ಶಾಂತ ವಾತಾವರಣ 🌤️'
            advice = 'ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ'
            accent = '#16A34A'; bg = '#F0FDF4'

        nc_dist_dict[k] = {
            "district_key": k,
            "name_kn": d.get('district_kn') or d.get('name_kn') or k,
            "name_en": d.get('district_en') or d.get('name_en') or '',
            "region": region,
            "level": lvl,
            "level_label_kn": level_label,
            "accent_color": accent,
            "bg_color": bg,
            "raw_warning": d.get('warning_info', ''),
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

    # Pre-render Hourly Forecast
    hourly_list = bengaluru.get('hourly_24h', [])
    hourly_html = ""
    for idx, h in enumerate(hourly_list):
        is_now = "now" if idx == 0 else ""
        time_str = h.get('time', f"{idx}:00")
        icon_str = h.get('icon', '⛅')
        temp_str = f"{round(h.get('temp_c', 24))}°"
        rain_chance = h.get('rain_chance', h.get('precip_prob', 0))
        hourly_html += f"""
        <div class="hourly-item {is_now}">
          <div class="hi-time">{time_str}</div>
          <div class="hi-icon">{icon_str}</div>
          <div class="hi-temp">{temp_str}</div>
          <div class="hi-rain">💧 {rain_chance}%</div>
        </div>"""

    el_hourly = soup.find(id='hourly-scroll')
    if el_hourly:
        el_hourly.clear()
        el_hourly.append(BeautifulSoup(hourly_html, 'html.parser'))

    # Pre-render 7-Day Forecast
    forecast_list = bengaluru.get('forecast_7d', [])
    forecast_html = ""
    for idx, f in enumerate(forecast_list):
        is_today = "today" if idx == 0 else ""
        day_kn = f.get('day_kn', 'ಇಂದು' if idx == 0 else ('ನಾಳೆ' if idx == 1 else 'ದಿನ'))
        date_str = f.get('date', '')
        icon_str = f.get('icon', '⛅')
        desc_str = f.get('desc_kn', 'ಸಾಮಾನ್ಯ ಹವಾಮಾನ')
        rain_prob = f.get('precip_prob', 0)
        temp_max = round(f.get('temp_max', 28))
        temp_min = round(f.get('temp_min', 20))
        forecast_html += f"""
        <div class="forecast-h-card {is_today}">
          <div class="fhc-day">{day_kn}</div>
          <div class="fhc-date">{date_str}</div>
          <div class="fhc-icon">{icon_str}</div>
          <div class="fhc-desc">{desc_str}</div>
          <div class="fhc-rain-pill">💧 {rain_prob}%</div>
          <div class="fhc-temp-row">
            <span class="fhc-max">{temp_max}°</span>
            <span class="fhc-min">{temp_min}°</span>
          </div>
        </div>"""

    el_forecast = soup.find(id='forecast-h-scroll')
    if el_forecast:
        el_forecast.clear()
        el_forecast.append(BeautifulSoup(forecast_html, 'html.parser'))

    # Pre-render 31 Districts Live Weather Grid
    district_grid_html = ""
    for k, d in districts.items():
        c = d.get('current', {})
        temp_c = round(c.get('temp_c', 25))
        rain_chance = c.get('rain_chance', 0)
        humidity = c.get('humidity', 70)
        wind_kmh = round(c.get('wind_kmh', 10))
        desc_kn = c.get('desc_kn', 'ಭಾಗಶಃ ಮೋಡ')
        icon_str = c.get('icon', '⛅')
        hq_str = d.get('hq', '')
        d_name = d.get('name_kn', k)
        alert_class = f"alert-{d.get('alert_level')}" if d.get('alert_level') else ""

        district_grid_html += f"""
          <div class="dw-card {alert_class}" onclick="selectDistrict('{k}')">
            <div class="dw-header">
              <div>
                <div class="dw-name">{d_name}</div>
                <div class="dw-hq">{hq_str}</div>
              </div>
              <div class="dw-icon">{icon_str}</div>
            </div>
            <div class="dw-temp-row">
              <span class="dw-temp">{temp_c}°</span>
              <span class="dw-desc">{desc_kn}</span>
            </div>
            <div class="dw-stats">
              <span>💧 {rain_chance}%</span>
              <span>💨 {wind_kmh} km/h</span>
              <span>🌡️ {humidity}%</span>
            </div>
          </div>"""

    el_grid = soup.find(id='district-grid')
    if el_grid:
        el_grid.clear()
        el_grid.append(BeautifulSoup(district_grid_html, 'html.parser'))

    # 3. Update window.districtWarnings5D in script
    for s in soup.find_all('script'):
        if s.string and 'window.districtWarnings5D =' in s.string:
            sc = s.string
            idx1 = sc.find('window.districtWarnings5D =')
            idx2 = sc.find(';\n', idx1)
            new_json = json.dumps(master_d5, ensure_ascii=False)
            s.string = sc[:idx1] + f'window.districtWarnings5D = {new_json}' + sc[idx2:]
            break

    # Save to both locations
    final_html = str(soup)
    ROOT_DIR.joinpath("weather.html").write_text(final_html, encoding='utf-8')
    ROOT_DIR.joinpath("namma-karnataka", "weather.html").write_text(final_html, encoding='utf-8')
    print("=== SUCCESS: weather.html synced with latest IMD Nowcast & KSNDMC data ===")

if __name__ == "__main__":
    sync_weather()
