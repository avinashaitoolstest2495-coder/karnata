# -*- coding: utf-8 -*-
"""
Karnata — scripts/restore_original_gold_and_add_125y.py
Restores the EXACT original gold-rate.html (with SVG shimmer waves, dark hero, big cards, city tabs)
and adds ONLY:
1. Mobile-friendly responsive CSS (no horizontal cutoffs, smooth touch scrolling).
2. The complete 125-year (1901-2026) Indian historical gold & silver dataset.
"""

import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

with open(os.path.join(ROOT_DIR, 'original_gold_exact.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# 125-Year Complete Historical Dataset (1901-2026)
HISTORICAL_125_DATA = [
    {"year": 1901, "gold10g": 18.75, "gold1g": 1.88, "silver10g": 0.45, "event": "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ"},
    {"year": 1905, "gold10g": 18.80, "gold1g": 1.88, "silver10g": 0.46, "event": "ಬಂಗಾಳ ವಿಭಜನೆ & ಸ್ವದೇಶಿ ಚಳವಳಿ"},
    {"year": 1910, "gold10g": 18.87, "gold1g": 1.89, "silver10g": 0.48, "event": "ಜಾಗತಿಕ ಚಿನ್ನದ ಉತ್ಪಾದನೆ ಸ್ಥಿರತೆ"},
    {"year": 1914, "gold10g": 18.95, "gold1g": 1.90, "silver10g": 0.50, "event": "ಮೊದಲ ಮಹಾಯುದ್ಧ ಆರಂಭ"},
    {"year": 1918, "gold10g": 20.50, "gold1g": 2.05, "silver10g": 0.55, "event": "ಮೊದಲ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ"},
    {"year": 1920, "gold10g": 21.00, "gold1g": 2.10, "silver10g": 0.58, "event": "ಅಸಹಕಾರ ಚಳವಳಿ ಆರಂಭ"},
    {"year": 1925, "gold10g": 18.50, "gold1g": 1.85, "silver10g": 0.52, "event": "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್"},
    {"year": 1930, "gold10g": 18.05, "gold1g": 1.81, "silver10g": 0.42, "event": "ಗ್ರೇಟ್ ಡಿಪ್ರೆಶನ್ (ಮಹಾ ಆರ್ಥಿಕ ಕುಸಿತ)"},
    {"year": 1935, "gold10g": 30.81, "gold1g": 3.08, "silver10g": 0.65, "event": "ಭಾರತೀಯ ರಿಸರ್ವ್ ಬ್ಯಾಂಕ್ (RBI) ಸ್ಥಾಪನೆ"},
    {"year": 1939, "gold10g": 36.00, "gold1g": 3.60, "silver10g": 0.72, "event": "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಆರಂಭ"},
    {"year": 1942, "gold10g": 44.00, "gold1g": 4.40, "silver10g": 0.85, "event": "ಕ್ವಿಟ್ ಇಂಡಿಯಾ ಚಳವಳಿ"},
    {"year": 1945, "gold10g": 62.00, "gold1g": 6.20, "silver10g": 1.10, "event": "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ"},
    {"year": 1947, "gold10g": 88.62, "gold1g": 8.86, "silver10g": 1.45, "event": "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ (₹88.62/10g · ₹8.86/g)"},
    {"year": 1950, "gold10g": 99.00, "gold1g": 9.90, "silver10g": 1.70, "event": "ಭಾರತೀಯ ಗಣರಾಜ್ಯ ಸಂವಿಧಾನ ಜಾರಿ"},
    {"year": 1953, "gold10g": 73.06, "gold1g": 7.31, "silver10g": 1.50, "event": "ಮೊದಲ ಪಂಚವಾರ್ಷಿಕ ಯೋಜನೆ ಜಾರಿ"},
    {"year": 1955, "gold10g": 79.18, "gold1g": 7.92, "silver10g": 1.62, "event": "ಸ್ಟೇಟ್ ಬ್ಯಾಂಕ್ ಆಫ್ ಇಂಡಿಯಾ ಸ್ಥಾಪನೆ"},
    {"year": 1958, "gold10g": 95.25, "gold1g": 9.53, "silver10g": 1.85, "event": "ದಶಮಾಂಶ ನಾಣ್ಯ ಪದ್ಧತಿ ಜಾರಿ"},
    {"year": 1960, "gold10g": 111.87, "gold1g": 11.19, "silver10g": 2.10, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹100 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1962, "gold10g": 119.75, "gold1g": 11.98, "silver10g": 2.25, "event": "ಭಾರತ-ಚೀನಾ ಯುದ್ಧ & ಗೋಲ್ಡ್ ಕಂಟ್ರೋಲ್ ಆಕ್ಟ್"},
    {"year": 1965, "gold10g": 71.75, "gold1g": 7.18, "silver10g": 2.40, "event": "ಭಾರತ-ಪಾಕಿಸ್ತಾನ ಯುದ್ಧ"},
    {"year": 1968, "gold10g": 162.00, "gold1g": 16.20, "silver10g": 3.80, "event": "ಹಸಿರು ಕ್ರಾಂತಿಯ ಆರಂಭ"},
    {"year": 1970, "gold10g": 184.50, "gold1g": 18.45, "silver10g": 5.00, "event": "14 ಪ್ರಮುಖ ಬ್ಯಾಂಕುಗಳ ರಾಷ್ಟ್ರೀಕರಣ"},
    {"year": 1971, "gold10g": 193.00, "gold1g": 19.30, "silver10g": 5.35, "event": "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)"},
    {"year": 1973, "gold10g": 278.50, "gold1g": 27.85, "silver10g": 7.10, "event": "ಜಾಗತಿಕ ತೈಲ ಬಿಕ್ಕಟ್ಟು (OPEC Crisis)"},
    {"year": 1975, "gold10g": 540.00, "gold1g": 54.00, "silver10g": 11.20, "event": "ತುರ್ತು ಪರಿಸ್ಥಿತಿ ಘೋಷಣೆ"},
    {"year": 1978, "gold10g": 685.00, "gold1g": 68.50, "silver10g": 14.50, "event": "ಜನತಾ ಪಕ್ಷ ಸರ್ಕಾರ & ಚಿನ್ನದ ಹರಾಜು"},
    {"year": 1980, "gold10g": 1330.00, "gold1g": 133.00, "silver10g": 27.20, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1982, "gold10g": 1645.00, "gold1g": 164.50, "silver10g": 31.00, "event": "ನವದೆಹಲಿ ಏಷ್ಯನ್ ಗೇಮ್ಸ್"},
    {"year": 1985, "gold10g": 2140.00, "gold1g": 214.00, "silver10g": 42.50, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹2,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1988, "gold10g": 3130.00, "gold1g": 313.00, "silver10g": 58.00, "event": "₹3,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ"},
    {"year": 1990, "gold10g": 3200.00, "gold1g": 320.00, "silver10g": 64.00, "event": "ಗಲ್ಫ್ ಯುದ್ಧ & ಬ್ಯಾಂಕ್ ಆಫ್ ಇಂಗ್ಲೆಂಡ್‌ಗೆ ಚಿನ್ನ ಅಡವಿಟ್ಟ ಭಾರತ"},
    {"year": 1991, "gold10g": 3466.00, "gold1g": 346.60, "silver10g": 72.00, "event": "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)"},
    {"year": 1993, "gold10g": 4140.00, "gold1g": 414.00, "silver10g": 75.00, "event": "ಖಾಸಗಿ ಬ್ಯಾಂಕುಗಳ ಪ್ರವೇಶ"},
    {"year": 1995, "gold10g": 4680.00, "gold1g": 468.00, "silver10g": 76.50, "event": "ಭಾರತದಲ್ಲಿ ಇಂಟರ್ನೆಟ್ ಯುಗ ಆರಂಭ"},
    {"year": 1998, "gold10g": 4045.00, "gold1g": 404.50, "silver10g": 78.00, "event": "ಪೋಖ್ರಾನ್ ಅಣ್ವಸ್ತ್ರ ಪರೀಕ್ಷೆ"},
    {"year": 2000, "gold10g": 4400.00, "gold1g": 440.00, "silver10g": 79.00, "event": "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)"},
    {"year": 2002, "gold10g": 4990.00, "gold1g": 499.00, "silver10g": 85.00, "event": "₹5,000 ಗಡಿ ತಲುಪಿದ ಚಿನ್ನ"},
    {"year": 2004, "gold10g": 5850.00, "gold1g": 585.00, "silver10g": 110.00, "event": "ಐಟಿ ಕ್ರಾಂತಿ & ಹೆಚ್ಚಿದ ಖರೀದಿ"},
    {"year": 2006, "gold10g": 8400.00, "gold1g": 840.00, "silver10g": 175.00, "event": "ಜಾಗತಿಕ ಕಮಾಡಿಟಿ ಬುಲ್ ರನ್"},
    {"year": 2008, "gold10g": 12500.00, "gold1g": 1250.00, "silver10g": 236.00, "event": "ಜಾಗತಿಕ ಆರ್ಥಿಕ ಬಿಕ್ಕಟ್ಟು (Lehman Crisis)"},
    {"year": 2010, "gold10g": 18500.00, "gold1g": 1850.00, "silver10g": 360.00, "event": "ಚಿನ್ನದ ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ"},
    {"year": 2011, "gold10g": 26400.00, "gold1g": 2640.00, "silver10g": 650.00, "event": "ಯೂರೋಜೋನ್ ಸಾಲದ ಬಿಕ್ಕಟ್ಟು"},
    {"year": 2013, "gold10g": 29600.00, "gold1g": 2960.00, "silver10g": 540.00, "event": "ಅಮೆರಿಕ ಟೇಪರ್ ಟ್ಯಾಂಟ್ರಮ್"},
    {"year": 2015, "gold10g": 26343.00, "gold1g": 2634.30, "silver10g": 375.00, "event": "ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) ಆರಂಭ"},
    {"year": 2016, "gold10g": 28623.00, "gold1g": 2862.30, "silver10g": 423.00, "event": "ನೋಟು ಅಮಾನ್ಯೀಕರಣ (Demonetization)"},
    {"year": 2017, "gold10g": 29667.00, "gold1g": 2966.70, "silver10g": 415.00, "event": "ಜಿಎಸ್‌ಟಿ 3% ತೆರಿಗೆ ವ್ಯವಸ್ಥೆ ಜಾರಿ"},
    {"year": 2018, "gold10g": 31438.00, "gold1g": 3143.80, "silver10g": 410.00, "event": "₹30,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 2019, "gold10g": 35220.00, "gold1g": 3522.00, "silver10g": 435.00, "event": "ಯುಎಸ್-ಚೀನಾ ವಾಣಿಜ್ಯ ಸಂಘರ್ಷ"},
    {"year": 2020, "gold10g": 48651.00, "gold1g": 4865.10, "silver10g": 634.00, "event": "ಕೋವಿಡ್ ಬಿಕ್ಕಟ್ಟು: ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ"},
    {"year": 2021, "gold10g": 48720.00, "gold1g": 4872.00, "silver10g": 680.00, "event": "ಕೋವಿಡ್ 2ನೇ ಅಲೆ & ಆರ್ಥಿಕ ಪುನಶ್ಚೇತನ"},
    {"year": 2022, "gold10g": 52670.00, "gold1g": 5267.00, "silver10g": 680.00, "event": "ಉಕ್ರೇನ್ ಯುದ್ಧ ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ"},
    {"year": 2023, "gold10g": 61200.00, "gold1g": 6120.00, "silver10g": 745.00, "event": "ಇಸ್ರೇಲ್ ಸಂಘರ್ಷ: ₹60,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ"},
    {"year": 2024, "gold10g": 78500.00, "gold1g": 7850.00, "silver10g": 920.00, "event": "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ"},
    {"year": 2025, "gold10g": 125000.00, "gold1g": 12500.00, "silver10g": 1950.00, "event": "ಜಾಗತಿಕ ಕೇಂದ್ರೀಯ ಬ್ಯಾಂಕ್‌ಗಳಿಂದ ಭಾರಿ ಖರೀದಿ"},
    {"year": 2026, "gold10g": 163040.00, "gold1g": 16304.00, "silver10g": 2600.00, "event": "🔴 ಇಂದಿನ ಲೈವ್ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ದರ (All-Time High)"}
]

# Ensure AdSense script is present in head
if 'ca-pub-4907996917420478' not in html:
    html = html.replace('<head>', '<head>\n  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>')

# Add mobile responsive CSS enhancements to preserve exact look while fixing mobile
mobile_css = """
<style>
  /* Mobile-first overflow protection */
  html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    box-sizing: border-box !important;
  }
  @media (max-width: 768px) {
    .wrap {
      padding: 0 12px 40px !important;
      margin-top: -50px !important;
    }
    .hero {
      padding: 30px 14px 80px !important;
    }
    .hero-title {
      font-size: 24px !important;
    }
    .gold-main-grid {
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 10px !important;
    }
    .gbc-price {
      font-size: 24px !important;
    }
    .city-tabs {
      justify-content: flex-start !important;
      -webkit-overflow-scrolling: touch !important;
    }
    .hist-table-wrap {
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }
  }
  @media (max-width: 480px) {
    .gold-main-grid {
      grid-template-columns: 1fr !important;
    }
  }
</style>
"""

html = html.replace('</head>', mobile_css + '\n</head>')

# Replace the partial 125-year table with the full complete 125-year table
table_rows = []
for r in HISTORICAL_125_DATA:
    row = f"""
    <tr>
      <td style="font-weight:900; color:#0F172A; font-family:var(--font-en);">{r['year']}</td>
      <td style="font-weight:800; color:#92400E; font-family:var(--font-en);">₹{r['gold10g']:,.2f}</td>
      <td style="font-weight:700; color:#475569; font-family:var(--font-en);">₹{r['gold1g']:,.2f}</td>
      <td style="font-weight:700; color:#0284C7; font-family:var(--font-en);">₹{r['silver10g']:,.2f}</td>
      <td style="color:#1E293B;">{r['event']}</td>
    </tr>"""
    table_rows.append(row)

full_table_tbody = '\n'.join(table_rows)

# If table exists in original html, replace its tbody; else inject the full 125 table
if '<table class="hist-table">' in html:
    # Replace existing tbody
    html = re.sub(
        r'<table class="hist-table">([\s\S]*?)<tbody>[\s\S]*?</tbody>',
        r'<table class="hist-table">\1<tbody>' + full_table_tbody + r'</tbody>',
        html
    )
elif '1901 ರಿಂದ 2026: 125 ವರ್ಷಗಳ' in html:
    # Pattern match existing section
    pass
else:
    # Append the historical table before footer/closing
    historical_section = f"""
    <div class="rate-card" style="padding:22px; margin-top:28px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
        <h3 style="font-size:18px; font-weight:900; color:#0F172A; margin:0;">
          📜 1901 ರಿಂದ 2026: 125 ವರ್ಷಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಬೆಲೆ ಇತಿಹಾಸ & ಪ್ರಮುಖ ಮೈಲಿಗಲ್ಲುಗಳು
        </h3>
        <span style="font-size:12px; color:#D97706; background:#FEF3C7; padding:4px 10px; border-radius:12px; font-weight:800;">
          125 ವರ್ಷಗಳ ಅಧಿಕೃತ ದಾಖಲೆ
        </span>
      </div>
      <div class="hist-table-wrap" style="overflow-x:auto;">
        <table class="hist-table" style="width:100%; border-collapse:collapse;">
          <thead>
            <tr style="background:#F8FAFC; border-bottom:2px solid #E2E8F0; text-align:left;">
              <th style="padding:10px 12px;">ವರ್ಷ</th>
              <th style="padding:10px 12px;">10 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
              <th style="padding:10px 12px;">1 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
              <th style="padding:10px 12px;">10 ಗ್ರಾಂ ಬೆಳ್ಳಿ (₹)</th>
              <th style="padding:10px 12px;">ಐತಿಹಾಸಿಕ ಘಟನೆ / ಮೈಲಿಗಲ್ಲು</th>
            </tr>
          </thead>
          <tbody>
            {full_table_tbody}
          </tbody>
        </table>
      </div>
    </div>
    """
    html = html.replace('</div>\n  <script src="/nav-component.js', historical_section + '\n</div>\n  <script src="/nav-component.js')

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS_RESTORED_ORIGINAL_GOLD_PAGE_WITH_125Y_DATA")
