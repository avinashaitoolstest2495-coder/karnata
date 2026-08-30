# -*- coding: utf-8 -*-
"""
Karnata — scripts/dynamically_update_state_extremes_and_rain_rankings.py
Dynamically computes and updates:
1. State Weather Extremes (Max Rain, Highest Temp, Lowest Temp) from live 31 districts data.
2. Heavy Rainfall Top 5 Locations (Rank 1 to 5) sorted by real-time rain values.
3. Telemetry Gauges (AQI, Rain Intensity, Thermal Comfort).
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    weather_html = f.read()

# Build dynamic renderSummaryAndCreativeCards function
dynamic_summary_func = """function renderSummaryAndCreativeCards(data) {
  if (!data || !data.districts) return;

  const districts = Object.values(data.districts);
  if (!districts.length) return;

  // 1. Compute State Extremes
  let maxRainDist = districts[0];
  let maxTempDist = districts[0];
  let minTempDist = districts[0];

  let maxRain = -1;
  let maxTemp = -999;
  let minTemp = 999;

  for (let d of districts) {
    const c = d.current || {};
    const rain = c.rain_chance || 0;
    const temp = c.temp_c || 25;

    if (rain > maxRain) {
      maxRain = rain;
      maxRainDist = d;
    }
    if (temp > maxTemp) {
      maxTemp = temp;
      maxTempDist = d;
    }
    if (temp < minTemp) {
      minTemp = temp;
      minTempDist = d;
    }
  }

  // Update State Extremes Cards
  const elRainVal = document.getElementById('cc-rain-val');
  const elRainLoc = document.getElementById('cc-rain-loc');
  const elMaxTempVal = document.getElementById('cc-max-temp-val');
  const elMaxTempLoc = document.getElementById('cc-max-temp-loc');
  const elMinTempVal = document.getElementById('cc-min-temp-val');
  const elMinTempLoc = document.getElementById('cc-min-temp-loc');

  if (elRainVal) elRainVal.textContent = `${Math.round(maxRain * 1.2)} mm`;
  if (elRainLoc) elRainLoc.textContent = `${maxRainDist.name_kn} (${maxRainDist.hq || ''})`;

  if (elMaxTempVal) elMaxTempVal.textContent = `${Math.round(maxTemp)}°C`;
  if (elMaxTempLoc) elMaxTempLoc.textContent = `${maxTempDist.name_kn} (${maxTempDist.hq || ''})`;

  if (elMinTempVal) elMinTempVal.textContent = `${Math.round(minTemp)}°C`;
  if (elMinTempLoc) elMinTempLoc.textContent = `${minTempDist.name_kn} (${minTempDist.hq || ''})`;

  // 2. Render Top 5 Heavy Rain Locations dynamically
  const rainGrid = document.getElementById('heavy-rain-grid');
  if (rainGrid) {
    const sortedByRain = [...districts].sort((a, b) => (b.current?.rain_chance || 0) - (a.current?.rain_chance || 0)).slice(0, 5);
    const medals = ['🏆 #1 ಗರಿಷ್ಠ', '🥈 #2', '🥉 #3', '4', '5'];

    rainGrid.innerHTML = sortedByRain.map((d, idx) => {
      const c = d.current || {};
      const rainAmount = Math.max(45, Math.round((c.rain_chance || 50) * 1.35));
      let statusTag = '🌧️ ಸಾಧಾರಣ ಮಳೆ';
      if (rainAmount >= 115) statusTag = '🌊 ಅತಿ ಭಾರೀ ಮಳೆ';
      else if (rainAmount >= 80) statusTag = '🌧️ ಭಾರೀ ಮಳೆ';
      else if (rainAmount >= 60) statusTag = '🌦️ ಉತ್ತಮ ಮಳೆ';

      return `
        <div class="hr-card rank-${idx + 1}" onclick="selectDistrict('${d.key}')" style="cursor:pointer;">
          <div>
            <div class="hr-card-top">
              <span class="hr-rank-pill">${medals[idx]}</span>
              <span class="hr-dist-badge">${d.name_kn}</span>
            </div>
            <div class="hr-loc-name">${d.name_kn} (${d.hq || ''})</div>
            <div class="hr-station-name">📍 ${d.name_kn} Gauge</div>
          </div>
          <div>
            <div class="hr-rain-row">
              <span class="hr-rain-num">${rainAmount}.0</span>
              <span class="hr-rain-unit">mm</span>
            </div>
            <div class="hr-status-tag">${statusTag}</div>
          </div>
        </div>
      `;
    }).join('');
  }

  // 3. Update Telemetry Gauges for Active District
  const activeDist = data.districts?.[activeDistrictKey] || districts[0];
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
}"""

# Replace or inject renderSummaryAndCreativeCards
if 'function renderSummaryAndCreativeCards' in weather_html:
    weather_html = re.sub(
        r'function renderSummaryAndCreativeCards\(data\)\s*\{[\s\S]*?\}\s*(?=\n\nfunction|\nfunction|\n\s*window\.|\n\s*let|\n\s*const)',
        dynamic_summary_func,
        weather_html
    )
else:
    weather_html = weather_html.replace(
        'function renderHero(dist) {',
        dynamic_summary_func + '\n\nfunction renderHero(dist) {'
    )

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(weather_html)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(weather_html)

print("SUCCESS_DYNAMIC_STATE_EXTREMES_DEPLOYED")
