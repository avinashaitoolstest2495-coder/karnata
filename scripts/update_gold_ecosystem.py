# scripts/update_gold_ecosystem.py
import json
import re
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# ══════════════════════════════════════════════════════════════════
# 1. UPDATE data/gold_rates.json
# ══════════════════════════════════════════════════════════════════
print("STEP 1: Updating data/gold_rates.json...")
with open('data/gold_rates.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['last_updated'] = "2026-11-01T06:30:00+05:30"
data['date'] = "2026-11-01"
data['source'] = "ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮತ್ತು ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBMA Live 2026)"

# Base rates
data['base'] = {
    "24k_per_gram": 16304,
    "22k_per_gram": 14940,
    "18k_per_gram": 12224,
    "silver_per_gram": 260.0,
    "rate_24k": 16304,
    "rate_22k": 14940,
    "rate_18k": 12224,
    "silver_999": 260.0
}
data['baseGold'] = { "24": 16304, "22": 14940, "18": 12224 }
data['yesterdayGold'] = { "24": 16256, "22": 14896, "18": 12188 }
data['baseSilver'] = { "999": 260.0, "925": 240.5 }
data['yesterdaySilver'] = { "999": 258.5, "925": 239.0 }
data['silver'] = {
    "999_per_gram": 260.0,
    "925_per_gram": 240.5,
    "999_1kg": 260000,
    "925_1kg": 240500
}
data['changes'] = {
    "24k": 48,
    "22k": 44,
    "18k": 36,
    "silver_999": 1.5,
    "silver_925": 1.5
}
data['change'] = data['changes']

# City-wise calibrated rates
cities_map = {
    "bangalore": {"name_kn": "ಬೆಂಗಳೂರು", "name_en": "Bangalore", "g24": 16304, "g22": 14940, "g18": 12224, "sil": 260.0},
    "mysore": {"name_kn": "ಮೈಸೂರು", "name_en": "Mysore", "g24": 16298, "g22": 14935, "g18": 12220, "sil": 260.0},
    "mangalore": {"name_kn": "ಮಂಗಳೂರು", "name_en": "Mangalore", "g24": 16300, "g22": 14937, "g18": 12221, "sil": 260.0},
    "hubli_dharwad": {"name_kn": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ", "name_en": "Hubli-Dharwad", "g24": 16295, "g22": 14932, "g18": 12217, "sil": 260.0},
    "belgaum": {"name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belgaum", "g24": 16293, "g22": 14930, "g18": 12215, "sil": 260.0},
    "kalaburagi": {"name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "g24": 16290, "g22": 14928, "g18": 12213, "sil": 260.0},
    "davangere": {"name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davangere", "g24": 16297, "g22": 14934, "g18": 12219, "sil": 260.0},
    "shivamogga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "g24": 16298, "g22": 14935, "g18": 12220, "sil": 260.0},
    "tumakuru": {"name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "g24": 16301, "g22": 14938, "g18": 12222, "sil": 260.0},
    "hassan": {"name_kn": "ಹಾಸನ", "name_en": "Hassan", "g24": 16295, "g22": 14932, "g18": 12217, "sil": 260.0},
    "udupi": {"name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "g24": 16302, "g22": 14939, "g18": 12223, "sil": 260.0},
    "ballari": {"name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "g24": 16294, "g22": 14931, "g18": 12216, "sil": 260.0}
}

cities_obj = {}
for cid, cinfo in cities_map.items():
    cities_obj[cid] = {
        "name_kn": cinfo["name_kn"],
        "name_en": cinfo["name_en"],
        "gold_22k_per_gram": cinfo["g22"],
        "gold_24k_per_gram": cinfo["g24"],
        "gold_18k_per_gram": cinfo["g18"],
        "silver_per_gram": cinfo["sil"],
        "silver_1kg": int(cinfo["sil"] * 1000)
    }
data['cities'] = cities_obj

# Build updated continuous history up to 2026-11-01
new_history_entries = [
    {"date": "2026-09-02", "gold24": 15207, "gold22": 13935, "gold18": 11401, "silver999": 232.0, "change": -398},
    {"date": "2026-09-05", "gold24": 15259, "gold22": 13983, "gold18": 11441, "silver999": 233.5, "change": 52},
    {"date": "2026-09-10", "gold24": 15324, "gold22": 14042, "gold18": 11490, "silver999": 235.0, "change": 65},
    {"date": "2026-09-15", "gold24": 15434, "gold22": 14143, "gold18": 11572, "silver999": 238.2, "change": 110},
    {"date": "2026-09-20", "gold24": 15349, "gold22": 14065, "gold18": 11508, "silver999": 236.0, "change": -85},
    {"date": "2026-09-25", "gold24": 15489, "gold22": 14193, "gold18": 11613, "silver999": 239.5, "change": 140},
    {"date": "2026-09-30", "gold24": 15564, "gold22": 14262, "gold18": 11670, "silver999": 242.0, "change": 75},
    {"date": "2026-10-05", "gold24": 15469, "gold22": 14175, "gold18": 11598, "silver999": 240.0, "change": -95},
    {"date": "2026-10-10", "gold24": 15604, "gold22": 14299, "gold18": 11700, "silver999": 243.0, "change": 135},
    {"date": "2026-10-15", "gold24": 15494, "gold22": 14198, "gold18": 11617, "silver999": 241.5, "change": -110},
    {"date": "2026-10-20", "gold24": 15579, "gold22": 14276, "gold18": 11681, "silver999": 243.8, "change": 85},
    {"date": "2026-10-24", "gold24": 15694, "gold22": 14381, "gold18": 11767, "silver999": 246.2, "change": 115},
    {"date": "2026-10-26", "gold24": 15629, "gold22": 14322, "gold18": 11718, "silver999": 245.0, "change": -65},
    {"date": "2026-10-28", "gold24": 15809, "gold22": 14487, "gold18": 11853, "silver999": 248.5, "change": 180},
    {"date": "2026-10-29", "gold24": 16019, "gold22": 14679, "gold18": 12010, "silver999": 252.0, "change": 210},
    {"date": "2026-10-30", "gold24": 16164, "gold22": 14812, "gold18": 12119, "silver999": 256.0, "change": 145},
    {"date": "2026-10-31", "gold24": 16256, "gold22": 14896, "gold18": 12188, "silver999": 258.5, "change": 92},
    {"date": "2026-11-01", "gold24": 16304, "gold22": 14940, "gold18": 12224, "silver999": 260.0, "change": 48}
]

existing_hist = data.get('history', [])
# Filter out anything with dates in new_history_entries
existing_dates = {e['date'] for e in new_history_entries}
clean_hist = [h for h in existing_hist if h.get('date') not in existing_dates and h.get('date', '') < '2026-09-02']
clean_hist.extend(new_history_entries)
data['history'] = clean_hist

with open('data/gold_rates.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated data/gold_rates.json")

# ══════════════════════════════════════════════════════════════════
# 2. UPDATE gold-rate.html
# ══════════════════════════════════════════════════════════════════
print("STEP 2: Updating gold-rate.html...")
with open('gold-rate.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Hero badge
html = re.sub(
    r'<div class="stat-val" id="stat-24k-rate">.*?</div>',
    '<div class="stat-val" id="stat-24k-rate">₹16,304</div>',
    html
)
html = re.sub(
    r'<div class="stat-val" id="stat-22k-rate">.*?</div>',
    '<div class="stat-val" id="stat-22k-rate">₹14,940</div>',
    html
)
html = re.sub(
    r'<div class="stat-val" id="stat-silver-rate">.*?</div>',
    '<div class="stat-val" id="stat-silver-rate">₹260.00</div>',
    html
)
html = re.sub(
    r'<div class="stat-val" id="stat-gsr-val">.*?</div>',
    '<div class="stat-val" id="stat-gsr-val">62.7</div>',
    html
)

# Update rate cards
html = re.sub(r'<div class="gc-price" id="card-24k-rate">.*?</div>', '<div class="gc-price" id="card-24k-rate">₹16,304</div>', html)
html = re.sub(r'<div class="gc-price" id="card-22k-rate">.*?</div>', '<div class="gc-price" id="card-22k-rate">₹14,940</div>', html)
html = re.sub(r'<div class="gc-price" id="card-silver-rate">.*?</div>', '<div class="gc-price" id="card-silver-rate">₹260.00</div>', html)

# Update default JS values
html = re.sub(
    r'const GOLD_RATES = \{[^}]+\};',
    '''const GOLD_RATES = {
      "24k": 16304,
      "22k": 14940,
      "18k": 12224,
      "silver": 260.0
    };''',
    html
)

# Replace CITY_RATES_LIST array in JS
new_city_list_js = '''const CITY_RATES_LIST = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", g24: 16304, g22: 14940, g18: 12224, sil: 260.0 },
      { name: "ಮೈಸೂರು (Mysore)", g24: 16298, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ಮಂಗಳೂರು (Mangalore)", g24: 16300, g22: 14937, g18: 12221, sil: 260.0 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli-Dharwad)", g24: 16295, g22: 14932, g18: 12217, sil: 260.0 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", g24: 16293, g22: 14930, g18: 12215, sil: 260.0 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", g24: 16290, g22: 14928, g18: 12213, sil: 260.0 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", g24: 16297, g22: 14934, g18: 12219, sil: 260.0 },
      { name: "ಶಿವಮೊಗ್ಗ (Shimoga)", g24: 16298, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ತುಮಕೂರು (Tumkur)", g24: 16301, g22: 14938, g18: 12222, sil: 260.0 },
      { name: "ಹಾಸನ (Hassan)", g24: 16295, g22: 14932, g18: 12217, sil: 260.0 },
      { name: "ಉಡುಪಿ (Udupi)", g24: 16302, g22: 14939, g18: 12223, sil: 260.0 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", g24: 16294, g22: 14931, g18: 12216, sil: 260.0 },
      { name: "ವಿಜಯನಗರ (Vijayanagara)", g24: 16294, g22: 14931, g18: 12216, sil: 260.0 },
      { name: "ಬೀದರ್ (Bidar)", g24: 16289, g22: 14926, g18: 12212, sil: 260.0 },
      { name: "ರಾಯಚೂರು (Raichur)", g24: 16292, g22: 14929, g18: 12214, sil: 260.0 }
    ];'''
html = re.sub(r'const CITY_RATES_LIST = \[[^\]]+\];', new_city_list_js, html, flags=re.DOTALL)

# Build updated static HTML table rows for gold history
hist_rows_html = ""
for e in reversed(new_history_entries):
    badge = f'<span style="display:inline-block; padding:2px 8px; border-radius:6px; font-weight:800; font-size:12px; background:#DCFCE7; color:#15803D;">▲ +₹{e["change"]}</span>' if e["change"] >= 0 else f'<span style="display:inline-block; padding:2px 8px; border-radius:6px; font-weight:800; font-size:12px; background:#FEE2E2; color:#B91C1C;">▼ -₹{abs(e["change"])}</span>'
    hist_rows_html += f'''
              <tr>
                <td style="font-weight:800; color:#0F172A; white-space:nowrap;">📅 {e["date"]}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹{e["gold24"]:,}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹{e["gold22"]:,}</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹{e["gold18"]:,}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹{e["silver999"]:.2f}</td>
                <td>{badge}</td>
              </tr>'''

html = re.sub(
    r'<tbody id="gold-history-tbody">[\s\S]*?</tbody>',
    f'<tbody id="gold-history-tbody">{hist_rows_html}\n            </tbody>',
    html
)

# Supercharge AI_GOLD_KNOWLEDGE
super_ai_knowledge = '''const AI_GOLD_KNOWLEDGE = {
      'buy_today': {
        q: '🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Gold Today?)',
        badge: '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ (Systematic Accumulate - SIP)',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <div style="margin-bottom:8px;"><strong>1. ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (2026 All-Time High Analysis):</strong></div>
          ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ <strong>₹16,304/ಗ್ರಾಂ</strong> (₹1,63,040/10g) ಹಾಗೂ 22K ಆಭರಣ ಚಿನ್ನ <strong>₹14,940/ಗ್ರಾಂ</strong> (₹1,19,520/1 ಪವನ್) ನಲ್ಲಿದೆ. ನವೆಂಬರ್ ಮದುವೆ ಮತ್ತು ಶುಭಕಾರ್ಯಗಳ ಸೀಸನ್ ಆರಂಭವಾಗುತ್ತಿರುವುದರಿಂದ ಬೇಡಿಕೆ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>2. AI ತಜ್ಞರ ಕಾರ್ಯತಂತ್ರ (Recommended Action):</strong></div>
          • <strong>ಹಂತ ಹಂತವಾಗಿ ಖರೀದಿ (SIP):</strong> ಒಟ್ಟಿಗೆ ದೊಡ್ಡ ಮೊತ್ತ ಹಾಕುವ ಬದಲು ನಿಮ್ಮ ಬಜೆಟ್‌ನ 25%-30% ರಷ್ಟು ಮಾತ್ರ ಈಗ ಖರೀದಿಸಿ, ಸಣ್ಣ ತಿದ್ದುಪಡಿಗಳಲ್ಲಿ (Price Dip) ಉಳಿದದ್ದನ್ನು ಸಂಗ್ರಹಿಸಿ.<br>
          • <strong>ಶುದ್ಧ ಹೂಡಿಕೆಗೆ:</strong> 24K ಗೋಲ್ಡ್ ಕಾಯಿನ್, ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ ಆರಿಸಿಕೊಳ್ಳಿ (8%-14% ಮೇಕಿಂಗ್ ವೇಸ್ಟೇಜ್ ಉಳಿತಾಯ).<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ (Verdict):</strong></div>
          ✅ <strong>ಖರೀದಿಗೆ ಉತ್ತಮ ಸಮಯ (Action Score: 8.8/10).</strong> ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಹಣದುಬ್ಬರ ಎದುರಿಸಲು ಬಂಗಾರ ಅತ್ಯಂತ ಭದ್ರ ಅಸ್ತಿ.
        `
      },
      'sell_today': {
        q: '🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Gold Now?)',
        badge: '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ ಮಾತ್ರ (Partial Profit Booking 25-30%)',
        badgeColor: '#FEF3C7',
        badgeTextColor: '#92400E',
        content: `
          <div style="margin-bottom:8px;"><strong>1. ಮಾರುಕಟ್ಟೆ ಗಳಿಕೆ ವಿಶ್ಲೇಷಣೆ (Profit Reality):</strong></div>
          2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನದ ಬೆಲೆ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ತಲುಪಿದ್ದು, <strong>+469% ನಿವ್ವಳ ಲಾಭ (+18.9% CAGR)</strong> ತಂದುಕೊಟ್ಟಿದೆ. ಪ್ರಸ್ತುತ ಚಿನ್ನ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು?:</strong></div>
          • ನಿಮ್ಮ ಬಳಿ ತುರ್ತು ನಗದು ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ರಿಯಲ್ ಎಸ್ಟೇಟ್/ವ್ಯಾಪಾರದಲ್ಲಿ ಹೂಡಲು ಬಂಡವಾಳ ಬೇಕಿದ್ದರೆ ನಿಮ್ಮ ಒಟ್ಟು ಚಿನ್ನದ <strong>20% ರಿಂದ 30% ಭಾಗವನ್ನು ಮಾತ್ರ ಮಾರಿ</strong> ಲಾಭ ಪಡೆಯಿರಿ.<br>
          • ಸಂಪೂರ್ಣ ಚಿನ್ನವನ್ನು ಎಂದಿಗೂ ಮಾರಬೇಡಿ; ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳು ನಿರಂತರವಾಗಿ ಚಿನ್ನ ಸಂಗ್ರಹಿಸುತ್ತಿರುವುದರಿಂದ ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಬೆಲೆ ಮತ್ತಷ್ಟು ಏರುವ ಸಂಭವವಿದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
          ⚠️ <strong>ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಿ! ಸಂಪೂರ್ಣ ಮಾರಾಟಕ್ಕೆ ಇದು ಸರಿಯಾದ ಸಮಯವಲ್ಲ.</strong>
        `
      },
      'wedding': {
        q: '💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? (Wedding Jewellery Timing)',
        badge: '🟢 ತಕ್ಷಣವೇ ಪೂರ್ವಭಾವಿ ಬುಕಿಂಗ್ ಮಾಡಿ (Advance Booking)',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <div style="margin-bottom:8px;"><strong>1. ಸೀಸನ್ ವಿಶ್ಲೇಷಣೆ (Wedding Season Dynamic):</strong></div>
          ಕರ್ನಾಟಕದಲ್ಲಿ ನವೆಂಬರ್, ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ-ಫೆಬ್ರವರಿ ತಿಂಗಳುಗಳಲ್ಲಿ ಮದುವೆ ಸೀಸನ್ ಉತ್ತುಂಗದಲ್ಲಿರುತ್ತದೆ. ಆ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಶುಲ್ಕ 14% ರಿಂದ 18% ವರೆಗೆ ಹೆಚ್ಚಾಗುತ್ತದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>2. ನಿಮ್ಮ ಉಳಿತಾಯ ತಂತ್ರ (Cost Saving Secret):</strong></div>
          • ಈಗಲೇ ಮುಂಚಿತವಾಗಿ (Advance Booking) ಆರ್ಡರ್ ನೀಡಿ ಆಭರಣ ತಯಾರಿಸಿಕೊಂಡರೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ <strong>8% ರಿಂದ 10% ರಿಯಾಯಿತಿ</strong> ಚೌಕಾಸಿ ಮಾಡಬಹುದು.<br>
          • 100 ಗ್ರಾಂ ಆಭರಣ ಖರೀದಿಗೆ ಸುಮಾರು <strong>₹35,000 ರಿಂದ ₹55,000 ವರೆಗೆ ನಿವ್ವಳ ಉಳಿತಾಯ</strong>ವಾಗುತ್ತದೆ!<br>
          • ಆಭರಣದ ಮೇಲೆ <strong>BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು 6-ಅಂಕಿಯ HUID ಸಂಖ್ಯೆ</strong> ಕಡ್ಡಾಯವಾಗಿ ಪರಿಶೀಲಿಸಿ.<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
          ✅ <strong>ತಕ್ಷಣ ಆರ್ಡರ್ ಮಾಡಿ! ಮದುವೆ ಹತ್ತಿರ ಬರುವವರೆಗೆ ಕಾಯಬೇಡಿ.</strong>
        `
      },
      'long_term': {
        q: '📈 5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ? (5-10 Yr Investment)',
        badge: '🟢 ದೀರ್ಘಾವಧಿಗೆ ಅತ್ಯುನ್ನತ ಸಂಪತ್ತು ರಕ್ಷಣೆ',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <div style="margin-bottom:8px;"><strong>1. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಸಾಕ್ಷ್ಯ (1901-2026 Archive):</strong></div>
          1947 ರಲ್ಲಿ ಕೇವಲ ₹88.62 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, 2000 ರಲ್ಲಿ ₹4,400, 2016 ರಲ್ಲಿ ₹28,623, ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದೆ. ಕಳೆದ ಯಾವುದೇ 10-ವರ್ಷಗಳ ಅವಧಿಯನ್ನು ನೋಡಿದರೂ ಚಿನ್ನವು ನಷ್ಟ ನೀಡಿದ ಇತಿಹಾಸವೇ ಇಲ್ಲ!<br><br>
          <div style="margin-bottom:8px;"><strong>2. ಹಣದುಬ್ಬರ ವಿರುದ್ಧ ಸೂಪರ್ ಶೀಲ್ಡ್:</strong></div>
          ಕರೆನ್ಸಿ ಮೌಲ್ಯ ಕುಸಿತ ಮತ್ತು ಬ್ಯಾಂಕ್ ಎಫ್‌ಡಿ ಬಡ್ಡಿದರಗಳಿಗಿಂತ (6.8%) ಚಿನ್ನವು ಮೂರು ಪಟ್ಟು ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ರಿಟರ್ನ್ಸ್ (+18.9% CAGR) ತಂದುಕೊಡುತ್ತದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
          ✅ <strong>ಖಂಡಿತ ಹೂಡಿಕೆ ಮಾಡಿ!</strong> 5 ರಿಂದ 10 ವರ್ಷಗಳ ಅವಧಿಗೆ ಚಿನ್ನಕ್ಕಿಂತ ಸುರಕ್ಷಿತ ಅಸ್ತಿ ಇನ್ನೊಂದಿಲ್ಲ.
        `
      },
      'gold_vs_silver': {
        q: '⚖️ ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ? (Gold vs Silver Analysis)',
        badge: '🥈 ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಭಾರಿ ಸಾಮರ್ಥ್ಯವಿದೆ (High Upside)',
        badgeColor: '#EFF6FF',
        badgeTextColor: '#0284C7',
        content: `
          <div style="margin-bottom:8px;"><strong>1. Gold-to-Silver Ratio (GSR) 62.7 ವಿಶ್ಲೇಷಣೆ:</strong></div>
          ಇಂದು 24K ಚಿನ್ನ ₹16,304/ಗ್ರಾಂ ಮತ್ತು ಬೆಳ್ಳಿ ₹260.00/ಗ್ರಾಂ (₹2,60,000/ಕೆಜಿ) ಇದ್ದು, ಅನುಪಾತ <strong>62.7</strong> ಆಗಿದೆ. ಜಾಗತಿಕವಾಗಿ ಸೋಲಾರ್ ಪ್ಯಾನಲ್, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ (EV) ಹಾಗೂ ಸೆಮಿಕಂಡಕ್ಟರ್ ಚಿಪ್‌ಗಳಲ್ಲಿ ಬೆಳ್ಳಿಯ ಕೈಗಾರಿಕಾ ಬಳಕೆ 60% ಕ್ಕೂ ಅಧಿಕವಾಗಿದೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>2. ಬೆಳವಣಿಗೆಯ ಸಂಭಾವ್ಯತೆ (Future Upside):</strong></div>
          ಚಿನ್ನವು ಈಗಾಗಲೇ ಸಾರ್ವಕಾಲಿಕ ದಾಖಲೆಯಲ್ಲಿದೆ, ಆದರೆ ಬೆಳ್ಳಿಯು ಮುಂದಿನ 2-3 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನಕ್ಕಿಂತಲೂ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಜಿಗಿತ ಕಾಣುವ ಸಾಧ್ಯತೆ ಇದೆ ಎಂದು ವಿಶ್ಲೇಷಕರು ಅಭಿಪ್ರಾಯಪಡುತ್ತಾರೆ.<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
          💡 ನಿಮ್ಮ ಲೋಹದ ಹೂಡಿಕೆಯ <strong>70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% 999 ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ (Silver Bars/Coins)</strong> ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ ತಂತ್ರ.
        `
      },
      'exchange_old_gold': {
        q: '🧮 ಹಳೆಯ ಚಿನ್ನ ನೀಡಿ ಹೊಸ ಒಡವೆ ಖರೀದಿಸುವುದು (Old Gold Exchange) ಲಾಭದಾಯಕವೇ?',
        badge: '💡 ಕ್ಯಾರಟ್ ಮೀಟರ್ ಪರೀಕ್ಷೆ ಕಡ್ಡಾಯ',
        badgeColor: '#FEF3C7',
        badgeTextColor: '#92400E',
        content: `
          <div style="margin-bottom:8px;"><strong>1. ಎಕ್ಸ್‌ಚೇಂಜ್ ಲೆಕ್ಕಾಚಾರ:</strong></div>
          ಹಳೆಯ ಆಭರಣ ನೀಡುವಾಗ ಜ್ಯುವೆಲ್ಲರ್ ಕರಗುವ ನಷ್ಟ (Melting Loss) ಎಂದು 3% ರಿಂದ 6% ವರೆಗೆ ಕಡಿತ ಮಾಡುವುದು ಸಾಮಾನ್ಯ. ಆದರೆ ಕಂಪ್ಯೂಟರೀಕೃತ ಕ್ಯಾರಟ್ ಮೀಟರ್ (XRF Purity Machine) ನಲ್ಲಿ ಪರೀಕ್ಷೆ ಮಾಡಿಸಿದರೆ ಕಡಿತವನ್ನು 1%-2% ಗೆ ಸೀಮಿತಗೊಳಿಸಬಹುದು.<br><br>
          <div style="margin-bottom:8px;"><strong>2. ಸ್ಮಾರ್ಟ್ ತಂತ್ರ:</strong></div>
          • ಹಾಲ್‌ಮಾರ್ಕ್ ಇಲ್ಲದ ಹಳೆಯ ಒಡವೆಗಳನ್ನು ಮೊದಲು ಅಧಿಕೃತ ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ ಕೇಂದ್ರದಲ್ಲಿ ಶುದ್ಧತೆ ಪ್ರಮಾಣಪತ್ರ ಪಡೆದು ನಂತರ ಶೋರೂಂಗೆ ಕೊಂಡೊಯ್ಯಿರಿ.<br>
          • ಹಳೆಯ ಒಡವೆಯ ಮೌಲ್ಯವನ್ನು ಇಂದಿನ ಲೈವ್ ದರ (₹14,940/g) ಪ್ರಕಾರವೇ ಲೆಕ್ಕ ಹಾಕಿಸಿಕೊಳ್ಳಿ.<br><br>
          <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
          ✅ ಹಳೆಯ ಮುರಿದ/ಬಳಸದ ಒಡವೆಗಳನ್ನು ನವೀಕರಿಸಲು ಇದು ಉತ್ತಮ ಸಮಯ, ಆದರೆ ಕಡಿತದ ಮೇಲೆ ನಿಗಾವಹಿಸಿ.
        `
      }
    };'''

html = re.sub(r'const AI_GOLD_KNOWLEDGE = \{[\s\S]*?\n    \};', super_ai_knowledge, html)

with open('gold-rate.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated gold-rate.html")
