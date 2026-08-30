# -*- coding: utf-8 -*-
"""
Karnata — scripts/embed_exact_apmc_manual_article.py
Embeds the exact requested 9-section comprehensive APMC manual article into apmc-prices.html
and ensures it is permanently preserved across future updates.
"""

import json

with open("data/crop_analyzer_db.json", "r", encoding="utf-8") as f:
    crops_json_str = f.read()

article_html = """<article class="article-container font-kannada" style="line-height: 1.85; color: #222; font-size: 16px; margin-top: 40px; padding: 25px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px;">

  <header>
    <h1 style="font-size: 28px; color: #0f172a; margin-bottom: 12px; font-weight: 700;">ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು, ಕೃಷಿ ಉತ್ಪನ್ನ ಹರಾಜು & ರೈತ ವಹಿವಾಟು ಮಾರ್ಗದರ್ಶಿ (Karnataka APMC Mandi Rates & Farmer Trade Manual)</h1>
    <p style="color: #64748b; font-size: 14px; margin-bottom: 24px;">ಪ್ರಕಟಣೆ: Karnata.in ಕೃಷಿ & ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ವಿಭಾಗ | ಕೊನೆಯ ನವೀಕರಣ: 2026</p>
  </header>

  <hr style="border: 0; border-top: 1px solid #cbd5e1; margin-bottom: 25px;">

  <!-- SECTION 1 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">1. ಕೃಷಿ ಆರ್ಥಿಕತೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ದರಗಳ ಪಾರದರ್ಶಕತೆ</h2>
    <p>ಕರ್ನಾಟಕದ ಒಟ್ಟು ಜನಸಂಖ್ಯೆಯ ಅರ್ಧಕ್ಕಿಂತ ಹೆಚ್ಚು ಭಾಗವು ಕೃಷಿ ಮತ್ತು ತೋಟಗಾರಿಕಾ ಕ್ಷೇತ್ರವನ್ನು ತಮ್ಮ ಪ್ರಮುಖ ಜೀವನೋಪಾಯವಾಗಿ ಅವಲಂಬಿಸಿದೆ. ರೈತರು ತಿಂಗಳುಗಟ್ಟಲೆ ಬೆವರು ಸುರಿಸಿ, ಹವಾಮಾನ ವೈಪರೀತ್ಯಗಳ ನಡುವೆ ಬೆಳೆ ಬೆಳೆಯುವುದು ಒಂದು ಸವಾಲಾದರೆ, ಬೆಳೆದ ಬೆಳೆಗೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಸೂಕ್ತವಾದ ಮತ್ತು ನ್ಯಾಯಯುತವಾದ ಬೆಲೆ ಪಡೆಯುವುದು ಮತ್ತೊಂದು ದೊಡ್ಡ ಸವಾಲು. ದಲ್ಲಾಳಿಗಳ ಮತ್ತು ಮಧ್ಯವರ್ತಿಗಳ ಶೋಷಣೆಯಿಂದ ರೈತರನ್ನು ರಕ್ಷಿಸಲು ಸ್ಥಾಪಿಸಲಾದ <strong>ಕೃಷಿ ಉತ್ಪನ್ನ ಮಾರುಕಟ್ಟೆ ಸಮಿತಿಗಳು (APMC - Agricultural Produce Market Committees)</strong> ರಾಜ್ಯದ ಕೃಷಿ ಆರ್ಥಿಕತೆಯಲ್ಲಿ ನಿರ್ಣಾಯಕ ಪಾತ್ರ ವಹಿಸುತ್ತವೆ.</p>

    <p>ಪ್ರತಿದಿನ ರಾಜ್ಯದ ವಿವಿಧ ಜಿಲ್ಲೆಗಳ ಮಾರುಕಟ್ಟೆ ಅಂಗಳಗಳಲ್ಲಿ (Mandi Yards) ತರಕಾರಿಗಳು, ದವಸ ಧಾನ್ಯಗಳು, ಎಣ್ಣೆಕಾಳುಗಳು ಮತ್ತು ವಾಣಿಜ್ಯ ಬೆಳೆಗಳ ಬೆಲೆಗಳು ಪೂರೈಕೆ ಮತ್ತು ಬೇಡಿಕೆಯ (Demand and Supply) ಆಧಾರದ ಮೇಲೆ ಕ್ಷಣಕ್ಷಣಕ್ಕೂ ಬದಲಾಗುತ್ತವೆ. ರೈತರು ತಮ್ಮ ಉತ್ಪನ್ನಗಳನ್ನು ಮಾರುಕಟ್ಟೆಗೆ ಸಾಗಿಸುವ ಮುನ್ನ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ದರಗಳು, ಮಾದರಿ ಬೆಲೆ (Modal Price) ಮತ್ತು ಆವಕದ (Arrival Volume) ನಿಖರ ಮಾಹಿತಿಯನ್ನು ತಿಳಿದುಕೊಂಡರೆ ಉತ್ತಮ ಲಾಭ ಗಳಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ.</p>
  </section>

  <!-- SECTION 2 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">2. APMC ದರ ಪರಿಭಾಷೆಗಳು: ಬೆಲೆ ಪಟ್ಟಿಯನ್ನು ಓದುವುದು ಹೇಗೆ?</h2>
    <p>ದೈನಂದಿನ ಮಂಡಿ ಬೆಲೆ ಪಟ್ಟಿಯಲ್ಲಿ ಪ್ರಕಟವಾಗುವ ಪ್ರಮುಖ ಮೂರು ದರಗಳ ನೈಜ ಅರ್ಥವನ್ನು ಪ್ರತಿಯೊಬ್ಬ ರೈತರೂ ತಿಳಿದಿರಬೇಕು:</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 20px 0;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px;">
        <h3 style="color: #0f172a; margin-top: 0; font-size: 17px;">1. ಕನಿಷ್ಠ ದರ (Minimum Price)</h3>
        <p style="font-size: 14px;">ಆ ದಿನ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಹರಾಜಾದ ಅತಿ ಕಡಿಮೆ ಗುಣಮಟ್ಟದ, ಸಣ್ಣ ಗಾತ್ರದ ಅಥವಾ ಹಾನಿಗೊಳಗಾದ ಕೃಷಿ ಮಾಲಿಗೆ ವ್ಯಾಪಾರಿಗಳು ಕೂಗಿದ ಆರಂಭಿಕ ಕನಿಷ್ಠ ಬೆಲೆ (ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್ ಅಥವಾ ಬಾಕ್ಸ್ ಲೆಕ್ಕದಲ್ಲಿ).</p>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px;">
        <h3 style="color: #0f172a; margin-top: 0; font-size: 17px;">2. ಗರಿಷ್ಠ ದರ (Maximum Price)</h3>
        <p style="font-size: 14px;">ಅತ್ಯುನ್ನತ ಗುಣಮಟ್ಟದ (Grade-A / Premium Quality), ಒಂದೇ ಸಮನಾದ ಗಾತ್ರ ಮತ್ತು ಉತ್ತಮ ಬಣ್ಣವಿರುವ ಮಾಲಿಗೆ ದಿನದ ಹರಾಜಿನಲ್ಲಿ ಸಿಕ್ಕ ಅತಿ ಹೆಚ್ಚಿನ ಬೆಲೆ. ಈ ದರದಲ್ಲಿ ಸೀಮಿತ ಪ್ರಮಾಣದ ಸರಕು ಮಾತ್ರ ಮಾರಾಟವಾಗಿರುತ್ತದೆ.</p>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px;">
        <h3 style="color: #0f172a; margin-top: 0; font-size: 17px;">3. ಮಾದರಿ ದರ (Modal Price - ಅತ್ಯಂತ ಮುಖ್ಯ)</h3>
        <p style="font-size: 14px;">ಮಾರುಕಟ್ಟೆಗೆ ಬಂದ ಒಟ್ಟು ಮಾಲಿನ ಪೈಕಿ ಶೇಕಡಾ 70% ರಿಂದ 80% ರಷ್ಟು ಸರಕು ಯಾವ ಸರಾಸರಿ ಬೆಲೆಗೆ ಹರಾಜಾಯಿತೋ ಆ ದರವೇ ಮಾದರಿ ದರ. <strong>ರೈತರು ತಮ್ಮ ಆದಾಯದ ಲೆಕ್ಕಾಚಾರಕ್ಕೆ ಯಾವಾಗಲೂ ಈ ಮಾದರಿ ದರವನ್ನೇ ಮಾನದಂಡವಾಗಿ ಪರಿಗಣಿಸಬೇಕು.</strong></p>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px;">
        <h3 style="color: #0f172a; margin-top: 0; font-size: 17px;">4. ಆವಕ (Arrivals / Volume)</h3>
        <p style="font-size: 14px;">ಆ ದಿನ ಮಾರುಕಟ್ಟೆಗೆ ವಿವಿಧ ಹಳ್ಳಿಗಳಿಂದ ಬಂದಿಳಿದ ಒಟ್ಟು ಕೃಷಿ ಉತ್ಪನ್ನಗಳ ತೂಕ (ಕ್ವಿಂಟಾಲ್ಗಳು, ಟನ್ಗಳು ಅಥವಾ ಚೀಲಗಳ ಲೆಕ್ಕದಲ್ಲಿ). ಆವಕ ಹೆಚ್ಚಾದರೆ ಬೆಲೆ ಇಳಿಯುವ ಮತ್ತು ಆವಕ ಕಡಿಮೆಯಾದರೆ ಬೆಲೆ ಏರುವ ಸಾಧ್ಯತೆ ಇರುತ್ತದೆ.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 3 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">3. ಕರ್ನಾಟಕದ ಪ್ರಸಿದ್ಧ APMC ಮಾರುಕಟ್ಟೆಗಳು ಮತ್ತು ಅವುಗಳ ಪ್ರಮುಖ ಬೆಳೆಗಳ ವಿಶೇಷತೆ</h2>
    <p>ಕರ್ನಾಟಕದ ವಿವಿಧ ಜಿಲ್ಲೆಗಳು ಭೌಗೋಳಿಕ ಮತ್ತು ಹವಾಮಾನ ವೈಶಿಷ್ಟ್ಯಗಳ ಕಾರಣದಿಂದ ನಿರ್ದಿಷ್ಟ ಕೃಷಿ ಬೆಳೆಗಳ ವಹಿವಾಟಿನಲ್ಲಿ ಅಖಿಲ ಭಾರತ ಮಟ್ಟದಲ್ಲಿ ಹೆಸರುವಾಸಿಯಾಗಿವೆ:</p>

    <div style="overflow-x: auto;">
      <table style="width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 14px;">
        <thead>
          <tr style="background: #0f172a; color: #ffffff; text-align: left;">
            <th style="padding: 10px; border: 1px solid #cbd5e1;">APMC ಮಾರುಕಟ್ಟೆ</th>
            <th style="padding: 10px; border: 1px solid #cbd5e1;">ಜಿಲ್ಲೆ</th>
            <th style="padding: 10px; border: 1px solid #cbd5e1;">ಪ್ರಮುಖ ಬೆಳೆಗಳು (Commodities)</th>
            <th style="padding: 10px; border: 1px solid #cbd5e1;">ಮಾರುಕಟ್ಟೆಯ ಮಹತ್ವ ಮತ್ತು ರಾಷ್ಟ್ರೀಯ ಪ್ರಭಾವ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಕೋಲಾರ & ಚಿಂತಾಮಣಿ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಟೊಮ್ಯಾಟೋ, ಮಾವು, ಕೋಸು, ಬೀನ್ಸ್</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಏಷ್ಯಾದ 2ನೇ ಬೃಹತ್ ಟೊಮ್ಯಾಟೋ ಮಂಡಿ. ಇಲ್ಲಿಂದ ತಮಿಳುನಾಡು, ಆಂಧ್ರ, ಕೇರಳ, ಮಹಾರಾಷ್ಟ್ರ, ಪಶ್ಚಿಮ ಬಂಗಾಳ ಮತ್ತು ಬಾಂಗ್ಲಾದೇಶಕ್ಕೂ ಟೊಮ್ಯಾಟೋ ರಫ್ತಾಗುತ್ತದೆ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಬ್ಯಾಡಗಿ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಹಾವೇರಿ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಒಣ ಮೆಣಸಿನಕಾಯಿ (ಕಡ್ಡಿ & ಡಬ್ಬಿ)</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅಂತಾರಾಷ್ಟ್ರೀಯ ಖ್ಯಾತಿಯ ಮಸಾಲೆ ಮಾರುಕಟ್ಟೆ. ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿಯ ಗಾಢ ಕೆಂಪು ಬಣ್ಣ ಮತ್ತು ಓಲಿಯೋರೆಸಿನ್ ಅಂಶದಿಂದಾಗಿ ಯುರೋಪ್ ಮತ್ತು ಅಮೆರಿಕದ ಫುಡ್ ಕಂಪನಿಗಳಿಗೆ ಭಾರಿ ಬೇಡಿಕೆಯಿದೆ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ತಿಪಟೂರು & ಅರಸೀಕೆರೆ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ತುಮಕೂರು, ಹಾಸನ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಉಂಡೆ ಕೊಬ್ಬರಿ (Copra), ಹಸಿ ತೆಂಗಿನಕಾಯಿ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಭಾರತದ ನಂಬರ್ 1 ಕೊಬ್ಬರಿ ಮಾರುಕಟ್ಟೆ. ಉತ್ತರ ಭಾರತದ ಹಬ್ಬಗಳು ಮತ್ತು ಮದುವೆ ಸೀಸನ್ಗಳಲ್ಲಿ ತಿಪಟೂರು ಕೊಬ್ಬರಿಗೆ ವ್ಯಾಪಕ ಬೇಡಿಕೆಯಿರುತ್ತದೆ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಶಿವಮೊಗ್ಗ & ಸಾಗರ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಶಿವಮೊಗ್ಗ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಅಡಿಕೆ (ರಾಶಿ, ಚಾಲಿ, ಬೆಟ್ಟೆ, ಸರಕು, ಗೋರಬುಲು)</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಮಲೆನಾಡು ಭಾಗದ ಅಡಿಕೆ ಧಾರಣೆ ನಿಗದಿಪಡಿಸುವ ಪ್ರಮುಖ ಕೇಂದ್ರ. ಕ್ಯಾಂಪ್ಕೋ (CAMPCO) ಮತ್ತು ಮ್ಯಾಮ್ಕೋಸ್ (MAMCOS) ಸಂಸ್ಥೆಗಳು ಇಲ್ಲಿ ಪ್ರಮುಖ ಪಾತ್ರ ವಹಿಸುತ್ತವೆ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಕಲಬುರಗಿ & ಯಾದಗಿರಿ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕಲಬುರಗಿ, ಯಾದಗಿರಿ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ತೊಗರಿ ಬೇಳೆ (Red Gram / Tur Dal)</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">'ತೊಗರಿಯ ಕಣಜ' ಎಂದೇ ಖ್ಯಾತ. ಕರ್ನಾಟಕದ ಜಿಐ ಟ್ಯಾಗ್ (GI Tag) ಪಡೆದಿರುವ ಕಲಬುರಗಿ ತೊಗರಿ ಬೇಳೆಗೆ ದೇಶದ ಬೇಳೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ವಿಶೇಷ ಸ್ಥಾನವಿದೆ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ರಾಯಚೂರು & ಬಳ್ಳಾರಿ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ರಾಯಚೂರು, ಬಳ್ಳಾರಿ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಹತ್ತಿ (Cotton), ಸೋನಾ ಮಸೂರಿ ಭತ್ತ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಬೃಹತ್ ಹತ್ತಿ ಜಿನ್ನಿಂಗ್ ಗಿರಣಿಗಳು ಮತ್ತು ವಿಶ್ವಪ್ರಸಿದ್ಧ ತುಂಗಭದ್ರಾ ಬೆಲ್ಟ್ನ ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿ ವಹಿವಾಟಿನ ಕೇಂದ್ರ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಯಶವಂತಪುರ & ದಾಸನಪುರ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಬೆಂಗಳೂರು ನಗರ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಈರುಳ್ಳಿ, ಆಲೂಗಡ್ಡೆ, ಬೆಳ್ಳುಳ್ಳಿ, ಆಹಾರ ಧಾನ್ಯಗಳು</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ರಾಜ್ಯದ ಅತಿ ದೊಡ್ಡ ಗ್ರಾಹಕ ಮಾರುಕಟ್ಟೆ. ಮಹಾರಾಷ್ಟ್ರ, ಮಧ್ಯಪ್ರದೇಶ ಮತ್ತು ಉತ್ತರ ಭಾರತದಿಂದ ಬರುವ ದಿನಸಿ ಸರಕುಗಳ ಪ್ರಮುಖ ವಿತರಣಾ ಕೇಂದ್ರ.</td>
          </tr>
          <tr>
            <td style="padding: 10px; border: 1px solid #e2e8f0;"><strong>ಗದಗ & ಹುಬ್ಬಳ್ಳಿ APMC</strong></td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಗದಗ, ಧಾರವಾಡ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಕಡಲೆ (Bengal Gram), ಶೇಂಗಾ, ಜೋಳ, ಸೂರ್ಯಕಾಂತಿ</td>
            <td style="padding: 10px; border: 1px solid #e2e8f0;">ಉತ್ತರ ಕರ್ನಾಟಕದ ಎಣ್ಣೆಕಾಳು ಮತ್ತು ಹಿಂಗಾರು ಧಾನ್ಯಗಳ ಅತ್ಯುನ್ನತ ಮಾರುಕಟ್ಟೆ.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 4 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">4. ಇ-ನ್ಯಾಮ್ (e-NAM) ಮತ್ತು ಕರ್ನಾಟಕದ ReMS ಇ-ಹರಾಜು ಕ್ರಾಂತಿ</h2>
    <p>ಸಾಂಪ್ರದಾಯಿಕವಾಗಿ ನಡೆಯುತ್ತಿದ್ದ ರಹಸ್ಯ ಹರಾಜು (ಬಟ್ಟೆಯಡಿಯಲ್ಲಿ ಬೆರಳುಗಳ ಸನ್ನೆ ಮೂಲಕ ದರ ಕೂಗುವ ಪದ್ಧತಿ) ಮತ್ತು ವ್ಯಾಪಾರಿಗಳ ಸಿಂಡಿಕೇಟ್ ಮುರಿಯಲು ಕರ್ನಾಟಕ ಸರ್ಕಾರವು <strong>ರಾಷ್ಟ್ರೀಯ ಇ-ಮಾರುಕಟ್ಟೆ ಸೇವೆಗಳು (ReMS - Rashtriya e-Market Services)</strong> ಮೂಲಕ ವಿದ್ಯುನ್ಮಾನ ಟೆಂಡರ್ ವ್ಯವಸ್ಥೆಯನ್ನು ಜಾರಿಗೆ ತಂದಿದೆ. ಇದು ಕೇಂದ್ರ ಸರ್ಕಾರದ <strong>e-NAM (National Agriculture Market)</strong> ಪೋರ್ಟಲ್ ಜೊತೆ ಸಂಯೋಜಿತವಾಗಿದೆ.</p>

    <h3 style="font-size: 18px; color: #1e293b;">ಇ-ಹರಾಜು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?</h3>
    <ol style="padding-left: 20px;">
      <li><strong>ಗೇಟ್ ಎಂಟ್ರಿ & ಲಾಟ್ ತಯಾರಿ:</strong> ರೈತರು ತಂದ ಸರಕಿಗೆ ತೂಕದ ಆಧಾರದ ಮೇಲೆ ವಿಶಿಷ್ಟ ಲಾಟ್ ನಂಬರ್ (Lot Number) ನೀಡಲಾಗುತ್ತದೆ.</li>
      <li><strong>ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ (Assaying):</strong> ಮಾದರಿ ಸರಕನ್ನು ತೆಗೆದುಕೊಂಡು ತೇವಾಂಶ (Moisture), ಸ್ವಚ್ಛತೆ ಮತ್ತು ಗಾತ್ರವನ್ನು ಆಧುನಿಕ ಲ್ಯಾಬ್ಗಳಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ ಆನ್ಲೈನ್ನಲ್ಲಿ ಅಪ್ಲೋಡ್ ಮಾಡಲಾಗುತ್ತದೆ.</li>
      <li><strong>ಆನ್ಲೈನ್ ಬಿಡ್ಡಿಂಗ್ (Online Bidding):</strong> ದೇಶದ ಯಾವುದೇ ಮೂಲೆಯಲ್ಲಿರುವ ಪರವಾನಗಿ ಪಡೆದ ವ್ಯಾಪಾರಿಗಳು ಕಂಪ್ಯೂಟರ್ ಅಥವಾ ಮೊಬೈಲ್ ಮೂಲಕ ಸ್ಪರ್ಧಾತ್ಮಕ ದರಗಳನ್ನು ಕೂಗುತ್ತಾರೆ.</li>
      <li><strong>ರೈತನ ಒಪ್ಪಿಗೆ:</strong> ಅಂತಿಮವಾಗಿ ಬಂದ ಅತ್ಯಧಿಕ ದರ ರೈತನ ಮೊಬೈಲ್ಗೆ ಎಸ್ಎಂಎಸ್ ಮೂಲಕ ಬರುತ್ತದೆ. ಆ ದರ ತೃಪ್ತಿಕರವಾಗಿದ್ದರೆ ಮಾತ್ರ ರೈತ 'ಒಪ್ಪಿಗೆ' (Accept) ನೀಡಬಹುದು. ಬೆಲೆ ಕಡಿಮೆ ಎನಿಸಿದರೆ ತಿರಸ್ಕರಿಸಿ ಮುಂದಿನ ದಿನಕ್ಕೆ ಕಾಯ್ದಿರಿಸಬಹುದು.</li>
      <li><strong>ನೇರ ಬ್ಯಾಂಕ್ ಜಮೆ (Direct Benefit Transfer):</strong> ಮಾಲು ಮಾರಾಟವಾದ ಕೆಲವೇ ಗಂಟೆಗಳಲ್ಲಿ ಹಣವು ಮಧ್ಯವರ್ತಿಗಳ ಕೈಗೆ ಹೋಗದೆ ನೇರವಾಗಿ ರೈತನ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.</li>
    </ol>
  </section>

  <!-- SECTION 5 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">5. ಬೆಂಬಲ ಬೆಲೆ ಯೋಜನೆ (MSP - Minimum Support Price) vs ಮಂಡಿ ದರ</h2>
    <p>ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಬೆಳೆಗಳ ಉತ್ಪಾದನೆ ವಿಪರೀತವಾಗಿ ಹೆಚ್ಚಾಗಿ ಬೆಲೆಗಳು ನೆಲಕಚ್ಚಿದಾಗ ರೈತರಿಗೆ ಆರ್ಥಿಕ ರಕ್ಷಣೆ ನೀಡಲು ಕೇಂದ್ರ ಮತ್ತು ರಾಜ್ಯ ಸರ್ಕಾರಗಳು ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP) ಯೋಜನೆಯನ್ನು ಜಾರಿಗೊಳಿಸುತ್ತವೆ:</p>

    <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 20px; border-radius: 8px; margin: 15px 0;">
      <h3 style="color: #065f46; margin-top: 0;">ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಗಳ ಕಾರ್ಯವಿಧಾನ:</h3>
      <ul style="margin-bottom: 0;">
        <li><strong>ಖರೀದಿ ಕೇಂದ್ರಗಳ ಸ್ಥಾಪನೆ:</strong> ತೊಗರಿ, ಕಡಲೆ, ರಾಗಿ, ಜೋಳ, ಭತ್ತ, ಹೆಸರುಕಾಳು ಮತ್ತು ಕೊಬ್ಬರಿ ಬೆಲೆಗಳು ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ MSP ಗಿಂತ ಕಡಿಮೆಯಾದಾಗ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ ಖರೀದಿ ಕೇಂದ್ರಗಳನ್ನು ತೆರೆಯುತ್ತದೆ.</li>
        <li><strong>FAQ ನಿಯಮಗಳು (Fair Average Quality):</strong> ಸರ್ಕಾರ ನಿಗದಿಪಡಿಸಿದ ಗುಣಮಟ್ಟದ ಮಾನದಂಡಗಳನ್ನು (ತೇವಾಂಶ ಮಿತಿ ಸಾಮಾನ್ಯವಾಗಿ 12% ಒಳಗೆ, ಧೂಳು ರಹಿತ ಮತ್ತು ಕೀಟಬಾಧೆ ಇಲ್ಲದಿರುವುದು) ಹೊಂದಿರುವ ಮಾಲನ್ನು ಮಾತ್ರ ಬೆಂಬಲ ಬೆಲೆಯಲ್ಲಿ ಖರೀದಿಸಲಾಗುತ್ತದೆ.</li>
        <li><strong>ಫ್ರೂಟ್ಸ್ ಐಡಿ (FRUITS ID) ಕಡ್ಡಾಯ:</strong> ರೈತರು ತಮ್ಮ ಪಹಣಿ (RTC) ಆಧಾರಿತ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ FRUITS ತಂತ್ರಾಂಶದಲ್ಲಿ ನೋಂದಾಯಿಸಿಕೊಂಡು ಬೆಂಬಲ ಬೆಲೆ ಕೇಂದ್ರಗಳಲ್ಲಿ ಮಾಲು ನೀಡಿ ಹಣ ಪಡೆಯಬಹುದು.</li>
      </ul>
    </div>
  </section>

  <!-- SECTION 6 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">6. ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಪಡೆಯಲು ರೈತರಿಗೆ 5 ಪ್ರಮುಖ ತಂತ್ರಗಳು</h2>
    <ol style="padding-left: 20px;">
      <li><strong>ಗ್ರೇಡಿಂಗ್ ಮತ್ತು ಕ್ಲೀನಿಂಗ್ (Grading at Farm Gate):</strong> ಹೊಲದಲ್ಲೇ ಮಾಲನ್ನು ದೊಡ್ಡ ಗಾತ್ರ, ಮಧ್ಯಮ ಗಾತ್ರ ಮತ್ತು ಸಣ್ಣ ಗಾತ್ರಗಳಾಗಿ ಪ್ರತ್ಯೇಕಿಸಿ. ಮಿಶ್ರಣ ಮಾಡಿ ತಂದರೆ ಇಡೀ ರಾಶಿಗೆ ಸಣ್ಣ ಗಾತ್ರದ ಕಳಪೆ ಬೆಲೆಯೇ ಸಿಗುತ್ತದೆ.</li>
      <li><strong>ತೇವಾಂಶ ನಿಯಂತ್ರಣ (Proper Moisture Drying):</strong> ಮೆಣಸಿನಕಾಯಿ, ಅಡಿಕೆ, ಧಾನ್ಯಗಳು ಮತ್ತು ಕಾಳುಗಳನ್ನು ಸರಿಯಾಗಿ ಬಿಸಿಲಿನಲ್ಲಿ ಒಣಗಿಸಿ ತಂದರೆ ತೂಕ ಕಡಿತ ಮತ್ತು ದರ ಕಡಿತ ತಪ್ಪುತ್ತದೆ.</li>
      <li><strong>ಹಬ್ಬ ಮತ್ತು ಸೀಸನ್ ಆಧರಿತ ಬಿತ್ತನೆ:</strong> ಮಾರುಕಟ್ಟೆಗೆ ಒಟ್ಟಿಗೆ ಎಲ್ಲರ ಮಾಲು ಬರುವ ಪೀಕ್ ಸೀಸನ್ನಲ್ಲಿ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ. ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ ಅಥವಾ ತಡವಾಗಿ ಬೆಳೆ ಬರುವಂತೆ ಬಿತ್ತನೆ ಯೋಜನೆ ರೂಪಿಸಿದರೆ ಗರಿಷ್ಠ ಬೆಲೆ ಪಡೆಯಬಹುದು.</li>
      <li><strong>ವಖಾರ ನಿಗಮದ ಗೋದಾಮುಗಳ ಬಳಕೆ (Warehouse Receipt Finance):</strong> ಬೆಲೆ ತೀರಾ ಕಡಿಮೆಯಿದ್ದಾಗ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಉಗ್ರಾಣ ನಿಗಮದ (KSWC) ಗೋದಾಮುಗಳಲ್ಲಿ ಮಾಲನ್ನು ಸಂಗ್ರಹಿಸಿ, ಗೋದಾಮು ರಸೀದಿ ಮೇಲೆ ಬ್ಯಾಂಕಿನಿಂದ 70% ಸಾಲ ಪಡೆದು, ಬೆಲೆ ಏರಿದಾಗ ಮಾರಾಟ ಮಾಡಬಹುದು.</li>
      <li><strong>ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆಗಳು (FPO - Farmer Producer Organisations):</strong> ಸಣ್ಣ ರೈತರು ಒಗ್ಗೂಡಿ ಎಫ್ಪಿಒ ಮೂಲಕ ಸಾಮೂಹಿಕವಾಗಿ ನೇರ ಕಾರ್ಪೊರೇಟ್ ಕಂಪನಿಗಳಿಗೆ ಅಥವಾ ರಫ್ತುದಾರರಿಗೆ ಮಾರಾಟ ಮಾಡಿದರೆ ಮಂಡಿ ಶುಲ್ಕ ಉಳಿದು 20% ಹೆಚ್ಚುವರಿ ಲಾಭ ಸಿಗುತ್ತದೆ.</li>
    </ol>
  </section>

  <!-- SECTION 7 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">7. APMC ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ರೈತರ ಕಾನೂನುಬದ್ಧ ಹಕ್ಕುಗಳು ಮತ್ತು ರಕ್ಷಣೆ</h2>
    <p>ಕರ್ನಾಟಕ APMC ಕಾಯ್ದೆಯ ಅಡಿಯಲ್ಲಿ ಪ್ರತಿಯೊಬ್ಬ ರೈತನಿಗೂ ಈ ಕೆಳಗಿನ ಹಕ್ಕುಗಳನ್ನು ಕಲ್ಪಿಸಲಾಗಿದೆ:</p>
    <ul style="padding-left: 20px;">
      <li><strong>ಕಮಿಷನ್ ಕಡಿತ ನಿಷೇಧ:</strong> ನಿಯಮಗಳ ಪ್ರಕಾರ ಕೃಷಿ ಉತ್ಪನ್ನ ತರುವ ರೈತರಿಂದ ಯಾವುದೇ ದಲ್ಲಾಳಿ ಅಥವಾ ವ್ಯಾಪಾರಿ ಕಮಿಷನ್ (Commission) ಕಡಿತ ಮಾಡುವಂತಿಲ್ಲ. ಕಮಿಷನ್ ಶುಲ್ಕವನ್ನು ಖರೀದಿದಾರ ವ್ಯಾಪಾರಿಯೇ ಭರಿಸಬೇಕು.</li>
      <li><strong>ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಡಿಜಿಟಲ್ ತೂಕ:</strong> ಮಾರುಕಟ್ಟೆ ಅಂಗಳದಲ್ಲಿ ತೂಕ ಮಾಪನ ಇಲಾಖೆಯಿಂದ ಮುದ್ರೆ ಪಡೆದ ಡಿಜಿಟಲ್ ತೂಕದ ಯಂತ್ರಗಳಲ್ಲೇ ತೂಕ ಮಾಡಬೇಕು. ರೈತರಿಗೆ ಅನುಮಾನ ಬಂದರೆ APMC ಕಚೇರಿಯ ಧರ್ಮಕಾಂಟಾದಲ್ಲಿ ಮರುತೂಕ ಮಾಡಿಸಿಕೊಳ್ಳುವ ಹಕ್ಕಿದೆ.</li>
      <li><strong>ತಕ್ಷಣದ ಪಾವತಿ ರಸೀದಿ:</strong> ಮಾಲು ಮಾರಾಟವಾದ ತಕ್ಷಣ ಅಧಿಕೃತ ಗಣಕೀಕೃತ ತೂಕದ ಚೀಟಿ ಮತ್ತು ದರ ಪಟ್ಟಿಯನ್ನು (Bill) ಪಡೆಯುವುದು ರೈತನ ಹಕ್ಕು.</li>
    </ul>
  </section>

  <!-- SECTION 8 -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">8. Karnata.in APMC ಲೈವ್ ಮಾರುಕಟ್ಟೆ ದರ ಪಟ್ಟಿಯನ್ನು ಬಳಸುವುದು ಹೇಗೆ?</h2>
    <p>ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ತಕ್ಷಣ ಪರಿಶೀಲಿಸಲು ಈ ಕೆಳಗಿನ ಆಯ್ಕೆಗಳನ್ನು ಬಳಸಿ:</p>
    <ul style="padding-left: 20px;">
      <li><strong>ಜಿಲ್ಲೆ ಮತ್ತು ಮಂಡಿ ಆಯ್ಕೆ:</strong> ಡ್ರಾಪ್ಡೌನ್ ಮೆನುವಿನಿಂದ ನಿಮ್ಮ ಹತ್ತಿರದ APMC ಮಾರುಕಟ್ಟೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.</li>
      <li><strong>ಬೆಳೆ ಆಯ್ಕೆ (Commodity Filter):</strong> ನೀವು ಮಾರಾಟ ಮಾಡಲು ಬಯಸುವ ಬೆಳೆ (ಉದಾ: ಟೊಮ್ಯಾಟೋ, ಈರುಳ್ಳಿ, ಅಡಿಕೆ, ಕೊಬ್ಬರಿ, ಹತ್ತಿ, ಮೆಣಸಿನಕಾಯಿ) ಅನ್ನು ಸೆಲೆಕ್ಟ್ ಮಾಡಿ.</li>
      <li><strong>ದೈನಂದಿನ ವಿಶ್ಲೇಷಣೆ:</strong> ಆಯಾ ಬೆಳೆಯ ಇಂದಿನ ಕನಿಷ್ಠ ಬೆಲೆ, ಗರಿಷ್ಠ ಬೆಲೆ, ಮಾದರಿ ಬೆಲೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆಗೆ ಬಂದಿರುವ ಒಟ್ಟು ಆವಕದ ಪ್ರಮಾಣವನ್ನು ಲೈವ್ ಆಗಿ ವೀಕ್ಷಿಸಿ.</li>
    </ul>
  </section>

  <!-- SECTION 9: FAQS -->
  <section>
    <h2 style="font-size: 22px; color: #1e293b; margin-top: 25px; font-weight: 600;">9. APMC ಮಾರುಕಟ್ಟೆ ಕುರಿತು ಪ್ರಮುಖ ಪ್ರಶ್ನೋತ್ತರಗಳು (FAQs)</h2>

    <div style="margin-top: 15px;">
      <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 1: APMC ಯಲ್ಲಿ ಬೆಲೆ ಕುಸಿದಾಗ ರೈತರಿಗೆ ರಕ್ಷಣೆ ನೀಡುವ ಯೋಜನೆಗಳಿವೆಯೇ?</h3>
      <p style="margin-top: 0; color: #475569;">ಹೌದು, ತೋಟಗಾರಿಕಾ ಮತ್ತು ಕೃಷಿ ಬೆಳೆಗಳ ಮಾರುಕಟ್ಟೆ ದರವು ಉತ್ಪಾದನಾ ವೆಚ್ಚಕ್ಕಿಂತ ಗಣನೀಯವಾಗಿ ಕುಸಿದಾಗ ರಾಜ್ಯ ಸರ್ಕಾರವು 'ಮಾರುಕಟ್ಟೆ ಮಧ್ಯಪ್ರವೇಶ ಯೋಜನೆ' (Market Intervention Scheme - MIS) ಅಥವಾ ಪ್ರೋತ್ಸಾಹಧನ ಯೋಜನೆಯನ್ನು ಜಾರಿಗೊಳಿಸಿ ರೈತರಿಗೆ ನಷ್ಟ ಪರಿಹಾರ ಒದಗಿಸುತ್ತದೆ.</p>

      <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 2: ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ ಮತ್ತು ಸಾಮಾನ್ಯ ಮೆಣಸಿನಕಾಯಿ ದರದಲ್ಲಿ ಏಕೆ ಇಷ್ಟೊಂದು ವ್ಯತ್ಯಾಸವಿರುತ್ತದೆ?</h3>
      <p style="margin-top: 0; color: #475569;">ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿಯಲ್ಲಿ (KDL & DABBI) ಖಾರ ಕಡಿಮೆ ಇದ್ದು ನೈಸರ್ಗಿಕ ಕೆಂಪು ಬಣ್ಣ (ASTA Color Value) ಮತ್ತು ತೈಲದ ಅಂಶ ಅತ್ಯಂತ ಹೆಚ್ಚಾಗಿರುತ್ತದೆ. ಮಸಾಲೆ ಕಂಪನಿಗಳು, ಸೌಂದರ್ಯವರ್ಧಕ ಮತ್ತು ಲಿಪ್ಸ್ಟಿಕ್ ತಯಾರಿಕಾ ಉದ್ಯಮಗಳು ಈ ಬಣ್ಣದ ಸಾರಕ್ಕಾಗಿ ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿಗೆ ಅಂತಾರಾಷ್ಟ್ರೀಯ ಪ್ರೀಮಿಯಂ ದರವನ್ನು ನೀಡುತ್ತವೆ.</p>

      <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 3: ಅಡಿಕೆ ಮಾರಾಟದಲ್ಲಿ 'ಚಾಲಿ' ಮತ್ತು 'ರಾಶಿ' ಅಡಿಕೆಯ ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು?</h3>
      <p style="margin-top: 0; color: #475569;">ಚಾಲಿ ಅಡಿಕೆ (White Arecanut) ಎಂದರೆ ಪೂರ್ಣ ಬಲಿತ ಹಣ್ಣಡಿಕೆಯನ್ನು ಸಿಪ್ಪೆ ಸಹಿತ ಬಿಸಿಲಿನಲ್ಲಿ ಒಣಗಿಸಿ ನಂತರ ಸಿಪ್ಪೆ ತೆಗೆದು ಸಂಸ್ಕರಿಸಿದ ಬಿಳಿ ಅಡಿಕೆ (ಕರಾವಳಿ ಭಾಗದಲ್ಲಿ ಹೆಚ್ಚು). ರಾಶಿ ಅಡಿಕೆ (Red Arecanut) ಎಂದರೆ ಎಳೆಯ ಅಡಿಕೆಯನ್ನು ಸುಲಿದು, ಬೇಯಿಸಿ, ರಸದಲ್ಲಿ ಅದ್ದಿ ಒಣಗಿಸಿದ ಕೆಂಪು ಅಡಿಕೆ (ಶಿವಮೊಗ್ಗ, ಚಿತ್ರದುರ್ಗ, ಚಿಕ್ಕಮಗಳೂರು ಭಾಗದಲ್ಲಿ ಹೆಚ್ಚು).</p>

      <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 4: ಒಬ್ಬ ವ್ಯಾಪಾರಿ ರೈತನಿಗೆ ಹಣ ಪಾವತಿಸದೆ ವಂಚಿಸಿದರೆ ಎಲ್ಲಿ ದೂರು ನೀಡಬೇಕು?</h3>
      <p style="margin-top: 0; color: #475569;">ಸಂಬಂಧಪಟ್ಟ APMC ಮಾರುಕಟ್ಟೆಯ ಕಾರ್ಯದರ್ಶಿ (APMC Secretary) ಅವರಿಗೆ ತಕ್ಷಣವೇ ಲಿಖಿತ ದೂರು ನೀಡಬೇಕು. APMC ಕಾಯ್ದೆಯಡಿ ಕಾರ್ಯದರ್ಶಿಯವರು ವ್ಯಾಪಾರಿಯ ಲೈಸೆನ್ಸ್ ರದ್ದುಪಡಿಸಿ, ಅವರ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಮುಟ್ಟುಗೋಲು ಹಾಕಿಕೊಂಡು ರೈತನಿಗೆ ಬಾಕಿ ಹಣ ಕೊಡಿಸುವ ಕಾನೂನು ಅಧಿಕಾರ ಹೊಂದಿರುತ್ತಾರೆ.</p>

      <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 5px;">ಪ್ರಶ್ನೆ 5: ರೈತರು ತಮ್ಮ ತೋಟದಲ್ಲೇ ನೇರವಾಗಿ ಕಂಪನಿಗಳಿಗೆ ಮಾಲು ಮಾರಾಟ ಮಾಡಬಹುದೇ?</h3>
      <p style="margin-top: 0; color: #475569;">ಹೌದು, ಕರ್ನಾಟಕ ಕೃಷಿ ಉತ್ಪನ್ನ ಮಾರುಕಟ್ಟೆ ವ್ಯವಹಾರ (ನಿಯಂತ್ರಣ ಮತ್ತು ಅಭಿವೃದ್ಧಿ) ತಿದ್ದುಪಡಿ ಕಾಯ್ದೆಯ ಪ್ರಕಾರ ರೈತರು ತಮ್ಮ ಹೊಲದಲ್ಲೇ ನೇರವಾಗಿ ಖಾಸಗಿ ಕಂಪನಿಗಳಿಗೆ ಅಥವಾ ಗ್ರಾಹಕರಿಗೆ ಯಾವುದೇ ಮಂಡಿ ಸೆಸ್ ಇಲ್ಲದೆ ಮಾರಾಟ ಮಾಡಲು ಸಂಪೂರ್ಣ ಮುಕ್ತ ಅವಕಾಶವಿದೆ.</p>
    </div>
  </section>

  <!-- SUMMARY DISCLAIMER -->
  <footer style="margin-top: 30px; padding: 15px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; font-size: 13px; color: #166534;">
    <strong>ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ ಹಕ್ಕುತ್ಯಾಗ:</strong> Karnata.in ನಲ್ಲಿ ಪ್ರಕಟವಾಗುವ APMC ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳನ್ನು ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ (KSAMB), ReMS ಪೋರ್ಟಲ್ ಮತ್ತು ಕೇಂದ್ರ ಸರ್ಕಾರದ Agmarknet ದೈನಂದಿನ ಅಧಿಕೃತ ಬುಲೆಟಿನ್ಗಳ ಆಧಾರದ ಮೇಲೆ ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ. ನೈಜ ದರಗಳು ಗುಣಮಟ್ಟ, ತೇವಾಂಶ ಮತ್ತು ಹರಾಜಿನ ಸಮಯಕ್ಕೆ ಅನುಗುಣವಾಗಿ ವ್ಯತ್ಯಾಸವಾಗಬಹುದು.
  </footer>

</article>"""

