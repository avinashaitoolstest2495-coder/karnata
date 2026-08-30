import sys
sys.stdout.reconfigure(encoding='utf-8')

clean_nav_js = """/**
 * nav-component.js — Karnata v4 Masterclass Header
 * Injects single, clean, ultra-responsive 1-row header into tool pages with dropdown menus.
 * Rebranded: "ಕರ್ನಾಟ — Karnata.in (Universe Of Karnataka)"
 */
(function () {
  // Inject Google AdSense script for karnata.in
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
  padding: 0 12px;
  position: relative;
  overflow: visible !important;
  width: 100%;
  max-width: 100%;
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
  gap: 10px;
  padding: 0 4px;
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
  font-size: 18px;
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

/* 1-Row Combined Navigation Links */
.nk-nav-links {
  display: flex;
  align-items: center;
  gap: 4px;
  flex: 1;
  padding: 4px 0;
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
  position: relative;
}
.nk-nav-links::-webkit-scrollbar { display: none; }

@media (min-width: 1024px) {
  .nk-nav-links {
    overflow: visible !important;
  }
}

.nk-nav-link {
  padding: 6px 10px;
  border-radius: 18px;
  font-size: 12px;
  font-weight: 700;
  color: #4A3828;
  white-space: nowrap;
  text-decoration: none;
  border: 1px solid transparent;
  transition: all 0.15s ease;
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.nk-nav-link:hover { color: #C0392B; background: #FDECEA; border-color: rgba(192,57,43,0.2); }
.nk-nav-link.active { color: #fff; background: #C0392B; border-color: #C0392B; box-shadow: 0 2px 8px rgba(192,57,43,0.25); }

/* Dropdown Menu Component */
.nk-nav-dropdown {
  position: relative;
  display: inline-flex;
  align-items: center;
  flex-shrink: 0;
}
.nk-nav-dropbtn {
  padding: 6px 10px;
  border-radius: 18px;
  font-size: 12px;
  font-weight: 700;
  color: #4A3828;
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: inherit;
  transition: all 0.15s ease;
}
.nk-nav-dropdown:hover .nk-nav-dropbtn, .nk-nav-dropdown.active .nk-nav-dropbtn, .nk-nav-dropdown.open .nk-nav-dropbtn {
  color: #C0392B;
  background: #FDECEA;
  border-color: rgba(192,57,43,0.2);
}
.nk-dropdown-menu {
  display: none;
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  background: #FFFFFF;
  min-width: 200px;
  border-radius: 12px;
  box-shadow: 0 12px 36px rgba(0,0,0,0.2);
  border: 1px solid #CBD5E1;
  padding: 6px;
  z-index: 99999;
}
.nk-nav-dropdown:hover .nk-dropdown-menu, .nk-nav-dropdown.open .nk-dropdown-menu {
  display: block;
}
.nk-drop-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  font-size: 12.5px;
  font-weight: 700;
  color: #1E293B;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.nk-drop-item:hover {
  background: #FEF2F2;
  color: #C0392B;
}
.nk-drop-item.active {
  background: #FDECEA;
  color: #C0392B;
  font-weight: 800;
}

.nk-loc-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #FDECEA;
  border: 1.5px solid rgba(192,57,43,0.25);
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 11.5px;
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
.nk-notif-btn {
  width: 34px; height: 34px;
  border-radius: 50%;
  border: 1.5px solid #E0DAD0;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}
.nk-notif-btn:hover { border-color: #C0392B; background: #FDECEA; transform: translateY(-1px); }
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

      <!-- 1-Row Combined Navigation with Financial & News Dropdowns -->
      <div class="nk-nav-links">
        <!-- Dropdown 0: Karnataka (Portal, Cabinet Ministers, Former CMs, SIR 2026 Voter Roll) -->
        <div class="nk-nav-dropdown ${isActive('/karnataka') || isActive('/cabinet-ministers') || isActive('/former-cms') || isActive('/karnataka-sir-voter-roll') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>👑 ಕರ್ನಾಟಕ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/karnataka" class="nk-drop-item ${isActive('/karnataka') ? 'active' : ''}">👑 ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ</a>
            <a href="/karnataka-sir-voter-roll/" class="nk-drop-item ${isActive('/karnataka-sir-voter-roll') ? 'active' : ''}">🗳️ SIR 2026 ಮತದಾರರ ಪಟ್ಟಿ (Voter Roll)</a>
            <a href="/gram-panchayat" class="nk-drop-item ${isActive('/gram-panchayat') ? 'active' : ''}">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್ (5,958 GPs)</a>
            <a href="/nanna-sthala" class="nk-drop-item ${isActive('/nanna-sthala') ? 'active' : ''}">📍 ನನ್ನ ಸ್ಥಳ (My Karnataka Location)</a>
            <a href="/gba" class="nk-drop-item ${isActive('/gba') ? 'active' : ''}">🏙️ GBA ಬೆಂಗಳೂರು (5 ಪಾಲಿಕೆಗಳು & 369 ವಾರ್ಡ್‌ಗಳು)</a>
            <a href="/local-government" class="nk-drop-item ${isActive('/local-government') ? 'active' : ''}">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು & ವಾರ್ಡ್‌ಗಳು (810 ULB/ZP)</a>
            <a href="/cabinet-ministers" class="nk-drop-item ${isActive('/cabinet-ministers') ? 'active' : ''}">👥 ಸಚಿವ ಸಂಪುಟ (33 ಸಚಿವರು)</a>
            <a href="/former-cms" class="nk-drop-item ${isActive('/former-cms') ? 'active' : ''}">📜 ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು</a>
          </div>
        </div>
        <a href="/ask" class="nk-nav-link ${isActive('/ask') ? 'active' : ''}">🤖 askKARNATA</a>
        <a href="/nanna-sthala" class="nk-nav-link ${isActive('/nanna-sthala') ? 'active' : ''}">📍 ನನ್ನ ಸ್ಥಳ</a>
        <a href="/gba" class="nk-nav-link ${isActive('/gba') ? 'active' : ''}">🏙️ GBA ಬೆಂಗಳೂರು</a>
        <a href="/gram-panchayat" class="nk-nav-link ${isActive('/gram-panchayat') ? 'active' : ''}">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್</a>
        <a href="/local-government" class="nk-nav-link ${isActive('/local-government') ? 'active' : ''}">🏛️ ಸ್ಥಳೀಯ ಆಡಳಿತ</a>
        <a href="/officers" class="nk-nav-link ${isActive('/officers') ? 'active' : ''}">👥 ಅಧಿಕಾರಿಗಳು</a>
        <a href="/ai-jyothishya" class="nk-nav-link ${isActive('/ai-jyothishya') ? 'active' : ''}">🔮 AI ಜ್ಯೋತಿಷ್ಯ</a>
        <a href="/dam-levels" class="nk-nav-link ${isActive('/dam-levels') ? 'active' : ''}">💧 ಅಣೆಕಟ್ಟು</a>
        <a href="/weather" class="nk-nav-link ${isActive('/weather') ? 'active' : ''}">🌧️ ಹವಾಮಾನ</a>
        <a href="/apmc-prices" class="nk-nav-link ${isActive('/apmc-prices') ? 'active' : ''}">🌾 APMC</a>
        <a href="/mla-mp" class="nk-nav-link ${isActive('/mla-mp') ? 'active' : ''}">🏛️ MLA/MP</a>
        <a href="/karnataka-sir-voter-roll/" class="nk-nav-link ${isActive('/karnataka-sir-voter-roll') ? 'active' : ''}">🗳️ ಮತದಾರರ ಪಟ್ಟಿ</a>
        <a href="/karnataka-elections" class="nk-nav-link ${isActive('/karnataka-elections') ? 'active' : ''}">🗳️ ಚುನಾವಣೆ</a>
        <a href="/scheme-checker" class="nk-nav-link ${isActive('/scheme-checker') ? 'active' : ''}">📋 ಯೋಜನೆ</a>

        <!-- Dropdown 1: Finance (EMI, SIP, Salary) -->
        <div class="nk-nav-dropdown ${isActive('/emi-calculator') || isActive('/sip-calculator') || isActive('/salary-calculator') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>💰 ಹಣಕಾಸು / ಲೆಕ್ಕ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/emi-calculator" class="nk-drop-item ${isActive('/emi-calculator') ? 'active' : ''}">🏦 EMI ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/sip-calculator" class="nk-drop-item ${isActive('/sip-calculator') ? 'active' : ''}">📈 SIP ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/salary-calculator" class="nk-drop-item ${isActive('/salary-calculator') ? 'active' : ''}">💰 standard ಸಂಬಳದ ಲೆಕ್ಕ</a>
          </div>
        </div>

        <!-- Dropdown 2: News & Stories (Local News, Special Stories) -->
        <div class="nk-nav-dropdown ${isActive('/karnataka-local-news') || isActive('/karnataka-stories') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>📰 ಸುದ್ದಿ & ಲೇಖನ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/karnataka-local-news" class="nk-drop-item ${isActive('/karnataka-local-news') ? 'active' : ''}">📰 ಸ್ಥಳೀಯ ಸುದ್ದಿ (31 ಜಿಲ್ಲೆಗಳು)</a>
            <a href="/karnataka-stories" class="nk-drop-item ${isActive('/karnataka-stories') ? 'active' : ''}">✨ ವಿಶೇಷ ಲೇಖನಗಳು</a>
          </div>
        </div>

        <a href="/petrol-price" class="nk-nav-link ${isActive('/petrol-price') ? 'active' : ''}">⛽ ಪೆಟ್ರೋಲ್</a>
        <a href="/gold-rate" class="nk-nav-link ${isActive('/gold-rate') ? 'active' : ''}">🪙 ಚಿನ್ನ</a>
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

with open(r'c:\Users\avina\Downloads\karnata-site-with-cms\nav-component.js', 'w', encoding='utf-8') as f:
    f.write(clean_nav_js)

print("Successfully wrote clean nav-component.js!")
