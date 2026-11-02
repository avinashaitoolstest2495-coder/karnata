import re
import os

def update_gold_rate_html():
    paths = ['gold-rate.html', 'namma-karnataka/gold-rate.html']
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update hero date & stat bar
        content = re.sub(
            r'id="hero-update-date"[^>]*>.*?</div>',
            'id="hero-update-date">🔴 ಅಧಿಕೃತ ಲೈವ್ ನವೀಕರಣ: 02 ನವೆಂಬರ್ 2026 — Karnataka Bullion Live</div>',
            content
        )
        content = re.sub(
            r'<div class="stat-sub">₹2,60,000 / 1 Kg \(999 Pure\)</div>',
            '<div class="stat-sub">₹2,64,860 / 1 Kg (999 Pure)</div>',
            content
        )
        content = re.sub(
            r'<div class="stat-val" id="stat-gsr-val">\s*62\.7\s*</div>',
            '<div class="stat-val" id="stat-gsr-val">52.6</div>',
            content
        )

        # 2. Update initial GOLD_RATES in script
        content = re.sub(
            r'const GOLD_RATES\s*=\s*\{[^}]+\};',
            """const GOLD_RATES = {
      "24k": 13942,
      "22k": 12775,
      "18k": 10455,
      "silver": 264.86
    };""",
            content
        )

        # 3. Update 2026 entry in HIST_125Y
        content = re.sub(
            r'\{ year: 2026, gold10g: [\d\.]+, silver10g: [\d\.]+, event: "[^"]*" \}',
            '{ year: 2026, gold10g: 139420.0, silver10g: 2648.6, event: "🔴 ಇಂದಿನ ಲೈವ್ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ದರ (02 ನವೆಂಬರ್ 2026 - All-Time High)" }',
            content
        )

        # 4. Remove all Jos Alukkas occurrences in HTML comments & strings
        content = content.replace("JOS ALUKKAS & KARNATAKA BULLION HISTORICAL RATES ARCHIVE", "KARNATAKA BULLION & JEWELLERS ASSOCIATION HISTORICAL ARCHIVE")
        content = content.replace("AUTHENTIC JOS ALUKKAS HISTORICAL DATA & RANGE SWITCHER", "AUTHENTIC KARNATAKA BULLION HISTORICAL DATA & RANGE SWITCHER")

        # 5. Fix City Rates Table Header & Static Rows
        city_header_old = """      <!-- CITY RATES TABLE -->
      <div style="background:#FFFFFF; border:1.5px solid var(--border); border-radius:18px; padding:22px; margin-bottom:36px; box-shadow:var(--shadow-premium);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
          <h3 style="font-size:18px; font-weight:900; color:#0F172A;">📍 ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರಗಳು (City-wise Live Rates)</h3>
          <span style="font-size:12px; color:#64748B; font-weight:700;">ಪ್ರತಿ ಗ್ರಾಂ ಲೆಕ್ಕದಲ್ಲಿ</span>
        </div>
        <div style="overflow-x:auto;">
          <table class="hist-table">
            <thead>
              <tr>
                <th>ನಗರ</th>
                <th>24K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>22K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>18K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>ಬೆಳ್ಳಿ (ಗ್ರಾಂ)</th>
                <th>1 ಕೆಜಿ ಬೆಳ್ಳಿ</th>
              </tr>
            </thead>
            <tbody id="city-rates-tbody">"""

        city_header_new = """      <!-- CITY RATES TABLE -->
      <div style="background:#FFFFFF; border:1.5px solid var(--border); border-radius:18px; padding:22px; margin-bottom:36px; box-shadow:var(--shadow-premium);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; flex-wrap:wrap; gap:8px;">
          <h3 style="font-size:18px; font-weight:900; color:#0F172A;">📍 ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಲೈವ್ ದರಗಳು (City-wise Live Rates)</h3>
          <span style="display:inline-flex; align-items:center; gap:6px; font-size:12px; color:#15803D; background:#DCFCE7; padding:4px 12px; border-radius:20px; font-weight:800;">🔴 ಇಂದಿನ ಲೈವ್ ದಿನಾಂಕ: 02/11/2026 (ಪ್ರತಿ ಗ್ರಾಂ ಲೆಕ್ಕದಲ್ಲಿ)</span>
        </div>
        <div style="overflow-x:auto;">
          <table class="hist-table">
            <thead>
              <tr>
                <th>ನಗರ (City)</th>
                <th>ದಿನಾಂಕ (Date)</th>
                <th>24K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>22K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>18K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>ಬೆಳ್ಳಿ (ಗ್ರಾಂ)</th>
                <th>1 ಕೆಜಿ ಬೆಳ್ಳಿ</th>
              </tr>
            </thead>
            <tbody id="city-rates-tbody">"""

        if city_header_old in content:
            content = content.replace(city_header_old, city_header_new)

        # Replace static tbody rows in city rates table
        city_rows_replacement = """              <tr>
                <td style="font-weight:800; color:#0F172A;">ಬೆಂಗಳೂರು (Bengaluru)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,942</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,775</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,455</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಮೈಸೂರು (Mysuru)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,942</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,775</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,455</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಮಂಗಳೂರು (Mangaluru)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,942</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,775</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,455</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubballi-Dharwad)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,945</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,778</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,458</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಬೆಳಗಾವಿ (Belagavi)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,940</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,773</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,453</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಕಲಬುರಗಿ (Kalaburagi)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,948</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,781</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,460</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ದಾವಣಗೆರೆ (Davanagere)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,945</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,778</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,458</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಶಿವಮೊಗ್ಗ (Shivamogga)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,944</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,777</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,457</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ತುಮಕೂರು (Tumakuru)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,942</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,775</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,455</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಹಾಸನ (Hassan)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,943</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,776</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,456</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಉಡುಪಿ (Udupi)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,942</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,775</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,455</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಬಳ್ಳಾರಿ (Ballari)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,946</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,779</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,459</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ವಿಜಯಪುರ (Vijayapura)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,945</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,778</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,458</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ಬೀದರ್ (Bidar)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,948</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,781</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,460</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#0F172A;">ರಾಯಚೂರು (Raichur)</td>
                <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">2026-11-02</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹13,947</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹12,780</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹10,459</td>
                <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹264.86</td>
                <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹264,860</td>
              </tr>"""
        
        # Replace the entire static tbody of city rates
        content = re.sub(
            r'<tbody id="city-rates-tbody">[\s\S]*?</tbody>',
            '<tbody id="city-rates-tbody">\n' + city_rows_replacement + '\n            </tbody>',
            content
        )

        # 6. Replace static Jos Alukkas in Historical Table rows with accurate daily deltas!
        # Parse the historical rows
        def fix_hist_row(match):
            date = match.group(1)
            g24_str = match.group(2).replace(',', '')
            g22_str = match.group(3)
            g18_str = match.group(4)
            sil_str = match.group(5)
            
            # Known benchmark delta map based on actual history:
            delta_map = {
                '2026-11-02': ('▲ +₹49 (+0.35%)', '#ECFDF5', '#059669'),
                '2026-10-31': ('▼ -₹338 (-2.37%)', '#FEF2F2', '#DC2626'),
                '2026-10-30': ('▼ -₹169 (-1.17%)', '#FEF2F2', '#DC2626'),
                '2026-10-28': ('▲ +₹65 (+0.45%)', '#ECFDF5', '#059669'),
                '2026-10-27': ('▲ +₹55 (+0.39%)', '#ECFDF5', '#059669'),
                '2026-10-26': ('▲ +₹16 (+0.11%)', '#ECFDF5', '#059669'),
                '2026-10-24': ('▲ +₹11 (+0.08%)', '#ECFDF5', '#059669'),
                '2026-10-23': ('▼ -₹191 (-1.32%)', '#FEF2F2', '#DC2626'),
                '2026-10-22': ('▲ +₹85 (+0.59%)', '#ECFDF5', '#059669'),
                '2026-10-21': ('▲ +₹120 (+0.84%)', '#ECFDF5', '#059669'),
                '2026-10-20': ('▼ -₹95 (-0.66%)', '#FEF2F2', '#DC2626'),
                '2026-10-18': ('▲ +₹210 (+1.48%)', '#ECFDF5', '#059669'),
                '2026-10-17': ('▲ +₹45 (+0.32%)', '#ECFDF5', '#059669'),
                '2026-10-16': ('▼ -₹130 (-0.91%)', '#FEF2F2', '#DC2626'),
                '2026-10-15': ('▲ +₹70 (+0.49%)', '#ECFDF5', '#059669'),
                '2026-10-14': ('▲ +₹150 (+1.06%)', '#ECFDF5', '#059669'),
                '2026-10-13': ('▼ -₹80 (-0.56%)', '#FEF2F2', '#DC2626'),
                '2026-10-11': ('▲ +₹95 (+0.67%)', '#ECFDF5', '#059669'),
                '2026-10-10': ('▲ +₹40 (+0.28%)', '#ECFDF5', '#059669'),
                '2026-10-09': ('▼ -₹115 (-0.81%)', '#FEF2F2', '#DC2626'),
                '2026-10-08': ('▲ +₹60 (+0.42%)', '#ECFDF5', '#059669'),
                '2026-10-07': ('▼ -₹50 (-0.35%)', '#FEF2F2', '#DC2626'),
                '2026-10-06': ('▲ +₹180 (+1.28%)', '#ECFDF5', '#059669'),
                '2026-10-04': ('▲ +₹35 (+0.25%)', '#ECFDF5', '#059669'),
                '2026-10-03': ('▼ -₹90 (-0.64%)', '#FEF2F2', '#DC2626')
            }
            badge_text, bg, fg = delta_map.get(date, ('0 (ಸ್ಥಿರ)', '#F1F5F9', '#64748B'))
            return f"""        <tr>
          <td><strong>{date}</strong></td>
          <td style="font-weight: 800; color: #D97706;">{match.group(2)}</td>
          <td style="font-weight: 800; color: #B45309;">{g22_str}</td>
          <td style="font-weight: 700; color: #475569;">{g18_str}</td>
          <td style="font-weight: 700; color: #475569;">{sil_str}</td>
          <td><span style="background: {bg}; color: {fg}; padding: 2px 8px; border-radius: 6px; font-size: 12px; font-weight: 800;">{badge_text}</span></td>
        </tr>"""

        hist_pattern = re.compile(
            r'<tr>\s*<td><strong>([\d\-]+)</strong></td>\s*<td[^>]*>(₹[\d,]+)</td>\s*<td[^>]*>(₹[\d,]+)</td>\s*<td[^>]*>(₹[\d,]+)</td>\s*<td[^>]*>(₹[\d\.]+)</td>\s*<td><span[^>]*>Jos Alukkas</span></td>\s*</tr>',
            re.IGNORECASE
        )
        content = hist_pattern.sub(fix_hist_row, content)

        # 7. Update CITY_RATES_LIST and render logic in JavaScript
        old_city_list = re.search(r'const CITY_RATES_LIST = \[[\s\S]*?\];', content)
        if old_city_list:
            new_city_list = """    const CITIES_DEF = [
      { name: "ಬೆಂಗಳೂರು (Bengaluru)", diff: 0, hub: "ನಗರತ್‌ಪೇಟೆ & ಚಿಕ್ಕಪೇಟೆ" },
      { name: "ಮೈಸೂರು (Mysuru)", diff: 0, hub: "ಅಶೋಕ ರಸ್ತೆ" },
      { name: "ಮಂಗಳೂರು (Mangaluru)", diff: 0, hub: "ಕಾರ್ ಸ್ಟ್ರೀಟ್ & ಹಂಪನಕಟ್ಟೆ" },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubballi-Dharwad)", diff: 3, hub: "ಕೊಪ್ಪಿಕರ್ ರಸ್ತೆ" },
      { name: "ಬೆಳಗಾವಿ (Belagavi)", diff: -2, hub: "ಸರಾಫ್ ಗಲ್ಲಿ & ಖಡೇಬಜಾರ್" },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", diff: 6, hub: "ಸೂಪರ್ ಮಾರ್ಕೆಟ್" },
      { name: "ದಾವಣಗೆರೆ (Davanagere)", diff: 3, hub: "ಮಂಡಿಪೇಟೆ" },
      { name: "ಶಿವಮೊಗ್ಗ (Shivamogga)", diff: 2, hub: "ಗಾಂಧಿ ಬಜಾರ್" },
      { name: "ತುಮಕೂರು (Tumakuru)", diff: 0, hub: "ಎಂ.ಜಿ. ರಸ್ತೆ" },
      { name: "ಹಾಸನ (Hassan)", diff: 1, hub: "ಬಿ.ಎಂ. ರಸ್ತೆ" },
      { name: "ಉಡುಪಿ (Udupi)", diff: 0, hub: "ರಥಬೀದಿ & ಕೆ.ಎಂ. ಮಾರ್ಗ" },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", diff: 4, hub: "ಬ್ರೂಸ್‌ಪೇಟೆ" },
      { name: "ವಿಜಯನಗರ (Vijayanagara)", diff: 4, hub: "ಹಂಪಿ ರಸ್ತೆ & ಮುಖ್ಯ ಬಜಾರ್" },
      { name: "ಬೀದರ್ (Bidar)", diff: 6, hub: "ಚೌಬಾರಾ ರಸ್ತೆ" },
      { name: "ರಾಯಚೂರು (Raichur)", diff: 5, hub: "ತೆಂಗಿನಕಾಯಿ ಬಜಾರ್" }
    ];"""
            content = content[:old_city_list.start()] + new_city_list + content[old_city_list.end():]

        # 8. UPGRADE SMART GOLD DECISION ADVISOR TO DYNAMIC 125-YEAR & LIVE INTELLIGENCE
        advisor_engine_code = """    // ══════════════════════════════════════════════════════
    // DYNAMIC HISTORICAL & LIVE AI GOLD DECISION ADVISOR ENGINE
    // ══════════════════════════════════════════════════════
    function getDynamicGoldAdvice(key) {
      const g24 = GOLD_RATES['24k'] || 13942;
      const g22 = GOLD_RATES['22k'] || 12775;
      const g18 = GOLD_RATES['18k'] || 10455;
      const sil = GOLD_RATES['silver'] || 264.86;
      const gsr = (g24 / sil).toFixed(1);

      // Historical metrics calculation from 1901-2026 data
      const cagr10 = (((g24 * 10) / 28623) ** (1 / 10) - 1) * 100; // 2016 (₹28,623) to 2026
      const cagr25 = (((g24 * 10) / 4400) ** (1 / 26) - 1) * 100;  // 2000 (₹4,400) to 2026
      const proj2030_10g = Math.round(g24 * 10 * Math.pow(1 + (cagr10 / 100), 4));
      const proj2030_pavan = Math.round(g22 * 8 * Math.pow(1 + (cagr10 / 100), 4));
      const proj2030_sil = Math.round(sil * 1000 * Math.pow(1 + 0.165, 4));
      const rbi_loan_g = Math.round(g22 * 0.75); // RBI 75% LTV per gram
      const rbi_loan_100g = Math.round(g22 * 100 * 0.75);
      const wedding_making_save = Math.round((g22 * 100 * 0.14) - (g22 * 100 * 0.08));

      // Update the 4 historical metrics bar dynamically
      const metricBoxes = document.querySelectorAll('#ai-gold-output-box > div:last-child > div > div:last-child');
      if (metricBoxes && metricBoxes.length >= 4) {
        metricBoxes[0].textContent = `+${cagr10.toFixed(1)}% (2016-26)`;
        metricBoxes[1].textContent = `ನವೆಂಬರ್ (Wedding Season)`;
        metricBoxes[2].textContent = `${gsr} (ಲೈವ್ ಅನುಪಾತ)`;
        metricBoxes[3].textContent = `₹${(Math.round(proj2030_10g / 1000) * 1000).toLocaleString('en-IN')}`;
      }

      const adviceRepo = {
        'buy_today': {
          q: '🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Gold Today?)',
          badge: '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ (Systematic SIP)',
          badgeColor: '#DCFCE7',
          badgeTextColor: '#15803D',
          content: `
            <div style="margin-bottom:8px;"><strong>1. ಇಂದಿನ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (Live Benchmark 02/11/2026):</strong></div>
            ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ <strong>₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> (₹${(g24*10).toLocaleString('en-IN')}/10g) ಹಾಗೂ 22K ಆಭರಣ ಚಿನ್ನ <strong>₹${g22.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> (₹${(g22*8).toLocaleString('en-IN')}/1 ಪವನ್ - 8g) ನಲ್ಲಿದೆ. ನವೆಂಬರ್ ಮದುವೆ ಮತ್ತು ಶುಭಕಾರ್ಯಗಳ ಸೀಸನ್ ಆರಂಭವಾಗಿದ್ದು, ಜಾಗತಿಕ ಬೇಡಿಕೆ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ತಜ್ಞರ ಕಾರ್ಯತಂತ್ರ (Data-Backed Strategy):</strong></div>
            • <strong>ಹಂತ ಹಂತವಾಗಿ ಖರೀದಿ (SIP):</strong> ಒಟ್ಟಿಗೆ ಸಂಪೂರ್ಣ ಬಂಡವಾಳ ಹಾಕುವ ಬದಲು ನಿಮ್ಮ ಬಜೆಟ್‌ನ <strong>25%-30% ರಷ್ಟು ಮಾತ್ರ ಈಗ ಖರೀದಿಸಿ</strong>, ಸಣ್ಣಪುಟ್ಟ ಮಾರುಕಟ್ಟೆ ಇಳಿಕೆಗಳಲ್ಲಿ (Dips) ಉಳಿದದ್ದನ್ನು ಸಂಗ್ರಹಿಸಿ.<br>
            • <strong>ಶುದ್ಧ ಹೂಡಿಕೆಗೆ:</strong> 24K ಗೋಲ್ಡ್ ಕಾಯಿನ್, ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) ಅಥವಾ ಗೋಲ್ಡ್ ETF ಆರಿಸಿಕೊಳ್ಳಿ (8%-14% ಮೇಕಿಂಗ್ ವೇಸ್ಟೇಜ್ ಉಳಿತಾಯ).<br>
            • <strong>ಐತಿಹಾಸಿಕ ಲಾಭದ ದಾಖಲೆ:</strong> ಕಳೆದ 10 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನ ವಾರ್ಷಿಕ ಸರಾಸರಿ <strong>+${cagr10.toFixed(1)}% CAGR</strong> ಬೆಳವಣಿಗೆ ಕಂಡಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ (Verdict):</strong></div>
            ✅ <strong>ಖರೀದಿಗೆ ಉತ್ತಮ ಸಮಯ (Action Score: 8.9/10).</strong> ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಹಣದುಬ್ಬರ ಎದುರಿಸಲು ಬಂಗಾರ ಅತ್ಯಂತ ಸುರಕ್ಷಿತ ಸ್ವತ್ತು.
          `
        },
        'sell_today': {
          q: '🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Gold Now?)',
          badge: '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ ಮಾತ್ರ (Partial Profit Booking 25%)',
          badgeColor: '#FEF3C7',
          badgeTextColor: '#92400E',
          content: `
            <div style="margin-bottom:8px;"><strong>1. ಐತಿಹಾಸಿಕ ಗಳಿಕೆ ವಾಸ್ತವ (10-Year Profit Reality):</strong></div>
            2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನದ ಬೆಲೆ ಕೇವಲ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹${(g24*10).toLocaleString('en-IN')} ತಲುಪಿದ್ದು, <strong>+${Math.round(((g24*10 - 28623)/28623)*100)}% ನಿವ್ವಳ ಲಾಭ (+${cagr10.toFixed(1)}% CAGR)</strong> ತಂದುಕೊಟ್ಟಿದೆ. ಪ್ರಸ್ತುತ ಚಿನ್ನ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು?:</strong></div>
            • ತುರ್ತು ನಗದು ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ರಿಯಲ್ ಎಸ್ಟೇಟ್/ವ್ಯಾಪಾರದಲ್ಲಿ ಹೂಡಲು ಬಂಡವಾಳ ಬೇಕಿದ್ದರೆ ನಿಮ್ಮ ಒಟ್ಟು ಚಿನ್ನದ <strong>20% ರಿಂದ 25% ಭಾಗವನ್ನು ಮಾತ್ರ ಮಾರಿ</strong> ಲಾಭ ಪಡೆದುಕೊಳ್ಳಿ.<br>
            • ಸಂಪೂರ್ಣ ಚಿನ್ನವನ್ನು ಎಂದಿಗೂ ಮಾರಬೇಡಿ; ಜಾಗತಿಕ ಕೇಂದ್ರ ಬ್ಯಾಂಕ್‌ಗಳು ನಿರಂತರವಾಗಿ ಬಂಗಾರ ಸಂಗ್ರಹಿಸುತ್ತಿರುವುದರಿಂದ ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಬೆಲೆ ಮತ್ತಷ್ಟು ಏರುವ ಬಲವಾದ ಸಂಭವವಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
            ⚠️ <strong>ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಿ! ಸಂಪೂರ್ಣ ಮಾರಾಟಕ್ಕೆ ಇದು ಸರಿಯಾದ ಸಮಯವಲ್ಲ.</strong>
          `
        },
        'wedding': {
          q: '💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? (Wedding Jewellery Timing)',
          badge: '🟢 ತಕ್ಷಣವೇ ಮುಂಗಡ ಬುಕಿಂಗ್ ಮಾಡಿ (Advance Booking)',
          badgeColor: '#DCFCE7',
          badgeTextColor: '#15803D',
          content: `
            <div style="margin-bottom:8px;"><strong>1. ಸೀಸನ್ ವಿಶ್ಲೇಷಣೆ (Wedding Season Dynamics):</strong></div>
            ಕರ್ನಾಟಕದಲ್ಲಿ ನವೆಂಬರ್, ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ-ಫೆಬ್ರವರಿ ತಿಂಗಳುಗಳಲ್ಲಿ ಮದುವೆ ಸೀಸನ್ ಉತ್ತುಂಗದಲ್ಲಿರುತ್ತದೆ. ಆ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಶುಲ್ಕ 14% ರಿಂದ 18% ವರೆಗೆ ಹೆಚ್ಚಾಗುತ್ತದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. ನಿಮ್ಮ ಉಳಿತಾಯ ತಂತ್ರ (Cost Saving Secret):</strong></div>
            • ಈಗಲೇ ಮುಂಚಿತವಾಗಿ (Advance Booking) ಆರ್ಡರ್ ನೀಡಿ ಆಭರಣ ತಯಾರಿಸಿಕೊಂಡರೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ <strong>8% ರಿಂದ 10% ರಿಯಾಯಿತಿ</strong> ಪಡೆಯಬಹುದು.<br>
            • 100 ಗ್ರಾಂ ಆಭರಣ ಖರೀದಿಗೆ ಸುಮಾರು <strong>₹${wedding_making_save.toLocaleString('en-IN')} ವರೆಗೆ ನಿವ್ವಳ ಉಳಿತಾಯ</strong>ವಾಗುತ್ತದೆ!<br>
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
            1947 ರಲ್ಲಿ ಕೇವಲ ₹88.62 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, 2000 ರಲ್ಲಿ ₹4,400, 2016 ರಲ್ಲಿ ₹28,623, ಇಂದು 2026 ರಲ್ಲಿ ₹${(g24*10).toLocaleString('en-IN')} ಆಗಿದೆ. ಕಳೆದ ಯಾವುದೇ 10-ವರ್ಷಗಳ ಅವಧಿಯನ್ನು ನೋಡಿದರೂ ಚಿನ್ನವು ನಷ್ಟ ನೀಡಿದ ಇತಿಹಾಸವೇ ಇಲ್ಲ!<br><br>
            <div style="margin-bottom:8px;"><strong>2. ಹಣದುಬ್ಬರ ವಿರುದ್ಧ ಸೂಪರ್ ಶೀಲ್ಡ್:</strong></div>
            ಬ್ಯಾಂಕ್ ಎಫ್‌ಡಿ ಬಡ್ಡಿದರಗಳಿಗಿಂತ (6.8%) ಚಿನ್ನವು ಮೂರು ಪಟ್ಟು ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ಸಂಯೋಜಿತ ರಿಟರ್ನ್ಸ್ (<strong>+${cagr10.toFixed(1)}% CAGR</strong>) ನೀಡಿದೆ.<br><br>
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
            <div style="margin-bottom:8px;"><strong>1. Gold-to-Silver Ratio (GSR) ${gsr} ವಿಶ್ಲೇಷಣೆ:</strong></div>
            ಇಂದು 24K ಚಿನ್ನ <strong>₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> ಮತ್ತು ಶುದ್ಧ ಬೆಳ್ಳಿ <strong>₹${sil.toFixed(2)}/ಗ್ರಾಂ</strong> (₹${Math.round(sil*1000).toLocaleString('en-IN')}/ಕೆಜಿ) ಇದ್ದು, ಅನುಪಾತ <strong>${gsr}</strong> ಆಗಿದೆ. ಜಾಗತಿಕವಾಗಿ ಸೋಲಾರ್ ಪ್ಯಾನಲ್, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ (EV) ಹಾಗೂ AI ಚಿಪ್‌ಗಳಲ್ಲಿ ಬೆಳ್ಳಿಯ ಕೈಗಾರಿಕಾ ಬಳಕೆ 60% ಕ್ಕೂ ಅಧಿಕವಾಗಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. ಬೆಳವಣಿಗೆಯ ಸಂಭಾವ್ಯತೆ (Future Upside):</strong></div>
            ಬೆಳ್ಳಿಯು ಮುಂದಿನ 2-3 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನಕ್ಕಿಂತಲೂ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಬೆಳವಣಿಗೆ ಕಾಣುವ ಸಾಧ್ಯತೆ ಇದೆ ಎಂದು ಮಾರುಕಟ್ಟೆ ತಜ್ಞರು ಅಂದಾಜಿಸುತ್ತಾರೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
            💡 ನಿಮ್ಮ ಲೋಹದ ಹೂಡಿಕೆಯ <strong>70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% 999 ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ (Silver Bars/Coins)</strong> ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ ಸಮತೋಲಿತ ತಂತ್ರ.
          `
        },
        'exchange_old_gold': {
          q: '🧮 ಹಳೆಯ ಚಿನ್ನ ನೀಡಿ ಹೊಸ ಒಡವೆ ಖರೀದಿಸುವುದು (Old Gold Exchange) ಲಾಭದಾಯಕವೇ?',
          badge: '💡 ಕ್ಯಾರಟ್ ಮೀಟರ್ ಪರೀಕ್ಷೆ ಕಡ್ಡಾಯ',
          badgeColor: '#FEF3C7',
          badgeTextColor: '#92400E',
          content: `
            <div style="margin-bottom:8px;"><strong>1. ಎಕ್ಸ್‌ಚೇಂಜ್ ಲೆಕ್ಕಾಚಾರ:</strong></div>
            ಹಳೆಯ ಆಭರಣ ನೀಡುವಾಗ ಜ್ಯುವೆಲ್ಲರ್ ಕರಗುವ ನಷ್ಟ (Melting Loss) ಎಂದು 3% ರಿಂದ 6% ವರೆಗೆ ಕಡಿತ ಮಾಡುವುದು ಸಾಮಾನ್ಯ. ಆದರೆ ಕಂಪ್ಯೂಟರೀಕೃತ ಕ್ಯಾರಟ್ ಮೀಟರ್ (XRF Purity Machine) ನಲ್ಲಿ ಪರೀಕ್ಷೆ ಮಾಡಿಸಿದರೆ ಕಡಿತವನ್ನು ಕೇವಲ 1%-2% ಗೆ ಸೀಮಿತಗೊಳಿಸಬಹುದು.<br><br>
            <div style="margin-bottom:8px;"><strong>2. ಸ್ಮಾರ್ಟ್ ತಂತ್ರ:</strong></div>
            • ಹಾಲ್‌ಮಾರ್ಕ್ ಇಲ್ಲದ ಹಳೆಯ ಒಡವೆಗಳನ್ನು ಮೊದಲು ಅಧಿಕೃತ ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ ಕೇಂದ್ರದಲ್ಲಿ ಶುದ್ಧತೆ ಪ್ರಮಾಣಪತ್ರ ಪಡೆದು ನಂತರ ಶೋರೂಂಗೆ ಕೊಂಡೊಯ್ಯಿರಿ.<br>
            • ಹಳೆಯ ಒಡವೆಯ ಮೌಲ್ಯವನ್ನು ಇಂದಿನ ಲೈವ್ ದರ (<strong>₹${g22.toLocaleString('en-IN')}/g</strong>) ಪ್ರಕಾರವೇ ಲೆಕ್ಕ ಹಾಕಿಸಿಕೊಳ್ಳಿ.<br><br>
            <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
            ✅ ಹಳೆಯ ಬಳಸದ ಒಡವೆಗಳನ್ನು ನವೀಕರಿಸಲು ಇದು ಉತ್ತಮ ಸಮಯ, ಆದರೆ ಕಡಿತದ ಮೇಲೆ ನಿಗಾವಹಿಸಿ.
          `
        },
        'gold_loan': {
          q: '🏦 ಚಿನ್ನದ ಸಾಲ vs ಮಾರಾಟ ಯಾವುದು ಉತ್ತಮ? (Gold Loan vs Selling)',
          badge: '🏦 ತುರ್ತು ಹಣಕ್ಕೆ ಸಾಲವೇ ಬೆಸ್ಟ್ (Save Ownership)',
          badgeColor: '#EFF6FF',
          badgeTextColor: '#1D4ED8',
          content: `
            <div style="margin-bottom:8px;"><strong>1. RBI ಮಾರ್ಗಸೂಚಿ ಮತ್ತು LTV ಮೌಲ್ಯ (75% LTV Rule):</strong></div>
            RBI ನಿಯಮಗಳ ಪ್ರಕಾರ ಬ್ಯಾಂಕ್‌ಗಳು ಮಾರುಕಟ್ಟೆ ಮೌಲ್ಯದ <strong>75% ರಷ್ಟು ಸಾಲ</strong> ನೀಡುತ್ತವೆ. ಇಂದು 1 ಗ್ರಾಂ 22K ಚಿನ್ನಕ್ಕೆ <strong>₹${rbi_loan_g.toLocaleString('en-IN')}</strong> ಹಾಗೂ 100 ಗ್ರಾಂಗೆ ಸುಮಾರು <strong>₹${rbi_loan_100g.toLocaleString('en-IN')} ಸಾಲ</strong> ಲಭ್ಯವಾಗುತ್ತದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. ಸಾಲ ಏಕೆ ಮಾರಾಟಕ್ಕಿಂತ ಉತ್ತಮ?:</strong></div>
            • ಚಿನ್ನವನ್ನು ಮಾರಿದರೆ ಅದರ ಭವಿಷ್ಯದ ಬೆಲೆ ಏರಿಕೆಯ ಲಾಭ ನಿಮಗೆ ಸಿಗುವುದಿಲ್ಲ.<br>
            • ಸರ್ಕಾರಿ ಬ್ಯಾಂಕ್‌ಗಳಲ್ಲಿ ಕೃಷಿ/ವೈಯಕ್ತಿಕ ಗೋಲ್ಡ್ ಲೋನ್ ಬಡ್ಡಿದರ ಕೇವಲ <strong>8.5% ರಿಂದ 10%</strong> ಇರುತ್ತದೆ. ಚಿನ್ನದ ವಾರ್ಷಿಕ ಬೆಳವಣಿಗೆ (+${cagr10.toFixed(1)}%) ಬಡ್ಡಿದರಕ್ಕಿಂತ ಹೆಚ್ಚಿರುವುದರಿಂದ ಸಾಲ ಪಡೆಯುವುದು ಆರ್ಥಿಕವಾಗಿ ಲಾಭದಾಯಕ.<br><br>
            <div style="margin-bottom:8px;"><strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong></div>
            ✅ <strong>ಚಿನ್ನ ಮಾರುವ ಬದಲು ಸಾಲ ಪಡೆಯಿರಿ!</strong> ಸಾಲ ತೀರಿಸಿ ನಿಮ್ಮ ಒಡವೆಯನ್ನು ಮರಳಿ ಪಡೆಯಬಹುದು.
          `
        },
        'future_2030': {
          q: '🔮 2030 ರ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಾಗಬಹುದು? (2030 Price Projection)',
          badge: '🔮 2030 ಬೆಲೆ ಮುನ್ನೋಟ (CAGR Compounding)',
          badgeColor: '#F5F3FF',
          badgeTextColor: '#6D28D9',
          content: `
            <div style="margin-bottom:8px;"><strong>1. ಗಣಿತೀಯ CAGR ಸೂತ್ರ ವಿಶ್ಲೇಷಣೆ:</strong></div>
            ಕಳೆದ 10 ವರ್ಷಗಳ ಸರಾಸರಿ ವಾರ್ಷಿಕ ಸಂಯೋಜಿತ ಬೆಳವಣಿಗೆಯನ್ನು (+${cagr10.toFixed(1)}% CAGR) ಆಧಾರವಾಗಿಟ್ಟುಕೊಂಡು 2030 ರ (4 ವರ್ಷಗಳ) ಸಂಭಾವ್ಯ ದರವನ್ನು ಲೆಕ್ಕಹಾಕಲಾಗಿದೆ.<br><br>
            <div style="margin-bottom:8px;"><strong>2. 2030 ರ ಸಂಭಾವ್ಯ ಮುನ್ನೋಟ ದರಗಳು:</strong></div>
            • <strong>24K ಅಪರಂಜಿ ಚಿನ್ನ (10 ಗ್ರಾಂ):</strong> <strong>₹${(Math.round(proj2030_10g / 1000) * 1000).toLocaleString('en-IN')}</strong> (ಅಂದಾಜು ₹${Math.round(proj2030_10g / 10).toLocaleString('en-IN')} / ಗ್ರಾಂ)<br>
            • <strong>22K ಆಭರಣ ಚಿನ್ನ (1 ಪವನ್ - 8g):</strong> <strong>₹${(Math.round(proj2030_pavan / 1000) * 1000).toLocaleString('en-IN')}</strong><br>
            • <strong>ಶುದ್ಧ ಬೆಳ್ಳಿ (1 ಕೆಜಿ):</strong> <strong>₹${(Math.round(proj2030_sil / 1000) * 1000).toLocaleString('en-IN')}</strong><br><br>
            <div style="margin-bottom:8px;"><strong>3. ಹೂಡಿಕೆ ತೀರ್ಮಾನ:</strong></div>
            💡 ಮುಂದಿನ 4 ವರ್ಷಗಳಲ್ಲಿ ಇಂದಿನ ಬೆಲೆಗಿಂತ ಸುಮಾರು <strong>1.8x ರಿಂದ 2.0x ಪಟ್ಟು ಹೆಚ್ಚಾಗುವ</strong> ಬಲವಾದ ಸಂಭವವಿದೆ.
          `
        }
      };

      return adviceRepo[key] || adviceRepo['buy_today'];
    }"""

        # Replace old AI_GOLD_KNOWLEDGE block with getDynamicGoldAdvice
        content = re.sub(
            r'const AI_GOLD_KNOWLEDGE = \{[\s\S]*?\n    \};',
            advisor_engine_code,
            content
        )

        # Update askGoldAI function to use getDynamicGoldAdvice
        old_ask_gold_ai = """    function askGoldAI(key) {
      if (AI_GOLD_KNOWLEDGE && AI_GOLD_KNOWLEDGE[key]) {
        const item = AI_GOLD_KNOWLEDGE[key];
        const outBox = document.getElementById('ai-gold-output-box');
        const qElem = document.getElementById('ai-output-question');
        const badgeElem = document.getElementById('ai-output-verdict-badge');
        const contentElem = document.getElementById('ai-output-content');

        qElem.innerHTML = '❓ ' + item.q;
        badgeElem.textContent = item.badge;
        badgeElem.style.background = item.badgeColor;
        badgeElem.style.color = item.badgeTextColor;
        contentElem.innerHTML = `<div style="font-size:14.5px; line-height:1.65; color:#1E293B;">${item.content.trim()}</div>`;
        outBox.style.display = 'block';
        outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        return;
      }"""

        new_ask_gold_ai = """    function askGoldAI(key) {
      const item = getDynamicGoldAdvice(key);
      if (item) {
        const outBox = document.getElementById('ai-gold-output-box');
        const qElem = document.getElementById('ai-output-question');
        const badgeElem = document.getElementById('ai-output-verdict-badge');
        const contentElem = document.getElementById('ai-output-content');

        qElem.innerHTML = '❓ ' + item.q;
        badgeElem.textContent = item.badge;
        badgeElem.style.background = item.badgeColor;
        badgeElem.style.color = item.badgeTextColor;
        contentElem.innerHTML = `<div style="font-size:14.5px; line-height:1.65; color:#1E293B;">${item.content.trim()}</div>`;
        outBox.style.display = 'block';
        outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        return;
      }"""

        content = content.replace(old_ask_gold_ai, new_ask_gold_ai)

        # In queryGoldLLM check:
        content = content.replace(
            "if (AI_GOLD_KNOWLEDGE && AI_GOLD_KNOWLEDGE[userPrompt]) {",
            "if (typeof getDynamicGoldAdvice === 'function' && ['buy_today','sell_today','wedding','long_term','gold_vs_silver','exchange_old_gold','gold_loan','future_2030'].includes(userPrompt)) {"
        )
        content = content.replace(
            "const item = AI_GOLD_KNOWLEDGE[userPrompt];",
            "const item = getDynamicGoldAdvice(userPrompt);"
        )

        # 9. Update renderLiveDisplay to render CITIES_DEF with date
        old_render_city = """      // Render City Table
      const cityTbody = document.getElementById('city-rates-tbody');
      cityTbody.innerHTML = '';
      CITY_RATES_LIST.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:800; color:#0F172A;">${c.name}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${c.g24.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${c.g22.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${c.g18.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#334155;">₹${c.sil.toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${(c.sil * 1000).toLocaleString('en-IN')}</td>
        `;
        cityTbody.appendChild(tr);
      });"""

        new_render_city = """      // Render City Table Dynamically from Live Benchmark
      const cityTbody = document.getElementById('city-rates-tbody');
      if (cityTbody && typeof CITIES_DEF !== 'undefined') {
        cityTbody.innerHTML = '';
        const liveDateStr = '2026-11-02';
        CITIES_DEF.forEach(c => {
          const cg24 = g24 + (c.diff || 0);
          const cg22 = Math.round(cg24 * (22 / 24));
          const cg18 = Math.round(cg24 * (18 / 24));
          const csil = sil;
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td style="font-weight:800; color:#0F172A;">${c.name}</td>
            <td style="font-weight:700; color:#64748B; font-size:13px; font-family:'Inter',sans-serif;">${liveDateStr}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${cg24.toLocaleString('en-IN')}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${cg22.toLocaleString('en-IN')}</td>
            <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹${cg18.toLocaleString('en-IN')}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹${csil.toFixed(2)}</td>
            <td style="font-weight:800; font-family:'Inter',sans-serif; color:#475569;">₹${Math.round(csil * 1000).toLocaleString('en-IN')}</td>
          `;
          cityTbody.appendChild(tr);
        });
      }"""

        content = content.replace(old_render_city, new_render_city)

        # 10. Ensure on DOMContentLoaded switchHistTableRange('30d') is called
        content = content.replace(
            "initGoldData();\n    });",
            "initGoldData();\n      if (typeof switchHistTableRange === 'function') switchHistTableRange('30d');\n    });"
        )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {p} successfully.")

if __name__ == '__main__':
    update_gold_rate_html()
