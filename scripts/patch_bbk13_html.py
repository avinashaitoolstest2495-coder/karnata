# -*- coding: utf-8 -*-
"""
Patch bigg-boss-kannada-13.html with live Week 8 / Day 53 internet updates.
"""
import re

HTML_PATH = "bigg-boss-kannada-13.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Hero eyebrow
content = content.replace(
    '<div class="eyebrow"><i class="fa-solid fa-plane-departure"></i> BBK13 WORLD TOUR • DAY 01 LIVE</div>',
    '<div class="eyebrow"><i class="fa-solid fa-plane-departure"></i> BBK13 WORLD TOUR • DAY 53 LIVE (ವಾರ 08)</div>'
)

# 2. Add Live Breaking News Ticker right after hero section
breaking_ticker = '''
    <!-- BREAKING LIVE UPDATES TICKER (DAY 53 / WEEK 8) -->
    <div class="live-radar-ticker" style="background:linear-gradient(90deg, rgba(239,68,68,0.18) 0%, rgba(15,23,42,0.95) 50%, rgba(245,158,11,0.18) 100%); border:1px solid rgba(239,68,68,0.5); border-radius:14px; padding:12px 18px; margin:16px 0 24px; display:flex; align-items:center; gap:14px; flex-wrap:wrap; box-shadow:0 0 25px rgba(239,68,68,0.2);">
      <div style="background:#EF4444; color:#FFF; font-size:0.75rem; font-weight:900; padding:5px 12px; border-radius:6px; display:inline-flex; align-items:center; gap:6px; letter-spacing:1px;">
        <span class="day-live-pulse" style="color:#FFF;">●</span> ಲೈವ್ ಬ್ರೇಕಿಂಗ್ (DAY 53)
      </div>
      <div style="flex:1; min-width:280px; font-family:var(--font-kannada); font-size:0.92rem; color:#F8FAFC;">
        <marquee behavior="scroll" direction="left" scrollamount="6" onmouseover="this.stop();" onmouseout="this.start();">
          🚨 <strong>ರೆಡ್ ಕಾರ್ಡ್ ಎಲಿಮಿನೇಷನ್:</strong> ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ (Manja) ನೇರ ಎಲಿಮಿನೇಟ್ & ದೊಡ್ಮನೆಯಿಂದ ನಿರ್ಗಮನ! &nbsp;&nbsp;•&nbsp;&nbsp;
          👑 <strong>8ನೇ ವಾರದ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್:</strong> ಮ್ಯೂಸಿಯಂ ಟಾಸ್ಕ್ ಗೆದ್ದ ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ ಅವರಿಗೆ ಕ್ಯಾಪ್ಟನ್ಸಿ ಕಿರೀಟ & ಇಮ್ಯೂನಿಟಿ! &nbsp;&nbsp;•&nbsp;&nbsp;
          🔴 <strong>ವಾರ 08 ಡೇಂಜರ್ ಝೋನ್:</strong> 6 ಸ್ಪರ್ಧಿಗಳು (ತಾಂಡವ್ ರಾಮ್, ಆಸಿಯಾ ಫಿರ್ದೋಸ್, ಗಗನ್ ಚಿನ್ನಪ್ಪ, ಧನುಷ್ ಮಂಜುನಾಥ್, ಓಂಪ್ರಕಾಶ್ ರಾವ್, ಸಂಗೀತ ಭಟ್) ನಾಮಿನೇಟ್! &nbsp;&nbsp;•&nbsp;&nbsp;
          🎤 <strong>ಪಂಚಾಯ್ತಿ ಎಚ್ಚರಿಕೆ:</strong> ₹2.5 ಲಕ್ಷ ಮೈಕ್ ಡ್ಯಾಮೇಜ್ ಪ್ರಕರಣಕ್ಕೆ ಕಿಚ್ಚ ಸುದೀಪ್ ಗರಂ!
        </marquee>
      </div>
      <a href="#cabin" class="btn alt" style="padding:5px 12px; font-size:0.78rem; text-decoration:none;">ಲೈವ್ ವೋಟ್ ಮಾಡಿ</a>
    </div>
'''

if 'live-radar-ticker' not in content:
    content = content.replace(
        '</section>\n\n    <!-- 1. HOUSE CONTROL PULSE -->',
        '</section>\n' + breaking_ticker + '\n    <!-- 1. HOUSE CONTROL PULSE -->'
    )

