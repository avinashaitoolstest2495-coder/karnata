# -*- coding: utf-8 -*-
"""
Karnata — scripts/clean_vertical_cards_and_render_full_imd_nowcast.py
1. Removes orphaned vertical static cards from weather.html.
2. Injects the Official IMD Bengaluru District-Wise Nowcast & Warning Dashboard (id=13)
   with live color badges, warnings text, validity time, and 31-district interactive cards.
3. Ensures 24h hourly forecast and 7-day horizontal cards render seamlessly.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove all orphaned vertical forecast-h-card HTML blocks
clean_forecast_section = """  <!-- 24-HOUR HOURLY FORECAST -->
  <div class="hourly-card">
    <div class="sec-head" style="margin: 0 0 14px;">
      <div class="sec-title-text" id="hourly-title">⏱️ ಮುಂದಿನ 24 ಗಂಟೆಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ</div>
    </div>
    <div class="hourly-scroll" id="hourly-scroll"></div>
  </div>

  <!-- 7-DAY FORECAST (HORIZONTAL SCROLL) -->
  <div class="sec-head">
    <div class="sec-title-text" id="forecast-title">📅 ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (7-Day Outlook)</div>
  </div>
  <div class="forecast-horizontal-scroll" id="forecast-h-scroll"></div>"""

content = re.sub(
    r'<!-- 24-HOUR HOURLY FORECAST -->[\s\S]*?<!-- 7-DAY FORECAST -->[\s\S]*?<!-- 7-DAY FORECAST \(CREATIVE HORIZONTAL CARDS\) -->[\s\S]*?</div>\s*</div>\s*(?:<div class="forecast-h-card\s*"[\s\S]*?</div>\s*)+',
    clean_forecast_section,
    content
)

# 2. Build the Official IMD District-Wise Nowcast & Warnings Studio UI Component
imd_nowcast_dashboard_ui = """  <!-- ══════════════════════════════════════════════════════════════════════
       OFFICIAL IMD BENGALURU DISTRICT-WISE NOWCAST & WARNINGS (MAUSAM ID=13)
       ══════════════════════════════════════════════════════════════════════ -->
  <div class="card" style="background:#0F172A; color:#F8FAFC; border:1.5px solid #334155; border-radius:20px; padding:24px; margin:28px 0; box-shadow:0 12px 35px rgba(0,0,0,0.35);">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
      <div>
        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(225,29,72,0.2); border:1px solid #E11D48; color:#FDA4AF; padding:4px 14px; border-radius:100px; font-size:12px; font-weight:800; margin-bottom:8px;">
          <span style="width:8px; height:8px; background:#E11D48; border-radius:50%; display:inline-block; box-shadow:0 0 8px #E11D48;"></span>
          ಅಧಿಕೃತ ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ — IMD Bengaluru (Mausam id=13)
        </div>
        <h2 style="font-size:23px; font-weight:900; color:#FFF; margin:0 0 4px;">⚡ ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ನೌಕಾಸ್ಟ್ & ಎಚ್ಚರಿಕೆಗಳು (District-Wise Nowcast)</h2>
        <p style="font-size:13px; color:#94A3B8; margin:0;">ನೈಜ-ಸಮಯದ ಮಳೆ, ಗುಡುಗು, ಮಿಂಚು ಮತ್ತು ಗಾಳಿಯ ವೇಗದ ಅಧಿಕೃತ ಎಚ್ಚರಿಕೆ ಮಾಹಿತಿ.</p>
      </div>
      
      <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
        <span style="font-size:11.5px; background:rgba(255,255,255,0.1); padding:4px 10px; border-radius:6px; color:#E2E8F0; font-weight:700;" id="imdNowcastUpdateTime">⏱️ IMD ನವೀಕರಣ: ಲೈವ್</span>
        <button onclick="loadImdNowcastWarnings()" style="background:#2563EB; color:#FFF; border:none; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">🔄 ರಿಫ್ರೆಶ್</button>
      </div>
    </div>

    <!-- Alert Level Legend -->
    <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:18px; padding-bottom:14px; border-bottom:1px solid #1E293B; font-size:12px; font-weight:800;">
      <span style="display:inline-flex; align-items:center; gap:5px; color:#FCA5A5;"><span style="width:10px; height:10px; background:#EF4444; border-radius:50%;"></span> 🔴 Red (ಕೆಂಪು ಎಚ್ಚರಿಕೆ - Take Action)</span>
      <span style="display:inline-flex; align-items:center; gap:5px; color:#FDBA74;"><span style="width:10px; height:10px; background:#F97316; border-radius:50%;"></span> 🟠 Orange (ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ - Be Prepared)</span>
      <span style="display:inline-flex; align-items:center; gap:5px; color:#FDE047;"><span style="width:10px; height:10px; background:#EAB308; border-radius:50%;"></span> 🟡 Yellow (ಹಳದಿ ಮುನ್ನೆಚ್ಚರಿಕೆ - Be Updated)</span>
      <span style="display:inline-flex; align-items:center; gap:5px; color:#86EFAC;"><span style="width:10px; height:10px; background:#22C55E; border-radius:50%;"></span> 🟢 Green (ಹಸಿರು - No Warning)</span>
    </div>

    <!-- 31 Districts IMD Cards Grid -->
    <div id="imdNowcastContainer" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:14px;">
      <div style="text-align:center; padding:30px; color:#94A3B8; grid-column:1/-1;">IMD ಬೆಂಗಳೂರು ಅಧಿಕೃತ ನೌಕಾಸ್ಟ್ ಮಾಹಿತಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>
    </div>
  </div>
