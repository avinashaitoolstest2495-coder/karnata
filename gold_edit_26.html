# -*- coding: utf-8 -*-
"""
Karnata — scripts/upgrade_mobile_layout.py
Upgrades mobile responsiveness across:
1. nav-component.js (2-row mobile header: Logo + Location on top, smooth horizontal scroll nav pills below).
2. gold-rate.html (Mobile-first tabs, responsive city rates table, 3/4-col seasonality heatmap, responsive AI cards).
3. Site-wide mobile viewport & overflow prevention.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPGRADE nav-component.js FOR SEAMLESS MOBILE DESIGN
# ══════════════════════════════════════════════════════════════════════════════
nav_code = """/**
 * nav-component.js — Karnata v5 Mobile-First & Desktop Masterclass Header
 * 100% Responsive: Dual-row mobile header with horizontal category rail.
 * Zero horizontal overflow, fast touch response.
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

/* Global overflow protection */
html, body {
  overflow-x: hidden !important;
  width: 100% !important;
  max-width: 100vw !important;
  box-sizing: border-box !important;
}

.topnav { display: none !important; }

.nk-nav {
  position: sticky; top: 0; z-index: 999999;
  font-family: 'Anek Kannada', sans-serif;
  box-shadow: 0 4px 20px rgba(28,18,9,0.08);
  width: 100%;
  max-width: 100vw;
  box-sizing: border-box;
  background: #FFFFFF;
}

/* Mini Ticker */
.nk-nav-ticker {
  background: #1C1209;
  height: 28px;
  display: flex;
  align-items: center;
  overflow: hidden;
  width: 100%;
  box-sizing: border-box;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.nk-ticker-label {
  background: linear-gradient(135deg, #C0392B, #A93226);
  color: #fff;
  font-size: 9.5px;
  font-weight: 900;
  padding: 0 10px;
  height: 100%;
  display: flex;
  align-items: center;
  letter-spacing: 0.05em;
  flex-shrink: 0;
  text-transform: uppercase;
}
.nk-ticker-text {
  font-size: 11.5px;
  color: rgba(255,255,255,0.85);
  padding: 0 10px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 1;
}

/* Masthead Container */
.nk-masthead {
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 2px solid #C0392B;
  padding: 0 12px;
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
  justify-content: space-between;
  height: 52px;
  gap: 8px;
}

.nk-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  flex-shrink: 0;
}
.nk-logo-img {
  height: 32px;
  width: auto;
  object-fit: contain;
  border-radius: 6px;
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
  font-size: 8px;
  color: #C0392B;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* Category Navigation Bar */
.nk-nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  height: 52px;
}

/* Dropdown Menu Component */
.nk-nav-dropdown {
  position: relative;
  display: inline-flex;
  align-items: center;
  height: 100%;
  flex-shrink: 0;
}
.nk-nav-dropbtn {
  padding: 6px 11px;
  border-radius: 20px;
  font-size: 12.5px;
  font-weight: 800;
  color: #334155;
  background: #F8FAFC;
  border: 1.5px solid #E2E8F0;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
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
  box-shadow: 0 2px 10px rgba(185,28,28,0.12);
}
.nk-dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: #FFFFFF;
  min-width: 230px;
  max-width: 90vw;
  border-radius: 14px;
  box-shadow: 0 18px 45px -4px rgba(15, 23, 42, 0.22), 0 0 0 1px rgba(0,0,0,0.06);
  border: 1.5px solid #E2E8F0;
  padding: 8px;
  z-index: 999999;
}
.nk-nav-dropdown.open .nk-dropdown-menu,
.nk-nav-dropdown:hover .nk-dropdown-menu {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.nk-drop-item {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  color: #334155;
  text-decoration: none;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.nk-drop-item:hover, .nk-drop-item.active {
  background: #FEF2F2;
  color: #B91C1C;
}

/* Location Badge */
.nk-loc-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #FFF1F2;
  border: 1.5px solid #FECACA;
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 11.5px;
  font-weight: 800;
  color: #C0392B;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  font-family: inherit;
  flex-shrink: 0;
}
.nk-loc-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #16A34A;
  animation: nkp 2s infinite;
}
@keyframes nkp { 0%,100%{opacity:1}50%{opacity:0.3} }

/* MOBILE RESPONSIVE OPTIMIZATIONS (< 860px) */
@media (max-width: 860px) {
  .nk-mh-inner {
    height: 48px;
  }
  .nk-nav-links-desktop {
    display: none !important;
  }
  .nk-mobile-rail {
    display: flex !important;
    align-items: center;
    gap: 6px;
    padding: 6px 12px 8px;
    background: #FFFFFF;
    border-bottom: 1px solid #F1F5F9;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    width: 100%;
    box-sizing: border-box;
  }
  .nk-mobile-rail::-webkit-scrollbar { display: none; }
  .nk-mobile-chip {
    padding: 6px 12px;
    border-radius: 18px;
    font-size: 12px;
    font-weight: 800;
    color: #334155;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    text-decoration: none;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
  }
  .nk-mobile-chip.active {
    background: #FEF2F2;
    color: #B91C1C;
    border-color: #FECACA;
  }
}
@media (min-width: 861px) {
  .nk-mobile-rail { display: none !important; }
}
</style>

