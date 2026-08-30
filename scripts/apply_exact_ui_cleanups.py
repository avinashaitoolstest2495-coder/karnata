# -*- coding: utf-8 -*-
"""
Karnata — scripts/apply_exact_ui_cleanups.py
1. Removes labels:
   - "🏛️ KSNDMC ಅಧಿಕೃತ ಟೆಲಿಮೆಟ್ರಿ ಡ್ಯಾಶ್ಬೋರ್ಡ್ (https://ksndmc.org/en/WebDashboard)"
   - "ಅಧಿಕೃತ ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ — IMD Bengaluru (Mausam id=13)"
2. Changes time text to: "IMD UPDATE: 10:54 PM" / "IMD UPDATE"
3. Ensures live KSNDMC telemetry (56.5 mm Siddapur, 36.8°C Raichur, 18.2°C Dakshina Kannada)
   and top 5 GP rainfall rankings populate on load without fallback overwrites.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove KSNDMC source pill and clean tags
content = re.sub(
    r'<div style="display:inline-flex; align-items:center; gap:6px; background:#EFF6FF; border:1px solid #BFDBFE; color:#1D4ED8; padding:3px 12px; border-radius:100px; font-size:12px; font-weight:900; margin-bottom:6px;">\s*🏛️ KSNDMC[\s\S]*?</div>',
    '',
    content
)
content = content.replace('🌧️ ಗರಿಷ್ಠ ಮಳೆ ದಾಖಲಾದ ಸ್ಥಳ (KSNDMC)', '🌧️ ಗರಿಷ್ಠ ಮಳೆ ದಾಖಲಾದ ಸ್ಥಳ')
content = content.replace('🔥 ರಾಜ್ಯದ ಗರಿಷ್ಠ ಉಷ್ಣಾಂಶ (KSNDMC)', '🔥 ರಾಜ್ಯದ ಗರಿಷ್ಠ ಉಷ್ಣಾಂಶ')
content = content.replace('❄️ ರಾಜ್ಯದ ಕನಿಷ್ಠ ಉಷ್ಣಾಂಶ (KSNDMC)', '❄️ ರಾಜ್ಯದ ಕನಿಷ್ಠ ಉಷ್ಣಾಂಶ')

# 2. Remove IMD source pill
content = re.sub(
    r'<div style="display:inline-flex; align-items:center; gap:6px; background:#FFE4E6; border:1px solid #FDA4AF; color:#E11D48; padding:4px 14px; border-radius:100px; font-size:12.5px; font-weight:900; margin-bottom:8px;">\s*<span style="width:8px; height:8px; background:#E11D48; border-radius:50%; display:inline-block; box-shadow:0 0 6px #E11D48;"></span>\s*ಅಧಿಕೃತ ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ — IMD Bengaluru \(Mausam id=13\)\s*</div>',
    '',
    content
)

# 3. Change IMD update label in HTML and JS to IMD UPDATE
content = content.replace('id="imdNowcastUpdateTime">⏱️ IMD ನವೀಕರಣ: ಲೈವ್</span>', 'id="imdNowcastUpdateTime">IMD UPDATE</span>')
content = content.replace("'⏱️ IMD ನವೀಕರಣ: ' +", "'IMD UPDATE: ' +")

# 4. Make sure renderSummaryAndCreativeCards is called on load
content = re.sub(
    r'async function loadWeatherData\(\)\s*\{[\s\S]*?loadImdNowcastWarnings\(\);\s*\}',
    """async function loadWeatherData() {
  const currentKey = activeDistrictKey || 'bengaluru_urban';
  try {
    const res = await fetch(`/api/weather?district=${currentKey}&v=${Date.now()}`, { cache: 'no-store' });
    if (res.ok) {
      const data = await res.json();
      if (data && data.success) {
        window.weatherStore = data;
        weatherStore = data;

        const activeDist = data.districts?.[currentKey] || {
          name_kn: data.district_kn,
          key: data.district_key,
          current: data.current,
          hourly_24h: data.hourly_24h,
          forecast_7d: data.forecast_7d,
          forecast: data.forecast_7d
        };

        renderHero(activeDist);
        renderHourlyForecast(activeDist);
        render7DayForecast(activeDist);
        renderFaqAccordion(activeDist);
        renderDistrictsGrid(data);
      }
    }
  } catch(e) {
    console.warn('Live weather API fetch fallback:', e);
  }

  // Load KSNDMC Telemetry & State Extremes
  await renderSummaryAndCreativeCards(window.weatherStore);

  // Load IMD Nowcasts
  await loadImdNowcastWarnings();
}""",
    content
)

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_UI_LABELS_CLEANED_AND_DEPLOYED")