# 3. Update Captain's Cabin to Soundarya Shetty (Week 8)
old_captain_cabin = r'''    <!-- 2. CAPTAIN'S CABIN \(VIP COCKPIT SUITE\) -->
    <section class="section" id="captain-cabin">[\s\S]*?</section>'''

new_captain_cabin = '''    <!-- 2. CAPTAIN'S CABIN (VIP COCKPIT SUITE) -->
    <section class="section" id="captain-cabin">
      <div class="section-head">
        <div>
          <div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-crown"></i> CHIEF CAPTAIN OF THE HOUSE</div>
          <h2>ಕ್ಯಾಪ್ಟನ್ ಕ್ಯಾಬಿನ್</h2>
          <p class="kn">ದೊಡ್ಡಮನೆಯ ಅಧಿಕೃತ ನಾಯಕ ಮತ್ತು ಆಡಳಿತ ಸೂತ್ರ ಹಿಡಿದಿರುವ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ವಿವರ</p>
        </div>
        <div class="chip" style="color:var(--neon-gold); font-weight:800;">ವಾರ 08 ನಾಯಕತ್ವ</div>
      </div>

      <div class="captain-suite-card">
        <div class="captain-suite-grid">
          <div class="captain-avatar-frame">
            <img src="/assets/bbk13/contestants/passenger_02_face.jpg" alt="ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ" onerror="this.src='/assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
            <div class="captain-badge-overlay">
              <span style="color:var(--neon-gold); font-weight:900; font-size:0.95rem; font-family:var(--font-kannada);">👑 ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್</span>
              <div style="color:#FFF; font-size:0.8rem;">ಸೀಟ್ B01 • ಮಂಗಳೂರು</div>
            </div>
          </div>

          <div>
            <div class="eyebrow" style="color:var(--neon-green); margin-bottom:8px;">
              <i class="fa-solid fa-shield-halved"></i> ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ: 8ನೇ ವಾರದ ನಿರ್ಗಮನದಿಂದ ಮುಕ್ತ
            </div>
            <h3 style="font-size:1.9rem; color:#FFF; font-weight:900; font-family:var(--font-kannada); margin:4px 0 10px;">
              ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ (Soundarya Shetty)
            </h3>
            <p style="color:#CBD5E1; font-size:0.95rem; line-height:1.6; font-family:var(--font-kannada); margin-bottom:14px;">
              ರೋಚಕ ‘ಮ್ಯೂಸಿಯಂ ಕಳ್ಳತನ’ (Museum Heist) ಟಾಸ್ಕ್‌ನಲ್ಲಿ ತಂತ್ರಗಾರಿಕೆ, ಚುರುಕುತನ ಹಾಗೂ ದಿಟ್ಟ ನಿಲುವಿನಿಂದ ಜಯ ಸಾಧಿಸಿದ ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ ಅವರು ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13 ರ 8ನೇ ವಾರದ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ಆಗಿ ಅಧಿಕಾರ ಹಿಡಿದಿದ್ದಾರೆ. ಈ ವಾರದ ಎಲ್ಲಾ ಎಲಿಮಿನೇಷನ್ ಭೀತಿಯಿಂದ ಮುಕ್ತರಾಗಿದ್ದು, ಮನೆಯ ಆಡಳಿತ ನಡೆಸುತ್ತಿದ್ದಾರೆ.
            </p>

            <div class="captain-powers-grid">
              <div class="power-pill"><i class="fa-solid fa-bed" style="color:var(--neon-gold);"></i> <span>ಪ್ರತ್ಯೇಕ ಲಕ್ಷುರಿ ಬೆಡ್‌ರೂಂ</span></div>
              <div class="power-pill"><i class="fa-solid fa-utensils" style="color:var(--neon-cyan);"></i> <span>ಕ್ಯಾಪ್ಟನ್ ಸ್ಪೆಷಲ್ ಆಹಾರ</span></div>
              <div class="power-pill"><i class="fa-solid fa-list-check" style="color:var(--neon-green);"></i> <span>ಮನೆ ಕೆಲಸಗಳ ಹಂಚಿಕೆ ಹಕ್ಕು</span></div>
              <div class="power-pill"><i class="fa-solid fa-gavel" style="color:#EF4444;"></i> <span>ನಿಯಮ ಉಲ್ಲಂಘನೆಗೆ ಶಿಕ್ಷೆ</span></div>
            </div>

            <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center; margin-top:16px;">
              <button class="btn" style="background:linear-gradient(135deg, #B45309, #F59E0B); color:#000; font-weight:900; padding:12px 20px;" onclick="saluteCaptain()">
                <i class="fa-solid fa-hand-fist"></i> ಕ್ಯಾಪ್ಟನ್‌ಗೆ ಗೌರವ ಸಲ್ಲಿಸಿ (+50 XP)
              </button>
              <span id="captain-salute-count" style="font-size:0.85rem; color:var(--neon-gold); font-family:var(--font-kannada); font-weight:700;">
                ⭐ 18,920+ ಅಭಿಮಾನಿಗಳು ಗೌರವಿಸಿದ್ದಾರೆ
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>'''