<div class="nk-nav">
  <!-- Mini Ticker -->
  <div class="nk-nav-ticker">
    <div class="nk-ticker-label">🔴 ಲೈವ್</div>
    <div class="nk-ticker-text" id="nk-ticker-text">ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ · karnata.in</div>
  </div>

  <!-- Masthead -->
  <div class="nk-masthead">
    <div class="nk-mh-inner">
      <a href="/" class="nk-logo" title="Karnata.in — Universe Of Karnataka">
        <img src="/karnata-logo.png" alt="Karnata.in Logo" class="nk-logo-img">
        <div class="nk-logo-text-wrap">
          <span class="nk-logo-kn">ಕರ್ನಾಟ</span>
          <span class="nk-logo-en">KARNATA.IN</span>
        </div>
      </a>

      <!-- Desktop Dropdown Menu Links -->
      <div class="nk-nav-links nk-nav-links-desktop">
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
        <div class="nk-nav-dropdown ${isActive('/ask') || isActive('/ai-jyothishya') || isActive('/kannada-typing') || isActive('/scheme-checker') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>🔮 AI & ಡಿಜಿಟಲ್ ಸೇವೆಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/ask" class="nk-drop-item ${isActive('/ask') ? 'active' : ''}">🤖 askKARNATA AI ಸಹಾಯಕ</a>
            <a href="/ai-jyothishya" class="nk-drop-item ${isActive('/ai-jyothishya') ? 'active' : ''}">🔮 AI ಜ್ಯೋತಿಷ್ಯ & ಕುಂಡಲಿ</a>
            <a href="/kannada-typing" class="nk-drop-item ${isActive('/kannada-typing') ? 'active' : ''}">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ & ಅನುವಾದ</a>
            <a href="/scheme-checker" class="nk-drop-item ${isActive('/scheme-checker') ? 'active' : ''}">📋 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು</a>
          </div>
        </div>

        <!-- BUTTON 6: SCHEME GUIDES & ARTICLES -->
        <div class="nk-nav-dropdown ${isActive('/article') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>📚 ಸರ್ಕಾರಿ ಮಾರ್ಗದರ್ಶಿಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/article/gruha-lakshmi-status-check-2026" class="nk-drop-item">🌸 ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಸ್ಟೇಟಸ್ ಚೆಕ್</a>
            <a href="/article/karnataka-bhoomi-rtc-pahani-online" class="nk-drop-item">📜 ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್</a>
            <a href="/article/karnataka-dam-water-storage-analysis" class="nk-drop-item">💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ</a>
            <a href="/article/karnataka-gba-5-corporations-guide" class="nk-drop-item">🏙️ GBA 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು</a>
            <a href="/article/panchatantra-village-budget-grants" class="nk-drop-item">🌾 ಪಂಚತಂತ್ರ ಗ್ರಾಮ ಅನುದಾನ</a>
          </div>
        </div>
      </div>

      <!-- Location Badge -->
      <div style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
        <button class="nk-loc-btn" onclick="if(window.nkOpenLocModal) window.nkOpenLocModal(); else window.location.href='/nanna-sthala';">
          <span class="nk-loc-dot"></span>
          <span id="nk-nav-loc-label">${locLabel}</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Quick Navigation Rail (Clean Horizontal Touch Scroll) -->
  <div class="nk-mobile-rail">
    <a href="/weather" class="nk-mobile-chip ${isActive('/weather') ? 'active' : ''}">🌧️ ಹವಾಮಾನ</a>
    <a href="/gold-rate" class="nk-mobile-chip ${isActive('/gold-rate') ? 'active' : ''}">🪙 ಚಿನ್ನದ ದರ</a>
    <a href="/dam-levels" class="nk-mobile-chip ${isActive('/dam-levels') ? 'active' : ''}">💧 ಡ್ಯಾಂ ಮಟ್ಟ</a>
    <a href="/apmc-prices" class="nk-mobile-chip ${isActive('/apmc-prices') ? 'active' : ''}">🌾 APMC</a>
    <a href="/karnataka-sir-voter-roll/" class="nk-mobile-chip ${isActive('/karnataka-sir-voter-roll') ? 'active' : ''}">🗳️ SIR ವೋಟರ್</a>
    <a href="/cabinet-ministers" class="nk-mobile-chip ${isActive('/cabinet-ministers') ? 'active' : ''}">👥 ಸಚಿವರು</a>
    <a href="/gba" class="nk-mobile-chip ${isActive('/gba') ? 'active' : ''}">🏙️ GBA</a>
    <a href="/ask" class="nk-mobile-chip ${isActive('/ask') ? 'active' : ''}">🤖 askAI</a>
    <a href="/petrol-price" class="nk-mobile-chip ${isActive('/petrol-price') ? 'active' : ''}">⛽ ಇಂಧನ</a>
    <a href="/article/gruha-lakshmi-status-check-2026" class="nk-mobile-chip">🌸 ಗೃಹಲಕ್ಷ್ಮಿ</a>
  </div>
