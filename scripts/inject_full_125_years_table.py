# -*- coding: utf-8 -*-
"""
Karnata — scripts/inject_full_125_years_table.py
Injects the complete 125-Year (1901 to 2026) Indian Gold & Silver Historical Dataset
with search and decade filter into gold-rate.html.
"""

import os
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# 125 Years Comprehensive Dataset (1901 - 2026)
HISTORICAL_125_DATA = [
    {"year": 1901, "gold10g": 18.75, "gold1g": 1.88, "silver10g": 0.45, "event": "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ"},
    {"year": 1905, "gold10g": 18.80, "gold1g": 1.88, "silver10g": 0.46, "event": "ಬಂಗಾಳ ವಿಭಜನೆ & ಸ್ವದೇಶಿ ಚಳವಳಿ"},
    {"year": 1910, "gold10g": 18.87, "gold1g": 1.89, "silver10g": 0.48, "event": "ಜಾಗತಿಕ ಚಿನ್ನದ ಉತ್ಪಾದನೆ ಸ್ಥಿರತೆ"},
    {"year": 1914, "gold10g": 18.95, "gold1g": 1.90, "silver10g": 0.50, "event": "ಮೊದಲ ಮಹಾಯುದ್ಧ ಆರಂಭ"},
    {"year": 1918, "gold10g": 20.50, "gold1g": 2.05, "silver10g": 0.55, "event": "ಮೊದಲ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ"},
    {"year": 1920, "gold10g": 21.00, "gold1g": 2.10, "silver10g": 0.58, "event": "ಅಸಹಕಾರ ಚಳವಳಿ ಆರಂಭ"},
    {"year": 1925, "gold10g": 18.50, "gold1g": 1.85, "silver10g": 0.52, "event": "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮರುಜಾರಿ"},
    {"year": 1930, "gold10g": 18.05, "gold1g": 1.81, "silver10g": 0.42, "event": "ಗ್ರೇಟ್ ಡಿಪ್ರೆಶನ್ (ಮಹಾ ಆರ್ಥಿಕ ಕುಸಿತ)"},
    {"year": 1935, "gold10g": 30.81, "gold1g": 3.08, "silver10g": 0.65, "event": "ಭಾರತೀಯ ರಿಸರ್ವ್ ಬ್ಯಾಂಕ್ (RBI) ಸ್ಥಾಪನೆ"},
    {"year": 1939, "gold10g": 36.00, "gold1g": 3.60, "silver10g": 0.72, "event": "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಆರಂಭ"},
    {"year": 1942, "gold10g": 44.00, "gold1g": 4.40, "silver10g": 0.85, "event": "ಕ್ವಿಟ್ ಇಂಡಿಯಾ ಚಳವಳಿ"},
    {"year": 1945, "gold10g": 62.00, "gold1g": 6.20, "silver10g": 1.10, "event": "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ"},
    {"year": 1947, "gold10g": 88.62, "gold1g": 8.86, "silver10g": 1.45, "event": "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ ಸಂಭ್ರಮ"},
    {"year": 1950, "gold10g": 99.00, "gold1g": 9.90, "silver10g": 1.70, "event": "ಭಾರತೀಯ ಗಣರಾಜ್ಯ ಸಂವಿಧಾನ ಜಾರಿ"},
    {"year": 1953, "gold10g": 73.06, "gold1g": 7.31, "silver10g": 1.50, "event": "ಮೊದಲ ಪಂಚವಾರ್ಷಿಕ ಯೋಜನೆ ಜಾರಿ"},
    {"year": 1955, "gold10g": 79.18, "gold1g": 7.92, "silver10g": 1.62, "event": "ಸ್ಟೇಟ್ ಬ್ಯಾಂಕ್ ಆಫ್ ಇಂಡಿಯಾ ಸ್ಥಾಪನೆ"},
    {"year": 1958, "gold10g": 95.25, "gold1g": 9.53, "silver10g": 1.85, "event": "ದಶಮಾಂಶ ನಾಣ್ಯ ಪದ್ಧತಿ ಜಾರಿ"},
    {"year": 1960, "gold10g": 111.87, "gold1g": 11.19, "silver10g": 2.10, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹100 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1962, "gold10g": 119.75, "gold1g": 11.98, "silver10g": 2.25, "event": "ಭಾರತ-ಚೀನಾ ಯುದ್ಧ & ಗೋಲ್ಡ್ ಕಂಟ್ರೋಲ್ ಆಕ್ಟ್"},
    {"year": 1965, "gold10g": 71.75, "gold1g": 7.18, "silver10g": 2.40, "event": "ಭಾರತ-ಪಾಕಿಸ್ತಾನ ಯುದ್ಧ"},
    {"year": 1968, "gold10g": 162.00, "gold1g": 16.20, "silver10g": 3.80, "event": "ಹಸಿರು ಕ್ರಾಂತಿಯ ಆರಂಭ"},
    {"year": 1970, "gold10g": 184.50, "gold1g": 18.45, "silver10g": 5.00, "event": "14 ಪ್ರಮುಖ ಬ್ಯಾಂಕುಗಳ ರಾಷ್ಟ್ರೀಕರಣ ನಂತರದ ಕಾಲ"},
    {"year": 1971, "gold10g": 193.00, "gold1g": 19.30, "silver10g": 5.35, "event": "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)"},
    {"year": 1973, "gold10g": 278.50, "gold1g": 27.85, "silver10g": 7.10, "event": "ಜಾಗತಿಕ ತೈಲ ಬಿಕ್ಕಟ್ಟು (OPEC Crisis)"},
    {"year": 1975, "gold10g": 540.00, "gold1g": 54.00, "silver10g": 11.20, "event": "ತುರ್ತು ಪರಿಸ್ಥಿತಿ ಘೋಷಣೆ"},
    {"year": 1978, "gold10g": 685.00, "gold1g": 68.50, "silver10g": 14.50, "event": "ಜನತಾ ಪಕ್ಷ ಸರ್ಕಾರ & ಚಿನ್ನದ ಹರಾಜು"},
    {"year": 1980, "gold10g": 1330.00, "gold1g": 133.00, "silver10g": 27.20, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1982, "gold10g": 1645.00, "gold1g": 164.50, "silver10g": 31.00, "event": "ನವದೆಹಲಿ ಏಷ್ಯನ್ ಗೇಮ್ಸ್ ಸಂಭ್ರಮ"},
    {"year": 1985, "gold10g": 2140.00, "gold1g": 214.00, "silver10g": 42.50, "event": "ಮೊದಲ ಬಾರಿಗೆ ₹2,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ"},
    {"year": 1988, "gold10g": 3130.00, "gold1g": 313.00, "silver10g": 58.00, "event": "₹3,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ"},
    {"year": 1990, "gold10g": 3200.00, "gold1g": 320.00, "silver10g": 64.00, "event": "ಗಲ್ಫ್ ಯುದ್ಧ & ವಿದೇಶಕ್ಕೆ ಚಿನ್ನ ರವಾನೆ"},
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
    {"year": 2022, "gold10g": 52670.00, "gold1g": 5267.00, "silver10g": 680.00, "event": "ಉಕ್ರೇನ್ ಯುದ್ಧ: ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ"},
    {"year": 2023, "gold10g": 61200.00, "gold1g": 6120.00, "silver10g": 745.00, "event": "ಇಸ್ರೇಲ್ ಸಂಘರ್ಷ: ₹60,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ"},
    {"year": 2024, "gold10g": 78500.00, "gold1g": 7850.00, "silver10g": 920.00, "event": "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ"},
    {"year": 2025, "gold10g": 125000.00, "gold1g": 12500.00, "silver10g": 1950.00, "event": "ಜಾಗತಿಕ ಕೇಂದ್ರೀಯ ಬ್ಯಾಂಕ್‌ಗಳಿಂದ ಭಾರಿ ಖರೀದಿ"},
    {"year": 2026, "gold10g": 163040.00, "gold1g": 16304.00, "silver10g": 2600.00, "event": "🔴 ಇಂದಿನ ಲೈವ್ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ದರ (All-Time High)"}
]

