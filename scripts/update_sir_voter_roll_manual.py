# -*- coding: utf-8 -*-
"""
Karnata — scripts/update_sir_voter_roll_manual.py
Integrates the new creative SIR Electoral Roll Manual & Guide into
karnataka-sir-voter-roll.html and karnataka-sir-voter-roll/index.html.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

sir_manual_html = """<!-- KARNATA.IN CREATIVE SIR ELECTORAL ROLL MANUAL -->
<style>
  .sir-wrapper {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif, 'Noto Sans Kannada';
    color: #1e293b;
    line-height: 1.85;
    background: #ffffff;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    padding: 30px;
    box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.07);
    margin: 40px auto;
    max-width: 1100px;
  }
  .sir-hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #312e81 100%);
    color: #ffffff;
    padding: 40px 30px;
    border-radius: 16px;
    position: relative;
    overflow: hidden;
    margin-bottom: 35px;
  }
  .sir-hero::after {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, rgba(0,0,0,0) 70%);
    border-radius: 50%;
  }
  .sir-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(8px);
    color: #a5b4fc;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 16px;
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin-bottom: 15px;
    letter-spacing: 0.5px;
  }
  .sir-title {
    font-size: 28px;
    font-weight: 800;
    line-height: 1.35;
    margin: 0 0 15px 0;
    color: #ffffff;
  }
  .sir-subtitle {
    font-size: 15px;
    color: #cbd5e1;
    margin: 0;
  }
  .sir-section-title {
    font-size: 22px;
    font-weight: 700;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 40px 0 20px 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #f1f5f9;
  }
  .sir-section-title span.num {
    background: #4f46e5;
    color: #fff;
    font-size: 14px;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    font-weight: bold;
  }
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 16px;
    margin: 25px 0;
  }
  .stat-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .stat-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
  }
  .stat-label {
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
  }
  .stat-value {
    font-size: 24px;
    font-weight: 800;
    margin: 8px 0;
    color: #0f172a;
  }
  .stat-tag-red { color: #dc2626; background: #fee2e2; padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: 600; }
  .stat-tag-green { color: #16a34a; background: #dcfce7; padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: 600; }
  .stat-tag-amber { color: #d97706; background: #fef3c7; padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: 600; }

  /* TIMELINE UI */
  .timeline-container {
    position: relative;
    padding: 20px 0 20px 30px;
    margin: 25px 0;
    border-left: 3px solid #6366f1;
  }
  .timeline-item {
    position: relative;
    margin-bottom: 25px;
  }
  .timeline-item:last-child { margin-bottom: 0; }
  .timeline-dot {
    position: absolute;
    left: -38px;
    top: 5px;
    width: 14px;
    height: 14px;
    background: #6366f1;
    border-radius: 50%;
    border: 3px solid #ffffff;
    box-shadow: 0 0 0 3px #c7d2fe;
  }
  .timeline-date {
    font-weight: 700;
    color: #4338ca;
    font-size: 14px;
    margin-bottom: 4px;
  }
  .timeline-content {
    background: #f8fafc;
    padding: 14px 18px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    font-size: 14px;
  }

  /* CALLOUT BOXES */
  .alert-box-urgent {
    background: #fff1f2;
    border-left: 5px solid #e11d48;
    padding: 20px;
    border-radius: 10px;
    margin: 25px 0;
  }
  .court-card {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 1px solid #86efac;
    padding: 22px;
    border-radius: 12px;
    margin: 25px 0;
  }

  /* DOCUMENT GRID */
  .doc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 12px;
    margin: 15px 0;
  }
  .doc-item {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
  }
  .doc-icon {
    background: #e0e7ff;
    color: #4338ca;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
    flex-shrink: 0;
  }

  /* MODERN TABLE */
  .custom-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    border-radius: 10px;
    overflow: hidden;
    font-size: 14px;
  }
  .custom-table th {
    background: #0f172a;
    color: #ffffff;
    padding: 12px 16px;
    text-align: left;
  }
  .custom-table td {
    padding: 12px 16px;
    border-bottom: 1px solid #e2e8f0;
    background: #ffffff;
  }
  .custom-table tr:nth-child(even) td {
    background: #f8fafc;
  }

  /* FAQ CARDS */
  .faq-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 15px;
    transition: all 0.2s ease;
  }
  .faq-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .faq-q {
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 8px 0;
    display: flex;
    gap: 8px;
  }
  .faq-a {
    font-size: 14px;
    color: #475569;
    margin: 0;
  }
</style>

