# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_full_studio_ui.py
Generates the world-class, full-featured Visual Page & Article Studio in admin/index.html
with complete Page SEO, AI Geo, Hero, Header, and Full Article controls.
"""

import os
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STUDIO_HTML = """<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಕರ್ನಾಟ Full Pages & Articles Studio 2026 | Cloudflare Edge Sync</title>
  <meta name="robots" content="noindex, nofollow">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary: #E11D48;
      --primary-hover: #BE123C;
      --primary-light: #FFE4E6;
      --accent-blue: #2563EB;
      --accent-green: #059669;
      --accent-amber: #D97706;
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
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    /* TOP HEADER */
    .top-header {
      background: #0F172A;
      color: #FFF;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .brand-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #FFF;
    }
    .brand-name {
      font-size: 22px;
      font-weight: 900;
      color: #FDA4AF;
      letter-spacing: -0.5px;
    }
    .brand-badge {
      background: var(--primary);
      color: #FFF;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      font-family: var(--font-en);
      letter-spacing: 0.5px;
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-hdr {
      background: rgba(255,255,255,0.1);
      color: #E2E8F0;
      border: 1px solid rgba(255,255,255,0.15);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-hdr:hover { background: rgba(255,255,255,0.2); color: #FFF; }
    .btn-lock {
      background: rgba(225, 29, 72, 0.2);
      border-color: #E11D48;
      color: #FDA4AF;
    }
    .btn-lock:hover { background: #E11D48; color: #FFF; }

    /* NAVIGATION TABS */
    .nav-tabs {
      background: #FFFFFF;
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      display: flex;
      gap: 20px;
      overflow-x: auto;
    }
    .tab-btn {
      background: none;
      border: none;
      padding: 15px 8px;
      font-size: 15px;
      font-weight: 800;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      position: relative;
      font-family: var(--font-kn);
      transition: color 0.2s;
      white-space: nowrap;
    }
    .tab-btn:hover { color: var(--primary); }
    .tab-btn.active {
      color: var(--primary);
    }
    .tab-btn.active::after {
      content: '';
      position: absolute;
      bottom: -1px;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--primary);
      border-radius: 3px 3px 0 0;
    }

    /* MAIN CONTAINER */
    .main-container {
      max-width: 1360px;
      margin: 20px auto 80px;
      padding: 0 16px;
    }

    /* SPLIT-SCREEN LAYOUT FOR FULL PAGES CMS */
    .studio-layout {
      display: grid;
      grid-template-columns: 560px 1fr;
      gap: 24px;
      align-items: start;
    }
    @media (max-width: 1100px) {
      .studio-layout { grid-template-columns: 1fr; }
    }

    /* CARDS */
    .card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 4px 20px -2px rgba(0,0,0,0.03);
      margin-bottom: 20px;
    }
    .card-title {
      font-size: 16.5px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* PAGE SELECTOR CARDS */
    .page-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(125px, 1fr));
      gap: 8px;
      margin-bottom: 16px;
    }
    .page-item-card {
      background: #F8FAFC;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      padding: 10px 8px;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s;
    }
    .page-item-card:hover {
      background: #FFF1F2;
      border-color: var(--primary);
      transform: translateY(-2px);
    }
    .page-item-card.active {
      background: #FFF1F2;
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary);
    }
    .page-icon { font-size: 22px; margin-bottom: 2px; display: block; }
    .page-label { font-size: 12.5px; font-weight: 800; color: #1E293B; line-height: 1.25; }

    /* ACCORDION / SECTION COLLAPSE */
    .section-box {
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 14px;
      overflow: hidden;
      background: #FFFFFF;
    }
    .section-hdr {
      background: #F8FAFC;
      padding: 12px 16px;
      font-size: 14.5px;
      font-weight: 800;
      color: #1E293B;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid transparent;
      user-select: none;
    }
    .section-hdr:hover { background: #F1F5F9; }
    .section-hdr.open {
      border-bottom-color: var(--border);
      background: #EFF6FF;
      color: #1E40AF;
    }
    .section-content {
      padding: 16px;
    }

    /* FORM ELEMENTS */
    .form-group {
      margin-bottom: 14px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 800;
      color: #334155;
      margin-bottom: 5px;
    }
    .form-label span {
      font-size: 11px;
      font-weight: 500;
      color: #64748B;
      margin-left: 4px;
    }
    .input-text, .select-box, .textarea-box {
      width: 100%;
      border: 1.5px solid #CBD5E1;
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 14px;
      color: #0F172A;
      font-family: var(--font-kn);
      outline: none;
      transition: all 0.2s;
      background: #F8FAFC;
    }
    .input-text:focus, .select-box:focus, .textarea-box:focus {
      border-color: var(--primary);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.1);
    }

    /* VISUAL RICH TEXT CANVAS */
    .editor-box {
      border: 1.5px solid #CBD5E1;
      border-radius: 8px;
      overflow: hidden;
      background: #FFFFFF;
    }
    .editor-toolbar {
      background: #F1F5F9;
      border-bottom: 1px solid #E2E8F0;
      padding: 6px 8px;
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }
    .tb-btn {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 11.5px;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
    }
    .tb-btn:hover { background: #E2E8F0; }
    .visual-canvas {
      min-height: 160px;
      max-height: 320px;
      overflow-y: auto;
      padding: 12px;
      font-size: 14.5px;
      line-height: 1.7;
      color: #1E293B;
      outline: none;
    }

    /* CLOUDFLARE GLOBAL SYNC BUTTON */
    .btn-sync-cloudflare {
      background: linear-gradient(135deg, #E11D48 0%, #BE123C 100%);
      color: #FFFFFF;
      border: none;
      width: 100%;
      padding: 14px 20px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(225,29,72,0.35);
      transition: all 0.2s;
    }
    .btn-sync-cloudflare:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(225,29,72,0.45);
    }
    .btn-sync-cloudflare:disabled {
      background: #94A3B8;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
    }

    /* IFRAME LIVE PREVIEW */
    .preview-box {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05);
      position: sticky;
      top: 76px;
    }
    .preview-header {
      background: #0F172A;
      color: #CBD5E1;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      font-weight: 700;
    }
    .preview-iframe {
      width: 100%;
      height: 720px;
      border: none;
      display: block;
      background: #F8FAFC;
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
      <h2 style="font-size: 21px; font-weight: 900; margin: 0 0 4px; color: #FFF;">ಕರ್ನಾಟ CMS ಅಡ್ಮಿನ್</h2>
      <p style="font-size: 13px; color: #94A3B8; margin: 0 0 18px;">ಪುಟಗಳನ್ನು ಸಂಪಾದಿಸಲು ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ.</p>

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

  <!-- TOP HEADER -->
  <header class="top-header">
    <a href="/" class="brand-logo">
      <span class="brand-name">ಕರ್ನಾಟ</span>
      <span class="brand-badge">PAGES & ARTICLE STUDIO</span>
    </a>
    <div class="header-actions">
      <a href="/" target="_blank" class="btn-hdr">🌐 ಸೈಟ್ ವೀಕ್ಷಿಸಿ</a>
      <a href="/admin-transfers.html" class="btn-hdr">📑 ವರ್ಗಾವಣೆ ಅಡ್ಮಿನ್</a>
      <button onclick="window.karnataAdminLogout()" class="btn-hdr btn-lock">🔒 ಲಾಕ್</button>
    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <nav class="nav-tabs">
    <button class="tab-btn active" id="tabBtnPages" onclick="switchMainTab('pages')">
      <span>📄 ಪುಟಗಳ ಸಂಪೂರ್ಣ CMS (Full Pages Studio)</span>
    </button>
    <button class="tab-btn" id="tabBtnArticles" onclick="switchMainTab('articles')">
      <span>✍️ ಹೊಸ ಲೇಖನ ಪ್ರಕಟಿಸಿ (New Article)</span>
    </button>
    <button class="tab-btn" id="tabBtnManageArt" onclick="switchMainTab('manage-articles')">
      <span>📚 ಪ್ರಕಟಿತ ಲೇಖನಗಳು (<span id="pubCount">0</span>)</span>
    </button>
  </nav>

  <!-- MAIN BODY -->
  <main class="main-container">

    <!-- ══════════════════════════════════════════════════════════════════════════
         TAB 1: FULL PAGES VISUAL CMS (SEO, HERO, AI GEO, CONTENT, HEADER)
         ══════════════════════════════════════════════════════════════════════════ -->
    <div id="sectionPages">
      
      <!-- 1. PAGE SELECTOR GRID -->
      <div class="card" style="padding:16px;">
        <h3 class="card-title" style="margin-bottom:12px;">
          <span>👇 ಎಡಿಟ್ ಮಾಡಲು ಪುಟವನ್ನು ಆರಿಸಿ (Select Page to Edit Full):</span>
          <span style="font-size:12px; color:#059669; font-weight:700;">🟢 Cloudflare Edge Ready</span>
        </h3>
        
        <div class="page-grid" id="pageSelectorGrid">
          <div class="page-item-card active" onclick="selectPageForEdit('petrol-price.html', this)">
            <span class="page-icon">⛽</span>
            <div class="page-label">ಇಂಧನ ಬೆಲೆ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('gold-rate.html', this)">
            <span class="page-icon">🪙</span>
            <div class="page-label">ಚಿನ್ನ & ಬೆಳ್ಳಿ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('apmc-prices.html', this)">
            <span class="page-icon">🌾</span>
            <div class="page-label">APMC ದರ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('dam-levels.html', this)">
            <span class="page-icon">🌊</span>
            <div class="page-label">ಜಲಾಶಯಗಳು</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('weather.html', this)">
            <span class="page-icon">🌦️</span>
            <div class="page-label">ಹವಾಮಾನ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('mla-mp.html', this)">
            <span class="page-icon">🏛️</span>
            <div class="page-label">ಶಾಸಕರು & MP</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('scheme-checker.html', this)">
            <span class="page-icon">💡</span>
            <div class="page-label">ಯೋಜನೆಗಳು</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('kannada-typing.html', this)">
            <span class="page-icon">⌨️</span>
            <div class="page-label">ಕನ್ನಡ ಟೈಪಿಂಗ್</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('ai-jyothishya.html', this)">
            <span class="page-icon">🔮</span>
            <div class="page-label">ಜ್ಯೋತಿಷ್ಯ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('about.html', this)">
            <span class="page-icon">ℹ️</span>
            <div class="page-label">ನಮ್ಮ ಬಗ್ಗೆ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('contact.html', this)">
            <span class="page-icon">📞</span>
            <div class="page-label">ಸಂಪರ್ಕಿಸಿ</div>
          </div>
          <div class="page-item-card" onclick="selectPageForEdit('privacy.html', this)">
            <span class="page-icon">🔒</span>
            <div class="page-label">ಗೌಪ್ಯತಾ ನೀತಿ</div>
          </div>
        </div>
      </div>

      <!-- 2. STUDIO SPLIT-SCREEN LAYOUT -->
      <div class="studio-layout">
        
        <!-- LEFT: VISUAL FULL PAGE EDITORS (ACCORDIONS) -->
        <div>
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <strong style="font-size:16px; color:#0F172A;">⚙️ <span id="currentEditingPageName">ಇಂಧನ ಬೆಲೆ (petrol-price.html)</span></strong>
            <span style="font-size:11px; background:#D1FAE5; color:#065F46; font-weight:800; padding:2px 8px; border-radius:6px;">100% Visual Mode</span>
          </div>

          <form onsubmit="event.preventDefault(); saveAndSyncPageToCloudflare();">
            
            <!-- SECTION 1: HERO & BANNER -->
            <div class="section-box">
              <div class="section-hdr open" onclick="toggleSection(this)">
                <span>🎯 1. ಹೀರೋ ವಿಭಾಗ & ಬ್ಯಾನರ್ (Hero Section & Banner)</span>
                <span>▼</span>
              </div>
              <div class="section-content">
                <div class="form-group">
                  <label class="form-label">ಹೀರೋ ಮುಖ್ಯ ಶೀರ್ಷಿಕೆ <span>(Hero Headline) *</span></label>
                  <input type="text" id="heroTitleInput" class="input-text" placeholder="ಪುಟದ ಮುಖ್ಯ ಹೀರೋ ಶೀರ್ಷಿಕೆ...">
                </div>
                <div class="form-group">
                  <label class="form-label">ಹೀರೋ ಉಪಶೀರ್ಷಿಕೆ / ಪಂಚ್‌ಲೈನ್ <span>(Hero Subtitle)</span></label>
                  <textarea id="heroSubtitleInput" class="textarea-box" rows="2" placeholder="ವಿವರಣಾತ್ಮಕ ಉಪಶೀರ್ಷಿಕೆ..."></textarea>
                </div>
                <div class="form-group">
                  <label class="form-label">ಲೈವ್ ಬ್ಯಾಡ್ಜ್ ಪಠ್ಯ <span>(Live Badge Text)</span></label>
                  <input type="text" id="heroBadgeInput" class="input-text" placeholder="ಉದಾ: ⚡ ನೈಜ ಸಮಯ ನವೀಕರಣ">
                </div>
                <div class="form-group">
                  <label class="form-label">ವಿಶೇಷ ಸೂಚನೆ / ಅಲರ್ಟ್ ಬ್ಯಾನರ್ <span>(Announcement Banner)</span></label>
                  <input type="text" id="heroAlertInput" class="input-text" placeholder="ಉದಾ: 📢 ಇಂದಿನ ದರಗಳು ನವೀಕರಣಗೊಂಡಿವೆ...">
                </div>
              </div>
            </div>

            <!-- SECTION 2: AI GEO & DISTRICT INTELLIGENCE -->
            <div class="section-box">
              <div class="section-hdr" onclick="toggleSection(this)">
                <span>📍 2. AI ಜಿಯೋ & ಜಿಲ್ಲಾ ಇಂಟೆಲಿಜೆನ್ಸ್ (AI Geo & District Focus)</span>
                <span>▼</span>
              </div>
              <div class="section-content" style="display:none;">
                <div class="form-group">
                  <label class="form-label">ಡೀಫಾಲ್ಟ್ ಆದ್ಯತೆಯ ಜಿಲ್ಲೆ <span>(Default District Focus)</span></label>
                  <select id="geoDistrictInput" class="select-box">
                    <option value="ಬೆಂಗಳೂರು ನಗರ">ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban)</option>
                    <option value="ಮೈಸೂರು">ಮೈಸೂರು (Mysuru)</option>
                    <option value="ಬೆಳಗಾವಿ">ಬೆಳಗಾವಿ (Belagavi)</option>
                    <option value="ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ">ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubballi-Dharwad)</option>
                    <option value="ದಕ್ಷಿಣ ಕನ್ನಡ">ದಕ್ಷಿಣ ಕನ್ನಡ (Mangaluru / DK)</option>
                    <option value="ಕಲಬುರಗಿ">ಕಲಬುರಗಿ (Kalaburagi)</option>
                    <option value="ಶಿವಮೊಗ್ಗ">ಶಿವಮೊಗ್ಗ (Shivamogga)</option>
                    <option value="ತುಮಕೂರು">ತುಮಕೂರು (Tumakuru)</option>
                    <option value="ರಾಜ್ಯಾದ್ಯಂತ">ರಾಜ್ಯಾದ್ಯಂತ (Statewide All 31 Districts)</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label">ಸ್ಥಳೀಯ ಶುಭಾಶಯ ಸಂದೇಶ <span>(Localized Greeting)</span></label>
                  <input type="text" id="geoGreetingInput" class="input-text" placeholder="ಉದಾ: ನಮಸ್ಕಾರ, ನಿಮ್ಮ ಪ್ರದೇಶದ ಇಂದಿನ ಮಾಹಿತಿ ಇಲ್ಲಿದೆ.">
                </div>
                <div class="form-group">
                  <label class="form-label">ಗ್ರಾಹಕ / ರೈತ ಮಾರ್ಗದರ್ಶಿ ಸಲಹೆ <span>(District Advisory)</span></label>
                  <textarea id="geoAdvisoryInput" class="textarea-box" rows="2" placeholder="ಸ್ಥಳೀಯ ನಾಗರಿಕರಿಗೆ ಉಪಯುಕ್ತ ಮಾಹಿತಿ ಅಥವಾ ಸಲಹೆ..."></textarea>
                </div>
              </div>
            </div>

            <!-- SECTION 3: FULL VISUAL ARTICLE & BODY CONTENT -->
            <div class="section-box">
              <div class="section-hdr" onclick="toggleSection(this)">
                <span>📝 3. ಸಂಪೂರ್ಣ ಲೇಖನ & ಮಾಹಿತಿ ಮಾರ್ಗದರ್ಶಿ (Full Article Content)</span>
                <span>▼</span>
              </div>
              <div class="section-content" style="display:none;">
                <div class="form-group">
                  <label class="form-label">ವಿಷುಯಲ್ ಕಂಟೆಂಟ್ ಎಡಿಟರ್ <span>(WYSIWYG Rich Text - No HTML Code)</span></label>
                  
                  <div class="editor-box">
                    <div class="editor-toolbar">
                      <button type="button" class="tb-btn" onclick="execCmdPage('bold')"><b>B</b></button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('italic')"><i>I</i></button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('formatBlock', '<h2>')">📌 H2</button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('formatBlock', '<h3>')">🔹 H3</button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('insertUnorderedList')">• ಪಟ್ಟಿ</button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('insertOrderedList')">1. ಕ್ರಮಾಂಕ</button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('formatBlock', '<blockquote>')">❝ ಕೋಟ್</button>
                      <button type="button" class="tb-btn" onclick="promptInsertLinkPage()">🔗 ಲಿಂಕ್</button>
                      <button type="button" class="tb-btn" onclick="promptInsertImgPage()">🖼️ ಚಿತ್ರ</button>
                      <button type="button" class="tb-btn" onclick="execCmdPage('removeFormat')" style="color:#E11D48;">🧹 ಕ್ಲಿಯರ್</button>
                    </div>
                    <div id="pageArticleCanvas" class="visual-canvas" contenteditable="true" data-placeholder="ಇಲ್ಲಿ ಪುಟದ ಸಂಪೂರ್ಣ ಲೇಖನ ಮತ್ತು ಮಾರ್ಗದರ್ಶಿ ವಿವರವನ್ನು ಬರೆಯಿರಿ..."></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- SECTION 4: SEO & SOCIAL META -->
            <div class="section-box">
              <div class="section-hdr" onclick="toggleSection(this)">
                <span>🔍 4. ಗೂಗಲ್ SEO & ಸೋಶಿಯಲ್ ಕಾರ್ಡ್ (Page SEO & Social Meta)</span>
                <span>▼</span>
              </div>
              <div class="section-content" style="display:none;">
                <div class="form-group">
                  <label class="form-label">ಗೂಗಲ್ ಸರ್ಚ್ ಶೀರ್ಷಿಕೆ <span>(Google Meta Title) *</span></label>
                  <input type="text" id="seoTitleInput" class="input-text" placeholder="ಉದಾ: ಇಂದಿನ ಪೆಟ್ರೋಲ್ ಡೀಸೆಲ್ ಬೆಲೆ ಕರ್ನಾಟಕ | Karnata.in">
                </div>
                <div class="form-group">
                  <label class="form-label">ಗೂಗಲ್ ಸರ್ಚ್ ವಿವರಣೆ <span>(Meta Description) *</span></label>
                  <textarea id="seoDescInput" class="textarea-box" rows="2" placeholder="ಗೂಗಲ್ ಮತ್ತು ವಾಟ್ಸಾಪ್ ಪ್ರಿವ್ಯೂನಲ್ಲಿ ಕಾಣಿಸುವ 2 ಸಾಲಿನ ವಿವರಣೆ..."></textarea>
                </div>
                <div class="form-group">
                  <label class="form-label">ಸೋಶಿಯಲ್ ಕವರ್ ಚಿತ್ರ URL <span>(OG / WhatsApp Image)</span></label>
                  <input type="url" id="seoImageInput" class="input-text" placeholder="https://karnata.in/assets/icons/icon-512x512.png">
                </div>
              </div>
            </div>

            <!-- SECTION 5: HEADER & BRAND -->
            <div class="section-box">
              <div class="section-hdr" onclick="toggleSection(this)">
                <span>🏷️ 5. ಹೆಡರ್ & ಸೂಚನಾ ಪಟ್ಟಿ (Header & Live Notice Bar)</span>
                <span>▼</span>
              </div>
              <div class="section-content" style="display:none;">
                <div class="form-group">
                  <label class="form-label">ಹೆಡರ್ ಸಬ್-ಟೆಕ್ಸ್ಟ್ <span>(Header Subtitle)</span></label>
                  <input type="text" id="headerSubtextInput" class="input-text" placeholder="ಉದಾ: ಅಧಿಕೃತ ನಾಗರಿಕ ಮಾಹಿತಿ ಕೇಂದ್ರ">
                </div>
                <div class="form-group">
                  <label class="form-label">ಟಾಪ್ ನೋಟಿಸ್ ಬಾರ್ ಪಠ್ಯ <span>(Notice Bar Alert)</span></label>
                  <input type="text" id="headerNoticeInput" class="input-text" placeholder="ಉದಾ: ದೈನಂದಿನ ಬೆಳಿಗ್ಗೆ 6:00 ಗಂಟೆಗೆ ಲೈವ್ ನವೀಕರಣ">
                </div>
              </div>
            </div>

            <!-- GLOBAL CLOUDFLARE SYNC BUTTON -->
            <button type="submit" id="btnSyncCloudflare" class="btn-sync-cloudflare">
              <span>🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಸಿಂಕ್ (Save & Sync to Cloudflare Edge)</span>
            </button>
            <div id="syncStatusMsg" style="font-size:13px; font-weight:700; margin-top:12px; text-align:center;"></div>

          </form>

        </div>

        <!-- RIGHT: LIVE SPLIT-SCREEN REAL-TIME PREVIEW -->
        <div class="preview-box">
          <div class="preview-header">
            <span>👁️ ನೈಜ ಸಮಯ ಲೈವ್ ಪ್ರಿವ್ಯೂ (Real-Time Live Preview)</span>
            <div style="display:flex; gap:10px;">
              <a id="btnOpenNewTabPreview" href="/petrol-price.html" target="_blank" style="color:#FDA4AF; text-decoration:none; font-size:12px;">ಹೊಸ ಟ್ಯಾಬ್‌ನಲ್ಲಿ ತೆರೆಯಿರಿ ↗</a>
            </div>
          </div>
          <iframe id="pageLivePreviewIframe" class="preview-iframe" src="/petrol-price.html"></iframe>
        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════
         TAB 2: WRITE ARTICLES STUDIO
         ══════════════════════════════════════════════════════════════════════════ -->
    <div id="sectionArticles" style="display:none;">
      <div style="display:grid; grid-template-columns:1fr 360px; gap:24px; align-items:start;">
        <div class="card">
          <h3 class="card-title">✍️ ಹೊಸ ವಿಶೇಷ ಲೇಖನ ಬರೆಯಿರಿ (New Article Studio)</h3>
          
          <div class="form-group">
            <label class="form-label">ಲೇಖನದ ಮುಖ್ಯ ಶೀರ್ಷಿಕೆ <span>(Title) *</span></label>
            <input type="text" id="artTitle" class="input-text" style="font-size:18px; font-weight:800;" placeholder="ಉದಾ: ಕರ್ನಾಟಕ ರೈತರಿಗೆ ಬಂಪರ್ ಕೊಡುಗೆ...">
          </div>

          <div class="form-group">
            <label class="form-label">ಸಾರಾಂಶ <span>(Short Summary) *</span></label>
            <textarea id="artSummary" class="textarea-box" rows="2" placeholder="2-3 ಸಾಲುಗಳಲ್ಲಿ ಸಾರಾಂಶ ಬರೆಯಿರಿ..."></textarea>
          </div>

          <div class="form-group">
            <label class="form-label">ಲೇಖನದ ಸಂಪೂರ್ಣ ವಿವರ <span>(Visual Article Content) *</span></label>
            <div class="editor-box">
              <div class="editor-toolbar">
                <button type="button" class="tb-btn" onclick="execCmdArt('bold')"><b>B</b></button>
                <button type="button" class="tb-btn" onclick="execCmdArt('italic')"><i>I</i></button>
                <button type="button" class="tb-btn" onclick="execCmdArt('formatBlock', '<h2>')">📌 H2</button>
                <button type="button" class="tb-btn" onclick="execCmdArt('formatBlock', '<h3>')">🔹 H3</button>
                <button type="button" class="tb-btn" onclick="execCmdArt('insertUnorderedList')">• ಪಟ್ಟಿ</button>
                <button type="button" class="tb-btn" onclick="execCmdArt('insertOrderedList')">1. ಕ್ರಮಾಂಕ</button>
                <button type="button" class="tb-btn" onclick="execCmdArt('formatBlock', '<blockquote>')">❝ ಕೋಟ್</button>
                <button type="button" class="tb-btn" onclick="promptInsertImgArt()">🖼️ ಚಿತ್ರ</button>
                <button type="button" class="tb-btn" onclick="execCmdArt('removeFormat')" style="color:#E11D48;">🧹 ಕ್ಲಿಯರ್</button>
              </div>
              <div id="artContentCanvas" class="visual-canvas" contenteditable="true" style="min-height:280px;" data-placeholder="ಇಲ್ಲಿ ಲೇಖನವನ್ನು ಸಾಮಾನ್ಯವಾಗಿ ಬರೆಯಿರಿ..."></div>
            </div>
          </div>
        </div>

        <div class="card">
          <h3 class="card-title">🚀 ಪ್ರಕಟಣೆ ಸೆಟ್ಟಿಂಗ್ಸ್</h3>
          
          <div class="form-group">
            <label class="form-label">ವರ್ಗ (Category)</label>
            <select id="artCategory" class="select-box">
              <option value="explainer">✨ ವಿಶೇಷ ಲೇಖನ (Explainer)</option>
              <option value="politics">🏛️ ರಾಜಕೀಯ & ಸರ್ಕಾರ (Politics)</option>
              <option value="agriculture">🌾 ಕೃಷಿ & ಮಾರುಕಟ್ಟೆ (Agriculture)</option>
              <option value="finance">💰 ಹಣಕಾಸು & ಹೂಡಿಕೆ (Finance & Gold)</option>
              <option value="schemes">💡 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು (Govt Schemes)</option>
              <option value="transport">🚗 ಸಾರಿಗೆ & ಮೆಟ್ರೋ (Transport)</option>
              <option value="weather">🌦️ ಹವಾಮಾನ & ಮಳೆ (Weather)</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">ಲೇಖಕರ ಹೆಸರು (Author)</label>
            <input type="text" id="artAuthor" class="input-text" value="ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ">
          </div>

          <div class="form-group">
            <label class="form-label">ಕವರ್ ಚಿತ್ರ URL (Cover Image)</label>
            <input type="url" id="artCover" class="input-text" placeholder="https://images.unsplash.com/...">
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; padding:10px 14px; border-radius:8px; margin-bottom:16px;">
            <span style="font-size:13px; font-weight:700;">📌 ಮುಖಪುಟದಲ್ಲಿ ಪಿನ್ ಮಾಡಿ</span>
            <input type="checkbox" id="artPinHome" checked style="width:18px; height:18px; accent-color:var(--primary);">
          </div>

          <button type="button" id="btnPublishArt" class="btn-sync-cloudflare" onclick="publishArticle()">
            <span>🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)</span>
          </button>
          <div id="publishStatus" style="font-size:13px; font-weight:700; margin-top:10px; text-align:center;"></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════
         TAB 3: MANAGE PUBLISHED ARTICLES
         ══════════════════════════════════════════════════════════════════════════ -->
    <div id="sectionManageArt" style="display:none;">
      <div class="card">
        <h3 class="card-title">📚 ಪ್ರಕಟಿತ ಲೇಖನಗಳ ನಿರ್ವಹಣೆ (Published Articles)</h3>
        <div id="publishedListWrap">
          <div style="text-align:center; padding:40px; color:#94A3B8;">ಯಾವುದೇ ಲೇಖನಗಳು ಪ್ರಕಟವಾಗಿಲ್ಲ.</div>
        </div>
      </div>
    </div>

  </main>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // 1. GATEWAY AUTHENTICATION
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

    // 2. TAB SWITCHING
    function switchMainTab(tab) {
      document.getElementById('tabBtnPages').classList.toggle('active', tab === 'pages');
      document.getElementById('tabBtnArticles').classList.toggle('active', tab === 'articles');
      document.getElementById('tabBtnManageArt').classList.toggle('active', tab === 'manage-articles');

      document.getElementById('sectionPages').style.display = tab === 'pages' ? 'block' : 'none';
      document.getElementById('sectionArticles').style.display = tab === 'articles' ? 'block' : 'none';
      document.getElementById('sectionManageArt').style.display = tab === 'manage-articles' ? 'block' : 'none';

      if (tab === 'manage-articles') renderPublishedList();
    }

    function toggleSection(hdr) {
      const isOpen = hdr.classList.contains('open');
      const content = hdr.nextElementSibling;
      hdr.classList.toggle('open', !isOpen);
      content.style.display = isOpen ? 'none' : 'block';
      hdr.querySelector('span:last-child').textContent = isOpen ? '▼' : '▲';
    }

    // 3. FULL PAGES STUDIO LOGIC
    let activePageFilename = 'petrol-price.html';
    let masterPagesDb = {};

    const pageMetaDefaults = {
      'petrol-price.html': { name: 'ಇಂಧನ ಬೆಲೆ (Petrol Price)', icon: '⛽' },
      'gold-rate.html': { name: 'ಚಿನ್ನ & ಬೆಳ್ಳಿ (Gold Rate)', icon: '🪙' },
      'apmc-prices.html': { name: 'APMC ದರ (Mandi Rates)', icon: '🌾' },
      'dam-levels.html': { name: 'ಜಲಾಶಯಗಳು (Dam Levels)', icon: '🌊' },
      'weather.html': { name: 'ಹವಾಮಾನ (Weather)', icon: '🌦️' },
      'mla-mp.html': { name: 'ಶಾಸಕರು & MP (MLA Hub)', icon: '🏛️' },
      'scheme-checker.html': { name: 'ಯೋಜನೆಗಳು (Schemes)', icon: '💡' },
      'kannada-typing.html': { name: 'ಕನ್ನಡ ಟೈಪಿಂಗ್ (Typing)', icon: '⌨️' },
      'ai-jyothishya.html': { name: 'ಜ್ಯೋತಿಷ್ಯ (Jyothishya)', icon: '🔮' },
      'about.html': { name: 'ನಮ್ಮ ಬಗ್ಗೆ (About Us)', icon: 'ℹ️' },
      'contact.html': { name: 'ಸಂಪರ್ಕಿಸಿ (Contact Us)', icon: '📞' },
      'privacy.html': { name: 'ಗೌಪ್ಯತಾ ನೀತಿ (Privacy Policy)', icon: '🔒' }
    };

    async function loadMasterPagesData() {
      try {
        const res = await fetch('/api/pages?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          masterPagesDb = d.pages || {};
        }
      } catch(e) {}
    }

    function selectPageForEdit(filename, element) {
      activePageFilename = filename;
      document.querySelectorAll('.page-item-card').forEach(el => el.classList.remove('active'));
      if (element) element.classList.add('active');

      const info = pageMetaDefaults[filename] || { name: filename, icon: '📄' };
      document.getElementById('currentEditingPageName').textContent = `${info.name} (${filename})`;
      document.getElementById('pageLivePreviewIframe').src = '/' + filename + '?t=' + Date.now();
      document.getElementById('btnOpenNewTabPreview').href = '/' + filename;

      populatePageFields(filename);
    }

    function populatePageFields(filename) {
      const pageData = masterPagesDb[filename] || {};
      const hero = pageData.hero || {};
      const geo = pageData.ai_geo || {};
      const seo = pageData.seo || {};
      const header = pageData.header || {};
      const content = pageData.content || {};

      document.getElementById('heroTitleInput').value = hero.title || '';
      document.getElementById('heroSubtitleInput').value = hero.subtitle || '';
      document.getElementById('heroBadgeInput').value = hero.badge || '⚡ ನೈಜ ಸಮಯ ನವೀಕರಣ';
      document.getElementById('heroAlertInput').value = hero.banner_alert || '';

      document.getElementById('geoDistrictInput').value = geo.default_district || 'ಬೆಂಗಳೂರು ನಗರ';
      document.getElementById('geoGreetingInput').value = geo.localized_greeting || 'ನಮಸ್ಕಾರ, ನಿಮ್ಮ ಪ್ರದೇಶದ ಇಂದಿನ ಮಾಹಿತಿ ಇಲ್ಲಿದೆ.';
      document.getElementById('geoAdvisoryInput').value = geo.district_advisory || '';

      document.getElementById('pageArticleCanvas').innerHTML = content.full_article_html || '';

      document.getElementById('seoTitleInput').value = seo.title || '';
      document.getElementById('seoDescInput').value = seo.meta_desc || '';
      document.getElementById('seoImageInput').value = seo.og_image || 'https://karnata.in/assets/icons/icon-512x512.png';

      document.getElementById('headerSubtextInput').value = header.brand_subtext || '';
      document.getElementById('headerNoticeInput').value = header.notice_bar || '';

      document.getElementById('syncStatusMsg').innerHTML = '';
    }

    function execCmdPage(cmd, val = null) {
      document.getElementById('pageArticleCanvas').focus();
      document.execCommand(cmd, false, val);
    }
    function promptInsertLinkPage() {
      const url = prompt('URL ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execCmdPage('createLink', url);
    }
    function promptInsertImgPage() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL):', 'https://');
      if (url && url !== 'https://') execCmdPage('insertImage', url);
    }

    async function saveAndSyncPageToCloudflare() {
      const btn = document.getElementById('btnSyncCloudflare');
      const status = document.getElementById('syncStatusMsg');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗುತ್ತಿದೆ (Syncing to Cloudflare Edge)...';
      status.innerHTML = '<span style="color:#2563EB;">⚡ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ನೆಟ್‌ವರ್ಕ್‌ನಲ್ಲಿ ಡೇಟಾ ನವೀಕರಣಗೊಳ್ಳುತ್ತಿದೆ...</span>';

      const payload = {
        page_id: activePageFilename,
        name_kn: pageMetaDefaults[activePageFilename]?.name || activePageFilename,
        updated_at: new Date().toISOString(),
        hero: {
          title: document.getElementById('heroTitleInput').value.trim(),
          subtitle: document.getElementById('heroSubtitleInput').value.trim(),
          badge: document.getElementById('heroBadgeInput').value.trim(),
          banner_alert: document.getElementById('heroAlertInput').value.trim()
        },
        ai_geo: {
          default_district: document.getElementById('geoDistrictInput').value,
          localized_greeting: document.getElementById('geoGreetingInput').value.trim(),
          district_advisory: document.getElementById('geoAdvisoryInput').value.trim()
        },
        content: {
          full_article_html: document.getElementById('pageArticleCanvas').innerHTML.trim(),
          summary: document.getElementById('seoDescInput').value.trim()
        },
        seo: {
          title: document.getElementById('seoTitleInput').value.trim(),
          meta_desc: document.getElementById('seoDescInput').value.trim(),
          og_image: document.getElementById('seoImageInput').value.trim(),
          keywords: ''
        },
        header: {
          brand_subtext: document.getElementById('headerSubtextInput').value.trim(),
          notice_bar: document.getElementById('headerNoticeInput').value.trim()
        }
      };

      try {
        const res = await fetch('/api/pages', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          masterPagesDb[activePageFilename] = payload;
          status.innerHTML = `<span style="color:#059669;">🎉 ಯಶಸ್ವಿಯಾಗಿದೆ! ಬದಲಾವಣೆಗಳು ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದ್ದು, ಜಗತ್ತಿನ ಎಲ್ಲಾ ಡಿವೈಸ್‌ಗಳಲ್ಲೂ ಲೈವ್ ಅಪ್ಡೇಟ್ ಆಗಿದೆ!</span>`;
          alert(`✅ "${pageMetaDefaults[activePageFilename]?.name || activePageFilename}" ಪುಟವು ಯಶಸ್ವಿಯಾಗಿ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಸರ್ವರ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದೆ!`);
          document.getElementById('pageLivePreviewIframe').src = '/' + activePageFilename + '?t=' + Date.now();
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch(err) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ: ${err.message}</span>`;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಸಿಂಕ್ (Save & Sync to Cloudflare Edge)';
      }
    }

    // 4. ARTICLE CMS LOGIC
    function execCmdArt(cmd, val = null) {
      document.getElementById('artContentCanvas').focus();
      document.execCommand(cmd, false, val);
    }
    function promptInsertImgArt() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್:', 'https://');
      if (url && url !== 'https://') execCmdArt('insertImage', url);
    }

    let allArticles = [];

    async function loadArticles() {
      try {
        const res = await fetch('/api/articles?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          allArticles = d.articles || [];
        }
      } catch(e) {}
      document.getElementById('pubCount').textContent = allArticles.length;
    }

    function renderPublishedList() {
      const wrap = document.getElementById('publishedListWrap');
      if (!allArticles.length) {
        wrap.innerHTML = `<div style="text-align:center; padding:40px; color:#94A3B8;">ಯಾವುದೇ ಲೇಖನಗಳು ಪ್ರಕಟವಾಗಿಲ್ಲ.</div>`;
        return;
      }

      wrap.innerHTML = allArticles.map(a => {
        const slug = a.slug || a.id;
        const cat = (a.category || 'explainer').toLowerCase();
        const liveUrl = `/news/${cat}/${slug}`;
        return `
          <div style="background:#FFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <strong style="font-size:15px; color:#0F172A;">${a.title_kn || a.title}</strong>
              <div style="font-size:12px; color:#64748B;">🏷️ ${a.category || 'explainer'} • ✍️ ${a.author || 'ಕರ್ನಾಟ ತಂಡ'}</div>
            </div>
            <div style="display:flex; gap:8px;">
              <a href="${liveUrl}" target="_blank" style="background:#ECFDF5; color:#059669; padding:4px 10px; border-radius:6px; font-size:12px; font-weight:700; text-decoration:none;">👁️ ನೋಡಿ</a>
            </div>
          </div>
        `;
      }).join('');
    }

    async function publishArticle() {
      const title = document.getElementById('artTitle').value.trim();
      const summary = document.getElementById('artSummary').value.trim();
      const bodyHtml = document.getElementById('artContentCanvas').innerHTML.trim();
      const category = document.getElementById('artCategory').value || 'explainer';
      const author = document.getElementById('artAuthor').value.trim() || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      const coverImage = document.getElementById('artCover').value.trim() || 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80';
      const isPin = document.getElementById('artPinHome').checked;

      if (!title) { alert('ದಯವಿಟ್ಟು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ'); return; }
      if (!bodyHtml) { alert('ದಯವಿಟ್ಟು ಲೇಖನದ ವಿವರವನ್ನು ಬರೆಯಿರಿ'); return; }

      const slug = title.toLowerCase().replace(/[\s_]+/g, '-').replace(/[^\w\-]+/g, '') || ('post-' + Date.now());
      const btn = document.getElementById('btnPublishArt');
      const status = document.getElementById('publishStatus');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಪ್ರಕಟಿಸಲಾಗುತ್ತಿದೆ...';

      const payload = {
        id: slug,
        slug: slug,
        title_kn: title,
        title: title,
        summary_kn: summary || title,
        summary: summary || title,
        category: category,
        author: author,
        cover_image: coverImage,
        body_html: bodyHtml,
        pin_home: isPin,
        priority: 10,
        status: 'published',
        updated_at: new Date().toISOString()
      };

      try {
        const res = await fetch('/api/articles', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          status.innerHTML = `<span style="color:#059669;">✅ ಯಶಸ್ವಿಯಾಗಿ ಪ್ರಕಟವಾಗಿದೆ!</span>`;
          alert('🎉 ಲೇಖನವು ತಕ್ಷಣವೇ ಪ್ರಕಟವಾಗಿದೆ!');
          loadArticles();
        }
      } catch(e) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ</span>`;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
      }
    }

    // INITIAL INITIALIZATION
    (async function init() {
      await loadMasterPagesData();
      selectPageForEdit('petrol-price.html', document.querySelector('.page-item-card'));
      await loadArticles();
    })();
  </script>
</body>
</html>
"""

# Save to admin/index.html and replicas
admin_path = os.path.join(ROOT_DIR, 'admin', 'index.html')
with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(STUDIO_HTML)

replicas = [
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'index.html'),
    os.path.join(ROOT_DIR, 'cms', 'admin.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'cms', 'admin.html')
]

for r in replicas:
    os.makedirs(os.path.dirname(r), exist_ok=True)
    with open(r, 'w', encoding='utf-8') as f:
        f.write(STUDIO_HTML)
    print(f"Synced studio to {r}")

print("SUCCESS_FULL_PAGES_STUDIO_BUILT")