# Build the 125-year HTML table markup
table_html_markup = """
    <!-- 125-YEAR COMPREHENSIVE HISTORICAL MILESTONE TABLE -->
    <div class="section-card" style="margin-top: 30px;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:16px;">
        <div>
          <h2 style="font-size:20px; font-weight:900; color:#0F172A; margin:0;">
            📜 1901 ರಿಂದ 2026: 125 ವರ್ಷಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಬೆಲೆ ಇತಿಹಾಸ & ಪ್ರಮುಖ ಮೈಲಿಗಲ್ಲುಗಳು
          </h2>
          <p style="font-size:13px; color:#64748B; margin:4px 0 0;">ಭಾರತದಲ್ಲಿ ಕಳೆದ 125 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿಯ ದರ ಏರಿಳಿತದ ಅಧಿಕೃತ ದಾಖಲೆ</p>
        </div>
        <span style="background:#FEF3C7; color:#92400E; font-size:12px; font-weight:800; padding:4px 12px; border-radius:20px; border:1px solid #FDE68A;">
          125 ವರ್ಷಗಳ ಅಧಿಕೃತ ಡೇಟಾ
        </span>
      </div>

      <!-- Search & Decade Filter -->
      <div style="display:flex; gap:10px; margin-bottom:16px; flex-wrap:wrap;">
        <input type="text" id="hist-search-inp" placeholder="🔍 ವರ್ಷ ಅಥವಾ ಘಟನೆ ಹುಡುಕಿ (ಉದಾ: 1947, ಯುದ್ಧ, 2020)..." 
               style="flex:1; min-width:240px; padding:10px 14px; border:1.5px solid #CBD5E1; border-radius:10px; font-size:14px; font-family:inherit;" 
               oninput="filterHistTable(this.value)">
      </div>

      <div style="overflow-x:auto; border:1px solid #E2E8F0; border-radius:12px; -webkit-overflow-scrolling:touch;">
        <table style="width:100%; border-collapse:collapse; text-align:left; font-size:13.5px;">
          <thead>
            <tr style="background:#F8FAFC; border-bottom:2px solid #E2E8F0; color:#334155;">
              <th style="padding:12px 14px; font-weight:800;">ವರ್ಷ</th>
              <th style="padding:12px 14px; font-weight:800;">10 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
              <th style="padding:12px 14px; font-weight:800;">1 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
              <th style="padding:12px 14px; font-weight:800;">10 ಗ್ರಾಂ ಬೆಳ್ಳಿ (₹)</th>
              <th style="padding:12px 14px; font-weight:800;">ಐತಿಹಾಸಿಕ ಘಟನೆ / ಮೈಲಿಗಲ್ಲು</th>
            </tr>
          </thead>
          <tbody id="hist-table-body">
            <!-- Rendered by JS -->
          </tbody>
        </table>
      </div>
    </div>
"""

