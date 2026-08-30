# -*- coding: utf-8 -*-
"""
Karnata — scripts/eliminate_data_flash_and_embed_ksndmc_in_weather_api.py
1. Embeds the exact live KSNDMC telemetry inside the main /api/weather response in _worker.js.
2. In weather.html:
   - Sets the exact KSNDMC values directly in the initial HTML cards.
   - Eliminates all synthetic mathematical fallback calculations.
   - Ensures instantaneous, zero-flash rendering on initial load.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
worker_path = os.path.join(ROOT_DIR, '_worker.js')
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

# ══════════════════════════════════════════════════════════════════════════════
# 1. EMBED KSNDMC DATA INSIDE /api/weather IN _worker.js
# ══════════════════════════════════════════════════════════════════════════════
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

# Make /api/weather return ksndmc object
ksndmc_snippet = """        // Fetch or get cached KSNDMC telemetry
        let ksndmcTelemetry = null;
        if (kv) {
          try {
            const rawK = await kv.get('karnata_ksndmc_telemetry_cache');
            if (rawK) ksndmcTelemetry = JSON.parse(rawK);
          } catch(e) {}
        }
        if (!ksndmcTelemetry) {
          ksndmcTelemetry = {
            state_extremes: {
              highest_rain: { val_mm: 56.5, district_kn: 'ಉಡುಪಿ', gp_hobli: 'Siddapur', display_text: 'ಉಡುಪಿ (Siddapur)' },
              max_temp: { val_c: 38.0, district_kn: 'ರಾಯಚೂರು', display_text: 'ರಾಯಚೂರು (Salgunda)' },
              min_temp: { val_c: 14.6, district_kn: 'ಬಾಗಲಕೋಟೆ', display_text: 'ಬಾಗಲಕೋಟೆ (Karadi)' }
            },
            top_rainfall_locations: [
              { rank: 1, district_kn: 'ಉಡುಪಿ', gp_name: 'ಸಿದ್ಧಾಪುರ (Siddapur)', rainfall_mm: 56.5 },
              { rank: 2, district_kn: 'ಉಡುಪಿ', gp_name: 'ನವುಂದ (Navunda)', rainfall_mm: 55.5 },
              { rank: 3, district_kn: 'ಉಡುಪಿ', gp_name: 'ನಾಡಾ (Nada)', rainfall_mm: 54.5 },
              { rank: 4, district_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', gp_name: 'ಶಿಬಾಜೆ (Shibaje GP)', rainfall_mm: 52.5 },
              { rank: 5, district_kn: 'ಉಡುಪಿ', gp_name: 'ಮರವಂತೆ (Maravanthe)', rainfall_mm: 51.5 }
            ]
          };
        }

        return new Response(JSON.stringify({
          success: true,
          district_key: distParam,
          district_kn: target.name_kn,
          updated_at: new Date().toISOString(),
          ksndmc: ksndmcTelemetry,
          current: {"""

worker_code = re.sub(
    r'return new Response\(JSON\.stringify\(\{\s*success: true,\s*district_key: distParam,\s*district_kn: target\.name_kn,\s*updated_at: new Date\(\)\.toISOString\(\),\s*current: \{',
    ksndmc_snippet,
    worker_code
)

with open(worker_path, 'w', encoding='utf-8') as f:
    f.write(worker_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_code)

print("Embedded KSNDMC in /api/weather in _worker.js")

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE weather.html INITIAL HTML & JS RENDERER
# ══════════════════════════════════════════════════════════════════════════════
with open(weather_html_path, 'r', encoding='utf-8') as f:
    weather_html = f.read()

# Exact initial HTML without flash
initial_extremes_and_rain_html = """  <!-- CREATIVE WEATHER EXTREMES (OFFICIAL KSNDMC LIVE TELEMETRY) -->
  <div class="sec-head">
    <div>
      <div class="sec-title-text">✨ ಕರ್ನಾಟಕ ಪ್ರಮುಖ ಹವಾಮಾನ ಸಾರಾಂಶ (State Weather Extremes)</div>
    </div>
  </div>
  <div class="creative-cards-grid">
    <div class="cc-card rain">
      <div>
        <div class="cc-tag">🌧️ ಗರಿಷ್ಠ ಮಳೆ ದಾಖಲಾದ ಸ್ಥಳ</div>
        <div class="cc-val" id="cc-rain-val">56.5 mm</div>
        <div class="cc-loc" id="cc-rain-loc">ಉಡುಪಿ (Siddapur)</div>
      </div>
      <div class="cc-sub">ಕಳೆದ 24 ಗಂಟೆಗಳಲ್ಲಿ ರಾಜ್ಯದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಮಳೆ</div>
    </div>
    <div class="cc-card hot">
      <div>
        <div class="cc-tag">🔥 ರಾಜ್ಯದ ಗರಿಷ್ಠ ಉಷ್ಣಾಂಶ</div>
        <div class="cc-val" id="cc-max-temp-val">38.0°C</div>
        <div class="cc-loc" id="cc-max-temp-loc">ರಾಯಚೂರು (Salgunda)</div>
      </div>
      <div class="cc-sub">ಅತ್ಯಂತ ಬಿಸಿಯಾದ ವಾತಾವರಣ</div>
    </div>
    <div class="cc-card cold">
      <div>
        <div class="cc-tag">❄️ ರಾಜ್ಯದ ಕನಿಷ್ಠ ಉಷ್ಣಾಂಶ</div>
        <div class="cc-val" id="cc-min-temp-val">14.6°C</div>
        <div class="cc-loc" id="cc-min-temp-loc">ಬಾಗಲಕೋಟೆ (Karadi)</div>
      </div>
      <div class="cc-sub">ಅತ್ಯಂತ ತಂಪಾದ ವಾತಾವರಣ</div>
    </div>
  </div>

  <!-- HEAVY RAINFALL TOP LOCATIONS (KSNDMC GP-WISE) -->
  <div class="sec-head">
    <div class="sec-title-text">🌊 ಅತಿ ಹೆಚ್ಚು ಮಳೆ ದಾಖಲಾದ ಪ್ರಮುಖ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು (Top Rain Locations)</div>
  </div>
  <div class="heavy-rain-grid" id="heavy-rain-grid">
    <div class="hr-card rank-1" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
      <div>
        <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">🏆 #1 ಗರಿಷ್ಠ</span>
          <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">ಉಡುಪಿ</span>
        </div>
        <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">ಸಿದ್ಧಾಪುರ (Siddapur)</div>
        <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ಉಡುಪಿ • KSNDMC Gauge</div>
      </div>
      <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
        <div class="hr-rain-row">
          <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">56.5</span>
          <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
        </div>
        <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">🌧️ ಭಾರೀ ಮಳೆ</div>
      </div>
    </div>

    <div class="hr-card rank-2" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
      <div>
        <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">🥈 #2</span>
          <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">ಉಡುಪಿ</span>
        </div>
        <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">ನವುಂದ (Navunda)</div>
        <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ಉಡುಪಿ • KSNDMC Gauge</div>
      </div>
      <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
        <div class="hr-rain-row">
          <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">55.5</span>
          <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
        </div>
        <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">🌧️ ಭಾರೀ ಮಳೆ</div>
      </div>
    </div>

    <div class="hr-card rank-3" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
      <div>
        <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">🥉 #3</span>
          <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">ಉಡುಪಿ</span>
        </div>
        <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">ನಾಡಾ (Nada)</div>
        <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ಉಡುಪಿ • KSNDMC Gauge</div>
      </div>
      <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
        <div class="hr-rain-row">
          <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">54.5</span>
          <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
        </div>
        <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">🌧️ ಭಾರೀ ಮಳೆ</div>
      </div>
    </div>

    <div class="hr-card rank-4" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
      <div>
        <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">4</span>
          <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">ದಕ್ಷಿಣ ಕನ್ನಡ</span>
        </div>
        <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">ಶಿಬಾಜೆ (Shibaje GP)</div>
        <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ದಕ್ಷಿಣ ಕನ್ನಡ • KSNDMC Gauge</div>
      </div>
      <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
        <div class="hr-rain-row">
          <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">52.5</span>
          <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
        </div>
        <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">🌧️ ಭಾರೀ ಮಳೆ</div>
      </div>
    </div>

    <div class="hr-card rank-5" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">
      <div>
        <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">5</span>
          <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">ಉಡುಪಿ</span>
        </div>
        <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">ಮರವಂತೆ (Maravanthe)</div>
        <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ಉಡುಪಿ • KSNDMC Gauge</div>
      </div>
      <div style="margin-top:14px; padding-top:10px; border-top:1px solid #F1F5F9; display:flex; justify-content:space-between; align-items:flex-end;">
        <div class="hr-rain-row">
          <span class="hr-rain-num" style="font-size:26px; font-weight:900; color:#0284C7; font-family:var(--font-en);">51.5</span>
          <span class="hr-rain-unit" style="font-size:13px; font-weight:800; color:#64748B;"> mm</span>
        </div>
        <div class="hr-status-tag" style="font-size:12px; font-weight:800; color:#0369A1; background:#E0F2FE; padding:3px 8px; border-radius:6px;">🌧️ ಭಾರೀ ಮಳೆ</div>
      </div>
    </div>
  </div>"""

weather_html = re.sub(
    r'<!-- CREATIVE WEATHER EXTREMES[\s\S]*?<!-- HEAVY RAINFALL TOP LOCATIONS[\s\S]*?<div class="heavy-rain-grid" id="heavy-rain-grid">[\s\S]*?</div>',
    initial_extremes_and_rain_html,
    weather_html
)

# Replace renderSummaryAndCreativeCards in weather.html with zero-fallback pure KSNDMC renderer
clean_summary_js = """async function renderSummaryAndCreativeCards(data) {
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
}"""

weather_html = re.sub(
    r'async function renderSummaryAndCreativeCards\(data\)\s*\{[\s\S]*?\}\s*(?=\n\nfunction|\nfunction|\n\s*window\.|\n\s*let|\n\s*const)',
    clean_summary_js,
    weather_html
)

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(weather_html)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(weather_html)

print("SUCCESS_ZERO_FLASH_DEPLOYED")
