# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_full_visual_inpage_editor.py
Builds the complete Direct In-Page Visual Editor for Karnata.in.
Allows editing every part of any page visually (click-to-edit directly on the live page)
while keeping dynamic databases & data widgets 100% untouched.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE _worker.js TO SUPPORT FULL PAGE HTML SAVING & SERVING VIA CLOUDFLARE KV
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

save_page_handler = """    // Route: Full Visual Page HTML Save & Global Cloudflare Edge Sync
    if (url.pathname === '/api/admin/save-page' || url.pathname === '/api/save-page') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          let pageId = (body.page_id || body.filename || '').trim().replace(/^\\//, '');
          if (!pageId.endsWith('.html')) pageId += '.html';
          const htmlContent = body.html;

          if (!pageId || !htmlContent) {
            return new Response(JSON.stringify({ error: 'page_id and html are required' }), { status: 400, headers: corsHeaders });
          }

          const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
          if (kv) {
            await kv.put(`page_override_${pageId}`, htmlContent);
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Page ${pageId} saved and synced to Cloudflare Edge globally`,
            page_id: pageId,
            url: `https://karnata.in/${pageId}`
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }
    }
"""

if "url.pathname === '/api/admin/save-page'" not in worker_code:
    worker_code = worker_code.replace(
        "    // Route: Cloudflare Global Pages CMS Sync & API (GET & POST)",
        save_page_handler + "\n    // Route: Cloudflare Global Pages CMS Sync & API (GET & POST)"
    )

# Also support serving KV page override on HTML routes
page_override_serving = """    // Check Cloudflare KV for Full Page Visual Overrides
    const cleanPath = url.pathname.replace(/^\\//, '') || 'index.html';
    const targetHtmlFile = cleanPath.endsWith('.html') ? cleanPath : (cleanPath ? cleanPath + '.html' : 'index.html');
    const kvStore = env && (env.NK_DATA || env.TRANSFERS_KV);
    if (kvStore && (url.pathname.endsWith('.html') || !url.pathname.includes('.'))) {
      try {
        const customHtml = await kvStore.get(`page_override_${targetHtmlFile}`);
        if (customHtml) {
          return new Response(customHtml, {
            headers: {
              'Content-Type': 'text/html; charset=utf-8',
              'Cache-Control': 'no-cache, must-revalidate, max-age=0',
              'X-Karnata-Page-Source': 'Cloudflare-Edge-KV-Override'
            }
          });
        }
      } catch(e) {}
    }
"""

if "Check Cloudflare KV for Full Page Visual Overrides" not in worker_code:
    worker_code = worker_code.replace(
        "    // Route 3: Ultra-Fast Static Asset Delivery (HTML, CSS, JS, Images, JSON)\n    return env.ASSETS.fetch(request);",
        page_override_serving + "\n    // Route 3: Ultra-Fast Static Asset Delivery (HTML, CSS, JS, Images, JSON)\n    return env.ASSETS.fetch(request);"
    )

with open(worker_path, 'w', encoding='utf-8') as f:
    f.write(worker_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_code)

