# -*- coding: utf-8 -*-
"""
Karnata — scripts/replace_old_renderSummaryAndCreativeCards.py
Replaces the old renderSummaryAndCreativeCards function at line 3288 in weather.html with pure KSNDMC logic.
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_func = """async function renderSummaryAndCreativeCards(data) {
  const ksndmc = data?.ksndmc || null;
  
  if (ksndmc && ksndmc.state_extremes) {
    applyKsndmcDataToDOM(ksndmc);
  } else {
    try {
      const res = await fetch('/api/ksndmc/telemetry?t=' + Date.now(), { cache: 'no-store' });
      if (res.ok) {
        const liveK = await res.json();
        if (liveK && liveK.state_extremes) {
          applyKsndmcDataToDOM(liveK);
        }
      }
    } catch(e) {
      console.warn('KSNDMC fetch notice:', e);
    }
  }

  // Active District Telemetry Gauges
  if (data && data.districts) {
    const activeDist = data.districts[activeDistrictKey] || Object.values(data.districts)[0];
    if (activeDist) {
      const cur = activeDist.current || {};
      const aqi = getDistrictAQI(activeDist.key);

      const elAqiVal = document.getElementById('gauge-aqi-val');
      const elAqiBar = document.getElementById('gauge-aqi-bar');
      const elRainGaugeVal = document.getElementById('gauge-rain-val');
      const elRainGaugeBar = document.getElementById('gauge-rain-bar');
      const elTempGaugeVal = document.getElementById('gauge-temp-val');
      const elTempGaugeBar = document.getElementById('gauge-temp-bar');

      if (elAqiVal) elAqiVal.textContent = aqi.val;
      if (elAqiBar) elAqiBar.style.width = `${Math.min(100, Math.round((aqi.val / 200) * 100))}%`;

      if (elRainGaugeVal) elRainGaugeVal.textContent = `${cur.rain_chance || 0}%`;
      if (elRainGaugeBar) elRainGaugeBar.style.width = `${cur.rain_chance || 0}%`;

      if (elTempGaugeVal) elTempGaugeVal.textContent = `${Math.round(cur.temp_c || 25)}°C`;
      if (elTempGaugeBar) elTempGaugeBar.style.width = `${Math.min(100, Math.round((cur.temp_c / 45) * 100))}%`;
    }
  }
}

function applyKsndmcDataToDOM(ksndmc) {
  const ext = ksndmc.state_extremes || {};
  const hRain = ext.highest_rain || {};
  const maxT = ext.max_temp || {};
  const minT = ext.min_temp || {};

  const elRainVal = document.getElementById('cc-rain-val');
  const elRainLoc = document.getElementById('cc-rain-loc');
  const elMaxTempVal = document.getElementById('cc-max-temp-val');
  const elMaxTempLoc = document.getElementById('cc-max-temp-loc');
  const elMinTempVal = document.getElementById('cc-min-temp-val');
  const elMinTempLoc = document.getElementById('cc-min-temp-loc');

  if (elRainVal && hRain.val_mm) elRainVal.textContent = `${hRain.val_mm} mm`;
  if (elRainLoc) elRainLoc.textContent = hRain.display_text || `${hRain.district_kn || 'ಉಡುಪಿ'} (${hRain.gp_hobli || 'Siddapur'})`;

  if (elMaxTempVal && maxT.val_c) elMaxTempVal.textContent = `${maxT.val_c}°C`;
  if (elMaxTempLoc) elMaxTempLoc.textContent = maxT.display_text || `${maxT.district_kn || 'ರಾಯಚೂರು'}`;

  if (elMinTempVal && minT.val_c) elMinTempVal.textContent = `${minT.val_c}°C`;
  if (elMinTempLoc) elMinTempLoc.textContent = minT.display_text || `${minT.district_kn || 'ಬಾಗಲಕೋಟೆ'}`;

  const rainGrid = document.getElementById('heavy-rain-grid');
  const topLocations = ksndmc.top_rainfall_locations || [];
  if (rainGrid && topLocations.length) {
    const medals = ['🏆 #1 ಗರಿಷ್ಠ', '🥈 #2', '🥉 #3', '4', '5'];
    rainGrid.innerHTML = topLocations.slice(0, 5).map((loc, idx) => {
      const rainAmount = loc.rainfall_mm || 0;
      let statusTag = '🌧️ ಸಾಧಾರಣ ಮಳೆ';
      if (rainAmount >= 64.5) statusTag = '🌊 ಅತಿ ಭಾರೀ ಮಳೆ';
      else if (rainAmount >= 35.5) statusTag = '🌧️ ಭಾರೀ ಮಳೆ';
      else if (rainAmount >= 15.0) statusTag = '🌦️ ಉತ್ತಮ ಮಳೆ';

      return `
        <div class="hr-card rank-${idx + 1}" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
          <div>
            <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">${medals[idx] || (idx + 1)}</span>
              <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">${loc.district_kn || loc.district_en}</span>
            </div>
            <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">${loc.gp_name}</div>
            <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ${loc.district_kn || loc.district_en} • KSNDMC Gauge</div>
          </div>
          <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
            <div class="hr-rain-row">
              <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">${rainAmount.toFixed(1)}</span>
              <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
            </div>
            <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">${statusTag}</div>
          </div>
        </div>
      `;
    }).join('');
  }
}
"""

# Find lines containing renderSummaryAndCreativeCards
start_idx = -1
end_idx = -1

for i, l in enumerate(lines):
    if 'function renderSummaryAndCreativeCards(data)' in l or 'async function renderSummaryAndCreativeCards(data)' in l:
        start_idx = i
    if start_idx != -1 and i > start_idx and 'function renderRealKSNDMCTweets' in l:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx] = [new_func + '\n']
    print(f"Replaced lines {start_idx+1} to {end_idx+1}")

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("SUCCESS_OLD_FUNCTION_REPLACED")
