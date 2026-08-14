/**
 * nav-component.js — Karnata v4 Masterclass Header
 * Injects single, clean, ultra-responsive header into tool pages.
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

  const links = [
    { href:'/ask.html',               label:'🤖 askKARNATA' },
    { href:'/gold-rate.html',         label:'🥇 ಚಿನ್ನ' },
    { href:'/petrol-price.html',      label:'⛽ ಪೆಟ್ರೋಲ್' },
    { href:'/dam-levels.html',        label:'💧 ಅಣೆಕಟ್ಟು' },
    { href:'/weather.html',           label:'🌧️ ಹವಾಮಾನ' },
    { href:'/apmc-prices.html',       label:'🌾 APMC' },
    { href:'/mla-mp.html',           label:'🏛️ MLA/MP' },
    { href:'/karnataka-elections.html', label:'🗳️ ಚುನಾವಣೆ 1978-2023' },
    { href:'/emi-calculator.html',    label:'🏦 EMI' },
    { href:'/sip-calculator.html',    label:'📈 SIP' },
    { href:'/salary-calculator.html', label:'💰 ಸಂಬಳ' },
    { href:'/scheme-checker.html',    label:'📋 ಯೋಜನೆ' },
    { href:'/news-explainers.html',   label:'📰 ಸುದ್ದಿ' },
    { href:'/cms/admin.html',         label:'⚙️ CMS' },
    { href:'/more-tools.html',        label:'🛠️ ಇನ್ನಷ್ಟು' },
  ];

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
  position: sticky; top: 0; z-index: 100;
  font-family: 'Anek Kannada', sans-serif;
  box-shadow: 0 4px 20px rgba(28,18,9,0.08);
}
.nk-nav-ticker {
  background: #1C1209;
  height: 32px;
  display: flex;
  align-items: center;
  overflow: hidden;
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
  padding-left: 14px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.nk-ticker-text span { color: #FFD700; font-weight: 700; margin: 0 4px; }

.nk-masthead {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 3px solid #C0392B;
  padding: 0 16px;
}
.nk-mh-inner {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  height: 56px;
  gap: 16px;
  padding: 0 20px;
}
.nk-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}
.nk-logo-box {
  width: 36px; height: 36px;
  background: linear-gradient(135deg, #C0392B 0%, #D4830A 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFF;
  font-weight: 900;
  font-size: 18px;
  box-shadow: 0 2px 8px rgba(192,57,43,0.25);
}
.nk-logo-text-wrap {
  display: flex;
  flex-direction: column;
}
.nk-logo-kn {
  font-size: 20px;
  font-weight: 900;
  color: #1C1209;
  line-height: 1;
  letter-spacing: -0.5px;
}
.nk-logo-en {
  font-size: 9px;
  color: #C0392B;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.nk-nav-links {
  display: flex;
  gap: 4px;
  overflow-x: auto;
  scrollbar-width: none;
  flex: 1;
  padding: 4px 0;
}
.nk-nav-links::-webkit-scrollbar { display: none; }
.nk-nav-link {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  color: #4A3828;
  white-space: nowrap;
  text-decoration: none;
  border: 1px solid transparent;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
}
.nk-nav-link:hover { color: #C0392B; background: #FDECEA; border-color: rgba(192,57,43,0.2); }
.nk-nav-link.active { color: #fff; background: #C0392B; border-color: #C0392B; box-shadow: 0 2px 8px rgba(192,57,43,0.25); }

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
.nk-notif-btn {
  width: 36px; height: 36px;
  border-radius: 50%;
  border: 1.5px solid #E0DAD0;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
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
        <img src="/karnata-logo.png" alt="Karnata.in Logo" style="height:38px; object-fit:contain; border-radius:6px;">
        <div class="nk-logo-text-wrap">
          <span class="nk-logo-kn">ಕರ್ನಾಟ</span>
          <span class="nk-logo-en">KARNATA.IN</span>
        </div>
      </a>
      <div class="nk-nav-links">
        ${links.map(l => `<a href="${l.href}" class="nk-nav-link ${isActive(l.href) ? 'active' : ''}">${l.label}</a>`).join('')}
      </div>
      <div style="display:flex;align-items:center;gap:8px;flex-shrink:0;">
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

  // Mobile bottom nav
  const mobileNav = `
<nav id="nk-mob-nav" style="
  display:none;position:fixed;bottom:0;left:0;right:0;
  background:rgba(255,255,255,0.95);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border-top:1px solid #E0DAD0;
  padding:6px 0 env(safe-area-inset-bottom,6px);
  z-index:99;box-shadow:0 -4px 24px rgba(28,18,9,0.08);
  font-family:'Anek Kannada',sans-serif;
">
  <div style="display:grid;grid-template-columns:repeat(5,1fr);">
    ${[
      {href:'/index.html',          icon:'🏠', label:'ಮುಖಪುಟ'},
      {href:'/gold-rate.html',      icon:'🥇', label:'ಚಿನ್ನ'},
      {href:'/petrol-price.html',   icon:'⛽', label:'ಪೆಟ್ರೋಲ್'},
      {href:'/dam-levels.html',     icon:'💧', label:'ಅಣೆಕಟ್ಟು'},
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
  body{padding-bottom:62px!important;}
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

  // Load live ticker data
  fetch('/data/gold_rates.json').then(r=>r.json()).then(g=>{
    const p22 = g?.base?.['22k_per_gram'];
    const ch  = g?.change?.['22k'] || 0;
    const el  = document.getElementById('nk-ticker-text');
    if(el && p22) {
      el.innerHTML = `🥇 22K ಚಿನ್ನ <span>₹${p22}/g</span> &nbsp;${ch>=0?'▲':'▼'} ₹${Math.abs(ch)} &nbsp;·&nbsp; ⛽ ಪೆಟ್ರೋಲ್ &nbsp;·&nbsp; 💧 ಅಣೆಕಟ್ಟು ಮಟ್ಟ &nbsp;·&nbsp; Karnata.in — Universe Of Karnataka`;
    }
  }).catch(()=>{});

  // Wire location button
  const locBtn = document.getElementById('nk-loc-btn');
  if(locBtn) {
    locBtn.addEventListener('click', () => {
      if(typeof showGeoSheet === 'function') showGeoSheet();
      else window.location.href = '/index.html#geo';
    });
  }

  // Notif button
  const notifBtn = document.getElementById('nk-notif-btn');
  if(notifBtn) {
    notifBtn.addEventListener('click', () => {
      if(typeof showNotif === 'function') showNotif();
      else if(typeof OneSignal !== 'undefined') OneSignal.Notifications.requestPermission();
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
        <a href="/gold-rates.html" style="color:#CBD5E1; text-decoration:none;">🥇 ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ</a>
        <a href="/petrol-diesel.html" style="color:#CBD5E1; text-decoration:none;">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</a>
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

  if (!window.location.pathname.includes('/ask') && !document.querySelector('footer')) {
    document.body.insertAdjacentHTML('beforeend', footerHTML);
  }

})();
