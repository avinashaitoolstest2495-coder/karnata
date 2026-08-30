# -*- coding: utf-8 -*-
"""
Karnata — scripts/inject_weather_guide_article_and_verify.py
Injects the requested Agro-Meteorology & Vedic Rain Science guide article into weather.html.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

article_html = """  <!-- ══════════════════════════════════════════════════════════════════════
       AGRO-METEOROLOGY, 27 RAIN NAKSHATRAS & VEDIC RAIN SCIENCE GUIDE
       ══════════════════════════════════════════════════════════════════════ -->
  <article class="weather-guide-container font-kannada" style="line-height: 1.85; color: #1e293b; font-size: 16px; margin-top: 40px; padding: 30px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">

    <!-- HERO BANNER -->
    <header style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #075985 100%); color: #ffffff; padding: 35px 25px; border-radius: 12px; margin-bottom: 30px; text-align: center;">
      <span style="background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 20px; font-size: 13px; letter-spacing: 1px; text-transform: uppercase;">Agro-Meteorology & Vedic Rain Science</span>
      <h1 style="font-size: 30px; margin: 15px 0 10px 0; font-weight: 800; line-height: 1.3;">ಕರ್ನಾಟಕ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ, 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು, ವಾಹನಗಳು ಮತ್ತು ಕೃಷಿ ಮಳೆ ವಿಜ್ಞಾನದ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶಿ</h1>
      <p style="color: #e0f2fe; font-size: 15px; margin: 0; max-width: 800px; margin-left: auto; margin-right: auto;">ಸಾಂಪ್ರದಾಯಿಕ ಮಳೆ ನಕ್ಷತ್ರ ಗಾದೆಗಳು &bull; ಮುಂಗಾರು-ಹಿಂಗಾರು ಚಲನವಲನ &bull; KSNDMC-IMD ಲೈವ್ ಹವಾಮಾನ ತಂತ್ರಜ್ಞಾನ</p>
    </header>

    <!-- SECTION 1 -->
    <section>
      <h2 style="font-size: 22px; color: #0f172a; margin-top: 25px; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">1. ಪೀಠಿಕೆ: ಕರ್ನಾಟಕದ ವೈವಿಧ್ಯಮಯ ಹವಾಮಾನ ಮತ್ತು ಕೃಷಿ ಪರಂಪರೆ</h2>
      <p>ಕರ್ನಾಟಕವು ಭೌಗೋಳಿಕವಾಗಿ ಅತ್ಯಂತ ವೈವಿಧ್ಯಮಯ ಹವಾಮಾನ ಲಕ್ಷಣಗಳನ್ನು ಹೊಂದಿರುವ ರಾಜ್ಯವಾಗಿದೆ. ಅರಬ್ಬಿ ಸಮುದ್ರದ ತೀರದಿಂದ ಪ್ರಾರಂಭವಾಗಿ ದಟ್ಟ ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ಮಳೆಕಾಡುಗಳು, ಹಚ್ಚಹಸಿರಿನ ಮಲೆನಾಡು, ಫಲವತ್ತಾದ ಕಾವೇರಿ ಕಣಿವೆಯ ದಕ್ಷಿಣ ಬಯಲು ಸೀಮೆ ಮತ್ತು ಒಣಹವೆಯ ಉತ್ತರ ಕರ್ನಾಟಕದ ಕಪ್ಪು ಮಣ್ಣಿನ ವಿಶಾಲ ಬಯಲು ಸೀಮೆಯವರೆಗೆ ರಾಜ್ಯದ ಹವಾಮಾನವು ಕ್ಷಣಕ್ಷಣಕ್ಕೂ ಭಿನ್ನ ಸ್ವರೂಪವನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ಕರ್ನಾಟಕದ ಕೃಷಿ ಆರ್ಥಿಕತೆ, ಜಲಾಶಯಗಳ ಒಳಹರಿವು ಮತ್ತು ರೈತರ ಬಿತ್ತನೆ ಚಟುವಟಿಕೆಗಳು ಸಂಪೂರ್ಣವಾಗಿ ಮಳೆಯ ಆಗಮನ ಮತ್ತು ಹಂಚಿಕೆಯ ಮೇಲೆಯೇ ಅವಲಂಬಿತವಾಗಿವೆ.</p>

      <p>ನಮ್ಮ ಪೂರ್ವಜರು ಮತ್ತು ರೈತ ಸಮುದಾಯವು ಆಧುನಿಕ ಉಪಗ್ರಹಗಳು ಹಾಗೂ ಹವಾಮಾನ ರಾಡಾರ್ಗಳು ಬರುವ ಮುಂಚೆಯೇ ಸೂರ್ಯನ ಸಂಚಾರ ಮತ್ತು <strong>27 ಮಳೆ ನಕ್ಷತ್ರಗಳ (27 Rain Nakshatras)</strong> ಆಧಾರದ ಮೇಲೆ ಮಳೆಯ ಪ್ರಮಾಣ, ಗಾಳಿಯ ದಿಕ್ಕು ಮತ್ತು ಬಿತ್ತನೆಯ ಮುಹೂರ್ತವನ್ನು ಅಚ್ಚುಕಟ್ಟಾಗಿ ಲೆಕ್ಕ ಹಾಕುತ್ತಿದ್ದರು. ಇಂದು ಆಧುನಿಕ ವಿಜ್ಞಾನದ ಡಾಪ್ಲರ್ ರಾಡಾರ್ ಮುನ್ಸೂಚನೆಗಳ ಜೊತೆಗೆ ನಮ್ಮ ಪ್ರಾಚೀನ ಮಳೆ ನಕ್ಷತ್ರಗಳ ಜ್ಞಾನವನ್ನು ಸಂಯೋಜಿಸಿ ನೋಡುವುದು ಕೃಷಿಕರಿಗೆ ಮತ್ತು ಪ್ರಕೃತಿ ಪ್ರಿಯರಿಗೆ ಅತ್ಯಂತ ಉಪಯುಕ್ತವಾಗಿದೆ.</p>
    </section>

    <!-- SECTION 2: 27 RAIN NAKSHATRAS (CORE ATTRACTION) -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">2. ಕರ್ನಾಟಕದ 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು, ವಾಹನಗಳು ಮತ್ತು ಜಾನಪದ ಗಾದೆಗಳು (Complete Rain Nakshatras Guide)</h2>
      <p>ವೈದಿಕ ಖಗೋಳ ಪದ್ಧತಿಯಂತೆ ಸೂರ್ಯನು ಒಂದೊಂದು ನಕ್ಷತ್ರದಲ್ಲಿ ಸುಮಾರು 13 ರಿಂದ 14 ದಿನಗಳ ಕಾಲ ಸಂಚರಿಸುತ್ತಾನೆ. ಸೂರ್ಯನು ನಿರ್ದಿಷ್ಟ ನಕ್ಷತ್ರಕ್ಕೆ ಪ್ರವೇಶಿಸಿದಾಗ ಉಂಟಾಗುವ ಹವಾಮಾನ ಬದಲಾವಣೆ ಮತ್ತು ಮಳೆಯನ್ನು ಆಯಾ 'ಮಳೆ ನಕ್ಷತ್ರ' ಎನ್ನಲಾಗುತ್ತದೆ. ವರ್ಷದ 27 ಮಳೆ ನಕ್ಷತ್ರಗಳ ಸಂಪೂರ್ಣ ಪಟ್ಟಿ, ಅವುಗಳ ಪ್ರವೇಶ ಸಮಯ ಮತ್ತು ಅವುಗಳ ಹಿಂದಿರುವ ಜನಪ್ರಿಯ ಗಾದೆ ಮಾತುಗಳ ವಿವರ ಇಲ್ಲಿದೆ:</p>

      <div style="overflow-x: auto; margin-top: 20px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 14px; background: #ffffff;">
          <thead>
            <tr style="background: linear-gradient(90deg, #0f172a, #1e293b); color: #ffffff; text-align: left;">
              <th style="padding: 12px; border: 1px solid #334155;">ನಕ್ಷತ್ರ ಸಂಖ್ಯೆ & ಹೆಸರು</th>
              <th style="padding: 12px; border: 1px solid #334155;">ಸರಿಸುಮಾರು ಇಂಗ್ಲಿಷ್ ದಿನಾಂಕ</th>
              <th style="padding: 12px; border: 1px solid #334155;">ಋತುಮಾನ / ಮಳೆಯ ವಿಧ</th>
              <th style="padding: 12px; border: 1px solid #334155;">ಜನಪ್ರಿಯ ಮಳೆ ಗಾದೆ ಮತ್ತು ರೈತರ ಅನುಭವ ಸತ್ಯ</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #f8fafc;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #0369a1;">1. ಅಶ್ವಿನಿ (Aswini)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಏಪ್ರಿಲ್ 14 - ಏಪ್ರಿಲ್ 27</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಬೇಸಿಗೆ ಮಳೆ / ಮುಂಗಾರಿನ ಮುನ್ಸೂಚನೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಅಶ್ವಿನಿ ಮಳೆ ಬಿದ್ದರೆ ಅಕ್ಕಿ ಕಾಳು ಪುಕ್ಕಟೆ"</em> — ಬೇಸಿಗೆಯ ಮೊದಲ ಮಳೆ ಬಿದ್ದರೆ ಭೂಮಿ ತಂಪಾಗಿ ಉತ್ತಮ ಮುಂಗಾರಿಗೆ ನಾಂದಿಯಾಗುತ್ತದೆ.</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #0369a1;">2. ಭರಣಿ (Bharani)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಏಪ್ರಿಲ್ 27 - ಮೇ 11</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಗುಡುಗು-ಮಿಂಚಿನ ಅಕಾಲಿಕ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಭರಣಿ ಮಳೆ ಬಂದರೆ ಧರಣಿ ತಣಿಯುತ್ತದೆ"</em> — ರಭಸದ ಗಾಳಿ-ಗುಡುಗಿನ ಮಳೆ, ಭೂಮಿಯ ಕಾವನ್ನು ಇಳಿಸಿ ಉಳುಮೆಗೆ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ.</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #0369a1;">3. ಕೃತಿಕಾ (Krittika)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮೇ 11 - ಮೇ 25</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕಾರ್ತೆ ಮಳೆ / ಮಾವಿನ ಮಳೆ (Mango Showers)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಕೃತಿಕಾ ಮಳೆಗೆ ಕೆರೆ ತುಂಬಿದರೆ ಕುರಿ ಕಾಯೋನು ಕೂಡ ಬದುಕಿಯಾನು"</em> — ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಿಗೆ, ಮಾವಿನ ಇಳುವರಿಗೆ ಅತ್ಯಂತ ಶ್ರೇಷ್ಠ.</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #0369a1;">4. ರೋಹಿಣಿ (Rohini)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮೇ 25 - ಜೂನ್ 08</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮುಂಗಾರು ಪ್ರವೇಶದ ಪೂರ್ವ ಸಿದ್ಧತೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ರೋಹಿಣಿ ಮಳೆ ಓಣಿ ತುಂಬ"</em> ಅಥವಾ <em>"ರೋಹಿಣಿ ಮಳೆಗೆ ಓಣಿಯೆಲ್ಲ ಕೆಸರು"</em> — ವ್ಯಾಪಕವಾಗಿ ಸುರಿದು ಹಳ್ಳ-ಕೊಳ್ಳಗಳಿಗೆ ನೀರು ತರುತ್ತದೆ.</td>
            </tr>
            <tr style="background: #ecfdf5;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #047857;">5. ಮೃಗಶಿರಾ (Mrigashira)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜೂನ್ 08 - ಜೂನ್ 22</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ನೈಋತ್ಯ ಮುಂಗಾರಿನ ಆರಂಭ (Monsoon Onset)</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಮೃಗಶಿರೆಯ ಮಳೆ ಮಣ್ಣು ಹದ"</em> — ರಾಜ್ಯಾದ್ಯಂತ ಮುಂಗಾರು ಬಿತ್ತನೆಗೆ ಅತ್ಯಂತ ಶುಭದಾಯಕ ನಕ್ಷತ್ರ.</td>
            </tr>
            <tr style="background: #ecfdf5;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #047857;">6. ಆರಿದ್ರಾ (Aridra)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜೂನ್ 22 - ಜುಲೈ 06</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜೋರು ಮುಂಗಾರು ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಆರಿದ್ರಾ ಮಳೆ ಆದ್ರೂ ಉಂಟು ಹೋದ್ರೂ ಉಂಟು"</em> — ನದಿಗಳಲ್ಲಿ ನೀರಿನ ಹರಿವು ಹೆಚ್ಚಾಗಿ ಅಣೆಕಟ್ಟುಗಳಿಗೆ ಒಳಹರಿವು ಆರಂಭ.</td>
            </tr>
            <tr style="background: #ecfdf5;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #047857;">7. ಪುನರ್ವಸು (Punarvasu)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜುಲೈ 06 - ಜುಲೈ 20</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮಲೆನಾಡು & ಕರಾವಳಿ ಅಬ್ಬರ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಪುನರ್ವಸು ಮಳೆಗೆ ಪುನಃ ನೆರೆ"</em> — ಭತ್ತದ ನಾಟಿಗೆ ಮತ್ತು ಕೆರೆ ತುಂಬಲು ಸೂಕ್ತವಾದ ನಿರಂತರ ಮಳೆ.</td>
            </tr>
            <tr style="background: #ecfdf5;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #047857;">8. ಪುಷ್ಯ (Pushya)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜುಲೈ 20 - ಆಗಸ್ಟ್ 03</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಪೀಕ್ ಮುಂಗಾರು ಮಳೆ (Peak Monsoon)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಪುಷ್ಯದ ಮಳೆ ಪೋಷಿಸಿದಂತೆ"</em> — ಬೆಳೆಗಳು ಹಚ್ಚಹಸಿರಾಗಿ ಬೆಳೆಯಲು ಸತತ ಜಿಟಿಜಿಟಿ ಮಳೆ.</td>
            </tr>
            <tr style="background: #ecfdf5;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #047857;">9. ಆಶ್ಲೇಷ (Ashlesha)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಆಗಸ್ಟ್ 03 - ಆಗಸ್ಟ್ 17</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಭಾರೀ ಪ್ರವಾಹದ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಆಶ್ಲೇಷ ಮಳೆ ಅಪ್ಪಳಿಸಿ ಸುರಿಯುತ್ತದೆ"</em> — ಬೆಟ್ಟಗುಡ್ಡಗಳಲ್ಲಿ ಜಲಪಾತಗಳು ಮೈದುಂಬಿ ಹರಿಯುವ ಕಾಲ.</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #b45309;">10. ಮಘಾ (Magha)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಆಗಸ್ಟ್ 17 - ಆಗಸ್ಟ್ 31</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ದೊಡ್ಡ ಹನಿಗಳ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಮಘಾ ಮಳೆ ಬಂದರೆ ಮಗನಂತೆ ಸಾಕುವುದು"</em> — ತಾಯಿ ಮಗನನ್ನು ಪೋಷಿಸುವಂತೆ ಬೆಳೆಗಳನ್ನು ರಕ್ಷಿಸುವ ಜೀವಜಲ.</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #b45309;">11. ಹುಬ್ಬಾ / ಪುಬ್ಬಾ (Pubba)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಆಗಸ್ಟ್ 31 - ಸೆಪ್ಟೆಂಬರ್ 13</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ರಾಗಿ ಮತ್ತು ಜೋಳದ ತೆನೆ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಹುಬ್ಬಾ ಮಳೆ ಬಂದರೆ ಹುಲ್ಲು ಕೂಡ ಕಾಳು ಕಟ್ಟುತ್ತದೆ"</em> — ದವಸ ಧಾನ್ಯಗಳಲ್ಲಿ ಕಾಳು ತುಂಬಲು ಅತ್ಯಮೂಲ್ಯ ಮಳೆ.</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #b45309;">12. ಉತ್ತರಾ (Uttara)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಸೆಪ್ಟೆಂಬರ್ 13 - ಸೆಪ್ಟೆಂಬರ್ 27</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮುಂಗಾರಿನ ಅಂತಿಮ ಹಂತ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಉತ್ತರಾ ಮಳೆ ಊಟಕ್ಕೆ ಆಸರೆ"</em> — ಮುಂಗಾರು ಬೆಳೆಗಳ ಕೊಯ್ಲಿಗೆ ಹಾಗೂ ಹಿಂಗಾರು ಭೂಮಿ ಹದಕ್ಕೆ ಸಹಕಾರಿ.</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1d4ed8;">13. ಹಸ್ತಾ (Hasta)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಸೆಪ್ಟೆಂಬರ್ 27 - ಅಕ್ಟೋಬರ್ 11</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಹಿಂಗಾರು ಮಳೆಯ ಆರಂಭ (Northeast Monsoon)</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಹಸ್ತಾ ಮಳೆ ಹೋದರೆ ಕೈ ಕಟ್ಟಿ ಕುಳಿತುಕೊ"</em> — ಹಸ್ತಾ ಮಳೆ ಕೈಕೊಟ್ಟರೆ ಉತ್ತರ ಕರ್ನಾಟಕದ ಹಿಂಗಾರು ಬೆಳೆ ಸಂಕಷ್ಟಕ್ಕೆ ಸಿಲುಕುತ್ತದೆ.</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1d4ed8;">14. ಚಿತ್ತಾ (Chitta)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅಕ್ಟೋಬರ್ 11 - ಅಕ್ಟೋಬರ್ 24</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಸಂಜೆ ಗುಡುಗು ಸಹಿತ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಚಿತ್ತಾ ಮಳೆ ಬಂದರೆ ಪುಟ್ಟಕ್ಕನೂ ಬದುಕ್ಯಾಳು"</em> — ಕಡಲೆ, ಜೋಳ, ಸೂರ್ಯಕಾಂತಿ ಬಿತ್ತನೆಗೆ ಜೀವನಾಡಿ.</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1d4ed8;">15. ಸ್ವಾತಿ (Swati)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅಕ್ಟೋಬರ್ 24 - ನವೆಂಬರ್ 06</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮುತ್ತಿನ ಮಳೆ / ಹಿಂಗಾರು ಅಬ್ಬರ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ಸ್ವಾತಿ ಮಳೆ ಮುತ್ತು"</em> — ಸ್ವಾತಿ ಮಳೆಯ ಹನಿ ಸಿಂಪಿ ಒಳಗೆ ಬಿದ್ದರೆ ಮುತ್ತಾಗುತ್ತದೆ ಎಂಬ ಪೌರಾಣಿಕ ಪ್ರತೀತಿ.</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1d4ed8;">16. ವಿಶಾಖಾ (Vishakha)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ನವೆಂಬರ್ 06 - ನವೆಂಬರ್ 19</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಹಿಂಗಾರಿನ ಇಳಿಮುಖ ಮಳೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><em>"ವಿಶಾಖಾ ಮಳೆಗೆ ವಿಷಾದವಿಲ್ಲ"</em> — ಚಳಿಗಾಲದ ಆಗಮನಕ್ಕೆ ಮುನ್ನ ಬೀಳುವ ಕೊನೆಯ ಹಂತದ ಮಳೆ.</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #64748b;">17. ಅನೂರಾಧ (Anuradha)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ನವೆಂಬರ್ 19 - ಡಿಸೆಂಬರ್ 02</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಚಳಿಗಾಲದ ಮಳೆ / ಇಬ್ಬನಿ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಬಂಗಾಳ ಕೊಲ್ಲಿಯ ಚಂಡಮಾರುತಗಳಿಂದ ದಕ್ಷಿಣ ಒಳನಾಡಿನಲ್ಲಿ ಆಗಾಗ್ಗೆ ತುಂತುರು ಮಳೆ.</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #64748b;">18 ರಿಂದ 27. ಜ್ಯೇಷ್ಠಾದಿಂದ ರೇವತಿವರೆಗೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಡಿಸೆಂಬರ್ ನಿಂದ ಏಪ್ರಿಲ್ ವರೆಗೆ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಶುಷ್ಕ ಹವೆ / ಬೇಸಿಗೆ ಕಾಲ</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮೂಲ, ಪೂರ್ವಾಷಾಢ, ಉತ್ತರಾಷಾಢ, ಶ್ರವಣ, ಧನಿಷ್ಠಾ, ಶತಭಿಷಾ, ಪೂರ್ವಾಭಾದ್ರ, ಉತ್ತರಾಭಾದ್ರ, ರೇವತಿ — ಶುಷ್ಕತೆ ಮತ್ತು ತಾಪಮಾನ ಏರಿಕೆಯ ಕಾಲ.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- VAHANA CONCEPT CARD -->
      <div style="background: #fefce8; border: 1px solid #fef08a; padding: 20px; border-radius: 10px; margin-top: 20px;">
        <h3 style="color: #854d0e; margin-top: 0; font-size: 17px;">ಮಳೆ ನಕ್ಷತ್ರಗಳ ವಾಹನಗಳು (Nakshatra Vahanas Explained):</h3>
        <p style="font-size: 14px; margin-bottom: 8px;">ಸೂರ್ಯನು ನಕ್ಷತ್ರಕ್ಕೆ ಪ್ರವೇಶಿಸುವ ದಿನದ ವಾರ ಮತ್ತು ತಿಥಿಯ ಆಧಾರದ ಮೇಲೆ ಆ ನಕ್ಷತ್ರಕ್ಕೆ ನಿರ್ದಿಷ್ಟ ವಾಹನವನ್ನು ಪಂಚಾಂಗದಲ್ಲಿ ನಿಗದಿಪಡಿಸಲಾಗುತ್ತದೆ. ಜಾನಪದ ನಂಬಿಕೆಯ ಪ್ರಕಾರ:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-size: 13px; color: #713f12;">
          <div>&bull; <strong>ಆನೆ ವಾಹನ (Elephant):</strong> ಭಾರಿ ವರ್ಷಧಾರೆ, ಪ್ರವಾಹ.</div>
          <div>&bull; <strong>ಕುದುರೆ ವಾಹನ (Horse):</strong> ವೇಗದ ಗಾಳಿ ಸಹಿತ ಮಧ್ಯಮ ಮಳೆ.</div>
          <div>&bull; <strong>ಕತ್ತೆ ವಾಹನ (Donkey):</strong> ಅಲ್ಪ ಮಳೆ, ತಡವಾದ ಮೋಡಗಳು.</div>
          <div>&bull; <strong>ಮಂಡೂಕ / ಕಪ್ಪೆ (Frog):</strong> ನಿರಂತರ ಹಿತಕರ ಜಿಟಿಜಿಟಿ ಮಳೆ.</div>
          <div>&bull; <strong>ನವಿಲು ವಾಹನ (Peacock):</strong> ಸಾಧಾರಣ ಮಳೆ, ಶುಭದಾಯಕ.</div>
          <div>&bull; <strong>ನರಿ / ನಾಯಿ ವಾಹನ (Fox/Dog):</strong> ಗಾಳಿಯ ಆರ್ಭಟ ಹೆಚ್ಚು, ಮಳೆ ಕಡಿಮೆ.</div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: AGRO-CLIMATIC ZONES -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">3. ಕರ್ನಾಟಕದ 3 ಪ್ರಮುಖ ಕೃಷಿ-ಹವಾಮಾನ ವಲಯಗಳು (Agro-Climatic Zones)</h2>
      <p>ಮಳೆ ಮತ್ತು ತಾಪಮಾನದ ವಿತರಣೆಯ ಆಧಾರದ ಮೇಲೆ ಕರ್ನಾಟಕವನ್ನು ಪ್ರಮುಖವಾಗಿ 3 ವಿಶಾಲ ವಲಯಗಳಾಗಿ ವಿಂಗಡಿಸಲಾಗಿದೆ:</p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 20px 0;">
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 18px; border-radius: 8px;">
          <h4 style="color: #166534; margin-top: 0; font-size: 17px;">1. ಕರಾವಳಿ & ಮಲೆನಾಡು ವಲಯ (Coastal & Malnad)</h4>
          <p style="font-size: 14px; margin-bottom: 5px;"><strong>ಜಿಲ್ಲೆಗಳು:</strong> ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ, ಉತ್ತರ ಕನ್ನಡ, ಶಿವಮೊಗ್ಗ, ಚಿಕ್ಕಮಗಳೂರು, ಕೊಡಗು, ಹಾಸನದ ಪಶ್ಚಿಮ ಭಾಗ.</p>
          <p style="font-size: 13px; color: #15803d;"><strong>ವಾರ್ಷಿಕ ಮಳೆ:</strong> 2,500 ಮಿ.ಮೀ ನಿಂದ 4,500+ ಮಿ.ಮೀ. ಆಗುಂಬೆ ಮತ್ತು ಹುಲಿಕಲ್ ಕರ್ನಾಟಕದ 'ಚಿರಾಪುಂಜಿ' ಎಂದೇ ಪ್ರಸಿದ್ಧ. ಅಡಿಕೆ, ಕಾಫಿ, ರಬ್ಬರ್, ತೆಂಗು ಮತ್ತು ಭತ್ತ ಪ್ರಮುಖ ಬೆಳೆಗಳು.</p>
        </div>

        <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 18px; border-radius: 8px;">
          <h4 style="color: #92400e; margin-top: 0; font-size: 17px;">2. ಉತ್ತರ ಒಳನಾಡು ವಲಯ (North Interior Dry Zone)</h4>
          <p style="font-size: 14px; margin-bottom: 5px;"><strong>ಜಿಲ್ಲೆಗಳು:</strong> ಬೆಳಗಾವಿ, ವಿಜಯಪುರ, ಬಾಗಲಕೋಟೆ, ಕಲಬುರಗಿ, ಬೀದರ್, ಯಾದಗಿರಿ, ರಾಯಚೂರು, ಕೊಪ್ಪಳ, ಗದಗ, ಹಾವೇರಿ, ಬಳ್ಳಾರಿ, ವಿಜಯನಗರ.</p>
          <p style="font-size: 13px; color: #b45309;"><strong>ವಾರ್ಷಿಕ ಮಳೆ:</strong> 500 ಮಿ.ಮೀ ನಿಂದ 750 ಮಿ.ಮೀ (ಶುಷ್ಕ & ಅರೆ-ಶುಷ್ಕ). ಕಪ್ಪು ಮಣ್ಣಿನ ಪ್ರದೇಶ. ತೊಗರಿ, ಕಡಲೆ, ಹತ್ತಿ, ಜೋಳ, ಸೂರ್ಯಕಾಂತಿ, ಮೆಣಸಿನಕಾಯಿ ಪ್ರಮುಖ ಬೆಳೆಗಳು.</p>
        </div>

        <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 18px; border-radius: 8px;">
          <h4 style="color: #1e40af; margin-top: 0; font-size: 17px;">3. ದಕ್ಷಿಣ ಒಳನಾಡು ವಲಯ (South Interior Zone)</h4>
          <p style="font-size: 14px; margin-bottom: 5px;"><strong>ಜಿಲ್ಲೆಗಳು:</strong> ಬೆಂಗಳೂರು ನಗರ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, ಮಂಡ್ಯ, ಮೈಸೂರು, ಚಾಮರಾಜನಗರ, ರಾಮನಗರ, ತುಮಕೂರು, ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ.</p>
          <p style="font-size: 13px; color: #1d4ed8;"><strong>ವಾರ್ಷಿಕ ಮಳೆ:</strong> 650 ಮಿ.ಮೀ ನಿಂದ 950 ಮಿ.ಮೀ. ಕೆಂಪು ಮಣ್ಣಿನ ಪ್ರದೇಶ. ರಾಗಿ, ಭತ್ತ, ಕಬ್ಬು, ರೇಷ್ಮೆ, ಮಾವು, ದ್ರಾಕ್ಷಿ ಮತ್ತು ತರಕಾರಿ ಬೆಳೆಗಳು ಪ್ರಮುಖವಾಗಿವೆ.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 4: MONSOON MECHANICS -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">4. ಮುಂಗಾರು vs ಹಿಂಗಾರು ಮಳೆ ವಿಜ್ಞಾನ (Monsoon Mechanics)</h2>
      <p>ಕರ್ನಾಟಕದ ಒಟ್ಟು ವಾರ್ಷಿಕ ಮಳೆಯು ಎರಡು ಪ್ರತ್ಯೇಕ ಮಾನ್ಸೂನ್ ಮಾರುತಗಳ ವ್ಯವಸ್ಥೆಯಿಂದ ಬರುತ್ತದೆ:</p>

      <div style="overflow-x: auto; margin-top: 15px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
          <thead>
            <tr style="background: #0f172a; color: #ffffff; text-align: left;">
              <th style="padding: 10px; border: 1px solid #cbd5e1;">ಮಾನದಂಡ</th>
              <th style="padding: 10px; border: 1px solid #cbd5e1;">ನೈಋತ್ಯ ಮುಂಗಾರು (Southwest Monsoon)</th>
              <th style="padding: 10px; border: 1px solid #cbd5e1;">ಈಶಾನ್ಯ ಹಿಂಗಾರು (Northeast Monsoon)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಸಮಯಾವಧಿ</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಜೂನ್ನಿಂದ ಸೆಪ್ಟೆಂಬರ್ವರೆಗೆ (4 ತಿಂಗಳು)</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅಕ್ಟೋಬರ್ನಿಂದ ಡಿಸೆಂಬರ್ವರೆಗೆ (3 ತಿಂಗಳು)</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಮಳೆಯ ಪಾಲು</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ರಾಜ್ಯದ ಒಟ್ಟು ಮಳೆಯ ಶೇಕಡಾ 70% ರಿಂದ 75%</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ರಾಜ್ಯದ ಒಟ್ಟು ಮಳೆಯ ಶೇಕಡಾ 15% ರಿಂದ 20%</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಮಾರುತಗಳ ಮೂಲ</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅರಬ್ಬಿ ಸಮುದ್ರದಿಂದ ಬೀಸುವ ತೇವಾಂಶಭರಿತ ನೈಋತ್ಯ ಮಾರುತಗಳು</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಹಿಮಾಲಯ & ಬಂಗಾಳ ಕೊಲ್ಲಿಯಿಂದ ಮರಳಿ ಬೀಸುವ ಈಶಾನ್ಯ ಮಾರುತಗಳು</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಹೆಚ್ಚು ಲಾಭ ಪಡೆಯುವ ಜಿಲ್ಲೆಗಳು</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕರಾವಳಿ, ಮಲೆನಾಡು ಮತ್ತು ಕಾವೇರಿ-ಕೃಷ್ಣಾ ನದಿ ಕೊಳ್ಳಗಳು</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ತುಮಕೂರು, ಬೆಂಗಳೂರು, ಚಾಮರಾಜನಗರ</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಅಣೆಕಟ್ಟುಗಳಿಗೆ ಮಹತ್ವ</strong></td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">KRS, ಆಲಮಟ್ಟಿ, ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಭದ್ರಾ ಜಲಾಶಯಗಳು ಭರ್ತಿಯಾಗುವುದು ಈ ಮುಂಗಾರಿನಿಂದಲೇ.</td>
              <td style="padding: 10px; border: 1px solid #e2e8f0;">ಬಯಲು ಸೀಮೆಯ ಕೆರೆ-ಕಟ್ಟೆಗಳು ಮತ್ತು ಅಂತರ್ಜಲ ಮರುಪೂರಣಕ್ಕೆ ನಿರ್ಣಾಯಕ.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 5: MODERN METEOROLOGY TECH -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">5. ಆಧುನಿಕ ಹವಾಮಾನ ತಂತ್ರಜ್ಞಾನ: KSNDMC & IMD ನೆಟ್ವರ್ಕ್</h2>
      <p>ಕರ್ನಾಟಕವು ದೇಶದಲ್ಲೇ ಅತ್ಯಂತ ಮುಂದುವರಿದ ಗ್ರಾಮೀಣ ಹವಾಮಾನ ಮಾನಿಟರಿಂಗ್ ವ್ಯವಸ್ಥೆಯನ್ನು ಹೊಂದಿದೆ:</p>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; margin: 15px 0;">
        <ul style="padding-left: 20px; margin: 0; font-size: 14px;">
          <li><strong>ಟೆಲಿಮೆಟ್ರಿಕ್ ಮಳೆ ಮಾಪನ ಕೇಂದ್ರಗಳು (TRGs):</strong> ಕರ್ನಾಟಕ ರಾಜ್ಯ ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಉಸ್ತುವಾರಿ ಕೇಂದ್ರವು (KSNDMC) ರಾಜ್ಯದ ಪ್ರತಿಯೊಂದು ಗ್ರಾಮ ಪಂಚಾಯತಿ ಮಟ್ಟದಲ್ಲೂ (6,000+ ಕೇಂದ್ರಗಳು) ಸ್ವಯಂಚಾಲಿತ ಸೋಲಾರ್ ಟೆಲಿಮೆಟ್ರಿಕ್ ಮಳೆ ಮಾಪಕಗಳನ್ನು ಅಳವಡಿಸಿದೆ. ಪ್ರತಿ 15 ನಿಮಿಷಕ್ಕೊಮ್ಮೆ ಮಳೆಯ ಲೈವ್ ಡೇಟಾ ಸರ್ವರ್ಗೆ ರವಾನೆಯಾಗುತ್ತದೆ.</li>
          <li><strong>ಡಾಪ್ಲರ್ ವೆದರ್ ರಾಡಾರ್ (DWR Bengaluru & Goa):</strong> ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆಯು (IMD) ಬೆಂಗಳೂರಿನಲ್ಲಿ ಅಳವಡಿಸಿರುವ ಡಾಪ್ಲರ್ ರಾಡಾರ್ ಸುಮಾರು 250 ರಿಂದ 300 ಕಿ.ಮೀ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಮೋಡಗಳ ಸಾಂದ್ರತೆ, ಮಳೆಯ ತೀವ್ರತೆ ಮತ್ತು ಗುಡುಗು-ಮಿಂಚಿನ ಮುನ್ಸೂಚನೆಯನ್ನು ಕ್ಷಣಾರ್ಧದಲ್ಲಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ.</li>
          <li><strong>ವರುಣ ಮಿತ್ರ ಹೆಲ್ಪ್ಲೈನ್ (Varuna Mitra 24x7):</strong> ರೈತರು ತಮ್ಮ ಗ್ರಾಮದ ಹವಾಮಾನ ಮತ್ತು ಮಳೆ ಮುನ್ಸೂಚನೆಯನ್ನು ತಿಳಿಯಲು <strong>9243345433</strong> ಗೆ ಕರೆ ಮಾಡಿ ಉಚಿತ ಮಾಹಿತಿ ಪಡೆಯಬಹುದು.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 6: HOW TO USE THE TOOL -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">6. Karnata.in ಹವಾಮಾನ & ಮಳೆ ಟ್ರ್ಯಾಕರ್ ಅನ್ನು ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?</h2>
      <p>ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು ತಾಲೂಕಿನ ನಿಖರ ಹವಾಮಾನ ಮಾಹಿತಿಯನ್ನು ಲೈವ್ ಆಗಿ ವೀಕ್ಷಿಸಲು ಈ ಕೆಳಗಿನ ಸೌಲಭ್ಯಗಳನ್ನು ಬಳಸಿ:</p>
      <ul style="padding-left: 20px;">
        <li><strong>ಪ್ರಸ್ತುತ ತಾಪಮಾನ & ಆರ್ದ್ರತೆ (Temperature & Humidity):</strong> ಇಂದಿನ ನೈಜ ತಾಪಮಾನ (°C), ಅನುಭವವಾಗುವ ಶಾಖ (Feels Like) ಮತ್ತು ಗಾಳಿಯಲ್ಲಿರುವ ತೇವಾಂಶದ ವಿವರ.</li>
        <li><strong>ಗಾಳಿಯ ವೇಗ ಮತ್ತು ದಿಕ್ಕು (Wind Speed & Direction):</strong> ಕಿಲೋಮೀಟರ್ ಪ್ರತಿ ಗಂಟೆಯಲ್ಲಿ (km/h) ಗಾಳಿಯ ವೇಗ ಮತ್ತು ಮಳೆ ಮೋಡಗಳ ಚಲನೆಯ ದಿಕ್ಕು.</li>
        <li><strong>7 ದಿನಗಳ ವಿಸ್ತೃತ ಮುನ್ಸೂಚನೆ (7-Day Forecast):</strong> ಮುಂಬರುವ ವಾರದಲ್ಲಿ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ (Rain Probability %), ಗರಿಷ್ಠ-ಕನಿಷ್ಠ ತಾಪಮಾನದ ಟ್ರೆಂಡ್.</li>
        <li><strong>ಪ್ರಸ್ತುತ ಮಳೆ ನಕ್ಷತ್ರ ವಿವರ:</strong> ಇಂದು ಯಾವ ಮಳೆ ನಕ್ಷತ್ರ ಚಾಲ್ತಿಯಲ್ಲಿದೆ ಮತ್ತು ಯಾವ ವಾಹನ ಪ್ರಭಾವದಲ್ಲಿದೆ ಎಂಬ ಸಾಂಪ್ರದಾಯಿಕ ಮಾಹಿತಿ.</li>
      </ul>
    </section>

    <!-- SECTION 7: FAQS -->
    <section style="margin-top: 35px;">
      <h2 style="font-size: 22px; color: #0f172a; font-weight: 700; border-left: 5px solid #0284c7; padding-left: 12px;">7. ಹವಾಮಾನ ಮತ್ತು ಮಳೆ ನಕ್ಷತ್ರಗಳ ಕುರಿತು ಪ್ರಮುಖ ಪ್ರಶ್ನೋತ್ತರಗಳು (FAQs)</h2>

      <div style="margin-top: 15px;">
        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 1: ಮಳೆ ನಕ್ಷತ್ರಗಳು ವೈಜ್ಞಾನಿಕವೇ ಅಥವಾ ಕೇವಲ ಮೂಢನಂಬಿಕೆಯೇ?</h3>
        <p style="margin-top: 0; color: #475569;">ಮಳೆ ನಕ್ಷತ್ರಗಳು ಯಾವುದೇ ಮೂಢನಂಬಿಕೆಯಲ್ಲ; ಅವು ಸೂರ್ಯನ ವಾರ್ಷಿಕ ಕ್ರಾಂತಿವೃತ್ತದ ಚಲನೆ ಮತ್ತು ಋತುಮಾನದ ಬದಲಾವಣೆಗಳನ್ನು ಗುರುತಿಸುವ ಅತ್ಯಂತ ನಿಖರವಾದ ಪ್ರಾಚೀನ ಖಗೋಳ-ಹವಾಮಾನ ಕ್ಯಾಲೆಂಡರ್ ಆಗಿದೆ. ನೂರಾರು ವರ್ಷಗಳಿಂದ ರೈತರ ಅನುಭವ ಮತ್ತು ಅಂಕಿಅಂಶಗಳಿಂದ ಇವು ಪುಷ್ಟೀಕರಿಸಲ್ಪಟ್ಟಿವೆ.</p>

        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 2: 'ಆಗುಂಬೆ' ಗಿಂತ ಹೆಚ್ಚು ಮಳೆ ಬೀಳುವ ಸ್ಥಳ ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?</h3>
        <p style="margin-top: 0; color: #475569;">ಹೌದು, ಐತಿಹಾಸಿಕವಾಗಿ ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ತೀರ್ಥಹಳ್ಳಿ ತಾಲೂಕಿನ ಆಗುಂಬೆಯನ್ನು 'ದಕ್ಷಿಣ ಭಾರತದ ಚಿರಾಪುಂಜಿ' ಎನ್ನಲಾಗುತ್ತದೆ. ಆದರೆ ಇತ್ತೀಚಿನ ದಶಕಗಳ ಅಂಕಿಅಂಶಗಳ ಪ್ರಕಾರ ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಸಿದ್ದಾಪುರ ಬಳಿಯ <strong>ಹುಲಿಕಲ್ (Hulikal)</strong> ಮತ್ತು ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಯ ಖಾನಾಪುರ ತಾಲೂಕಿನ <strong>ಅಮಗಾಂವ್ (Amagaon)</strong> ನಲ್ಲಿ ಆಗುಂಬೆಗಿಂತಲೂ ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ಮಳೆ ದಾಖಲಾಗುತ್ತಿದೆ.</p>

        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 3: ಎಲ್-ನಿನೋ (El Niño) ಮತ್ತು ಲಾ-ನಿನಾ (La Niña) ಕರ್ನಾಟಕದ ಮಳೆಯ ಮೇಲೆ ಹೇಗೆ ಪರಿಣಾಮ ಬೀರುತ್ತವೆ?</h3>
        <p style="margin-top: 0; color: #475569;">ಪೆಸಿಫಿಕ್ ಸಾಗರದ ಮೇಲ್ಮೈ ನೀರು ಅತಿಯಾಗಿ ಬಿಸಿಯಾಗುವ 'ಎಲ್-ನಿನೋ' ವರ್ಷಗಳಲ್ಲಿ ಭಾರತ ಮತ್ತು ಕರ್ನಾಟಕದಲ್ಲಿ ಮುಂಗಾರು ಮಳೆ ದುರ್ಬಲಗೊಂಡು ಬರಗಾಲ ಉಂಟಾಗುವ ಸಾಧ್ಯತೆ ಇರುತ್ತದೆ. ಇದಕ್ಕೆ ವಿರುದ್ಧವಾಗಿ 'ಲಾ-ನಿನಾ' ಸ್ಥಿತಿಯಿದ್ದಾಗ ರಾಜ್ಯದಲ್ಲಿ ವಾಡಿಕೆಗಿಂತ ಅತ್ಯಧಿಕ ಮಳೆ ಮತ್ತು ಉತ್ತಮ ಜಲಾಶಯ ಭರ್ತಿ ದಾಖಲಾಗುತ್ತದೆ.</p>

        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 4: ಯೆಲ್ಲೋ, ಆರೆಂಜ್ ಮತ್ತು ರೆಡ್ ಅಲರ್ಟ್ ಮಳೆ ಎಚ್ಚರಿಕೆಗಳ ಅರ್ಥವೇನು?</h3>
        <p style="margin-top: 0; color: #475569;">ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆಯ (IMD) ಬಣ್ಣದ ಎಚ್ಚರಿಕೆಗಳು:</p>
        <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 14px; color: #475569;">
          <li><strong>ಗ್ರೀನ್ ಅಲರ್ಟ್ (Green):</strong> ಯಾವುದೇ ಅಪಾಯವಿಲ್ಲ, ಸಾಮಾನ್ಯ ಹವಾಮಾನ.</li>
          <li><strong>ಯೆಲ್ಲೋ ಅಲರ್ಟ್ (Yellow):</strong> ನಿಗಾ ಇರಿಸಿ (Watch) — 64.5 ಮಿ.ಮೀ ನಿಂದ 115.5 ಮಿ.ಮೀ ವರೆಗೆ ಭಾರಿ ಮಳೆ ಸಾಧ್ಯತೆ.</li>
          <li><strong>ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange):</strong> ಸನ್ನದ್ಧರಾಗಿರಿ (Be Prepared) — 115.6 ಮಿ.ಮೀ ನಿಂದ 204.4 ಮಿ.ಮೀ ವರೆಗೆ ಅತಿ ಭಾರಿ ಮಳೆ.</li>
          <li><strong>ರೆಡ್ ಅಲರ್ಟ್ (Red):</strong> ತಕ್ಷಣ ರಕ್ಷಣಾ ಕ್ರಮ ಕೈಗೊಳ್ಳಿ (Take Action) — 204.5 ಮಿ.ಮೀ ಗಿಂತಲೂ ಹೆಚ್ಚಿನ ಅತ್ಯಂತ ಭಾರಿ ವರ್ಷಧಾರೆ, ಪ್ರವಾಹ ಭೀತಿ.</li>
        </ul>

        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 5: ಬೆಂಗಳೂರಿನಲ್ಲಿ ಬೇಸಿಗೆಯಲ್ಲಿ ಸಂಜೆ ಹೊತ್ತು ಭಾರಿ ಗುಡುಗು ಮಳೆ ಏಕೆ ಬರುತ್ತದೆ?</h3>
        <p style="margin-top: 0; color: #475569;">ಬೆಂಗಳೂರಿನಲ್ಲಿ ಮಾರ್ಚ್ನಿಂದ ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಧ್ಯಾಹ್ನದ ತೀವ್ರ ತಾಪಮಾನದಿಂದಾಗಿ ಬಿಸಿಯಾದ ಗಾಳಿ ವೇಗವಾಗಿ ಮೇಲೇರುತ್ತದೆ (Convectional Current). ಸಂಜೆಯ ವೇಳೆಗೆ ಇದು 'ಕ್ಯುಮುಲೋನಿಂಬಸ್' (Cumulonimbus) ಕಾರ್ಮೋಡಗಳಾಗಿ ಮಾರ್ಪಟ್ಟು ಆಲಿಕಲ್ಲು (Hailstorm) ಮತ್ತು ಭಾರಿ ಗುಡುಗು ಸಹಿತ ಮಳೆಯನ್ನು ಸುರಿಸುತ್ತದೆ.</p>
      </div>
    </section>

    <!-- SUMMARY FOOTER -->
    <footer style="margin-top: 30px; padding: 18px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; font-size: 13px; color: #166534;">
      <strong>ಮಾಹಿತಿ ಮತ್ತು ದತ್ತಾಂಶ ಹಕ್ಕುತ್ಯಾಗ:</strong> Karnata.in ನಲ್ಲಿ ಪ್ರಕಟವಾಗುವ ಹವಾಮಾನ ದತ್ತಾಂಶಗಳನ್ನು ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ (IMD), ಕರ್ನಾಟಕ ರಾಜ್ಯ ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಉಸ್ತುವಾರಿ ಕೇಂದ್ರ (KSNDMC) ಮತ್ತು ಜಾಗತಿಕ ಹವಾಮಾನ ಉಪಗ್ರಹ ಮಾದರಿಗಳ ಆಧಾರದ ಮೇಲೆ ನವೀಕರಿಸಲಾಗುತ್ತದೆ. ಹವಾಮಾನವು ನೈಸರ್ಗಿಕ ಪ್ರಕ್ರಿಯೆಯಾಗಿದ್ದು ಸ್ಥಳೀಯ ವಾತಾವರಣದ ಒತ್ತಡಕ್ಕೆ ತಕ್ಕಂತೆ ಅಲ್ಪ ಬದಲಾವಣೆಗಳಾಗಬಹುದು.
    </footer>

  </article>
"""

# Place article right before closing </div> of .wrap
content = content.replace(
    '  <!-- DISTRICT WEATHER GRID -->\n  <div class="dist-weather-grid" id="district-grid"></div>\n\n</div>',
    '  <!-- DISTRICT WEATHER GRID -->\n  <div class="dist-weather-grid" id="district-grid"></div>\n\n' + article_html + '\n</div>'
)

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_WEATHER_GUIDE_ARTICLE_INJECTED")