"""

# Place the dashboard right above the FAQ section
if "IMD BENGALURU DISTRICT-WISE NOWCAST" not in content:
    content = content.replace(
        '<div class="sec-head">\n    <div class="sec-title-text">💬 ನಿಮ್ಮ ಏರಿಯಾದ ಹವಾಮಾನ FAQ ಪ್ರಶೋತ್ತರಗಳು',
        imd_nowcast_dashboard_ui + '\n  <div class="sec-head">\n    <div class="sec-title-text">💬 ನಿಮ್ಮ ಏರಿಯಾದ ಹವಾಮಾನ FAQ ಪ್ರಶೋತ್ತರಗಳು'
    )

# 3. Enhance loadImdNowcastWarnings function to render all 31 districts with full IMD Kannada text
enhanced_imd_loader_js = """    async function loadImdNowcastWarnings() {
      const container = document.getElementById('imdNowcastContainer');
      const timeElem = document.getElementById('imdNowcastUpdateTime');
      if (!container) return;

      try {
        const res = await fetch('/api/weather/nowcast?t=' + Date.now(), { cache: 'no-store' });
        if (res.ok) {
          const data = await res.json();
          const districts = data.districts || {};
          const keys = Object.keys(districts);
          
          if (timeElem && data.updated_at) {
            timeElem.textContent = '⏱️ IMD ನವೀಕರಣ: ' + new Date(data.updated_at).toLocaleTimeString('kn-IN', { hour: '2-digit', minute: '2-digit' });
          }

          if (!keys.length) {
            container.innerHTML = `<div style="text-align:center; padding:24px; color:#94A3B8; grid-column:1/-1;">ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಪ್ರಸ್ತುತ ಹವಾಮಾನ ಸ್ಥಿರವಾಗಿದೆ (ಹಸಿರು ವಲಯ).</div>`;
            return;
          }

          container.innerHTML = keys.map(k => {
            const d = districts[k];
            let badgeBg = '#065F46';
            let badgeColor = '#A7F3D0';
            let cardBorder = '#047857';
            let alertClass = 'tag-green';

            if (d.alert_level === 'RED') {
              badgeBg = '#991B1B'; badgeColor = '#FEE2E2'; cardBorder = '#EF4444'; alertClass = 'tag-red';
            } else if (d.alert_level === 'ORANGE') {
              badgeBg = '#9A3412'; badgeColor = '#FFEDD5'; cardBorder = '#F97316'; alertClass = 'tag-orange';
            } else if (d.alert_level === 'YELLOW') {
              badgeBg = '#854D0E'; badgeColor = '#FEF9C3'; cardBorder = '#EAB308'; alertClass = 'tag-yellow';
            }

            return `
              <div style="background:rgba(30,41,59,0.7); border:1.5px solid ${cardBorder}; border-radius:14px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; transition:transform 0.2s;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='none'">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                    <div>
                      <strong style="font-size:16.5px; color:#FFF; display:block;">${d.district_kn}</strong>
                      <span style="font-size:11px; color:#94A3B8;">${d.district_en || ''}</span>
                    </div>
                    <span style="font-size:11px; font-weight:900; background:${badgeBg}; color:${badgeColor}; padding:4px 10px; border-radius:20px; box-shadow:0 2px 6px rgba(0,0,0,0.2);">
                      ${d.severity_icon} ${d.alert_level_kn}
                    </span>
                  </div>
                  <div style="font-size:13px; color:#CBD5E1; line-height:1.5; margin:0 0 12px; background:rgba(15,23,42,0.6); padding:10px; border-radius:8px; border-left:3px solid ${cardBorder};">
                    ${d.warning_info}
                  </div>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; color:#64748B; border-top:1px solid rgba(255,255,255,0.08); padding-top:8px;">
                  <span>🏛️ IMD ಬೆಂಗಳೂರು ನೌಕಾಸ್ಟ್</span>
                  <a href="https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13" target="_blank" style="color:#60A5FA; text-decoration:none; font-weight:700;">ಅಧಿಕೃತ IMD ವೆಬ್‌ಸೈಟ್ ↗</a>
                </div>
              </div>
            `;
          }).join('');
        }
      } catch(e) {
        console.warn('IMD Nowcast load notice:', e);
      }
    }"""

content = re.sub(
    r'async function loadImdNowcastWarnings\(\)\s*\{[\s\S]*?console\.warn\(\'IMD Nowcast load notice:\', e\);\s*\}\s*\}',
    enhanced_imd_loader_js,
    content
)

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_CLEANED_AND_RENDERED_IMD_NOWCAST")