# Full HTML template
full_html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="canonical" href="https://karnata.in/apmc-prices">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) | Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಅಧಿಕೃತ ಲೈವ್ ದರಗಳು ಮತ್ತು 24 ಪ್ರಮುಖ ಬೆಳೆಗಳ ಕಳೆದ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಬೆಲೆ ಏರಿಳಿತ ವಿಶ್ಲೇಷಣೆ (2016-2026). ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟದ ಸರಿಯಾದ ಸಮಯ, MSP ಮಾರ್ಗದರ್ಶಿ.">
  <meta name="keywords" content="APMC price Karnataka, 10 year crop price analysis, krama karnataka gov in, Karnataka mandi rates today, arecanut price trend, byadgi chilli rate, ragi msp, tomato price kolar">
  
  <!-- OpenGraph & Social SEO -->
  <meta property="og:title" content="APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) — Karnata.in">
  <meta property="og:description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಲೈವ್ ದರಗಳು & ಕಳೆದ 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ಏರಿಳಿತ ಮುನ್ಸೂಚನೆ. ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟಕ್ಕೆ ಸರಿಯಾದ ಸಮಯ!">
  <meta property="og:url" content="https://karnata.in/apmc-prices.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Karnata.in">
  <meta property="og:locale" content="kn_IN">
  <meta property="og:image" content="https://karnata.in/assets/icons/icon-512x512.png">

  <!-- Google Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/apmc-prices.html",
    "description": "Official Karnataka APMC agricultural market prices and 10-year historical seasonal price analyzer for farmers."
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  
  <!-- Chart.js for 10-Year Crop Trends -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="/data-loader.js"></script>
  <script src="/nav-component.js"></script>

  <style>
    :root {{
      --primary-dark: #0A3E20;
      --primary: #15803D;
      --primary-accent: #22C55E;
      --primary-light: #F0FDF4;
      --accent-gold: #D97706;
      --accent-bg: #FEF3C7;
      --danger-red: #DC2626;
      --danger-bg: #FEF2F2;
      --bg-slate: #F8FAFC;
      --card-white: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --radius-lg: 18px;
      --radius-md: 12px;
      --shadow-premium: 0 10px 30px -5px rgba(15, 23, 42, 0.07);
    }}
    
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Anek Kannada', sans-serif;
      background: var(--bg-slate);
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }}
    
    /* ════ HERO BANNER ════ */
    .apmc-hero {{
      background: linear-gradient(135deg, #062E18 0%, #0F5E32 50%, #15803D 100%);
      color: #FFFFFF;
      padding: 40px 20px 85px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid #FACC15;
    }}
    .apmc-hero::after {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 80% 20%, rgba(34, 197, 94, 0.25) 0%, transparent 60%);
      pointer-events: none;
    }}
    .apmc-hero h1 {{
      font-size: 32px;
      font-weight: 900;
      margin-bottom: 8px;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 10px rgba(0,0,0,0.35);
    }}
    .apmc-hero p {{
      font-size: 15px;
      color: #E2E8F0;
      max-width: 820px;
      margin: 0 auto 16px;
      font-weight: 500;
      line-height: 1.65;
    }}
    .hero-badge-row {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .apmc-hero-tag {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255,255,255,0.14);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 12.5px;
      font-weight: 800;
      color: #FEF08A;
    }}

    /* ════ TOP STATS BAR ════ */
    .stats-bar {{
      max-width: 1200px;
      margin: -50px auto 28px;
      padding: 0 16px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      position: relative;
      z-index: 10;
    }}
    @media (max-width: 900px) {{ .stats-bar {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 520px) {{ .stats-bar {{ grid-template-columns: 1fr; }} }}
    
    .stat-card {{
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px 16px;
      box-shadow: var(--shadow-premium);
      text-align: center;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }}
    .stat-card::before {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: linear-gradient(90deg, #22C55E, #15803D);
      opacity: 0;
      transition: opacity 0.25s;
    }}
    .stat-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -6px rgba(21, 128, 61, 0.15);
      border-color: #86EFAC;
    }}
    .stat-card:hover::before {{ opacity: 1; }}
    .stat-icon {{ font-size: 26px; margin-bottom: 4px; }}
    .stat-val {{ font-size: 24px; font-weight: 900; color: var(--primary-dark); font-family: 'Inter', sans-serif; }}
    .stat-lbl {{ font-size: 13px; font-weight: 800; color: var(--text-main); margin-top: 2px; }}
    .stat-sub {{ font-size: 11px; color: var(--text-muted); font-weight: 600; }}

    /* ════ MAIN WRAPPER ════ */
    .apmc-container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 16px 50px;
    }}

    /* ════ MODE SWITCHER TABS ════ */
    .mode-tabs {{
      display: flex;
      gap: 10px;
      background: #E2E8F0;
      padding: 6px;
      border-radius: 16px;
      margin-bottom: 28px;
    }}
    .mode-tab {{
      flex: 1;
      text-align: center;
      padding: 14px 20px;
      font-size: 16px;
      font-weight: 800;
      border-radius: 12px;
      cursor: pointer;
      border: none;
      background: transparent;
      color: var(--text-muted);
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-family: inherit;
    }}
    .mode-tab.active {{
      background: #FFFFFF;
      color: var(--primary-dark);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08);
      font-weight: 900;
    }}

    /* ══════════════════════════════════════════════════════
         SECTION 1: 10-YEAR CROP INTELLIGENCE ANALYZER
    ══════════════════════════════════════════════════════ */
    .analyzer-box {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 20px;
      padding: 28px;
      box-shadow: var(--shadow-premium);
      margin-bottom: 36px;
    }}
    .analyzer-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 2px solid #F1F5F9;
    }}
    .analyzer-title {{
      font-size: 22px;
      font-weight: 900;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .crop-selector-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 320px;
    }}
    .crop-select {{
      width: 100%;
      padding: 12px 18px;
      font-size: 15px;
      font-weight: 800;
      font-family: inherit;
      border: 2px solid var(--primary);
      border-radius: 14px;
      background: #F0FDF4;
      color: var(--primary-dark);
      cursor: pointer;
      outline: none;
      box-shadow: 0 2px 8px rgba(21, 128, 61, 0.08);
    }}
    .crop-select:focus {{
      border-color: #14532D;
      background: #FFFFFF;
    }}

    /* ANALYZER 2-COLUMN GRID */
    .analyzer-insights-grid {{
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 28px;
      margin-bottom: 28px;
    }}
    @media (max-width: 920px) {{ .analyzer-insights-grid {{ grid-template-columns: 1fr; }} }}

    /* CHART CARD WRAPPER */
    .chart-container-box {{
      background: #FAFCFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    }}
    .chart-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}
    .chart-badge {{
      background: #DCFCE7;
      color: #166534;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 20px;
      border: 1px solid #BBF7D0;
    }}

    /* 12-MONTH HEATMAP */
    .heatmap-card-box {{
      margin-top: 22px;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 16px;
    }}
    .season-heatmap {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 5px;
      margin-top: 12px;
    }}
    @media (max-width: 720px) {{ .season-heatmap {{ grid-template-columns: repeat(6, 1fr); gap: 6px; }} }}
    
    .heat-cell {{
      padding: 10px 4px;
      text-align: center;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 800;
      transition: transform 0.15s;
    }}
    .heat-cell:hover {{ transform: scale(1.06); }}
    .heat-cell.peak {{ background: #15803D; color: #FFFFFF; box-shadow: 0 2px 6px rgba(21, 128, 61, 0.3); }}
    .heat-cell.good {{ background: #86EFAC; color: #14532D; }}
    .heat-cell.avg {{ background: #FEF08A; color: #713F12; }}
    .heat-cell.low {{ background: #FCA5A5; color: #7F1D1D; }}
    .heat-cell.crash {{ background: #DC2626; color: #FFFFFF; box-shadow: 0 2px 6px rgba(220, 38, 38, 0.25); }}

    /* SMART ADVICE CARDS */
    .advice-card {{
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      margin-bottom: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .advice-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }}
    .advice-card.best-time {{
      background: #F0FDF4;
      border-color: #86EFAC;
    }}
    .advice-card.warning-time {{
      background: #FEF2F2;
      border-color: #FECACA;
    }}
    .advice-card.strategy-box {{
      background: #FFFBEB;
      border-color: #FDE68A;
    }}
    .advice-title {{
      font-size: 15px;
      font-weight: 900;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .advice-desc {{
      font-size: 14px;
      color: #334155;
      line-height: 1.65;
      font-weight: 500;
    }}

    /* PROFIT CALCULATOR WIDGET */
    .calculator-widget {{
      background: linear-gradient(135deg, #0F5E32 0%, #15803D 100%);
      color: #FFFFFF;
      border-radius: 18px;
      padding: 22px;
      box-shadow: 0 8px 24px rgba(21, 128, 61, 0.2);
    }}
    .calc-row {{
      display: flex;
      gap: 12px;
      align-items: center;
      margin-top: 14px;
      flex-wrap: wrap;
    }}
    .calc-input {{
      flex: 1;
      padding: 10px 14px;
      border-radius: 10px;
      border: 2px solid rgba(255,255,255,0.4);
      background: rgba(255,255,255,0.95);
      color: #0F172A;
      font-size: 15px;
      font-weight: 800;
      font-family: inherit;
      outline: none;
    }}
    .calc-result-box {{
      background: rgba(0,0,0,0.25);
      padding: 14px;
      border-radius: 12px;
      margin-top: 14px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      text-align: center;
    }}

    /* ════ RIGHT COLUMN WAREHOUSE PLEDGE LOAN WIDGET ════ */
    .warehouse-widget {{
      background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
      color: #FFFFFF;
      border-radius: 18px;
      padding: 22px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.2);
      border: 1.5px solid #334155;
    }}
    .wh-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 14px;
    }}
    .wh-item {{
      background: rgba(255,255,255,0.08);
      padding: 10px 12px;
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.12);
    }}
    .wh-lbl {{ font-size: 11px; opacity: 0.8; }}
    .wh-val {{ font-size: 15px; font-weight: 900; color: #38BDF8; font-family: 'Inter', sans-serif; margin-top: 2px; }}

    /* ════ ADVANCED FEATURES: 10-YEAR DATA TABLE & TIMELINE ════ */
    .history-table-box {{
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 22px;
      margin-top: 28px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .history-table-title {{
      font-size: 17px;
      font-weight: 900;
      color: var(--primary-dark);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .hist-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }}
    .hist-table th {{
      background: #F1F5F9;
      color: #334155;
      padding: 10px 12px;
      text-align: left;
      font-weight: 800;
      border-bottom: 2px solid #CBD5E1;
    }}
    .hist-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid #E2E8F0;
      color: #1E293B;
    }}
    .hist-table tr:hover {{
      background: #F8FAFC;
    }}
    .hist-growth-badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 11.5px;
      font-weight: 800;
      font-family: 'Inter', sans-serif;
    }}
    .hist-growth-badge.pos {{ background: #DCFCE7; color: #15803D; }}
    .hist-growth-badge.neg {{ background: #FEE2E2; color: #DC2626; }}

    /* DATA SOURCE CITATION BOX */
    .source-citation-box {{
      background: #F8FAFC;
      border: 1.5px solid #CBD5E1;
      border-radius: 14px;
      padding: 18px 22px;
      margin-top: 24px;
    }}
    .source-citation-title {{
      font-size: 14.5px;
      font-weight: 900;
      color: #1E293B;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .source-citation-list {{
      font-size: 13px;
      color: #475569;
      line-height: 1.7;
      padding-left: 20px;
    }}

    /* ══════════════════════════════════════════════════════
         SECTION 2: LIVE APMC MANDI RATES GRID
    ══════════════════════════════════════════════════════ */
    .controls-panel {{
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-premium);
    }}
    .filter-row {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 14px;
      margin-bottom: 16px;
    }}
    @media (max-width: 768px) {{ .filter-row {{ grid-template-columns: 1fr; }} }}
    
    .select-input, .search-input {{
      width: 100%;
      padding: 12px 16px;
      font-size: 14px;
      font-family: inherit;
      font-weight: 700;
      border: 1.5px solid var(--border);
      border-radius: 12px;
      background: #F8FAFC;
      color: var(--text-main);
      outline: none;
      transition: all 0.2s;
    }}
    .select-input:focus, .search-input:focus {{
      border-color: var(--primary);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
    }}

    .category-pills {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .category-pills::-webkit-scrollbar {{ display: none; }}
    .cat-pill {{
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 800;
      background: #F1F5F9;
      color: var(--text-muted);
      border: 1px solid var(--border);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .cat-pill.active, .cat-pill:hover {{
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
      box-shadow: 0 4px 12px rgba(21, 128, 61, 0.2);
    }}

    /* APMC CARDS 3-COLUMN GRID */
    .apmc-card-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
      margin-bottom: 36px;
    }}
    @media (max-width: 980px) {{ .apmc-card-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 620px) {{ .apmc-card-grid {{ grid-template-columns: 1fr; }} }}

    .mandi-card {{
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .mandi-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 28px -4px rgba(21, 128, 61, 0.15);
      border-color: #86EFAC;
    }}
    .mc-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}
    .mc-crop-name {{
      font-size: 17px;
      font-weight: 900;
      color: var(--text-main);
      line-height: 1.3;
    }}
    .mc-mandi {{
      font-size: 12.5px;
      font-weight: 800;
      color: var(--primary);
      margin-top: 3px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .mc-variety-pill {{
      font-size: 11px;
      background: #F1F5F9;
      color: #334155;
      padding: 3px 10px;
      border-radius: 20px;
      font-weight: 800;
      border: 1px solid #CBD5E1;
      white-space: nowrap;
    }}
    .mc-price-box {{
      background: #F0FDF4;
      border: 1.5px solid #BBF7D0;
      border-radius: 12px;
      padding: 14px;
      text-align: center;
      margin-bottom: 14px;
    }}
    .mc-modal-price {{
      font-size: 28px;
      font-weight: 900;
      color: var(--primary-dark);
      font-family: 'Inter', sans-serif;
    }}
    .mc-unit {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 700;
      margin-top: 2px;
    }}
    .mc-range-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      background: #F8FAFC;
      padding: 10px 12px;
      border-radius: 10px;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }}
    .mc-range-val {{
      font-weight: 900;
      color: var(--text-main);
      font-family: 'Inter', sans-serif;
    }}
    .mc-share-btn {{
      width: 100%;
      background: #10B981;
      color: #FFFFFF;
      border: none;
      padding: 10px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: inherit;
      transition: background 0.15s;
    }}
    .mc-share-btn:hover {{ background: #059669; }}
  </style>
</head>
<body>

  <!-- ════ HERO BANNER ════ -->
  <header class="apmc-hero">
    <div class="hero-badge-row">
      <div class="apmc-hero-tag">🌾 ಕರ್ನಾಟಕ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಮಂಡಳಿ (KSAMB) & ReMS ಲೈವ್ ಪೋರ್ಟಲ್</div>
      <div class="apmc-hero-tag" style="color:#BBF7D0; border-color:#86EFAC;">⚡ 100% ಅಧಿಕೃತ ದರಗಳು</div>
    </div>
    <h1 style="margin-top:14px;">APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ</h1>
    <p>ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ನೈಜ ದರಗಳು, ಕಳೆದ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಏರಿಳಿತ (2016-2026), ಗರಿಷ್ಠ ಬೆಲೆಯ ಸೀಸನ್ ಹಾಗೂ ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟದ ಸರಿಯಾದ ಸಮಯದ ಸ್ಮಾರ್ಟ್ ಮಾರ್ಗದರ್ಶಿ.</p>
    <div style="font-size:12.5px; color:#FEF08A; font-weight:800;" id="hero-update-date">🔴 ಅಧಿಕೃತ KRAMA ಲೈವ್ ನವೀಕರಣ: 2026-08-28 — krama.karnataka.gov.in</div>
  </header>

  <!-- ════ 4 SUMMARY STATS ════ -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-icon">🌾</div>
      <div class="stat-val" id="stat-total-records">6,697</div>
      <div class="stat-lbl">ಇಂದಿನ ದರ ನಮೂದುಗಳು</div>
      <div class="stat-sub">174 APMC ಮಂಡಿಗಳು (KRAMA Live)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📊</div>
      <div class="stat-val" id="stat-avg-price">₹4,680</div>
      <div class="stat-lbl">ರಾಜ್ಯ ಸರಾಸರಿ ಮಾದರಿ ದರ</div>
      <div class="stat-sub">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್ (100 Kg)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🔥</div>
      <div class="stat-val" id="stat-top-crop">₹56,500</div>
      <div class="stat-lbl">ಅತ್ಯಧಿಕ ಬೆಲೆಯ ಬೆಳೆ</div>
      <div class="stat-sub">ರಾಶಿ / ಚಾಲಿ ಅಡಿಕೆ</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📈</div>
      <div class="stat-val">24 ಬೆಳೆಗಳು</div>
      <div class="stat-lbl">10 ವರ್ಷಗಳ ಬೆಲೆ ಮುನ್ಸೂಚನೆ</div>
      <div class="stat-sub">2016 - 2026 ಐತಿಹಾಸಿಕ ವಿಶ್ಲೇಷಣೆ</div>
    </div>
  </div>

  <!-- ════ MAIN WRAPPER ════ -->
  <div class="apmc-container">

    <!-- MODE TABS -->
    <div class="mode-tabs">
      <button class="mode-tab active" id="tab-live" onclick="switchMode('live')">
        <span>🌾 ಇಂದಿನ ಲೈವ್ APMC ದರಗಳು (6,697 Mandi Rates)</span>
      </button>
      <button class="mode-tab" id="tab-analyzer" onclick="switchMode('analyzer')">
        <span>📈 ರೈತರ 10 ವರ್ಷಗಳ ಬೆಲೆ ವಿಶ್ಲೇಷಕ & ಮುನ್ಸೂಚನೆ (2016-2026)</span>
      </button>
    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 1: 10-YEAR CROP INTELLIGENCE ANALYZER
    ══════════════════════════════════════════════════════ -->
    <div id="view-analyzer" style="display:none;">
      
      <div class="analyzer-box">
        <div class="analyzer-header">
          <div class="analyzer-title">
            <span>📊 ರೈತರ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (Crop Rate & Seasonality Intelligence)</span>
          </div>
          <div class="crop-selector-wrap">
            <label style="font-size:14px; font-weight:800; white-space:nowrap; color:#14532D;">ಬೆಳೆ ಆಯ್ಕೆ ಮಾಡಿ:</label>
            <select id="analyzer-crop-select" class="crop-select" onchange="updateCropAnalysis()">
              <option value="arecanut">🌴 ಅಡಿಕೆ (Arecanut - Rashi/Chali)</option>
              <option value="paddy">🌾 ಸೋನಾ ಮಸೂರಿ ಭತ್ತ (Paddy)</option>
              <option value="byadgi_chilli">🌶️ ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ (Byadgi Dry Chilli)</option>
              <option value="tur_dal">🫘 ತೊಗರಿ ಬೇಳೆ (Red Gram / Tur Dal)</option>
              <option value="copra">🥥 ಕೊಬ್ಬರಿ & ತೆಂಗಿನಕಾಯಿ (Copra / Coconut)</option>
              <option value="cotton">☁️ ಹತ್ತಿ (Cotton - DCH/Bt)</option>
              <option value="ragi">🌾 ರಾಗಿ (Finger Millet / Ragi)</option>
              <option value="jowar">🌾 ಬಿಳಿ ಜೋಳ (Jowar / Maldandi)</option>
              <option value="maize">🌽 ಮೆಕ್ಕೆಜೋಳ (Maize)</option>
              <option value="onion">🧅 ಈರುಳ್ಳಿ (Onion)</option>
              <option value="tomato">🍅 ಟೊಮ್ಯಾಟೋ (Tomato)</option>
              <option value="potato">🥔 ಆಲೂಗಡ್ಡೆ (Potato)</option>
              <option value="coffee">☕ ಕಾಫಿ (Coffee - Arabica / Robusta)</option>
              <option value="ginger">🫚 ಶುಂಠಿ (Ginger)</option>
              <option value="garlic">🧄 ಬೆಳ್ಳುಳ್ಳಿ (Garlic)</option>
              <option value="turmeric">🟡 ಅರಿಶಿನ (Turmeric)</option>
              <option value="groundnut">🥜 ಶೇಂಗಾ / ಕಡಲೆಕಾಯಿ (Groundnut)</option>
              <option value="bengal_gram">🫘 ಕಡಲೆ (Bengal Gram / Chana)</option>
              <option value="green_gram">🫘 ಹೆಸರುಕಾಳು (Green Gram / Moong)</option>
              <option value="sunflower">🌻 ಸೂರ್ಯಕಾಂತಿ (Sunflower)</option>
              <option value="cardamom">🟢 ಏಲಕ್ಕಿ (Green Cardamom)</option>
              <option value="pepper">⚫ ಕಾಳುಮೆಣಸು (Black Pepper)</option>
              <option value="silk">🐛 ರೇಷ್ಮೆ ಗೂಡು (Silk Cocoon)</option>
              <option value="wheat">🌾 ಜವಾರಿ ಗೋಧಿ (Wheat)</option>
            </select>
          </div>
        </div>

        <!-- INSIGHTS GRID -->
        <div class="analyzer-insights-grid">
          
          <!-- LEFT: 10-Year Price Trend Chart & Heatmap & Calculator -->
          <div>
            <div class="chart-container-box">
              <div class="chart-header-row">
                <h3 style="font-size:16px; font-weight:900; color:#0f172a;" id="chart-heading">10 ವರ್ಷಗಳ ಬೆಲೆ ಪ್ರವೃತ್ತಿ (2016–2026)</h3>
                <span class="chart-badge" id="chart-cagr-badge">+101.7% ಬೆಳವಣಿಗೆ</span>
              </div>
              <div style="height:270px; position:relative;">
                <canvas id="cropTrendChart"></canvas>
              </div>
            </div>

            <!-- 12-Month Heatmap -->
            <div class="heatmap-card-box">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="font-size:14px; font-weight:900; color:#0f172a;">12 ತಿಂಗಳ ಬೆಲೆ ಏರಿಳಿತ ಹರಿವು (Seasonality Heatmap)</h4>
                <span style="font-size:11.5px; color:#15803D; font-weight:800;">ಹಸಿರು = ಗರಿಷ್ಠ ಬೆಲೆ</span>
              </div>
              <div class="season-heatmap" id="season-heatmap-grid"></div>
            </div>

            <!-- Crop Profit Calculator Widget (Left) -->
            <div class="calculator-widget" style="margin-top:22px;">
              <div style="display:flex; align-items:center; gap:8px; font-size:15px; font-weight:900;">
                <span>🧮 ಬೆಳೆ ಮಾರಾಟ ಲಾಭದ ಕ್ಯಾಲ್ಕುಲೇಟರ್</span>
              </div>
              <div style="font-size:12.5px; opacity:0.9; margin-top:2px;">ನಿಮ್ಮ ಬೆಳೆಯ ಪ್ರಮಾಣ ನಮೂದಿಸಿ, ಗರಿಷ್ಠ ಮತ್ತು ಕುಸಿತ ಸೀಸನ್ ನಡುವಿನ ಲಾಭದ ವ್ಯತ್ಯಾಸ ನೋಡಿ:</div>
              <div class="calc-row">
                <input type="number" id="calc-qty" class="calc-input" value="20" placeholder="ಕ್ವಿಂಟಾಲ್ ಪ್ರಮಾಣ (ಉದಾ: 20)" oninput="calculateCropProfit()">
                <span style="font-weight:800; font-size:14px;" id="calc-unit-label">ಕ್ವಿಂಟಾಲ್</span>
              </div>
              <div class="calc-result-box">
                <div>
                  <div style="font-size:11px; opacity:0.85;">ಗರಿಷ್ಠ ಸೀಸನ್ ಆದಾಯ:</div>
                  <div style="font-size:18px; font-weight:900; color:#86EFAC;" id="calc-peak-val">₹11,30,000</div>
                </div>
                <div>
                  <div style="font-size:11px; opacity:0.85;">ಕುಸಿತ ಸೀಸನ್ ಆದಾಯ:</div>
                  <div style="font-size:18px; font-weight:900; color:#FCA5A5;" id="calc-low-val">₹8,80,000</div>
                </div>
                <div style="grid-column:1/-1; border-top:1px solid rgba(255,255,255,0.2); padding-top:6px; font-size:12.5px; font-weight:800; color:#FEF08A;" id="calc-diff-val">
                  💡 ಸರಿಯಾದ ಸಮಯದಲ್ಲಿ ಮಾರಿದರೆ ಸಿಗುವ ನಿವ್ವಳ ಹೆಚ್ಚುವರಿ ಲಾಭ: +₹2,50,000
                </div>
              </div>
            </div>

          </div>

          <!-- RIGHT: AI Smart Advice & When to Sell & Warehouse Pledge Loan Widget -->
          <div>
            <!-- Best Time to Sell -->
            <div class="advice-card best-time">
              <div class="advice-title" style="color:#15803D;">
                <span>🟢 ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು? (Peak Price Window)</span>
              </div>
              <div class="advice-desc" id="adv-best-time"></div>
            </div>

            <!-- Price Drop Warning -->
            <div class="advice-card warning-time">
              <div class="advice-title" style="color:#DC2626;">
                <span>🔴 ಯಾವಾಗ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ? (Harvest Glut Warning)</span>
              </div>
              <div class="advice-desc" id="adv-worst-time"></div>
            </div>

            <!-- Smart Storage & Marketing Strategy -->
            <div class="advice-card strategy-box">
              <div class="advice-title" style="color:#92400E;">
                <span>💡 ರೈತರಿಗೆ ಸ್ಮಾರ್ಟ್ ಶೇಖರಣಾ ತಂತ್ರ & ಲಾಭದ ಲೆಕ್ಕ</span>
              </div>
              <div class="advice-desc" id="adv-strategy"></div>
            </div>

            <!-- MSP & Benchmark Stats -->
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:14px; margin-bottom:16px;">
              <div style="background:#F0FDF4; border:1.5px solid #BBF7D0; padding:14px; border-radius:14px; text-align:center;">
                <div style="font-size:11.5px; color:#15803D; font-weight:800;">ಸರ್ಕಾರಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP)</div>
                <div style="font-size:17px; font-weight:900; color:#14532D; margin-top:2px;" id="adv-msp"></div>
              </div>
              <div style="background:#FEF3C7; border:1.5px solid #FDE68A; padding:14px; border-radius:14px; text-align:center;">
                <div style="font-size:11.5px; color:#92400E; font-weight:800;">10 ವರ್ಷಗಳ ಒಟ್ಟು ಬೆಳವಣಿಗೆ</div>
                <div style="font-size:17px; font-weight:900; color:#78350F; margin-top:2px;" id="adv-cagr"></div>
              </div>
            </div>

            <!-- ════ NEW FEATURE BESIDE CALCULATOR: KSWC WAREHOUSE & PLEDGE LOAN WIDGET ════ -->
            <div class="warehouse-widget">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:900; display:flex; align-items:center; gap:6px;">
                  <span>🏛️ ಉಗ್ರಾಣ ಶೇಖರಣೆ & 7% ರಶೀದಿ ಸಾಲ ಗೈಡ್</span>
                </div>
                <span style="font-size:11px; background:#0284C7; padding:2px 8px; border-radius:10px; font-weight:800;">KSWC ಸಬ್ಸಿಡಿ</span>
              </div>
              <div style="font-size:12.5px; opacity:0.88; margin-top:4px;">
                ಬೆಲೆ ಕಡಿಮೆ ಇದ್ದಾಗ ತಕ್ಷಣ ಮಾರದೆ KSWC ಉಗ್ರಾಣದಲ್ಲಿರಿಸಿ e-NWR ರಶೀದಿ ಮೇಲೆ ಬ್ಯಾಂಕ್ ಸಾಲ ಪಡೆಯುವ ಲೆಕ್ಕಾಚಾರ:
              </div>
              <div class="wh-grid">
                <div class="wh-item">
                  <div class="wh-lbl">ತಿಂಗಳ ಉಗ್ರಾಣ ಶುಲ್ಕ (Subsidy)</div>
                  <div class="wh-val" id="wh-rent">₹4.50 / ಕ್ವಿಂಟಾಲ್</div>
                </div>
                <div class="wh-item">
                  <div class="wh-lbl">ಸಿಗುವ ಸಾಲ ಮೊತ್ತ (70% Value)</div>
                  <div class="wh-val" id="wh-loan">₹7,91,000</div>
                </div>
                <div class="wh-item">
                  <div class="wh-lbl">ಬಡ್ಡಿದರ (Pledge Loan Rate)</div>
                  <div class="wh-val" style="color:#FACC15;">7% ವಾರ್ಷಿಕ ರಿಯಾಯಿತಿ</div>
                </div>
                <div class="wh-item">
                  <div class="wh-lbl">4 ತಿಂಗಳ ಶೇಖರಣಾ ನಿವ್ವಳ ಲಾಭ</div>
                  <div class="wh-val" style="color:#4ADE80;" id="wh-net-gain">+₹1,68,000</div>
                </div>
              </div>
              <div style="margin-top:10px; font-size:11.5px; opacity:0.9; background:rgba(255,255,255,0.05); padding:8px; border-radius:8px;">
                📌 <strong>ರೈತರ ಗಮನಕ್ಕೆ:</strong> KSWC ಉಗ್ರಾಣಗಳಲ್ಲಿ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ 50% ಬಾಡಿಗೆ ರಿಯಾಯಿತಿ ಸಿಗುತ್ತದೆ. ಬೆಳೆ ಶೇಖರಿಸಿದ ರಶೀದಿಯನ್ನು ಬ್ಯಾಂಕಿಗೆ ನೀಡಿ ತುರ್ತು ಹಣ ಪಡೆಯಬಹುದು.
              </div>
            </div>

          </div>

        </div>

        <!-- ════ 10-YEAR HISTORICAL YEAR-BY-YEAR DATA TABLE & EVENTS ════ -->
        <div class="history-table-box">
          <div class="history-table-title">
            <span id="hist-table-heading">📋 ವರ್ಷಾವಾರು 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ದರ ಪಟ್ಟಿ & ಮಾರುಕಟ್ಟೆ ಘಟನೆಗಳು (2016–2026)</span>
            <span style="font-size:12px; color:#166534; background:#DCFCE7; padding:4px 12px; border-radius:20px; font-weight:800;">ಅಧಿಕೃತ ಇತಿಹಾಸ</span>
          </div>
          <div style="overflow-x:auto;">
            <table class="hist-table">
              <thead>
                <tr>
                  <th>ವರ್ಷ</th>
                  <th>ಸರಾಸರಿ ದರ (₹)</th>
                  <th>ಕನಿಷ್ಠ - ಗರಿಷ್ಠ ಶ್ರೇಣಿ</th>
                  <th>ವಾರ್ಷಿಕ ಬದಲಾವಣೆ (YoY %)</th>
                  <th>ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆ ಅಂಶ / ಕಾರಣ</th>
                </tr>
              </thead>
              <tbody id="hist-table-body"></tbody>
            </table>
          </div>
        </div>

        <!-- ════ OFFICIAL DATA SOURCES TRANSPARENCY ════ -->
        <div class="source-citation-box">
          <div class="source-citation-title">
            <span>🏛️ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಅಂಕಿ-ಅಂಶಗಳ ಅಧಿಕೃತ ಮೂಲಗಳು (Official Data Repositories)</span>
          </div>
          <ol class="source-citation-list">
            <li><strong>ಕೇಂದ್ರ ಕೃಷಿ ಸಚಿವಾಲಯದ ಆರ್ಥಿಕ ಮತ್ತು ಸಾಂಖ್ಯಿಕ ನಿರ್ದೇಶನಾಲಯ (DES, MoA&FW):</strong> 2016 ರಿಂದ 2026 ರ ವಾರ್ಷಿಕ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ವರದಿಗಳು (Agricultural Statistics at a Glance).</li>
            <li><strong>ಕೃಷಿ ವೆಚ್ಚ ಮತ್ತು ಬೆಲೆಗಳ ಆಯೋಗ (CACP):</strong> ಖಾರಿಫ್ ಮತ್ತು ಹಿಂಗಾರು ಬೆಳೆಗಳ ವಾರ್ಷಿಕ ಬೆಲೆ ನೀತಿ ವರದಿಗಳು ಹಾಗೂ ಉತ್ಪಾದನಾ ವೆಚ್ಚ ಲೆಕ್ಕಾಚಾರಗಳು.</li>
            <li><strong>ರಾಷ್ಟ್ರೀಯ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಪೋರ್ಟಲ್ (Agmarknet):</strong> ಕರ್ನಾಟಕದ ಮಂಡಿಗಳಲ್ಲಿ ದಾಖಲಾದ ಐತಿಹಾಸಿಕ ಮಾಸಿಕ ಆವಕ ಮತ್ತು ಮಾದರಿ ದರಗಳ ಸಂಗ್ರಹ.</li>
            <li><strong>ಕೇಂದ್ರ ಸಾಂಬಾರ ಮಂಡಳಿ & ಕ್ಯಾಂಪ್ಕೋ (CAMPCO / Spices Board / CSB):</strong> ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ಅಡಿಕೆ, ಕೊಬ್ಬರಿ, ಏಲಕ್ಕಿ, ಕಾಳುಮೆಣಸು ಮತ್ತು ರೇಷ್ಮೆ ಗೂಡುಗಳ ಅಧಿಕೃತ ವಹಿವಾಟು ದರಗಳು.</li>
            <li><strong>ಕರ್ನಾಟಕ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ (KSAMB & KRAMA):</strong> ರಾಜ್ಯದ 174 APMC ಮಾರುಕಟ್ಟೆಗಳ ಅಧಿಕೃತ ದೈನಂದಿನ ಮತ್ತು ಮಾಸಿಕ ಹರಾಜು ಬುಲೆಟಿನ್‌ಗಳು.</li>
          </ol>
        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 2: LIVE APMC MANDI RATES (6,697 Mandis)
    ══════════════════════════════════════════════════════ -->
    <div id="view-live">
      
      <!-- CONTROLS -->
      <div class="controls-panel">
        <div class="filter-row">
          <select id="market-select" class="select-input" onchange="filterData(true)">
            <option value="all">🏪 ಎಲ್ಲಾ ಮಾರುಕಟ್ಟೆಗಳು (All 174 Mandis)</option>
          </select>
          <select id="commodity-select" class="select-input" onchange="filterData(true)">
            <option value="all">🌾 ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳು (All Commodities)</option>
          </select>
          <input type="text" id="apmc-search" class="search-input" placeholder="🔍 ಬೆಳೆ ಹೆಸರು ಅಥವಾ ಮಾರುಕಟ್ಟೆ ಹುಡುಕಿ..." oninput="filterData(true)">
        </div>

        <div class="category-pills">
          <button class="cat-pill active" onclick="setCategory('all', this)">🌾 ಎಲ್ಲಾ ವಿಭಾಗಗಳು</button>
          <button class="cat-pill" onclick="setCategory('cash', this)">🌴 ವಾಣಿಜ್ಯ ಬೆಳೆ (Cash Crops)</button>
          <button class="cat-pill" onclick="setCategory('grain', this)">🌾 ಆಹಾರ ಧಾನ್ಯಗಳು (Grains)</button>
          <button class="cat-pill" onclick="setCategory('pulse', this)">🫘 ಬೇಳೆಕಾಳುಗಳು (Pulses)</button>
          <button class="cat-pill" onclick="setCategory('veg', this)">🥕 ತರಕಾರಿಗಳು (Vegetables)</button>
          <button class="cat-pill" onclick="setCategory('fruit', this)">🍎 ಹಣ್ಣುಗಳು (Fruits)</button>
          <button class="cat-pill" onclick="setCategory('spice', this)">🌶️ ಸಾಂಬಾರ ಪದಾರ್ಥ (Spices)</button>
          <button class="cat-pill" onclick="setCategory('oilseed', this)">🌻 ಎಣ್ಣೆಕಾಳು (Oilseeds)</button>
        </div>
      </div>

      <!-- CARDS GRID -->
      <div class="apmc-card-grid" id="apmc-card-grid"></div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         OFFICIAL 9-SECTION FARMER TRADE MANUAL ARTICLE
    ══════════════════════════════════════════════════════ -->
    {article_html}

  </div>

  <script>
    // ══════════════════════════════════════════════════════
    // COMPLETE 24 CROPS HISTORICAL DATABASE (2016–2026)
    // ══════════════════════════════════════════════════════
    const CROP_ANALYZER_DB = {crops_json_str};

    let currentMode = 'live';
    let chartInstance = null;
    let apmcData = [];
    let currentCat = 'all';

    function switchMode(mode) {{
      currentMode = mode;
      document.getElementById('tab-live').classList.toggle('active', mode === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', mode === 'analyzer');
      document.getElementById('view-live').style.display = mode === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = mode === 'analyzer' ? 'block' : 'none';
      
      if (mode === 'analyzer') {{
        updateCropAnalysis();
      }}
    }}

    function updateCropAnalysis() {{
      const select = document.getElementById('analyzer-crop-select');
      const cropKey = select ? select.value : 'arecanut';
      const data = CROP_ANALYZER_DB[cropKey] || CROP_ANALYZER_DB['arecanut'];

      document.getElementById('chart-heading').textContent = `${{data.name}} — 10 ವರ್ಷಗಳ ಬೆಲೆ ಇತಿಹಾಸ (2016–2026 ₹/${{data.unit}})`;
      document.getElementById('chart-cagr-badge').textContent = data.cagr.split(' ')[0] + ' ಬೆಳವಣಿಗೆ';
      document.getElementById('adv-best-time').textContent = data.bestTime;
      document.getElementById('adv-worst-time').textContent = data.worstTime;
      document.getElementById('adv-strategy').textContent = data.strategy;
      document.getElementById('adv-msp').textContent = data.msp;
      document.getElementById('adv-cagr').textContent = data.cagr;
      document.getElementById('calc-unit-label').textContent = data.unit;

      // Render 12-Month Heatmap
      const heatmapGrid = document.getElementById('season-heatmap-grid');
      heatmapGrid.innerHTML = '';
      data.seasonality.forEach(s => {{
        const cell = document.createElement('div');
        cell.className = `heat-cell ${{s.status}}`;
        cell.innerHTML = `<div>${{s.m}}</div><div style="font-size:9.5px; opacity:0.95; margin-top:2px;">${{s.lbl}}</div>`;
        heatmapGrid.appendChild(cell);
      }});

      // Render Historical Table
      renderHistoryTable(data);

      // Render Chart.js
      renderTrendChart(data);
      calculateCropProfit();
    }}

    function renderHistoryTable(data) {{
      document.getElementById('hist-table-heading').textContent = `📋 ${{data.name}} — ವರ್ಷಾವಾರು 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ದರ ಪಟ್ಟಿ & ಮಾರುಕಟ್ಟೆ ಘಟನೆಗಳು (2016–2026)`;
      const tbody = document.getElementById('hist-table-body');
      tbody.innerHTML = '';

      let prevPrice = null;
      data.history.forEach(item => {{
        let yoyBadge = '—';
        if (prevPrice !== null) {{
          const diff = ((item.price - prevPrice) / prevPrice) * 100;
          const isPos = diff >= 0;
          const sign = isPos ? '+' : '';
          const cls = isPos ? 'pos' : 'neg';
          yoyBadge = `<span class="hist-growth-badge ${{cls}}">${{sign}}${{diff.toFixed(1)}}%</span>`;
        }}
        prevPrice = item.price;

        const minMaxStr = item.min ? `₹${{item.min.toLocaleString('en-IN')}} - ₹${{item.max.toLocaleString('en-IN')}}` : '—';

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#0A3E20;">${{item.year}}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#15803D;">₹${{item.price.toLocaleString('en-IN')}} / ${{data.unit}}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">${{minMaxStr}}</td>
          <td>${{yoyBadge}}</td>
          <td style="font-size:13px; color:#334155;">${{item.event || 'ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ನಿರಂತರ ವಹಿವಾಟು'}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function calculateCropProfit() {{
      const select = document.getElementById('analyzer-crop-select');
      const cropKey = select ? select.value : 'arecanut';
      const data = CROP_ANALYZER_DB[cropKey] || CROP_ANALYZER_DB['arecanut'];

      const qtyInput = document.getElementById('calc-qty');
      const qty = parseFloat(qtyInput ? qtyInput.value : 20) || 1;

      const latestPrice = data.history[data.history.length-1].price;
      const peakTotal = Math.round(qty * (data.peakPrice || (latestPrice * 1.15)));
      const lowTotal = Math.round(qty * (data.lowPrice || (latestPrice * 0.78)));
      const diff = peakTotal - lowTotal;

      document.getElementById('calc-peak-val').textContent = `₹${{peakTotal.toLocaleString('en-IN')}}`;
      document.getElementById('calc-low-val').textContent = `₹${{lowTotal.toLocaleString('en-IN')}}`;
      document.getElementById('calc-diff-val').textContent = `💡 ಸರಿಯಾದ ಸಮಯದಲ್ಲಿ ಮಾರಿದರೆ ಸಿಗುವ ನಿವ್ವಳ ಹೆಚ್ಚುವರಿ ಲಾಭ: +₹${{diff.toLocaleString('en-IN')}}`;

      // Update Warehouse Widget
      const loanVal = Math.round(lowTotal * 0.70);
      const rentCost = Math.round(qty * 4.5 * 4); // 4 months rent
      const interestCost = Math.round(loanVal * 0.07 * (4/12));
      const netStorageGain = diff - (rentCost + interestCost);

      document.getElementById('wh-loan').textContent = `₹${{loanVal.toLocaleString('en-IN')}}`;
      document.getElementById('wh-net-gain').textContent = `+₹${{Math.max(0, netStorageGain).toLocaleString('en-IN')}}`;
    }}

    function renderTrendChart(crop) {{
      const ctx = document.getElementById('cropTrendChart').getContext('2d');
      if (chartInstance) {{
        chartInstance.destroy();
      }}

      const labels = crop.history.map(h => h.year);
      const prices = crop.history.map(h => h.price);

      // Create Gradient
      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(34, 197, 94, 0.35)');
      gradient.addColorStop(1, 'rgba(34, 197, 94, 0.0)');

      chartInstance = new Chart(ctx, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [{{
            label: `ಸರಾಸರಿ ದರ (₹/${{crop.unit}})`,
            data: prices,
            borderColor: '#15803D',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#0A3E20',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
            pointRadius: 6,
            pointHoverRadius: 8
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: '#0F172A',
              titleFont: {{ family: 'Inter', size: 12, weight: 'bold' }},
              bodyFont: {{ family: 'Inter', size: 13, weight: 'bold' }},
              padding: 10,
              cornerRadius: 8,
              callbacks: {{
                label: function(ctx) {{
                  return ` ದರ: ₹${{ctx.parsed.y.toLocaleString('en-IN')}} / ${{crop.unit}}`;
                }}
              }}
            }}
          }},
          scales: {{
            y: {{
              ticks: {{
                callback: function(v) {{ return '₹' + v.toLocaleString('en-IN'); }},
                font: {{ family: 'Inter', size: 11, weight: '600' }},
                color: '#64748B'
              }},
              grid: {{ color: '#E2E8F0', strokeDash: [4, 4] }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{ font: {{ family: 'Inter', size: 11, weight: 'bold' }}, color: '#334155' }}
            }}
          }}
        }}
      }});
    }}

    // ══════════════════════════════════════════════════════
    // LIVE APMC DATA LOADER & RENDERING
    // ══════════════════════════════════════════════════════
    function init() {{
      fetch('/data/apmc_prices.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {{
          let list = [];
          if (data && data.items && Array.isArray(data.items)) {{
            list = data.items;
          }} else if (data && data.payload && typeof window.decryptPayload === 'function') {{
            const dec = window.decryptPayload(data.payload);
            list = Array.isArray(dec) ? dec : (dec.items || []);
          }} else if (Array.isArray(data)) {{
            list = data;
          }}

          if (list && list.length > 0) {{
            apmcData = list;
            populateDropdowns();
            filterData(true);
            updateSummaryStats(list);
          }}
        }})
        .catch(e => console.warn("APMC Data load:", e));
    }}

    function updateSummaryStats(list) {{
      document.getElementById('stat-total-records').textContent = list.length.toLocaleString('en-IN');
      const sum = list.reduce((acc, curr) => acc + (curr.avg || 0), 0);
      const avg = Math.round(sum / list.length);
      document.getElementById('stat-avg-price').textContent = `₹${{avg.toLocaleString('en-IN')}}`;

      const top = list.reduce((maxItem, item) => (item.avg > maxItem.avg ? item : maxItem), list[0]);
      if (top) {{
        document.getElementById('stat-top-crop').textContent = `₹${{top.avg.toLocaleString('en-IN')}}`;
      }}
    }}

    function populateDropdowns() {{
      const selectMandi = document.getElementById('market-select');
      const markets = [...new Set(apmcData.map(d => d.market))].filter(Boolean).sort();
      selectMandi.innerHTML = '<option value="all">🏪 ಎಲ್ಲಾ ಮಾರುಕಟ್ಟೆಗಳು (All 174 Mandis)</option>';
      markets.forEach(m => {{
        const opt = document.createElement('option');
        opt.value = m;
        opt.textContent = `${{m}} APMC`;
        selectMandi.appendChild(opt);
      }});

      const selectComm = document.getElementById('commodity-select');
      const commodities = [...new Set(apmcData.map(d => (d.cropKn || d.cropEn || d.crop).split('/')[0].trim()))].filter(Boolean).sort();
      selectComm.innerHTML = '<option value="all">🌾 ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳು (All Commodities)</option>';
      commodities.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        selectComm.appendChild(opt);
      }});
    }}

    function setCategory(cat, btn) {{
      document.querySelectorAll('.cat-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCat = cat;
      filterData(true);
    }}

    function filterData(reset) {{
      const marketFilter = document.getElementById('market-select').value;
      const commodityFilter = document.getElementById('commodity-select').value;
      const searchTxt = document.getElementById('apmc-search').value.toLowerCase().trim();

      let filtered = apmcData;

      if (currentCat !== 'all') {{
        filtered = filtered.filter(d => d.cat === currentCat);
      }}
      if (marketFilter !== 'all') {{
        filtered = filtered.filter(d => d.market === marketFilter);
      }}
      if (commodityFilter !== 'all') {{
        filtered = filtered.filter(d => 
          (d.cropKn && d.cropKn.includes(commodityFilter)) ||
          (d.cropEn && d.cropEn.toLowerCase().includes(commodityFilter.toLowerCase())) ||
          (d.crop && d.crop.includes(commodityFilter))
        );
      }}
      if (searchTxt) {{
        filtered = filtered.filter(d => 
          (d.crop && d.crop.toLowerCase().includes(searchTxt)) ||
          (d.cropKn && d.cropKn.toLowerCase().includes(searchTxt)) ||
          (d.cropEn && d.cropEn.toLowerCase().includes(searchTxt)) ||
          (d.market && d.market.toLowerCase().includes(searchTxt)) ||
          (d.variety && d.variety.toLowerCase().includes(searchTxt))
        );
      }}

      renderGrid(filtered);
    }}

    function renderGrid(list) {{
      const grid = document.getElementById('apmc-card-grid');
      grid.innerHTML = '';

      if (list.length === 0) {{
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:50px 20px; color:#64748b; font-weight:800; font-size:16px;">🔍 ಯಾವುದೇ ಫಲಿತಾಂಶ ಕಂಡುಬಂದಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ಬೆಳೆ ಅಥವಾ ಮಾರುಕಟ್ಟೆ ಆಯ್ಕೆ ಮಾಡಿ.</div>';
        return;
      }}

      const displayList = list.slice(0, 180);
      displayList.forEach(item => {{
        const cropName = item.cropKn || item.cropEn || item.crop;
        const variety = item.variety || 'ಸಾಮಾನ್ಯ';
        const modalPrice = item.avg ? `₹${{item.avg.toLocaleString('en-IN')}}` : '—';
        const minPrice = item.min ? `₹${{item.min.toLocaleString('en-IN')}}` : '—';
        const maxPrice = item.max ? `₹${{item.max.toLocaleString('en-IN')}}` : '—';
        const arrivals = item.arrivals ? `${{item.arrivals.toLocaleString('en-IN')}} ಕ್ವಿಂಟಾಲ್` : 'ಮಂಡಿ ಲೈವ್';

        const card = document.createElement('div');
        card.className = 'mandi-card';
        card.innerHTML = `
          <div>
            <div class="mc-header">
              <div>
                <div class="mc-crop-name">${{cropName}}</div>
                <div class="mc-mandi">📍 ${{item.market}} APMC (${{item.district || 'ಕರ್ನಾಟಕ'}})</div>
              </div>
              <span class="mc-variety-pill">${{variety}}</span>
            </div>
            
            <div class="mc-price-box">
              <div style="font-size:11.5px; color:#15803D; font-weight:900;">ಇಂದಿನ ಮಾದರಿ ದರ (Modal Price)</div>
              <div class="mc-modal-price">${{modalPrice}}</div>
              <div class="mc-unit">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ (100 Kg)</div>
            </div>

            <div class="mc-range-grid">
              <div>ಕನಿಷ್ಠ: <span class="mc-range-val">${{minPrice}}</span></div>
              <div style="text-align:right;">ಗರಿಷ್ಠ: <span class="mc-range-val">${{maxPrice}}</span></div>
              <div style="grid-column:1/-1; margin-top:3px; font-size:11.5px;">ಆವಕ (Arrivals): <span style="font-weight:800; color:#0F172A;">${{arrivals}}</span></div>
            </div>
          </div>

          <button class="mc-share-btn" onclick="shareWhatsApp('${{cropName}}', '${{item.market}}', '${{modalPrice}}', '${{minPrice}}', '${{maxPrice}}')">
            <span>📲 WhatsApp ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ</span>
          </button>
        `;
        grid.appendChild(card);
      }});
    }}

    function shareWhatsApp(crop, market, modal, min, max) {{
      const text = `🌾 *Karnata.in — APMC ಮಾರುಕಟ್ಟೆ ದರ*\\n\\nಬೆಳೆ: *${{crop}}*\\nಮಾರುಕಟ್ಟೆ: *${{market}} APMC*\\nಇಂದಿನ ಮಾದರಿ ದರ: *${{modal}} / ಕ್ವಿಂಟಾಲ್*\\nಕನಿಷ್ಠ: ${{min}} | ಗರಿಷ್ಠ: ${{max}}\\n\\nಎಲ್ಲಾ 174 APMC ಮಾರುಕಟ್ಟೆಗಳ ಲೈವ್ ದರ ಹಾಗೂ 10 ವರ್ಷಗಳ ಬೆಲೆ ಮುನ್ಸೂಚನೆ ವೀಕ್ಷಿಸಿ:\\nhttps://karnata.in/apmc-prices.html`;
      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(text), '_blank');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      init();
    }});
  </script>
</body>
</html>
"""

with open("apmc-prices.html", "w", encoding="utf-8") as f:
    f.write(full_html)

with open("namma-karnataka/apmc-prices.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("SUCCESS_PERMANENTLY_EMBEDDED_EXACT_ARTICLE")