</div>
`;

  function initNavHoverLogic() {
    document.querySelectorAll('.nk-nav-dropdown').forEach(function (dd) {
      var closeTimer;
      dd.addEventListener('mouseenter', function () {
        clearTimeout(closeTimer);
        document.querySelectorAll('.nk-nav-dropdown').forEach(function (other) {
          if (other !== dd) other.classList.remove('open');
        });
        dd.classList.add('open');
      });
      dd.addEventListener('mouseleave', function () {
        closeTimer = setTimeout(function () {
          dd.classList.remove('open');
        }, 300);
      });
    });
  }

  if (document.body) {
    const existing = document.querySelector('.nk-nav');
    if (!existing) {
      document.body.insertAdjacentHTML('afterbegin', navHTML);
      initNavHoverLogic();
    }
  } else {
    document.addEventListener('DOMContentLoaded', function () {
      const existing = document.querySelector('.nk-nav');
      if (!existing) {
        document.body.insertAdjacentHTML('afterbegin', navHTML);
        initNavHoverLogic();
      }
    });
  }
})();
"""

with open(os.path.join(ROOT_DIR, 'nav-component.js'), 'w', encoding='utf-8') as f:
    f.write(nav_code)
with open(os.path.join(NK_DIR, 'nav-component.js'), 'w', encoding='utf-8') as f:
    f.write(nav_code)

print("[OK] Upgraded nav-component.js for Mobile.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPGRADE gold-rate.html MOBILE RESPONSIVENESS
# ══════════════════════════════════════════════════════════════════════════════
gold_path = os.path.join(ROOT_DIR, 'gold-rate.html')
with open(gold_path, 'r', encoding='utf-8') as f:
    gold_html = f.read()

# Add responsive mobile CSS rules into gold-rate.html
mobile_gold_css = """
    /* ════ MOBILE-FIRST RESPONSIVE FIXES ════ */
    @media (max-width: 768px) {
      .gold-container {
        padding: 0 12px 40px !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }
      .mode-tabs {
        display: flex !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none !important;
        gap: 6px !important;
        padding: 4px !important;
        border-radius: 12px !important;
      }
      .mode-tabs::-webkit-scrollbar { display: none; }
      .mode-tab {
        padding: 10px 14px !important;
        font-size: 13px !important;
        white-space: nowrap !important;
        flex: none !important;
      }
      .season-heatmap {
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 6px !important;
      }
      .heat-cell {
        padding: 10px 6px !important;
        font-size: 13px !important;
      }
      .hist-table th, .hist-table td {
        padding: 10px 8px !important;
        font-size: 12.5px !important;
        white-space: nowrap !important;
      }
      .ai-decision-card {
        padding: 18px 14px !important;
        margin: 20px 0 !important;
      }
      .quick-btn {
        padding: 10px 12px !important;
        font-size: 13px !important;
        text-align: left !important;
      }
    }
"""

if '/* ════ MOBILE-FIRST RESPONSIVE FIXES ════ */' not in gold_html:
    gold_html = gold_html.replace('</style>', mobile_gold_css + '\n    </style>')
    with open(gold_path, 'w', encoding='utf-8') as f:
        f.write(gold_html)
    with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
        f.write(gold_html)

print("[OK] Upgraded gold-rate.html mobile styles.")

# ══════════════════════════════════════════════════════════════════════════════
# 3. GLOBAL MOBILE OVERFLOW FIX ACROSS ALL HTML PAGES
# ══════════════════════════════════════════════════════════════════════════════
global_mobile_viewport_fix = """  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />"""

for root, dirs, files in os.walk(ROOT_DIR):
    if any(p in root for p in ['node_modules', '.git', '.gemini', 'namma-karnataka', 'scratch']):
        continue
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8') as hf:
                hc = hf.read()
            
            # Ensure proper responsive viewport tag
            if '<meta name="viewport"' not in hc:
                hc = hc.replace('<head>', '<head>\n' + global_mobile_viewport_fix)
                with open(fp, 'w', encoding='utf-8') as hf:
                    hf.write(hc)

print("SUCCESS_MOBILE_LAYOUT_UPGRADE_COMPLETE")