<article class="sir-wrapper">

  <!-- HERO SECTION -->
  <header class="sir-hero">
    <span class="sir-badge">&bull; ECI &amp; CEO KARNATAKA SPECIAL REVISION 2026</span>
    <h1 class="sir-title">ಕರ್ನಾಟಕ ವಿಶೇಷ ತೀವ್ರ ಮತದಾರರ ಪಟ್ಟಿ ಪರಿಷ್ಕರಣೆ (SIR): ಕರಡು ಪಟ್ಟಿ, 1.08 ಕೋಟಿ ಹೆಸರುಗಳ ಡಿಲೀಟ್, ನೋಟಿಸ್ ಹಂತ ಮತ್ತು ಮರುಸೇರ್ಪಡೆ ಸಮಗ್ರ ಕೈಪಿಡಿ</h1>
    <p class="sir-subtitle">2002ರ ಬಳಿಕ 24 ವರ್ಷಗಳ ನಂತರ ನಡೆದ ಐತಿಹಾಸಿಕ ಪರಿಷ್ಕರಣೆ &bull; ಹಕ್ಕು-ಆಕ್ಷೇಪಣೆ ಸಲ್ಲಿಕೆ &bull; 11 ಅಧಿಕೃತ ದಾಖಲೆಗಳು &bull; ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ತೀರ್ಪು</p>
  </header>

  <!-- SECTION 1 -->
  <section>
    <div class="sir-section-title">
      <span class="num">1</span>
      <span>ಪೀಠಿಕೆ: ಮತದಾನದ ಹಕ್ಕು ಮತ್ತು ತೀವ್ರ ಪರಿಷ್ಕರಣೆಯ ಮಹತ್ವ</span>
    </div>
    <p>ಪ್ರಜಾಪ್ರಭುತ್ವದ ಪರಮೋಚ್ಚ ಶಕ್ತಿಯೇ ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕನಿಗೆ ಸಂವಿಧಾನ ನೀಡಿರುವ ಮತದಾನದ ಹಕ್ಕು. ಆದರೆ ಚುನಾವಣೆಯ ದಿನದಂದು ನಿಮ್ಮ ಬಳಿ ವೋಟರ್ ಐಡಿ (EPIC Card) ಇದ್ದರೂ, ಅಧಿಕೃತ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ (Electoral Roll) ನಿಮ್ಮ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ನೀವು ಮತ ಚಲಾಯಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ. ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿ 2002 ರ ನಂತರ, ಅಂದರೆ ಬರೋಬ್ಬರಿ <strong>24 ವರ್ಷಗಳ ಬಳಿಕ</strong> ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗವು (ECI) <strong>ವಿಶೇಷ ತೀವ್ರ ಮತದಾರರ ಪಟ್ಟಿ ಪರಿಷ್ಕರಣೆ (Special Intensive Revision - SIR)</strong> ಆಂದೋಲನವನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಜಾರಿಗೊಳಿಸಿದೆ.</p>

    <p>ಬೂತ್ ಮಟ್ಟದ ಅಧಿಕಾರಿಗಳು (BLO) ಮನೆ-ಮನೆಗೆ ತೆರಳಿ ನಡೆಸಿದ ಈ ಸಮೀಕ್ಷೆಯ ನಂತರ ಕರ್ನಾಟಕ ಮುಖ್ಯ ಚುನಾವಣಾಧಿಕಾರಿಗಳ (CEO Karnataka) ಕಚೇರಿಯು ಪರಿಷ್ಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಬಿಡುಗಡೆ ಮಾಡಿದೆ. ಈ ಬೃಹತ್ ಪರಿಷ್ಕರಣೆಯಲ್ಲಿ ರಾಜ್ಯದ <strong>1 ಕೋಟಿ 7 ಲಕ್ಷಕ್ಕೂ ಅಧಿಕ ಮತದಾರರನ್ನು</strong> ಪಟ್ಟಿಯಿಂದ ಕೈಬಿಡಲಾಗಿದ್ದು (ASDDO ವರ್ಗ), <strong>43.81 ಲಕ್ಷಕ್ಕೂ ಹೆಚ್ಚು ಜನರಿಗೆ</strong> ನೋಟಿಸ್ ಜಾರಿ ಮಾಡಲಾಗುತ್ತಿದೆ. ನಿಮ್ಮ ಮತದಾನದ ಹಕ್ಕನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ಪ್ರತಿಯೊಬ್ಬರೂ ಅನುಸರಿಸಬೇಕಾದ ಸಂಪೂರ್ಣ ಕ್ರಮಗಳು ಇಲ್ಲಿವೆ.</p>
  </section>

  <!-- SECTION 2: STATS DASHBOARD -->
  <section>
    <div class="sir-section-title">
      <span class="num">2</span>
      <span>ಕರ್ನಾಟಕ SIR ಅಂಕಿಅಂಶಗಳ ಸಂಪೂರ್ಣ ಡ್ಯಾಶ್ಬೋರ್ಡ್</span>
    </div>
    
    <div class="stat-grid">
      <div class="stat-card">
        <div class="stat-label">ಪರಿಷ್ಕರಣೆಗೂ ಮುನ್ನ ಒಟ್ಟು ಮತದಾರರು</div>
        <div class="stat-value">5,54,32,314</div>
        <span class="stat-tag-amber">ಜೂನ್ 16 ರಲ್ಲಿದ್ದ ಒಟ್ಟು ಎಲೆಕ್ಟರ್ಸ್</span>
      </div>
      <div class="stat-card">
        <div class="stat-label">ಪ್ರಸ್ತುತ ಕರಡು ಪಟ್ಟಿಯ ಮತದಾರರು</div>
        <div class="stat-value">4,46,80,151</div>
        <span class="stat-tag-green">ಪ್ರಸ್ತುತ ಕರಡು ಪಟ್ಟಿ ಗಾತ್ರ</span>
      </div>
      <div class="stat-card">
        <div class="stat-label">ಡಿಲೀಟ್ ಆದ ಮತದಾರರು (ASDDO)</div>
        <div class="stat-value" style="color: #dc2626;">1,07,96,415</div>
        <span class="stat-tag-red">- 1.08 ಕೋಟಿ ಹೆಸರುಗಳು ರದ್ದು</span>
      </div>
      <div class="stat-card">
        <div class="stat-label">ನೋಟಿಸ್ ಪಡೆಯುತ್ತಿರುವ ಮತದಾರರು</div>
        <div class="stat-value" style="color: #d97706;">43,81,335</div>
        <span class="stat-tag-amber">ಒಟ್ಟು ಮತದಾರರ ಪೈಕಿ 9.82%</span>
      </div>
    </div>

    <!-- GENDER BREAKDOWN TABLE -->
    <table class="custom-table">
      <thead>
        <tr>
          <th>ಮತದಾರರ ವರ್ಗ</th>
          <th>ಜೂನ್ 16 ರಲ್ಲಿದ್ದ ಮತದಾರರು</th>
          <th>ಕರಡು ಪಟ್ಟಿಯಲ್ಲಿರುವ ಮತದಾರರು</th>
          <th>ರದ್ದುಗೊಂಡ ಹೆಸರುಗಳು</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ಪುರುಷ ಮತದಾರರು (Male)</strong></td>
          <td>2,75,89,406</td>
          <td>2,22,01,727</td>
          <td style="color: #dc2626; font-weight: bold;">- 53,87,679</td>
        </tr>
        <tr>
          <td><strong>ಮಹಿಳಾ ಮತದಾರರು (Female)</strong></td>
          <td>2,78,37,913</td>
          <td>2,24,75,553</td>
          <td style="color: #dc2626; font-weight: bold;">- 53,62,360</td>
        </tr>
        <tr>
          <td><strong>ತೃತೀಯ ಲಿಂಗಿಗಳು (Others)</strong></td>
          <td>4,995</td>
          <td>2,871</td>
          <td style="color: #dc2626; font-weight: bold;">- 2,124</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SECTION 3: ASDDO BREAKDOWN -->
  <section>
    <div class="sir-section-title">
      <span class="num">3</span>
      <span>ASDDO ವರ್ಗ ಎಂದರೇನು? 1.08 ಕೋಟಿ ಹೆಸರುಗಳು ಡಿಲೀಟ್ ಆಗಲು ಕಾರಣಗಳೇನು?</span>
    </div>
    
    <p>ಮನೆ-ಮನೆ ಪರಿಶೀಲನೆಯ ವೇಳೆ ಈ ಕೆಳಗಿನ 5 ಪ್ರಮುಖ ಕಾರಣಗಳಿಗಾಗಿ ಹೆಸರುಗಳನ್ನು ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ತೆಗೆದುಹಾಕಲಾಗಿದೆ:</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin: 20px 0;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-top: 4px solid #64748b; padding: 15px; border-radius: 8px;">
        <strong style="color: #0f172a; font-size: 15px;">A - Absent (ಗೈರುಹಾಜರಿ)</strong>
        <p style="font-size: 13px; color: #475569; margin: 6px 0 0 0;">ಬಿಎಲ್ಒಗಳು ಕನಿಷ್ಠ 2 ರಿಂದ 3 ಬಾರಿ ಮನೆಗೆ ಭೇಟಿ ನೀಡಿದರೂ ಪತ್ತೆಯಾಗದ ಮತದಾರರು.</p>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-top: 4px solid #0284c7; padding: 15px; border-radius: 8px;">
        <strong style="color: #0f172a; font-size: 15px;">S - Shifted (ಸ್ಥಳಾಂತರ)</strong>
        <p style="font-size: 13px; color: #475569; margin: 6px 0 0 0;">ಹಿಂದಿನ ವಾಸಸ್ಥಳವನ್ನು ಶಾಶ್ವತವಾಗಿ ತೊರೆದು ಬೇರೆ ನಗರ ಅಥವಾ ವಾರ್ಡ್ಗೆ ವಲಸೆ ಹೋದವರು.</p>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-top: 4px solid #ef4444; padding: 15px; border-radius: 8px;">
        <strong style="color: #0f172a; font-size: 15px;">D - Dead (ಮೃತಪಟ್ಟವರು)</strong>
        <p style="font-size: 13px; color: #475569; margin: 6px 0 0 0;">ಮರಣ ಪ್ರಮಾಣಪತ್ರ ಅಥವಾ ಕುಟುಂಬದವರ ದೃಢೀಕರಣದಿಂದ ರದ್ದುಗೊಂಡ ಮೃತ ಮತದಾರರು.</p>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-top: 4px solid #f59e0b; padding: 15px; border-radius: 8px;">
        <strong style="color: #0f172a; font-size: 15px;">D - Duplicate (ನಕಲಿ/ಪುನರಾವರ್ತನೆ)</strong>
        <p style="font-size: 13px; color: #475569; margin: 6px 0 0 0;">ಹಳ್ಳಿ ಮತ್ತು ಬೆಂಗಳೂರು ಎರಡೂ ಕಡೆ ಅಥವಾ ಒಂದೇ ವಾರ್ಡ್ನಲ್ಲಿ ಎರಡು ಬಾರಿ ಹೆಸರಿದ್ದವರ ಎಂಟ್ರಿ.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 4: TIMELINE -->
  <section>
    <div class="sir-section-title">
      <span class="num">4</span>
      <span>SIR 2026 ಪ್ರಮುಖ ದಿನಾಂಕಗಳು ಮತ್ತು ವೇಳಾಪಟ್ಟಿ (Action Deadlines)</span>
    </div>

    <div class="timeline-container">
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">ಆಗಸ್ಟ್ 24, 2026</div>
        <div class="timeline-content"><strong>ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ಪ್ರಕಟಣೆ:</strong> ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಸಾರ್ವಜನಿಕ ಪರಿಶೀಲನೆಗೆ ಕರಡು ಪಟ್ಟಿ ಮುಕ್ತ.</div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">ಆಗಸ್ಟ್ 24 ರಿಂದ ಸೆಪ್ಟೆಂಬರ್ 23, 2026 (ಕೇವಲ 30 ದಿನಗಳು)</div>
        <div class="timeline-content"><strong>ಹಕ್ಕು ಮತ್ತು ಆಕ್ಷೇಪಣೆಗಳ ಸಲ್ಲಿಕೆ (Claims Window):</strong> ಹೆಸರಿಲ್ಲದವರು ಫಾರ್ಮ್-6 ಮತ್ತು ತಿದ್ದುಪಡಿಗೆ ಫಾರ್ಮ್-8 ಸಲ್ಲಿಸಲು ಅವಕಾಶ.</div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">ಆಗಸ್ಟ್ 31, 2026 ರಿಂದ ಆರಂಭ</div>
        <div class="timeline-content"><strong>ನೋಟಿಸ್ ವಿತರಣೆ:</strong> 43.81 ಲಕ್ಷ ಮತದಾರರಿಗೆ ಬಿಎಲ್ಒಗಳಿಂದ ಮನೆ-ಮನೆಗೆ ನೋಟಿಸ್ ಹಸ್ತಾಂತರ.</div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">ಆಗಸ್ಟ್ 24 ರಿಂದ ಅಕ್ಟೋಬರ್ 22, 2026</div>
        <div class="timeline-content"><strong>ವಿಚಾರಣೆ ಮತ್ತು ವಿಲೇವಾರಿ ಹಂತ:</strong> ERO/AERO ಕಚೇರಿಗಳಲ್ಲಿ ದಾಖಲೆಗಳ ಭೌತಿಕ ಪರಿಶೀಲನೆ.</div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot" style="background: #10b981; box-shadow: 0 0 0 3px #a7f3d0;"></div>
        <div class="timeline-date" style="color: #059669;">ಅಕ್ಟೋಬರ್ 27, 2026</div>
        <div class="timeline-content" style="border-color: #86efac; background: #f0fdf4;"><strong>ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ ಪ್ರಕಟಣೆ (Final Electoral Roll):</strong> ಮುಂಬರುವ ಎಲ್ಲಾ ಚುನಾವಣೆಗಳಿಗೆ ಈ ಪಟ್ಟಿಯೇ ಅಂತಿಮ.</div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: STEP BY STEP VERIFICATION -->
  <section>
    <div class="sir-section-title">
      <span class="num">5</span>
      <span>ಕರಡು ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು ಪರಿಶೀಲಿಸುವ ವಿಧಾನ (5 ಹಂತಗಳು)</span>
    </div>

    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px; margin: 20px 0;">
      <ol style="padding-left: 20px; margin: 0;">
        <li style="margin-bottom: 12px;"><strong>ಅಧಿಕೃತ ಪೋರ್ಟಲ್ಗೆ ಭೇಟಿ ನೀಡಿ:</strong> ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗದ ಅಧಿಕೃತ ವೆಬ್ಸೈಟ್ <code>voters.eci.gov.in</code> ಅಥವಾ <code>ceo.karnataka.gov.in</code> ಗೆ ಲಾಗಿನ್ ಆಗಿ.</li>
        <li style="margin-bottom: 12px;"><strong>EPIC ಸಂಖ್ಯೆ ಮೂಲಕ ಹುಡುಕಿ:</strong> ನಿಮ್ಮ ಹಳೆಯ ವೋಟರ್ ಐಡಿ ಕಾರ್ಡ್ ಮೇಲಿರುವ 10 ಅಂಕಿಯ EPIC ನಂಬರ್ ನಮೂದಿಸಿ ಸರ್ಚ್ ಮಾಡಿ.</li>
        <li style="margin-bottom: 12px;"><strong>ವಿವರಗಳ ಮೂಲಕ ಹುಡುಕಿ:</strong> ಹೆಸರು ಬದಲಾಗಿದ್ದರೆ ನಿಮ್ಮ ಹೆಸರು, ತಂದೆ/ಗಂಡನ ಹೆಸರು, ವಯಸ್ಸು ಮತ್ತು ಜಿಲ್ಲೆ/ಕ್ಷೇತ್ರವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಹುಡುಕಿ.</li>
        <li style="margin-bottom: 12px;"><strong>ಮತಗಟ್ಟೆ ಸಂಖ್ಯೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:</strong> ಪ್ರತಿ ಬೂತ್ಗೆ 1,200 ಮತದಾರರ ಮಿತಿ ನಿಗದಿಪಡಿಸಿದ್ದರಿಂದ ಮತಗಟ್ಟೆಗಳು <strong>60,923 ಕ್ಕೆ ಏರಿಕೆಯಾಗಿವೆ</strong>. ನಿಮ್ಮ ಬೂತ್ ಬದಲಾಗಿದೆಯೇ ಗಮನಿಸಿ.</li>
        <li><strong>ಬಿಎಲ್ಒ ಸಂಪರ್ಕಿಸಿ:</strong> ಆನ್ಲೈನ್ನಲ್ಲಿ ಹೆಸರು ಸಿಗದಿದ್ದರೆ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಗ್ರಾಮ ಪಂಚಾಯತಿ ಅಥವಾ ವಾರ್ಡ್ ಕಚೇರಿಯಲ್ಲಿರುವ ಮುದ್ರಿತ ಪಟ್ಟಿಯಲ್ಲಿ ಖುದ್ದಾಗಿ ನೋಡಿ.</li>
      </ol>
    </div>
  </section>

  <!-- SECTION 6: NOTICE PROCESS & 11 DOCUMENTS -->
  <section>
    <div class="sir-section-title">
      <span class="num">6</span>
      <span>BLO ನೋಟಿಸ್ ಬಂದವರಿಗೆ ಕಡ್ಡಾಯ ನಿಯಮಾವಳಿ ಮತ್ತು 11 ದಾಖಲೆಗಳು</span>
    </div>

    <div class="alert-box-urgent">
      <strong style="color: #9f1239; font-size: 16px; display: block; margin-bottom: 6px;">&bull; ಕಡ್ಡಾಯ ಭೌತಿಕ ಹಾಜರಾತಿ ನಿಯಮ (Physical Appearance Mandatory):</strong>
      <p style="margin: 0; font-size: 14px; color: #881337;">ನೋಟಿಸ್ನಲ್ಲಿರುವ ಕ್ಯೂಆರ್ (QR) ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ ಆನ್ಲೈನ್ನಲ್ಲಿ ದಾಖಲೆ ಅಪ್ಲೋಡ್ ಮಾಡಿದರೂ ಕೂಡ, ಅಂತಿಮ ಪರಿಶೀಲನೆಗಾಗಿ ನೀವು <strong>ERO/AERO ಅಧಿಕಾರಿಯ ಮುಂದೆ ಖುದ್ದಾಗಿ ಹಾಜರಾಗಲೇಬೇಕು!</strong> ಗರಿಷ್ಠ ಎರಡು ಬಾರಿ ಮಾತ್ರ ನೋಟಿಸ್ ನೀಡಲಾಗುತ್ತದೆ; ಹಾಜರಾಗದಿದ್ದರೆ ಹೆಸರು ಶಾಶ್ವತವಾಗಿ ರದ್ದಾಗುತ್ತದೆ.</p>
    </div>

    <p><strong>ವಿಚಾರಣೆಗೆ ಹಾಜರಾಗುವಾಗ ಆಧಾರ್ ಕಾರ್ಡ್ ಜೊತೆಗೆ ಈ ಕೆಳಗಿನ 11 ಅಧಿಕೃತ ದಾಖಲೆಗಳಲ್ಲಿ ಒಂದನ್ನು ಕಡ್ಡಾಯವಾಗಿ ಕೊಂಡೊಯ್ಯಬೇಕು:</strong></p>

    <div class="doc-grid">
      <div class="doc-item"><span class="doc-icon">1</span> ಭಾರತೀಯ ಪಾಸ್ಪೋರ್ಟ್ (Passport)</div>
      <div class="doc-item"><span class="doc-icon">2</span> ಚಾಲನಾ ಪರವಾನಗಿ (Driving License)</div>
      <div class="doc-item"><span class="doc-icon">3</span> ಪ್ಯಾನ್ ಕಾರ್ಡ್ (PAN Card)</div>
      <div class="doc-item"><span class="doc-icon">4</span> ಸರ್ಕಾರಿ ನೌಕರರ ಸರ್ವಿಸ್ ಐಡಿ</div>
      <div class="doc-item"><span class="doc-icon">5</span> ಬ್ಯಾಂಕ್ / ಪೋಸ್ಟ್ ಆಫೀಸ್ ಪಾಸ್ಬುಕ್</div>
      <div class="doc-item"><span class="doc-icon">6</span> ಎನ್ಪಿಆರ್ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ (RGI Card)</div>
      <div class="doc-item"><span class="doc-icon">7</span> ನರೇಗಾ ಜಾಬ್ ಕಾರ್ಡ್ (MGNREGA)</div>
      <div class="doc-item"><span class="doc-icon">8</span> ಕಾರ್ಮಿಕ ಆರೋಗ್ಯ ವಿಮೆ ಕಾರ್ಡ್</div>
      <div class="doc-item"><span class="doc-icon">9</span> ಪಿಂಚಣಿ ಪಾವತಿ ಆದೇಶ (PPO Order)</div>
      <div class="doc-item"><span class="doc-icon">10</span> ಶಾಸಕರು/ಸಂಸದರ ಅಧಿಕೃತ ಐಡಿ</div>
      <div class="doc-item"><span class="doc-icon">11</span> ಅಂಗವಿಕಲರ UDID ಪ್ರಮಾಣಪತ್ರ</div>
    </div>
  </section>

  <!-- SECTION 7: FORMS COMPARISON -->
  <section>
    <div class="sir-section-title">
      <span class="num">7</span>
      <span>ಯಾವ ಉದ್ದೇಶಕ್ಕೆ ಯಾವ ಫಾರ್ಮ್ ಹಾಕಬೇಕು? (Forms Matrix)</span>
    </div>

    <table class="custom-table">
      <thead>
        <tr>
          <th>ಫಾರ್ಮ್ ಸಂಖ್ಯೆ</th>
          <th>ಉದ್ದೇಶ &amp; ಬಳಕೆ</th>
          <th>ಅರ್ಜಿ ಸಲ್ಲಿಸಲು ಅರ್ಹರು</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color: #4338ca; font-size: 15px;">ಫಾರ್ಮ್ 6 (Form-6)</strong></td>
          <td><strong>ಹೊಸ ಮತದಾರರ ಸೇರ್ಪಡೆ &amp; ಡಿಲೀಟ್ ಆದವರ ಮರುಸೇರ್ಪಡೆ</strong></td>
          <td>18 ವರ್ಷ ತುಂಬಿದ ಯುವಕರು ಮತ್ತು SIR ನಲ್ಲಿ ಹೆಸರು ಕೈಬಿಡಲಾದ ಅರ್ಹ ನಾಗರಿಕರು.</td>
        </tr>
        <tr>
          <td><strong>ಫಾರ್ಮ್ 6A (Form-6A)</strong></td>
          <td>ಅನಿವಾಸಿ ಭಾರತೀಯ ಮತದಾರರ ನೋಂದಣಿ (NRI Electors)</td>
          <td>ವಿದೇಶದಲ್ಲಿ ನೆಲೆಸಿರುವ ಭಾರತೀಯ ಪಾಸ್ಪೋರ್ಟ್ ಹೊಂದಿರುವ ನಾಗರಿಕರು.</td>
        </tr>
        <tr>
          <td><strong>ಫಾರ್ಮ್ 7 (Form-7)</strong></td>
          <td>ಆಕ್ಷೇಪಣೆ ಸಲ್ಲಿಕೆ &amp; ಅನರ್ಹರ ಹೆಸರು ತೆಗೆದುಹಾಕುವ ಅರ್ಜಿ</td>
          <td>ಮೃತ ವ್ಯಕ್ತಿಗಳ ಹೆಸರು ಡಿಲೀಟ್ ಮಾಡಲು ಅಥವಾ ನಕಲಿ ಎಂಟ್ರಿ ಆಕ್ಷೇಪಿಸಲು.</td>
        </tr>
        <tr>
          <td><strong style="color: #059669; font-size: 15px;">ಫಾರ್ಮ್ 8 (Form-8)</strong></td>
          <td><strong>ವಿಳಾಸ ಬದಲಾವಣೆ, ಕಾಗುಣಿತ ತಿದ್ದುಪಡಿ &amp; ಫೋಟೋ ಬದಲಾವಣೆ</strong></td>
          <td>ಸರಳೀಕೃತ ಫಾರ್ಮ್; ಒಂದೇ ಅರ್ಜಿಯಲ್ಲಿ ಗರಿಷ್ಠ 4 ತಿದ್ದುಪಡಿಗಳನ್ನು ಮಾಡಬಹುದು.</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SECTION 8: LEGAL RIGHTS & SUPREME COURT VERDICT -->
  <section>
    <div class="sir-section-title">
      <span class="num">8</span>
      <span>ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ತೀರ್ಪು ಮತ್ತು ನಾಗರಿಕರ ಸಾಂವಿಧಾನಿಕ ಹಕ್ಕುಗಳು</span>
    </div>

    <div class="court-card">
      <h3 style="color: #166534; margin-top: 0; font-size: 17px;">&bull; ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಮಹತ್ವದ ಆದೇಶ (ADR v. ECI - 2026 INSC 564):</h3>
      <p style="font-size: 14px; margin-bottom: 8px;"><strong>1. ಪೌರತ್ವ ರದ್ದಾಗುವುದಿಲ್ಲ:</strong> ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ಹೆಸರು ಕೈಬಿಟ್ಟ ಮಾತ್ರಕ್ಕೆ ವ್ಯಕ್ತಿಯ ಭಾರತೀಯ ಪೌರತ್ವ ರದ್ದಾಗುವುದಿಲ್ಲ. ಪೌರತ್ವ ಕಾಯ್ದೆ 1955 ರ ಅಡಿಯಲ್ಲಿ ಸಕ್ಷಮ ಪ್ರಾಧಿಕಾರ ಮಾತ್ರ ಪೌರತ್ವ ನಿರ್ಧರಿಸಲು ಸಾಧ್ಯ.</p>
      <p style="font-size: 14px; margin-bottom: 8px;"><strong>2. ನೈಸರ್ಗಿಕ ನ್ಯಾಯ ಪಾಲನೆ ಕಡ್ಡಾಯ:</strong> ನಿಯಮ 21A ಪ್ರಕಾರ ಮತದಾರನಿಗೆ ಶೋಕಾಸ್ ನೋಟಿಸ್ ಮತ್ತು ವಿಚಾರಣೆಯ ಅವಕಾಶ ನೀಡದೆ ಏಕಾಏಕಿ ಹೆಸರನ್ನು ರದ್ದುಗೊಳಿಸುವಂತಿಲ್ಲ.</p>
      <p style="font-size: 14px; margin-bottom: 0;"><strong>3. ಉದ್ಯೋಗ ನಿಮಿತ್ತ ಗೈರುಹಾಜರಿ:</strong> ಜನಪ್ರತಿನಿಧಿ ಕಾಯ್ದೆ ಸೆಕ್ಷನ್ 20(1A) ಪ್ರಕಾರ, ಕೆಲಸಕ್ಕಾಗಿ ತಾತ್ಕಾಲಿಕವಾಗಿ ಊರು ಬಿಟ್ಟವರನ್ನು ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ತೆಗೆದುಹಾಕಲು ಬರುವುದಿಲ್ಲ.</p>
    </div>

    <h3 style="font-size: 17px; color: #0f172a; margin-top: 20px;">ಅರ್ಜಿ ತಿರಸ್ಕೃತವಾದರೆ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಕೆಯ 3 ಹಂತಗಳು (Appeals Ladder):</h3>
    <ul style="padding-left: 20px; font-size: 14px;">
      <li><strong>ಮೊದಲ ಮೇಲ್ಮನವಿ (Section 24(a)):</strong> ERO ಆದೇಶದ ವಿರುದ್ಧ <strong>15 ದಿನಗಳೊಳಗೆ</strong> ಜಿಲ್ಲಾಧಿಕಾರಿಗಳಿಗೆ (DM/DC) ಲಿಖಿತ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಿ.</li>
      <li><strong>ಎರಡನೇ ಮೇಲ್ಮನವಿ (Section 24(b)):</strong> ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಆದೇಶದ ವಿರುದ್ಧ ಕರ್ನಾಟಕದ ಮುಖ್ಯ ಚುನಾವಣಾಧಿಕಾರಿಗಳಿಗೆ (CEO Karnataka) ₹5 ಶುಲ್ಕದೊಂದಿಗೆ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಿ.</li>
      <li><strong>ಹೈಕೋರ್ಟ್ ಮೊರೆ (Writ Petition):</strong> ಕಾನೂನುಬಾಹಿರವಾಗಿ ಮತದಾನದ ಹಕ್ಕು ಕಸಿದುಕೊಂಡರೆ ಸಂವಿಧಾನದ 226ನೇ ವಿಧಿಯಡಿ ಹೈಕೋರ್ಟ್ನಲ್ಲಿ ರಿಟ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.</li>
    </ul>
  </section>

  <!-- SECTION 9: FAQS -->
  <section>
    <div class="sir-section-title">
      <span class="num">9</span>
      <span>ಪದೇ ಪದೇ ಕೇಳಲಾಗುವ ಪ್ರಮುಖ ಪ್ರಶ್ನೋತ್ತರಗಳು (Comprehensive FAQs)</span>
    </div>

    <div class="faq-card">
      <div class="faq-q"><span>Q1.</span> ನನ್ನ ಬಳಿ ವೋಟರ್ ಐಡಿ (EPIC) ಇದೆ, ಆದರೂ ಕರಡು ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರಿಲ್ಲ ಏಕೆ?</div>
      <div class="faq-a">ವೋಟರ್ ಐಡಿ ಕೇವಲ ಗುರುತಿನ ಚೀಟಿ. ಸಮೀಕ್ಷೆಯ ವೇಳೆ ನೀವು ಮನೆಯಲ್ಲಿ ಸಿಗದಿದ್ದಾಗ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದಾಗ ಹೆಸರು ASDDO ಪಟ್ಟಿಗೆ ಸೇರಿರಬಹುದು. ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಕಾರ್ಡ್ ಇದ್ದರೂ ಮತದಾನ ಮಾಡಲು ಸಾಧ್ಯವಿಲ್ಲ. ತಕ್ಷಣವೇ ಫಾರ್ಮ್-6 ಸಲ್ಲಿಸಿ.</div>
    </div>

    <div class="faq-card">
      <div class="faq-q"><span>Q2.</span> ಹೆಸರು ಸೇರ್ಪಡೆ ಅಥವಾ ತಿದ್ದುಪಡಿಗೆ ಹಣ ಪಾವತಿಸಬೇಕೇ?</div>
      <div class="faq-a">ಇಲ್ಲ. ಚುನಾವಣಾ ಆಯೋಗದ ಪೋರ್ಟಲ್ನಲ್ಲಿ ಅಥವಾ ಬಿಎಲ್ಒ ಮೂಲಕ ಫಾರ್ಮ್-6, 7, 8 ಸಲ್ಲಿಸುವುದು ಸಂಪೂರ್ಣ ಉಚಿತ. ಯಾವುದೇ ಅಧಿಕಾರಿ ಅಥವಾ ಮಧ್ಯವರ್ತಿಗೆ ಹಣ ನೀಡುವ ಅಗತ್ಯವಿಲ್ಲ.</div>
    </div>

    <div class="faq-card">
      <div class="faq-q"><span>Q3.</span> ಮತದಾನದ ದಿನದಂದು ಬೂತ್ನಲ್ಲಿ 'ಟೆಂಡರ್ಡ್ ವೋಟ್' ಹಾಕಬಹುದೇ?</div>
      <div class="faq-a">ಇಲ್ಲ. ನಿಯಮ 49P ಪ್ರಕಾರ ಟೆಂಡರ್ಡ್ ವೋಟ್ ಚಲಾಯಿಸಲು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು ಇರಲೇಬೇಕು. ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಬೇರೆ ಯಾರಾದರೂ ನಕಲಿ ವೋಟ್ ಹಾಕಿದ್ದರೆ ಮಾತ್ರ ಇದು ಅನ್ವಯ. ಹೆಸರೇ ಇಲ್ಲದಿದ್ದರೆ ಮತದಾನ ಕೇಂದ್ರದೊಳಗೆ ಪ್ರವೇಶವಿರುವುದಿಲ್ಲ.</div>
    </div>

    <div class="faq-card">
      <div class="faq-q"><span>Q4.</span> ನಾಮಪತ್ರ ಸಲ್ಲಿಕೆಯ ಅಂತಿಮ ದಿನದ ಮಹತ್ವವೇನು?</div>
      <div class="faq-a">ಜನಪ್ರತಿನಿಧಿ ಕಾಯ್ದೆಯ ಸೆಕ್ಷನ್ 23(3) ರ ಪ್ರಕಾರ, ಯಾವುದೇ ಚುನಾವಣೆಯ ನಾಮಪತ್ರ ಸಲ್ಲಿಕೆಯ ಕೊನೆಯ ದಿನದ ನಂತರ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಯಾವುದೇ ಬದಲಾವಣೆ ಅಥವಾ ಹೊಸ ಹೆಸರು ಸೇರ್ಪಡೆ ಮಾಡಲು ಕಾನೂನಿನಲ್ಲಿ ಅವಕಾಶವಿರುವುದಿಲ್ಲ. ಆದ್ದರಿಂದ ಚುನಾವಣೆಗೂ ಮುನ್ನವೇ ಹೆಸರನ್ನು ಸರಿಪಡಿಸಿಕೊಳ್ಳಬೇಕು.</div>
    </div>
  </section>

  <!-- FOOTER DISCLAIMER -->
  <footer style="margin-top: 35px; padding: 20px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; font-size: 13px; color: #64748b; text-align: center;">
    <strong>ಅಧಿಕೃತ ಪ್ರಕಟಣೆ ಮತ್ತು ಜಾಗೃತಿ ಹಕ್ಕುತ್ಯಾಗ:</strong> ಈ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗ (ECI) ಮತ್ತು ಕರ್ನಾಟಕ ಮುಖ್ಯ ಚುನಾವಣಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (CEO Karnataka) ಹೊರಡಿಸಿರುವ ಅಧಿಕೃತ ಸುತ್ತೋಲೆಗಳು ಹಾಗೂ ಪ್ರಜಾಪ್ರತಿನಿಧಿ ಕಾಯ್ದೆ 1950 ರ ಆಧಾರದ ಮೇಲೆ ಸಾರ್ವಜನಿಕ ಜಾಗೃತಿಗಾಗಿ ಪ್ರಕಟಿಸಲಾಗಿದೆ. ಮತದಾರರು ತಮ್ಮ ವಿವರಗಳನ್ನು ಕಡ್ಡಾಯವಾಗಿ <code>voters.eci.gov.in</code> ನಲ್ಲಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ಕೋರಲಾಗಿದೆ.
  </footer>

</article>"""

target_files = [
    os.path.join(ROOT_DIR, 'karnataka-sir-voter-roll.html'),
    os.path.join(ROOT_DIR, 'karnataka-sir-voter-roll', 'index.html'),
    os.path.join(NK_DIR, 'karnataka-sir-voter-roll.html'),
    os.path.join(NK_DIR, 'karnataka-sir-voter-roll', 'index.html'),
]

for tf in target_files:
    if not os.path.exists(tf):
        continue
    with open(tf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace existing article (either .eroll-guide or .sir-wrapper)
    pattern = r'<!-- KARNATA\.IN CREATIVE SIR ELECTORAL ROLL MANUAL -->[\s\S]*?</article>|<article class=["\'](?:eroll-guide|sir-wrapper)[\s\S]*?</article>'
    if re.search(pattern, content):
        content = re.sub(pattern, sir_manual_html, content, count=1)
    else:
        # Insert before <div class="notice-bar">
        content = content.replace('<div class="notice-bar">', sir_manual_html + '\n\n    <div class="notice-bar">')

    with open(tf, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[OK] Updated {tf}")

print("SUCCESS_SIR_VOTER_ROLL_MANUAL_INTEGRATED")
