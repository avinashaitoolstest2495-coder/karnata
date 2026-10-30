import sys
import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Title & Meta Description
    old_title = '<title>ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ | Karnataka Live News, Weather, Gold, Dam & Governance Portal — Karnata.in</title>'
    new_title = '<title>ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ &amp; ನಾಗರಿಕ ಸೇವೆಗಳ ಪೋರ್ಟಲ್ — Karnata.in</title>'
    if old_title in html:
        html = html.replace(old_title, new_title)
    else:
        html = re.sub(r'<title>.*?</title>', new_title, html, count=1)

    old_desc = 'ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ: ಇಂದಿನ ಹವಾಮಾನ, 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು, ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ, ಸಚಿವರು ಮತ್ತು ಸರ್ಕಾರಿ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು.'
    new_desc = 'ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ: ಇಂದಿನ ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರ, ಪೆಟ್ರೋಲ್ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಹವಾಮಾನ, APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ, ಮತದಾರರ ಪಟ್ಟಿ ಹಾಗೂ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ವಿವರ.'
    html = html.replace(old_desc, new_desc)

    # 2. Update .live-row CSS to responsive 5-grid
    old_live_css = """.live-row {
  display: flex;
  flex-direction: row;
  gap: 8px;
  margin-bottom: 16px;
  width: 100%;
}
@media(max-width:640px) {
  .live-row { flex-wrap: wrap; }
  .live-row .live-card { flex: 1 1 calc(33% - 8px); }
}"""

    new_live_css = """.live-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  margin-bottom: 20px;
  width: 100%;
}
@media(max-width:960px) {
  .live-row { grid-template-columns: repeat(3, 1fr); }
}
@media(max-width:600px) {
  .live-row { grid-template-columns: repeat(2, 1fr); gap: 8px; }
  .live-row .live-card:last-child { grid-column: span 2; }
}"""
    if old_live_css in html:
        html = html.replace(old_live_css, new_live_css)

    # 3. Update .tools-grid CSS
    old_tools_css = """.tools-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 36px;
}
@media(max-width:600px) { .tools-grid { grid-template-columns: repeat(2, 1fr); } }"""

    new_tools_css = """.tools-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  margin-bottom: 32px;
}
@media(max-width:960px) { .tools-grid { grid-template-columns: repeat(3, 1fr); } }
@media(max-width:600px) { .tools-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; } }"""
    if old_tools_css in html:
        html = html.replace(old_tools_css, new_tools_css)

    # 4. Polish .tool-tile CSS
    old_tile_css = """.tool-tile {
  background: var(--card-bg);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 18px 14px;
  text-align: center;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: var(--shadow-flat);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
.tool-tile:hover {
  border-color: var(--k-red);
  box-shadow: var(--shadow-hover);
  transform: translateY(-3px);
}
.tt-icon-wrap {
  width: 48px; height: 48px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  transition: transform 0.2s ease;
}
.tool-tile:hover .tt-icon-wrap { transform: scale(1.12); }"""

    new_tile_css = """.tool-tile {
  background: var(--card-bg);
  border: 1.5px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 16px 12px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: var(--shadow-flat);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  text-decoration: none;
}
.tool-tile:hover {
  border-color: var(--k-red);
  box-shadow: var(--shadow-hover);
  transform: translateY(-3px);
}
.tt-icon-wrap {
  width: 44px; height: 44px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  transition: transform 0.2s ease;
}
.tool-tile:hover .tt-icon-wrap { transform: scale(1.1); }"""
    if old_tile_css in html:
        html = html.replace(old_tile_css, new_tile_css)

    # 5. Clean Ticker label
    html = html.replace('<div class="ticker-label"><div class="pulse-ring"></div>🔴 ಲೈವ್‌</div>',
                        '<div class="ticker-label"><div class="pulse-ring"></div>🔴 ಲೈವ್ ಮಾಹಿತಿ</div>')

    # 6. Masthead Tagline Clean-up
    old_tagline = '<div class="mh-tagline">Universe Of Karnataka<br>ನಿಮ್ಮ ಜಿಲ್ಲೆ · ನಿಮ್ಮ ಭಾಷೆ · ನಿಮ್ಮ ಮಾಹಿತಿ</div>'
    new_tagline = '<div class="mh-tagline">ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಲೈವ್ ಮಾಹಿತಿ ಪೋರ್ಟಲ್<br><span style="font-size:11.5px;color:var(--text-muted);font-weight:600;">ನಾಗರಿಕ ಸೇವೆಗಳು · ಜಿಲ್ಲಾವಾರು ಮಾಹಿತಿ · ನೈಜ ಸಮಯದ ದರಗಳು</span></div>'
    html = html.replace(old_tagline, new_tagline)

    # 7. Navigation Tabs Redesign (6 Focused Dropdowns)
    old_nav_tabs_regex = r'<nav class="nav-tabs">.*?</nav>'
    new_nav_tabs = """<nav class="nav-tabs">
  <div class="nav-tabs-inner">
    
    <!-- 1. ADMINISTRATION & CITIZEN SERVICES -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>🏛️ ಆಡಳಿತ &amp; ನಾಗರಿಕ ಸೇವೆಗಳು</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="karnataka.html" class="nav-tab-dropitem">👑 ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ</a>
        <a href="gba.html" class="nav-tab-dropitem">🏙️ GBA ಬೆಂಗಳೂರು (5 ಪಾಲಿಕೆಗಳು &amp; 369 ವಾರ್ಡ್)</a>
        <a href="gram-panchayat.html" class="nav-tab-dropitem">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್ (5,958 GPs)</a>
        <a href="nanna-sthala.html" class="nav-tab-dropitem">📍 ನನ್ನ ಸ್ಥಳ (My Location)</a>
        <a href="cabinet-ministers.html" class="nav-tab-dropitem">👥 ಸಚಿವ ಸಂಪುಟ (33 ಸಚಿವರು)</a>
        <a href="former-cms.html" class="nav-tab-dropitem">📜 ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು</a>
        <a href="local-government.html" class="nav-tab-dropitem">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು (810 ULB)</a>
        <a href="officers.html" class="nav-tab-dropitem">👥 ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ</a>
      </div>
    </div>

    <!-- 2. ELECTIONS & REPRESENTATIVES -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>🗳️ ಚುನಾವಣೆ &amp; ಶಾಸಕರು</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="karnataka-sir-voters-final-list.html" class="nav-tab-dropitem" style="color:var(--k-red); font-weight:800;">🗳️ SIR 2026 ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ (Final List)</a>
        <a href="mla-mp.html" class="nav-tab-dropitem">🏛️ ಶಾಸಕರು, MLC &amp; ಸಂಸದರು (MLA / MP)</a>
        <a href="karnataka-sir-voter-roll.html" class="nav-tab-dropitem">🗳️ SIR 2026 ಮತದಾರರ ಕರಡು ಪಟ್ಟಿ (Draft Roll)</a>
        <a href="karnataka-elections.html" class="nav-tab-dropitem">🗳️ ಕರ್ನಾಟಕ ಚುನಾವಣೆ ಫಲಿತಾಂಶಗಳು</a>
      </div>
    </div>

    <!-- 3. KANNADA ART & LITERATURE -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>🎨 ಕನ್ನಡ ಕಲೆ &amp; ಸಾಹಿತ್ಯ</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="kannada-posters.html" class="nav-tab-dropitem" style="color:var(--k-red); font-weight:800;">🎨 ಕನ್ನಡ ಪೋಸ್ಟರ್ ಮೇಕರ್ (Posters &amp; Quotes)</a>
        <a href="sahitya-kannada-keyboard.html" class="nav-tab-dropitem">⌨️ ಸಾಹಿತ್ಯ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ (Android App)</a>
        <a href="kannada-typing.html" class="nav-tab-dropitem">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ &amp; ಲಿಪ್ಯಂತರ</a>
      </div>
    </div>

    <!-- 4. AGRI, WATER & WEATHER -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>💧 ಕೃಷಿ, ನೀರು &amp; ಹವಾಮಾನ</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="dam-levels.html" class="nav-tab-dropitem">💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Live Dam Levels)</a>
        <a href="weather.html" class="nav-tab-dropitem">🌧️ ಹವಾಮಾನ &amp; ಮಳೆ ವರದಿ</a>
        <a href="apmc-prices.html" class="nav-tab-dropitem">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು</a>
      </div>
    </div>

    <!-- 5. FINANCE & MARKET RATES -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>💰 ಮಾರುಕಟ್ಟೆ &amp; ಹಣಕಾಸು</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="gold-rate.html" class="nav-tab-dropitem">🪙 ಚಿನ್ನ &amp; ಬೆಳ್ಳಿ ದರ</a>
        <a href="petrol-price.html" class="nav-tab-dropitem">⛽ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್ ದರ</a>
        <a href="emi-calculator.html" class="nav-tab-dropitem">🏦 EMI ಲೆಕ್ಕಾಚಾರ</a>
        <a href="sip-calculator.html" class="nav-tab-dropitem">📈 SIP ಲೆಕ್ಕಾಚಾರ</a>
        <a href="salary-calculator.html" class="nav-tab-dropitem">💰 ಸಂಬಳದ ಲೆಕ್ಕ</a>
      </div>
    </div>

    <!-- 6. AI & SMART SERVICES -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="toggleNavDropdown(this, event)">
        <span>🤖 AI &amp; ಡಿಜಿಟಲ್ ಸೇವೆಗಳು</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="scheme-checker.html" class="nav-tab-dropitem" style="color:#059669; font-weight:800;">📋 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತೆ ಪರಿಶೀಲಕ</a>
        <a href="quiz.html" class="nav-tab-dropitem">🧠 ದೈನಂದಿನ ರಸಪ್ರಶ್ನೆ (Daily Quiz)</a>
        <a href="ask.html" class="nav-tab-dropitem">🤖 askKARNATA AI ಸಹಾಯಕ</a>
        <a href="ai-jyothishya.html" class="nav-tab-dropitem">🔮 AI ಜ್ಯೋತಿಷ್ಯ &amp; ಕುಂಡಲಿ</a>
      </div>
    </div>
  </div>
</nav>"""
    html = re.sub(old_nav_tabs_regex, new_nav_tabs, html, count=1, flags=re.DOTALL)

    # 8. Clean Search Box Placeholder
    html = html.replace('placeholder="ಕರ್ನಾಟಕದ ಮಾಹಿತಿ ಹುಡುಕಿ ಅಥವಾ ಪ್ರಶ್ನೆ ಕೇಳಿ..."',
                        'placeholder="ಕರ್ನಾಟಕದ ಯಾವುದೇ ಮಾಹಿತಿ ಹುಡುಕಿ... (ಉದಾ: ಮತದಾರರ ಪಟ್ಟಿ, ಚಿನ್ನದ ದರ, ಗೃಹಲಕ್ಷ್ಮಿ, KRS ಡ್ಯಾಂ)"')

    # 9. SIR Hero Banner Redesign (Pure Kannada, Authoritative, Zero Waste Words)
    old_sir_banner_regex = r'<!-- FEATURED: KARNATAKA SIR 2026 VOTERS LIST HERO BANNER -->.*?<!-- SMART SEARCH RESULTS CONTAINER -->'
    new_sir_banner = """<!-- FEATURED: KARNATAKA SIR 2026 VOTERS LIST HERO BANNER -->
    <div class="sir-hero-banner" style="background:linear-gradient(135deg, #064E3B 0%, #0F172A 100%); border:1.5px solid #10B981; border-radius:18px; padding:20px 24px; margin-bottom:24px; box-shadow:0 8px 24px rgba(6,78,59,0.25); color:#FFFFFF; position:relative; overflow:hidden;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
        <div style="flex:1; min-width:260px;">
          <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(16,185,129,0.22); border:1px solid rgba(52,211,153,0.4); color:#A7F3D0; font-size:11.5px; font-weight:800; padding:4px 12px; border-radius:20px; margin-bottom:8px;">
            🗳️ ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗ (ECI) ಅಧಿಕೃತ ಪ್ರಕಟಣೆ
          </div>
          <h2 style="font-size:22px; font-weight:900; margin:0 0 6px 0; color:#FFFFFF; font-family:'Anek Kannada',sans-serif; letter-spacing:-0.01em;">
            ಕರ್ನಾಟಕ ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ 2026
          </h2>
          <p style="font-size:13.5px; color:#CBD5E1; margin:0; line-height:1.45;">
            ರಾಜ್ಯದ 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ 62,517 ಮತಗಟ್ಟೆಗಳ ಅಧಿಕೃತ ಅಂತಿಮ ಪಟ್ಟಿ (PDF) ಹಾಗೂ EPIC ವೋಟರ್ ID ಹುಡುಕಾಟ.
          </p>
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
          <a href="/karnataka-sir-voters-final-list" style="background:linear-gradient(135deg, #10B981 0%, #059669 100%); color:#FFFFFF; font-size:14.5px; font-weight:900; padding:12px 22px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:6px; box-shadow:0 4px 14px rgba(16,185,129,0.35); flex-shrink:0; transition:transform 0.15s;">
            📄 ಅಂತಿಮ ಪಟ್ಟಿ ಪರಿಶೀಲಿಸಿ →
          </a>
          <a href="/karnataka-sir-voter-roll" style="background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); color:#E2E8F0; font-size:13.5px; font-weight:700; padding:11px 18px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:4px; flex-shrink:0;">
            🔍 ಕರಡು ಪಟ್ಟಿ
          </a>
        </div>
      </div>
    </div>

    <!-- SMART SEARCH RESULTS CONTAINER -->"""
    html = re.sub(old_sir_banner_regex, new_sir_banner, html, count=1, flags=re.DOTALL)

    # 10. Live Bento Row (Fix "ಬೆಂಗಳೂರು ಲೀಟರ್" to "ಪ್ರತಿ ಲೀಟರ್‌ಗೆ", KRS label, Gold format)
    html = html.replace('<div class="lc-change nc" id="lc-petrol-ch">ಬೆಂಗಳೂರು ಲೀಟರ್</div>',
                        '<div class="lc-change nc" id="lc-petrol-ch">ಪ್ರತಿ ಲೀಟರ್‌ಗೆ</div>')
    html = html.replace('<div class="lc-label">KRS ಅಣೆಕಟ್ಟು</div>',
                        '<div class="lc-label">KRS ಜಲಾಶಯ</div>')

    # 11. Tools Grid: 10 Essential Services (including Posters & Keyboard)
    old_tools_grid_regex = r'<!-- TOOLS GRID -->.*?<!-- DAMS -->'
    new_tools_grid = """<!-- TOOLS GRID -->
    <div class="sh">
      <div class="sh-title"><div class="sh-icon">🛠️</div>ಉಪಯುಕ್ತ ನಾಗರಿಕ ಸೇವೆಗಳು</div>
      <a href="local-government.html" class="sh-link">ಎಲ್ಲಾ ಸೇವೆಗಳು →</a>
    </div>

    <div class="tools-grid">
      <a href="kannada-posters.html" class="tool-tile" style="border:1.5px solid #FECDD3; background:linear-gradient(135deg, #FFF1F2 0%, #FFF 100%);">
        <div class="tt-icon-wrap" style="background:#E11D48; color:#fff;">🎨</div>
        <span class="tt-label" style="font-weight:900; color:#BE123C;">ಕನ್ನಡ ಪೋಸ್ಟರ್ ಮೇಕರ್</span>
        <span style="font-size:11px; color:#9F1239; font-weight:700;">ನುಡಿಮುತ್ತು &amp; ಶುಭಾಶಯ</span>
      </a>

      <a href="sahitya-kannada-keyboard.html" class="tool-tile" style="border:1.5px solid #FED7AA; background:linear-gradient(135deg, #FFF7ED 0%, #FFF 100%);">
        <div class="tt-icon-wrap" style="background:#F97316; color:#fff;">⌨️</div>
        <span class="tt-label" style="font-weight:900; color:#C2410C;">ಸಾಹಿತ್ಯ ಕೀಬೋರ್ಡ್</span>
        <span style="font-size:11px; color:#9A3412; font-weight:700;">ಆಂಡ್ರಾಯ್ಡ್ ಆ್ಯಪ್</span>
      </a>

      <a href="karnataka-sir-voters-final-list.html" class="tool-tile" style="border:1.5px solid #A7F3D0; background:linear-gradient(135deg, #ECFDF5 0%, #FFF 100%);">
        <div class="tt-icon-wrap" style="background:#059669; color:#fff;">🗳️</div>
        <span class="tt-label" style="font-weight:900; color:#065F46;">ಮತದಾರರ ಪಟ್ಟಿ 2026</span>
        <span style="font-size:11px; color:#047857; font-weight:700;">ಅಂತಿಮ ಪಟ್ಟಿ PDF</span>
      </a>

      <a href="scheme-checker.html" class="tool-tile" style="border:1.5px solid #BAE6FD; background:linear-gradient(135deg, #F0F9FF 0%, #FFF 100%);">
        <div class="tt-icon-wrap" style="background:#0284C7; color:#fff;">📋</div>
        <span class="tt-label" style="font-weight:900; color:#0369A1;">ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು</span>
        <span style="font-size:11px; color:#0284C7; font-weight:700;">ಅರ್ಹತೆ ಪರಿಶೀಲಕ</span>
      </a>

      <a href="quiz.html" class="tool-tile" style="border:1.5px solid #DDD6FE; background:linear-gradient(135deg, #F5F3FF 0%, #FFF 100%);">
        <div class="tt-icon-wrap" style="background:#7C3AED; color:#fff;">🧠</div>
        <span class="tt-label" style="font-weight:900; color:#5B21B6;">ದೈನಂದಿನ ರಸಪ್ರಶ್ನೆ</span>
        <span style="font-size:11px; color:#6D28D9; font-weight:700;">ಸಾಮಾನ್ಯ ಜ್ಞಾನ</span>
      </a>

      <a href="mla-mp.html" class="tool-tile">
        <div class="tt-icon-wrap bg-t-4">🏛️</div>
        <span class="tt-label">ಶಾಸಕರು &amp; ಸಂಸದರು</span>
        <span style="font-size:11px; color:var(--text-muted); font-weight:600;">MLA &amp; MP ವಿವರ</span>
      </a>

      <a href="dam-levels.html" class="tool-tile">
        <div class="tt-icon-wrap bg-t-8">💧</div>
        <span class="tt-label">ಜಲಾಶಯ ಮಟ್ಟ</span>
        <span style="font-size:11px; color:var(--text-muted); font-weight:600;">ಲೈವ್ ಡ್ಯಾಂ ವರದಿ</span>
      </a>

      <a href="apmc-prices.html" class="tool-tile">
        <div class="tt-icon-wrap bg-t-2">🌾</div>
        <span class="tt-label">APMC ಮಾರುಕಟ್ಟೆ</span>
        <span style="font-size:11px; color:var(--text-muted); font-weight:600;">ದೈನಂದಿನ ಧಾರಣೆ</span>
      </a>

      <a href="emi-calculator.html" class="tool-tile">
        <div class="tt-icon-wrap bg-t-1">🏦</div>
        <span class="tt-label">ಹಣಕಾಸು ಲೆಕ್ಕ</span>
        <span style="font-size:11px; color:var(--text-muted); font-weight:600;">EMI, SIP &amp; ಸಂಬಳ</span>
      </a>

      <a href="/districts" class="tool-tile">
        <div class="tt-icon-wrap bg-t-7">🗺️</div>
        <span class="tt-label">31 ಜಿಲ್ಲೆಗಳು</span>
        <span style="font-size:11px; color:var(--text-muted); font-weight:600;">ಸಮಗ್ರ ಜಿಲ್ಲಾ ದರ್ಶನ</span>
      </a>
    </div>

    <!-- DAMS -->"""
    html = re.sub(old_tools_grid_regex, new_tools_grid, html, count=1, flags=re.DOTALL)

    # 12. Dam Section Titles
    html = html.replace('<div class="sh-title"><div class="sh-icon">💧</div>ಅಣೆಕಟ್ಟುಗಳಲ್ಲಿ ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ</div>',
                        '<div class="sh-title"><div class="sh-icon">💧</div>ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ</div>')
    html = html.replace('<a href="dam-levels.html" class="sh-link">ಎಲ್ಲ ಅಣೆಕಟ್ಟುಗಳು →</a>',
                        '<a href="dam-levels.html" class="sh-link">ಎಲ್ಲಾ ಅಣೆಕಟ್ಟುಗಳು →</a>')

    # 13. Daily Quiz Header Polish
    html = html.replace('<h3 class="hqc-title">ಇಂದಿನ ವಿಶೇಷ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರಿಸಿ! ನಿಮ್ಮ ಕರ್ನಾಟಕ ಸಾಮಾನ್ಯ ಜ್ಞಾನ ಪರೀಕ್ಷಿಸಿಕೊಳ್ಳಿ</h3>',
                        '<h3 class="hqc-title">ದಿನದ ಕರ್ನಾಟಕ ರಸಪ್ರಶ್ನೆ — ನಿಮ್ಮ ಜ್ಞಾನ ಪರೀಕ್ಷಿಸಿಕೊಳ್ಳಿ</h3>')
    html = html.replace('<a href="quiz.html" class="sh-link" style="color:#E11D48; font-weight:800;">ಪೂರ್ಣ 20 ಪ್ರಶ್ನೆಗಳನ್ನು ಆಡಿ →</a>',
                        '<a href="quiz.html" class="sh-link" style="color:#E11D48; font-weight:800;">ಪೂರ್ಣ 20 ಪ್ರಶ್ನೆಗಳು →</a>')

    # 14. Government Schemes Banner Clean-up (Remove "58 + 48 = 106")
    old_schemes_banner_regex = r'<!-- ══ GOVERNMENT GUIDES & CITIZEN SCHEMES ══════════════════════ -->.*?<div style="display:grid; grid-template-columns:repeat\(auto-fit, minmax\(280px, 1fr\)\);'
    new_schemes_banner = """<!-- ══ GOVERNMENT GUIDES & CITIZEN SCHEMES ══════════════════════ -->
    <div class="sh" style="margin-top:28px;">
      <div class="sh-title"><div class="sh-icon">📚</div>ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು &amp; ಅರ್ಹತೆ ಪರಿಶೀಲಕ</div>
      <a href="scheme-checker.html" class="sh-link" style="color:#047857; font-weight:900;">ಎಲ್ಲಾ ಯೋಜನೆಗಳು →</a>
    </div>

    <div style="background:linear-gradient(135deg, #090D16 0%, #1E1B4B 50%, #7F1D1D 100%); border:1.5px solid #F59E0B; border-radius:18px; padding:20px 24px; margin-bottom:18px; color:#FFF; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px; box-shadow:0 8px 24px rgba(15,23,42,0.2);">
      <div style="flex:1; min-width:260px;">
        <div style="display:inline-flex; gap:6px; align-items:center; background:rgba(245,158,11,0.2); border:1px solid rgba(251,191,36,0.45); color:#FDE68A; font-size:11.5px; font-weight:800; padding:4px 12px; border-radius:999px; margin-bottom:8px;">
          📋 ಕೇಂದ್ರ ಮತ್ತು ರಾಜ್ಯ ಸರ್ಕಾರದ ಸವಲತ್ತುಗಳು
        </div>
        <h3 style="font-size:20px; font-weight:900; color:#FFF; margin:0 0 6px 0;">ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಸ್ಮಾರ್ಟ್ ಅರ್ಹತೆ ಪರಿಶೀಲಕ</h3>
        <p style="font-size:13.5px; color:#CBD5E1; margin:0; line-height:1.45;">
          ಗೃಹಲಕ್ಷ್ಮಿ, ಅನ್ನಭಾಗ್ಯ, ಯುವನಿಧಿ, ಪಿಎಂ ಕಿಸಾನ್, ವಿದ್ಯಾರ್ಥಿವೇತನ ಸೇರಿದಂತೆ ನಿಮ್ಮ ಕುಟುಂಬಕ್ಕೆ ಲಭ್ಯವಿರುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಕ್ಷಣಾರ್ಧದಲ್ಲಿ ತಿಳಿಯಿರಿ.
        </p>
      </div>
      <a href="scheme-checker.html" style="background:linear-gradient(135deg, #F59E0B 0%, #D97706 100%); color:#0F172A; font-size:14.5px; font-weight:900; padding:12px 22px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:6px; box-shadow:0 4px 14px rgba(245,158,11,0.35); flex-shrink:0;">
        🔍 ನನ್ನ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ →
      </a>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));"""
    html = re.sub(old_schemes_banner_regex, new_schemes_banner, html, count=1, flags=re.DOTALL)

    # 15. APMC sidebar button
    html = html.replace('ಎಲ್ಲ 174 APMC ಬೆಲೆ ನೋಡಿ →', 'ಎಲ್ಲಾ 174 APMC ಧಾರಣೆಗಳು →')

    # 16. MLA widget button
    html = html.replace('🏛️ ನಿಮ್ಮ ಕ್ಷೇತ್ರದ MLA ಯಾರು?', '🏛️ ನಿಮ್ಮ ಕ್ಷೇತ್ರದ ಶಾಸಕರು (MLA) ಯಾರು?')

    # 17. Footer Clean-up (Remove "Universe Of Karnataka")
    old_footer_regex = r'<!-- ══ FOOTER ════════════════════════════════════════════ -->.*?<!-- ══ MOBILE NAV ══════════════════════════════════════ -->'
    new_footer = """<!-- ══ FOOTER ════════════════════════════════════════════ -->
<footer class="footer">
  <div class="footer-inner">
    <div>
      <div class="footer-brand">ಕರ್ನಾಟ — Karnata.in</div>
      <div class="footer-desc">ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗಾಗಿ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ವೇದಿಕೆ. ಚಿನ್ನ-ಬೆಳ್ಳಿ ಬೆಲೆ, ಇಂಧನ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಶಾಸಕರು, APMC ಧಾರಣೆ ಮತ್ತು ಹವಾಮಾನದ ನೈಜ ಸಮಯದ ಮಾಹಿತಿ.</div>
    </div>
    <div>
      <div class="footer-col-title">ಲೈವ್ ಮಾಹಿತಿ</div>
      <div class="footer-links">
        <a href="gold-rate.html"    class="footer-link">🥇 ಚಿನ್ನ &amp; ಬೆಳ್ಳಿ ದರ</a>
        <a href="petrol-price.html" class="footer-link">⛽ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್</a>
        <a href="dam-levels.html"   class="footer-link">💧 ಜಲಾಶಯಗಳ ಮಟ್ಟ</a>
        <a href="apmc-prices.html"   class="footer-link">🌾 APMC ಮಾರುಕಟ್ಟೆ</a>
        <a href="weather.html"      class="footer-link">🌧️ ಹವಾಮಾನ &amp; ಮಳೆ</a>
      </div>
    </div>
    <div>
      <div class="footer-col-title">ನಾಗರಿಕ ಸೇವೆಗಳು</div>
      <div class="footer-links">
        <a href="kannada-posters.html" class="footer-link">🎨 ಕನ್ನಡ ಪೋಸ್ಟರ್ ಮೇಕರ್</a>
        <a href="sahitya-kannada-keyboard.html" class="footer-link">⌨️ ಸಾಹಿತ್ಯ ಕೀಬೋರ್ಡ್</a>
        <a href="karnataka-sir-voters-final-list.html" class="footer-link">🗳️ ಮತದಾರರ ಪಟ್ಟಿ 2026</a>
        <a href="scheme-checker.html"    class="footer-link">📋 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು</a>
        <a href="quiz.html"              class="footer-link">🧠 ದೈನಂದಿನ ರಸಪ್ರಶ್ನೆ</a>
        <a href="mla-mp.html"            class="footer-link">🏛️ ಶಾಸಕರು &amp; ಸಂಸದರು</a>
        <a href="local-government.html" class="footer-link">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು (810 ULB)</a>
        <a href="/districts"             class="footer-link">🗺️ 31 ಜಿಲ್ಲೆಗಳು</a>
      </div>
    </div>
    <div>
      <div class="footer-col-title">Policies &amp; Info</div>
      <div class="footer-links">
        <a href="/about"          class="footer-link">About Us</a>
        <a href="/contact"        class="footer-link">Contact Us</a>
        <a href="/privacy-policy" class="footer-link">Privacy Policy</a>
        <a href="/terms"          class="footer-link">Terms &amp; Conditions</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 Karnata.in · ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಕೇಂದ್ರ</span>
    <span>ಮಾಹಿತಿ ಮೂಲ: IBJA · ಕರ್ನಾಟಕ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ · Open-Meteo · agmarknet.gov.in · ECI</span>
  </div>
</footer>

<!-- ══ MOBILE NAV ══════════════════════════════════════ -->"""
    html = re.sub(old_footer_regex, new_footer, html, count=1, flags=re.DOTALL)

    # 18. Notification & Geo dialog texts
    html = html.replace('<button class="nb-yes" onclick="requestPush()">✅ ಚಾಲು ಮಾಡಿ</button>',
                        '<button class="nb-yes" onclick="requestPush()">✅ ಅನುಮತಿಸಿ</button>')
    html = html.replace('<button class="nb-no" onclick="closeNotif()">ನಂತರ</button>',
                        '<button class="nb-no" onclick="closeNotif()">ನಂತರ ನೆನಪಿಸಿ</button>')
    html = html.replace('<span class="gs-skip" onclick="closeGeoSheet()">ನಂತರ ಆಯ್ಕೆ ಮಾಡುತ್ತೇನೆ</span>',
                        '<span class="gs-skip" onclick="closeGeoSheet()">ನಂತರ ನೋಡುತ್ತೇನೆ</span>')

    # 19. Mobile Nav Drawer Groups Update
    old_drawer_regex = r'<div class="mnd-overlay" id="mobile-nav-drawer".*?<!-- ══ GEO BOTTOM SHEET'
    new_drawer = """<div class="mnd-overlay" id="mobile-nav-drawer" onclick="if(event.target===this) toggleMobileNavDrawer()">
  <div class="mnd-sheet">
    <div class="mnd-header">
      <div class="mnd-title">🌐 ಕರ್ನಾಟಕ ಸಮಗ್ರ ಸೇವೆಗಳು</div>
      <button class="mnd-close-btn" onclick="toggleMobileNavDrawer()">✕</button>
    </div>
    <div class="mnd-body">
      
      <div class="mnd-group">
        <div class="mnd-g-title">🏛️ ಆಡಳಿತ &amp; ನಾಗರಿಕ ಸೇವೆಗಳು</div>
        <div class="mnd-g-links">
          <a href="karnataka.html">👑 ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ</a>
          <a href="gba.html">🏙️ GBA ಬೆಂಗಳೂರು (5 ಪಾಲಿಕೆಗಳು &amp; 369 ವಾರ್ಡ್)</a>
          <a href="gram-panchayat.html">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್ (5,958 GPs)</a>
          <a href="nanna-sthala.html">📍 ನನ್ನ ಸ್ಥಳ (My Location)</a>
          <a href="cabinet-ministers.html">👥 ಸಚಿವ ಸಂಪುಟ (33 ಸಚಿವರು)</a>
          <a href="former-cms.html">📜 ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು</a>
          <a href="local-government.html">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು (810 ULB)</a>
          <a href="officers.html">👥 ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">🗳️ ಚುನಾವಣೆ &amp; ಶಾಸಕರು</div>
        <div class="mnd-g-links">
          <a href="karnataka-sir-voters-final-list.html" style="color:var(--k-red); font-weight:800;">🗳️ SIR 2026 ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ</a>
          <a href="mla-mp.html">🏛️ ಶಾಸಕರು, MLC &amp; ಸಂಸದರು (MLA/MP)</a>
          <a href="karnataka-sir-voter-roll.html">🗳️ SIR 2026 ಮತದಾರರ ಕರಡು ಪಟ್ಟಿ</a>
          <a href="karnataka-elections.html">🗳️ ಕರ್ನಾಟಕ ಚುನಾವಣೆ ಫಲಿತಾಂಶ</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">🎨 ಕನ್ನಡ ಕಲೆ &amp; ಸಾಹಿತ್ಯ</div>
        <div class="mnd-g-links">
          <a href="kannada-posters.html" style="color:var(--k-red); font-weight:800;">🎨 ಕನ್ನಡ ಪೋಸ್ಟರ್ ಮೇಕರ್ (Posters &amp; Quotes)</a>
          <a href="sahitya-kannada-keyboard.html">⌨️ ಸಾಹಿತ್ಯ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ (Android App)</a>
          <a href="kannada-typing.html">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ &amp; ಲಿಪ್ಯಂತರ</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">💧 ಕೃಷಿ, ನೀರು &amp; ಹವಾಮಾನ</div>
        <div class="mnd-g-links">
          <a href="dam-levels.html">💧 ಜಲಾಶಯಗಳ ಮಟ್ಟ (Live Dam Levels)</a>
          <a href="weather.html">🌧️ ಹವಾಮಾನ &amp; ಮಳೆ ವರದಿ</a>
          <a href="apmc-prices.html">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">💰 ಮಾರುಕಟ್ಟೆ &amp; ಹಣಕಾಸು</div>
        <div class="mnd-g-links">
          <a href="gold-rate.html">🪙 ಚಿನ್ನ &amp; ಬೆಳ್ಳಿ ದರ</a>
          <a href="petrol-price.html">⛽ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್ ದರ</a>
          <a href="emi-calculator.html">🏦 EMI ಲೆಕ್ಕಾಚಾರ</a>
          <a href="sip-calculator.html">📈 SIP ಲೆಕ್ಕಾಚಾರ</a>
          <a href="salary-calculator.html">💰 ಸಂಬಳದ ಲೆಕ್ಕ</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">🤖 AI &amp; ಡಿಜಿಟಲ್ ಸೇವೆಗಳು</div>
        <div class="mnd-g-links">
          <a href="scheme-checker.html" style="color:#059669; font-weight:800;">📋 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತೆ ಪರಿಶೀಲಕ</a>
          <a href="quiz.html" style="color:#E11D48; font-weight:800;">🧠 ದೈನಂದಿನ ರಸಪ್ರಶ್ನೆ (Daily Quiz)</a>
          <a href="ask.html">🤖 askKARNATA AI ಸಹಾಯಕ</a>
          <a href="ai-jyothishya.html">🔮 AI ಜ್ಯೋತಿಷ್ಯ &amp; ಕುಂಡಲಿ</a>
        </div>
      </div>

      <div class="mnd-group">
        <div class="mnd-g-title">📚 ಸರ್ಕಾರಿ ಮಾರ್ಗದರ್ಶಿಗಳು</div>
        <div class="mnd-g-links">
          <a href="/article/gruha-lakshmi-status-check-2026">🌸 ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಸ್ಟೇಟಸ್ ಚೆಕ್</a>
          <a href="/article/karnataka-bhoomi-rtc-pahani-online">📜 ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್</a>
          <a href="/article/karnataka-dam-water-storage-analysis">💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ</a>
          <a href="/article/karnataka-gba-5-corporations-guide">🏙️ GBA 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು</a>
          <a href="/article/panchatantra-village-budget-grants">🌾 ಪಂಚತಂತ್ರ ಗ್ರಾಮ ಅನುದಾನ</a>
        </div>
      </div>

    </div>
  </div>
</div>

<!-- ══ GEO BOTTOM SHEET"""
    html = re.sub(old_drawer_regex, new_drawer, html, count=1, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully redesigned index.html with pure Kannada, sleek UI, and removed waste words!")

if __name__ == '__main__':
    main()
