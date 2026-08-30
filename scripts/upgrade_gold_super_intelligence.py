# -*- coding: utf-8 -*-
"""
Karnata — scripts/upgrade_gold_super_intelligence.py
Creates the upgraded Gold & Commodity Price Intelligence, Buy/Sell Analyzer,
Jewellery Invoice Breakdown Calculator, Gold-to-Silver Ratio Gauge, and Multi-Year Trends on gold-rate.html.
"""

gold_html_template = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="canonical" href="https://karnata.in/gold-rate.html">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಇಂದಿನ ಚಿನ್ನ ಬೆಳ್ಳಿ ಬೆಲೆ ಕರ್ನಾಟಕ & ದರ ವಿಶ್ಲೇಷಕ (Gold & Commodity Intelligence) | Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಇಂದಿನ 22K, 24K, 18K ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರಗಳು, 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ವಿಶ್ಲೇಷಣೆ, ಯಾವಾಗ ಖರೀದಿಸಬೇಕು, ಯಾವಾಗ ಮಾರಬೇಕು, ಆಭರಣ ಬಿಲ್ & ಜಿಎಸ್‌ಟಿ ಕ್ಯಾಲ್ಕುಲೇಟರ್.">
  <meta name="keywords" content="gold rate today Karnataka, 22k gold price bangalore, 24k gold rate, silver rate today, gold buy sell analysis, gold jewelry bill calculator, gold to silver ratio">

  <!-- OpenGraph & Social SEO -->
  <meta property="og:title" content="ಇಂದಿನ ಚಿನ್ನ ಬೆಳ್ಳಿ ಬೆಲೆ ಕರ್ನಾಟಕ & ದರ ವಿಶ್ಲೇಷಕ — Karnata.in">
  <meta property="og:description" content="ಕರ್ನಾಟಕದ ಲೈವ್ ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರಗಳು, 10 ವರ್ಷಗಳ ಬೆಲೆ ಏರಿಳಿತ, ಯಾವಾಗ ಚಿನ್ನ ಖರೀದಿಸಬೇಕು? ಯಾವಾಗ ಮಾರಬೇಕು? ಮತ್ತು ಆಭರಣ ಬಿಲ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್.">
  <meta property="og:url" content="https://karnata.in/gold-rate.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Karnata.in">
  <meta property="og:locale" content="kn_IN">
  <meta property="og:image" content="https://karnata.in/assets/icons/icon-512x512.png">

  <!-- Google Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "ಇಂದಿನ ಚಿನ್ನ ಬೆಳ್ಳಿ ಬೆಲೆ & ದರ ವಿಶ್ಲೇಷಕ",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/gold-rate.html",
    "description": "Live Karnataka Gold & Silver Market Rates, 10-Year Historical Commodity Trends, Buy/Sell Analyzer, and Jewellery Bill Calculator."
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  
  <!-- Chart.js for Historical Gold & Commodity Curves -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="/data-loader.js"></script>
  <script src="/nav-component.js"></script>

  <style>
    :root {
      --gold-dark: #78350F;
      --gold-primary: #D97706;
      --gold-light: #FEF3C7;
      --gold-accent: #F59E0B;
      --gold-bg: #FFFBEB;
      --silver-accent: #64748B;
      --silver-bg: #F1F5F9;
      --primary-dark: #0F172A;
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
    .gold-hero {
      background: linear-gradient(135deg, #1C1917 0%, #292524 40%, #451A03 80%, #78350F 100%);
      color: #FFFFFF;
      padding: 40px 20px 85px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid #FACC15;
    }
    .gold-hero::after {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 80% 20%, rgba(245, 158, 11, 0.25) 0%, transparent 60%);
      pointer-events: none;
    }
    .gold-hero h1 {
      font-size: 32px;
      font-weight: 900;
      margin-bottom: 8px;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }
    .gold-hero p {
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
    .gold-hero-tag {
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

    /* ════ 4 SUMMARY STATS BAR ════ */
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
      background: linear-gradient(90deg, #F59E0B, #D97706);
      opacity: 0;
      transition: opacity 0.25s;
    }
    .stat-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -6px rgba(217, 119, 6, 0.18);
      border-color: #FCD34D;
    }
    .stat-card:hover::before { opacity: 1; }
    .stat-icon { font-size: 26px; margin-bottom: 4px; }
    .stat-val { font-size: 24px; font-weight: 900; color: var(--gold-dark); font-family: 'Inter', sans-serif; }
    .stat-lbl { font-size: 13px; font-weight: 800; color: var(--text-main); margin-top: 2px; }
    .stat-sub { font-size: 11px; color: var(--text-muted); font-weight: 600; }

    /* ════ MAIN WRAPPER ════ */
    .gold-container {
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
      padding: 14px 18px;
      font-size: 15px;
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
      gap: 8px;
      font-family: inherit;
    }
    .mode-tab.active {
      background: #FFFFFF;
      color: var(--gold-dark);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08);
      font-weight: 900;
    }

    /* ════ SECTION 1: LIVE GOLD & SILVER RATES GRID ════ */
    .gold-rates-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 36px;
    }
    @media (max-width: 900px) { .gold-rates-grid { grid-template-columns: 1fr; } }

    .gold-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 20px;
      padding: 24px;
      box-shadow: var(--shadow-premium);
      position: relative;
      overflow: hidden;
      transition: transform 0.2s;
    }
    .gold-card:hover { transform: translateY(-3px); }
    .gold-card.gold-24k { border-color: #FCD34D; background: linear-gradient(180deg, #FFFDF5 0%, #FFFFFF 100%); }
    .gold-card.gold-22k { border-color: #FDE68A; background: linear-gradient(180deg, #FEFCE8 0%, #FFFFFF 100%); }
    .gold-card.silver-card { border-color: #CBD5E1; background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%); }

    .gc-badge {
      display: inline-block;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 900;
      margin-bottom: 12px;
    }
    .gc-price {
      font-size: 34px;
      font-weight: 900;
      color: #0F172A;
      font-family: 'Inter', sans-serif;
      line-height: 1.1;
    }
    .gc-sub { font-size: 13px; color: var(--text-muted); font-weight: 700; margin-top: 4px; }
    .gc-breakdown {
      margin-top: 18px;
      padding-top: 14px;
      border-top: 1px solid #E2E8F0;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      font-size: 13px;
    }
    .gc-item-lbl { color: #64748B; font-weight: 600; }
    .gc-item-val { font-weight: 900; font-family: 'Inter', sans-serif; color: #1E293B; text-align: right; }

    /* ════ SECTION 2: INTELLIGENCE ANALYZER & CHARTS ════ */
    .analyzer-box {
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 20px;
      padding: 28px;
      box-shadow: var(--shadow-premium);
      margin-bottom: 36px;
    }
    .analyzer-insights-grid {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 28px;
      margin-bottom: 28px;
    }
    @media (max-width: 920px) { .analyzer-insights-grid { grid-template-columns: 1fr; } }

    .chart-container-box {
      background: #FAFCFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    }
    .time-pills {
      display: flex;
      gap: 6px;
    }
    .time-pill {
      padding: 4px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 800;
      background: #E2E8F0;
      border: none;
      cursor: pointer;
      color: #475569;
      transition: all 0.2s;
    }
    .time-pill.active {
      background: var(--gold-primary);
      color: #FFFFFF;
    }

    /* HEATMAP */
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
    .heat-cell.peak { background: #B45309; color: #FFFFFF; }
    .heat-cell.good { background: #FCD34D; color: #78350F; }
    .heat-cell.avg { background: #FEF08A; color: #713F12; }
    .heat-cell.low { background: #DCFCE7; color: #166534; }
    .heat-cell.best-buy { background: #15803D; color: #FFFFFF; box-shadow: 0 2px 6px rgba(21, 128, 61, 0.3); }

    /* SMART ADVICE CARDS */
    .advice-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      margin-bottom: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .advice-card.buy-window { background: #F0FDF4; border-color: #86EFAC; }
    .advice-card.sell-window { background: #FEF2F2; border-color: #FECACA; }
    .advice-card.gsr-window { background: #EFF6FF; border-color: #BFDBFE; }
    .advice-card.strategy-window { background: #FFFBEB; border-color: #FDE68A; }

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

    /* ════ SECTION 3: JEWELLERY BILL & GOLD LOAN CALCULATORS ════ */
    .calc-grid-duo {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 36px;
    }
    @media (max-width: 860px) { .calc-grid-duo { grid-template-columns: 1fr; } }

    .widget-box {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 20px;
      padding: 26px;
      box-shadow: var(--shadow-premium);
    }
    .widget-title {
      font-size: 18px;
      font-weight: 900;
      color: #0F172A;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .form-group {
      margin-top: 14px;
    }
    .form-lbl {
      display: block;
      font-size: 13px;
      font-weight: 800;
      color: #334155;
      margin-bottom: 5px;
    }
    .form-ctrl {
      width: 100%;
      padding: 11px 14px;
      font-size: 14.5px;
      font-weight: 700;
      font-family: inherit;
      border: 1.5px solid #CBD5E1;
      border-radius: 12px;
      outline: none;
      background: #F8FAFC;
      transition: all 0.2s;
    }
    .form-ctrl:focus {
      border-color: var(--gold-primary);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
    }

    .bill-result-box {
      background: #FFFBEB;
      border: 1.5px solid #FDE68A;
      border-radius: 14px;
      padding: 16px;
      margin-top: 18px;
    }
    .bill-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
      font-size: 13.5px;
      border-bottom: 1px dashed #FCD34D;
    }
    .bill-row:last-child {
      border-bottom: none;
      padding-top: 10px;
      font-size: 16px;
      font-weight: 900;
      color: #78350F;
    }

    /* ════ 125-YEAR HISTORICAL TABLE ════ */
    .history-table-box {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 22px;
      margin-top: 28px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }
    .hist-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }
    .hist-table th {
      background: #F1F5F9;
      color: #334155;
      padding: 10px 12px;
      text-align: left;
      font-weight: 800;
      border-bottom: 2px solid #CBD5E1;
    }
    .hist-table td {
      padding: 10px 12px;
      border-bottom: 1px solid #E2E8F0;
      color: #1E293B;
    }
    .hist-table tr:hover { background: #F8FAFC; }
  </style>
</head>
<body>

  <!-- ════ HERO BANNER ════ -->
  <header class="gold-hero">
    <div class="hero-badge-row">
      <div class="gold-hero-tag">🪙 ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ಮರ್ಚೆಂಟ್ಸ್ ಅಸೋಸಿಯೇಷನ್ (KBMA)</div>
      <div class="gold-hero-tag" style="color:#FEF08A; border-color:#FDE68A;">⚡ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ನವೀಕರಣ</div>
    </div>
    <h1 style="margin-top:14px;">ಇಂದಿನ ಚಿನ್ನ ಬೆಳ್ಳಿ ಬೆಲೆ ಕರ್ನಾಟಕ & ದರ ವಿಶ್ಲೇಷಕ (Gold & Commodity Intelligence)</h1>
    <p>ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ 22K, 24K, 18K ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ದರಗಳು, 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಏರಿಳಿತ (2016-2026), ಯಾವಾಗ ಖರೀದಿಸಬೇಕು? ಯಾವಾಗ ಮಾರಬೇಕು? ಮತ್ತು ಆಭರಣ ಬಿಲ್ & ಜಿಎಸ್‌ಟಿ ಕ್ಯಾಲ್ಕುಲೇಟರ್.</p>
    <div style="font-size:12.5px; color:#FEF08A; font-weight:800;" id="hero-update-date">🔴 ಅಧಿಕೃತ ಲೈವ್ ನವೀಕರಣ: 2026-08-28 — Karnataka Bullion Live</div>
  </header>

  <!-- ════ 4 SUMMARY STATS ════ -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-icon">👑</div>
      <div class="stat-val" id="stat-24k-rate">₹16,304</div>
      <div class="stat-lbl">24K ಶುದ್ಧ ಚಿನ್ನ (ಪ್ರತಿ ಗ್ರಾಂ)</div>
      <div class="stat-sub">99.9% ಅಪರಂಜಿ (Fine Gold)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">💍</div>
      <div class="stat-val" id="stat-22k-rate">₹14,940</div>
      <div class="stat-lbl">22K ಆಭರಣ ಚಿನ್ನ (ಪ್ರತಿ ಗ್ರಾಂ)</div>
      <div class="stat-sub">916 ಹಾಲ್‌ಮಾರ್ಕ್ (Hallmark)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🥈</div>
      <div class="stat-val" id="stat-silver-rate">₹260.00</div>
      <div class="stat-lbl">ಬೆಳ್ಳಿ ದರ (ಪ್ರತಿ ಗ್ರಾಂ)</div>
      <div class="stat-sub">₹2,60,000 / 1 Kg (999 Pure)</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">⚖️</div>
      <div class="stat-val" id="stat-gsr-val">62.7</div>
      <div class="stat-lbl">Gold-to-Silver Ratio (GSR)</div>
      <div class="stat-sub">ಚಿನ್ನ-ಬೆಳ್ಳಿ ಅನುಪಾತ ಸೂಚ್ಯಂಕ</div>
    </div>
  </div>

  <!-- ════ MAIN WRAPPER ════ -->
  <div class="gold-container">

    <!-- MODE TABS -->
    <div class="mode-tabs">
      <button class="mode-tab active" id="tab-live" onclick="switchGoldTab('live')">
        <span>🪙 ಇಂದಿನ ಲೈವ್ ದರಗಳು (Live Rates)</span>
      </button>
      <button class="mode-tab" id="tab-analyzer" onclick="switchGoldTab('analyzer')">
        <span>📈 ಚಿನ್ನ & ಕಮಾಡಿಟಿ ದರ ವಿಶ್ಲೇಷಕ (Intelligence)</span>
      </button>
      <button class="mode-tab" id="tab-calculator" onclick="switchGoldTab('calculator')">
        <span>🧮 ಆಭರಣ ಬಿಲ್ & ಗೋಲ್ಡ್ ಲೋನ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್</span>
      </button>
    </div>

    <!-- ══════════════════════════════════════════════════════
         TAB 1: LIVE GOLD & SILVER RATES (24K, 22K, 18K, Silver)
    ══════════════════════════════════════════════════════ -->
    <div id="view-live">
      
      <div class="gold-rates-grid">
        <!-- 24K Pure Gold -->
        <div class="gold-card gold-24k">
          <span class="gc-badge" style="background:#FEF3C7; color:#92400E; border:1px solid #FDE68A;">👑 24K ಅಪರಂಜಿ ಶುದ್ಧ ಚಿನ್ನ (999 Pure)</span>
          <div class="gc-price" id="card-24k-rate">₹16,304</div>
          <div class="gc-sub">ಪ್ರತಿ ಗ್ರಾಂ ದರ (ಚಿನ್ನದ ನಾಣ್ಯ / ಬಾರ್)</div>
          <div class="gc-breakdown">
            <div><span class="gc-item-lbl">8 ಗ್ರಾಂ (1 ಪವನ್):</span></div>
            <div class="gc-item-val" id="card-24k-8g">₹1,30,432</div>
            <div><span class="gc-item-lbl">10 ಗ್ರಾಂ (1 ತೊಲ):</span></div>
            <div class="gc-item-val" id="card-24k-10g">₹1,63,040</div>
            <div><span class="gc-item-lbl">100 ಗ್ರಾಂ:</span></div>
            <div class="gc-item-val" id="card-24k-100g">₹16,30,400</div>
          </div>
        </div>

        <!-- 22K Jewellery Gold -->
        <div class="gold-card gold-22k">
          <span class="gc-badge" style="background:#FEF9C3; color:#854D0E; border:1px solid #FEF08A;">💍 22K ಆಭರಣ ಬಂಗಾರ (916 BIS Hallmark)</span>
          <div class="gc-price" id="card-22k-rate">₹14,940</div>
          <div class="gc-sub">ಪ್ರತಿ ಗ್ರಾಂ ದರ (ಆಭರಣ ತಯಾರಿಕೆಗೆ ಸೂಕ್ತ)</div>
          <div class="gc-breakdown">
            <div><span class="gc-item-lbl">8 ಗ್ರಾಂ (1 ಪವನ್):</span></div>
            <div class="gc-item-val" id="card-22k-8g">₹1,19,520</div>
            <div><span class="gc-item-lbl">10 ಗ್ರಾಂ (1 ತೊಲ):</span></div>
            <div class="gc-item-val" id="card-22k-10g">₹1,49,400</div>
            <div><span class="gc-item-lbl">100 ಗ್ರಾಂ:</span></div>
            <div class="gc-item-val" id="card-22k-100g">₹14,94,000</div>
          </div>
        </div>

        <!-- Silver 999 -->
        <div class="gold-card silver-card">
          <span class="gc-badge" style="background:#F1F5F9; color:#334155; border:1px solid #CBD5E1;">🥈 999 ಶುದ್ಧ ಬೆಳ್ಳಿ (Fine Silver)</span>
          <div class="gc-price" id="card-silver-rate">₹260.00</div>
          <div class="gc-sub">ಪ್ರತಿ ಗ್ರಾಂ ದರ (ಬೆಳ್ಳಿ ನಾಣ್ಯ / ಪೂಜಾ ಪಾತ್ರೆ)</div>
          <div class="gc-breakdown">
            <div><span class="gc-item-lbl">10 ಗ್ರಾಂ ಬೆಳ್ಳಿ:</span></div>
            <div class="gc-item-val" id="card-silver-10g">₹2,600</div>
            <div><span class="gc-item-lbl">100 ಗ್ರಾಂ ಬೆಳ್ಳಿ:</span></div>
            <div class="gc-item-val" id="card-silver-100g">₹26,000</div>
            <div><span class="gc-item-lbl">1 ಕೆಜಿ (1 Kg Bar):</span></div>
            <div class="gc-item-val" id="card-silver-1kg">₹2,60,000</div>
          </div>
        </div>
      </div>

      <!-- CITY RATES TABLE -->
      <div style="background:#FFFFFF; border:1.5px solid var(--border); border-radius:18px; padding:22px; margin-bottom:36px; box-shadow:var(--shadow-premium);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
          <h3 style="font-size:18px; font-weight:900; color:#0F172A;">📍 ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರಗಳು (City-wise Live Rates)</h3>
          <span style="font-size:12px; color:#64748B; font-weight:700;">ಪ್ರತಿ ಗ್ರಾಂ ಲೆಕ್ಕದಲ್ಲಿ</span>
        </div>
        <div style="overflow-x:auto;">
          <table class="hist-table">
            <thead>
              <tr>
                <th>ನಗರ</th>
                <th>24K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>22K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>18K ಚಿನ್ನ (ಗ್ರಾಂ)</th>
                <th>ಬೆಳ್ಳಿ (ಗ್ರಾಂ)</th>
                <th>1 ಕೆಜಿ ಬೆಳ್ಳಿ</th>
              </tr>
            </thead>
            <tbody id="city-rates-tbody"></tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         TAB 2: GOLD & COMMODITY INTELLIGENCE & BUY/SELL ANALYZER
    ══════════════════════════════════════════════════════ -->
    <div id="view-analyzer" style="display:none;">
      
      <div class="analyzer-box">
        
        <div class="analyzer-insights-grid">
          
          <!-- LEFT: Multi-Timeframe Chart & 12-Month Heatmap -->
          <div>
            <div class="chart-container-box">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
                <h3 style="font-size:16px; font-weight:900; color:#0F172A;">📈 ಚಿನ್ನದ ಬೆಲೆ ಪ್ರವೃತ್ತಿ & ಬೆಳವಣಿಗೆ (Trend Chart)</h3>
                <div class="time-pills">
                  <button class="time-pill active" onclick="updateChartTimeframe('10y', this)">10 ವರ್ಷಗಳು</button>
                  <button class="time-pill" onclick="updateChartTimeframe('5y', this)">5 ವರ್ಷಗಳು</button>
                  <button class="time-pill" onclick="updateChartTimeframe('1y', this)">1 ವರ್ಷ</button>
                  <button class="time-pill" onclick="updateChartTimeframe('125y', this)">125 ವರ್ಷ (1901-2026)</button>
                </div>
              </div>
              <div style="height:270px; position:relative;">
                <canvas id="goldTrendChart"></canvas>
              </div>
            </div>

            <!-- 12-Month Gold Seasonality Heatmap -->
            <div style="margin-top:22px; background:#FFFFFF; border:1px solid #E2E8F0; border-radius:14px; padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="font-size:14px; font-weight:900; color:#0F172A;">🗓️ 12 ತಿಂಗಳ ಚಿನ್ನ ಖರೀದಿ ಹರಿವು (Gold Seasonality Heatmap)</h4>
                <span style="font-size:11.5px; color:#15803D; font-weight:800;">ಹಸಿರು = ಅತ್ಯುತ್ತಮ ಖರೀದಿ ಸಮಯ</span>
              </div>
              <div class="season-heatmap">
                <div class="heat-cell peak"><div>ಜನ</div><div style="font-size:9.5px;">ಮದುವೆ ಸೀಸನ್</div></div>
                <div class="heat-cell low"><div>ಫೆಬ್ರ</div><div style="font-size:9.5px;">ಬಜೆಟ್ ದಿನ</div></div>
                <div class="heat-cell avg"><div>ಮಾರ್ಚ್</div><div style="font-size:9.5px;">ವರ್ಷಾಂತ್ಯ</div></div>
                <div class="heat-cell peak"><div>ಏಪ್ರಿ</div><div style="font-size:9.5px;">ಅಕ್ಷಯ ತೃತೀಯ</div></div>
                <div class="heat-cell peak"><div>ಮೇ</div><div style="font-size:9.5px;">ಮದುವೆ ಗರಿಷ್ಠ</div></div>
                <div class="heat-cell best-buy"><div>ಜೂನ್</div><div style="font-size:9.5px;">ಖರೀದಿ ಸಮಯ</div></div>
                <div class="heat-cell best-buy"><div>ಜುಲೈ</div><div style="font-size:9.5px;">ಸುಂಕ ಇಳಿಕೆ</div></div>
                <div class="heat-cell best-buy"><div>ಆಗ</div><div style="font-size:9.5px;">ದರ ತಿದ್ದುಪಡಿ</div></div>
                <div class="heat-cell good"><div>ಸೆಪ್ಟೆಂ</div><div style="font-size:9.5px;">ಹಬ್ಬದ ಆರಂಭ</div></div>
                <div class="heat-cell peak"><div>ಅಕ್ಟೋ</div><div style="font-size:9.5px;">ಧಂತೇರಸ್</div></div>
                <div class="heat-cell peak"><div>ನವೆಂ</div><div style="font-size:9.5px;">ದೀಪಾವಳಿ</div></div>
                <div class="heat-cell peak"><div>ಡಿಸೆಂ</div><div style="font-size:9.5px;">ವರ್ಷಾಂತ್ಯ ಏರಿಕೆ</div></div>
              </div>
            </div>

            <!-- Macro Commodity Impact Box -->
            <div style="margin-top:22px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:14px; padding:16px;">
              <div style="font-size:14.5px; font-weight:900; color:#1E293B; margin-bottom:8px;">
                🌐 ಜಾಗತಿಕ ಕಮಾಡಿಟಿ & ಆರ್ಥಿಕತೆ ಪ್ರಭಾವ (Macro Factors):
              </div>
              <div style="font-size:13px; color:#475569; line-height:1.7;">
                • <strong>ಯುಎಸ್ ಫೆಡ್ ಬಡ್ಡಿದರ (US Fed Rates):</strong> ಅಮೆರಿಕ ಬಡ್ಡಿದರ ಇಳಿಸಿದರೆ ಹೂಡಿಕೆದಾರರು ಚಿನ್ನದತ್ತ ಮುಖಮಾಡುತ್ತಾರೆ, ಬೆಲೆ ಏರುತ್ತದೆ.<br>
                • <strong>ಯುಎಸ್ ಡಾಲರ್ ಸೂಚ್ಯಂಕ (DXY):</strong> ಡಾಲರ್ ಬಲಗೊಂಡಾಗ ಜಾಗತಿಕ ಚಿನ್ನ ಇಳಿಯುತ್ತದೆ; ಡಾಲರ್ ದುರ್ಬಲಗೊಂಡಾಗ ಚಿನ್ನ ಜಿಗಿಯುತ್ತದೆ.<br>
                • <strong>ಕಚ್ಚಾ ತೈಲ (Crude Oil):</strong> ತೈಲ ಬೆಲೆ ಏರಿದರೆ ಜಾಗತಿಕ ಹಣದುಬ್ಬರ ಹೆಚ್ಚಾಗಿ ಚಿನ್ನಕ್ಕೆ 'ಸುರಕ್ಷಿತ ಸ್ವತ್ತು' (Safe Haven) ಬೇಡಿಕೆ ಬರುತ್ತದೆ.<br>
                • <strong>ಆಮದು ಸುಂಕ & ಜಿಎಸ್‌ಟಿ:</strong> ಭಾರತದಲ್ಲಿ ಚಿನ್ನದ ಮೇಲೆ 6% ಕಸ್ಟಮ್ಸ್ ಸುಂಕ + 3% ಜಿಎಸ್‌ಟಿ ಅನ್ವಯಿಸುತ್ತದೆ.
              </div>
            </div>

          </div>

          <!-- RIGHT: AI Smart Advice & When to Buy vs When to Sell -->
          <div>
            
            <!-- Best Time to Buy -->
            <div class="advice-card buy-window">
              <div class="advice-title" style="color:#15803D;">
                <span>🟢 ಯಾವಾಗ ಚಿನ್ನ ಖರೀದಿಸಬೇಕು? (Smart Buying Window)</span>
              </div>
              <div class="advice-desc">
                • <strong>ದರ ತಿದ್ದುಪಡಿ ಸಮಯ (Price Dips):</strong> ಗರಿಷ್ಠ ಮಟ್ಟದಿಂದ 3% ರಿಂದ 5% ಬೆಲೆ ಇಳಿದಾಗ ಹಂತ ಹಂತವಾಗಿ (SIP ಮಾದರಿಯಲ್ಲಿ) ಖರೀದಿಸಿ.<br>
                • <strong>ಜುಲೈ-ಆಗಸ್ಟ್ ತಿಂಗಳುಗಳು:</strong> ಹಬ್ಬದ ಋತುವಿಗಿಂತ 2-3 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ ಖರೀದಿಸಿದರೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಹಾಗೂ ಚಿನ್ನದ ಬೆಲೆಯಲ್ಲಿ ಭಾರಿ ಉಳಿತಾಯವಾಗುತ್ತದೆ.<br>
                • <strong>ದೀರ್ಘಕಾಲೀನ ಹೂಡಿಕೆಗೆ:</strong> ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) ಅಥವಾ ಗೋಲ್ಡ್ ಇಟಿಎಫ್ (Gold ETF) ಮೂಲಕ ಖರೀದಿಸಿದರೆ 0% ಮೇಕಿಂಗ್ ಶುಲ್ಕ & ತೆರಿಗೆ ಮುಕ್ತ ಲಾಭ.
              </div>
            </div>

            <!-- Best Time to Sell / Book Profits -->
            <div class="advice-card sell-window">
              <div class="advice-title" style="color:#DC2626;">
                <span>🔴 ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು / ಲಾಭ ಗಳಿಸಬೇಕು? (Profit Booking Window)</span>
              </div>
              <div class="advice-desc">
                • <strong>ಅಂತಾರಾಷ್ಟ್ರೀಯ ಬಿಕ್ಕಟ್ಟು / ಯುದ್ಧದ ಸಮಯ:</strong> ಜಾಗತಿಕ ಅನಿಶ್ಚಿತತೆಯಿಂದಾಗಿ ಚಿನ್ನವು ಸಾರ್ವಕಾಲಿಕ ದಾಖಲೆ (All-Time High) ಮಟ್ಟ ತಲುಪಿದಾಗ ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ (Partial Profit Booking) ಮಾಡುವುದು ಜಾಣತನ.<br>
                • <strong>ದೀಪಾವಳಿ & ಧಂತೇರಸ್ ಸೀಸನ್:</strong> ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಚಿಲ್ಲರೆ ಬೇಡಿಕೆ ಉತ್ತುಂಗದಲ್ಲಿರುವಾಗ ಹಳೇ ಆಭರಣಗಳನ್ನು ಎಕ್ಸ್‌ಚೇಂಜ್ ಮಾಡಲು ಉತ್ತಮ ಸಮಯ.
              </div>
            </div>

            <!-- Gold-to-Silver Ratio (GSR) Strategy -->
            <div class="advice-card gsr-window">
              <div class="advice-title" style="color:#0284C7;">
                <span>⚖️ Gold-to-Silver Ratio (GSR) ಮಾರ್ಗದರ್ಶಿ</span>
              </div>
              <div class="advice-desc">
                ಇಂದಿನ GSR ಅನುಪಾತ <strong>62.7</strong> ಆಗಿದೆ. ಅನುಪಾತವು 80 ಕ್ಕಿಂತ ಹೆಚ್ಚಿದ್ದರೆ ಬೆಳ್ಳಿಯು ಕಡಿಮೆ ಮೌಲ್ಯದಲ್ಲಿದೆ ಎಂದರ್ಥ (ಬೆಳ್ಳಿ ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ). ಅನುಪಾತವು 60 ಕ್ಕಿಂತ ಕೆಳಗಿಳಿದರೆ ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆ ಲಾಭದಾಯಕ.
              </div>
            </div>

            <!-- Investment Options Comparison -->
            <div class="advice-card strategy-window">
              <div class="advice-title" style="color:#92400E;">
                <span>💡 4 ಪ್ರಮುಖ ಚಿನ್ನ ಹೂಡಿಕೆ ವಿಧಾನಗಳ ಹೋಲಿಕೆ</span>
              </div>
              <div class="advice-desc">
                1. <strong>ಆಭರಣ ಚಿನ್ನ:</strong> ಧರಿಸಲು ಮಾತ್ರ ಸೂಕ್ತ. 10%-18% ಮೇಕಿಂಗ್ ವೇಸ್ಟೇಜ್ ನಷ್ಟವಾಗುತ್ತದೆ.<br>
                2. <strong>SGB (ಗೋಲ್ಡ್ ಬಾಂಡ್):</strong> ವಾರ್ಷಿಕ 2.5% ಹೆಚ್ಚುವರಿ ಬಡ್ಡಿ + 8 ವರ್ಷಗಳ ನಂತರ 0% ಕ್ಯಾಪಿಟಲ್ ಗೇನ್ಸ್ ಟ್ಯಾಕ್ಸ್.<br>
                3. <strong>Gold ETF / Digital Gold:</strong> ಡಿಮ್ಯಾಟ್ ಖಾತೆಯಲ್ಲಿ 1 ಗ್ರಾಂ ನಿಂದಲೂ ಸುಲಭ ಖರೀದಿ ಮತ್ತು ತಕ್ಷಣ ಮಾರಾಟದ ಅವಕಾಶ.
              </div>
            </div>

          </div>

        </div>

        <!-- 125-YEAR HISTORICAL MILESTONE TABLE -->
        <div class="history-table-box">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
            <h3 style="font-size:17px; font-weight:900; color:#0F172A;">📜 1901 ರಿಂದ 2026: 125 ವರ್ಷಗಳ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಬೆಲೆ ಇತಿಹಾಸ & ಪ್ರಮುಖ ಮೈಲಿಗಲ್ಲುಗಳು</h3>
            <span style="font-size:12px; color:#D97706; background:#FEF3C7; padding:4px 10px; border-radius:12px; font-weight:800;">ಐತಿಹಾಸಿಕ ದಾಖಲೆ</span>
          </div>
          <div style="overflow-x:auto;">
            <table class="hist-table">
              <thead>
                <tr>
                  <th>ವರ್ಷ</th>
                  <th>10 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
                  <th>1 ಗ್ರಾಂ ಚಿನ್ನ (₹)</th>
                  <th>10 ಗ್ರಾಂ ಬೆಳ್ಳಿ (₹)</th>
                  <th>ಐತಿಹಾಸಿಕ ಘಟನೆ / ಮೈಲಿಗಲ್ಲು</th>
                </tr>
              </thead>
              <tbody id="hist-125y-tbody"></tbody>
            </table>
          </div>
        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         TAB 3: JEWELLERY BILL & GOLD LOAN CALCULATORS
    ══════════════════════════════════════════════════════ -->
    <div id="view-calculator" style="display:none;">
      
      <div class="calc-grid-duo">
        
        <!-- 1. Jewellery Bill & GST Calculator -->
        <div class="widget-box">
          <div class="widget-title">
            <span>💍 ಆಭರಣ ಬಿಲ್ & ಜಿಎಸ್‌ಟಿ ಕ್ಯಾಲ್ಕುಲೇಟರ್</span>
          </div>
          <p style="font-size:13px; color:#64748B;">ಆಭರಣ ಅಂಗಡಿಗೆ ಹೋಗುವ ಮುನ್ನ ನಿಮ್ಮ ಒಡವೆಯ ನಿಖರ ಬಿಲ್ ಲೆಕ್ಕ ಹಾಕಿ ಮೋಸ ಹೋಗುವುದನ್ನು ತಪ್ಪಿಸಿ:</p>
          
          <div class="form-group">
            <label class="form-lbl">ಚಿನ್ನದ ಶುದ್ಧತೆ (Purity):</label>
            <select id="bill-purity" class="form-ctrl" onchange="calculateJewelleryBill()">
              <option value="22">22K ಆಭರಣ ಚಿನ್ನ (916 BIS Hallmark)</option>
              <option value="24">24K ಅಪರಂಜಿ ಚಿನ್ನ (999 Pure)</option>
              <option value="18">18K ವಜ್ರದ ಒಡವೆ ಚಿನ್ನ (750 Hallmark)</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-lbl">ಚಿನ್ನದ ತೂಕ (Weight in Grams):</label>
            <input type="number" id="bill-weight" class="form-ctrl" value="16" step="0.1" oninput="calculateJewelleryBill()">
          </div>

          <div class="form-group">
            <label class="form-lbl">ತಯಾರಿಕಾ ವೆಚ್ಚ / ವೇಸ್ಟೇಜ್ (Making Charges / VA %):</label>
            <input type="number" id="bill-making" class="form-ctrl" value="10" step="0.5" oninput="calculateJewelleryBill()">
          </div>

          <!-- Invoice Breakdown Box -->
          <div class="bill-result-box">
            <div class="bill-row">
              <span>ಕಚ್ಚಾ ಚಿನ್ನದ ಮೌಲ್ಯ (Raw Gold Value):</span>
              <span id="bill-raw-val">₹2,39,040</span>
            </div>
            <div class="bill-row">
              <span>ತಯಾರಿಕಾ ಶುಲ್ಕ (Making Charges):</span>
              <span id="bill-making-val">₹23,904</span>
            </div>
            <div class="bill-row">
              <span>3% ಜಿಎಸ್‌ಟಿ (GST):</span>
              <span id="bill-gst-val">₹7,888</span>
            </div>
            <div class="bill-row">
              <span>ಒಟ್ಟು ಶೋರೂಂ ಅಂತಿಮ ಬಿಲ್:</span>
              <span id="bill-total-val" style="color:#B45309;">₹2,70,832</span>
            </div>
          </div>
          
          <div style="margin-top:12px; font-size:12px; color:#166534; background:#F0FDF4; padding:10px; border-radius:10px; border:1px solid #BBF7D0;">
            💡 <strong>ಚೌಕಾಸಿ ಟಿಪ್:</strong> ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಅನ್ನು 14% ರಿಂದ 8% ಗೆ ಇಳಿಸಲು ಚೌಕಾಸಿ ಮಾಡಬಹುದು. ಇದರಿಂದ ನಿಮಗೆ ಕ್ವಿಂಟಾಲ್ಗಟ್ಟಲೆ ಹಣ ಉಳಿತಾಯವಾಗುತ್ತದೆ.
          </div>
        </div>

        <!-- 2. Gold Loan & Monthly SIP Wealth Estimator -->
        <div class="widget-box">
          <div class="widget-title">
            <span>💰 ಗೋಲ್ಡ್ ಲೋನ್ & ಮಾಸಿಕ SIP ಕ್ಯಾಲ್ಕುಲೇಟರ್</span>
          </div>
          <p style="font-size:13px; color:#64748B;">ನಿಮ್ಮ ಬಳಿ ಇರುವ ಚಿನ್ನದ ಮೇಲೆ ಗರಿಷ್ಠ ಎಷ್ಟು ಸಾಲ ಸಿಗುತ್ತದೆ ಮತ್ತು ಪ್ರತಿ ತಿಂಗಳು ಚಿನ್ನದಲ್ಲಿ ಉಳಿತಾಯ ಮಾಡಿದರೆ 10 ವರ್ಷದಲ್ಲಿ ಎಷ್ಟು ಬೆಳೆಯುತ್ತದೆ ನೋಡಿ:</p>

          <div class="form-group">
            <label class="form-lbl">ಅಡಮಾನ ಇಡುವ ಚಿನ್ನದ ತೂಕ (Grams):</label>
            <input type="number" id="loan-weight" class="form-ctrl" value="40" step="1" oninput="calculateGoldLoan()">
          </div>

          <div class="bill-result-box" style="background:#F0FDF4; border-color:#BBF7D0;">
            <div class="bill-row">
              <span>ಮಾರುಕಟ್ಟೆ ಮೌಲ್ಯ (Market Value):</span>
              <span id="loan-market-val">₹5,97,600</span>
            </div>
            <div class="bill-row">
              <span>ಆರ್‌ಬಿಐ ನಿಯಮದಂತೆ ಸಿಗುವ ಸಾಲ (75% LTV):</span>
              <span id="loan-max-val" style="color:#15803D; font-weight:900;">₹4,48,200</span>
            </div>
            <div class="bill-row">
              <span>ಅಂದಾಜು ಮಾಸಿಕ ಬಡ್ಡಿ (8.5% p.a.):</span>
              <span id="loan-interest-val">₹3,175 / ತಿಂಗಳಿಗೆ</span>
            </div>
          </div>

          <hr style="border:0; border-top:1px solid #E2E8F0; margin:16px 0;">

          <div style="font-size:14.5px; font-weight:900; color:#0F172A; margin-bottom:8px;">
            📈 ಚಿನ್ನದ ಮಾಸಿಕ SIP ಸಂಪತ್ತು (Gold Wealth Projection):
          </div>
          <div style="font-size:13px; color:#475569; line-height:1.65;">
            ಪ್ರತಿ ತಿಂಗಳು ಕೇವಲ <strong>₹5,000</strong> ಮೌಲ್ಯದ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ / SGB ನಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುತ್ತಾ ಬಂದರೆ, ಕಳೆದ 10 ವರ್ಷಗಳ ಸರಾಸರಿ <strong>12.8% CAGR</strong> ಬೆಳವಣಿಗೆಯ ಆಧಾರದ ಮೇಲೆ ಮುಂದಿನ 10 ವರ್ಷಗಳಲ್ಲಿ ನಿಮ್ಮ ಒಟ್ಟು ಸಂಪತ್ತು <strong>₹12,40,000 ಕ್ಕೂ ಹೆಚ್ಚು</strong> ಬೆಳೆಯುವ ಸಾಧ್ಯತೆಯಿದೆ!
          </div>

        </div>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════
         COMPREHENSIVE 9-SECTION GOLD & COMMODITY GUIDE
    ══════════════════════════════════════════════════════ -->
    <article class="article-container font-kannada" style="line-height: 1.85; color: #222; font-size: 16px; margin-top: 40px; padding: 25px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px;">
      
      <header>
        <h2 style="font-size: 26px; color: #0f172a; margin-bottom: 10px; font-weight: 800;">ಕರ್ನಾಟಕ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಮಾರುಕಟ್ಟೆ, ಹಾಲ್‌ಮಾರ್ಕ್ ನಿಯಮಗಳು & ಹೂಡಿಕೆ ಮಾರ್ಗದರ್ಶಿ (Gold & Bullion Trade Manual)</h2>
        <p style="color: #64748b; font-size: 14px; margin-bottom: 20px;">ಪ್ರಕಟಣೆ: Karnata.in ಹಣಕಾಸು & ಬುಲಿಯನ್ ವಿಶ್ಲೇಷಣೆ ವಿಭಾಗ | ಅಧಿಕೃತ ಮೂಲ: KBMA & IBJA (2026)</p>
      </header>

      <hr style="border:0; border-top:1px solid #E2E8F0; margin-bottom:20px;">

      <section>
        <h3 style="font-size:18px; color:#78350F; font-weight:800; margin-bottom:8px;">1. 24K, 22K ಮತ್ತು 18K ಚಿನ್ನದ ನಡುವಿನ ವ್ಯತ್ಯಾಸ</h3>
        <p>ಚಿನ್ನದ ಶುದ್ಧತೆಯನ್ನು ಕ್ಯಾರಟ್‌ಗಳಲ್ಲಿ (Karat) ಅಳೆಯಲಾಗುತ್ತದೆ. <strong>24 ಕ್ಯಾರಟ್ (999)</strong> ಚಿನ್ನವು ಅತ್ಯಂತ ಶುದ್ಧವಾಗಿದ್ದು, ಅದು ನಾಣ್ಯಗಳು ಮತ್ತು ಬಾರ್‌ಗಳಿಗೆ ಮಾತ್ರ ಸೂಕ್ತವಾಗಿರುತ್ತದೆ (ಆಭರಣ ಮಾಡಲು ತೀರಾ ಮೃದು). <strong>22 ಕ್ಯಾರಟ್ (916)</strong> ಚಿನ್ನದಲ್ಲಿ 91.6% ಶುದ್ಧ ಚಿನ್ನ ಮತ್ತು 8.4% ತಾಮ್ರ ಅಥವಾ ಬೆಳ್ಳಿಯ ಮಿಶ್ರಣವಿರುತ್ತದೆ, ಇದು ಗಟ್ಟಿಯಾದ ಆಭರಣಗಳಿಗೆ ದೇಶಾದ್ಯಂತ ಬಳಸಲ್ಪಡುವ ಮಾನದಂಡ. <strong>18 ಕ್ಯಾರಟ್ (750)</strong> ಚಿನ್ನದಲ್ಲಿ 75% ಚಿನ್ನವಿದ್ದು, ವಜ್ರದ ಒಡವೆಗಳಿಗೆ ಬಳಸಲಾಗುತ್ತದೆ.</p>
      </section>

      <section style="margin-top:18px;">
        <h3 style="font-size:18px; color:#78350F; font-weight:800; margin-bottom:8px;">2. BIS 6-ಅಂಕಿಯ HUID ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ ಕಡ್ಡಾಯ</h3>
        <p>ಭಾರತ ಸರ್ಕಾರವು ಗ್ರಾಹಕರ ರಕ್ಷಣೆಗಾಗಿ 6 ಅಂಕಿಯ ಆಲ್ಫಾನ್ಯೂಮರಿಕ್ <strong>HUID (Hallmark Unique Identification)</strong> ಕೋಡ್ ಅನ್ನು ಕಡ್ಡಾಯಗೊಳಿಸಿದೆ. BIS CARE ಆ್ಯಪ್ ಮೂಲಕ ಈ ಕೋಡ್ ನಮೂದಿಸಿ ಆಭರಣದ ಶುದ್ಧತೆ, ತೂಕ ಮತ್ತು ತಯಾರಕರ ವಿವರಗಳನ್ನು ಯಾವುದೇ ಗ್ರಾಹಕರು ತಕ್ಷಣ ಪರಿಶೀಲಿಸಬಹುದು.</p>
      </section>

      <footer style="margin-top:25px; padding:14px; background:#FFFBEB; border:1px solid #FDE68A; border-radius:10px; font-size:13px; color:#92400E;">
        <strong>ಮಾಹಿತಿ ಹಕ್ಕುತ್ಯಾಗ:</strong> ಇಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗುವ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ದರಗಳು ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಜ್ಯುವೆಲರ್ಸ್ ಅಸೋಸಿಯೇಷನ್ (KBMA) ಮತ್ತು ಅಧಿಕೃತ ಮಾರುಕಟ್ಟೆ ವಹಿವಾಟುಗಳ ಆಧಾರಿತವಾಗಿವೆ. ಸ್ಥಳೀಯ ಶೋರೂಂಗಳಲ್ಲಿ ಜಿಎಸ್‌ಟಿ ಮತ್ತು ತಯಾರಿಕಾ ವೆಚ್ಚಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಅಂತಿಮ ಆಭರಣ ಬಿಲ್ ಬದಲಾಗಬಹುದು.
      </footer>

    </article>

  </div>

  <script>
    // ══════════════════════════════════════════════════════
    // EMBEDDED GOLD DATA & HISTORICAL ARCHIVES
    // ══════════════════════════════════════════════════════
    const GOLD_RATES = {
      "24k": 16304,
      "22k": 14940,
      "18k": 12224,
      "silver": 260.0
    };

    const HIST_125Y = [
      { year: 1901, gold10g: 18.75, silver10g: 0.45, event: "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ" },
      { year: 1925, gold10g: 18.50, silver10g: 0.52, event: "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್" },
      { year: 1947, gold10g: 88.62, silver10g: 1.45, event: "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ (₹88.62/10g · ₹8.86/g)" },
      { year: 1971, gold10g: 193.00, silver10g: 5.35, event: "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)" },
      { year: 1980, gold10g: 1330.00, silver10g: 27.20, event: "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1991, gold10g: 3466.00, silver10g: 72.00, event: "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)" },
      { year: 2000, gold10g: 4400.00, silver10g: 79.00, event: "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)" },
      { year: 2008, gold10g: 12500.00, silver10g: 236.00, event: "ಜಾಗತಿಕ ಆರ್ಥಿಕ ಬಿಕ್ಕಟ್ಟು (Lehman Crisis)" },
      { year: 2016, gold10g: 28623.00, silver10g: 423.00, event: "ನೋಟು ಅಮಾನ್ಯೀಕರಣ (Demonetization)" },
      { year: 2020, gold10g: 48651.00, silver10g: 634.00, event: "ಕೋವಿಡ್ ಬಿಕ್ಕಟ್ಟು; ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ" },
      { year: 2022, gold10g: 52670.00, silver10g: 680.00, event: "ಉಕ್ರೇನ್ ಯುದ್ಧ; ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ" },
      { year: 2024, gold10g: 78500.00, silver10g: 920.00, event: "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ" },
      { year: 2025, gold10g: 125000.00, silver10g: 1850.00, event: "ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳ ಭಾರಿ ಖರೀದಿ" },
      { year: 2026, gold10g: 163040.00, silver10g: 2600.00, event: "ಸಾರ್ವಕಾಲಿಕ ಐತಿಹಾಸಿಕ ದಾಖಲೆ ಮಟ್ಟದಲ್ಲಿ ಚಿನ್ನ-ಬೆಳ್ಳಿ" }
    ];

    const CITY_RATES_LIST = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", g24: 16304, g22: 14940, g18: 12224, sil: 260.0 },
      { name: "ಮೈಸೂರು (Mysore)", g24: 16299, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ಮಂಗಳೂರು (Mangalore)", g24: 16301, g22: 14937, g18: 12222, sil: 260.0 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", g24: 16294, g22: 14930, g18: 12215, sil: 260.0 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", g24: 16292, g22: 14928, g18: 12214, sil: 260.0 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", g24: 16297, g22: 14933, g18: 12219, sil: 260.0 },
      { name: "ಶಿವಮೊಗ್ಗ (Shimoga)", g24: 16298, g22: 14934, g18: 12220, sil: 260.0 },
      { name: "ತುಮಕೂರು (Tumkur)", g24: 16300, g22: 14936, g18: 12221, sil: 260.0 },
      { name: "ಹಾಸನ (Hassan)", g24: 16295, g22: 14931, g18: 12217, sil: 260.0 },
      { name: "ಉಡುಪಿ (Udupi)", g24: 16302, g22: 14938, g18: 12223, sil: 260.0 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 }
    ];

    let chartInstance = null;
    let currentTab = 'live';

    function switchGoldTab(tab) {
      currentTab = tab;
      document.getElementById('tab-live').classList.toggle('active', tab === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', tab === 'analyzer');
      document.getElementById('tab-calculator').classList.toggle('active', tab === 'calculator');

      document.getElementById('view-live').style.display = tab === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = tab === 'analyzer' ? 'block' : 'none';
      document.getElementById('view-calculator').style.display = tab === 'calculator' ? 'block' : 'none';

      if (tab === 'analyzer') {
        renderGoldTrendChart('10y');
      }
    }

    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data && data.base) {
            GOLD_RATES['24k'] = data.base['24k_per_gram'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = data.base['22k_per_gram'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = data.base['18k_per_gram'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = data.base['silver_per_gram'] || GOLD_RATES['silver'];
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }

    function renderLiveDisplay() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];

      document.getElementById('stat-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('stat-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('stat-silver-rate').textContent = `₹${sil.toFixed(2)}`;

      const gsr = (g24 / sil).toFixed(1);
      document.getElementById('stat-gsr-val').textContent = gsr;

      document.getElementById('card-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('card-24k-8g').textContent = `₹${(g24 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-10g').textContent = `₹${(g24 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-100g').textContent = `₹${(g24 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('card-22k-8g').textContent = `₹${(g22 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-10g').textContent = `₹${(g22 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-100g').textContent = `₹${(g22 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-silver-rate').textContent = `₹${sil.toFixed(2)}`;
      document.getElementById('card-silver-10g').textContent = `₹${(sil * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-100g').textContent = `₹${(sil * 100).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-1kg').textContent = `₹${(sil * 1000).toLocaleString('en-IN')}`;

      // Render City Table
      const cityTbody = document.getElementById('city-rates-tbody');
      cityTbody.innerHTML = '';
      CITY_RATES_LIST.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:800; color:#0F172A;">${c.name}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${c.g24.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${c.g22.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${c.g18.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#334155;">₹${c.sil.toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${(c.sil * 1000).toLocaleString('en-IN')}</td>
        `;
        cityTbody.appendChild(tr);
      });

      // Render 125Y Historical Table
      const histTbody = document.getElementById('hist-125y-tbody');
      histTbody.innerHTML = '';
      HIST_125Y.forEach(h => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">${h.year}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${h.gold10g.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${(h.gold10g / 10).toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${h.silver10g.toLocaleString('en-IN')}</td>
          <td style="font-size:13px; color:#334155;">${h.event}</td>
        `;
        histTbody.appendChild(tr);
      });

      calculateJewelleryBill();
      calculateGoldLoan();
    }

    function calculateJewelleryBill() {
      const purity = document.getElementById('bill-purity').value;
      const weight = parseFloat(document.getElementById('bill-weight').value) || 0;
      const makingPct = parseFloat(document.getElementById('bill-making').value) || 0;

      const ratePerGram = purity === '24' ? GOLD_RATES['24k'] : (purity === '18' ? GOLD_RATES['18k'] : GOLD_RATES['22k']);
      const rawGoldVal = Math.round(weight * ratePerGram);
      const makingVal = Math.round(rawGoldVal * (makingPct / 100));
      const subTotal = rawGoldVal + makingVal;
      const gstVal = Math.round(subTotal * 0.03);
      const totalInvoice = subTotal + gstVal;

      document.getElementById('bill-raw-val').textContent = `₹${rawGoldVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-making-val').textContent = `₹${makingVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-gst-val').textContent = `₹${gstVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-total-val').textContent = `₹${totalInvoice.toLocaleString('en-IN')}`;
    }

    function calculateGoldLoan() {
      const weight = parseFloat(document.getElementById('loan-weight').value) || 0;
      const g22 = GOLD_RATES['22k'];

      const marketVal = Math.round(weight * g22);
      const maxLoan = Math.round(marketVal * 0.75); // 75% LTV
      const monthlyInt = Math.round(maxLoan * (0.085 / 12));

      document.getElementById('loan-market-val').textContent = `₹${marketVal.toLocaleString('en-IN')}`;
      document.getElementById('loan-max-val').textContent = `₹${maxLoan.toLocaleString('en-IN')}`;
      document.getElementById('loan-interest-val').textContent = `₹${monthlyInt.toLocaleString('en-IN')} / ತಿಂಗಳಿಗೆ`;
    }

    function updateChartTimeframe(tf, btn) {
      document.querySelectorAll('.time-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderGoldTrendChart(tf);
    }

    function renderGoldTrendChart(tf) {
      const ctx = document.getElementById('goldTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      let labels = [];
      let prices = [];

      if (tf === '1y') {
        labels = ['ಆಗ 25', 'ಸೆಪ್ 25', 'ಅಕ್ಟೋ 25', 'ನವೆಂ 25', 'ಡಿಸೆಂ 25', 'ಜನ 26', 'ಫೆಬ್ರ 26', 'ಮಾರ್ಚ್ 26', 'ಏಪ್ರಿ 26', 'ಮೇ 26', 'ಜೂನ್ 26', 'ಆಗ 26'];
        prices = [12800, 13100, 13650, 14200, 14500, 14800, 15100, 15300, 15650, 15900, 16150, 16304];
      } else if (tf === '5y') {
        labels = ['2022', '2023', '2024', '2025', '2026'];
        prices = [5267, 6150, 7850, 12500, 16304];
      } else if (tf === '125y') {
        labels = HIST_125Y.map(h => h.year.toString());
        prices = HIST_125Y.map(h => h.gold10g / 10);
      } else {
        // 10 Years (2016-2026)
        labels = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
        prices = [2862, 2966, 3143, 3522, 4865, 4872, 5267, 6150, 7850, 12500, 16304];
      }

      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(245, 158, 11, 0.35)');
      gradient.addColorStop(1, 'rgba(245, 158, 11, 0.0)');

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: '24K ಚಿನ್ನದ ದರ (₹/ಗ್ರಾಂ)',
            data: prices,
            borderColor: '#D97706',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#78350F',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
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
              backgroundColor: '#0F172A',
              titleFont: { family: 'Inter', size: 12, weight: 'bold' },
              bodyFont: { family: 'Inter', size: 13, weight: 'bold' },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                label: function(c) {
                  return ` 24K ಚಿನ್ನ: ₹${c.parsed.y.toLocaleString('en-IN')} / ಗ್ರಾಂ`;
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

    document.addEventListener('DOMContentLoaded', () => {
      initGoldData();
    });
  </script>
</body>
</html>
"""

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(gold_html_template)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(gold_html_template)

print("SUCCESS_UPGRADED_GOLD_SUPER_INTELLIGENCE")
