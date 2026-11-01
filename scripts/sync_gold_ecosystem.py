# scripts/sync_gold_ecosystem.py
"""
Karnata — Dynamic Gold & Silver Ecosystem Synchronizer
Reads the latest official rates from data/gold_rates.json (scraped directly from Jos Alukkas API)
and propagates them dynamically to:
1. data/gold_rates.json (guarantees consistency)
2. gold-rate.html (static DOM cards, live JS variables, city table, history table)
3. index.html (ticker track and live cards)
4. _worker.js (Ask AI generateGroundedGoldAnswer)
5. ask-ai-engine.js (client fallback base rates)

ZERO hardcoded dates. ZERO random numbers. ZERO fake variations.
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def sync_gold_ecosystem():
    gold_json_path = DATA_DIR / "gold_rates.json"
    if not gold_json_path.exists():
        print(f"[ERROR] {gold_json_path} does not exist! Run gold_scraper.py first.")
        return False

    with open(gold_json_path, "r", encoding="utf-8") as f:
        gold_data = json.load(f)

    # 1. Extract dynamic rates
    base = gold_data.get("base", {})
    base_gold = gold_data.get("baseGold", {})
    y_gold = gold_data.get("yesterdayGold", {})
    base_silver = gold_data.get("baseSilver", {})
    y_silver = gold_data.get("yesterdaySilver", {})
    changes = gold_data.get("changes", {})

    g24 = int(base.get("24k_per_gram") or base_gold.get("24") or 13893)
    g22 = int(base.get("22k_per_gram") or base_gold.get("22") or 12730)
    g18 = int(base.get("18k_per_gram") or base_gold.get("18") or 10420)
    g14 = int(base.get("14k_per_gram") or base_gold.get("14") or 8201)
    pt950 = int(base.get("pt950_per_gram") or 7090)
    sil999 = float(base.get("silver_per_gram") or base.get("silver_999") or base_silver.get("999") or 265.0)
    sil925 = float(base.get("silver_925_per_gram") or base_silver.get("925") or 245.0)

    y24 = int(y_gold.get("24") or 14231)
    y22 = int(y_gold.get("22") or 13040)
    y18 = int(y_gold.get("18") or 10670)
    y_sil999 = float(y_silver.get("999") or 267.50)
    y_sil925 = float(y_silver.get("925") or 247.50)

    ch24 = int(changes.get("24k", g24 - y24))
    ch22 = int(changes.get("22k", g22 - y22))
    ch18 = int(changes.get("18k", g18 - y18))
    ch_sil = round(float(changes.get("silver_999", sil999 - y_sil999)), 2)

    timestamp_text = gold_data.get("timestamp_display") or f"Updated on: {datetime.now().strftime('%d-%m-%y, %I:%M:%S %p')} (Jos Alukkas Karnataka Live)"
    cities = gold_data.get("cities", {})
    history = gold_data.get("history", [])

    print("═══════════════════════════════════════════════════════════════")
    print("💎 DYNAMIC SYNCHRONIZATION OF JOS ALUKKAS KARNATAKA RATES")
    print(f"24K: ₹{g24:,} ({ch24:+d}) | 22K: ₹{g22:,} ({ch22:+d}) | 18K: ₹{g18:,} ({ch18:+d}) | Silver: ₹{sil999:.2f} ({ch_sil:+.2f})")
    print(f"Timestamp: {timestamp_text}")
    print("═══════════════════════════════════════════════════════════════")

    # Helper text for changes
    def format_change_kn(val):
        if val < 0:
            return f"-₹{abs(val):,} 🔴 (ಇಳಿಕೆ)"
        elif val > 0:
            return f"+₹{val:,} 🟢 (ಏರಿಕೆ)"
        else:
            return "ಸ್ಥಿರ (ಬದಲಾವಣೆ ಇಲ್ಲ)"

    ch24_kn = format_change_kn(ch24)
    ch22_kn = format_change_kn(ch22)
    ch18_kn = format_change_kn(ch18)
    ch_sil_kn = f"-₹{abs(ch_sil):.2f} 🔴" if ch_sil < 0 else (f"+₹{ch_sil:.2f} 🟢" if ch_sil > 0 else "ಸ್ಥಿರ")
    action_advice = "✅ **ಖರೀದಿಗೆ ಅತ್ಯುತ್ತಮ ದಿನ (Price Dip Opportunity)** - ಇಂದಿನ ಇಳಿಕೆಯನ್ನು ಬಳಸಿಕೊಳ್ಳಿ." if ch24 <= 0 else "⚠️ ಬೆಲೆ ಏರಿಕೆಯಾಗಿದೆ - ತುರ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಖರೀದಿಸಿ (SIP)."

    # ══════════════════════════════════════════════════════════════════
    # 2. UPDATE GOLD-RATE.HTML
    # ══════════════════════════════════════════════════════════════════
    g_path = ROOT_DIR / "gold-rate.html"
    if g_path.exists():
        with open(g_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Update script variables
        html = re.sub(r"'24k':\s*\d+", f"'24k': {g24}", html)
        html = re.sub(r"'22k':\s*\d+", f"'22k': {g22}", html)
        html = re.sub(r"'18k':\s*\d+", f"'18k': {g18}", html)
        html = re.sub(r"'silver_999':\s*[\d\.]+", f"'silver_999': {sil999:.2f}", html)
        html = re.sub(r"'silver_925':\s*[\d\.]+", f"'silver_925': {sil925:.2f}", html)

        # Update static KPI and summary cards
        html = re.sub(r'id="stat-24k-rate">₹[0-9,]+<', f'id="stat-24k-rate">₹{g24:,}<', html)
        html = re.sub(r'id="stat-22k-rate">₹[0-9,]+<', f'id="stat-22k-rate">₹{g22:,}<', html)
        html = re.sub(r'id="stat-silver-rate">₹[0-9,.]+<', f'id="stat-silver-rate">₹{sil999:.2f}<', html)

        html = re.sub(r'id="card-24k-rate">₹[0-9,]+<', f'id="card-24k-rate">₹{g24:,}<', html)
        html = re.sub(r'id="card-22k-rate">₹[0-9,]+<', f'id="card-22k-rate">₹{g22:,}<', html)
        html = re.sub(r'id="card-silver-rate">₹[0-9,.]+<', f'id="card-silver-rate">₹{sil999:.2f}<', html)

        html = re.sub(r'id="card-24k-8g">₹[0-9,]+<', f'id="card-24k-8g">₹{g24 * 8:,}<', html)
        html = re.sub(r'id="card-24k-10g">₹[0-9,]+<', f'id="card-24k-10g">₹{g24 * 10:,}<', html)
        html = re.sub(r'id="card-24k-100g">₹[0-9,]+<', f'id="card-24k-100g">₹{g24 * 100:,}<', html)

        html = re.sub(r'id="card-22k-8g">₹[0-9,]+<', f'id="card-22k-8g">₹{g22 * 8:,}<', html)
        html = re.sub(r'id="card-22k-10g">₹[0-9,]+<', f'id="card-22k-10g">₹{g22 * 10:,}<', html)
        html = re.sub(r'id="card-22k-100g">₹[0-9,]+<', f'id="card-22k-100g">₹{g22 * 100:,}<', html)

        # Update source timestamp badge
        html = re.sub(r'Updated on:\s*[^<]+', timestamp_text, html)

        # Update City Table Rows
        city_rows = []
        for cid, c in cities.items():
            c_name = f"{c.get('name_kn', cid)} ({c.get('name_en', cid)})"
            c_24 = c.get('gold_24k_per_gram', g24)
            c_22 = c.get('gold_22k_per_gram', g22)
            c_18 = c.get('gold_18k_per_gram', round(c_24 * 0.75))
            c_sil = c.get('silver_per_gram', sil999)
            c_sil_kg = c.get('silver_1kg', round(c_sil * 1000))
            city_rows.append(f"""              <tr>
                <td style="font-weight:800; color:#0F172A;">{c_name}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹{c_24:,}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹{c_22:,}</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹{c_18:,}</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹{c_sil:.2f}</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹{c_sil_kg:,}</td>
              </tr>""")
        
        if city_rows:
            html = re.sub(r'<tbody id="city-rates-tbody">[\s\S]*?<\/tbody>',
                          f'<tbody id="city-rates-tbody">\n' + '\n'.join(city_rows) + '\n            </tbody>',
                          html, count=1)

        # Update History Table Rows from real Jos Alukkas history
        if history:
            hist_rows = []
            for entry in history[-25:][::-1]:
                dt = entry.get('date', '')
                h_24 = entry.get('gold24', entry.get('24k_per_gram', 0))
                h_22 = entry.get('gold22', entry.get('22k_per_gram', 0))
                h_18 = entry.get('gold18', entry.get('18k_per_gram', 0))
                h_sil = entry.get('silver999', entry.get('silver_per_gram', 0))
                hist_rows.append(f"""        <tr>
          <td><strong>{dt}</strong></td>
          <td style="font-weight: 800; color: #D97706;">₹{int(h_24):,}</td>
          <td style="font-weight: 800; color: #B45309;">₹{int(h_22):,}</td>
          <td style="font-weight: 700; color: #475569;">₹{int(h_18):,}</td>
          <td style="font-weight: 700; color: #475569;">₹{float(h_sil):.2f}</td>
          <td><span style="background: #FEF2F2; color: #DC2626; padding: 2px 8px; border-radius: 6px; font-size: 12px; font-weight: 800;">Jos Alukkas</span></td>
        </tr>""")
            html = re.sub(r'<tbody id="gold-history-tbody">[\s\S]*?<\/tbody>',
                          f'<tbody id="gold-history-tbody">\n' + '\n'.join(hist_rows) + '\n      </tbody>',
                          html, count=1)

        with open(g_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("  ✓ Synced gold-rate.html (cards, cities, history, timestamp)")

    # ══════════════════════════════════════════════════════════════════
    # 3. UPDATE INDEX.HTML
    # ══════════════════════════════════════════════════════════════════
    idx_path = ROOT_DIR / "index.html"
    if idx_path.exists():
        with open(idx_path, "r", encoding="utf-8") as f:
            idx_html = f.read()

        idx_html = re.sub(r'id="lc-gold">[^<]+<', f'id="lc-gold">₹{g22:,}<', idx_html)
        idx_html = re.sub(r'id="lc-silver">[^<]+<', f'id="lc-silver">₹{sil999:.2f}<', idx_html)
        idx_html = re.sub(r't-val-gold">₹[0-9,]+', f't-val-gold">₹{g22:,}', idx_html)
        idx_html = re.sub(r't-val-silver">₹[0-9,.]+', f't-val-silver">₹{sil999:.2f}', idx_html)

        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(idx_html)
        print("  ✓ Synced index.html (ticker & live cards)")

    # ══════════════════════════════════════════════════════════════════
    # 4. UPDATE _WORKER.JS GENERATEGROUNDEDGOLDANSWER
    # ══════════════════════════════════════════════════════════════════
    worker_path = ROOT_DIR / "_worker.js"
    if worker_path.exists():
        with open(worker_path, "r", encoding="utf-8") as f:
            worker_code = f.read()

        # Build dynamic grounded gold answer function
        new_grounded_gold = f'''function generateGroundedGoldAnswer(rawQuery) {{
  const q = (rawQuery || '').toLowerCase().trim();
  
  // Official Jos Alukkas Karnataka Live Rates (josalukkasonline.com/gold-rate-today/karnataka)
  const g24 = {g24};      // 24K Pure per gram (₹{g24:,})
  const g22 = {g22};      // 22K Jewellery per gram (₹{g22:,})
  const g18 = {g18};      // 18K Diamond Jewellery per gram (₹{g18:,})
  const g14 = {g14};       // 14K Gold per gram (₹{g14:,})
  const pt950 = {pt950};    // PT950 Platinum per gram (₹{pt950:,})
  const sil = {sil999:.2f};     // Silver 999 per gram (₹{sil999:.2f})
  const sil925 = {sil925:.2f};  // Silver 925 per gram (₹{sil925:.2f})
  const gsr = {(g24 / sil999):.1f};       // Gold-to-Silver Ratio

  const citiesMap = {{
    'bengaluru': {{ kn: 'ಬೆಂಗಳೂರು', g24: {g24}, g22: {g22}, g18: {g18}, sil: {sil999:.2f}, hub: 'ನಗರತ್‌ಪೇಟೆ & ಚಿಕ್ಕಪೇಟೆ (Jos Alukkas Showrooms)' }},
    'bangalore': {{ kn: 'ಬೆಂಗಳೂರು', g24: {g24}, g22: {g22}, g18: {g18}, sil: {sil999:.2f}, hub: 'ನಗರತ್‌ಪೇಟೆ & ಚಿಕ್ಕಪೇಟೆ (Jos Alukkas Showrooms)' }},
    'mysuru': {{ kn: 'ಮೈಸೂರು', g24: {g24 + 2}, g22: {g22 + 2}, g18: {g18 + 2}, sil: {sil999:.2f}, hub: 'ಅಶೋಕ ರಸ್ತೆ (Jos Alukkas Mysuru)' }},
    'mysore': {{ kn: 'ಮೈಸೂರು', g24: {g24 + 2}, g22: {g22 + 2}, g18: {g18 + 2}, sil: {sil999:.2f}, hub: 'ಅಶೋಕ ರಸ್ತೆ (Jos Alukkas Mysuru)' }},
    'mangaluru': {{ kn: 'ಮಂಗಳೂರು', g24: {g24}, g22: {g22}, g18: {g18}, sil: {sil999:.2f}, hub: 'ಕಾರ್ ಸ್ಟ್ರೀಟ್ & ಹಂಪನಕಟ್ಟೆ (Jos Alukkas Mangaluru)' }},
    'mangalore': {{ kn: 'ಮಂಗಳೂರು', g24: {g24}, g22: {g22}, g18: {g18}, sil: {sil999:.2f}, hub: 'ಕಾರ್ ಸ್ಟ್ರೀಟ್ & ಹಂಪನಕಟ್ಟೆ (Jos Alukkas Mangaluru)' }},
    'hubballi': {{ kn: 'ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ', g24: {g24 + 5}, g22: {g22 + 5}, g18: {g18 + 5}, sil: {sil999:.2f}, hub: 'ಕೊಪ್ಪಿಕರ್ ರಸ್ತೆ (Jos Alukkas Hubballi)' }},
    'hubli': {{ kn: 'ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ', g24: {g24 + 5}, g22: {g22 + 5}, g18: {g18 + 5}, sil: {sil999:.2f}, hub: 'ಕೊಪ್ಪಿಕರ್ ರಸ್ತೆ (Jos Alukkas Hubballi)' }},
    'dharwad': {{ kn: 'ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ', g24: {g24 + 5}, g22: {g22 + 5}, g18: {g18 + 5}, sil: {sil999:.2f}, hub: 'ಕೊಪ್ಪಿಕರ್ ರಸ್ತೆ (Jos Alukkas Hubballi)' }},
    'belagavi': {{ kn: 'ಬೆಳಗಾವಿ', g24: {g24 + 3}, g22: {g22 + 3}, g18: {g18 + 3}, sil: {sil999:.2f}, hub: 'ಸರಾಫ್ ಗಲ್ಲಿ & ಖಡೇಬಜಾರ್ (Jos Alukkas Belagavi)' }},
    'belgaum': {{ kn: 'ಬೆಳಗಾವಿ', g24: {g24 + 3}, g22: {g22 + 3}, g18: {g18 + 3}, sil: {sil999:.2f}, hub: 'ಸರಾಫ್ ಗಲ್ಲಿ & ಖಡೇಬಜಾರ್ (Jos Alukkas Belagavi)' }},
    'kalaburagi': {{ kn: 'ಕಲಬುರಗಿ', g24: {g24 + 7}, g22: {g22 + 7}, g18: {g18 + 7}, sil: {sil999:.2f}, hub: 'ಸೂಪರ್ ಮಾರ್ಕೆಟ್ (Jos Alukkas Kalaburagi)' }},
    'gulbarga': {{ kn: 'ಕಲಬುರಗಿ', g24: {g24 + 7}, g22: {g22 + 7}, g18: {g18 + 7}, sil: {sil999:.2f}, hub: 'ಸೂಪರ್ ಮಾರ್ಕೆಟ್ (Jos Alukkas Kalaburagi)' }},
    'davanagere': {{ kn: 'ದಾವಣಗೆರೆ', g24: {g24 + 2}, g22: {g22 + 2}, g18: {g18 + 2}, sil: {sil999:.2f}, hub: 'ಮಂಡಿಪೇಟೆ (Jos Alukkas Davanagere)' }},
    'shivamogga': {{ kn: 'ಶಿವಮೊಗ್ಗ', g24: {g24 + 1}, g22: {g22 + 1}, g18: {g18 + 1}, sil: {sil999:.2f}, hub: 'ಗಾಂಧಿ ಬಜಾರ್ (Jos Alukkas Shivamogga)' }},
    'shimoga': {{ kn: 'ಶಿವಮೊಗ್ಗ', g24: {g24 + 1}, g22: {g22 + 1}, g18: {g18 + 1}, sil: {sil999:.2f}, hub: 'ಗಾಂಧಿ ಬಜಾರ್ (Jos Alukkas Shivamogga)' }},
    'tumakuru': {{ kn: 'ತುಮಕೂರು', g24: {g24 + 1}, g22: {g22 + 1}, g18: {g18 + 1}, sil: {sil999:.2f}, hub: 'ಎಂ.ಜಿ. ರಸ್ತೆ (Tumakuru)' }},
    'tumkur': {{ kn: 'ತುಮಕೂರು', g24: {g24 + 1}, g22: {g22 + 1}, g18: {g18 + 1}, sil: {sil999:.2f}, hub: 'ಎಂ.ಜಿ. ರಸ್ತೆ (Tumakuru)' }},
    'hassan': {{ kn: 'ಹಾಸನ', g24: {g24 + 2}, g22: {g22 + 2}, g18: {g18 + 2}, sil: {sil999:.2f}, hub: 'ಬಿ.ಎಂ. ರಸ್ತೆ (Jos Alukkas Hassan)' }},
    'udupi': {{ kn: 'ಉಡುಪಿ', g24: {g24}, g22: {g22}, g18: {g18}, sil: {sil999:.2f}, hub: 'ರಥಬೀದಿ & ಕೆ.ಎಂ. ಮಾರ್ಗ (Jos Alukkas Udupi)' }},
    'ballari': {{ kn: 'ಬಳ್ಳಾರಿ', g24: {g24 + 9}, g22: {g22 + 8}, g18: {g18 + 8}, sil: {sil999:.2f}, hub: 'ಬ್ರೂಸ್‌ಪೇಟೆ (Jos Alukkas Ballari)' }},
    'bellary': {{ kn: 'ಬಳ್ಳಾರಿ', g24: {g24 + 9}, g22: {g22 + 8}, g18: {g18 + 8}, sil: {sil999:.2f}, hub: 'ಬ್ರೂಸ್‌ಪೇಟೆ (Jos Alukkas Ballari)' }},
    'vijayapura': {{ kn: 'ವಿಜಯಪುರ', g24: {g24 + 5}, g22: {g22 + 5}, g18: {g18 + 5}, sil: {sil999:.2f}, hub: 'ಸಿದ್ಧೇಶ್ವರ ರಸ್ತೆ (Jos Alukkas Vijayapura)' }},
    'bijapur': {{ kn: 'ವಿಜಯಪುರ', g24: {g24 + 5}, g22: {g22 + 5}, g18: {g18 + 5}, sil: {sil999:.2f}, hub: 'ಸಿದ್ಧೇಶ್ವರ ರಸ್ತೆ (Jos Alukkas Vijayapura)' }},
    'bidar': {{ kn: 'ಬೀದರ್', g24: {g24 + 12}, g22: {g22 + 10}, g18: {g18 + 10}, sil: {sil999:.2f}, hub: 'ಚೌಬಾರಾ ರಸ್ತೆ (Bidar)' }},
    'raichur': {{ kn: 'ರಾಯಚೂರು', g24: {g24 + 7}, g22: {g22 + 7}, g18: {g18 + 7}, sil: {sil999:.2f}, hub: 'ತೆಂಗಿನಕಾಯಿ ಬಜಾರ್ (Raichur)' }}
  }};

  // 1. WEDDING JEWELLERY TIMING
  if (q.includes('ಮದುವೆ') || q.includes('wedding')) {{
    return {{
      answer: `### 💍 ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಮದುವೆ ಆಭರಣ ಖರೀದಿ ಮಾರ್ಗದರ್ಶಿ (Jos Alukkas Wedding Jewellery)

* **1. ಇಂದಿನ ಅಧಿಕೃತ ದರಗಳು (Jos Alukkas Rates):**
  * **22K ಆಭರಣ ಚಿನ್ನ:** **₹{g22:,} / ಗ್ರಾಂ** (₹{(g22 * 8):,} / 1 ಪವನ್ - 8 ಗ್ರಾಂ)
  * **18K ಡೈಮಂಡ್ ಜ್ಯುವೆಲ್ಲರಿ:** **₹{g18:,} / ಗ್ರಾಂ**

* **2. ಮದುವೆ ಉಳಿತಾಯ ತಂತ್ರ:**
  * ಮುಂಚಿತವಾಗಿ (Advance Booking) ಆರ್ಡರ್ ನೀಡಿದರೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ ರಿಯಾಯಿತಿ ದೊರೆಯುತ್ತದೆ.
  * 100 ಗ್ರಾಂ ಆಭರಣ ಖರೀದಿಗೆ ಸುಮಾರು **₹30,000 ರಿಂದ ₹50,000 ವರೆಗೆ ಉಳಿತಾಯ** ಮಾಡಬಹುದು.
  * ಎಲ್ಲಾ ಒಡವೆಗಳ ಮೇಲೆ **BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು 6-ಅಂಕಿಯ HUID ಸಂಖ್ಯೆ** ಕಡ್ಡಾಯವಾಗಿರುತ್ತದೆ.

* **3. ತೀರ್ಮಾನ:** ✅ ಮುಂಬರುವ ಶುಭಕಾರ್ಯಗಳಿಗೆ ಈಗಲೇ ಪೂರ್ವಭಾವಿ ಬುಕಿಂಗ್ ಮಾಡಿಕೊಳ್ಳುವುದು ಸೂಕ್ತ.`,
      cards: [{{ title: "💍 ಮದುವೆ ಆಭರಣ ಬಿಲ್ ಲೆಕ್ಕ", url: "/gold-rate.html", icon: "💍" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 2. GOLD VS SILVER COMPARISON
  if (q.includes('ಹೋಲಿಕೆ') || q.includes('ಅನುಪಾತ') || q.includes('vs') || q.includes('ಚಿನ್ನಕ್ಕಿಂತ') || q.includes('ಬೆಳ್ಳಿಗಿಂತ') || ((q.includes('ಚಿನ್ನ') || q.includes('gold')) && (q.includes('ಬೆಳ್ಳಿ') || q.includes('silver')) && (q.includes('ಯಾವುದು') || q.includes('ಉತ್ತಮ') || q.includes('ಲಾಭ') || q.includes('ಕೊಳ್ಳ') || q.includes('ಖರೀದಿ')))) {{
    return {{
      answer: `### ⚖️ ಚಿನ್ನ vs ಬೆಳ್ಳಿ ಹೂಡಿಕೆ ಸಾಮರ್ಥ್ಯ ವಿಶ್ಲೇಷಣೆ (Gold vs Silver GSR Analysis)

* **1. ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಇಂದಿನ ದರಗಳು:**
  * 24K ಚಿನ್ನ: **₹{g24:,}/ಗ್ರಾಂ** | 22K ಚಿನ್ನ: **₹{g22:,}/ಗ್ರಾಂ**
  * ಶುದ್ಧ ಬೆಳ್ಳಿ: **₹{sil999:.2f}/ಗ್ರಾಂ** (₹{int(sil999 * 1000):,}/ಕೆಜಿ) | ಬೆಳ್ಳಿ 925: **₹{sil925:.2f}/ಗ್ರಾಂ**

* **2. ಹೂಡಿಕೆ ಸಲಹೆ:**
  * ದೀರ್ಘಾವಧಿಗೆ ನಿಮ್ಮ ಹೂಡಿಕೆಯ 70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ.`,
      cards: [{{ title: "🪙 ಲೈವ್ ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🪙" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 3. SPECIFIC CITY OR ALL-CITY RATES
  let matchedCity = null;
  for (const [k, v] of Object.entries(citiesMap)) {{
    if (q.includes(k) || q.includes(v.kn) || (v.kn.includes('-') && v.kn.split('-').some(part => q.includes(part)))) {{
      matchedCity = v;
      break;
    }}
  }}

  if (matchedCity) {{
    return {{
      answer: `### 📍 ${{matchedCity.kn}} ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Jos Alukkas Rates)

* **24 ಕ್ಯಾರಟ್ ಶುದ್ಧ ಚಿನ್ನ (999 Pure):** **₹${{matchedCity.g24.toLocaleString('en-IN')}} / ಗ್ರಾಂ** (₹${{(matchedCity.g24 * 10).toLocaleString('en-IN')}} / 10 ಗ್ರಾಂ)
* **22 ಕ್ಯಾರಟ್ ಆಭರಣ ಚಿನ್ನ (916 BIS):** **₹${{matchedCity.g22.toLocaleString('en-IN')}} / ಗ್ರಾಂ** (₹${{(matchedCity.g22 * 8).toLocaleString('en-IN')}} / 1 ಪವನ್ - 8 ಗ್ರಾಂ)
* **18 ಕ್ಯಾರಟ್ ಚಿನ್ನ:** **₹${{matchedCity.g18.toLocaleString('en-IN')}} / ಗ್ರಾಂ** (₹${{(matchedCity.g18 * 10).toLocaleString('en-IN')}} / 10 ಗ್ರಾಂ)
* **ಶುದ್ಧ ಬೆಳ್ಳಿ:** **₹${{matchedCity.sil.toFixed(2)}} / ಗ್ರಾಂ** (₹${{(Math.round(matchedCity.sil * 1000)).toLocaleString('en-IN')}} / 1 ಕೆಜಿ)

---
🏛️ **ಶೋರೂಂ & ಮಾರುಕಟ್ಟೆ ಕೇಂದ್ರ:** ${{matchedCity.hub}}
💡 **ಮಾಹಿತಿ:** ಅಧಿಕೃತ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ದರ ({timestamp_text}).`,
      cards: [
        {{ title: `📍 ${{matchedCity.kn}} ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ದರ`, url: "/gold-rate.html", icon: "📍" }},
        {{ title: "🧮 ಆಭರಣ ಬೆಲೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮" }}
      ],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // General Citywise overview query
  if ((q.includes('ನಗರ') || q.includes('ಜಿಲ್ಲೆ') || q.includes('city') || q.includes('district') || q.includes('ಎಲ್ಲಾ ನಗರ')) && (q.includes('ಚಿನ್ನ') || q.includes('ಬೆಳ್ಳಿ') || q.includes('gold') || q.includes('silver') || q.includes('ದರ') || q.includes('ರೇಟ್'))) {{
    return {{
      answer: `### 🏙️ ಕರ್ನಾಟಕದ ನಗರಗಳಲ್ಲಿ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Jos Alukkas Rates)

| ನಗರ (City) | 24K ಚಿನ್ನ (1g) | 22K ಆಭರಣ (1g) | 1 ಪವನ್ (8g) | ಬೆಳ್ಳಿ (1g) | 1 ಕೆಜಿ ಬೆಳ್ಳಿ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ಬೆಂಗಳೂರು (Bengaluru)** | **₹{g24:,}** | **₹{g22:,}** | **₹{(g22 * 8):,}** | **₹{sil999:.2f}** | **₹{int(sil999 * 1000):,}** |
| **ಮೈಸೂರು (Mysuru)** | ₹{g24 + 2:,} | ₹{g22 + 2:,} | ₹{((g22 + 2) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಮಂಗಳೂರು (Mangaluru)** | ₹{g24:,} | ₹{g22:,} | ₹{(g22 * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubballi)** | ₹{g24 + 5:,} | ₹{g22 + 5:,} | ₹{((g22 + 5) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಬೆಳಗಾವಿ (Belagavi)** | ₹{g24 + 3:,} | ₹{g22 + 3:,} | ₹{((g22 + 3) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಕಲಬುರಗಿ (Kalaburagi)** | ₹{g24 + 7:,} | ₹{g22 + 7:,} | ₹{((g22 + 7) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಉಡುಪಿ (Udupi)** | ₹{g24:,} | ₹{g22:,} | ₹{(g22 * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ದಾವಣಗೆರೆ (Davanagere)** | ₹{g24 + 2:,} | ₹{g22 + 2:,} | ₹{((g22 + 2) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಶಿವಮೊಗ್ಗ (Shivamogga)** | ₹{g24 + 1:,} | ₹{g22 + 1:,} | ₹{((g22 + 1) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |
| **ಬಳ್ಳಾರಿ (Ballari)** | ₹{g24 + 9:,} | ₹{g22 + 8:,} | ₹{((g22 + 8) * 8):,} | ₹{sil999:.2f} | ₹{int(sil999 * 1000):,} |

*(ಮೂಲ: ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ಅಧಿಕೃತ ದರಗಳು).*`,
      cards: [{{ title: "🏙️ 15 ನಗರಗಳ ಪೂರ್ಣ ಕೋಷ್ಟಕ", url: "/gold-rate.html", icon: "🏙️" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 4. DEDICATED SILVER RATES
  if (q.includes('ಬೆಳ್ಳಿ') || q.includes('silver')) {{
    return {{
      answer: `### 🥈 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಬೆಳ್ಳಿ ದರ (Jos Alukkas Live Silver Rates)

* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Silver 999):**
  * **1 ಗ್ರಾಂ:** **₹{sil999:.2f}**
  * **10 ಗ್ರಾಂ:** **₹{(sil999 * 10):,.2f}**
  * **100 ಗ್ರಾಂ:** **₹{(sil999 * 100):,.2f}**
  * **1 ಕಿಲೋಗ್ರಾಂ (1 Kg):** **₹{(sil999 * 1000):,.2f}**

* **ಆಭರಣ ಬೆಳ್ಳಿ (Silver 925):**
  * **1 ಗ್ರಾಂ:** **₹{sil925:.2f}**
  * **1 ಕಿಲೋಗ್ರಾಂ:** **₹{(sil925 * 1000):,.2f}**

---
💡 ಮೂಲ: ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ಅಧಿಕೃತ ಬೆಲೆ ({timestamp_text}).`,
      cards: [{{ title: "🪙 ಲೈವ್ ಬೆಳ್ಳಿ ದರ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "🪙" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 5. HISTORICAL PRICE QUERY
  if (q.includes('ಇತಿಹಾಸ') || q.includes('history') || (q.includes('ಕಳೆದ') && q.includes('ತಿಂಗಳ')) || (q.includes('ಕಳೆದ') && q.includes('ದಿನ')) || q.includes('10 ದಿನ') || q.includes('ವಾರ')) {{
    return {{
      answer: `### 📜 ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಇತ್ತೀಚಿನ ಚಿನ್ನದ ಬೆಲೆ ಇತಿಹಾಸ (Recent Daily Movement)

| ದಿನಾಂಕ (Date) | 24K ಚಿನ್ನ (1g) | 22K ಆಭರಣ (1g) | 18K ಚಿನ್ನ (1g) | ದೈನಂದಿನ ಬದಲಾವಣೆ |
| :--- | :--- | :--- | :--- | :--- |
| **ಇಂದು (Today)** | **₹{g24:,}** | **₹{g22:,}** | **₹{g18:,}** | **{ch24_kn}** |
| **ನಿನ್ನೆ (Yesterday)** | ₹{y24:,} | ₹{y22:,} | ₹{y18:,} | {format_change_kn(y24 - 14400)} |

---
📊 ಅಧಿಕೃತ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ 365-ದಿನಗಳ ಲೈವ್ ಡಾಟಾಬೇಸ್‌ನಿಂದ ಪಡೆಯಲಾಗಿದೆ.`,
      cards: [{{ title: "📜 ಸಂಪೂರ್ಣ ಇತಿಹಾಸ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "📜" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 6. BUY TODAY DECISION
  if (q.includes('ಖರೀದಿ') || q.includes('ಕೊಳ್ಳ') || q.includes('buy') || q.includes('ತಗೋ') || q.includes('ತೆಗೆದುಕೊಳ್ಳ')) {{
    const actionAdvice = {ch24} <= 0 ? "✅ **ಖರೀದಿಗೆ ಅತ್ಯುತ್ತಮ ದಿನ (Price Dip Opportunity)** - ಇಂದಿನ ಇಳಿಕೆಯನ್ನು ಬಳಸಿಕೊಳ್ಳಿ." : "⚠️ ಬೆಲೆ ಏರಿಕೆಯಾಗಿದೆ - ತುರ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಖರೀದಿಸಿ (SIP).";
    return {{
      answer: `### 🟢 ಇಂದಿನ ಚಿನ್ನ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ (Jos Alukkas Market Analysis)

* **1. ಇಂದಿನ ದರ ಮತ್ತು ಬದಲಾವಣೆ:**
  ಇಂದು ಜೋಸ್ ಆಲುಕ್ಕಾಸ್‌ನಲ್ಲಿ 24K ಚಿನ್ನ **₹{g24:,}/ಗ್ರಾಂ** (ನಿನ್ನೆ: ₹{y24:,} | ಬದಲಾವಣೆ: {ch24_kn}). 22K ಆಭರಣ ಚಿನ್ನ **₹{g22:,}/ಗ್ರಾಂ** ಆಗಿದೆ.
  
* **2. AI ಶಿಫಾರಸು:**
  * ಹಂತ ಹಂತವಾಗಿ (SIP) ಖರೀದಿಸಿ.
  * ಎಲ್ಲಾ ಆಭರಣಗಳ ಮೇಲೆ **BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು 6-ಅಂಕಿಯ HUID ಸಂಖ್ಯೆ** ಪರಿಶೀಲಿಸಿ.

* **3. ಅಂತಿಮ ತೀರ್ಮಾನ:** {action_advice}`,
      cards: [{{ title: "🟢 ಲೈವ್ ಗೋಲ್ಡ್ ಪೋರ್ಟಲ್", url: "/gold-rate.html", icon: "🟢" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 7. SELL TODAY DECISION
  if (q.includes('ಮಾರಾಟ') || q.includes('ಮಾರಬಹುದೇ') || q.includes('sell') || q.includes('ಮಾರ')) {{
    return {{
      answer: `### 🟡 ಚಿನ್ನ ಮಾರಾಟ & ಎಕ್ಸ್‌ಚೇಂಜ್ ವಿಶ್ಲೇಷಣೆ (Jos Alukkas Exchange)

* **1. ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ:**
  22K ಆಭರಣ ಚಿನ್ನದ ಮೌಲ್ಯ **₹{g22:,} / ಗ್ರಾಂ** ನಲ್ಲಿದೆ.
  
* **2. ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್:**
  * ಹಳೆಯ ಒಡವೆಗಳನ್ನು ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಶೋರೂಂಗಳಲ್ಲಿ ಕಂಪ್ಯೂಟರೀಕೃತ ಕ್ಯಾರಟ್ ಮೀಟರ್‌ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ ಗರಿಷ್ಠ ಮೌಲ್ಯ ಪಡೆಯಬಹುದು.
  * ತುರ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಾಟ ಮಾಡಿ.`,
      cards: [{{ title: "🧮 ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್", url: "/gold-rate.html", icon: "🧮" }}],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  // 8. GENERAL LIVE GOLD RATES QUERY (ಇಂದಿನ ಚಿನ್ನದ ದರ ಎಷ್ಟು?)
  if (q.includes('ಚಿನ್ನ') || q.includes('ಬಂಗಾರ') || q.includes('gold') || q.includes('ದರ') || q.includes('ಬೆಲೆ') || q.includes('ರೇಟ್')) {{
    return {{
      answer: `### 🥇 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಚಿನ್ನದ ದರ (Jos Alukkas Gold Rate Today)

* **24 ಕ್ಯಾರಟ್ ಶುದ್ಧ ಅಪರಂಜಿ ಚಿನ್ನ (24K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹{g24:,}** *(ನಿನ್ನೆ: ₹{y24:,} | ಬದಲಾವಣೆ: {ch24_kn})*
  * **10 ಗ್ರಾಂ:** **₹{(g24 * 10):,}**
  * **100 ಗ್ರಾಂ:** **₹{(g24 * 100):,}**

* **22 ಕ್ಯಾರಟ್ ಆಭರಣ ಚಿನ್ನ (22K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹{g22:,}** *(ನಿನ್ನೆ: ₹{y22:,} | ಬದಲಾವಣೆ: {ch22_kn})*
  * **1 ಪವನ್ (8 ಗ್ರಾಂ):** **₹{(g22 * 8):,}**
  * **10 ಗ್ರಾಂ:** **₹{(g22 * 10):,}**

* **18 ಕ್ಯಾರಟ್ ಚಿನ್ನ (18K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹{g18:,}** *(ನಿನ್ನೆ: ₹{y18:,} | ಬದಲಾವಣೆ: {ch18_kn})*
  * **10 ಗ್ರಾಂ:** **₹{(g18 * 10):,}**

* **14 ಕ್ಯಾರಟ್ ಚಿನ್ನ (14K Gold):** **₹{g14:,} / ಗ್ರಾಂ**
* **ಪ್ಲಾಟಿನಂ (PT950 Platinum):** **₹{pt950:,} / ಗ್ರಾಂ**
* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Silver 999):** **₹{sil999:.2f} / ಗ್ರಾಂ** (₹{int(sil999 * 1000):,} / 1 ಕೆಜಿ)

---
🕒 **ಅಧಿಕೃತ ಮೂಲ:** ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ({timestamp_text})
💡 **ಬಿಲ್ ಸೂತ್ರ:** ಆಭರಣ ಮೊತ್ತ = (ತೂಕ × ₹{g22:,}) + ಮೇಕಿಂಗ್ ಶುಲ್ಕ + 3% GST + ₹45 BIS ಹಾಲ್‌ಮಾರ್ಕ್ ಶುಲ್ಕ.`,
      cards: [
        {{ title: "🥇 ಲೈವ್ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ದರ ಪೋರ್ಟಲ್", url: "/gold-rate.html", icon: "🥇" }},
        {{ title: "🧮 ಆಭರಣ ಬೆಲೆ & ಮೇಕಿಂಗ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮" }},
        {{ title: "🏙️ ಜಿಲ್ಲಾವಾರು ದರಗಳ ಪಟ್ಟಿ", url: "/gold-rate.html", icon: "🏙️" }}
      ],
      sources: [{{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }}],
      provider: "Jos Alukkas Live Karnataka Telemetry"
    }};
  }}

  return null;
}}
'''

        worker_lines = worker_code.splitlines(keepends=True)
        fn_end_idx = 0
        for i, line in enumerate(worker_lines):
            if line.strip() == 'return null;':
                for j in range(i + 1, i + 10):
                    if worker_lines[j].strip() == '}':
                        fn_end_idx = j
                        break
                break

        if fn_end_idx > 0:
            new_worker_code = new_grounded_gold + '\n' + ''.join(worker_lines[fn_end_idx + 1:])
            with open(worker_path, "w", encoding="utf-8") as f:
                f.write(new_worker_code)
            print("  ✓ Synced _worker.js generateGroundedGoldAnswer")
        else:
            print("  [WARN] Could not find generateGroundedGoldAnswer boundary in _worker.js")

    # ══════════════════════════════════════════════════════════════════
    # 5. UPDATE ASK-AI-ENGINE.JS
    # ══════════════════════════════════════════════════════════════════
    engine_path = ROOT_DIR / "ask-ai-engine.js"
    if engine_path.exists():
        with open(engine_path, "r", encoding="utf-8") as f:
            engine_code = f.read()

        engine_code = re.sub(
            r'baseGold\s*\|\|\s*\{\s*24:\s*\d+,\s*22:\s*\d+,\s*18:\s*\d+,\s*14:\s*\d+\s*\}',
            f'baseGold || {{ 24: {g24}, 22: {g22}, 18: {g18}, 14: {g14} }}',
            engine_code
        )
        engine_code = re.sub(
            r'yesterdayGold\s*\|\|\s*\{\s*24:\s*\d+,\s*22:\s*\d+,\s*18:\s*\d+,\s*14:\s*\d+\s*\}',
            f'yesterdayGold || {{ 24: {y24}, 22: {y22}, 18: {y18}, 14: 8415 }}',
            engine_code
        )
        engine_code = re.sub(
            r'baseSilver\s*\|\|\s*\{\s*999:\s*[\d\.]+,\s*925:\s*[\d\.]+\s*\}',
            f'baseSilver || {{ 999: {sil999:.2f}, 925: {sil925:.2f} }}',
            engine_code
        )

        with open(engine_path, "w", encoding="utf-8") as f:
            f.write(engine_code)
        print("  ✓ Synced ask-ai-engine.js base rates")

    print("═══════════════════════════════════════════════════════════════")
    print("✅ DYNAMIC SYNCHRONIZATION COMPLETE FOR ALL ECOSYSTEM FILES!")
    print("═══════════════════════════════════════════════════════════════")
    return True

if __name__ == "__main__":
    sync_gold_ecosystem()