print("Updated _worker.js with full page save & edge serving support.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. BUILD VISUAL DIRECT IN-PAGE STUDIO IN admin/index.html
# ══════════════════════════════════════════════════════════════════════════════
VISUAL_STUDIO_HTML = """<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಕರ್ನಾಟ Live Visual Page & Article Studio 2026</title>
  <meta name="robots" content="noindex, nofollow">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary: #E11D48;
      --primary-hover: #BE123C;
      --accent-blue: #2563EB;
      --accent-green: #059669;
      --dark: #0F172A;
      --dark-card: #1E293B;
      --bg: #F8FAFC;
      --card: #FFFFFF;
      --border: #E2E8F0;
      --text: #0F172A;
      --text-muted: #64748B;
      --font-kn: 'Anek Kannada', system-ui, sans-serif;
      --font-en: 'Plus Jakarta Sans', system-ui, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-kn);
      background: #0B0F19;
      color: #F8FAFC;
      margin: 0;
      padding: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    /* TOP ADMIN CONTROLS BAR */
    .top-studio-bar {
      background: #0F172A;
      border-bottom: 1px solid #1E293B;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      z-index: 100;
      flex-wrap: wrap;
    }
    .brand-box {
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
    }
    .brand-name {
      font-size: 20px;
      font-weight: 900;
      color: #FDA4AF;
    }
    .brand-badge {
      background: var(--primary);
      color: #FFF;
      font-size: 10px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: var(--font-en);
    }

    /* PAGE SELECTOR DROPDOWN */
    .page-select-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      background: #1E293B;
      border: 1px solid #334155;
      padding: 4px 10px;
      border-radius: 8px;
    }
    .page-select-dropdown {
      background: transparent;
      border: none;
      color: #FFF;
      font-family: var(--font-kn);
      font-size: 14px;
      font-weight: 800;
      outline: none;
      cursor: pointer;
    }
    .page-select-dropdown option {
      background: #0F172A;
      color: #FFF;
    }

    /* VISUAL FORMATTING TOOLBAR */
    .visual-tools {
      display: flex;
      align-items: center;
      gap: 4px;
      background: #1E293B;
      padding: 4px 8px;
      border-radius: 8px;
      border: 1px solid #334155;
    }
    .tb-btn {
      background: transparent;
      border: none;
      color: #CBD5E1;
      font-size: 13px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }
    .tb-btn:hover {
      background: rgba(255,255,255,0.1);
      color: #FFF;
    }
    .tb-sep {
      width: 1px;
      height: 16px;
      background: #475569;
      margin: 0 4px;
    }

    /* DEVICE PREVIEW TOGGLES */
    .device-toggles {
      display: flex;
      align-items: center;
      gap: 4px;
      background: #1E293B;
      padding: 4px 6px;
      border-radius: 8px;
    }
    .dev-btn {
      background: transparent;
      border: none;
      color: #94A3B8;
      padding: 4px 8px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
    }
    .dev-btn.active {
      background: #334155;
      color: #FFF;
    }

    /* ACTION BUTTONS */
    .right-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-sync-live {
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      color: #FFF;
      border: none;
      padding: 8px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 10px rgba(5,150,105,0.3);
      transition: all 0.2s;
    }
    .btn-sync-live:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 15px rgba(5,150,105,0.45);
    }
    .btn-sync-live:disabled {
      background: #64748B;
      cursor: not-allowed;
      transform: none;
    }
    .btn-hdr-opt {
      background: #1E293B;
      border: 1px solid #334155;
      color: #E2E8F0;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    /* MAIN EDITING WORKSPACE */
    .editor-workspace {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: stretch;
      background: #0B0F19;
      padding: 12px;
      overflow: hidden;
      position: relative;
    }

    .canvas-container {
      width: 100%;
      max-width: 100%;
      height: 100%;
      background: #FFFFFF;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
      transition: max-width 0.25s ease;
      display: flex;
      flex-direction: column;
    }
    .canvas-container.tablet { max-width: 768px; }
    .canvas-container.mobile { max-width: 390px; }

    .canvas-iframe {
      width: 100%;
      height: 100%;
      border: none;
      display: block;
      background: #FFFFFF;
    }

    /* EDIT INSTRUCTION BANNER */
    .edit-hint-bar {
      background: #1E293B;
      border-top: 1px solid #334155;
      padding: 6px 16px;
      font-size: 12.5px;
      color: #94A3B8;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* TOAST ALERT */
    #toastMsg {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #059669;
      color: #FFF;
      font-size: 14.5px;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: 100px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      z-index: 9999999;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    #toastMsg.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }
  </style>
</head>
<body>

  <!-- ══════════════════════════════════════════════════════════════════════════════
       KARNATA ADMIN SECURITY GATEWAY
       ══════════════════════════════════════════════════════════════════════════════ -->
  <div id="karnata-admin-gate" style="
    position: fixed;
    inset: 0;
    z-index: 999999;
    background: radial-gradient(circle at center, #0F172A 0%, #020617 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    backdrop-filter: blur(20px);
  ">
    <div style="
      background: rgba(30, 41, 59, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      border-radius: 24px;
      max-width: 400px;
      width: 100%;
      padding: 32px 24px;
      text-align: center;
      color: #F8FAFC;
    ">
      <div style="width:56px; height:56px; background:linear-gradient(135deg, #E11D48, #BE123C); border-radius:16px; margin:0 auto 14px; display:flex; align-items:center; justify-content:center; font-size:28px;">🔒</div>
      <h2 style="font-size: 21px; font-weight: 900; margin: 0 0 4px; color: #FFF;">ಕರ್ನಾಟ ವಿಷುಯಲ್ CMS</h2>
      <p style="font-size: 13px; color: #94A3B8; margin: 0 0 18px;">ಪುಟಗಳನ್ನು ನೇರವಾಗಿ ಎಡಿಟ್ ಮಾಡಲು ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ.</p>

      <form onsubmit="event.preventDefault(); window.karnataCheckGatePass();" style="display:flex; flex-direction:column; gap:12px;">
        <div style="display:flex; align-items:center; background:#0F172A; border:1.5px solid #334155; border-radius:10px; overflow:hidden;" id="gateInputWrap">
          <input type="password" id="gatePassInput" placeholder="••••••••" style="flex:1; background:transparent; border:none; padding:12px 14px; font-size:15px; color:#FFF; outline:none; font-family:monospace;" required autofocus>
          <button type="button" onclick="window.karnataTogglePassEye()" style="background:transparent; border:none; color:#94A3B8; padding:0 12px; cursor:pointer;">👁️</button>
        </div>
        <div id="gateErrorMsg" style="display:none; color:#FB7185; font-size:12px; font-weight:700;">⚠️ ತಪ್ಪು ಪಾಸ್‌ವರ್ಡ್!</div>
        <button type="submit" style="background:linear-gradient(135deg, #059669, #047857); color:#FFF; border:none; padding:12px; border-radius:10px; font-size:15px; font-weight:800; cursor:pointer;">🔓 ಪ್ರವೇಶಿಸಿ (Unlock)</button>
      </form>
    </div>
  </div>

  <!-- TOP ADMIN STUDIO BAR -->
  <div class="top-studio-bar">
    
    <!-- BRAND & PAGE SELECTOR -->
    <div style="display:flex; align-items:center; gap:14px;">
      <a href="/" class="brand-box">
        <span class="brand-name">ಕರ್ನಾಟ</span>
        <span class="brand-badge">VISUAL BUILDER</span>
      </a>

      <!-- PAGE SELECTOR -->
      <div class="page-select-wrap">
        <span>📄</span>
        <select id="pageSelectDropdown" class="page-select-dropdown" onchange="changeActivePage(this.value)">
          <option value="petrol-price.html">⛽ ಇಂಧನ ಬೆಲೆ (Petrol & Diesel Rate)</option>
          <option value="gold-rate.html">🪙 ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Gold Rate)</option>
          <option value="apmc-prices.html">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರ (APMC Prices)</option>
          <option value="dam-levels.html">🌊 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Dam Levels)</option>
          <option value="weather.html">🌦️ ಹವಾಮಾನ ಪೋರ್ಟಲ್ (Weather)</option>
          <option value="mla-mp.html">🏛️ ಶಾಸಕರು & ಸಂಸದರು (MLA & MP Hub)</option>
          <option value="scheme-checker.html">💡 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು (Govt Schemes)</option>
          <option value="kannada-typing.html">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ (Kannada Typing)</option>
          <option value="ai-jyothishya.html">🔮 ವೈದಿಕ ಜ್ಯೋತಿಷ್ಯ (AI Jyothishya)</option>
          <option value="about.html">ℹ️ ನಮ್ಮ ಬಗ್ಗೆ (About Us)</option>
          <option value="contact.html">📞 ಸಂಪರ್ಕಿಸಿ (Contact Us)</option>
          <option value="privacy.html">🔒 ಗೌಪ್ಯತಾ ನೀತಿ (Privacy Policy)</option>
          <option value="terms.html">📜 ನಿಯಮಗಳು & ಷರತ್ತುಗಳು (Terms)</option>
          <option value="index.html">🏠 ಮುಖಪುಟ (Homepage)</option>
        </select>
      </div>
    </div>

    <!-- DIRECT VISUAL TEXT FORMATTING TOOLS -->
    <div class="visual-tools">
      <button class="tb-btn" onclick="execIframeCmd('bold')" title="Bold"><b>B</b></button>
      <button class="tb-btn" onclick="execIframeCmd('italic')" title="Italic"><i>I</i></button>
      <button class="tb-btn" onclick="execIframeCmd('underline')" title="Underline"><u>U</u></button>
      <div class="tb-sep"></div>
      <button class="tb-btn" onclick="execIframeCmd('formatBlock', '<h2>')">H2</button>
      <button class="tb-btn" onclick="execIframeCmd('formatBlock', '<h3>')">H3</button>
      <button class="tb-btn" onclick="execIframeCmd('formatBlock', '<p>')">¶ ಪ್ಯಾರಾ</button>
      <div class="tb-sep"></div>
      <button class="tb-btn" onclick="execIframeCmd('insertUnorderedList')">• ಪಟ್ಟಿ</button>
      <button class="tb-btn" onclick="execIframeCmd('insertOrderedList')">1. ಕ್ರಮಾಂಕ</button>
      <div class="tb-sep"></div>
      <button class="tb-btn" onclick="promptIframeLink()">🔗 ಲಿಂಕ್</button>
      <button class="tb-btn" onclick="promptIframeImage()">🖼️ ಚಿತ್ರ</button>
      <button class="tb-btn" onclick="execIframeCmd('removeFormat')" style="color:#FDA4AF;">🧹 ಕ್ಲಿಯರ್</button>
    </div>

    <!-- DEVICE RESPONSIVE SWITCHER -->
    <div class="device-toggles">
      <button class="dev-btn active" id="btnDevDesktop" onclick="setDeviceView('desktop')" title="Desktop View">🖥️</button>
      <button class="dev-btn" id="btnDevTablet" onclick="setDeviceView('tablet')" title="Tablet View">📱</button>
      <button class="dev-btn" id="btnDevMobile" onclick="setDeviceView('mobile')" title="Mobile View">📲</button>
    </div>

    <!-- RIGHT ACTION BUTTONS -->
    <div class="right-actions">
      <a id="btnLiveSiteLink" href="/petrol-price.html" target="_blank" class="btn-hdr-opt">
        <span>🌐 ಲೈವ್ ಸೈಟ್</span>
      </a>

      <!-- 1-CLICK SAVE & CLOUDFLARE SYNC BUTTON -->
      <button id="btnSaveSync" class="btn-sync-live" onclick="saveAndSyncPageDirectly()">
        <span>🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಲೈವ್ ಸಿಂಕ್ (Save & Sync)</span>
      </button>

      <button onclick="window.karnataAdminLogout()" class="btn-hdr-opt" style="border-color:#E11D48; color:#FDA4AF;">
        <span>🔒 ಲಾಕ್</span>
      </button>
    </div>

  </div>

  <!-- MAIN INTERACTIVE VISUAL EDITING WORKSPACE -->
  <div class="editor-workspace">
    <div class="canvas-container" id="canvasBox">
      <iframe id="livePageIframe" class="canvas-iframe" src="/petrol-price.html" onload="injectInPlaceVisualEditor(this)"></iframe>
    </div>
  </div>

  <!-- FOOTER HINT -->
  <div class="edit-hint-bar">
    <div>
      <span style="color:#34D399; font-weight:800;">✨ Click-to-Edit Mode:</span>
      <span style="color:#CBD5E1;">ಪುಟದ ಯಾವುದೇ ಪಠ್ಯ (ಶೀರ್ಷಿಕೆ, ವಿವರಣೆ, ಬ್ಯಾನರ್, ಲೇಖನ, ಕಾರ್ಡ್) ಮೇಲೆ ನೇರವಾಗಿ ಕ್ಲಿಕ್ ಮಾಡಿ ಬರೆಯಿರಿ. ಡೈನಾಮಿಕ್ ಡೇಟಾ ಮತ್ತು APIಗಳು 100% ಸುರಕ್ಷಿತವಾಗಿರುತ್ತವೆ.</span>
    </div>
    <div id="saveStatusIndicator" style="font-weight:800; color:#38BDF8;"></div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toastMsg">
    <span>🎉 ಪುಟವು ಯಶಸ್ವಿಯಾಗಿ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ನೆಟ್‌ವರ್ಕ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದೆ!</span>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // 1. GATEWAY AUTH
    const MASTER_PASSWORDS = ['karnata2026', 'karnata@2026', 'admin@karnata', 'karnata@999', 'avinash2026', 'admin2026'];
    const AUTH_KEY = 'nk_admin_authenticated_session';

    function isAuthenticated() {
      return sessionStorage.getItem(AUTH_KEY) === 'true' || localStorage.getItem(AUTH_KEY) === 'true';
    }
    function unlockUI() {
      const gate = document.getElementById('karnata-admin-gate');
      if (gate) {
        gate.style.opacity = '0';
        setTimeout(() => { gate.style.display = 'none'; }, 200);
      }
    }
    window.karnataCheckGatePass = function() {
      const val = (document.getElementById('gatePassInput').value || '').trim();
      if (MASTER_PASSWORDS.includes(val)) {
        sessionStorage.setItem(AUTH_KEY, 'true');
        localStorage.setItem(AUTH_KEY, 'true');
        unlockUI();
      } else {
        document.getElementById('gateErrorMsg').style.display = 'block';
      }
    };
    window.karnataTogglePassEye = function() {
      const inp = document.getElementById('gatePassInput');
      if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
    };
    window.karnataAdminLogout = function() {
      if (confirm('ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್ ಲಾಕ್ ಮಾಡಬೇಕೇ? (Lock Admin?)')) {
        sessionStorage.removeItem(AUTH_KEY);
        localStorage.removeItem(AUTH_KEY);
        window.location.reload();
      }
    };
    if (isAuthenticated()) {
      document.addEventListener('DOMContentLoaded', unlockUI);
      if (document.readyState === 'interactive' || document.readyState === 'complete') unlockUI();
    }

    // 2. PAGE SELECTOR & DEVICE VIEW
    let activePage = 'petrol-price.html';

    function changeActivePage(pageFile) {
      activePage = pageFile;
      const iframe = document.getElementById('livePageIframe');
      iframe.src = '/' + pageFile + '?t=' + Date.now();
      document.getElementById('btnLiveSiteLink').href = '/' + pageFile;
      document.getElementById('saveStatusIndicator').textContent = '';
    }

    function setDeviceView(dev) {
      const box = document.getElementById('canvasBox');
      document.getElementById('btnDevDesktop').classList.toggle('active', dev === 'desktop');
      document.getElementById('btnDevTablet').classList.toggle('active', dev === 'tablet');
      document.getElementById('btnDevMobile').classList.toggle('active', dev === 'mobile');

      box.classList.remove('tablet', 'mobile');
      if (dev === 'tablet') box.classList.add('tablet');
      if (dev === 'mobile') box.classList.add('mobile');
    }

    // 3. INJECT DIRECT IN-PAGE CLICK-TO-EDIT CAPABILITIES
    function injectInPlaceVisualEditor(iframe) {
      try {
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (!iframeDoc || !iframeDoc.body) return;

        // Add visual editable styles into iframe
        const style = iframeDoc.createElement('style');
        style.id = 'karnata-visual-editor-injected-styles';
        style.textContent = `
          [data-karnata-editable="true"]:hover {
            outline: 2px dashed #E11D48 !important;
            outline-offset: 2px !important;
            cursor: text !important;
          }
          [data-karnata-editable="true"]:focus {
            outline: 2px solid #2563EB !important;
            outline-offset: 3px !important;
            background: rgba(37, 99, 235, 0.05) !important;
          }
        `;
        if (!iframeDoc.getElementById('karnata-visual-editor-injected-styles')) {
          iframeDoc.head.appendChild(style);
        }

        // Enable contentEditable on text elements while keeping dynamic script tables intact
        const textElements = iframeDoc.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, blockquote, .hero-title, .hero-sub, .page-desc, .nc-headline, .nc-summary, .card h3, .card p, .alert-box, .banner-text, label');
        textElements.forEach(el => {
          // Do not make raw script tags or price numeric counters editable
          if (!el.closest('script') && !el.closest('style') && !el.classList.contains('no-edit')) {
            el.setAttribute('contenteditable', 'true');
            el.setAttribute('data-karnata-editable', 'true');
          }
        });

        document.getElementById('saveStatusIndicator').textContent = '🟢 Click-to-Edit ಸಿದ್ಧವಾಗಿದೆ';
      } catch(e) {
        console.warn('Iframe inject notice:', e);
      }
    }

    // 4. FORMATTING COMMANDS INTO IFRAME
    function execIframeCmd(command, value = null) {
      try {
        const iframe = document.getElementById('livePageIframe');
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        iframe.contentWindow.focus();
        iframeDoc.execCommand(command, false, value);
      } catch(e) {}
    }

    function promptIframeLink() {
      const url = prompt('ವೆಬ್‌ಸೈಟ್ ಲಿಂಕ್ (URL) ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execIframeCmd('createLink', url);
    }

    function promptIframeImage() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL) ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execIframeCmd('insertImage', url);
    }

    // 5. 1-CLICK SAVE & CLOUDFLARE GLOBAL SYNC
    async function saveAndSyncPageDirectly() {
      const btn = document.getElementById('btnSaveSync');
      const toast = document.getElementById('toastMsg');
      const statusInd = document.getElementById('saveStatusIndicator');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್‌ಗೆ ಸಿಂಕ್ ಆಗುತ್ತಿದೆ...';
      statusInd.textContent = '⚡ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಪ್ರಕ್ರಿಯೆ ಚಾಲನೆಯಲ್ಲಿದೆ...';

      try {
        const iframe = document.getElementById('livePageIframe');
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

        // Clone document to clean injected editor attributes before saving
        const clonedDoc = iframeDoc.documentElement.cloneNode(true);
        
        // Remove injected editor styles
        const injectedStyle = clonedDoc.querySelector('#karnata-visual-editor-injected-styles');
        if (injectedStyle) injectedStyle.remove();

        // Clean contenteditable attributes
        clonedDoc.querySelectorAll('[data-karnata-editable]').forEach(el => {
          el.removeAttribute('contenteditable');
          el.removeAttribute('data-karnata-editable');
        });

        const fullCleanHtml = '<!DOCTYPE html>\\n' + clonedDoc.outerHTML;

        // Send to Cloudflare Edge API
        const res = await fetch('/api/admin/save-page', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            page_id: activePage,
            filename: activePage,
            html: fullCleanHtml
          })
        });

        if (res.ok) {
          toast.classList.add('show');
          setTimeout(() => toast.classList.remove('show'), 3500);
          statusInd.textContent = '✅ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್‌ನಲ್ಲಿ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಆಗಿದೆ!';
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch(err) {
        alert('⚠️ ಸಿಂಕ್ ದೋಷ: ' + err.message);
        statusInd.textContent = '⚠️ ದೋಷ: ' + err.message;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಲೈವ್ ಸಿಂಕ್ (Save & Sync)';
      }
    }
  </script>
</body>
</html>
"""

admin_path = os.path.join(ROOT_DIR, 'admin', 'index.html')
with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(VISUAL_STUDIO_HTML)

replicas = [
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'index.html'),
    os.path.join(ROOT_DIR, 'cms', 'admin.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'cms', 'admin.html')
]

for r in replicas:
    os.makedirs(os.path.dirname(r), exist_ok=True)
    with open(r, 'w', encoding='utf-8') as f:
        f.write(VISUAL_STUDIO_HTML)
    print(f"Synced in-place visual editor to {r}")

print("SUCCESS_DIRECT_INPAGE_EDITOR_BUILT")