content = re.sub(old_captain_cabin, new_captain_cabin, content, count=1)

# 4. Update renderSeatHTML to handle eliminated contestants (like Modern Mahakavi Manja)
old_render_seat = r'''    function renderSeatHTML\(c\) \{
      const isNominated = \(c\.status === 'NOMINATED' \|\| c\.nominationStatus === true\);
      const isCaptain = \(c\.status === 'CAPTAIN' \|\| c\.captaincyStatus === 'ACTIVE_CAPTAIN'\);

      let cardClass = 'seat-unit safe-card-cruising';
      let statusBadge = `<span class="safe-status-badge"><i class="fa-solid fa-shield-halved"></i> 🟢 ಸುರಕ್ಷಿತ \(SAFE CRUISING\)</span>`;
      let flightStrip = `<div class="safe-cruising-ribbon"><i class="fa-solid fa-plane-circle-check"></i> ಗಗನಯಾನ ಸುರಕ್ಷಿತ • ಈ ವಾರ ಯಾವುದೇ ಎಲಿಮಿನೇಷನ್ ಭೀತಿ ಇಲ್ಲ!</div>`;

      if \(isNominated\) \{
        cardClass = 'seat-unit departure-card-alert';
        statusBadge = `<span class="gate-departure-badge"><span class="pulse-red-dot"></span> 🔴 ನಿರ್ಗಮನ ಗೇಟ್ \(DEPARTURE LIST\)</span>`;
        flightStrip = `<div class="departure-hazard-ribbon"><i class="fa-solid fa-triangle-exclamation"></i> <strong>ನಿರ್ಗಮನ ಎಚ್ಚರಿಕೆ:</strong> ಎಲಿಮಿನೇಷನ್ ಭೀತಿ! ರಕ್ಷಿಸಲು ವೋಟ್ ಮಾಡಿ</div>`;
      \} else if \(isCaptain\) \{
        cardClass = 'seat-unit captain-card-luxury';
        statusBadge = `<span class="captain-status-badge"><i class="fa-solid fa-crown"></i> 👑 ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್</span>`;
        flightStrip = `<div class="captain-honor-ribbon"><i class="fa-solid fa-star"></i> ದೊಡ್ಡಮನೆ ನಾಯಕ • ಈ ವಾರ ಸಂಪೂರ್ಣ ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ!</div>`;
      \}'''

