/**
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
      <a href="/index.html" class="nk-logo" title="Karnata.in — Universe Of Karnataka">
        <img src="/karnata-logo.png" alt="Karnata.in Logo" style="height:36px; object-fit:contain; border-radius:6px;">
        <div class="nk-logo-text-wrap">
          <span class="nk-logo-kn">ಕರ್ನಾಟ</span>
          <span class="nk-logo-en">KARNATA.IN</span>
        </div>
      </a>

      <!-- 1-Row Combined Navigation with Financial & News Dropdowns -->
      <div class="nk-nav-links">
        <a href="/ask.html" class="nk-nav-link ${isActive('/ask.html') ? 'active' : ''}">🤖 askKARNATA</a>
        <a href="/officers.html" class="nk-nav-link ${isActive('/officers.html') ? 'active' : ''}">🏛️ ಅಧಿಕಾರಿಗಳು</a>
        <a href="/ai-jyothishya.html" class="nk-nav-link ${isActive('/ai-jyothishya.html') ? 'active' : ''}">🔮 AI ಜ್ಯೋತಿಷ್ಯ</a>
        <a href="/gold-rate.html" class="nk-nav-link ${isActive('/gold-rate.html') ? 'active' : ''}">🥇 ಚಿನ್ನ</a>
        <a href="/petrol-price.html" class="nk-nav-link ${isActive('/petrol-price.html') ? 'active' : ''}">⛽ ಪೆಟ್ರೋಲ್</a>
        <a href="/dam-levels.html" class="nk-nav-link ${isActive('/dam-levels.html') ? 'active' : ''}">💧 ಅಣೆಕಟ್ಟು</a>
        <a href="/weather.html" class="nk-nav-link ${isActive('/weather.html') ? 'active' : ''}">🌧️ ಹವಾಮಾನ</a>
        <a href="/apmc-prices.html" class="nk-nav-link ${isActive('/apmc-prices.html') ? 'active' : ''}">🌾 APMC</a>
        <a href="/mla-mp.html" class="nk-nav-link ${isActive('/mla-mp.html') ? 'active' : ''}">🏛️ MLA/MP</a>
        <a href="/karnataka-elections.html" class="nk-nav-link ${isActive('/karnataka-elections.html') ? 'active' : ''}">🗳️ ಚುನಾವಣೆ</a>
        <a href="/scheme-checker.html" class="nk-nav-link ${isActive('/scheme-checker.html') ? 'active' : ''}">📋 ಯೋಜನೆ</a>

        <!-- Dropdown 1: Finance (EMI, SIP, Salary) -->
        <div class="nk-nav-dropdown ${isActive('/emi-calculator.html') || isActive('/sip-calculator.html') || isActive('/salary-calculator.html') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>💰 ಹಣಕಾಸು / ಲೆಕ್ಕ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/emi-calculator.html" class="nk-drop-item ${isActive('/emi-calculator.html') ? 'active' : ''}">🏦 EMI ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/sip-calculator.html" class="nk-drop-item ${isActive('/sip-calculator.html') ? 'active' : ''}">📈 SIP ಲೆಕ್ಕಾಚಾರ</a>
            <a href="/salary-calculator.html" class="nk-drop-item ${isActive('/salary-calculator.html') ? 'active' : ''}">💰 ಸಂಬಳದ ಲೆಕ್ಕ</a>
          </div>
        </div>

        <!-- Dropdown 2: News & Stories (Local News, Special Stories) -->
        <div class="nk-nav-dropdown ${isActive('/karnataka-local-news.html') || isActive('/karnataka-stories.html') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>📰 ಸುದ್ದಿ & ಲೇಖನ</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/karnataka-local-news.html" class="nk-drop-item ${isActive('/karnataka-local-news.html') ? 'active' : ''}">📰 ಸ್ಥಳೀಯ ಸುದ್ದಿ (31 ಜಿಲ್ಲೆಗಳು)</a>
            <a href="/karnataka-stories.html" class="nk-drop-item ${isActive('/karnataka-stories.html') ? 'active' : ''}">✨ ವಿಶೇಷ ಲೇಖನಗಳು</a>
          </div>
        </div>

        <a href="/more-tools.html" class="nk-nav-link ${isActive('/more-tools.html') ? 'active' : ''}">🛠️ ಇನ್ನಷ್ಟು</a>
      </div>

      <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
        <button class="nk-notif-btn" onclick="window.location.href='/index.html#smart-search-input'" title="Karnata Smart Search Engine" style="background:#FFE4E6;border-color:#FECDD3;">🤖</button>
        <button class="nk-loc-btn" id="nk-loc-btn">
          <div class="nk-loc-dot"></div>
          <span id="nk-loc-text">${locLabel}</span>
        </button>
        <button class="nk-notif-btn" id="nk-notif-btn" title="ಅಧಿಸೂಚನೆ">🔔</button>
      </div>
    </div>
  </div>
</div>`;

  const isAskPage = window.location.pathname.toLowerCase().includes('ask');

  // Mobile bottom nav (suppressed on ask AI page)
  const mobileNav = isAskPage ? '' : `
<nav id="nk-mob-nav" style="
  display:none;position:fixed;bottom:0;left:0;right:0;
  background:rgba(255,255,255,0.98);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border-top:1px solid #E0DAD0;
  padding:6px 0 env(safe-area-inset-bottom,6px);
  z-index:9999;box-shadow:0 -4px 24px rgba(28,18,9,0.08);
  font-family:'Anek Kannada',sans-serif;
">
  <div style="display:grid;grid-template-columns:repeat(5,1fr);">
    ${[
      {href:'/index.html',          icon:'🏠', label:'ಮುಖಪುಟ'},
      {href:'/ai-jyothishya.html',  icon:'🔮', label:'ಜ್ಯೋತಿಷ್ಯ'},
      {href:'/karnataka-local-news.html', icon:'📰', label:'ಸುದ್ದಿ'},
      {href:'/gold-rate.html',      icon:'🥇', label:'ಚಿನ್ನ'},
      {href:'/more-tools.html',     icon:'🛠️', label:'ಇನ್ನಷ್ಟು'},
    ].map(b => `
      <a href="${b.href}" style="
        display:flex;flex-direction:column;align-items:center;
        gap:2px;padding:6px 2px;text-decoration:none;
      ">
        <span style="font-size:20px">${b.icon}</span>
        <span style="font-size:9px;font-weight:700;color:${isActive(b.href)?'#C0392B':'#BAA898'};">${b.label}</span>
      </a>`).join('')}
  </div>
</nav>
<style>
@media(max-width:860px){
  #nk-mob-nav{display:block!important;}
  body{padding-bottom:66px!important;}
}
</style>`;

  // Inject nav if no existing topnav/nk-nav
  if (!document.querySelector('.nk-nav') && !document.querySelector('.masthead') && !document.querySelector('.ticker-wrap')) {
    document.body.insertAdjacentHTML('afterbegin', navHTML);
  }

  // Inject mobile nav
  if (!document.querySelector('#nk-mob-nav') && !document.querySelector('.mobile-nav')) {
    document.body.insertAdjacentHTML('beforeend', mobileNav);
  }

  // Close dropdowns when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nk-nav-dropdown')) {
      document.querySelectorAll('.nk-nav-dropdown.open').forEach(d => d.classList.remove('open'));
    }
  });

  // Load live ticker data
  fetch('/data/gold_rates.json').then(r=>r.json()).then(g=>{
    const p22 = g?.base?.['22k_per_gram'] || g?.baseGold?.[22];
    const ch  = g?.change?.['22k'] || g?.changes?.['22k'] || 0;
    const el  = document.getElementById('nk-ticker-text');
    if(el && p22) {
      el.innerHTML = `🥇 22K ಚಿನ್ನ <span>₹${p22}/g</span> &nbsp;${ch>=0?'▲':'▼'} ₹${Math.abs(ch)} &nbsp;·&nbsp; 🔮 AI ಜ್ಯೋತಿಷ್ಯ &nbsp;·&nbsp; ⛽ ಪೆಟ್ರೋಲ್ &nbsp;·&nbsp; 💧 ಅಣೆಕಟ್ಟು ಮಟ್ಟ &nbsp;·&nbsp; Karnata.in`;
    }
  }).catch(()=>{});

  // Universal Notification Toast Function
  window.showKarnataToast = function(title, msg) {
    let toast = document.getElementById('nk-universal-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'nk-universal-toast';
      toast.style.cssText = 'position:fixed;top:80px;right:20px;z-index:99999;background:#0F172A;color:#FFF;border-radius:12px;padding:14px 20px;max-width:320px;box-shadow:0 10px 30px rgba(0,0,0,0.25);border-left:4px solid #E11D48;font-family:"Anek Kannada",sans-serif;display:none;';
      document.body.appendChild(toast);
    }
    toast.innerHTML = `<div style="font-weight:900;font-size:14.5px;margin-bottom:3px;">${title}</div><div style="font-size:12.5px;color:#94A3B8;line-height:1.4;">${msg}</div>`;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 4500);
  };

  // Wire Location Button
  const locBtn = document.getElementById('nk-loc-btn');
  if(locBtn) {
    locBtn.addEventListener('click', () => {
      if(typeof showGeoSheet === 'function') showGeoSheet();
      else window.location.href = '/index.html#geo';
    });
  }

  // Universal AdSense Compliant Footer Injection
  const footerHTML = `
<footer style="background:#0F172A; color:#94A3B8; padding:48px 20px 32px; font-family:'Anek Kannada',sans-serif; margin-top:60px; border-top:4px solid #E11D48;">
  <div style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:32px;">
    <div>
      <div style="font-size:22px; font-weight:900; color:#FFF; margin-bottom:12px;">ಕರ್ನಾಟ (Karnata.in)</div>
      <p style="font-size:13.5px; line-height:1.7; color:#CBD5E1;">ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳು, ಶಾಸಕರು, ಸಂಸದರು, ಸಜೀವ APMC ಕೃಷಿ ದರಗಳು, ಚಿನ್ನ-ಇಂಧನ ಬೆಲೆಗಳು ಹಾಗೂ ಸುದ್ದಿ ಮಾಹಿತಿಯ ಅಧಿಕೃತ ಮುಕ್ತ ಡಿಜಿಟಲ್ ವೇದಿಕೆ.</p>
    </div>
    <div>
      <div style="font-size:16px; font-weight:800; color:#FFF; margin-bottom:14px;">📍 ಜಿಲ್ಲೆಗಳು & ಸೇವೆಗಳು</div>
      <div style="display:flex; flex-direction:column; gap:8px; font-size:13.5px;">
        <a href="/districts/" style="color:#CBD5E1; text-decoration:none;">📍 31 ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿ</a>
        <a href="/ai-jyothishya.html" style="color:#CBD5E1; text-decoration:none;">🔮 AI ಜ್ಯೋತಿಷ್ಯ & ಕುಂಡಲಿ</a>
        <a href="/gold-rate.html" style="color:#CBD5E1; text-decoration:none;">🥇 ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ</a>
        <a href="/petrol-price.html" style="color:#CBD5E1; text-decoration:none;">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</a>
        <a href="/apmc-prices.html" style="color:#CBD5E1; text-decoration:none;">🌾 APMC ಕೃಷಿ ದರಗಳು</a>
        <a href="/dam-levels.html" style="color:#CBD5E1; text-decoration:none;">💧 ಜಲಾಶಯಗಳ ನೀರು</a>
      </div>
    </div>
    <div>
      <div style="font-size:16px; font-weight:800; color:#FFF; margin-bottom:14px;">📜 ನೀತಿಗಳು & ನಿಯಮಗಳು</div>
      <div style="display:flex; flex-direction:column; gap:8px; font-size:13.5px;">
        <a href="/about.html" style="color:#CBD5E1; text-decoration:none;">ℹ️ ನಮ್ಮ ಬಗ್ಗೆ (About Us)</a>
        <a href="/contact.html" style="color:#CBD5E1; text-decoration:none;">✉️ ಸಂಪರ್ಕಿಸಿ (Contact Us)</a>
        <a href="/privacy-policy.html" style="color:#CBD5E1; text-decoration:none;">🔒 ಖಾಸಗೀತಾ ನೀತಿ (Privacy Policy)</a>
        <a href="/terms.html" style="color:#CBD5E1; text-decoration:none;">📜 ನಿಯಮಗಳು & ಷರತ್ತುಗಳು (Terms)</a>
      </div>
    </div>
  </div>
  <div style="max-width:1200px; margin:32px auto 0; padding-top:20px; border-top:1px solid #1E293B; text-align:center; font-size:13px; color:#64748B;">
    © 2026 Karnata.in (ಕರ್ನಾಟ) — Universe of Karnataka. All Rights Reserved.
  </div>
</footer>`;

  function injectFooter() {
    if (isAskPage || document.querySelector('footer') || document.querySelector('.site-footer')) return;
    if (document.body) {
      document.body.insertAdjacentHTML('beforeend', footerHTML);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFooter);
  } else {
    injectFooter();
  }

})();
