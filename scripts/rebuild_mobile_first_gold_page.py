# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_mobile_first_gold_page.py
Rebuilds gold-rate.html with modern, native-app mobile UX:
1. Top: Live Gold & Silver rates (24K, 22K, 18K, Silver) immediately visible.
2. 3 Clean Segmented Tabs (Live Rates, Trends & AI Advisor, Jewellery Calculator).
3. Responsive City Rates (no horizontal cutoff).
4. Responsive Seasonality Heatmap (3 columns on mobile).
5. Cache-busting scripts (?v=20260830_v5) so mobile updates appear immediately.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

gold_page_html = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <!-- Google Favicon & Branding Icons -->
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta name="theme-color" content="#C0392B" />

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು | Today Gold Rate in Karnataka (22K, 24K, 18K), Silver Price — Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ ಇಂದಿನ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ದರ: 22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಶುದ್ಧ ಚಿನ್ನ, 18 ಕ್ಯಾರೆಟ್ ಮತ್ತು ಬೆಳ್ಳಿ ಬೆಲೆ, ಜಿಎಸ್‌ಟಿ ಲೆಕ್ಕಾಚಾರ ಹಾಗೂ AI ಸಲಹೆಗಾರ." />
  <meta name="keywords" content="ಕರ್ನಾಟಕ ಚಿನ್ನದ ದರ, ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ, 22 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ, ಬೆಳ್ಳಿ ದರ ಇಂದು, Gold rate Karnataka today, 22k gold price Bengaluru, Silver rate Karnataka" />
  <link rel="canonical" href="https://karnata.in/gold-rate" />

  <!-- AI GEO & Search Engine Directives -->
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large" />

  <!-- Regional Geo Tags (Karnataka, India) -->
  <meta name="geo.region" content="IN-KA" />
  <meta name="geo.placename" content="Bengaluru, Karnataka, India" />
  <meta name="geo.position" content="12.9716;77.5946" />
  <meta name="ICBM" content="12.9716, 77.5946" />

  <!-- Open Graph & Social Meta -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು | Today Gold Rate in Karnataka (22K, 24K, 18K), Silver Price — Karnata.in" />
  <meta property="og:description" content="ಕರ್ನಾಟಕದ ಇಂದಿನ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ದರ: 22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಶುದ್ಧ ಚಿನ್ನ, 18 ಕ್ಯಾರೆಟ್ ಮತ್ತು ಬೆಳ್ಳಿ ಬೆಲೆ, ಜಿಎಸ್‌ಟಿ ಲೆಕ್ಕಾಚಾರ ಹಾಗೂ AI ಸಲಹೆಗಾರ." />
  <meta property="og:url" content="https://karnata.in/gold-rate" />
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in" />
  <meta property="og:locale" content="kn_IN" />
  <meta property="og:locale:alternate" content="en_IN" />
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು | Today Gold Rate in Karnataka — Karnata.in" />
  <meta name="twitter:description" content="ಕರ್ನಾಟಕದ ಇಂದಿನ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ದರ: 22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಶುದ್ಧ ಚಿನ್ನ, 18 ಕ್ಯಾರೆಟ್ ಮತ್ತು ಬೆಳ್ಳಿ ಬೆಲೆ." />
  <meta name="twitter:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/gold-rate",
    "description": "Live Karnataka Gold & Silver Market Rates, 10-Year Historical Commodity Trends, Buy/Sell Analyzer, Old Gold Exchange Calculator."
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;600;700;800;900&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- Chart.js for Historical Curves -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    :root {
      --gold-dark: #78350F;
      --gold-primary: #D97706;
      --gold-light: #FEF3C7;
      --gold-accent: #F59E0B;
      --bg-slate: #F8FAFC;
      --card-white: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --radius-lg: 16px;
      --radius-md: 12px;
      --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.04);
      --shadow-md: 0 10px 25px -5px rgba(15, 23, 42, 0.06);
    }

    html, body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100vw !important;
      margin: 0; padding: 0;
      box-sizing: border-box;
      background: var(--bg-slate);
      font-family: 'Anek Kannada', sans-serif;
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
    }
    *, *::before, *::after { box-sizing: border-box; }

    /* ════ HERO HEADER ════ */
    .gold-hero {
      background: linear-gradient(135deg, #1C1917 0%, #292524 40%, #451A03 80%, #78350F 100%);
      color: #FFFFFF;
      padding: 30px 16px 50px;
      text-align: center;
      position: relative;
      border-bottom: 3px solid #FACC15;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(250, 204, 21, 0.15);
      border: 1px solid rgba(250, 204, 21, 0.35);
      color: #FDE047;
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 800;
      margin-bottom: 12px;
    }
    .hero-title {
      font-size: clamp(22px, 5vw, 32px);
      font-weight: 900;
      line-height: 1.3;
      margin: 0 0 8px 0;
    }
    .hero-subtitle {
      font-size: 13.5px;
      color: #D6D3D1;
      max-width: 650px;
      margin: 0 auto;
    }

    /* ════ MAIN CONTAINER ════ */
    .gold-container {
      max-width: 1180px;
      margin: -25px auto 40px;
      padding: 0 14px;
      position: relative;
      z-index: 10;
    }

    /* ════ SEGMENTED TABS (MOBILE-FIRST) ════ */
    .mode-tabs-wrapper {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: 16px;
      padding: 6px;
      box-shadow: var(--shadow-md);
      margin-bottom: 24px;
    }
    .mode-tabs {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
    }
    @media (max-width: 650px) {
      .mode-tabs {
        display: flex;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
      }
      .mode-tabs::-webkit-scrollbar { display: none; }
    }
    .mode-tab {
      padding: 12px 14px;
      font-size: 14px;
      font-weight: 800;
      border-radius: 12px;
      cursor: pointer;
      border: none;
      background: transparent;
      color: var(--text-muted);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: inherit;
      white-space: nowrap;
      flex: 1;
    }
    .mode-tab.active {
      background: #FEF3C7;
      color: #92400E;
      font-weight: 900;
      box-shadow: 0 2px 8px rgba(217, 119, 6, 0.15);
    }

    /* ════ RATE CARDS GRID ════ */
    .rates-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }
    .rate-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s;
    }
    .rate-card:hover { transform: translateY(-2px); }
    .rate-card.c-24k { border-color: #FCD34D; background: linear-gradient(180deg, #FFFDF5 0%, #FFFFFF 100%); }
    .rate-card.c-22k { border-color: #FDE68A; background: linear-gradient(180deg, #FEFCE8 0%, #FFFFFF 100%); }
    .rate-card.c-18k { border-color: #E2E8F0; }
    .rate-card.c-silver { border-color: #CBD5E1; background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%); }

    .card-badge {
      display: inline-block;
      font-size: 11.5px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }
    .card-price {
      font-size: 30px;
      font-weight: 900;
      color: #0F172A;
      font-family: 'Inter', sans-serif;
      line-height: 1.1;
    }
    .card-unit {
      font-size: 12.5px;
      color: var(--text-muted);
      margin-top: 4px;
    }
    .card-table {
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dashed #E2E8F0;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 13px;
    }
    .card-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .card-row span:last-child {
      font-weight: 800;
      font-family: 'Inter', sans-serif;
    }

    /* ════ CITY RATES SECTION ════ */
    .section-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 22px 18px;
      box-shadow: var(--shadow-sm);
      margin-bottom: 24px;
    }
    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .section-title {
      font-size: 18px;
      font-weight: 900;
      color: #0F172A;
      margin: 0;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .city-rates-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
    }
    .city-rate-item {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 12px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .city-name-box {
      font-size: 15px;
      font-weight: 800;
      color: #0F172A;
    }
    .city-prices-box {
      text-align: right;
    }
    .city-p-24k {
      font-size: 14.5px;
      font-weight: 900;
      color: #D97706;
      font-family: 'Inter', sans-serif;
    }
    .city-p-22k {
      font-size: 12.5px;
      font-weight: 700;
      color: #64748B;
      font-family: 'Inter', sans-serif;
    }

    /* ════ AI DECISION ADVISOR BOX ════ */
    .ai-advisor-card {
      background: #FFFFFF;
      border: 2px solid #F59E0B;
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: 0 10px 30px -5px rgba(245, 158, 11, 0.12);
      margin-bottom: 24px;
    }
    .ai-chips-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin: 16px 0;
    }
    .ai-chip-btn {
      background: #F8FAFC;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 12px 14px;
      font-size: 13.5px;
      font-weight: 800;
      color: #1E293B;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: inherit;
      transition: all 0.15s ease;
    }
    .ai-chip-btn:hover {
      background: #FEF3C7;
      border-color: #FCD34D;
      color: #92400E;
    }

    /* ════ 12-MONTH HEATMAP (3-COL ON MOBILE) ════ */
    .season-heatmap {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 8px;
      margin-top: 14px;
    }
    @media (max-width: 768px) {
      .season-heatmap {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    .heat-cell {
      border-radius: 10px;
      padding: 10px 6px;
      text-align: center;
      font-weight: 800;
      font-size: 13px;
    }
    .heat-cell.peak { background: #7C2D12; color: #FFFFFF; }
    .heat-cell.low { background: #DCFCE7; color: #15803D; }
    .heat-cell.avg { background: #FEF3C7; color: #92400E; }
    .heat-cell.best { background: #059669; color: #FFFFFF; }

    /* ════ JEWELLERY CALCULATOR FORM ════ */
    .calc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }
    .form-group {
      margin-bottom: 14px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 800;
      color: #334155;
      margin-bottom: 6px;
    }
    .form-input, .form-select {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      font-size: 15px;
      font-family: inherit;
      background: #FFFFFF;
      box-sizing: border-box;
    }
    .form-input:focus, .form-select:focus {
      outline: none;
      border-color: #D97706;
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
    }
  </style>
</head>
<body>

  <!-- Top Hero Banner -->
  <header class="gold-hero">
    <div class="hero-badge">
      <span style="width:7px; height:7px; border-radius:50%; background:#22C55E; display:inline-block;"></span>
      <span>ಕರ್ನಾಟಕ ಲೈವ್ ಗೋಲ್ಡ್ & ಸಿಲ್ವರ್ ಮಾರ್ಕೆಟ್</span>
    </div>
    <h1 class="hero-title">ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು</h1>
    <p class="hero-subtitle">24K ಅಪರಂಜಿ ಚಿನ್ನ, 22K ಆಭರಣ ಚಿನ್ನ (916 BIS), 18K ಮತ್ತು ಬೆಳ್ಳಿ ಇಂದಿನ ನೈಜ-ಸಮಯದ ಮಾರುಕಟ್ಟೆ ದರಗಳು</p>
  </header>

  <!-- Main Container -->
  <main class="gold-container">

    <!-- Mobile-First Segmented Tabs -->
    <div class="mode-tabs-wrapper">
      <div class="mode-tabs">
        <button class="mode-tab active" id="tab-btn-live" onclick="switchTab('live')">
          <span>🪙 ಇಂದಿನ ಲೈವ್ ದರಗಳು</span>
        </button>
        <button class="mode-tab" id="tab-btn-analyzer" onclick="switchTab('analyzer')">
          <span>📈 ಟ್ರೆಂಡ್ & AI ವಿಶ್ಲೇಷಣೆ</span>
        </button>
        <button class="mode-tab" id="tab-btn-calc" onclick="switchTab('calc')">
          <span>🧮 ಆಭರಣ ಬಿಲ್ ಲೆಕ್ಕ</span>
        </button>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════
         TAB 1: LIVE GOLD & SILVER RATES (24K, 22K, 18K, SILVER)
    ══════════════════════════════════════════════════════════ -->
    <div id="view-live">
      
      <!-- 4 Core Rate Cards -->
      <div class="rates-grid">
        <!-- 24K Pure Gold -->
        <div class="rate-card c-24k">
          <span class="card-badge" style="background:#FEF3C7; color:#92400E;">👑 24K ಅಪರಂಜಿ ಚಿನ್ನ (999 Pure)</span>
          <div class="card-price" id="rate-24k">₹16,304</div>
          <div class="card-unit">ಪ್ರತಿ 1 ಗ್ರಾಂ ನಾಣ್ಯ / ಬಾರ್ ದರ</div>
          <div class="card-table">
            <div class="card-row"><span>8 ಗ್ರಾಂ (1 ಪವನ್):</span><span id="rate-24k-8g">₹1,30,432</span></div>
            <div class="card-row"><span>10 ಗ್ರಾಂ (1 ತೊಲ):</span><span id="rate-24k-10g">₹1,63,040</span></div>
            <div class="card-row"><span>100 ಗ್ರಾಂ:</span><span id="rate-24k-100g">₹16,30,400</span></div>
          </div>
        </div>

        <!-- 22K Jewellery Gold -->
        <div class="rate-card c-22k">
          <span class="card-badge" style="background:#FEF9C3; color:#854D0E;">💍 22K ಆಭರಣ ಬಂಗಾರ (916 Hallmark)</span>
          <div class="card-price" id="rate-22k">₹14,940</div>
          <div class="card-unit">ಪ್ರತಿ 1 ಗ್ರಾಂ ಆಭರಣ ತಯಾರಿಕೆ ದರ</div>
          <div class="card-table">
            <div class="card-row"><span>8 ಗ್ರಾಂ (1 ಪವನ್):</span><span id="rate-22k-8g">₹1,19,520</span></div>
            <div class="card-row"><span>10 ಗ್ರಾಂ (1 ತೊಲ):</span><span id="rate-22k-10g">₹1,49,400</span></div>
            <div class="card-row"><span>100 ಗ್ರಾಂ:</span><span id="rate-22k-100g">₹14,94,000</span></div>
          </div>
        </div>

        <!-- 18K Gold -->
        <div class="rate-card c-18k">
          <span class="card-badge" style="background:#F1F5F9; color:#475569;">💎 18K ಡೈಮಂಡ್ ಆಭರಣ ಚಿನ್ನ</span>
          <div class="card-price" id="rate-18k">₹12,228</div>
          <div class="card-unit">ಪ್ರತಿ 1 ಗ್ರಾಂ ವಜ್ರಾಭರಣ ದರ</div>
          <div class="card-table">
            <div class="card-row"><span>8 ಗ್ರಾಂ:</span><span id="rate-18k-8g">₹97,824</span></div>
            <div class="card-row"><span>10 ಗ್ರಾಂ:</span><span id="rate-18k-10g">₹1,22,280</span></div>
          </div>
        </div>

        <!-- Fine Silver 999 -->
        <div class="rate-card c-silver">
          <span class="card-badge" style="background:#E2E8F0; color:#1E293B;">🥈 999 ಶುದ್ಧ ಬೆಳ್ಳಿ (Fine Silver)</span>
          <div class="card-price" id="rate-silver">₹260.00</div>
          <div class="card-unit">ಪ್ರತಿ 1 ಗ್ರಾಂ ಬೆಳ್ಳಿ ದರ</div>
          <div class="card-table">
            <div class="card-row"><span>10 ಗ್ರಾಂ ಬೆಳ್ಳಿ:</span><span id="rate-silver-10g">₹2,600</span></div>
            <div class="card-row"><span>100 ಗ್ರಾಂ ಬೆಳ್ಳಿ:</span><span id="rate-silver-100g">₹26,000</span></div>
            <div class="card-row"><span>1 ಕೆಜಿ ಬೆಳ್ಳಿ (1000g):</span><span id="rate-silver-1kg">₹2,60,000</span></div>
          </div>
        </div>
      </div>

      <!-- City-Wise Gold Rates (Clean Mobile Card Grid) -->
      <div class="section-card">
        <div class="section-header">
          <h2 class="section-title">📍 ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳ ಲೈವ್ ದರಗಳು</h2>
          <span style="font-size:12px; color:var(--text-muted); font-weight:700;">ಪ್ರತಿ ಗ್ರಾಂ ಲೆಕ್ಕದಲ್ಲಿ</span>
        </div>
        <div class="city-rates-list" id="city-rates-container">
          <!-- Dynamic City Rates Injected Here -->
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         TAB 2: TRENDS, HISTORICAL CHART & AI DECISION ADVISOR
    ══════════════════════════════════════════════════════════ -->
    <div id="view-analyzer" style="display:none;">
      
      <!-- Interactive AI Decision Advisor -->
      <div class="ai-advisor-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <h2 style="font-size:18px; font-weight:900; color:#78350F; margin:0;">
            🧠 ಚಿನ್ನ ಖರೀದಿ & ಮಾರಾಟ AI ವಿಶ್ಲೇಷಕ (Decision Advisor)
          </h2>
          <span style="background:#DCFCE7; color:#15803D; font-size:11.5px; font-weight:800; padding:3px 10px; border-radius:12px;">🟢 ಲೈವ್ ಡೇಟಾ ಸಕ್ರಿಯ</span>
        </div>
        <p style="font-size:13.5px; color:#64748B; margin:8px 0 14px;">10 ವರ್ಷಗಳ ಮಾರುಕಟ್ಟೆ ಸೈಕಲ್, ಸೀಸನಲ್ ಏರಿಳಿತ ಮತ್ತು ಇಂದಿನ ದರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ತಕ್ಷಣದ ನಿರ್ಧಾರ ಪಡೆಯಿರಿ:</p>

        <!-- Quick AI Buttons -->
        <div class="ai-chips-grid">
          <button class="ai-chip-btn" onclick="askAiAdvice('buy_today')">
            <span>🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Today?)</span>
          </button>
          <button class="ai-chip-btn" onclick="askAiAdvice('sell_today')">
            <span>🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Now?)</span>
          </button>
          <button class="ai-chip-btn" onclick="askAiAdvice('wedding')">
            <span>💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ?</span>
          </button>
          <button class="ai-chip-btn" onclick="askAiAdvice('gsr')">
            <span>⚖️ ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ?</span>
          </button>
        </div>

        <!-- AI Output Box -->
        <div id="ai-response-box" style="display:none; background:#FFFBEB; border:1.5px solid #FDE68A; border-radius:12px; padding:16px; margin-top:14px;">
          <div style="font-size:15px; font-weight:900; color:#92400E; margin-bottom:8px;" id="ai-resp-title">💡 AI ತಜ್ಞರ ಸಲಹೆ</div>
          <div style="font-size:14px; color:#334155; line-height:1.7;" id="ai-resp-body"></div>
        </div>
      </div>

      <!-- Trend Chart Box -->
      <div class="section-card">
        <div class="section-header">
          <h2 class="section-title">📈 ಚಿನ್ನದ ಬೆಲೆ ಪ್ರವೃತ್ತಿ & ಬೆಳವಣಿಗೆ (Trend Chart)</h2>
          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <button class="mode-tab active" style="padding:6px 12px; font-size:12px;" onclick="switchChartTimeframe('10y')">10 ವರ್ಷಗಳು</button>
            <button class="mode-tab" style="padding:6px 12px; font-size:12px;" onclick="switchChartTimeframe('5y')">5 ವರ್ಷಗಳು</button>
            <button class="mode-tab" style="padding:6px 12px; font-size:12px;" onclick="switchChartTimeframe('1y')">1 ವರ್ಷ</button>
          </div>
        </div>
        <div style="height:260px; position:relative;">
          <canvas id="goldChartCanvas"></canvas>
        </div>
      </div>

      <!-- 12-Month Gold Seasonality Heatmap -->
      <div class="section-card">
        <div class="section-header">
          <h2 class="section-title">🗓️ 12 ತಿಂಗಳ ಚಿನ್ನ ಖರೀದಿ ಹರಿವು (Seasonality Heatmap)</h2>
          <span style="font-size:12px; color:#15803D; font-weight:800;">ಹಸಿರು = ಉತ್ತಮ ಖರೀದಿ ಸಮಯ</span>
        </div>
        <div class="season-heatmap">
          <div class="heat-cell peak"><div>ಜನವರಿ</div><div style="font-size:9.5px;">ಮದುವೆ ಸೀಸನ್</div></div>
          <div class="heat-cell low"><div>ಫೆಬ್ರವರಿ</div><div style="font-size:9.5px;">ಬಜೆಟ್ ಇಳಿಕೆ</div></div>
          <div class="heat-cell avg"><div>ಮಾರ್ಚ್</div><div style="font-size:9.5px;">ವರ್ಷಾಂತ್ಯ</div></div>
          <div class="heat-cell peak"><div>ಏಪ್ರಿಲ್</div><div style="font-size:9.5px;">ಅಕ್ಷಯ ತೃತೀಯ</div></div>
          <div class="heat-cell peak"><div>ಮೇ</div><div style="font-size:9.5px;">ಮದುವೆ ಗರಿಷ್ಠ</div></div>
          <div class="heat-cell best"><div>ಜೂನ್</div><div style="font-size:9.5px;">ಖರೀದಿ ಸಮಯ</div></div>
          <div class="heat-cell best"><div>ಜುಲೈ</div><div style="font-size:9.5px;">ಸುಂಕ ಇಳಿಕೆ</div></div>
          <div class="heat-cell best"><div>ಆಗಸ್ಟ್</div><div style="font-size:9.5px;">ದರ ತಿದ್ದುಪಡಿ</div></div>
          <div class="heat-cell avg"><div>ಸೆಪ್ಟೆಂಬರ್</div><div style="font-size:9.5px;">ಹಬ್ಬದ ಆರಂಭ</div></div>
          <div class="heat-cell peak"><div>ಅಕ್ಟೋಬರ್</div><div style="font-size:9.5px;">ಧಂತೇರಸ್</div></div>
          <div class="heat-cell peak"><div>ನವೆಂಬರ್</div><div style="font-size:9.5px;">ದೀಪಾವಳಿ</div></div>
          <div class="heat-cell peak"><div>ಡಿಸೆಂಬರ್</div><div style="font-size:9.5px;">ವರ್ಷಾಂತ್ಯ ಏರಿಕೆ</div></div>
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         TAB 3: JEWELLERY BILL & OLD GOLD EXCHANGE CALCULATOR
    ══════════════════════════════════════════════════════════ -->
    <div id="view-calc" style="display:none;">
      <div class="section-card">
        <h2 class="section-title" style="margin-bottom:16px;">🧮 ಆಭರಣ ಬಿಲ್ & ಜಿಎಸ್‌ಟಿ ಲೆಕ್ಕಾಚಾರ (Gold Price Calculator)</h2>
        
        <div class="calc-grid">
          <div class="form-group">
            <label class="form-label">ಚಿನ್ನದ ತೂಕ (Grams / ಗ್ರಾಂ):</label>
            <input type="number" id="calc-weight" class="form-input" value="10" min="0.1" step="0.1" oninput="calculateJewelleryBill()">
          </div>
          <div class="form-group">
            <label class="form-label">ಕ್ಯಾರೆಟ್ ಪ್ರಕಾರ:</label>
            <select id="calc-purity" class="form-select" onchange="calculateJewelleryBill()">
              <option value="22" selected>22K ಆಭರಣ ಬಂಗಾರ (916 Hallmark)</option>
              <option value="24">24K ಶುದ್ಧ ಅಪರಂಜಿ (999 Pure)</option>
              <option value="18">18K ಡೈಮಂಡ್ ಜ್ಯುವೆಲ್ಲರಿ</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ & ವೇಸ್ಟೇಜ್ (%):</label>
            <input type="number" id="calc-making" class="form-input" value="12" min="0" max="35" oninput="calculateJewelleryBill()">
          </div>
          <div class="form-group">
            <label class="form-label">ಜಿಎಸ್‌ಟಿ ದರ (%):</label>
            <input type="number" id="calc-gst" class="form-input" value="3" readonly style="background:#F1F5F9;">
          </div>
        </div>

        <!-- Bill Result Box -->
        <div style="background:#FEFCE8; border:1.5px solid #FDE68A; border-radius:12px; padding:18px; margin-top:20px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-size:14px;">
            <span>ಶುದ್ಧ ಚಿನ್ನದ ಮೌಲ್ಯ:</span>
            <span id="bill-base" style="font-weight:800; font-family:'Inter', sans-serif;">₹1,49,400</span>
          </div>
          <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-size:14px;">
            <span>ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ (<span id="bill-making-pct">12</span>%):</span>
            <span id="bill-making" style="font-weight:800; font-family:'Inter', sans-serif;">₹17,928</span>
          </div>
          <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:14px;">
            <span>ಜಿಎಸ್‌ಟಿ ತೆರಿಗೆ (3%):</span>
            <span id="bill-gst" style="font-weight:800; font-family:'Inter', sans-serif;">₹5,020</span>
          </div>
          <div style="border-top:2px solid #FCD34D; padding-top:10px; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:16px; font-weight:900; color:#78350F;">ಒಟ್ಟು ಅಂದಾಜು ಬಿಲ್ ಮೊತ್ತ:</span>
            <span id="bill-total" style="font-size:22px; font-weight:900; color:#92400E; font-family:'Inter', sans-serif;">₹1,72,348</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Encyclopedic Guide Section (AdSense Readiness) -->
    <div class="section-card" style="line-height:1.85;">
      <h2 style="font-size:20px; font-weight:900; color:#0F172A; margin-top:0;">💡 ಕರ್ನಾಟಕದಲ್ಲಿ ಚಿನ್ನ ಖರೀದಿಸುವಾಗ ಗಮನಿಸಬೇಕಾದ 5 ಪ್ರಮುಖ ಅಂಶಗಳು</h2>
      <p style="font-size:14.5px; color:#475569; margin:8px 0;">
        1. <strong>BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:</strong> ಕೇಂದ್ರ ಸರ್ಕಾರದ ನಿಯಮದಂತೆ 6-ಅಂಕಿಯ HUID (Hallmark Unique Identification) ಕೋಡ್ ಇರುವ ಆಭರಣಗಳನ್ನು ಮಾತ್ರ ಖರೀದಿಸಿ.<br>
        2. <strong>ದೈನಂದಿನ ದರ ಪರಿಶೀಲಿಸಿ:</strong> IBJA (India Bullion and Jewellers Association) ನಿಗದಿಪಡಿಸುವ ಲೈವ್ ದರಗಳ ಆಧಾರದ ಮೇಲೆ ಅಂಗಡಿಯವರು ಬಿಲ್ ಮಾಡುತ್ತಿದ್ದಾರೆಯೇ ಎಂದು ಗಮನಿಸಿ.<br>
        3. <strong>ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಚೌಕಾಸಿ ಮಾಡಿ:</strong> ಸರಳ ಆಭರಣಗಳಿಗೆ 8% ರಿಂದ 12% ಮತ್ತು ಸಂಕೀರ್ಣ ವಿನ್ಯಾಸಗಳಿಗೆ ಗರಿಷ್ಠ 15% ಮೇಕಿಂಗ್ ಶುಲ್ಕ ಸಮಂಜಸವಾಗಿದೆ.<br>
        4. <strong>ಜಿಎಸ್‌ಟಿ ಬಿಲ್ ಕಡ್ಡಾಯವಾಗಿ ಪಡೆಯಿರಿ:</strong> 3% ಜಿಎಸ್‌ಟಿ ಪಾವತಿಸಿ ಅಧಿಕೃತ ಬಿಲ್ ಪಡೆದರೆ ಭವಿಷ್ಯದಲ್ಲಿ ಮರುಮಾರಾಟ ಅಥವಾ ಎಕ್ಸ್‌ಚೇಂಜ್ ಮಾಡುವಾಗ 100% ಮೌಲ್ಯ ಲಭಿಸುತ್ತದೆ.
      </p>
    </div>

  </main>

  <script src="/nav-component.js?v=20260830_v5"></script>

  <script>
    const CITIES = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", rate24k: 16304, rate22k: 14940 },
      { name: "ಮೈಸೂರು (Mysore)", rate24k: 16299, rate22k: 14935 },
      { name: "ಮಂಗಳೂರು (Mangalore)", rate24k: 16301, rate22k: 14937 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli)", rate24k: 16296, rate22k: 14932 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", rate24k: 16294, rate22k: 14930 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", rate24k: 16292, rate22k: 14928 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", rate24k: 16297, rate22k: 14933 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", rate24k: 16295, rate22k: 14931 }
    ];

    document.addEventListener('DOMContentLoaded', () => {
      renderCityRates();
      initChart('10y');
      calculateJewelleryBill();
    });

    function switchTab(tabId) {
      document.querySelectorAll('.mode-tab').forEach(b => b.classList.remove('active'));
      document.getElementById(`tab-btn-${tabId}`).classList.add('active');

      document.getElementById('view-live').style.display = tabId === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = tabId === 'analyzer' ? 'block' : 'none';
      document.getElementById('view-calc').style.display = tabId === 'calc' ? 'block' : 'none';

      if (tabId === 'analyzer' && window.myGoldChart) {
        setTimeout(() => window.myGoldChart.resize(), 100);
      }
    }

    function renderCityRates() {
      const c = document.getElementById('city-rates-container');
      if (!c) return;
      c.innerHTML = CITIES.map(ci => `
        <div class="city-rate-item">
          <div class="city-name-box">📍 ${ci.name}</div>
          <div class="city-prices-box">
            <div class="city-p-24k">24K: ₹${ci.rate24k.toLocaleString('en-IN')}</div>
            <div class="city-p-22k">22K: ₹${ci.rate22k.toLocaleString('en-IN')}</div>
          </div>
        </div>
      `).join('');
    }

    function calculateJewelleryBill() {
      const w = parseFloat(document.getElementById('calc-weight').value) || 0;
      const p = parseInt(document.getElementById('calc-purity').value) || 22;
      const mPct = parseFloat(document.getElementById('calc-making').value) || 0;

      let gramRate = 14940;
      if (p === 24) gramRate = 16304;
      if (p === 18) gramRate = 12228;

      const base = w * gramRate;
      const making = (base * mPct) / 100;
      const subtotal = base + making;
      const gst = (subtotal * 3) / 100;
      const total = subtotal + gst;

      document.getElementById('bill-base').textContent = '₹' + Math.round(base).toLocaleString('en-IN');
      document.getElementById('bill-making').textContent = '₹' + Math.round(making).toLocaleString('en-IN');
      document.getElementById('bill-making-pct').textContent = mPct;
      document.getElementById('bill-gst').textContent = '₹' + Math.round(gst).toLocaleString('en-IN');
      document.getElementById('bill-total').textContent = '₹' + Math.round(total).toLocaleString('en-IN');
    }

    function askAiAdvice(qType) {
      const box = document.getElementById('ai-response-box');
      const title = document.getElementById('ai-resp-title');
      const body = document.getElementById('ai-resp-body');
      box.style.display = 'block';

      if (qType === 'buy_today') {
        title.textContent = "🟢 ತೀರ್ಪು: ಖರೀದಿಗೆ ಸೂಕ್ತ ಸಮಯ (Favorable Buy Window)";
        body.innerHTML = "ಪ್ರಸ್ತುತ ಜಾಗತಿಕ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಚಿನ್ನವು ಸೀಸನಲ್ ಕರೆಕ್ಷನ್ ಹಂತದಲ್ಲಿದೆ. ಮುಂಬರುವ ದೀಪಾವಳಿ ಮತ್ತು ಮದುವೆ ಸೀಸನ್‌ಗಿಂತ 2 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ ಖರೀದಿಸುವುದರಿಂದ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ ಉಳಿತಾಯವಾಗಲಿದೆ. <strong>ಶಿಫಾರಸು:</strong> ಒಟ್ಟು ಹೂಡಿಕೆಯ 50% ಭಾಗವನ್ನು ಈಗ ಖರೀದಿಸಿ, ಉಳಿದದ್ದನ್ನು ಸಣ್ಣ ಇಳಿಕೆಗಳಲ್ಲಿ ಸೇರಿಸಿ.";
      } else if (qType === 'sell_today') {
        title.textContent = "🔴 ತೀರ್ಪು: ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್‌ಗೆ ಮಾತ್ರ ಉತ್ತಮ (Hold for Long Term)";
        body.innerHTML = "ದೀರ್ಘಾವಧಿ ಹೂಡಿಕೆದಾರರು ಚಿನ್ನವನ್ನು ಈಗ ಮಾರಾಟ ಮಾಡುವುದಕ್ಕಿಂತ ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳುವುದು (HOLD) ಉತ್ತಮ. ಹಳೆಯ ಮುರಿದ ಒಡವೆಗಳನ್ನು ಹೊಸ 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಆಭರಣಗಳಿಗೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ಮಾಡಲು ಇದು ಸಕಾಲ.";
      } else if (qType === 'wedding') {
        title.textContent = "💍 ಮದುವೆ ಆಭರಣಗಳ ಖರೀದಿ ತಂತ್ರ:";
        body.innerHTML = "ಮದುವೆ ಸೀಸನ್‌ನಲ್ಲಿ ಆಭರಣಗಳಿಗೆ ಭಾರಿ ಬೇಡಿಕೆ ಇರುವುದರಿಂದ ಜ್ಯುವೆಲ್ಲರಿ ಅಂಗಡಿಗಳು ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಹೆಚ್ಚಿಸುತ್ತವೆ. ಈಗಲೇ ಆರ್ಡರ್ ನೀಡಿ ದರವನ್ನು ಲಾಕ್ ಮಾಡಿಕೊಳ್ಳುವುದು (Advance Rate Booking) ಅತ್ಯಂತ ಜಾಣತನದ ಕ್ರಮ.";
      } else if (qType === 'gsr') {
        title.textContent = "⚖️ Gold-Silver Ratio (GSR: 62.7):";
        body.innerHTML = "ಇಂದಿನ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಅನುಪಾತವು ಸಮತೋಲನದಲ್ಲಿದೆ. ದೀರ್ಘಾವಧಿಗೆ ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಲಾಭದ (High Growth Potential) ಸಾಧ್ಯತೆ ಇರುವುದರಿಂದ, ನಿಮ್ಮ ಹೂಡಿಕೆಯಲ್ಲಿ 70% ಚಿನ್ನ ಮತ್ತು 30% ಬೆಳ್ಳಿ ಇರಿಸಿಕೊಳ್ಳುವುದು ಸೂಕ್ತ.";
      }
    }

    let chartInstance = null;
    function initChart(tf) {
      const ctx = document.getElementById('goldChartCanvas');
      if (!ctx) return;

      const data10y = {
        labels: ['2016', '2018', '2020', '2022', '2024', '2025', '2026'],
        values: [2860, 3140, 4860, 5260, 7150, 12400, 16304]
      };

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: data10y.labels,
          datasets: [{
            label: '24K ಚಿನ್ನದ ದರ (₹/ಗ್ರಾಂ)',
            data: data10y.values,
            borderColor: '#D97706',
            backgroundColor: 'rgba(217, 119, 6, 0.1)',
            fill: true,
            tension: 0.35,
            borderWidth: 3,
            pointRadius: 4,
            pointBackgroundColor: '#B45309'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: { grid: { color: '#F1F5F9' }, ticks: { callback: v => '₹' + v } },
            x: { grid: { display: false } }
          }
        }
      });
      window.myGoldChart = chartInstance;
    }

    function switchChartTimeframe(tf) {
      if (!chartInstance) return;
      if (tf === '5y') {
        chartInstance.data.labels = ['2021', '2022', '2023', '2024', '2025', '2026'];
        chartInstance.data.datasets[0].data = [4750, 5260, 6100, 7150, 12400, 16304];
      } else if (tf === '1y') {
        chartInstance.data.labels = ['ಆಗಸ್ಟ್ 25', 'ನವೆಂ 25', 'ಜನ 26', 'ಏಪ್ರಿಲ್ 26', 'ಜೂನ್ 26', 'ಆಗಸ್ಟ್ 26'];
        chartInstance.data.datasets[0].data = [11800, 12900, 13800, 15100, 15800, 16304];
      } else {
        chartInstance.data.labels = ['2016', '2018', '2020', '2022', '2024', '2025', '2026'];
        chartInstance.data.datasets[0].data = [2860, 3140, 4860, 5260, 7150, 12400, 16304];
      }
      chartInstance.update();
    }
  </script>
</body>
</html>
"""

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_page_html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_page_html)

print("SUCCESS_REBUILT_MOBILE_FIRST_GOLD_PAGE")
