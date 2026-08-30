nav_component_code = """/**
 * nav-component.js — Karnata v4 Masterclass Header
 * Exactly 6 Hover Dropdown Navigation Buttons across all pages.
 * Opens seamlessly on cursor hover and click/touch.
 */
(function () {
  if (typeof window !== 'undefined' && !document.querySelector('script[src*="googlesyndication.com"]')) {
    const adScript = document.createElement('script');
    adScript.async = true;
    adScript.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478";
    adScript.crossOrigin = "anonymous";
    document.head.appendChild(adScript);
  }

  const path = window.location.pathname;
  function isActive(href) {
    if (href === '/index.html' || href === '/') return path === '/' || path.endsWith('/index.html');
    return path.includes(href.replace('/', ''));
  }

  function savedLoc() {
    try { const s = JSON.parse(localStorage.getItem('nk_s3') || '{}'); return s.taluk || s.districtKn || null; }
    catch(e) { return null; }
  }

  const locLabel = savedLoc() || 'ಸ್ಥಳ ಆಯ್ಕೆ';

  const navHTML = `
<style>
@import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;600;700;800;900&display=swap');

/* Hide legacy duplicate topnav if present */
.topnav { display: none !important; }

.nk-nav {
  position: sticky; top: 0; z-index: 9999;
  font-family: 'Anek Kannada', sans-serif;
  box-shadow: 0 4px 20px rgba(28,18,9,0.08);
}
.nk-nav-ticker {
  background: #1C1209;
  height: 32px;
  display: flex;
  align-items: center;
  overflow: hidden;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.nk-ticker-label {
  background: linear-gradient(135deg, #C0392B, #A93226);
  color: #fff;
  font-size: 10px;
  font-weight: 900;
  padding: 0 14px;
  height: 100%;
  display: flex;
  align-items: center;
  letter-spacing: 0.1em;
  flex-shrink: 0;
  text-transform: uppercase;
}
.nk-ticker-text {
  font-size: 12px;
  color: rgba(255,255,255,0.85);
  padding: 0 14px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 1;
  min-width: 0;
}
.nk-ticker-text span { color: #FFD700; font-weight: 700; margin: 0 4px; }

.nk-masthead {
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 3px solid #C0392B;
  padding: 0 16px;
  position: relative;
  overflow: visible !important;
  width: 100%;
  box-sizing: border-box;
}
.nk-mh-inner {
  max-width: 1280px;
  width: 100%;
  box-sizing: border-box;
  margin: 0 auto;
  display: flex;
  align-items: center;
  height: 56px;
  gap: 14px;
  position: relative;
  overflow: visible !important;
}
.nk-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  flex-shrink: 0;
}
.nk-logo-box {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, #C0392B 0%, #D4830A 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFF;
  font-weight: 900;
  font-size: 16px;
  box-shadow: 0 2px 8px rgba(192,57,43,0.25);
}
.nk-logo-text-wrap {
  display: flex;
  flex-direction: column;
}
.nk-logo-kn {
  font-size: 19px;
  font-weight: 900;
  color: #1C1209;
  line-height: 1;
  letter-spacing: -0.5px;
}
.nk-logo-en {
  font-size: 8.5px;
  color: #C0392B;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* 6-Button Combined Navigation Links with Smooth Hover */
.nk-nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  flex: 1;
  padding: 4px 0;
  overflow: visible !important;
}

@media (max-width: 990px) {
  .nk-nav-links {
    overflow-x: auto !important;
    scrollbar-width: none;
  }
  .nk-nav-links::-webkit-scrollbar { display: none; }
}

/* Dropdown Menu Component */
.nk-nav-dropdown {
  position: relative;
  display: inline-flex;
  align-items: center;
  flex-shrink: 0;
}
.nk-nav-dropbtn {
  padding: 7px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 800;
  color: #334155;
  background: #F8FAFC;
  border: 1.5px solid #E2E8F0;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: inherit;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.nk-nav-dropdown:hover .nk-nav-dropbtn,
.nk-nav-dropdown.active .nk-nav-dropbtn,
.nk-nav-dropdown.open .nk-nav-dropbtn {
  color: #B91C1C;
  background: #FEF2F2;
  border-color: #FECACA;
  box-shadow: 0 2px 10px rgba(185,28,28,0.1);
}
.nk-dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: #FFFFFF;
  min-width: 240px;
  border-radius: 14px;
  box-shadow: 0 16px 40px -4px rgba(15, 23, 42, 0.18), 0 0 0 1px rgba(0,0,0,0.06);
  border: 1px solid #E2E8F0;
  padding: 8px;
  z-index: 999999;
  margin-top: 4px;
}
/* Invisible hover bridge to prevent menu from closing when moving cursor */
.nk-dropdown-menu::before {
  content: '';
  position: absolute;
  top: -12px;
  left: 0;
  right: 0;
  height: 12px;
}
.nk-nav-dropdown:hover .nk-dropdown-menu,
.nk-nav-dropdown:focus-within .nk-dropdown-menu,
.nk-nav-dropdown.open .nk-dropdown-menu {
  display: block;
  animation: nkFadeDown 0.18s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes nkFadeDown {
  from { opacity: 0; transform: translateY(-6px); }
  to { opacity: 1; transform: translateY(0); }
}
.nk-drop-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 12px;
  font-size: 13px;
  font-weight: 700;
  color: #1E293B;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.nk-drop-item:hover {
  background: #FEF2F2;
  color: #B91C1C;
  transform: translateX(3px);
}
.nk-drop-item.active {
  background: #FDECEA;
  color: #B91C1C;
  font-weight: 800;
}

.nk-loc-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #FDECEA;
  border: 1.5px solid rgba(192,57,43,0.25);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 12px;
  font-weight: 800;
  color: #C0392B;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  font-family: 'Anek Kannada', sans-serif;
  flex-shrink: 0;
}
.nk-loc-btn:hover { background: #C0392B; color: #fff; transform: translateY(-1px); }
.nk-loc-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #16A34A;
  animation: nkp 2s infinite;
}
@keyframes nkp { 0%,100%{opacity:1}50%{opacity:0.3} }
</style>
<div class="nk-nav">
  <!-- Mini ticker for tool pages -->
  <div class="nk-nav-ticker">
    <div class="nk-ticker-label">🔴 ಲೈವ್</div>
    <div class="nk-ticker-text" id="nk-ticker-text">ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ · karnata.in</div>
  </div>
  <!-- Masthead -->
  <div class="nk-masthead">
    <div class="nk-mh-inner">
      <a href="/" class="nk-logo" title="Karnata.in — Universe Of Karnataka">
        <img src="/karnata-logo.png" alt="Karnata.in Logo" style="height:36px; object-fit:contain; border-radius:6px;">
        <div class="nk-logo-text-wrap">
          <span class="nk-logo-kn">ಕರ್ನಾಟ</span>
          <span class="nk-logo-en">KARNATA.IN</span>
        </div>
      </a>

      <!-- EXACTLY 6 HOVER DROPDOWN MENU BUTTONS -->
      <div class="nk-nav-links">
        
        <!-- BUTTON 1: KARNATAKA & ADMINISTRATION -->
        <div class="nk-nav-dropdown ${isActive('/karnataka') || isActive('/gba') || isActive('/gram-panchayat') || isActive('/nanna-sthala') || isActive('/cabinet-ministers') || isActive('/former-cms') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>👑 ಕರ್ನಾಟಕ & ಆಡಳಿತ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/karnataka" class="nk-drop-item ${isActive('/karnataka') ? 'active' : ''}">👑 ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ</a>
            <a href="/gba" class="nk-drop-item ${isActive('/gba') ? 'active' : ''}">🏙️ GBA ಬೆಂಗಳೂರು (5 ಪಾಲಿಕೆಗಳು & 369 ವಾರ್ಡ್)</a>
            <a href="/gram-panchayat" class="nk-drop-item ${isActive('/gram-panchayat') ? 'active' : ''}">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್ (5,958 GPs)</a>
            <a href="/nanna-sthala" class="nk-drop-item ${isActive('/nanna-sthala') ? 'active' : ''}">📍 ನನ್ನ ಸ್ಥಳ (My Location)</a>
            <a href="/cabinet-ministers" class="nk-drop-item ${isActive('/cabinet-ministers') ? 'active' : ''}">👥 ಸಚಿವ ಸಂಪುಟ (33 ಸಚಿವರು)</a>
            <a href="/former-cms" class="nk-drop-item ${isActive('/former-cms') ? 'active' : ''}">📜 ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು</a>
            <a href="/local-government" class="nk-drop-item ${isActive('/local-government') ? 'active' : ''}">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು (810 ULB)</a>
            <a href="/officers" class="nk-drop-item ${isActive('/officers') ? 'active' : ''}">👥 ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ</a>
          </div>
        </div>

        <!-- BUTTON 2: ELECTIONS & REPRESENTATIVES -->
        <div class="nk-nav-dropdown ${isActive('/mla-mp') || isActive('/karnataka-sir-voter-roll') || isActive('/karnataka-elections') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>🗳️ ಚುನಾವಣೆ & ಪ್ರತಿನಿಧಿಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/mla-mp" class="nk-drop-item ${isActive('/mla-mp') ? 'active' : ''}">🏛️ ಶಾಸಕರು, MLC & ಸಂಸದರು (MLA / MLC / MP)</a>
            <a href="/karnataka-sir-voter-roll/" class="nk-drop-item ${isActive('/karnataka-sir-voter-roll') ? 'active' : ''}">🗳️ SIR 2026 ಮತದಾರರ ಕರಡು ಪಟ್ಟಿ</a>
            <a href="/karnataka-elections" class="nk-drop-item ${isActive('/karnataka-elections') ? 'active' : ''}">🗳️ ಕರ್ನಾಟಕ ಚುನಾವಣೆ ಫಲಿತಾಂಶ</a>
          </div>
        </div>

        <!-- BUTTON 3: AGRI, WATER & WEATHER -->
        <div class="nk-nav-dropdown ${isActive('/dam-levels') || isActive('/weather') || isActive('/apmc-prices') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>💧 ಕೃಷಿ, ನೀರು & ಹವಾಮಾನ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/dam-levels" class="nk-drop-item ${isActive('/dam-levels') ? 'active' : ''}">💧 ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ (Live Dam Levels)</a>
            <a href="/weather" class="nk-drop-item ${isActive('/weather') ? 'active' : ''}">🌧️ ಹವಾಮಾನ & ಮಳೆ ವರದಿ</a>
            <a href="/apmc-prices" class="nk-drop-item ${isActive('/apmc-prices') ? 'active' : ''}">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು</a>
          </div>
        </div>

        <!-- BUTTON 4: FINANCE & MARKET RATES -->
        <div class="nk-nav-dropdown ${isActive('/petrol-price') || isActive('/gold-rate') || isActive('/emi-calculator') || isActive('/sip-calculator') || isActive('/salary-calculator') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>💰 ಹಣಕಾಸು & ಮಾರುಕಟ್ಟೆ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/petrol-price" class="nk-drop-item ${isActive('/petrol-price') ? 'active' : ''}">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</a>
            <a href="/gold-rate" class="nk-drop-item ${isActive('/gold-rate') ? 'active' : ''}">🪙 ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ</a>
            <a href="/emi-calculator" class="nk-drop-item ${isActive('/emi-calculator') ? 'active' : ''}">🏦 EMI ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/sip-calculator" class="nk-drop-item ${isActive('/sip-calculator') ? 'active' : ''}">📈 SIP ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/salary-calculator" class="nk-drop-item ${isActive('/salary-calculator') ? 'active' : ''}">💰 ಸಂಬಳದ ಲೆಕ್ಕ</a>
          </div>
        </div>

        <!-- BUTTON 5: AI & DIGITAL SERVICES -->
        <div class="nk-nav-dropdown ${isActive('/ask') || isActive('/ai-jyothishya') || isActive('/kannada-typing') || isActive('/scheme-checker') || isActive('/bhoomi-rtc') || isActive('/kaveri-reports') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>🔮 AI & ಡಿಜಿಟಲ್ ಸೇವೆಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/ask" class="nk-drop-item ${isActive('/ask') ? 'active' : ''}">🤖 askKARNATA AI ಸಹಾಯಕ</a>
            <a href="/ai-jyothishya" class="nk-drop-item ${isActive('/ai-jyothishya') ? 'active' : ''}">🔮 AI ಜ್ಯೋತಿಷ್ಯ & ಕುಂಡಲಿ</a>
            <a href="/kannada-typing" class="nk-drop-item ${isActive('/kannada-typing') ? 'active' : ''}">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ & ಅನುವಾದ</a>
            <a href="/scheme-checker" class="nk-drop-item ${isActive('/scheme-checker') ? 'active' : ''}">📋 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು</a>
            <a href="/bhoomi-rtc" class="nk-drop-item ${isActive('/bhoomi-rtc') ? 'active' : ''}">📄 ಭೂಮಿ RTC & ಪಹಣಿ</a>
            <a href="/kaveri-reports" class="nk-drop-item ${isActive('/kaveri-reports') ? 'active' : ''}">📑 ಕಾವೇರಿ ಆಸ್ತಿ ವರದಿ</a>
          </div>
        </div>

        <!-- BUTTON 6: NEWS & ARTICLES -->
        <div class="nk-nav-dropdown ${isActive('/karnataka-local-news') || isActive('/karnataka-stories') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>📰 ಸುದ್ದಿ & ಲೇಖನಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/karnataka-local-news" class="nk-drop-item ${isActive('/karnataka-local-news') ? 'active' : ''}">📰 ಸ್ಥಳೀಯ ಸುದ್ದಿ (31 ಜಿಲ್ಲೆಗಳು)</a>
            <a href="/karnataka-stories" class="nk-drop-item ${isActive('/karnataka-stories') ? 'active' : ''}">✨ ವಿಶೇಷ ವಿಶ್ಲೇಷಣೆ & ಲೇಖನಗಳು</a>
          </div>
        </div>

      </div>

      <!-- Right controls -->
      <div style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
        <button class="nk-loc-btn" onclick="if(window.nkOpenLocModal) window.nkOpenLocModal(); else window.location.href='/nanna-sthala';">
          <span class="nk-loc-dot"></span>
          <span id="nk-nav-loc-label">${locLabel}</span>
        </button>
      </div>
    </div>
  </div>
</div>
`;

  if (document.body) {
    const existing = document.querySelector('.nk-nav');
    if (!existing) {
      document.body.insertAdjacentHTML('afterbegin', navHTML);
    }
  } else {
    document.addEventListener('DOMContentLoaded', function () {
      const existing = document.querySelector('.nk-nav');
      if (!existing) {
        document.body.insertAdjacentHTML('afterbegin', navHTML);
      }
    });
  }
})();
"""

with open('nav-component.js', 'w', encoding='utf-8') as f:
    f.write(nav_component_code)

print("SUCCESS_REBUILT_NAV_COMPONENT_JS")
