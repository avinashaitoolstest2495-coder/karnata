# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_full_apmc_page.py
Generates the complete APMC Market & 10-Year Crop Price Analyzer (ರೈತರ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ & ಬೆಲೆ ಏರಿಳಿತ ಮುನ್ಸೂಚನೆ 2016-2026).
"""

import json

html_content = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="canonical" href="https://karnata.in/apmc-prices">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) | Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ಲೈವ್ ದರಗಳು ಮತ್ತು ಕಳೆದ 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ಏರಿಳಿತ ವಿಶ್ಲೇಷಣೆ (2016-2026). ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟಕ್ಕೆ ಅತ್ಯುತ್ತಮ ತಿಂಗಳುಗಳು, ಗರಿಷ್ಠ ಬೆಲೆ ಹಾಗೂ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP) ಮಾರ್ಗದರ್ಶಿ.">
  <meta name="keywords" content="APMC price Karnataka, 10 year crop price analysis, Karnataka mandi rates today, best time to sell arecanut, byadgi chilli rate trend, tur dal price forecast, tomato price kolar, krama karnataka gov in">
  
  <!-- OpenGraph & Social SEO -->
  <meta property="og:title" content="APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) — Karnata.in">
  <meta property="og:description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ಲೈವ್ ದರಗಳು & ಕಳೆದ 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ಏರಿಳಿತ ಮುನ್ಸೂಚನೆ. ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟಕ್ಕೆ ಸರಿಯಾದ ಸಮಯ!">
  <meta property="og:url" content="https://karnata.in/apmc-prices.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Karnata.in">
  <meta property="og:locale" content="kn_IN">
  <meta property="og:image" content="https://karnata.in/assets/icons/icon-512x512.png">
  
  <!-- Google Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/apmc-prices.html",
    "description": "Live Karnataka APMC agricultural commodity prices and 10-year historical seasonal price analyzer for farmers."
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  
  <!-- Chart.js for 10-Year Crop Trends -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="/data-loader.js"></script>
  <script src="/nav-component.js"></script>

  <style>
    :root {
      --primary: #15803D;
      --primary-dark: #14532D;
      --primary-light: #DCFCE7;
      --accent: #D97706;
      --accent-light: #FEF3C7;
      --danger: #DC2626;
      --danger-light: #FEE2E2;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --radius: 14px;
      --shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.06);
    }
    
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Anek Kannada', sans-serif;
      background: var(--bg);
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }
    
    /* HERO BANNER */
    .apmc-hero {
      background: linear-gradient(135deg, #0D4A2B 0%, #15803D 50%, #166534 100%);
      color: #FFFFFF;
      padding: 36px 20px 75px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid #FACC15;
    }
    .apmc-hero h1 {
      font-size: 28px;
      font-weight: 900;
      margin-bottom: 6px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .apmc-hero p {
      font-size: 14.5px;
      color: #E2E8F0;
      max-width: 760px;
      margin: 0 auto 12px;
      font-weight: 500;
    }
    .apmc-hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 4px 14px;
      border-radius: 30px;
      font-size: 11.5px;
      font-weight: 700;
      color: #FEF08A;
    }

    /* TOP STATS CARDS */
    .stats-bar {
      max-width: 1180px;
      margin: -45px auto 24px;
      padding: 0 16px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      position: relative;
      z-index: 10;
    }
    @media (max-width: 900px) { .stats-bar { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 500px) { .stats-bar { grid-template-columns: 1fr; } }
    
    .stat-card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      box-shadow: var(--shadow);
      text-align: center;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .stat-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -4px rgba(21, 128, 61, 0.15);
    }
    .stat-icon { font-size: 24px; margin-bottom: 4px; }
    .stat-val { font-size: 22px; font-weight: 900; color: var(--primary-dark); font-family: 'Inter', sans-serif; }
    .stat-lbl { font-size: 12.5px; font-weight: 700; color: var(--text-main); margin-top: 2px; }
    .stat-sub { font-size: 11px; color: var(--text-muted); }

    /* MAIN CONTAINER */
    .apmc-container {
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 16px 40px;
    }

    /* MODE TOGGLE TABS */
    .mode-tabs {
      display: flex;
      gap: 8px;
      background: #E2E8F0;
      padding: 5px;
      border-radius: 14px;
      margin-bottom: 24px;
    }
    .mode-tab {
      flex: 1;
      text-align: center;
      padding: 12px 16px;
      font-size: 15px;
      font-weight: 800;
      border-radius: 10px;
      cursor: pointer;
      border: none;
      background: transparent;
      color: var(--text-muted);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: inherit;
    }
    .mode-tab.active {
      background: #FFFFFF;
      color: var(--primary-dark);
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    /* ═══ SECTION 1: 10-YEAR ANALYZER ENGINE ═══ */
    .analyzer-box {
      background: #FFFFFF;
      border: 1.5px solid #CBD5E1;
      border-radius: 18px;
      padding: 24px;
      box-shadow: var(--shadow);
      margin-bottom: 30px;
    }
    .analyzer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .analyzer-title {
      font-size: 20px;
      font-weight: 900;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .crop-selector-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 280px;
    }
    .crop-select {
      width: 100%;
      padding: 10px 14px;
      font-size: 14px;
      font-weight: 800;
      font-family: inherit;
      border: 2px solid var(--primary);
      border-radius: 12px;
      background: #F0FDF4;
      color: var(--primary-dark);
      cursor: pointer;
      outline: none;
    }

    /* ANALYZER GRID */
    .analyzer-insights-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    @media (max-width: 850px) { .analyzer-insights-grid { grid-template-columns: 1fr; } }

    /* SMART ADVICE CARDS */
    .advice-card {
      background: #F8FAFC;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 18px;
      margin-bottom: 14px;
    }
    .advice-card.best-time {
      background: #F0FDF4;
      border-color: #86EFAC;
    }
    .advice-card.warning-time {
      background: #FEF2F2;
      border-color: #FECACA;
    }
    .advice-title {
      font-size: 14.5px;
      font-weight: 800;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .advice-desc {
      font-size: 13.5px;
      color: #334155;
      line-height: 1.6;
    }

    /* 12-MONTH HEATMAP */
    .season-heatmap {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 4px;
      margin-top: 14px;
    }
    @media (max-width: 700px) { .season-heatmap { grid-template-columns: repeat(6, 1fr); gap: 6px; } }
    .heat-cell {
      padding: 8px 4px;
      text-align: center;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
    }
    .heat-cell.peak { background: #15803D; color: #FFFFFF; }
    .heat-cell.good { background: #86EFAC; color: #14532D; }
    .heat-cell.avg { background: #FEF08A; color: #713F12; }
    .heat-cell.low { background: #FCA5A5; color: #7F1D1D; }
    .heat-cell.crash { background: #DC2626; color: #FFFFFF; }

    /* ═══ SECTION 2: LIVE APMC MARKET FEED ═══ */
    .controls-panel {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 20px;
      box-shadow: var(--shadow);
    }
    .filter-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 768px) { .filter-row { grid-template-columns: 1fr; } }
    
    .select-input, .search-input {
      width: 100%;
      padding: 10px 14px;
      font-size: 13.5px;
      font-family: inherit;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      background: #F8FAFC;
      color: var(--text-main);
      outline: none;
    }
    .select-input:focus, .search-input:focus {
      border-color: var(--primary);
      background: #FFFFFF;
    }

    .category-pills {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }
    .category-pills::-webkit-scrollbar { display: none; }
    .cat-pill {
      padding: 7px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 700;
      background: #F1F5F9;
      color: var(--text-muted);
      border: 1px solid var(--border);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s;
    }
    .cat-pill.active, .cat-pill:hover {
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
    }

    /* APMC CARDS 3-COLUMN GRID */
    .apmc-card-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 30px;
    }
    @media (max-width: 950px) { .apmc-card-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 600px) { .apmc-card-grid { grid-template-columns: 1fr; } }

    .mandi-card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      box-shadow: var(--shadow);
      transition: transform 0.2s, box-shadow 0.2s;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .mandi-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 24px -4px rgba(0,0,0,0.1);
      border-color: #86EFAC;
    }
    .mc-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
    }
    .mc-crop-name {
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.3;
    }
    .mc-mandi {
      font-size: 12px;
      font-weight: 700;
      color: var(--primary);
      margin-top: 2px;
    }
    .mc-price-box {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-radius: 10px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }
    .mc-modal-price {
      font-size: 26px;
      font-weight: 900;
      color: var(--primary-dark);
      font-family: 'Inter', sans-serif;
    }
    .mc-unit {
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .mc-range-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: #F8FAFC;
      padding: 8px 10px;
      border-radius: 8px;
      font-size: 11.5px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    .mc-range-val {
      font-weight: 800;
      color: var(--text-main);
      font-family: 'Inter', sans-serif;
    }
    .mc-share-btn {
      width: 100%;
      background: #25D366;
      color: #FFFFFF;
      border: none;
      padding: 8px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: inherit;
      transition: background 0.15s;
    }
    .mc-share-btn:hover { background: #1EBE5D; }
  </style>
</head>
<body>

  <!-- HERO SECTION -->
  <header class="apmc-hero">
    <div class="apmc-hero-tag">🌾 ಕರ್ನಾಟಕ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಮಂಡಳಿ (KSAMB) & ReMS ಲೈವ್ ಮಾಹಿತಿ</div>
    <h1>APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ</h1>
    <p>ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ಲೈವ್ ದರಗಳು, ಕಳೆದ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಏರಿಳಿತ (2016-2026), ಗರಿಷ್ಠ ಬೆಲೆಯ ಸೀಸನ್ ಹಾಗೂ ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟದ ಸ್ಮಾರ್ಟ್ ಮಾರ್ಗದರ್ಶಿ.</p>
    <div style="font-size:12px; color:#FEF08A; font-weight:700;" id="hero-update-date">🔴 ಇಂದಿನ ಲೈವ್ ದರ ನವೀಕರಣ: 2026-08-28 — krama.karnataka.gov.in</div>
  </header>

  <!-- 4 SUMMARY STATS -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-icon">🌾</div>
      <div class="stat-val" id="stat-total-records">1,838</div>
      <div class="stat-lbl">ಇಂದಿನ ದರ ನಮೂದುಗಳು</div>
      <div class="stat-sub">174 APMC ಮಂಡಿಗಳು</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📊</div>
      <div class="stat-val" id="stat-avg-price">₹4,850</div>
      <div class="stat-lbl">ರಾಜ್ಯ ಸರಾಸರಿ ಮಾದರಿ ದರ</div>
      <div class="stat-sub">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್ ಬೆಲೆ</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🔥</div>
      <div class="stat-val" id="stat-top-crop">₹56,500</div>
      <div class="stat-lbl">ಅತ್ಯಧಿಕ ಬೆಲೆಯ ಬೆಳೆ</div>
      <div class="stat-sub">ಅಡಿಕೆ (ರಾಶಿ / ಚಾಲಿ)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📈</div>
      <div class="stat-val">10 ವರ್ಷ</div>
      <div class="stat-lbl">ಬೆಲೆ ಏರಿಳಿತ ಮುನ್ಸೂಚನೆ</div>
      <div class="stat-sub">2016 - 2026 ಐತಿಹಾಸಿಕ ವಿಶ್ಲೇಷಣೆ</div>
    </div>
  </div>

  <!-- MAIN WRAPPER -->
  <div class="apmc-container">

    <!-- MODE TABS -->
    <div class="mode-tabs">
      <button class="mode-tab active" id="tab-live" onclick="switchMode('live')">
        <span>🌾 ಇಂದಿನ ಲೈವ್ APMC ದರಗಳು</span>
      </button>
      <button class="mode-tab" id="tab-analyzer" onclick="switchMode('analyzer')">
        <span>📈 ರೈತರ 10 ವರ್ಷಗಳ ಬೆಲೆ ವಿಶ್ಲೇಷಕ & ಮುನ್ಸೂಚನೆ (2016-2026)</span>
      </button>
    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 1: 10-YEAR CROP PRICE ANALYZER & ENGINE
    ══════════════════════════════════════════════════════ -->
    <div id="view-analyzer" style="display:none;">
      
      <div class="analyzer-box">
        <div class="analyzer-header">
          <div class="analyzer-title">
            <span>📊 ರೈತರ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (Crop Rate & Seasonality Intelligence)</span>
          </div>
          <div class="crop-selector-wrap">
            <label style="font-size:13px; font-weight:800; white-space:nowrap;">ಬೆಳೆ ಆಯ್ಕೆ ಮಾಡಿ:</label>
            <select id="analyzer-crop-select" class="crop-select" onchange="updateCropAnalysis()">
              <option value="arecanut">🌴 ಅಡಿಕೆ (Arecanut - Rashi/Chali)</option>
              <option value="byadgi_chilli">🌶️ ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ (Byadgi Dry Chilli)</option>
              <option value="tur_dal">🫘 ತೊಗರಿ ಬೇಳೆ (Red Gram / Tur Dal)</option>
              <option value="copra">🥥 ಕೊಬ್ಬರಿ & ತೆಂಗಿನಕಾಯಿ (Copra / Coconut)</option>
              <option value="cotton">☁️ ಹತ್ತಿ (Cotton - DCH/Bt)</option>
              <option value="paddy">🌾 ಸೋನಾ ಮಸೂರಿ ಭತ್ತ (Paddy)</option>
              <option value="ragi">🌾 ರಾಗಿ (Finger Millet / Ragi)</option>
              <option value="jowar">🌾 ಬಿಳಿ ಜೋಳ (Jowar / Maldandi)</option>
              <option value="maize">🌽 ಮೆಕ್ಕೆಜೋಳ (Maize)</option>
              <option value="onion">🧅 ಈರುಳ್ಳಿ (Onion)</option>
              <option value="tomato">🍅 ಟೊಮ್ಯಾಟೋ (Tomato)</option>
              <option value="coffee">☕ ಕಾಫಿ (Coffee - Arabica / Robusta)</option>
              <option value="ginger">🫚 ಶುಂಠಿ (Ginger)</option>
              <option value="turmeric">🟡 ಅರಿಶಿನ (Turmeric)</option>
              <option value="groundnut">🥜 ಶೇಂಗಾ / ಕಡಲೆಕಾಯಿ (Groundnut)</option>
              <option value="bengal_gram">🫘 ಕಡಲೆ (Bengal Gram / Chana)</option>
            </select>
          </div>
        </div>

        <!-- INSIGHTS GRID -->
        <div class="analyzer-insights-grid">
          
          <!-- LEFT: 10-Year Price Trend Chart -->
          <div>
            <h3 style="font-size:15px; font-weight:800; color:#1e293b; margin-bottom:12px;" id="chart-heading">10 ವರ್ಷಗಳ ಬೆಲೆ ಪ್ರವೃತ್ತಿ (2016–2026 ₹ / ಕ್ವಿಂಟಾಲ್)</h3>
            <div style="height:260px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:12px;">
              <canvas id="cropTrendChart"></canvas>
            </div>

            <!-- 12-Month Heatmap -->
            <div style="margin-top:20px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="font-size:13.5px; font-weight:800; color:#1e293b;">12 ತಿಂಗಳ ಬೆಲೆ ಏರಿಳಿತ ಹರಿವು (Seasonality Heatmap)</h4>
                <span style="font-size:11px; color:#16a34a; font-weight:800;">ಹಸಿರು = ಗರಿಷ್ಠ ಬೆಲೆ</span>
              </div>
              <div class="season-heatmap" id="season-heatmap-grid"></div>
            </div>
          </div>

          <!-- RIGHT: AI Smart Advice & When to Sell -->
          <div>
            <!-- Best Time to Sell -->
            <div class="advice-card best-time">
              <div class="advice-title" style="color:#15803D;">
                <span>🟢 ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು? (Peak Price Window)</span>
              </div>
              <div class="advice-desc" id="adv-best-time">
                ಜುಲೈ ನಿಂದ ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಅಡಿಕೆ ಬೆಲೆ ಗರಿಷ್ಠ ಮಟ್ಟ ತಲುಪುತ್ತದೆ. ಈ ಅವಧಿಯಲ್ಲಿ ಗುಟ್ಕಾ ಮತ್ತು ಪಾನ್ ಮಸಾಲಾ ಉದ್ಯಮಗಳಿಂದ ಬೇಡಿಕೆ ಹೆಚ್ಚಿರುತ್ತದೆ.
              </div>
            </div>

            <!-- Price Drop Warning -->
            <div class="advice-card warning-time">
              <div class="advice-title" style="color:#DC2626;">
                <span>🔴 ಯಾವಾಗ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ? (Harvest Glut Warning)</span>
              </div>
              <div class="advice-desc" id="adv-worst-time">
                ನವೆಂಬರ್ ನಿಂದ ಜನವರಿ ತಿಂಗಳಲ್ಲಿ ಹೊಸ ಅಡಿಕೆ ಕೊಯ್ಲು ಮಾರುಕಟ್ಟೆಗೆ ಭಾರಿ ಪ್ರಮಾಣದಲ್ಲಿ ಬರುವುದರಿಂದ ಬೆಲೆ 15% ರಿಂದ 20% ಕುಸಿಯುತ್ತದೆ.
              </div>
            </div>

            <!-- Smart Strategy -->
            <div class="advice-card">
              <div class="advice-title" style="color:#0F172A;">
                <span>💡 ರೈತರಿಗೆ ಸ್ಮಾರ್ಟ್ ಶೇಖರಣಾ ತಂತ್ರ & ಲಾಭದ ಲೆಕ್ಕ</span>
              </div>
              <div class="advice-desc" id="adv-strategy">
                ಕೊಯ್ಲಿನ ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡದೆ, ಸರಿಯಾಗಿ ಒಣಗಿಸಿ ಉಗ್ರಾಣದಲ್ಲಿ (KSWC Warehouse) 4 ತಿಂಗಳು ಶೇಖರಿಸಿ ಜುಲೈನಲ್ಲಿ ಮಾರಿದರೆ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹6,000 ರಿಂದ ₹10,000 ಹೆಚ್ಚಿನ ಲಾಭ ಪಡೆಯಬಹುದು.
              </div>
            </div>

            <!-- MSP & Benchmark Stats -->
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:12px;">
              <div style="background:#F0FDF4; border:1px solid #BBF7D0; padding:10px; border-radius:10px; text-align:center;">
                <div style="font-size:11px; color:#15803D; font-weight:700;">ಸರ್ಕಾರಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP)</div>
                <div style="font-size:16px; font-weight:900; color:#14532D;" id="adv-msp">MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ</div>
              </div>
              <div style="background:#FEF3C7; border:1px solid #FDE68A; padding:10px; border-radius:10px; text-align:center;">
                <div style="font-size:11px; color:#92400E; font-weight:700;">10 ವರ್ಷಗಳ ಒಟ್ಟು ಬೆಳವಣಿಗೆ</div>
                <div style="font-size:16px; font-weight:900; color:#78350F;" id="adv-cagr">+101.7% (ಬಲವಾದ ಏರಿಕೆ)</div>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 2: LIVE APMC MANDI RATES (174+ Mandis)
    ══════════════════════════════════════════════════════ -->
    <div id="view-live">
      
      <!-- CONTROLS -->
      <div class="controls-panel">
        <div class="filter-row">
          <select id="market-select" class="select-input" onchange="filterData(true)">
            <option value="all">🏪 ಎಲ್ಲಾ ಮಾರುಕಟ್ಟೆಗಳು (All 174 Mandis)</option>
          </select>
          <select id="commodity-select" class="select-input" onchange="filterData(true)">
            <option value="all">🌾 ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳು (All Commodities)</option>
          </select>
          <input type="text" id="apmc-search" class="search-input" placeholder="🔍 ಬೆಳೆ ಹೆಸರು ಅಥವಾ ಮಾರುಕಟ್ಟೆ ಹುಡುಕಿ..." oninput="filterData(true)">
        </div>

        <div class="category-pills">
          <button class="cat-pill active" onclick="setCategory('all', this)">🌾 ಎಲ್ಲಾ ವಿಭಾಗಗಳು</button>
          <button class="cat-pill" onclick="setCategory('cash', this)">🌴 ವಾಣಿಜ್ಯ ಬೆಳೆ (Cash Crops)</button>
          <button class="cat-pill" onclick="setCategory('grain', this)">🌾 ಆಹಾರ ಧಾನ್ಯಗಳು (Grains)</button>
          <button class="cat-pill" onclick="setCategory('pulse', this)">🫘 ಬೇಳೆಕಾಳುಗಳು (Pulses)</button>
          <button class="cat-pill" onclick="setCategory('veg', this)">🥕 ತರಕಾರಿಗಳು (Vegetables)</button>
          <button class="cat-pill" onclick="setCategory('fruit', this)">🍎 ಹಣ್ಣುಗಳು (Fruits)</button>
          <button class="cat-pill" onclick="setCategory('spice', this)">🌶️ ಸಾಂಬಾರ ಪದಾರ್ಥ (Spices)</button>
          <button class="cat-pill" onclick="setCategory('oilseed', this)">🌻 ಎಣ್ಣೆಕಾಳು (Oilseeds)</button>
        </div>
      </div>

      <!-- CARDS GRID -->
      <div class="apmc-card-grid" id="apmc-card-grid"></div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         COMPREHENSIVE 9-SECTION FARMER GUIDE & SEO MANUAL
    ══════════════════════════════════════════════════════ -->
    <article class="article-container font-kannada" style="line-height: 1.85; color: #222; font-size: 15.5px; margin-top: 40px; padding: 25px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;">
      
      <header>
        <h2 style="font-size: 24px; color: #0f172a; margin-bottom: 8px; font-weight: 800;">ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಮಾರ್ಗದರ್ಶಿ, ReMS ಇ-ಹರಾಜು ಮತ್ತು ಬೆಳೆ ಮಾರಾಟ ತಂತ್ರ</h2>
        <p style="color: #64748b; font-size: 13.5px; margin-bottom: 20px;">ಪ್ರಕಟಣೆ: Karnata.in ಕೃಷಿ & ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ವಿಭಾಗ | ಅಧಿಕೃತ ಮೂಲ: KSAMB & KRAMA</p>
      </header>

      <hr style="border:0; border-top:1px solid #E2E8F0; margin-bottom:20px;">

      <section>
        <h3 style="font-size:18px; color:#14532d; font-weight:700; margin-bottom:8px;">1. ಕರ್ನಾಟಕದ ಪ್ರಮುಖ APMC ಮಾರುಕಟ್ಟೆಗಳ ವಿಶೇಷತೆ</h3>
        <p>ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ 174 ಕ್ಕೂ ಹೆಚ್ಚು ಮುಖ್ಯ APMC ಮಾರುಕಟ್ಟೆಗಳು ಹಾಗೂ 350 ಕ್ಕೂ ಹೆಚ್ಚು ಉಪ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣಗಳು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿವೆ. ಪ್ರತಿ ಮಾರುಕಟ್ಟೆಯು ನಿರ್ದಿಷ್ಟ ಬೆಳೆಗೆ ದೇಶವ್ಯಾಪಿ ಪ್ರಸಿದ್ಧಿ ಪಡೆದಿದೆ:</p>
        <ul style="padding-left:20px; margin:10px 0;">
          <li><strong>ಬ್ಯಾಡಗಿ APMC:</strong> ಕೆಂಪು ಮೆಣಸಿನಕಾಯಿ ವಹಿವಾಟಿನಲ್ಲಿ ಏಷ್ಯಾದಲ್ಲೇ 2ನೇ ಅತಿ ದೊಡ್ಡ ಮಾರುಕಟ್ಟೆ (Byadgi KDL & Dabbi).</li>
          <li><strong>ಶಿವಮೊಗ್ಗ & ಸಾಗರ APMC:</strong> ಕೆಂಪು ರಾಶಿ ಅಡಿಕೆ ಮತ್ತು ಚಾಲಿ ಅಡಿಕೆಯ ರಾಜಧಾನಿ.</li>
          <li><strong>ತಿಪಟೂರು & ಅರಸೀಕೆರೆ APMC:</strong> ತೆಂಗಿನಕಾಯಿ ಮತ್ತು ಉಂಡೆ ಕೊಬ್ಬರಿಗೆ (Ball Copra) ವಿಶ್ವ ಪ್ರಸಿದ್ಧ ಕೇಂದ್ರ.</li>
          <li><strong>ಕೋಲಾರ & ಚಿಂತಾಮಣಿ APMC:</strong> ಏಷ್ಯಾದ ಎರಡನೇ ಅತಿ ದೊಡ್ಡ ಟೊಮ್ಯಾಟೋ ಮಾರುಕಟ್ಟೆ.</li>
          <li><strong>ಕಲಬುರಗಿ APMC:</strong> ಜಿಐ ಟ್ಯಾಗ್ ಮಾನ್ಯತೆ ಪಡೆದ ಕರ್ನಾಟಕದ ತೊಗರಿಯ ಕಣಜ.</li>
        </ul>
      </section>

      <section style="margin-top:20px;">
        <h3 style="font-size:18px; color:#14532d; font-weight:700; margin-bottom:8px;">2. ReMS ಇ-ಹರಾಜು ಮೂಲಕ ರೈತರಿಗೆ ಸಿಗುವ ರಕ್ಷಣೆ</h3>
        <p>ರೈತರು ತಂದ ಕೃಷಿ ಉತ್ಪನ್ನಗಳಿಗೆ ಆನ್‌ಲೈನ್ ಮೂಲಕ ದೇಶದಾದ್ಯಂತ ಇರುವ ಖರೀದಿದಾರರು ಬಿಡ್ ಮಾಡುತ್ತಾರೆ. ರೈತರು ತಮ್ಮ ಮೊಬೈಲ್‌ನಲ್ಲಿ ದರ ನೋಡಿ, ಬೆಲೆ ತೃಪ್ತಿಕರವಾಗಿದ್ದರೆ ಮಾತ್ರ ಮಾರಾಟಕ್ಕೆ ಒಪ್ಪಿಗೆ (Accept) ನೀಡಬಹುದು. ಬೆಲೆ ಕಡಿಮೆ ಎನಿಸಿದರೆ ತಿರಸ್ಕರಿಸಿ ಉಗ್ರಾಣದಲ್ಲಿ ಇಡಬಹುದು.</p>
      </section>

      <footer style="margin-top:25px; padding:12px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:8px; font-size:12.5px; color:#166534;">
        <strong>ಮಾಹಿತಿ ಹಕ್ಕುತ್ಯಾಗ:</strong> ಇಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗುವ APMC ದರಗಳು ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ (KSAMB), ReMS ಪೋರ್ಟಲ್ ಹಾಗೂ ಕೇಂದ್ರ ಸರ್ಕಾರದ Agmarknet ಅಧಿಕೃತ ಬುಲೆಟಿನ್‌ಗಳ ಆಧಾರಿತವಾಗಿವೆ. ನೈಜ ದರಗಳು ಗುಣಮಟ್ಟ, ತೇವಾಂಶ ಮತ್ತು ಹರಾಜಿನ ಸಮಯಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಬದಲಾಗಬಹುದು.
      </footer>

    </article>

  </div>

  <script>
    // ══════════════════════════════════════════════════════
    // 10-YEAR HISTORICAL CROPS DATA ENGINE (2016–2026)
    // ══════════════════════════════════════════════════════
    const CROP_ANALYZER_DB = {
      arecanut: {
        name: "ಅಡಿಕೆ (Arecanut - Rashi/Chali)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 28000 },
          { year: "2017", price: 30500 },
          { year: "2018", price: 32500 },
          { year: "2019", price: 35000 },
          { year: "2020", price: 38000 },
          { year: "2021", price: 44000 },
          { year: "2022", price: 48500 },
          { year: "2023", price: 50000 },
          { year: "2024", price: 52000 },
          { year: "2025", price: 54500 },
          { year: "2026", price: 56500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಜೂನ್ ನಿಂದ ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಅಡಿಕೆ ಬೆಲೆ ಗರಿಷ್ಠ ಮಟ್ಟ ತಲುಪುತ್ತದೆ. ಮಳೆಗಾಲದ ಅವಧಿಯಲ್ಲಿ ಮಾರುಕಟ್ಟೆಗೆ ಆವಕ ಕಡಿಮೆಯಾಗಿ ಉತ್ತರ ಭಾರತದ ಮಸಾಲೆ ಕಂಪನಿಗಳಿಂದ ಭಾರಿ ಬೇಡಿಕೆ ಇರುತ್ತದೆ.",
        worstTime: "ನವೆಂಬರ್ ನಿಂದ ಜನವರಿ ತಿಂಗಳಲ್ಲಿ ಹೊಸ ಅಡಿಕೆ ಕೊಯ್ಲು ಮಾರುಕಟ್ಟೆಗೆ ಭಾರಿ ಪ್ರಮಾಣದಲ್ಲಿ ಬರುವುದರಿಂದ ಬೆಲೆ 15% ರಿಂದ 22% ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಹೊಸ ಕೊಯ್ಲಿನ ಅಡಿಕೆಯನ್ನು ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡದೆ, ಸರಿಯಾಗಿ ಒಣಗಿಸಿ KSWC ಉಗ್ರಾಣದಲ್ಲಿ 4-5 ತಿಂಗಳು ಶೇಖರಿಸಿ ಜುಲೈ-ಆಗಸ್ಟ್‌ನಲ್ಲಿ ಮಾರಿದರೆ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹7,000 ರಿಂದ ₹10,000 ಹೆಚ್ಚಿನ ನಿವ್ವಳ ಲಾಭ ಪಡೆಯಬಹುದು.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ (ವಾಣಿಜ್ಯ ಬೆಳೆ)",
        cagr: "+101.7% (10 ವರ್ಷಗಳ ಭಾರಿ ಏರಿಕೆ)"
      },

      byadgi_chilli: {
        name: "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ (Byadgi Dry Chilli)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 12500 },
          { year: "2017", price: 9500 },
          { year: "2018", price: 16000 },
          { year: "2019", price: 18500 },
          { year: "2020", price: 24500 },
          { year: "2021", price: 31000 },
          { year: "2022", price: 42000 },
          { year: "2023", price: 54000 },
          { year: "2024", price: 48000 },
          { year: "2025", price: 45000 },
          { year: "2026", price: 44000 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಆಗಸ್ಟ್ ನಿಂದ ನವೆಂಬರ್ ತಿಂಗಳಲ್ಲಿ ರಫ್ತು ಬೇಡಿಕೆ ಮತ್ತು ಮಸಾಲೆ ಎಣ್ಣೆ ಸಾರ (Oleoresin Extraction) ಕಂಪನಿಗಳ ಖರೀದಿ ತೀವ್ರವಾಗಿ ಬೆಲೆ ಗರಿಷ್ಠ ಮಟ್ಟ ತಲುಪುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ ನಿಂದ ಏಪ್ರಿಲ್ ತಿಂಗಳಲ್ಲಿ ಬ್ಯಾಡಗಿ ಮಾರುಕಟ್ಟೆಗೆ ದಿನಕ್ಕೆ 2 ಲಕ್ಷ ಚೀಲ ಮೆಣಸಿನಕಾಯಿ ಆವಕವಾಗುವುದರಿಂದ ಬೆಲೆ ಭಾರಿ ಪ್ರಮಾಣದಲ್ಲಿ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಮಾರ್ಚ್‌ನಲ್ಲಿ ಬರುವ ಮಾಲನ್ನು ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್‌ನಲ್ಲಿ (Cold Storage) ಇರಿಸಿ, ಆಗಸ್ಟ್-ಅಕ್ಟೋಬರ್ ತಿಂಗಳಲ್ಲಿ ಮಾರಿದರೆ ಶೇಖರಣಾ ವೆಚ್ಚ ಕಳೆದು 30% ರಿಂದ 45% ಹೆಚ್ಚಿನ ಲಾಭ ನಿಶ್ಚಿತ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+252% (ಅತ್ಯಧಿಕ ದೀರ್ಘಕಾಲೀನ ಬೆಳವಣಿಗೆ)"
      },

      tur_dal: {
        name: "ತೊಗರಿ ಬೇಳೆ (Red Gram / Tur Dal)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 6200 },
          { year: "2017", price: 4800 },
          { year: "2018", price: 5600 },
          { year: "2019", price: 6100 },
          { year: "2020", price: 6800 },
          { year: "2021", price: 7100 },
          { year: "2022", price: 7500 },
          { year: "2023", price: 9200 },
          { year: "2024", price: 10800 },
          { year: "2025", price: 10200 },
          { year: "2026", price: 9800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಜುಲೈ ನಿಂದ ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ದೇಶೀಯ ದಾಸ್ತಾನು ಕಡಿಮೆಯಾಗಿ ಬೆಲೆ ಅತ್ಯಧಿಕವಾಗಿರುತ್ತದೆ.",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿಯಲ್ಲಿ ಕಲಬುರಗಿ, ಯಾದಗಿರಿ, ಬೀದರ್‌ನಲ್ಲಿ ಕೊಯ್ಲಿನ ನಂತರ ಮಾರುಕಟ್ಟೆಗೆ ಒಮ್ಮೆಲೇ ಮಾಲು ಬರುವುದರಿಂದ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಮಂಡಿ ದರವು MSP ಗಿಂತ ಕಡಿಮೆಯಿದ್ದಾಗ ನೇರವಾಗಿ ಸರ್ಕಾರದ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ. ಮಂಡಿ ದರ ಹೆಚ್ಚಿದ್ದರೆ ಜುಲೈವರೆಗೆ ಕಾಯ್ದಿರಿಸಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹7,550 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+58.0% (ಸ್ಥಿರ ಏರಿಕೆ)"
      },

      copra: {
        name: "ಕೊಬ್ಬರಿ & ತೆಂಗಿನಕಾಯಿ (Copra / Coconut)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 6800 },
          { year: "2017", price: 8500 },
          { year: "2018", price: 11500 },
          { year: "2019", price: 10800 },
          { year: "2020", price: 10200 },
          { year: "2021", price: 13000 },
          { year: "2022", price: 12000 },
          { year: "2023", price: 11200 },
          { year: "2024", price: 13500 },
          { year: "2025", price: 14200 },
          { year: "2026", price: 14800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಆಗಸ್ಟ್ ನಿಂದ ನವೆಂಬರ್ (ಗಣೇಶ ಚತುರ್ಥಿ, ದಸರಾ, ದೀಪಾವಳಿ ಹಬ್ಬಗಳ ಸೀಸನ್) ಕೊಬ್ಬರಿಗೆ ಭಾರಿ ಬೇಡಿಕೆ.",
        worstTime: "ಮಾರ್ಚ್ ನಿಂದ ಮೇ ಬೇಸಿಗೆ ತಿಂಗಳುಗಳಲ್ಲಿ ತೆಂಗಿನಕಾಯಿ ಆವಕ ಹೆಚ್ಚಾಗಿ ದರ ತಗ್ಗುತ್ತದೆ.",
        strategy: "ತಿಪಟೂರು ಉಂಡೆ ಕೊಬ್ಬರಿಯನ್ನು ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ ಗೋದಾಮಿನಲ್ಲಿಟ್ಟು ಹಬ್ಬದ ಸೀಸನ್‌ನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹12,000 / ಕ್ವಿಂಟಾಲ್ (Ball Copra MSP)",
        cagr: "+117.6% (ಲಾಭದಾಯಕ ಬೆಳವಣಿಗೆ)"
      },

      cotton: {
        name: "ಹತ್ತಿ (Cotton - DCH/Bt)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 4800 },
          { year: "2018", price: 5400 },
          { year: "2020", price: 5600 },
          { year: "2022", price: 10500 },
          { year: "2024", price: 7400 },
          { year: "2026", price: 7800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಅಕ್ಟೋ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ನವೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಮೇ ನಿಂದ ಜುಲೈ ತಿಂಗಳುಗಳಲ್ಲಿ ಜಿನ್ನಿಂಗ್ ಗಿರಣಿಗಳಿಂದ ಉತ್ತಮ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಅಕ್ಟೋಬರ್ ನಿಂದ ಡಿಸೆಂಬರ್ ಕೊಯ್ಲು ಸೀಸನ್‌ನಲ್ಲಿ ಆವಕ ಹೆಚ್ಚಿರುತ್ತದೆ.",
        strategy: "ತೇವಾಂಶ 8% ಗಿಂತ ಕಡಿಮೆ ಇರುವಂತೆ ಒಣಗಿಸಿ ಗ್ರೇಡಿಂಗ್ ಮಾಡಿ ಮಂಡಿಗೆ ತನ್ನಿ.",
        msp: "₹7,521 / ಕ್ವಿಂಟಾಲ್ (Medium Staple MSP)",
        cagr: "+62.5% (ಉತ್ತಮ ಬೆಳವಣಿಗೆ)"
      },

      paddy: {
        name: "ಸೋನಾ ಮಸೂರಿ ಭತ್ತ (Paddy)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 1550 },
          { year: "2018", price: 1850 },
          { year: "2020", price: 2100 },
          { year: "2022", price: 2450 },
          { year: "2024", price: 2850 },
          { year: "2026", price: 3100 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಜುಲೈ ನಿಂದ ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಹಳೇ ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿಗೆ ಭಾರಿ ಪ್ರೀಮಿಯಂ ದರ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿಯಲ್ಲಿ ಹೊಸ ಭತ್ತ ಬಂದಾಗ ಬೆಲೆ ಕನಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿರುತ್ತದೆ.",
        strategy: "ಭತ್ತವನ್ನು ಕನಿಷ್ಠ 6 ತಿಂಗಳು ಸುರಕ್ಷಿತವಾಗಿ ದಾಸ್ತಾನು ಇಟ್ಟು ಹಳೆಯದಾದ ನಂತರ ಮಾರಿದರೆ 35% ಹೆಚ್ಚು ದರ ಸಿಗುತ್ತದೆ.",
        msp: "₹2,320 / ಕ್ವಿಂಟಾಲ್ (Grade A MSP)",
        cagr: "+100.0% (ದ್ವಿಗುಣಗೊಂಡ ದರ)"
      },

      ragi: {
        name: "ರಾಗಿ (Finger Millet / Ragi)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 1900 },
          { year: "2018", price: 2897 },
          { year: "2020", price: 3295 },
          { year: "2022", price: 3578 },
          { year: "2024", price: 4290 },
          { year: "2026", price: 4600 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಮೇ ನಿಂದ ಜುಲೈ ತಿಂಗಳುಗಳಲ್ಲಿ ನಗರ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಬೇಡಿಕೆ ಗರಿಷ್ಠವಾಗಿರುತ್ತದೆ.",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ ಕೊಯ್ಲಿನ ಸಮಯದಲ್ಲಿ.",
        strategy: "ಸರ್ಕಾರದ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಗಳಲ್ಲಿ ನೋಂದಾಯಿಸಿ ₹4,290 ದರದಲ್ಲಿ ನೇರವಾಗಿ ಮಾರಾಟ ಮಾಡುವುದು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ.",
        msp: "₹4,290 / ಕ್ವಿಂಟಾಲ್ (ಸರ್ಕಾರಿ ಖರೀದಿ)",
        cagr: "+142.1% (ಬೆಂಬಲ ಬೆಲೆ ಆಧಾರಿತ ಭಾರಿ ಏರಿಕೆ)"
      },

      tomato: {
        name: "ಟೊಮ್ಯಾಟೋ (Tomato)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 1100 },
          { year: "2018", price: 1600 },
          { year: "2020", price: 2100 },
          { year: "2022", price: 3200 },
          { year: "2023", price: 12000 },
          { year: "2024", price: 4200 },
          { year: "2026", price: 2600 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ (ಮಳೆಗಾಲದ ಕೊರತೆ ಸಮಯದಲ್ಲಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹8,000 ವರೆಗೆ ಏರಿಕೆ).",
        worstTime: "ಡಿಸೆಂಬರ್ ನಿಂದ ಫೆಬ್ರವರಿ ಚಳಿಗಾಲದಲ್ಲಿ ಎಲ್ಲೆಡೆ ಭರಪೂರ ಬೆಳೆ ಬಂದಾಗ ಬೆಲೆ ₹500 ಕ್ಕೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಮೇ ತಿಂಗಳಲ್ಲಿ ನಾಟಿ ಮಾಡಿ ಜುಲೈನಲ್ಲಿ ಕೊಯ್ಲಿಗೆ ಬರುವಂತೆ ಯೋಜಿಸಿದರೆ ಗರಿಷ್ಠ ಆದಾಯ ಗಳಿಸಬಹುದು.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ (ಅಲ್ಪಾವಧಿ ಬೆಳೆ)",
        cagr: "ವಿಪರೀತ ಏರಿಳಿತ (High Volatility)"
      },

      onion: {
        name: "ಈರುಳ್ಳಿ (Onion)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        history: [
          { year: "2016", price: 1200 },
          { year: "2018", price: 1800 },
          { year: "2020", price: 3200 },
          { year: "2022", price: 2400 },
          { year: "2024", price: 3800 },
          { year: "2026", price: 3200 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜೂನ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಅಕ್ಟೋಬರ್ ಮತ್ತು ನವೆಂಬರ್ (ದೀಪಾವಳಿ ಸಮಯದಲ್ಲಿ ಹಳೇ ದಾಸ್ತಾನು ಮುಗಿದು ಹೊಸ ಮಾಲು ಬರುವ ಮಧ್ಯಂತರ ಅವಧಿ).",
        worstTime: "ಫೆಬ್ರವರಿ ನಿಂದ ಏಪ್ರಿಲ್ ಮಹಾರಾಷ್ಟ್ರ ಮತ್ತು ಕರ್ನಾಟಕದ ರಬಿ ಈರುಳ್ಳಿ ಮಾರುಕಟ್ಟೆ ತುಂಬಿದಾಗ.",
        strategy: "ಗಾಳಿ ಆಡುವ ವಿಶೇಷ ಈರುಳ್ಳಿ ಶೆಡ್‌ಗಳಲ್ಲಿ (Kanda Chawl) ಸಂಗ್ರಹಿಸಿ ಅಕ್ಟೋಬರ್‌ನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+166.7% (ಉತ್ತಮ ಬೆಳವಣಿಗೆ)"
      }
    };

    let currentMode = 'live';
    let chartInstance = null;
    let apmcData = [];
    let currentCat = 'all';

    function switchMode(mode) {
      currentMode = mode;
      document.getElementById('tab-live').classList.toggle('active', mode === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', mode === 'analyzer');
      document.getElementById('view-live').style.display = mode === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = mode === 'analyzer' ? 'block' : 'none';
      
      if (mode === 'analyzer') {
        updateCropAnalysis();
      }
    }

    function updateCropAnalysis() {
      const select = document.getElementById('analyzer-crop-select');
      const cropKey = select.value;
      const data = CROP_ANALYZER_DB[cropKey] || CROP_ANALYZER_DB['arecanut'];

      document.getElementById('chart-heading').textContent = `${data.name} — 10 ವರ್ಷಗಳ ಬೆಲೆ ಇತಿಹಾಸ (2016–2026 ₹/${data.unit})`;
      document.getElementById('adv-best-time').textContent = data.bestTime;
      document.getElementById('adv-worst-time').textContent = data.worstTime;
      document.getElementById('adv-strategy').textContent = data.strategy;
      document.getElementById('adv-msp').textContent = data.msp;
      document.getElementById('adv-cagr').textContent = data.cagr;

      // Render 12-Month Heatmap
      const heatmapGrid = document.getElementById('season-heatmap-grid');
      heatmapGrid.innerHTML = '';
      data.seasonality.forEach(s => {
        const cell = document.createElement('div');
        cell.className = `heat-cell ${s.status}`;
        cell.innerHTML = `<div>${s.m}</div><div style="font-size:9px; opacity:0.9;">${s.lbl}</div>`;
        heatmapGrid.appendChild(cell);
      });

      // Render Chart.js
      renderTrendChart(data);
    }

    function renderTrendChart(crop) {
      const ctx = document.getElementById('cropTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      const labels = crop.history.map(h => h.year);
      const prices = crop.history.map(h => h.price);

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: `ಸರಾಸರಿ ದರ (₹/${crop.unit})`,
            data: prices,
            borderColor: '#15803D',
            backgroundColor: 'rgba(21, 128, 61, 0.12)',
            fill: true,
            tension: 0.35,
            borderWidth: 3,
            pointBackgroundColor: '#14532D',
            pointRadius: 5,
            pointHoverRadius: 7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: function(ctx) {
                  return ` ದರ: ₹${ctx.parsed.y.toLocaleString('en-IN')} / ${crop.unit}`;
                }
              }
            }
          },
          scales: {
            y: {
              ticks: {
                callback: function(v) { return '₹' + v.toLocaleString('en-IN'); },
                font: { family: 'Inter', size: 11 }
              },
              grid: { color: '#E2E8F0' }
            },
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Inter', size: 11, weight: 'bold' } }
            }
          }
        }
      });
    }

    // ══════════════════════════════════════════════════════
    // LIVE APMC DATA LOADER & RENDERING
    // ══════════════════════════════════════════════════════
    function init() {
      fetch('/data/apmc_prices.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          let list = [];
          if (data && data.items && Array.isArray(data.items)) {
            list = data.items;
          } else if (data && data.payload && typeof window.decryptPayload === 'function') {
            const dec = window.decryptPayload(data.payload);
            list = Array.isArray(dec) ? dec : (dec.items || []);
          } else if (Array.isArray(data)) {
            list = data;
          }

          if (list && list.length > 0) {
            apmcData = list;
            populateDropdowns();
            filterData(true);
            updateSummaryStats(list);
          }
        })
        .catch(e => console.warn("APMC Data load:", e));
    }

    function updateSummaryStats(list) {
      document.getElementById('stat-total-records').textContent = list.length.toLocaleString('en-IN');
      const sum = list.reduce((acc, curr) => acc + (curr.avg || 0), 0);
      const avg = Math.round(sum / list.length);
      document.getElementById('stat-avg-price').textContent = `₹${avg.toLocaleString('en-IN')}`;

      const top = list.reduce((maxItem, item) => (item.avg > maxItem.avg ? item : maxItem), list[0]);
      if (top) {
        document.getElementById('stat-top-crop').textContent = `₹${top.avg.toLocaleString('en-IN')}`;
      }
    }

    function populateDropdowns() {
      const selectMandi = document.getElementById('market-select');
      const markets = [...new Set(apmcData.map(d => d.market))].filter(Boolean).sort();
      selectMandi.innerHTML = '<option value="all">🏪 ಎಲ್ಲಾ ಮಾರುಕಟ್ಟೆಗಳು (All 174 Mandis)</option>';
      markets.forEach(m => {
        const opt = document.createElement('option');
        opt.value = m;
        opt.textContent = `${m} APMC`;
        selectMandi.appendChild(opt);
      });

      const selectComm = document.getElementById('commodity-select');
      const commodities = [...new Set(apmcData.map(d => (d.cropKn || d.cropEn || d.crop).split('/')[0].trim()))].filter(Boolean).sort();
      selectComm.innerHTML = '<option value="all">🌾 ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳು (All Commodities)</option>';
      commodities.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        selectComm.appendChild(opt);
      });
    }

    function setCategory(cat, btn) {
      document.querySelectorAll('.cat-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCat = cat;
      filterData(true);
    }

    function filterData(reset) {
      const marketFilter = document.getElementById('market-select').value;
      const commodityFilter = document.getElementById('commodity-select').value;
      const searchTxt = document.getElementById('apmc-search').value.toLowerCase().trim();

      let filtered = apmcData;

      if (currentCat !== 'all') {
        filtered = filtered.filter(d => d.cat === currentCat);
      }
      if (marketFilter !== 'all') {
        filtered = filtered.filter(d => d.market === marketFilter);
      }
      if (commodityFilter !== 'all') {
        filtered = filtered.filter(d => 
          (d.cropKn && d.cropKn.includes(commodityFilter)) ||
          (d.cropEn && d.cropEn.toLowerCase().includes(commodityFilter.toLowerCase())) ||
          (d.crop && d.crop.includes(commodityFilter))
        );
      }
      if (searchTxt) {
        filtered = filtered.filter(d => 
          (d.crop && d.crop.toLowerCase().includes(searchTxt)) ||
          (d.cropKn && d.cropKn.toLowerCase().includes(searchTxt)) ||
          (d.cropEn && d.cropEn.toLowerCase().includes(searchTxt)) ||
          (d.market && d.market.toLowerCase().includes(searchTxt)) ||
          (d.variety && d.variety.toLowerCase().includes(searchTxt))
        );
      }

      renderGrid(filtered);
    }

    function renderGrid(list) {
      const grid = document.getElementById('apmc-card-grid');
      grid.innerHTML = '';

      if (list.length === 0) {
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:40px; color:#64748b; font-weight:700;">ಯಾವುದೇ ಫಲಿತಾಂಶ ಕಂಡುಬಂದಿಲ್ಲ.</div>';
        return;
      }

      const displayList = list.slice(0, 150); // Clean rendering limit
      displayList.forEach(item => {
        const cropName = item.cropKn || item.cropEn || item.crop;
        const variety = item.variety || 'ಸಾಮಾನ್ಯ';
        const modalPrice = item.avg ? `₹${item.avg.toLocaleString('en-IN')}` : '—';
        const minPrice = item.min ? `₹${item.min.toLocaleString('en-IN')}` : '—';
        const maxPrice = item.max ? `₹${item.max.toLocaleString('en-IN')}` : '—';
        const arrivals = item.arrivals ? `${item.arrivals} ಕ್ವಿಂಟಾಲ್` : 'ಮಂಡಿ ಲೈವ್';

        const card = document.createElement('div');
        card.className = 'mandi-card';
        card.innerHTML = `
          <div>
            <div class="mc-header">
              <div>
                <div class="mc-crop-name">${cropName}</div>
                <div class="mc-mandi">📍 ${item.market} APMC (${item.district || 'ಕರ್ನಾಟಕ'})</div>
              </div>
              <span style="font-size:11px; background:#E2E8F0; padding:2px 8px; border-radius:12px; font-weight:700;">${variety}</span>
            </div>
            
            <div class="mc-price-box">
              <div style="font-size:11px; color:#15803D; font-weight:800;">ಇಂದಿನ ಮಾದರಿ ದರ (Modal Price)</div>
              <div class="mc-modal-price">${modalPrice}</div>
              <div class="mc-unit">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ (100 Kg)</div>
            </div>

            <div class="mc-range-grid">
              <div>ಕನಿಷ್ಠ: <span class="mc-range-val">${minPrice}</span></div>
              <div style="text-align:right;">ಗರಿಷ್ಠ: <span class="mc-range-val">${maxPrice}</span></div>
              <div style="grid-column:1/-1; margin-top:2px; font-size:11px;">ಆವಕ: <span style="font-weight:700; color:#1e293b;">${arrivals}</span></div>
            </div>
          </div>

          <button class="mc-share-btn" onclick="shareWhatsApp('${cropName}', '${item.market}', '${modalPrice}', '${minPrice}', '${maxPrice}')">
            <span>📲 WhatsApp ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ</span>
          </button>
        `;
        grid.appendChild(card);
      });
    }

    function shareWhatsApp(crop, market, modal, min, max) {
      const text = `🌾 *Karnata.in — APMC ಮಾರುಕಟ್ಟೆ ದರ*\\n\\nಬೆಳೆ: *${crop}*\\nಮಾರುಕಟ್ಟೆ: *${market} APMC*\\nಇಂದಿನ ಮಾದರಿ ದರ: *${modal} / ಕ್ವಿಂಟಾಲ್*\\nಕನಿಷ್ಠ: ${min} | ಗರಿಷ್ಠ: ${max}\\n\\nಎಲ್ಲಾ 174 APMC ಮಾರುಕಟ್ಟೆಗಳ ಲೈವ್ ದರ ಹಾಗೂ 10 ವರ್ಷಗಳ ಬೆಲೆ ಮುನ್ಸೂಚನೆ ವೀಕ್ಷಿಸಿ:\\nhttps://karnata.in/apmc-prices.html`;
      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(text), '_blank');
    }

    document.addEventListener('DOMContentLoaded', () => {
      init();
    });
  </script>
</body>
</html>
"""

with open('apmc-prices.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS_REBUILT_FULL_APMC_PRICES_HTML")
