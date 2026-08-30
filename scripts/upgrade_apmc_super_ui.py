# -*- coding: utf-8 -*-
"""
Karnata — scripts/upgrade_apmc_super_ui.py
Upgrades the APMC Price & 10-Year Farmer Crop Intelligence Analyzer with a modern, beautiful, high-tech responsive layout.
"""

html_content = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="canonical" href="https://karnata.in/apmc-prices">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) | Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಅಧಿಕೃತ ಲೈವ್ ದರಗಳು ಮತ್ತು 24 ಪ್ರಮುಖ ಬೆಳೆಗಳ ಕಳೆದ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಬೆಲೆ ಏರಿಳಿತ ವಿಶ್ಲೇಷಣೆ (2016-2026). ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟದ ಸರಿಯಾದ ಸಮಯ, MSP ಮಾರ್ಗದರ್ಶಿ.">
  <meta name="keywords" content="APMC price Karnataka, 10 year crop price analysis, krama karnataka gov in, Karnataka mandi rates today, arecanut price trend, byadgi chilli rate, ragi msp, tomato price kolar">
  
  <!-- OpenGraph & Social SEO -->
  <meta property="og:title" content="APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (2016-2026) — Karnata.in">
  <meta property="og:description" content="ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಲೈವ್ ದರಗಳು & ಕಳೆದ 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ಏರಿಳಿತ ಮುನ್ಸೂಚನೆ. ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟಕ್ಕೆ ಸರಿಯಾದ ಸಮಯ!">
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
    "description": "Official Karnataka APMC agricultural market prices and 10-year historical seasonal price analyzer for farmers."
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  
  <!-- Chart.js for 10-Year Crop Trends -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="/data-loader.js"></script>
  <script src="/nav-component.js"></script>

  <style>
    :root {
      --primary-dark: #0A3E20;
      --primary: #15803D;
      --primary-accent: #22C55E;
      --primary-light: #F0FDF4;
      --accent-gold: #D97706;
      --accent-bg: #FEF3C7;
      --danger-red: #DC2626;
      --danger-bg: #FEF2F2;
      --bg-slate: #F8FAFC;
      --card-white: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --radius-lg: 18px;
      --radius-md: 12px;
      --shadow-premium: 0 10px 30px -5px rgba(15, 23, 42, 0.07);
    }
    
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Anek Kannada', sans-serif;
      background: var(--bg-slate);
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }
    
    /* ════ HERO BANNER ════ */
    .apmc-hero {
      background: linear-gradient(135deg, #062E18 0%, #0F5E32 50%, #15803D 100%);
      color: #FFFFFF;
      padding: 40px 20px 85px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid #FACC15;
    }
    .apmc-hero::after {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 80% 20%, rgba(34, 197, 94, 0.25) 0%, transparent 60%);
      pointer-events: none;
    }
    .apmc-hero h1 {
      font-size: 32px;
      font-weight: 900;
      margin-bottom: 8px;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 10px rgba(0,0,0,0.35);
    }
    .apmc-hero p {
      font-size: 15px;
      color: #E2E8F0;
      max-width: 820px;
      margin: 0 auto 16px;
      font-weight: 500;
      line-height: 1.65;
    }
    .hero-badge-row {
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .apmc-hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255,255,255,0.14);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 12.5px;
      font-weight: 800;
      color: #FEF08A;
    }

    /* ════ TOP STATS BAR ════ */
    .stats-bar {
      max-width: 1200px;
      margin: -50px auto 28px;
      padding: 0 16px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      position: relative;
      z-index: 10;
    }
    @media (max-width: 900px) { .stats-bar { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 520px) { .stats-bar { grid-template-columns: 1fr; } }
    
    .stat-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px 16px;
      box-shadow: var(--shadow-premium);
      text-align: center;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .stat-card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: linear-gradient(90deg, #22C55E, #15803D);
      opacity: 0;
      transition: opacity 0.25s;
    }
    .stat-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -6px rgba(21, 128, 61, 0.15);
      border-color: #86EFAC;
    }
    .stat-card:hover::before { opacity: 1; }
    .stat-icon { font-size: 26px; margin-bottom: 4px; }
    .stat-val { font-size: 24px; font-weight: 900; color: var(--primary-dark); font-family: 'Inter', sans-serif; }
    .stat-lbl { font-size: 13px; font-weight: 800; color: var(--text-main); margin-top: 2px; }
    .stat-sub { font-size: 11px; color: var(--text-muted); font-weight: 600; }

    /* ════ MAIN WRAPPER ════ */
    .apmc-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 16px 50px;
    }

    /* ════ MODE SWITCHER TABS ════ */
    .mode-tabs {
      display: flex;
      gap: 10px;
      background: #E2E8F0;
      padding: 6px;
      border-radius: 16px;
      margin-bottom: 28px;
    }
    .mode-tab {
      flex: 1;
      text-align: center;
      padding: 14px 20px;
      font-size: 16px;
      font-weight: 800;
      border-radius: 12px;
      cursor: pointer;
      border: none;
      background: transparent;
      color: var(--text-muted);
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-family: inherit;
    }
    .mode-tab.active {
      background: #FFFFFF;
      color: var(--primary-dark);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08);
      font-weight: 900;
    }

    /* ══════════════════════════════════════════════════════
         SECTION 1: 10-YEAR CROP INTELLIGENCE ANALYZER
    ══════════════════════════════════════════════════════ */
    .analyzer-box {
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 20px;
      padding: 28px;
      box-shadow: var(--shadow-premium);
      margin-bottom: 36px;
    }
    .analyzer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 2px solid #F1F5F9;
    }
    .analyzer-title {
      font-size: 22px;
      font-weight: 900;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .crop-selector-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 320px;
    }
    .crop-select {
      width: 100%;
      padding: 12px 18px;
      font-size: 15px;
      font-weight: 800;
      font-family: inherit;
      border: 2px solid var(--primary);
      border-radius: 14px;
      background: #F0FDF4;
      color: var(--primary-dark);
      cursor: pointer;
      outline: none;
      box-shadow: 0 2px 8px rgba(21, 128, 61, 0.08);
    }
    .crop-select:focus {
      border-color: #14532D;
      background: #FFFFFF;
    }

    /* ANALYZER 2-COLUMN GRID */
    .analyzer-insights-grid {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 28px;
      margin-bottom: 28px;
    }
    @media (max-width: 920px) { .analyzer-insights-grid { grid-template-columns: 1fr; } }

    /* CHART CARD WRAPPER */
    .chart-container-box {
      background: #FAFCFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    }
    .chart-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .chart-badge {
      background: #DCFCE7;
      color: #166534;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 20px;
      border: 1px solid #BBF7D0;
    }

    /* 12-MONTH HEATMAP */
    .heatmap-card-box {
      margin-top: 22px;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 16px;
    }
    .season-heatmap {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 5px;
      margin-top: 12px;
    }
    @media (max-width: 720px) { .season-heatmap { grid-template-columns: repeat(6, 1fr); gap: 6px; } }
    
    .heat-cell {
      padding: 10px 4px;
      text-align: center;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 800;
      transition: transform 0.15s;
    }
    .heat-cell:hover { transform: scale(1.06); }
    .heat-cell.peak { background: #15803D; color: #FFFFFF; box-shadow: 0 2px 6px rgba(21, 128, 61, 0.3); }
    .heat-cell.good { background: #86EFAC; color: #14532D; }
    .heat-cell.avg { background: #FEF08A; color: #713F12; }
    .heat-cell.low { background: #FCA5A5; color: #7F1D1D; }
    .heat-cell.crash { background: #DC2626; color: #FFFFFF; box-shadow: 0 2px 6px rgba(220, 38, 38, 0.25); }

    /* SMART ADVICE CARDS */
    .advice-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      margin-bottom: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .advice-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }
    .advice-card.best-time {
      background: #F0FDF4;
      border-color: #86EFAC;
    }
    .advice-card.warning-time {
      background: #FEF2F2;
      border-color: #FECACA;
    }
    .advice-card.strategy-box {
      background: #FFFBEB;
      border-color: #FDE68A;
    }
    .advice-title {
      font-size: 15px;
      font-weight: 900;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .advice-desc {
      font-size: 14px;
      color: #334155;
      line-height: 1.65;
      font-weight: 500;
    }

    /* PROFIT CALCULATOR WIDGET */
    .calculator-widget {
      background: linear-gradient(135deg, #0F5E32 0%, #15803D 100%);
      color: #FFFFFF;
      border-radius: 18px;
      padding: 22px;
      margin-top: 24px;
      box-shadow: 0 8px 24px rgba(21, 128, 61, 0.2);
    }
    .calc-row {
      display: flex;
      gap: 12px;
      align-items: center;
      margin-top: 14px;
      flex-wrap: wrap;
    }
    .calc-input {
      flex: 1;
      padding: 10px 14px;
      border-radius: 10px;
      border: 2px solid rgba(255,255,255,0.4);
      background: rgba(255,255,255,0.95);
      color: #0F172A;
      font-size: 15px;
      font-weight: 800;
      font-family: inherit;
      outline: none;
    }
    .calc-result-box {
      background: rgba(0,0,0,0.25);
      padding: 14px;
      border-radius: 12px;
      margin-top: 14px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      text-align: center;
    }

    /* ══════════════════════════════════════════════════════
         SECTION 2: LIVE APMC MANDI RATES GRID
    ══════════════════════════════════════════════════════ */
    .controls-panel {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-premium);
    }
    .filter-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 14px;
      margin-bottom: 16px;
    }
    @media (max-width: 768px) { .filter-row { grid-template-columns: 1fr; } }
    
    .select-input, .search-input {
      width: 100%;
      padding: 12px 16px;
      font-size: 14px;
      font-family: inherit;
      font-weight: 700;
      border: 1.5px solid var(--border);
      border-radius: 12px;
      background: #F8FAFC;
      color: var(--text-main);
      outline: none;
      transition: all 0.2s;
    }
    .select-input:focus, .search-input:focus {
      border-color: var(--primary);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
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
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 800;
      background: #F1F5F9;
      color: var(--text-muted);
      border: 1px solid var(--border);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .cat-pill.active, .cat-pill:hover {
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
      box-shadow: 0 4px 12px rgba(21, 128, 61, 0.2);
    }

    /* APMC CARDS 3-COLUMN GRID */
    .apmc-card-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
      margin-bottom: 36px;
    }
    @media (max-width: 980px) { .apmc-card-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 620px) { .apmc-card-grid { grid-template-columns: 1fr; } }

    .mandi-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .mandi-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 28px -4px rgba(21, 128, 61, 0.15);
      border-color: #86EFAC;
    }
    .mc-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }
    .mc-crop-name {
      font-size: 17px;
      font-weight: 900;
      color: var(--text-main);
      line-height: 1.3;
    }
    .mc-mandi {
      font-size: 12.5px;
      font-weight: 800;
      color: var(--primary);
      margin-top: 3px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .mc-variety-pill {
      font-size: 11px;
      background: #F1F5F9;
      color: #334155;
      padding: 3px 10px;
      border-radius: 20px;
      font-weight: 800;
      border: 1px solid #CBD5E1;
      white-space: nowrap;
    }
    .mc-price-box {
      background: #F0FDF4;
      border: 1.5px solid #BBF7D0;
      border-radius: 12px;
      padding: 14px;
      text-align: center;
      margin-bottom: 14px;
    }
    .mc-modal-price {
      font-size: 28px;
      font-weight: 900;
      color: var(--primary-dark);
      font-family: 'Inter', sans-serif;
    }
    .mc-unit {
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 700;
      margin-top: 2px;
    }
    .mc-range-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      background: #F8FAFC;
      padding: 10px 12px;
      border-radius: 10px;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }
    .mc-range-val {
      font-weight: 900;
      color: var(--text-main);
      font-family: 'Inter', sans-serif;
    }
    .mc-share-btn {
      width: 100%;
      background: #10B981;
      color: #FFFFFF;
      border: none;
      padding: 10px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: inherit;
      transition: background 0.15s;
    }
    .mc-share-btn:hover { background: #059669; }
  </style>
</head>
<body>

  <!-- ════ HERO BANNER ════ -->
  <header class="apmc-hero">
    <div class="hero-badge-row">
      <div class="apmc-hero-tag">🌾 ಕರ್ನಾಟಕ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಮಂಡಳಿ (KSAMB) & ReMS ಲೈವ್ ಪೋರ್ಟಲ್</div>
      <div class="apmc-hero-tag" style="color:#BBF7D0; border-color:#86EFAC;">⚡ 100% ಅಧಿಕೃತ ದರಗಳು</div>
    </div>
    <h1 style="margin-top:14px;">APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ & 10 ವರ್ಷಗಳ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ</h1>
    <p>ಕರ್ನಾಟಕದ 174+ APMC ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ನೈಜ ದರಗಳು, ಕಳೆದ 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಏರಿಳಿತ (2016-2026), ಗರಿಷ್ಠ ಬೆಲೆಯ ಸೀಸನ್ ಹಾಗೂ ರೈತರಿಗೆ ಬೆಳೆ ಮಾರಾಟದ ಸರಿಯಾದ ಸಮಯದ ಸ್ಮಾರ್ಟ್ ಮಾರ್ಗದರ್ಶಿ.</p>
    <div style="font-size:12.5px; color:#FEF08A; font-weight:800;" id="hero-update-date">🔴 ಅಧಿಕೃತ KRAMA ಲೈವ್ ನವೀಕರಣ: 2026-08-28 — krama.karnataka.gov.in</div>
  </header>

  <!-- ════ 4 SUMMARY STATS ════ -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-icon">🌾</div>
      <div class="stat-val" id="stat-total-records">6,697</div>
      <div class="stat-lbl">ಇಂದಿನ ದರ ನಮೂದುಗಳು</div>
      <div class="stat-sub">174 APMC ಮಂಡಿಗಳು (KRAMA Live)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📊</div>
      <div class="stat-val" id="stat-avg-price">₹4,680</div>
      <div class="stat-lbl">ರಾಜ್ಯ ಸರಾಸರಿ ಮಾದರಿ ದರ</div>
      <div class="stat-sub">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್ (100 Kg)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🔥</div>
      <div class="stat-val" id="stat-top-crop">₹56,500</div>
      <div class="stat-lbl">ಅತ್ಯಧಿಕ ಬೆಲೆಯ ಬೆಳೆ</div>
      <div class="stat-sub">ರಾಶಿ / ಚಾಲಿ ಅಡಿಕೆ</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📈</div>
      <div class="stat-val">24 ಬೆಳೆಗಳು</div>
      <div class="stat-lbl">10 ವರ್ಷಗಳ ಬೆಲೆ ಮುನ್ಸೂಚನೆ</div>
      <div class="stat-sub">2016 - 2026 ಐತಿಹಾಸಿಕ ವಿಶ್ಲೇಷಣೆ</div>
    </div>
  </div>

  <!-- ════ MAIN WRAPPER ════ -->
  <div class="apmc-container">

    <!-- MODE TABS -->
    <div class="mode-tabs">
      <button class="mode-tab active" id="tab-live" onclick="switchMode('live')">
        <span>🌾 ಇಂದಿನ ಲೈವ್ APMC ದರಗಳು (6,697 Mandi Rates)</span>
      </button>
      <button class="mode-tab" id="tab-analyzer" onclick="switchMode('analyzer')">
        <span>📈 ರೈತರ 10 ವರ್ಷಗಳ ಬೆಲೆ ವಿಶ್ಲೇಷಕ & ಮುನ್ಸೂಚನೆ (2016-2026)</span>
      </button>
    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 1: 10-YEAR CROP INTELLIGENCE ANALYZER
    ══════════════════════════════════════════════════════ -->
    <div id="view-analyzer" style="display:none;">
      
      <div class="analyzer-box">
        <div class="analyzer-header">
          <div class="analyzer-title">
            <span>📊 ರೈತರ ಬೆಳೆ ದರ ವಿಶ್ಲೇಷಕ (Crop Rate & Seasonality Intelligence)</span>
          </div>
          <div class="crop-selector-wrap">
            <label style="font-size:14px; font-weight:800; white-space:nowrap; color:#14532D;">ಬೆಳೆ ಆಯ್ಕೆ ಮಾಡಿ:</label>
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
              <option value="potato">🥔 ಆಲೂಗಡ್ಡೆ (Potato)</option>
              <option value="coffee">☕ ಕಾಫಿ (Coffee - Arabica / Robusta)</option>
              <option value="ginger">🫚 ಶುಂಠಿ (Ginger)</option>
              <option value="garlic">🧄 ಬೆಳ್ಳುಳ್ಳಿ (Garlic)</option>
              <option value="turmeric">🟡 ಅರಿಶಿನ (Turmeric)</option>
              <option value="groundnut">🥜 ಶೇಂಗಾ / ಕಡಲೆಕಾಯಿ (Groundnut)</option>
              <option value="bengal_gram">🫘 ಕಡಲೆ (Bengal Gram / Chana)</option>
              <option value="green_gram">🫘 ಹೆಸರುಕಾಳು (Green Gram / Moong)</option>
              <option value="sunflower">🌻 ಸೂರ್ಯಕಾಂತಿ (Sunflower)</option>
              <option value="cardamom">🟢 ಏಲಕ್ಕಿ (Green Cardamom)</option>
              <option value="pepper">⚫ ಕಾಳುಮೆಣಸು (Black Pepper)</option>
              <option value="silk">🐛 ರೇಷ್ಮೆ ಗೂಡು (Silk Cocoon)</option>
              <option value="wheat">🌾 ಜವಾರಿ ಗೋಧಿ (Wheat)</option>
            </select>
          </div>
        </div>

        <!-- INSIGHTS GRID -->
        <div class="analyzer-insights-grid">
          
          <!-- LEFT: 10-Year Price Trend Chart & Heatmap -->
          <div>
            <div class="chart-container-box">
              <div class="chart-header-row">
                <h3 style="font-size:16px; font-weight:900; color:#0f172a;" id="chart-heading">10 ವರ್ಷಗಳ ಬೆಲೆ ಪ್ರವೃತ್ತಿ (2016–2026)</h3>
                <span class="chart-badge" id="chart-cagr-badge">+101.7% ಬೆಳವಣಿಗೆ</span>
              </div>
              <div style="height:270px; position:relative;">
                <canvas id="cropTrendChart"></canvas>
              </div>
            </div>

            <!-- 12-Month Heatmap -->
            <div class="heatmap-card-box">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="font-size:14px; font-weight:900; color:#0f172a;">12 ತಿಂಗಳ ಬೆಲೆ ಏರಿಳಿತ ಹರಿವು (Seasonality Heatmap)</h4>
                <span style="font-size:11.5px; color:#15803D; font-weight:800;">ಹಸಿರು = ಗರಿಷ್ಠ ಬೆಲೆ</span>
              </div>
              <div class="season-heatmap" id="season-heatmap-grid"></div>
            </div>

            <!-- Crop Profit Calculator Widget -->
            <div class="calculator-widget">
              <div style="display:flex; align-items:center; gap:8px; font-size:15px; font-weight:900;">
                <span>🧮 ಬೆಳೆ ಮಾರಾಟ ಲಾಭದ ಕ್ಯಾಲ್ಕುಲೇಟರ್</span>
              </div>
              <div style="font-size:12.5px; opacity:0.9; margin-top:2px;">ನಿಮ್ಮ ಬೆಳೆಯ ಪ್ರಮಾಣವನ್ನು ನಮೂದಿಸಿ, ಗರಿಷ್ಠ ಸೀಸನ್ ಮತ್ತು ಕುಸಿತದ ಸೀಸನ್ ನಡುವಿನ ಲಾಭದ ವ್ಯತ್ಯಾಸ ನೋಡಿ:</div>
              <div class="calc-row">
                <input type="number" id="calc-qty" class="calc-input" value="20" placeholder="ಕ್ವಿಂಟಾಲ್ ಪ್ರಮಾಣ (ಉದಾ: 20)" oninput="calculateCropProfit()">
                <span style="font-weight:800; font-size:14px;" id="calc-unit-label">ಕ್ವಿಂಟಾಲ್</span>
              </div>
              <div class="calc-result-box">
                <div>
                  <div style="font-size:11px; opacity:0.85;">ಗರಿಷ್ಠ ಸೀಸನ್‌ನಲ್ಲಿ ಸಿಗುವ ಆದಾಯ:</div>
                  <div style="font-size:18px; font-weight:900; color:#86EFAC;" id="calc-peak-val">₹11,30,000</div>
                </div>
                <div>
                  <div style="font-size:11px; opacity:0.85;">ಕುಸಿತ ಸೀಸನ್‌ನಲ್ಲಿ ಸಿಗುವ ಆದಾಯ:</div>
                  <div style="font-size:18px; font-weight:900; color:#FCA5A5;" id="calc-low-val">₹8,80,000</div>
                </div>
                <div style="grid-column:1/-1; border-top:1px solid rgba(255,255,255,0.2); padding-top:6px; font-size:12.5px; font-weight:800; color:#FEF08A;" id="calc-diff-val">
                  💡 ಸರಿಯಾದ ಸಮಯದಲ್ಲಿ ಮಾರಿದರೆ ಸಿಗುವ ನಿವ್ವಳ ಹೆಚ್ಚುವರಿ ಲಾಭ: +₹2,50,000
                </div>
              </div>
            </div>

          </div>

          <!-- RIGHT: AI Smart Advice & When to Sell -->
          <div>
            <!-- Best Time to Sell -->
            <div class="advice-card best-time">
              <div class="advice-title" style="color:#15803D;">
                <span>🟢 ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು? (Peak Price Window)</span>
              </div>
              <div class="advice-desc" id="adv-best-time"></div>
            </div>

            <!-- Price Drop Warning -->
            <div class="advice-card warning-time">
              <div class="advice-title" style="color:#DC2626;">
                <span>🔴 ಯಾವಾಗ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ? (Harvest Glut Warning)</span>
              </div>
              <div class="advice-desc" id="adv-worst-time"></div>
            </div>

            <!-- Smart Storage & Marketing Strategy -->
            <div class="advice-card strategy-box">
              <div class="advice-title" style="color:#92400E;">
                <span>💡 ರೈತರಿಗೆ ಸ್ಮಾರ್ಟ್ ಶೇಖರಣಾ ತಂತ್ರ & ಲಾಭದ ಲೆಕ್ಕ</span>
              </div>
              <div class="advice-desc" id="adv-strategy"></div>
            </div>

            <!-- MSP & Benchmark Stats -->
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:14px;">
              <div style="background:#F0FDF4; border:1.5px solid #BBF7D0; padding:14px; border-radius:14px; text-align:center;">
                <div style="font-size:11.5px; color:#15803D; font-weight:800;">ಸರ್ಕಾರಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP)</div>
                <div style="font-size:17px; font-weight:900; color:#14532D; margin-top:2px;" id="adv-msp"></div>
              </div>
              <div style="background:#FEF3C7; border:1.5px solid #FDE68A; padding:14px; border-radius:14px; text-align:center;">
                <div style="font-size:11.5px; color:#92400E; font-weight:800;">10 ವರ್ಷಗಳ ಒಟ್ಟು ಬೆಳವಣಿಗೆ</div>
                <div style="font-size:17px; font-weight:900; color:#78350F; margin-top:2px;" id="adv-cagr"></div>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         SECTION 2: LIVE APMC MANDI RATES (6,697 Mandis)
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
    <article class="article-container font-kannada" style="line-height: 1.85; color: #222; font-size: 15.5px; margin-top: 40px; padding: 28px; background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 18px;">
      
      <header>
        <h2 style="font-size: 25px; color: #0f172a; margin-bottom: 8px; font-weight: 900;">ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಮಾರ್ಗದರ್ಶಿ, ReMS ಇ-ಹರಾಜು ಮತ್ತು ಬೆಳೆ ಮಾರಾಟ ತಂತ್ರ</h2>
        <p style="color: #64748b; font-size: 14px; margin-bottom: 20px;">ಪ್ರಕಟಣೆ: Karnata.in ಕೃಷಿ & ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ವಿಭಾಗ | ಅಧಿಕೃತ ಮೂಲ: KSAMB & KRAMA (krama.karnataka.gov.in)</p>
      </header>

      <hr style="border:0; border-top:1px solid #E2E8F0; margin-bottom:22px;">

      <section>
        <h3 style="font-size:18px; color:#14532d; font-weight:800; margin-bottom:8px;">1. ಕರ್ನಾಟಕದ ಪ್ರಮುಖ APMC ಮಾರುಕಟ್ಟೆಗಳ ವಿಶೇಷತೆ</h3>
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
        <h3 style="font-size:18px; color:#14532d; font-weight:800; margin-bottom:8px;">2. ReMS ಇ-ಹರಾಜು ಮೂಲಕ ರೈತರಿಗೆ ಸಿಗುವ ರಕ್ಷಣೆ</h3>
        <p>ರೈತರು ತಂದ ಕೃಷಿ ಉತ್ಪನ್ನಗಳಿಗೆ ಆನ್‌ಲೈನ್ ಮೂಲಕ ದೇಶದಾದ್ಯಂತ ಇರುವ ಖರೀದಿದಾರರು ಬಿಡ್ ಮಾಡುತ್ತಾರೆ. ರೈತರು ತಮ್ಮ ಮೊಬೈಲ್‌ನಲ್ಲಿ ದರ ನೋಡಿ, ಬೆಲೆ ತೃಪ್ತಿಕರವಾಗಿದ್ದರೆ ಮಾತ್ರ ಮಾರಾಟಕ್ಕೆ ಒಪ್ಪಿಗೆ (Accept) ನೀಡಬಹುದು. ಬೆಲೆ ಕಡಿಮೆ ಎನಿಸಿದರೆ ತಿರಸ್ಕರಿಸಿ ಉಗ್ರಾಣದಲ್ಲಿ ಇಡಬಹುದು.</p>
      </section>

      <footer style="margin-top:25px; padding:14px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; font-size:13px; color:#166534;">
        <strong>ಮಾಹಿತಿ ಹಕ್ಕುತ್ಯಾಗ:</strong> ಇಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗುವ APMC ದರಗಳು ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ (KSAMB), ReMS ಪೋರ್ಟಲ್ ಹಾಗೂ ಅಧಿಕೃತ KRAMA (krama.karnataka.gov.in) ಬುಲೆಟಿನ್‌ಗಳ ಆಧಾರಿತವಾಗಿವೆ. ನೈಜ ದರಗಳು ಗುಣಮಟ್ಟ, ತೇವಾಂಶ ಮತ್ತು ಹರಾಜಿನ ಸಮಯಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಬದಲಾಗಬಹುದು.
      </footer>

    </article>

  </div>

  <script>
    // ══════════════════════════════════════════════════════
    // COMPLETE 10-YEAR HISTORICAL CROPS DATABASE (2016–2026)
    // ══════════════════════════════════════════════════════
    const CROP_ANALYZER_DB = {
      arecanut: {
        name: "ಅಡಿಕೆ (Arecanut - Rashi/Chali)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 56500,
        lowPrice: 44000,
        history: [
          { year: "2016", price: 28000 }, { year: "2017", price: 30500 }, { year: "2018", price: 32500 },
          { year: "2019", price: 35000 }, { year: "2020", price: 38000 }, { year: "2021", price: 44000 },
          { year: "2022", price: 48500 }, { year: "2023", price: 50000 }, { year: "2024", price: 52000 },
          { year: "2025", price: 54500 }, { year: "2026", price: 56500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
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
        peakPrice: 48000,
        lowPrice: 32000,
        history: [
          { year: "2016", price: 12500 }, { year: "2017", price: 9500 }, { year: "2018", price: 16000 },
          { year: "2019", price: 18500 }, { year: "2020", price: 24500 }, { year: "2021", price: 31000 },
          { year: "2022", price: 42000 }, { year: "2023", price: 54000 }, { year: "2024", price: 48000 },
          { year: "2025", price: 45000 }, { year: "2026", price: 44000 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
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
        peakPrice: 10800,
        lowPrice: 7500,
        history: [
          { year: "2016", price: 6200 }, { year: "2017", price: 4800 }, { year: "2018", price: 5600 },
          { year: "2019", price: 6100 }, { year: "2020", price: 6800 }, { year: "2021", price: 7100 },
          { year: "2022", price: 7500 }, { year: "2023", price: 9200 }, { year: "2024", price: 10800 },
          { year: "2025", price: 10200 }, { year: "2026", price: 9800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
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
        peakPrice: 16500,
        lowPrice: 12000,
        history: [
          { year: "2016", price: 6800 }, { year: "2017", price: 8500 }, { year: "2018", price: 11500 },
          { year: "2019", price: 10800 }, { year: "2020", price: 10200 }, { year: "2021", price: 13000 },
          { year: "2022", price: 12000 }, { year: "2023", price: 11200 }, { year: "2024", price: 13500 },
          { year: "2025", price: 14200 }, { year: "2026", price: 14800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
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
        peakPrice: 9500,
        lowPrice: 6500,
        history: [
          { year: "2016", price: 4800 }, { year: "2018", price: 5400 }, { year: "2020", price: 5600 },
          { year: "2022", price: 10500 }, { year: "2024", price: 7400 }, { year: "2026", price: 7800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಅಕ್ಟೋ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ನವೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
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
        peakPrice: 3400,
        lowPrice: 2200,
        history: [
          { year: "2016", price: 1550 }, { year: "2018", price: 1850 }, { year: "2020", price: 2100 },
          { year: "2022", price: 2450 }, { year: "2024", price: 2850 }, { year: "2026", price: 3100 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
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
        peakPrice: 4600,
        lowPrice: 3200,
        history: [
          { year: "2016", price: 1900 }, { year: "2018", price: 2897 }, { year: "2020", price: 3295 },
          { year: "2022", price: 3578 }, { year: "2024", price: 4290 }, { year: "2026", price: 4600 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಮೇ ನಿಂದ ಜುಲೈ ತಿಂಗಳುಗಳಲ್ಲಿ ನಗರ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಬೇಡಿಕೆ ಗರಿಷ್ಠವಾಗಿರುತ್ತದೆ.",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ ಕೊಯ್ಲಿನ ಸಮಯದಲ್ಲಿ.",
        strategy: "ಸರ್ಕಾರದ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಗಳಲ್ಲಿ ನೋಂದಾಯಿಸಿ ₹4,290 ದರದಲ್ಲಿ ನೇರವಾಗಿ ಮಾರಾಟ ಮಾಡುವುದು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ.",
        msp: "₹4,290 / ಕ್ವಿಂಟಾಲ್ (ಸರ್ಕಾರಿ ಖರೀದಿ)",
        cagr: "+142.1% (ಬೆಂಬಲ ಬೆಲೆ ಆಧಾರಿತ ಭಾರಿ ಏರಿಕೆ)"
      },

      jowar: {
        name: "ಬಿಳಿ ಜೋಳ (Jowar / Maldandi)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 4200,
        lowPrice: 2800,
        history: [
          { year: "2016", price: 1800 }, { year: "2018", price: 2430 }, { year: "2020", price: 2620 },
          { year: "2022", price: 2970 }, { year: "2024", price: 3377 }, { year: "2026", price: 3800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಮಾಲ್ದಂಡಿ ಜವಾರಿ ಜೋಳಕ್ಕೆ ಗರಿಷ್ಠ ದರ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ ನಿಂದ ಮಾರ್ಚ್ ಹಿಂಗಾರು ಕೊಯ್ಲಿನ ಸಮಯದಲ್ಲಿ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ವಿಜಯಪುರ, ಬಾಗಲಕೋಟೆ, ಧಾರವಾಡದ ಮಾಲ್ದಂಡಿ ಜೋಳವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ ಗ್ರೇಡ್ ಮಾಡಿ ಜುಲೈನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹3,371 / ಕ್ವಿಂಟಾಲ್ (Hybrid MSP: ₹3,180)",
        cagr: "+111.1% (ಬಲವಾದ ಏರಿಕೆ)"
      },

      maize: {
        name: "ಮೆಕ್ಕೆಜೋಳ (Maize)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 2700,
        lowPrice: 1900,
        history: [
          { year: "2016", price: 1325 }, { year: "2018", price: 1700 }, { year: "2020", price: 1850 },
          { year: "2022", price: 2150 }, { year: "2024", price: 2350 }, { year: "2026", price: 2480 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಅಕ್ಟೋ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಮೇ ಮತ್ತು ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ಕೋಳಿ ಫಾರಂ (Poultry Feed) ಮತ್ತು ಪಿಷ್ಟ (Starch) ಕಾರ್ಖಾನೆಗಳಿಂದ ಭಾರಿ ಬೇಡಿಕೆ.",
        worstTime: "ಅಕ್ಟೋಬರ್ ಮತ್ತು ನವೆಂಬರ್ ಖಾರಿಫ್ ಕೊಯ್ಲು ಬಂದಾಗ ದಾವಣಗೆರೆ, ಹಾವೇರಿಯಲ್ಲಿ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಕೊಯ್ಲಿನ ನಂತರ ಬಿಸಿಲಿನಲ್ಲಿ ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ ತೇವಾಂಶ 12% ಒಳಗೆ ತಂದು ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹2,225 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+87.2% (ಸ್ಥಿರ ಬೆಳವಣಿಗೆ)"
      },

      onion: {
        name: "ಈರುಳ್ಳಿ (Onion)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 4800,
        lowPrice: 1800,
        history: [
          { year: "2016", price: 1200 }, { year: "2018", price: 1800 }, { year: "2020", price: 3200 },
          { year: "2022", price: 2400 }, { year: "2024", price: 3800 }, { year: "2026", price: 3200 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಅಕ್ಟೋಬರ್ ಮತ್ತು ನವೆಂಬರ್ (ದೀಪಾವಳಿ ಸಮಯದಲ್ಲಿ ಹಳೇ ದಾಸ್ತಾನು ಮುಗಿದು ಹೊಸ ಮಾಲು ಬರುವ ಮಧ್ಯಂತರ ಅವಧಿ).",
        worstTime: "ಫೆಬ್ರವರಿ ನಿಂದ ಏಪ್ರಿಲ್ ಮಹಾರಾಷ್ಟ್ರ ಮತ್ತು ಕರ್ನಾಟಕದ ರಬಿ ಈರುಳ್ಳಿ ಮಾರುಕಟ್ಟೆ ತುಂಬಿದಾಗ.",
        strategy: "ಗಾಳಿ ಆಡುವ ವಿಶೇಷ ಈರುಳ್ಳಿ ಶೆಡ್‌ಗಳಲ್ಲಿ (Kanda Chawl) ಸಂಗ್ರಹಿಸಿ ಅಕ್ಟೋಬರ್‌ನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+166.7% (ಉತ್ತಮ ಬೆಳವಣಿಗೆ)"
      },

      tomato: {
        name: "ಟೊಮ್ಯಾಟೋ (Tomato)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 4200,
        lowPrice: 900,
        history: [
          { year: "2016", price: 1100 }, { year: "2018", price: 1600 }, { year: "2020", price: 2100 },
          { year: "2022", price: 3200 }, { year: "2023", price: 12000 }, { year: "2024", price: 4200 },
          { year: "2026", price: 2600 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ (ಮಳೆಗಾಲದ ಕೊರತೆ ಸಮಯದಲ್ಲಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹8,000 ವರೆಗೆ ಏರಿಕೆ).",
        worstTime: "ಡಿಸೆಂಬರ್ ನಿಂದ ಫೆಬ್ರವರಿ ಚಳಿಗಾಲದಲ್ಲಿ ಎಲ್ಲೆಡೆ ಭರಪೂರ ಬೆಳೆ ಬಂದಾಗ ಬೆಲೆ ₹500 ಕ್ಕೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಮೇ ತಿಂಗಳಲ್ಲಿ ನಾಟಿ ಮಾಡಿ ಜುಲೈನಲ್ಲಿ ಕೊಯ್ಲಿಗೆ ಬರುವಂತೆ ಯೋಜಿಸಿದರೆ ಗರಿಷ್ಠ ಆದಾಯ ಗಳಿಸಬಹುದು.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ (ಅಲ್ಪಾವಧಿ ಬೆಳೆ)",
        cagr: "ವಿಪರೀತ ಏರಿಳಿತ (High Volatility)"
      },

      potato: {
        name: "ಆಲೂಗಡ್ಡೆ (Potato - Jyothi)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 3200,
        lowPrice: 1600,
        history: [
          { year: "2016", price: 1400 }, { year: "2018", price: 1650 }, { year: "2020", price: 2200 },
          { year: "2022", price: 2100 }, { year: "2024", price: 2800 }, { year: "2026", price: 2500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ ತಿಂಗಳಲ್ಲಿ ಹಾಸನ ಆಲೂಗಡ್ಡೆಗೆ ಗರಿಷ್ಠ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ-ಮಾರ್ಚ್ ಉತ್ತರ ಭಾರತದ ಆಗ್ರಾ ಆಲೂಗಡ್ಡೆ ಭಾರಿ ಪ್ರಮಾಣದಲ್ಲಿ ಬಂದಾಗ.",
        strategy: "ಹಾಸನ ಮತ್ತು ಚಿಕ್ಕಮಗಳೂರಿನಲ್ಲಿ ಬೇಸಿಗೆ ಆರಂಭದಲ್ಲೇ ಬಿತ್ತನೆ ಮಾಡಿ ಜುಲೈನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+78.6% (ಸ್ಥಿರ ಬೆಳವಣಿಗೆ)"
      },

      coffee: {
        name: "ಕಾಫಿ (Coffee - Arabica / Robusta)",
        unit: "50 ಕೆಜಿ ಚೀಲ",
        peakPrice: 23500,
        lowPrice: 17500,
        history: [
          { year: "2016", price: 7800 }, { year: "2018", price: 8500 }, { year: "2020", price: 9200 },
          { year: "2022", price: 14500 }, { year: "2024", price: 19000 }, { year: "2026", price: 22500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಜೂನ್ ನಿಂದ ಆಗಸ್ಟ್ (ಅಂತಾರಾಷ್ಟ್ರೀಯ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಬ್ರೆಜಿಲ್ ಹವಾಮಾನ ಕೊರತೆಯಿಂದ ಬೆಲೆ ದಾಖಲೆ ಮಟ್ಟಕ್ಕೆ ಏರುತ್ತದೆ).",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ ಹೊಸ ಕೊಯ್ಲಿನ ಆರಂಭಿಕ ಹಂತದಲ್ಲಿ.",
        strategy: "ಪಾರ್ಚ್‌ಮೆಂಟ್ ಕಾಫಿಯನ್ನು ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ ತೇವಾಂಶ 10% ಒಳಗೆ ಶೇಖರಿಸಿ ಜೂನ್-ಜುಲೈನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "ಅಂತಾರಾಷ್ಟ್ರೀಯ ಐಸಿಒ (ICO) ದರ ಆಧಾರಿತ",
        cagr: "+188.5% (ಐತಿಹಾಸಿಕ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ)"
      },

      ginger: {
        name: "ಶುಂಠಿ (Ginger)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 14500,
        lowPrice: 6500,
        history: [
          { year: "2016", price: 2200 }, { year: "2018", price: 4500 }, { year: "2020", price: 3800 },
          { year: "2022", price: 5600 }, { year: "2024", price: 14500 }, { year: "2026", price: 11500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }
        ],
        bestTime: "ಮೇ ನಿಂದ ಜುಲೈ ತಿಂಗಳುಗಳಲ್ಲಿ ಹಸಿ ಶುಂಠಿಗೆ ಗರಿಷ್ಠ ಬೇಡಿಕೆ ಇರುತ್ತದೆ.",
        worstTime: "ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿಯಲ್ಲಿ ಹೊಸ ಕೊಯ್ಲು ಮಾರುಕಟ್ಟೆಗೆ ಬಂದಾಗ.",
        strategy: "ಶುಂಠಿಯನ್ನು ಮಣ್ಣಿನಲ್ಲೇ ಕೆಲವು ತಿಂಗಳು ಬಿಟ್ಟು ಬೆಲೆ ಏರಿದ ನಂತರ ಅಗೆದು ಮಾರಾಟ ಮಾಡುವುದು ಉತ್ತಮ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+422.7% (ಭಾರಿ ಲಾಭದಾಯಕ ಬೆಳೆ)"
      },

      garlic: {
        name: "ಬೆಳ್ಳುಳ್ಳಿ (Garlic)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 24000,
        lowPrice: 12000,
        history: [
          { year: "2016", price: 6500 }, { year: "2018", price: 4800 }, { year: "2020", price: 8500 },
          { year: "2022", price: 7200 }, { year: "2024", price: 28000 }, { year: "2026", price: 18500 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "good", lbl: "ಉತ್ತಮ" }
        ],
        bestTime: "ಸೆಪ್ಟೆಂಬರ್ ನಿಂದ ನವೆಂಬರ್ ಹಬ್ಬದ ದಿನಗಳಲ್ಲಿ ಬೆಳ್ಳುಳ್ಳಿ ಬೆಲೆ ಉತ್ತುಂಗಕ್ಕೆ ತಲುಪುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ-ಮಾರ್ಚ್ ಮಧ್ಯಪ್ರದೇಶ ಮತ್ತು ಗುಜರಾತ್ ಹೊಸ ಬೆಳ್ಳುಳ್ಳಿ ಆವಕವಾದಾಗ.",
        strategy: "ಬಿಸಿಲಿನಲ್ಲಿ ಸಂಪೂರ್ಣ ಒಣಗಿಸಿ ತೂಗುಹಾಕಿ ಶೇಖರಿಸಿ ಸೆಪ್ಟೆಂಬರ್‌ನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+184.6% (ಉತ್ತಮ ಬೆಳವಣಿಗೆ)"
      },

      turmeric: {
        name: "ಅರಿಶಿನ (Turmeric - Finger)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 17500,
        lowPrice: 11000,
        history: [
          { year: "2016", price: 7200 }, { year: "2018", price: 6800 }, { year: "2020", price: 7500 },
          { year: "2022", price: 8200 }, { year: "2024", price: 16500 }, { year: "2026", price: 15200 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಆಗಸ್ಟ್ ಮತ್ತು ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳಲ್ಲಿ ಮಸಾಲೆ ಮತ್ತು ಔಷಧೀಯ ರಫ್ತುದಾರರಿಂದ ಹೆಚ್ಚಿನ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ ನಿಂದ ಏಪ್ರಿಲ್ ಚಾಮರಾಜನಗರ ಮತ್ತು ಮಹಾರಾಷ್ಟ್ರದ ಹೊಸ ಅರಿಶಿನ ಮಾರುಕಟ್ಟೆಗೆ ಬಂದಾಗ.",
        strategy: "ಪಾಲಿಶ್ ಮಾಡಿ ಗ್ರೇಡ್ ಮಾಡಿದ ಅರಿಶಿನ ಬೆರಳುಗಳಿಗೆ (Finger Turmeric) 20% ಹೆಚ್ಚುವರಿ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "+111.1% (ಬಲವಾದ ಏರಿಕೆ)"
      },

      groundnut: {
        name: "ಶೇಂಗಾ / ನೆಲಗಡಲೆ (Groundnut)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 7800,
        lowPrice: 5800,
        history: [
          { year: "2016", price: 4220 }, { year: "2018", price: 4890 }, { year: "2020", price: 5275 },
          { year: "2022", price: 6200 }, { year: "2024", price: 6783 }, { year: "2026", price: 7200 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಅಕ್ಟೋ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಮೇ ಮತ್ತು ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ಎಣ್ಣೆ ಗಿರಣಿಗಳಿಂದ ಭಾರಿ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್ ಪಾವಗಡ, ಚಿತ್ರದುರ್ಗದಲ್ಲಿ ಶೇಂಗಾ ಕೊಯ್ಲು ಮುಗಿದ ತಕ್ಷಣ.",
        strategy: "ಸಿಪ್ಪೆ ಸಮೇತ ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹6,783 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+70.6% (ಸ್ಥಿರ ಬೆಳವಣಿಗೆ)"
      },

      bengal_gram: {
        name: "ಕಡಲೆ (Bengal Gram / Chana)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 7200,
        lowPrice: 5200,
        history: [
          { year: "2016", price: 5400 }, { year: "2018", price: 4600 }, { year: "2020", price: 4900 },
          { year: "2022", price: 5300 }, { year: "2024", price: 6400 }, { year: "2026", price: 6800 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಆಗಸ್ಟ್ ಮತ್ತು ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಬೇಳೆ ಗಿರಣಿಗಳಿಂದ ಹೆಚ್ಚಿನ ದರ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಫೆಬ್ರವರಿ ಮತ್ತು ಮಾರ್ಚ್ ಗದಗ, ಬಾಗಲಕೋಟೆಯಲ್ಲಿ ಕೊಯ್ಲು ಆದಾಗ.",
        strategy: "ಮಂಡಿ ದರವು MSP ಗಿಂತ ಕಡಿಮೆಯಿದ್ದರೆ ನೇರವಾಗಿ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ.",
        msp: "₹5,650 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+25.9% (ಸುರಕ್ಷಿತ ಬೆಳೆ)"
      },

      green_gram: {
        name: "ಹೆಸರುಕಾಳು (Green Gram / Moong)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 9400,
        lowPrice: 7200,
        history: [
          { year: "2016", price: 5200 }, { year: "2018", price: 6975 }, { year: "2020", price: 7196 },
          { year: "2022", price: 7755 }, { year: "2024", price: 8558 }, { year: "2026", price: 8900 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಆಗ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಮೇ ಮತ್ತು ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗರಿಷ್ಠ ಬೆಲೆ ಇರುತ್ತದೆ.",
        worstTime: "ಸೆಪ್ಟೆಂಬರ್‌ನಲ್ಲಿ ಗದಗ, ಧಾರವಾಡದಲ್ಲಿ ಹೊಸ ಹೆಸರುಕಾಳು ಬಂದಾಗ.",
        strategy: "ಸರ್ಕಾರದ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರಗಳನ್ನು ಸದುಪಯೋಗಪಡಿಸಿಕೊಳ್ಳಿ.",
        msp: "₹8,682 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+71.2% (ಉತ್ತಮ ಬೆಳವಣಿಗೆ)"
      },

      sunflower: {
        name: "ಸೂರ್ಯಕಾಂತಿ (Sunflower)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 8200,
        lowPrice: 6200,
        history: [
          { year: "2016", price: 3950 }, { year: "2018", price: 5388 }, { year: "2020", price: 5885 },
          { year: "2022", price: 6400 }, { year: "2024", price: 7280 }, { year: "2026", price: 7600 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಡಿಸೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ ತಿಂಗಳಲ್ಲಿ ಎಣ್ಣೆ ಕಾರ್ಖಾನೆಗಳಿಂದ ಉತ್ತಮ ಬೇಡಿಕೆ.",
        worstTime: "ಮಾರ್ಚ್-ಏಪ್ರಿಲ್ ರಬಿ ಹಂಗಾಮಿನ ಕೊಯ್ಲಿನಲ್ಲಿ.",
        strategy: "ತೈಲಾಂಶ 40% ಗಿಂತ ಹೆಚ್ಚಿರುವ ಹೈಬ್ರಿಡ್ ಬೀಜಗಳನ್ನು ಬೆಳೆಸಿ.",
        msp: "₹7,280 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+92.4% (ದ್ವಿಗುಣಗೊಂಡ ಬೆಲೆ)"
      },

      cardamom: {
        name: "ಏಲಕ್ಕಿ (Green Cardamom)",
        unit: "ಕೆಜಿ",
        peakPrice: 3200,
        lowPrice: 1900,
        history: [
          { year: "2016", price: 950 }, { year: "2018", price: 1400 }, { year: "2020", price: 1850 },
          { year: "2022", price: 1600 }, { year: "2024", price: 2450 }, { year: "2026", price: 2750 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಏಪ್ರಿ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮೇ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಜೂನ್", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಅಕ್ಟೋ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ನವೆಂ", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಮೇ ನಿಂದ ಜುಲೈ ತಿಂಗಳುಗಳಲ್ಲಿ ರಫ್ತು ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗರಿಷ್ಠ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್ ಕೊಡಗು, ಹಾಸನದಲ್ಲಿ ಕೊಯ್ಲು ಆದಾಗ.",
        strategy: "8mm ದಪ್ಪ ಗಾತ್ರದ ಹಸಿರು ಬಣ್ಣ ಉಳಿಯುವಂತೆ ಡ್ರೈಯರ್‌ನಲ್ಲಿ ಒಣಗಿಸಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ (ರಫ್ತು ಆಧಾರಿತ)",
        cagr: "+189.5% (ಅತ್ಯುನ್ನತ ಲಾಭ)"
      },

      pepper: {
        name: "ಕಾಳುಮೆಣಸು (Black Pepper)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 72000,
        lowPrice: 55000,
        history: [
          { year: "2016", price: 68000 }, { year: "2018", price: 38000 }, { year: "2020", price: 34000 },
          { year: "2022", price: 51000 }, { year: "2024", price: 62000 }, { year: "2026", price: 66000 }
        ],
        seasonality: [
          { m: "ಜನ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಫೆಬ್ರ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮೇ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಜೂನ್", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಜುಲೈ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಆಗ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಅಕ್ಟೋ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ನವೆಂ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಡಿಸೆಂ", status: "low", lbl: "ಕುಸಿತ" }
        ],
        bestTime: "ಜುಲೈ ಮತ್ತು ಆಗಸ್ಟ್ ಮಳೆಗಾಲದಲ್ಲಿ ಮಸಾಲೆ ಕಂಪನಿಗಳಿಂದ ಭಾರಿ ಬೇಡಿಕೆ.",
        worstTime: "ಫೆಬ್ರವರಿ ಮತ್ತು ಮಾರ್ಚ್ ಕೊಯ್ಲಿನ ಸಮಯದಲ್ಲಿ.",
        strategy: "ಗಾರ್ಬಲ್ಡ್ (Garbled) ಗುಣಮಟ್ಟದ ಕಾಳುಮೆಣಸನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ ಜುಲೈನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ",
        cagr: "ಮರುಚೇತರಿಕೆ (Strong Recovery)"
      },

      silk: {
        name: "ರೇಷ್ಮೆ ಗೂಡು (Silk Cocoon - CB/Bivoltine)",
        unit: "ಕೆಜಿ",
        peakPrice: 720,
        lowPrice: 480,
        history: [
          { year: "2016", price: 320 }, { year: "2018", price: 420 }, { year: "2020", price: 380 },
          { year: "2022", price: 620 }, { year: "2024", price: 580 }, { year: "2026", price: 640 }
        ],
        seasonality: [
          { m: "ಜನ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಫೆಬ್ರ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಮಾರ್ಚ್", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಏಪ್ರಿ", status: "low", lbl: "ಕುಸಿತ" },
          { m: "ಮೇ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಜೂನ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಡಿಸೆಂ", status: "good", lbl: "ಉತ್ತಮ" }
        ],
        bestTime: "ಸೆಪ್ಟೆಂಬರ್ ನಿಂದ ನವೆಂಬರ್ (ದಸರಾ, ದೀಪಾವಳಿ ಮತ್ತು ಮದುವೆ ಸೀಸನ್ ಸೀರೆ ತಯಾರಕರಿಂದ ಭಾರಿ ಬೇಡಿಕೆ).",
        worstTime: "ಏಪ್ರಿಲ್-ಮೇ ಬೇಸಿಗೆಯಲ್ಲಿ ನೀರಿನ ಕೊರತೆಯಿಂದ ಗುಣಮಟ್ಟ ತಗ್ಗಿದಾಗ.",
        strategy: "ರಾಮನಗರ ಅಥವಾ ಶಿಡ್ಲಘಟ್ಟ ಸರ್ಕಾರಿ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಇ-ಹರಾಜು ಮೂಲಕ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "ಮಾರುಕಟ್ಟೆ ಹರಾಜು ಆಧಾರಿತ",
        cagr: "+100.0% (ದ್ವಿಗುಣಗೊಂಡ ದರ)"
      },

      wheat: {
        name: "ಜವಾರಿ ಗೋಧಿ (Wheat)",
        unit: "ಕ್ವಿಂಟಾಲ್",
        peakPrice: 2850,
        lowPrice: 2100,
        history: [
          { year: "2016", price: 1625 }, { year: "2018", price: 1840 }, { year: "2020", price: 1975 },
          { year: "2022", price: 2125 }, { year: "2024", price: 2275 }, { year: "2026", price: 2450 }
        ],
        seasonality: [
          { m: "ಜನ", status: "avg", lbl: "ಸಾಧಾರಣ" }, { m: "ಫೆಬ್ರ", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಮಾರ್ಚ್", status: "crash", lbl: "ಕನಿಷ್ಠ" }, { m: "ಏಪ್ರಿ", status: "crash", lbl: "ಕನಿಷ್ಠ" },
          { m: "ಮೇ", status: "low", lbl: "ಕುಸಿತ" }, { m: "ಜೂನ್", status: "avg", lbl: "ಸಾಧಾರಣ" },
          { m: "ಜುಲೈ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಆಗ", status: "good", lbl: "ಉತ್ತಮ" },
          { m: "ಸೆಪ್ಟೆಂ", status: "peak", lbl: "ಗರಿಷ್ಠ" }, { m: "ಅಕ್ಟೋ", status: "peak", lbl: "ಗರಿಷ್ಠ" },
          { m: "ನವೆಂ", status: "good", lbl: "ಉತ್ತಮ" }, { m: "ಡಿಸೆಂ", status: "good", lbl: "ಉತ್ತಮ" }
        ],
        bestTime: "ಸೆಪ್ಟೆಂಬರ್ ಮತ್ತು ಅಕ್ಟೋಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಗರಿಷ್ಠ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        worstTime: "ಮಾರ್ಚ್-ಏಪ್ರಿಲ್ ಕೊಯ್ಲಿನ ಸಮಯದಲ್ಲಿ ಉತ್ತರ ಕರ್ನಾಟಕದಲ್ಲಿ ಬೆಲೆ ಕುಸಿಯುತ್ತದೆ.",
        strategy: "ಉತ್ತರ ಕರ್ನಾಟಕದ ಸಾಂಪ್ರದಾಯಿಕ ಜವಾರಿ ಗೋಧಿಯನ್ನು ಹಿಟ್ಟಿನ ಗಿರಣಿಗಳಿಗೆ ಪ್ರೀಮಿಯಂ ದರದಲ್ಲಿ ನೇರವಾಗಿ ಮಾರಾಟ ಮಾಡಿ.",
        msp: "₹2,425 / ಕ್ವಿಂಟಾಲ್ (MSP 2025-26)",
        cagr: "+50.8% (ಸ್ಥಿರ ಏರಿಕೆ)"
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
      const cropKey = select ? select.value : 'arecanut';
      const data = CROP_ANALYZER_DB[cropKey] || CROP_ANALYZER_DB['arecanut'];

      document.getElementById('chart-heading').textContent = `${data.name} — 10 ವರ್ಷಗಳ ಬೆಲೆ ಇತಿಹಾಸ (2016–2026 ₹/${data.unit})`;
      document.getElementById('chart-cagr-badge').textContent = data.cagr.split(' ')[0] + ' ಬೆಳವಣಿಗೆ';
      document.getElementById('adv-best-time').textContent = data.bestTime;
      document.getElementById('adv-worst-time').textContent = data.worstTime;
      document.getElementById('adv-strategy').textContent = data.strategy;
      document.getElementById('adv-msp').textContent = data.msp;
      document.getElementById('adv-cagr').textContent = data.cagr;
      document.getElementById('calc-unit-label').textContent = data.unit;

      // Render 12-Month Heatmap
      const heatmapGrid = document.getElementById('season-heatmap-grid');
      heatmapGrid.innerHTML = '';
      data.seasonality.forEach(s => {
        const cell = document.createElement('div');
        cell.className = `heat-cell ${s.status}`;
        cell.innerHTML = `<div>${s.m}</div><div style="font-size:9.5px; opacity:0.95; margin-top:2px;">${s.lbl}</div>`;
        heatmapGrid.appendChild(cell);
      });

      // Render Chart.js
      renderTrendChart(data);
      calculateCropProfit();
    }

    function calculateCropProfit() {
      const select = document.getElementById('analyzer-crop-select');
      const cropKey = select ? select.value : 'arecanut';
      const data = CROP_ANALYZER_DB[cropKey] || CROP_ANALYZER_DB['arecanut'];

      const qtyInput = document.getElementById('calc-qty');
      const qty = parseFloat(qtyInput ? qtyInput.value : 20) || 1;

      const peakTotal = Math.round(qty * (data.peakPrice || (data.history[data.history.length-1].price * 1.1)));
      const lowTotal = Math.round(qty * (data.lowPrice || (data.history[data.history.length-1].price * 0.78)));
      const diff = peakTotal - lowTotal;

      document.getElementById('calc-peak-val').textContent = `₹${peakTotal.toLocaleString('en-IN')}`;
      document.getElementById('calc-low-val').textContent = `₹${lowTotal.toLocaleString('en-IN')}`;
      document.getElementById('calc-diff-val').textContent = `💡 ಸರಿಯಾದ ಸಮಯದಲ್ಲಿ ಮಾರಿದರೆ ಸಿಗುವ ನಿವ್ವಳ ಹೆಚ್ಚುವರಿ ಲಾಭ: +₹${diff.toLocaleString('en-IN')}`;
    }

    function renderTrendChart(crop) {
      const ctx = document.getElementById('cropTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      const labels = crop.history.map(h => h.year);
      const prices = crop.history.map(h => h.price);

      // Create Gradient
      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(34, 197, 94, 0.35)');
      gradient.addColorStop(1, 'rgba(34, 197, 94, 0.0)');

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: `ಸರಾಸರಿ ದರ (₹/${crop.unit})`,
            data: prices,
            borderColor: '#15803D',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#0A3E20',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
            pointRadius: 6,
            pointHoverRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#0F172A',
              titleFont: { family: 'Inter', size: 12, weight: 'bold' },
              bodyFont: { family: 'Inter', size: 13, weight: 'bold' },
              padding: 10,
              cornerRadius: 8,
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
                font: { family: 'Inter', size: 11, weight: '600' },
                color: '#64748B'
              },
              grid: { color: '#E2E8F0', strokeDash: [4, 4] }
            },
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Inter', size: 11, weight: 'bold' }, color: '#334155' }
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
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:50px 20px; color:#64748b; font-weight:800; font-size:16px;">🔍 ಯಾವುದೇ ಫಲಿತಾಂಶ ಕಂಡುಬಂದಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ಬೆಳೆ ಅಥವಾ ಮಾರುಕಟ್ಟೆ ಆಯ್ಕೆ ಮಾಡಿ.</div>';
        return;
      }

      const displayList = list.slice(0, 180);
      displayList.forEach(item => {
        const cropName = item.cropKn || item.cropEn || item.crop;
        const variety = item.variety || 'ಸಾಮಾನ್ಯ';
        const modalPrice = item.avg ? `₹${item.avg.toLocaleString('en-IN')}` : '—';
        const minPrice = item.min ? `₹${item.min.toLocaleString('en-IN')}` : '—';
        const maxPrice = item.max ? `₹${item.max.toLocaleString('en-IN')}` : '—';
        const arrivals = item.arrivals ? `${item.arrivals.toLocaleString('en-IN')} ಕ್ವಿಂಟಾಲ್` : 'ಮಂಡಿ ಲೈವ್';

        const card = document.createElement('div');
        card.className = 'mandi-card';
        card.innerHTML = `
          <div>
            <div class="mc-header">
              <div>
                <div class="mc-crop-name">${cropName}</div>
                <div class="mc-mandi">📍 ${item.market} APMC (${item.district || 'ಕರ್ನಾಟಕ'})</div>
              </div>
              <span class="mc-variety-pill">${variety}</span>
            </div>
            
            <div class="mc-price-box">
              <div style="font-size:11.5px; color:#15803D; font-weight:900;">ಇಂದಿನ ಮಾದರಿ ದರ (Modal Price)</div>
              <div class="mc-modal-price">${modalPrice}</div>
              <div class="mc-unit">ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ (100 Kg)</div>
            </div>

            <div class="mc-range-grid">
              <div>ಕನಿಷ್ಠ: <span class="mc-range-val">${minPrice}</span></div>
              <div style="text-align:right;">ಗರಿಷ್ಠ: <span class="mc-range-val">${maxPrice}</span></div>
              <div style="grid-column:1/-1; margin-top:3px; font-size:11.5px;">ಆವಕ (Arrivals): <span style="font-weight:800; color:#0F172A;">${arrivals}</span></div>
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

print("SUCCESS_UPGRADED_APMC_SUPER_UI")