new_render_seat = '''    function renderSeatHTML(c) {
      const isEliminated = (c.status === 'ELIMINATED' || c.eliminated === true);
      const isNominated = (!isEliminated && (c.status === 'NOMINATED' || c.nominationStatus === true));
      const isCaptain = (!isEliminated && (c.status === 'CAPTAIN' || c.captaincyStatus === 'ACTIVE_CAPTAIN'));

      let cardClass = 'seat-unit safe-card-cruising';
      let statusBadge = `<span class="safe-status-badge"><i class="fa-solid fa-shield-halved"></i> 🟢 ಸುರಕ್ಷಿತ (SAFE CRUISING)</span>`;
      let flightStrip = `<div class="safe-cruising-ribbon"><i class="fa-solid fa-plane-circle-check"></i> ಗಗನಯಾನ ಸುರಕ್ಷಿತ • ಈ ವಾರ ಯಾವುದೇ ಎಲಿಮಿನೇಷನ್ ಭೀತಿ ಇಲ್ಲ!</div>`;

      if (isEliminated) {
        cardClass = 'seat-unit eliminated-card-ejected';
        statusBadge = `<span class="eliminated-status-badge" style="background:#7F1D1D; color:#FECACA; border:1px solid #EF4444; padding:3px 8px; border-radius:6px; font-size:0.75rem; font-weight:800;"><i class="fa-solid fa-ban"></i> 🔴 ರೆಡ್ ಕಾರ್ಡ್ ಎಲಿಮಿನೇಟೆಡ್</span>`;
        flightStrip = `<div class="eliminated-hazard-ribbon" style="background:rgba(239,68,68,0.2); border:1px solid #EF4444; color:#FCA5A5; font-size:0.75rem; padding:4px 8px; border-radius:6px; margin-bottom:8px;"><i class="fa-solid fa-circle-xmark"></i> <strong>ವಿಮಾನದಿಂದ ನಿರ್ಗಮನ:</strong> ನೇರ ರೆಡ್ ಕಾರ್ಡ್ ಮೂಲಕ ಎಜೆಕ್ಟ್ ಆಗಿದ್ದಾರೆ</div>`;
      } else if (isNominated) {
        cardClass = 'seat-unit departure-card-alert';
        statusBadge = `<span class="gate-departure-badge"><span class="pulse-red-dot"></span> 🔴 ನಿರ್ಗಮನ ಗೇಟ್ (DEPARTURE LIST)</span>`;
        flightStrip = `<div class="departure-hazard-ribbon"><i class="fa-solid fa-triangle-exclamation"></i> <strong>ನಿರ್ಗಮನ ಎಚ್ಚರಿಕೆ:</strong> ಎಲಿಮಿನೇಷನ್ ಭೀತಿ! ರಕ್ಷಿಸಲು ವೋಟ್ ಮಾಡಿ</div>`;
      } else if (isCaptain) {
        cardClass = 'seat-unit captain-card-luxury';
        statusBadge = `<span class="captain-status-badge"><i class="fa-solid fa-crown"></i> 👑 ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್</span>`;
        flightStrip = `<div class="captain-honor-ribbon"><i class="fa-solid fa-star"></i> ದೊಡ್ಡಮನೆ ನಾಯಕ • ಈ ವಾರ ಸಂಪೂರ್ಣ ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ!</div>`;
      }'''

content = re.sub(old_render_seat, new_render_seat, content, count=1)

# 5. Update filterCabinCategory to handle eliminated
old_filter = r'''      if \(currentCabinFilter === 'NOMINATED'\) \{
        filtered = data\.filter\(c => c\.status === 'NOMINATED' \|\| c\.nominationStatus === true\);
      \} else if \(currentCabinFilter === 'SAFE'\) \{
        filtered = data\.filter\(c => c\.status !== 'NOMINATED' && c\.nominationStatus !== true\);
      \}'''

new_filter = '''      if (currentCabinFilter === 'NOMINATED') {
        filtered = data.filter(c => !c.eliminated && (c.status === 'NOMINATED' || c.nominationStatus === true));
      } else if (currentCabinFilter === 'SAFE') {
        filtered = data.filter(c => !c.eliminated && c.status !== 'NOMINATED' && c.nominationStatus !== true);
      }'''

content = re.sub(old_filter, new_filter, content, count=1)

# 6. Update C16 buzz note
content = re.sub(
    r'("id":\s*"C16",[\s\S]*?"gt_q":\s*"Modern Mahakavi Manja",\s*)"note":\s*"[^"]*"',
    r'\1"note": "ನಿಯಮ ಉಲ್ಲಂಘನೆ ಮತ್ತು ಅನುಚಿತ ವರ್ತನೆಗಾಗಿ ಸುದೀಪ್ ಅವರಿಂದ ನೇರ \'ರೆಡ್ ಕಾರ್ಡ್\' ಪಡೆದು ದೊಡ್ಮನೆಯಿಂದ ನಿರ್ಗಮಿಸಿದ್ದಾರೆ."',
    content
)

# 7. Update eviction oracle risk scores
content = content.replace(
    "const riskScores = { 'C02': 44, 'C06': 36, 'C08': 62, 'C01': 10 };",
    "const riskScores = { 'C05': 42, 'C06': 36, 'C08': 64, 'C10': 38, 'C12': 55, 'C14': 60, 'C01': 10, 'C02': 5 };"
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("bigg-boss-kannada-13.html patched successfully!")