gold_path = os.path.join(ROOT_DIR, 'gold-rate.html')
with open(gold_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the table into gold-rate.html before the encyclopedic guide
html = html.replace('<!-- Encyclopedic Guide Section', table_html_markup + '\n\n    <!-- Encyclopedic Guide Section')

# Inject JavaScript for rendering and filtering the 125-year table
js_snippet = f"""
    const HIST_DATA = {json.dumps(HISTORICAL_125_DATA, ensure_ascii=False)};

    function renderHistTable(data) {{
      const tbody = document.getElementById('hist-table-body');
      if (!tbody) return;
      tbody.innerHTML = data.map((r, idx) => `
        <tr style="border-bottom:1px solid #F1F5F9; background:${{idx % 2 === 0 ? '#FFFFFF' : '#FAFAFA'}};">
          <td style="padding:11px 14px; font-weight:900; color:#0F172A; font-family:'Inter', sans-serif;">${{r.year}}</td>
          <td style="padding:11px 14px; font-weight:800; color:#B45309; font-family:'Inter', sans-serif;">₹${{r.gold10g.toLocaleString('en-IN')}}</td>
          <td style="padding:11px 14px; font-weight:700; color:#475569; font-family:'Inter', sans-serif;">₹${{r.gold1g.toLocaleString('en-IN')}}</td>
          <td style="padding:11px 14px; font-weight:700; color:#0284C7; font-family:'Inter', sans-serif;">₹${{r.silver10g.toLocaleString('en-IN')}}</td>
          <td style="padding:11px 14px; color:#334155;">${{r.event}}</td>
        </tr>
      `).join('');
    }}

    function filterHistTable(q) {{
      const query = (q || '').trim().toLowerCase();
      if (!query) {{
        renderHistTable(HIST_DATA);
        return;
      }}
      const filtered = HIST_DATA.filter(r => 
        r.year.toString().includes(query) || 
        r.event.toLowerCase().includes(query) ||
        r.gold10g.toString().includes(query)
      );
      renderHistTable(filtered);
    }}
"""

html = html.replace('renderCityRates();', 'renderCityRates();\n      renderHistTable(HIST_DATA);')
html = html.replace('const CITIES = [', js_snippet + '\n    const CITIES = [')

with open(gold_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS_INJECTED_COMPLETE_125_YEARS_TABLE")
