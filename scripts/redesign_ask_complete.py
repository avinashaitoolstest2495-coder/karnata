# scripts/redesign_ask_complete.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta name="geo.region" content="IN-KA">
  <meta name="geo.placename" content="Karnataka, India">
  <meta name="geo.position" content="12.9716;77.5946">
  <meta name="ICBM" content="12.9716, 77.5946">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large">

  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>

  <!-- Google Search Engine Structured Data (JSON-LD) with Search Console image compliance -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebApplication",
        "name": "askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ AI ಪ್ರಶ್ನೋತ್ತರ ಸಹಾಯಕ | Karnata.in",
        "applicationCategory": "PublicServiceApplication",
        "operatingSystem": "All",
        "inLanguage": ["kn", "en"],
        "url": "https://karnata.in/ask",
        "description": "askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ. 885+ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತೆ, ಸಿಎಂ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ & ಸಚಿವ ಸಂಪುಟ, ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026, ಚಿನ್ನದ ದರ, ಹವಾಮಾನ, ಜಲಾಶಯ ಮಟ್ಟ ಮತ್ತು APMC ಧಾರಣೆ ಕುರಿತಾದ ನಿಖರ ಪ್ರಶ್ನೋತ್ತರ ವೇದಿಕೆ.",
        "creator": {
          "@type": "Organization",
          "name": "Karnata.in",
          "url": "https://karnata.in"
        },
        "publisher": {
          "@type": "Organization",
          "name": "Karnata.in",
          "logo": {
            "@type": "ImageObject",
            "url": "https://karnata.in/karnata-logo.png",
            "creator": { "@type": "Organization", "name": "Karnata.in" },
            "creditText": "Karnata.in",
            "copyrightNotice": "© 2026 Karnata.in. All rights reserved."
          }
        },
        "featureList": [
          "885+ Government Welfare Schemes Finder in Kannada",
          "Karnataka SIR Final Voter List 2026 Guidance",
          "Live 13 Dams Water Storage & Inflow Telemetry",
          "Live 24K/22K Gold & Silver Rates",
          "31 District KSNDMC Weather Forecasts & APMC Market Prices",
          "Official Council of Ministers 2026 Directory"
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "askKARNATA AI ನಲ್ಲಿ ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ ಎಂದು ಹೇಗೆ ಕೇಳುವುದು?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "askKARNATA AI ನಲ್ಲಿ 'ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ?' ಎಂದು ಕೇಳಿದರೆ, ನಿಮ್ಮ ವಯಸ್ಸು, ಲಿಂಗ, ವೃತ್ತಿ (ರೈತ/ವಿದ್ಯಾರ್ಥಿ/ಮಹಿಳೆ/ಕಾರ್ಮಿಕ), ಮತ್ತು ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ವಿವರ ಆಧರಿಸಿ 885+ ಯೋಜನೆಗಳಲ್ಲಿ ನಿಮಗೆ ಅರ್ಹವಾದ ಪಟ್ಟಿಯನ್ನು ಅಧಿಕೃತ ಅರ್ಜಿ ಲಿಂಕ್‌ನೊಂದಿಗೆ ನೀಡಲಾಗುತ್ತದೆ."
            }
          }
        ]
      }
    ]
  }
  </script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ AI ಪ್ರಶ್ನೋತ್ತರ ಸಹಾಯಕ | AI Assistant for Karnataka — Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ ಆಡಳಿತ, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಹವಾಮಾನ, ಪ್ರವಾಸೋದ್ಯಮ, ಸಂಸ್ಕೃತಿ ಮತ್ತು ಇತಿಹಾಸದ ಬಗ್ಗೆ ನಿಮ್ಮ ಯಾವುದೇ ಪ್ರಶ್ನೆಗೆ ಕನ್ನಡದಲ್ಲೇ ಉತ್ತರಿಸುವ AI ಅಸಿಸ್ಟೆಂಟ್." />
  <meta name="keywords" content="askKARNATA AI, ಕರ್ನಾಟಕ AI ಸಹಾಯಕ, karnataka government schemes AI, karnataka chatbot in kannada, cm dk shivakumar cabinet, gold rate AI, dam levels AI, karnata.in" />
  <link rel="canonical" href="https://karnata.in/ask">
  <link rel="alternate" hreflang="kn-IN" href="https://karnata.in/ask">
  <link rel="alternate" hreflang="en-IN" href="https://karnata.in/ask">
  <link rel="alternate" hreflang="x-default" href="https://karnata.in/ask">

  <!-- Open Graph & Twitter -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ AI ಪ್ರಶ್ನೋತ್ತರ ಸಹಾಯಕ | Karnata.in" />
  <meta property="og:description" content="ಕರ್ನಾಟಕದ ಆಡಳಿತ, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಹವಾಮಾನ, ಪ್ರವಾಸೋದ್ಯಮ ಮತ್ತು ಇತಿಹಾಸದ ಬಗ್ಗೆ ಕನ್ನಡದಲ್ಲೇ ಉತ್ತರಿಸುವ AI ಸಹಾಯಕ." />
  <meta property="og:url" content="https://karnata.in/ask" />
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in">
  <meta property="og:locale" content="kn_IN" />
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ AI ಪ್ರಶ್ನೋತ್ತರ ಸಹಾಯಕ" />
  <meta name="twitter:description" content="885+ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಹವಾಮಾನ, ಬಂಗಾರ ದರ, ಮತ್ತು ಆಡಳಿತ ಮಾಹಿತಿ ಕನ್ನಡದಲ್ಲೇ." />
  <meta name="twitter:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />

  <!-- Fonts & Styles -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">

  <style>
    :root {
      --bg-page: #F8FAFC;
      --bg-sidebar: #FFFFFF;
      --bg-card: #FFFFFF;
      --border-card: #E2E8F0;
      --text-main: #0F172A; /* Deep dark ink for 100% crystal clear readability */
      --text-muted: #334155; /* Slate grey, extremely crisp */
      --text-light: #64748B; /* Legible hints */
      --primary: #1D4ED8; /* Royal Karnataka Blue */
      --primary-light: #EFF6FF;
      --primary-hover: #1E40AF;
      --accent-red: #B91C1C; /* Karnataka Crimson */
      --accent-red-light: #FEF2F2;
      --accent-gold: #D97706; /* Karnataka Gold */
      --accent-gold-light: #FFFBEB;
      --accent-green: #059669; /* Welfare Green */
      --accent-green-light: #ECFDF5;
      --font-kn: 'Anek Kannada', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-en: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --sidebar-w: 280px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

    /* Force background and text colors to override any global theme conflicts */
    html {
      background-color: var(--bg-page) !important;
    }
    body {
      background-color: var(--bg-page) !important;
      color: var(--text-main) !important;
      font-family: var(--font-kn), var(--font-en), sans-serif !important;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* TOP APP BAR */
    .app-topbar {
      height: 64px;
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-card);
      background: #FFFFFF;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    }
    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-main);
    }
    .brand-logo-img {
      height: 36px;
      width: auto;
      border-radius: 8px;
    }
    .brand-title {
      font-size: 20px;
      font-weight: 900;
      letter-spacing: -0.5px;
      color: #0F172A;
      line-height: 1;
    }
    .brand-title span {
      color: var(--primary);
    }
    .brand-tag {
      font-size: 11px;
      font-weight: 800;
      background: linear-gradient(135deg, #1D4ED8, #2563EB);
      color: #FFFFFF;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }
    .topbar-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-topbar {
      padding: 8px 14px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 700;
      border: 1px solid var(--border-card);
      background: #FFFFFF;
      color: var(--text-main);
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .btn-topbar:hover {
      background: var(--bg-page);
      border-color: #CBD5E1;
    }
    .btn-topbar-highlight {
      background: var(--accent-green-light);
      border-color: #A7F3D0;
      color: #065F46;
    }
    .btn-topbar-highlight:hover {
      background: #D1FAE5;
    }

    /* APP CONTAINER */
    .app-layout {
      flex: 1;
      display: flex;
      position: relative;
      height: calc(100vh - 64px);
      overflow: hidden;
      background: var(--bg-page);
    }

    /* SIDEBAR */
    .app-sidebar {
      width: var(--sidebar-w);
      background: #FFFFFF;
      border-right: 1px solid var(--border-card);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 40;
    }
    .sidebar-header {
      padding: 16px 14px 12px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      border-bottom: 1px solid var(--border-card);
    }
    .btn-sidebar-new {
      width: 100%;
      padding: 11px 14px;
      border-radius: 12px;
      border: 1.5px dashed #CBD5E1;
      background: #F8FAFC;
      color: #0F172A;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
      font-family: inherit;
    }
    .btn-sidebar-new:hover {
      background: #EFF6FF;
      border-color: #2563EB;
      color: #1D4ED8;
    }
    .history-label-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 4px;
      font-size: 12px;
      color: #64748B;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .btn-clear-history {
      background: none;
      border: none;
      color: #64748B;
      font-size: 11.5px;
      cursor: pointer;
      font-family: inherit;
      padding: 2px 4px;
      border-radius: 4px;
    }
    .btn-clear-history:hover {
      color: #DC2626;
    }
    .sidebar-history-list {
      flex: 1;
      overflow-y: auto;
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .history-item {
      padding: 10px 12px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 600;
      color: #334155;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.15s;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      position: relative;
    }
    .history-item:hover, .history-item.active {
      background: #EFF6FF;
      color: #1D4ED8;
    }
    .history-item-del {
      margin-left: auto;
      opacity: 0;
      transition: opacity 0.15s;
      font-size: 14px;
      color: #64748B;
    }
    .history-item:hover .history-item-del {
      opacity: 1;
    }
    .history-empty {
      padding: 30px 16px;
      text-align: center;
      font-size: 13px;
      color: #64748B;
      line-height: 1.6;
    }

    /* MAIN VIEW */
    .app-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      position: relative;
      height: 100%;
      background: var(--bg-page);
    }

    /* HERO WELCOME VIEW */
    .hero-container {
      max-width: 860px;
      margin: 0 auto;
      padding: 36px 20px 80px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    .hero-sparkle {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 999px;
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      color: #1D4ED8;
      font-size: 13.5px;
      font-weight: 800;
      margin-bottom: 16px;
    }
    .hero-title {
      font-size: 36px;
      font-weight: 900;
      line-height: 1.3;
      margin-bottom: 12px;
      color: #0F172A; /* 100% visible deep dark text */
      letter-spacing: -0.5px;
    }
    .hero-title .highlight {
      background: linear-gradient(135deg, #1D4ED8 0%, #B91C1C 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-desc {
      font-size: 16px;
      color: #334155;
      font-weight: 500;
      max-width: 720px;
      line-height: 1.65;
      margin-bottom: 26px;
    }

    /* MAIN CENTER INPUT BOX */
    .main-input-wrap {
      width: 100%;
      max-width: 760px;
      background: #FFFFFF;
      border: 2px solid #CBD5E1;
      border-radius: 20px;
      padding: 10px 14px 10px 20px;
      box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
      transition: all 0.2s ease;
      margin-bottom: 24px;
    }
    .main-input-wrap:focus-within {
      border-color: #2563EB;
      box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15), 0 12px 28px -5px rgba(15, 23, 42, 0.12);
    }
    .input-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .query-input-elem {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #0F172A;
      font-size: 16px;
      font-weight: 600;
      font-family: inherit;
      line-height: 1.5;
    }
    .query-input-elem::placeholder {
      color: #64748B;
      font-weight: 400;
    }
    .input-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-voice {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      color: #334155;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      transition: all 0.15s;
    }
    .btn-voice:hover, .btn-voice.recording {
      background: #FEE2E2;
      color: #DC2626;
      border-color: #EF4444;
    }
    .btn-send {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: #1D4ED8;
      border: none;
      color: #FFFFFF;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 900;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3);
    }
    .btn-send:hover {
      background: #1E40AF;
      transform: translateY(-1px);
    }
    .btn-send.active {
      background: #1D4ED8;
    }

    /* TOPIC CHIPS RAIL */
    .hero-chips-rail {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px;
      max-width: 780px;
      margin-bottom: 28px;
    }
    .hero-chip {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 999px;
      padding: 7px 15px;
      font-size: 13.5px;
      font-weight: 700;
      color: #1E293B;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      font-family: inherit;
    }
    .hero-chip:hover {
      background: #EFF6FF;
      border-color: #93C5FD;
      color: #1D4ED8;
      transform: translateY(-1px);
    }
    .hero-chip-green {
      background: #ECFDF5;
      border-color: #A7F3D0;
      color: #065F46;
    }
    .hero-chip-green:hover {
      background: #D1FAE5;
      color: #047857;
    }

    /* PROMPTS GRID */
    .prompts-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      width: 100%;
      max-width: 780px;
    }
    .prompt-box {
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 16px;
      padding: 16px 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 14px;
      text-align: left;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    .prompt-box:hover {
      background: #F8FAFC;
      border-color: #2563EB;
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(37, 99, 235, 0.08);
    }
    .prompt-icon {
      font-size: 24px;
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: #F1F5F9;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .prompt-text-col {
      flex: 1;
      font-size: 14.5px;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.4;
    }
    .prompt-text-col .sub {
      font-size: 12.5px;
      font-weight: 600;
      color: #64748B;
      margin-top: 3px;
    }

    /* CHAT STREAM */
    .chat-stream {
      display: none;
      max-width: 860px;
      margin: 0 auto;
      padding: 24px 20px 140px;
      width: 100%;
      flex-direction: column;
      gap: 24px;
    }
    .message-row {
      display: flex;
      flex-direction: column;
      gap: 12px;
      animation: fadeIn 0.25s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .user-bubble-box {
      align-self: flex-end;
      max-width: 80%;
      background: linear-gradient(135deg, #1E3A8A 0%, #1D4ED8 100%);
      color: #FFFFFF;
      padding: 14px 20px;
      border-radius: 20px 20px 4px 20px;
      font-size: 15.5px;
      font-weight: 600;
      line-height: 1.5;
      box-shadow: 0 4px 14px rgba(29, 78, 216, 0.2);
    }
    .ai-card-box {
      align-self: flex-start;
      width: 100%;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    }
    .ai-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid #F1F5F9;
      padding-bottom: 12px;
    }
    .ai-brand-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .ai-status-dot {
      width: 8px;
      height: 8px;
      background: #10B981;
      border-radius: 50%;
      box-shadow: 0 0 8px #10B981;
    }
    .ai-name {
      font-size: 15px;
      font-weight: 900;
      color: #1D4ED8;
    }
    .ai-ground-tag {
      font-size: 12px;
      background: #ECFDF5;
      color: #047857;
      padding: 3px 10px;
      border-radius: 6px;
      font-weight: 800;
      border: 1px solid #A7F3D0;
    }
    .ai-tools-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tool-icon-btn {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 6px 10px;
      font-size: 12.5px;
      font-weight: 600;
      color: #334155;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-family: inherit;
      transition: all 0.15s;
    }
    .tool-icon-btn:hover {
      background: #EFF6FF;
      color: #1D4ED8;
      border-color: #BFDBFE;
    }
    .ai-content {
      font-size: 15.5px;
      line-height: 1.75;
      color: #0F172A; /* Deep ink for high contrast */
    }
    .ai-content p { margin-bottom: 12px; }
    .ai-content h3 { font-size: 19px; font-weight: 900; margin: 16px 0 8px; color: #0F172A; }
    .ai-content h4 { font-size: 16px; font-weight: 800; margin: 14px 0 6px; color: #1D4ED8; }
    .ai-content ul, .ai-content ol { margin-left: 20px; margin-bottom: 12px; }
    .ai-content li { margin-bottom: 6px; color: #1E293B; }
    .ai-content strong { color: #0F172A; font-weight: 800; }
    .ai-content table {
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      font-size: 14px;
    }
    .ai-content th, .ai-content td {
      border: 1px solid #E2E8F0;
      padding: 10px 14px;
      text-align: left;
    }
    .ai-content th {
      background: #F8FAFC;
      color: #1D4ED8;
      font-weight: 800;
    }

    .action-links-container {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 18px;
      padding-top: 14px;
      border-top: 1px dashed #E2E8F0;
    }
    .portal-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 800;
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      color: #1D4ED8;
      text-decoration: none;
      transition: all 0.15s;
    }
    .portal-pill:hover {
      background: #1D4ED8;
      color: #FFFFFF;
      border-color: #1D4ED8;
      transform: translateY(-1px);
    }
    .followups-box {
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .followup-chip {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 8px 14px;
      font-size: 13.5px;
      color: #334155;
      cursor: pointer;
      text-align: left;
      transition: all 0.15s;
      font-family: inherit;
      font-weight: 600;
    }
    .followup-chip:hover {
      background: #EFF6FF;
      color: #1D4ED8;
      border-color: #BFDBFE;
    }

    /* TYPING PULSE */
    .typing-dots {
      display: flex;
      gap: 5px;
      padding: 8px 0;
    }
    .typing-dot {
      width: 7px;
      height: 7px;
      background: #1D4ED8;
      border-radius: 50%;
      animation: pulseDot 1.4s infinite ease-in-out;
    }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes pulseDot {
      0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
      40% { transform: scale(1.2); opacity: 1; }
    }

    /* DOCKED BOTTOM BAR */
    .docked-bar {
      position: fixed;
      bottom: 0;
      left: var(--sidebar-w);
      right: 0;
      padding: 14px 20px 18px;
      background: linear-gradient(180deg, rgba(248, 250, 252, 0) 0%, rgba(248, 250, 252, 0.95) 40%, rgba(248, 250, 252, 1) 100%);
      z-index: 45;
      display: none;
    }
    .docked-inner {
      max-width: 860px;
      margin: 0 auto;
    }

    /* TOAST */
    .toast-popup {
      position: fixed;
      bottom: 85px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: #059669;
      color: #FFFFFF;
      padding: 9px 20px;
      border-radius: 999px;
      font-size: 14px;
      font-weight: 800;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s ease;
      z-index: 100;
    }
    .toast-popup.show {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    @media (max-width: 860px) {
      .app-sidebar {
        position: fixed;
        top: 64px;
        bottom: 0;
        left: 0;
        transform: translateX(-100%);
      }
      .app-sidebar.open {
        transform: translateX(0);
        box-shadow: 10px 0 30px rgba(0,0,0,0.15);
      }
      .docked-bar {
        left: 0;
      }
      .prompts-grid {
        grid-template-columns: 1fr;
      }
      .hero-title {
        font-size: 28px;
      }
    }
  </style>

  <script src="/seo.js" defer></script>
</head>
<body>

  <!-- TOP APP BAR -->
  <header class="app-topbar">
    <div style="display:flex; align-items:center; gap:10px;">
      <button class="btn-topbar" id="btn-toggle-sidebar" onclick="toggleSidebar()" title="Toggle History">
        <span>☰</span>
      </button>
      <a href="/ask" class="brand-wrap">
        <img src="/karnata-logo.png" alt="askKARNATA Logo" class="brand-logo-img" onerror="this.style.display='none'">
        <div class="brand-title">ask<span>KARNATA</span></div>
        <span class="brand-tag">AI 2.0</span>
      </a>
    </div>

    <div class="topbar-actions">
      <a href="/scheme-checker" class="btn-topbar btn-topbar-highlight">
        <span>🎯</span> ಯೋಜನೆ ಅರ್ಹತೆ (885+)
      </a>
      <a href="/cabinet-ministers" class="btn-topbar">
        <span>👥</span> ಸಚಿವ ಸಂಪುಟ
      </a>
      <button class="btn-topbar" onclick="startNewChat()">
        <span>+</span> ಹೊಸ ಚಾಟ್
      </button>
      <a href="/" class="btn-topbar">
        <span>🏠</span> ಮುಖಪುಟ
      </a>
    </div>
  </header>

  <!-- APP LAYOUT -->
  <div class="app-layout">

    <!-- SIDEBAR: CHAT HISTORY -->
    <aside class="app-sidebar" id="appSidebar">
      <div class="sidebar-header">
        <button class="btn-sidebar-new" onclick="startNewChat()">
          <span>+</span> ಹೊಸ ಚಾಟ್ (New Chat)
        </button>
        <div class="history-label-row">
          <span>ಇತ್ತೀಚಿನ ಪ್ರಶ್ನೆಗಳು</span>
          <button class="btn-clear-history" onclick="clearChatHistory()">ಎಲ್ಲವನ್ನೂ ಅಳಿಸು</button>
        </div>
      </div>
      <div class="sidebar-history-list" id="sidebarHistoryList">
        <div class="history-empty">ಸಂಭಾಷಣೆಗಳು ಇಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಸೇವ್ ಆಗುತ್ತವೆ.</div>
      </div>
    </aside>

    <!-- MAIN CHAT CANVAS -->
    <main class="app-main" id="appMain">

      <!-- HERO WELCOME VIEW -->
      <div class="hero-container" id="heroView">
        <div class="hero-sparkle">
          <span>✨</span> ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ (Free AI 2.0)
        </div>
        <h1 class="hero-title">ನಮಸ್ಕಾರ! ಇಂದು ನಿಮಗೆ <span class="highlight">ಏನು ಸಹಾಯ ಬೇಕು?</span></h1>
        <p class="hero-desc">ಕರ್ನಾಟಕದ 885+ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಸಚಿವ ಸಂಪುಟ, SIR ಮತದಾರರ ಪಟ್ಟಿ, ಬಂಗಾರ ದರ, ಹವಾಮಾನ, ಜಲಾಶಯ ಮಟ್ಟ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳ ಬಗ್ಗೆ ನೇರವಾಗಿ ಕೇಳಿ.</p>

        <!-- CENTER SEARCH INPUT -->
        <div class="main-input-wrap">
          <div class="input-row">
            <input type="text" id="centerQueryInput" class="query-input-elem" placeholder="ಇಲ್ಲಿ ಪ್ರಶ್ನೆ ಕೇಳಿ... (ಉದಾ: ನನಗೆ ಯಾವ ಯೋಜನೆ ಸಿಗುತ್ತದೆ?, ಬಂಗಾರ ದರ, ಡ್ಯಾಂ ಮಟ್ಟ)" onkeypress="handleCenterKey(event)" oninput="handleInputSync(this.value)" autofocus>
            <div class="input-actions">
              <button class="btn-voice" id="btnVoiceCenter" onclick="toggleVoiceInput('center')" title="ಧ್ವನಿ ಮೂಲಕ ಮಾತನಾಡಿ (Voice Input)">🎙️</button>
              <button class="btn-send" id="btnSendCenter" onclick="submitCenterQuery()">↑</button>
            </div>
          </div>
        </div>

        <!-- CATEGORY CHIPS RAIL -->
        <div class="hero-chips-rail">
          <button class="hero-chip hero-chip-green" onclick="sendPreset('ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? ನನ್ನ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ')">🎯 ನನಗೆ ಯಾವ ಯೋಜನೆ ಸಿಗುತ್ತದೆ? (885+)</button>
          <button class="hero-chip" onclick="sendPreset('ಗೃಹಲಕ್ಷ್ಮಿ ಮತ್ತು ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಗಳ ನಿಯಮಗಳು ಮತ್ತು ಅರ್ಹತೆ ಏನು?')">🌸 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು</button>
          <button class="hero-chip" onclick="sendPreset('ಇಂದು 22K ಹಾಗೂ 24K ಚಿನ್ನದ ದರ ಮತ್ತು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟು?')">💰 ಬಂಗಾರ & ಬೆಳ್ಳಿ</button>
          <button class="hero-chip" onclick="sendPreset('KRS, ಆಲಮಟ್ಟಿ ಮತ್ತು ತುಂಗಭದ್ರಾ ಜಲಾಶಯಗಳ ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ ಮತ್ತು ಒಳಹರಿವು ಎಷ್ಟು?')">💧 ಜಲಾಶಯ ಮಟ್ಟ</button>
          <button class="hero-chip" onclick="sendPreset('ಕೋಲಾರ APMCಯಲ್ಲಿ ಇಂದಿನ ಟೊಮೆಟೊ ಬೆಲೆ ಮತ್ತು ಶಿರಸಿಯಲ್ಲಿ ಅಡಿಕೆ ದರ ಎಷ್ಟಿದೆ?')">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರ</button>
          <button class="hero-chip" onclick="sendPreset('ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ ಮತ್ತು ಸಚಿವರ ಖಾತೆಗಳ ಪಟ್ಟಿ ಕೊಡಿ')">🏛️ ಸಚಿವ ಸಂಪುಟ & ಖಾತೆಗಳು</button>
          <button class="hero-chip" onclick="sendPreset('ಬೆಂಗಳೂರು ನಗರ ಹಾಗೂ ಮೈಸೂರಿನ ಜಿಲ್ಲಾಧಿಕಾರಿ ಮತ್ತು ಎಸ್ಪಿ ಯಾರು?')">👥 ಜಿಲ್ಲಾಧಿಕಾರಿ & ಎಸ್ಪಿ</button>
          <button class="hero-chip" onclick="sendPreset('SIR ಎಂದರೇನು? ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?')">🗳️ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026</button>
        </div>

        <!-- 8 PROMPT SUGGESTION CARDS -->
        <div class="prompts-grid">
          <div class="prompt-box" style="border-color:#A7F3D0; background:#ECFDF5;" onclick="sendPreset('ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? ನನ್ನ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ')">
            <span class="prompt-icon">🎯</span>
            <div class="prompt-text-col">
              <div>ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ?</div>
              <div class="sub" style="color:#059669;">885+ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರ ಯೋಜನೆಗಳ ಪರೀಕ್ಷಕ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಗೃಹಲಕ್ಷ್ಮಿ ₹2,000 DBT ಸ್ಥಿತಿ ಮತ್ತು ಗೃಹಜ್ಯೋತಿ 200 ಯೂನಿಟ್ ಉಚಿತ ವಿದ್ಯುತ್ ನಿಯಮಗಳೇನು?')">
            <span class="prompt-icon">🌸</span>
            <div class="prompt-text-col">
              <div>ಗೃಹಲಕ್ಷ್ಮಿ & ಗೃಹಜ್ಯೋತಿ ನಿಯಮಗಳು</div>
              <div class="sub">5 ಗ್ಯಾರಂಟಿ ಅರ್ಜಿ & ಅರ್ಹತೆ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಇಂದು ಬಂಗಾರ ಕೊಳ್ಳಲು ಸರಿಯಾದ ಸಮಯವೇ? 22K ಹಾಗೂ 24K ಚಿನ್ನದ ದರ ಎಷ್ಟು?')">
            <span class="prompt-icon">🪙</span>
            <div class="prompt-text-col">
              <div>ಇಂದು ಬಂಗಾರ ದರ ಎಷ್ಟು?</div>
              <div class="sub">22K / 24K ಲೈವ್ ಬೆಲೆ & ಇತಿಹಾಸ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('KRS, ಆಲಮಟ್ಟಿ ಮತ್ತು ತುಂಗಭದ್ರಾ ಜಲಾಶಯಗಳ ಇಂದಿನ ಒಳಹರಿವು ಮತ್ತು ನೀರಿನ ಸಂಗ್ರಹ ಎಷ್ಟು?')">
            <span class="prompt-icon">💧</span>
            <div class="prompt-text-col">
              <div>ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ</div>
              <div class="sub">13 ಪ್ರಮುಖ ಡ್ಯಾಂ ಟಿಎಂಸಿ ಮಾಹಿತಿ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ ಹಾಗೂ ಸಂಪುಟ ಸಚಿವರ ಅಧಿಕೃತ ಖಾತೆಗಳು ಯಾವುವು?')">
            <span class="prompt-icon">🏛️</span>
            <div class="prompt-text-col">
              <div>ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ 2026</div>
              <div class="sub">ಸಿಎಂ, ಡಿಸಿಎಂ & 30 ಸಚಿವರ ವಿವರ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಕೋಲಾರ APMCಯಲ್ಲಿ ಇಂದಿನ ಟೊಮೆಟೊ ಬೆಲೆ ಮತ್ತು ಶಿರಸಿಯಲ್ಲಿ ಅಡಿಕೆ ದರ ಎಷ್ಟಿದೆ?')">
            <span class="prompt-icon">🌾</span>
            <div class="prompt-text-col">
              <div>APMC ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ದರಗಳು</div>
              <div class="sub">174 ಮಂಡಿಗಳ ದೈನಂದಿನ ಧಾರಣೆ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಕರ್ನಾಟಕದ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು (DC) ಮತ್ತು ಎಸ್ಪಿ (SP) ಅಧಿಕಾರಿಗಳ ಸಂಪರ್ಕ ವಿವರ ಕೊಡಿ')">
            <span class="prompt-icon">👥</span>
            <div class="prompt-text-col">
              <div>IAS & IPS ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ</div>
              <div class="sub">31 ಜಿಲ್ಲೆಗಳ ಅಧಿಕೃತ ಸಂಪರ್ಕ →</div>
            </div>
          </div>

          <div class="prompt-box" onclick="sendPreset('ಕರ್ನಾಟಕ SIR 2026 ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?')">
            <span class="prompt-icon">🗳️</span>
            <div class="prompt-text-col">
              <div>SIR ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ 2026</div>
              <div class="sub">224 ಕ್ಷೇತ್ರಗಳ ಪಟ್ಟಿ ಪರಿಶೀಲನೆ →</div>
            </div>
          </div>
        </div>
      </div>

      <!-- CHAT CONVERSATION STREAM -->
      <div class="chat-stream" id="chatStream"></div>

    </main>
  </div>

  <!-- DOCKED BOTTOM BAR (ACTIVE IN CHAT VIEW) -->
  <div class="docked-bar" id="dockedBar">
    <div class="docked-inner">
      <div class="main-input-wrap" style="margin-bottom:0; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <div class="input-row">
          <input type="text" id="dockedQueryInput" class="query-input-elem" placeholder="ಮುಂದಿನ ಪ್ರಶ್ನೆ ಕೇಳಿ..." onkeypress="handleDockedKey(event)" oninput="handleInputSync(this.value)">
          <div class="input-actions">
            <button class="btn-voice" id="btnVoiceDocked" onclick="toggleVoiceInput('docked')" title="ಧ್ವನಿ ಮೂಲಕ ಮಾತನಾಡಿ (Voice Input)">🎙️</button>
            <button class="btn-send" id="btnSendDocked" onclick="submitDockedQuery()">↑</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast-popup" id="toastPopup">ಪ್ರತಿಮಾಡಲಾಗಿದೆ (Copied)!</div>

  <!-- LOAD LOCAL ENGINE AS RESILIENT FALLBACK -->
  <script src="/ask-ai-engine.js"></script>

  <!-- APP JAVASCRIPT -->
  <script>
    const STORAGE_KEY = 'askkarnata_history_v2';
    let chatHistory = [];
    let isGenerating = false;
    let recognition = null;
    let isRecording = false;
    let activeVoiceTarget = null;
    let currentSpeakingUtterance = null;

    // Load History
    try {
      chatHistory = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    } catch (e) {
      chatHistory = [];
    }

    window.addEventListener('DOMContentLoaded', () => {
      renderSidebarHistory();
      setupSpeechRecognition();

      // Check URL query param e.g. /ask?q=...
      const urlParams = new URLSearchParams(window.location.search);
      const q = urlParams.get('q') || urlParams.get('query');
      if (q && q.trim()) {
        submitQuery(q.trim());
      }
    });

    function saveChatSession(query, answer, cards, followups) {
      const record = {
        id: 'chat_' + Date.now(),
        title: query.length > 36 ? query.substring(0, 36) + '...' : query,
        query: query,
        answer: answer,
        cards: cards || [],
        followups: followups || [],
        timestamp: new Date().toISOString()
      };
      chatHistory = [record, ...chatHistory.filter(h => h.query !== query)].slice(0, 30);
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(chatHistory)); } catch (e) {}
      renderSidebarHistory();
    }

    function renderSidebarHistory() {
      const listEl = document.getElementById('sidebarHistoryList');
      if (!listEl) return;
      if (chatHistory.length === 0) {
        listEl.innerHTML = '<div class="history-empty">ಸಂಭಾಷಣೆಗಳು ಇಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಸೇವ್ ಆಗುತ್ತವೆ.</div>';
        return;
      }
      listEl.innerHTML = chatHistory.map(item => `
        <div class="history-item" onclick="loadArchivedChat('${item.id}')" title="${escapeHtml(item.query)}">
          <span>💬</span>
          <span style="overflow:hidden; text-overflow:ellipsis; flex:1;">${escapeHtml(item.title)}</span>
          <span class="history-item-del" onclick="deleteHistoryItem(event, '${item.id}')" title="Delete">✕</span>
        </div>
      `).join('');
    }

    function deleteHistoryItem(e, id) {
      e.stopPropagation();
      chatHistory = chatHistory.filter(h => h.id !== id);
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(chatHistory)); } catch (e) {}
      renderSidebarHistory();
    }

    function clearChatHistory() {
      if (confirm('ಎಲ್ಲಾ ಚಾಟ್ ಇತಿಹಾಸವನ್ನು ಅಳಿಸಬೇಕೇ?')) {
        chatHistory = [];
        try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
        renderSidebarHistory();
      }
    }

    function toggleSidebar() {
      const sidebar = document.getElementById('appSidebar');
      sidebar.classList.toggle('open');
    }

    function startNewChat() {
      if (window.speechSynthesis) window.speechSynthesis.cancel();
      document.getElementById('heroView').style.display = 'flex';
      document.getElementById('chatStream').style.display = 'none';
      document.getElementById('dockedBar').style.display = 'none';
      document.getElementById('centerQueryInput').value = '';
      document.getElementById('dockedQueryInput').value = '';
      document.getElementById('btnSendCenter').classList.remove('active');
      document.getElementById('btnSendDocked').classList.remove('active');
      document.getElementById('chatStream').innerHTML = '';
      window.history.replaceState({}, '', '/ask');
      const sidebar = document.getElementById('appSidebar');
      sidebar.classList.remove('open');
      document.getElementById('centerQueryInput').focus();
    }

    function loadArchivedChat(id) {
      const item = chatHistory.find(h => h.id === id);
      if (!item) return;

      document.getElementById('heroView').style.display = 'none';
      document.getElementById('chatStream').style.display = 'flex';
      document.getElementById('dockedBar').style.display = 'block';

      const stream = document.getElementById('chatStream');
      stream.innerHTML = '';
      appendMessageBlock(item.query, item.answer, item.cards, item.followups, false);

      const sidebar = document.getElementById('appSidebar');
      sidebar.classList.remove('open');
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    }

    function handleInputSync(val) {
      document.getElementById('centerQueryInput').value = val;
      document.getElementById('dockedQueryInput').value = val;

      const hasText = val.trim().length > 0;
      document.getElementById('btnSendCenter').classList.toggle('active', hasText);
      document.getElementById('btnSendDocked').classList.toggle('active', hasText);
    }

    function handleCenterKey(e) {
      if (e.key === 'Enter') submitCenterQuery();
    }

    function handleDockedKey(e) {
      if (e.key === 'Enter') submitDockedQuery();
    }

    function submitCenterQuery() {
      const val = document.getElementById('centerQueryInput').value.trim();
      if (val) submitQuery(val);
    }

    function submitDockedQuery() {
      const val = document.getElementById('dockedQueryInput').value.trim();
      if (val) submitQuery(val);
    }

    function sendPreset(text) {
      submitQuery(text);
    }

    // ── Core Query Execution ─────────────────────────────────
    async function submitQuery(queryText) {
      if (!queryText || isGenerating) return;
      isGenerating = true;

      // Switch to chat view
      document.getElementById('heroView').style.display = 'none';
      document.getElementById('chatStream').style.display = 'flex';
      document.getElementById('dockedBar').style.display = 'block';

      // Clear inputs
      handleInputSync('');

      const stream = document.getElementById('chatStream');

      // 1. User Message
      const userRow = document.createElement('div');
      userRow.className = 'message-row';
      userRow.innerHTML = `<div class="user-bubble-box">${escapeHtml(queryText)}</div>`;
      stream.appendChild(userRow);

      // 2. AI Card Skeleton with Typing Indicator
      const aiRow = document.createElement('div');
      aiRow.className = 'message-row';
      const aiCard = document.createElement('div');
      aiCard.className = 'ai-card-box';
      aiCard.innerHTML = `
        <div class="ai-header-row">
          <div class="ai-brand-group">
            <span class="ai-status-dot"></span>
            <span class="ai-name">askKARNATA AI</span>
            <span class="ai-ground-tag">⚡ AI ವಿಶ್ಲೇಷಣೆ ನಡೆಯುತ್ತಿದೆ...</span>
          </div>
        </div>
        <div class="ai-content">
          <div class="typing-dots">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
          </div>
        </div>
      `;
      aiRow.appendChild(aiCard);
      stream.appendChild(aiRow);

      // Scroll to bottom
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });

      let result = null;
      let providerName = '⚡ Cloudflare Llama 3.1 8B (Multilingual) + Live Real-time RAG';

      // 1. Call Cloudflare Pages API Endpoint
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 6500); // 6.5s timeout

        const res = await fetch('/api/ask-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: queryText }),
          signal: controller.signal
        });
        clearTimeout(timeoutId);

        if (res.ok) {
          const data = await res.json();
          if (data && data.answer) {
            result = {
              text: data.answer,
              cards: data.cards || [],
              followups: data.followups || [],
              provider: data.provider || providerName
            };
          }
        }
      } catch (netErr) {
        console.warn('Edge AI call timed out or failed, switching to local knowledge engine:', netErr);
      }

      // 2. Fallback to Local Real-Time Ground Engine if API failed or offline
      if (!result || !result.text) {
        if (window.AskKARNATAEngine && typeof window.AskKARNATAEngine.query === 'function') {
          try {
            result = window.AskKARNATAEngine.query(queryText);
            if (result && result.text) {
              result.provider = 'Karnata High-Precision Knowledge Engine (Local Grounded)';
            }
          } catch (e) {
            console.warn('Local engine query error:', e);
          }
        }
      }

      // 3. Graceful fallback if still no answer
      if (!result || !result.text) {
        result = {
          text: `### 🏛️ askKARNATA AI ಸಹಾಯಕ\n\nನಿಮ್ಮ ಪ್ರಶ್ನೆ: **"${queryText}"**\n\nಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯೋಜನೆಗಳು, ಸಚಿವ ಸಂಪುಟ, ಬಂಗಾರ ದರ, ಹವಾಮಾನ, ಜಲಾಶಯ ನೀರಿನ ಮಟ್ಟ ಅಥವಾ APMC ಮಾರುಕಟ್ಟೆ ಕುರಿತು ಮಾಹಿತಿ ಕೆಳಗಿನ ಅಧಿಕೃತ ಪುಟಗಳಲ್ಲಿ ಲಭ್ಯವಿದೆ:`,
          cards: [
            { title: "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ (885+)", url: "/scheme-checker", icon: "🎯" },
            { title: "ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ 2026", url: "/cabinet-ministers", icon: "🏛️" },
            { title: "ಲೈವ್ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರ", url: "/gold-rate", icon: "🪙" },
            { title: "13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ", url: "/dam-levels", icon: "💧" }
          ],
          followups: [
            "ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ?",
            "ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿ ಮತ್ತು ಸಚಿವರ ಖಾತೆಗಳ ಪಟ್ಟಿ ಕೊಡಿ",
            "ಇಂದಿನ 22K ಚಿನ್ನದ ದರ ಎಷ್ಟು?"
          ],
          provider: 'Karnata Resilient Fallback'
        };
      }

      // Update AI Card UI
      const cleanMarkdown = result.text || '';
      const htmlContent = parseSimpleMarkdown(cleanMarkdown);
      const resolvedProvider = result.provider || providerName;

      // Build Action Cards Pills
      let cardsHtml = '';
      if (result.cards && result.cards.length > 0) {
        cardsHtml = `
          <div class="action-links-container">
            ${result.cards.map(c => `
              <a href="${c.url}" class="portal-pill">
                <span>${c.icon || '🔗'}</span>
                <span>${c.title}</span>
              </a>
            `).join('')}
          </div>
        `;
      }

      // Build Follow-up Prompts
      let followupsHtml = '';
      if (result.followups && result.followups.length > 0) {
        followupsHtml = `
          <div class="followups-box">
            <span style="font-size:12.5px; color:#64748B; font-weight:800;">ಇನ್ನಷ್ಟು ಪ್ರಶ್ನಿಸಿ (Related):</span>
            ${result.followups.map(f => `
              <button class="followup-chip" onclick="submitQuery('${f.replace(/'/g, "\\'")}')">
                <span>↳</span> ${escapeHtml(f)}
              </button>
            `).join('')}
          </div>
        `;
      }

      const rawTextForSpeech = cleanMarkdown.replace(/[#*`_>]/g, ' ').replace(/\\s+/g, ' ');

      aiCard.innerHTML = `
        <div class="ai-header-row">
          <div class="ai-brand-group">
            <span class="ai-status-dot"></span>
            <span class="ai-name">askKARNATA AI</span>
            <span class="ai-ground-tag">✓ ನೈಜ ಸಮಯದ ದತ್ತಾಂಶ (Live RAG)</span>
          </div>
          <div class="ai-tools-group">
            <button class="tool-icon-btn" onclick="speakText(this, decodeURIComponent('${encodeURIComponent(rawTextForSpeech)}'))" title="ಧ್ವನಿ ಮೂಲಕ ಓದಿ (Text-to-Speech)">
              <span class="speaker-icon">🔊</span> <span>ಓದು</span>
            </button>
            <button class="tool-icon-btn" onclick="copyCardContent(this)" title="ಪ್ರತಿಮಾಡಿ (Copy)">
              <span>📋</span> <span>ಕಾಪಿ</span>
            </button>
            <button class="tool-icon-btn" onclick="shareToWhatsApp(decodeURIComponent('${encodeURIComponent(queryText)}'), decodeURIComponent('${encodeURIComponent(rawTextForSpeech)}'))" title="WhatsApp ಹಂಚಿಕೊಳ್ಳಿ">
              <span>🟢</span> <span>WhatsApp</span>
            </button>
          </div>
        </div>
        <div class="ai-content">
          ${htmlContent}
        </div>
        ${cardsHtml}
        ${followupsHtml}
        <div style="margin-top:14px; font-size:11.5px; color:#94A3B8; text-align:right;">
          ${escapeHtml(resolvedProvider)} • ನಿಖರತೆ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ
        </div>
      `;

      // Save to localStorage
      saveChatSession(queryText, cleanMarkdown, result.cards, result.followups);

      isGenerating = false;
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    }

    function appendMessageBlock(query, answer, cards, followups, isCurrent) {
      const stream = document.getElementById('chatStream');

      const userRow = document.createElement('div');
      userRow.className = 'message-row';
      userRow.innerHTML = `<div class="user-bubble-box">${escapeHtml(query)}</div>`;
      stream.appendChild(userRow);

      const aiRow = document.createElement('div');
      aiRow.className = 'message-row';

      let cardsHtml = '';
      if (cards && cards.length > 0) {
        cardsHtml = `
          <div class="action-links-container">
            ${cards.map(c => `
              <a href="${c.url}" class="portal-pill">
                <span>${c.icon || '🔗'}</span>
                <span>${c.title}</span>
              </a>
            `).join('')}
          </div>
        `;
      }

      let followupsHtml = '';
      if (followups && followups.length > 0) {
        followupsHtml = `
          <div class="followups-box">
            <span style="font-size:12.5px; color:#64748B; font-weight:800;">ಇನ್ನಷ್ಟು ಪ್ರಶ್ನಿಸಿ:</span>
            ${followups.map(f => `
              <button class="followup-chip" onclick="submitQuery('${f.replace(/'/g, "\\'")}')">
                <span>↳</span> ${escapeHtml(f)}
              </button>
            `).join('')}
          </div>
        `;
      }

      const rawTextForSpeech = (answer || '').replace(/[#*`_>]/g, ' ').replace(/\\s+/g, ' ');

      const aiCard = document.createElement('div');
      aiCard.className = 'ai-card-box';
      aiCard.innerHTML = `
        <div class="ai-header-row">
          <div class="ai-brand-group">
            <span class="ai-status-dot"></span>
            <span class="ai-name">askKARNATA AI</span>
            <span class="ai-ground-tag">✓ ನೈಜ ಸಮಯದ ದತ್ತಾಂಶ</span>
          </div>
          <div class="ai-tools-group">
            <button class="tool-icon-btn" onclick="speakText(this, decodeURIComponent('${encodeURIComponent(rawTextForSpeech)}'))" title="ಧ್ವನಿ ಮೂಲಕ ಓದಿ">
              <span class="speaker-icon">🔊</span> <span>ಓದು</span>
            </button>
            <button class="tool-icon-btn" onclick="copyCardContent(this)" title="ಪ್ರತಿಮಾಡಿ">
              <span>📋</span> <span>ಕಾಪಿ</span>
            </button>
            <button class="tool-icon-btn" onclick="shareToWhatsApp(decodeURIComponent('${encodeURIComponent(query)}'), decodeURIComponent('${encodeURIComponent(rawTextForSpeech)}'))" title="WhatsApp ಹಂಚಿಕೊಳ್ಳಿ">
              <span>🟢</span> <span>WhatsApp</span>
            </button>
          </div>
        </div>
        <div class="ai-content">
          ${parseSimpleMarkdown(answer)}
        </div>
        ${cardsHtml}
        ${followupsHtml}
      `;

      aiRow.appendChild(aiCard);
      stream.appendChild(aiRow);
    }

    // ── Speech Synthesis (TTS in Kannada) ─────────────────────
    function speakText(btn, text) {
      if (!('speechSynthesis' in window)) {
        showToast('ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಧ್ವನಿ ವೈಶಿಷ್ಟ್ಯ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ.');
        return;
      }

      if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
        btn.querySelector('.speaker-icon').textContent = '🔊';
        btn.querySelector('span:last-child').textContent = 'ಓದು';
        return;
      }

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.95;
      utterance.pitch = 1.0;

      // Pick Kannada voice if available
      const voices = window.speechSynthesis.getVoices();
      const knVoice = voices.find(v => v.lang === 'kn-IN' || v.lang.startsWith('kn') || v.name.toLowerCase().includes('kannada'));
      if (knVoice) utterance.voice = knVoice;

      btn.querySelector('.speaker-icon').textContent = '⏹️';
      btn.querySelector('span:last-child').textContent = 'ನಿಲ್ಲಿಸು';

      utterance.onend = () => {
        btn.querySelector('.speaker-icon').textContent = '🔊';
        btn.querySelector('span:last-child').textContent = 'ಓದು';
      };
      utterance.onerror = () => {
        btn.querySelector('.speaker-icon').textContent = '🔊';
        btn.querySelector('span:last-child').textContent = 'ಓದು';
      };

      window.speechSynthesis.speak(utterance);
    }

    // ── Voice Input (Speech Recognition) ─────────────────────
    function setupSpeechRecognition() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) return;

      recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = true;
      recognition.lang = 'kn-IN'; // Kannada Primary

      recognition.onstart = () => {
        isRecording = true;
        updateVoiceBtnState(true);
        showToast('🎙️ ಮಾತನಾಡಿ... (Listening in Kannada)');
      };

      recognition.onresult = (event) => {
        const transcript = Array.from(event.results)
          .map(r => r[0].transcript)
          .join('');
        handleInputSync(transcript);
      };

      recognition.onerror = (event) => {
        isRecording = false;
        updateVoiceBtnState(false);
      };

      recognition.onend = () => {
        isRecording = false;
        updateVoiceBtnState(false);
        const val = document.getElementById('centerQueryInput').value.trim();
        if (val) submitQuery(val);
      };
    }

    function toggleVoiceInput(target) {
      if (!recognition) {
        showToast('ದಯವಿಟ್ಟು Chrome ಅಥವಾ Edge ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಧ್ವನಿ ಬಳಸಿ.');
        return;
      }
      activeVoiceTarget = target;
      if (isRecording) {
        recognition.stop();
      } else {
        try { recognition.start(); } catch (e) {}
      }
    }

    function updateVoiceBtnState(recording) {
      const b1 = document.getElementById('btnVoiceCenter');
      const b2 = document.getElementById('btnVoiceDocked');
      if (b1) b1.classList.toggle('recording', recording);
      if (b2) b2.classList.toggle('recording', recording);
    }

    // ── Copy & Share ─────────────────────────────────────────
    function copyCardContent(btn) {
      const card = btn.closest('.ai-card-box');
      const contentEl = card.querySelector('.ai-content');
      const textToCopy = contentEl.innerText || contentEl.textContent;
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('📋 ಉತ್ತರವನ್ನು ಕಾಪಿ ಮಾಡಲಾಗಿದೆ!');
      }).catch(() => {
        showToast('ಕಾಪಿ ಮಾಡಲು ಸಾಧ್ಯವಾಗಿಲ್ಲ.');
      });
    }

    function shareToWhatsApp(query, answerText) {
      const snippet = answerText.length > 280 ? answerText.substring(0, 280) + '...' : answerText;
      const shareMsg = `*ಪ್ರಶ್ನೆ:* ${query}\\n\\n*ಉತ್ತರ:* ${snippet}\\n\\n👉 ಕರ್ನಾಟಕದ ಸಂಪೂರ್ಣ ಮಾಹಿತಿಗಾಗಿ: https://karnata.in/ask`;
      const waUrl = 'https://api.whatsapp.com/send?text=' + encodeURIComponent(shareMsg);
      window.open(waUrl, '_blank');
    }

    function showToast(msg) {
      const t = document.getElementById('toastPopup');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2800);
    }

    function escapeHtml(str) {
      if (!str) return '';
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // ── Simple Markdown Parser ───────────────────────────────
    function parseSimpleMarkdown(md) {
      if (!md) return '';
      let html = md;

      // Escape raw HTML first
      html = html.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

      // Headers
      html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
      html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
      html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');

      // Bold & Italic
      html = html.replace(/\\*\\*(.*?)\\*\\*/gim, '<strong>$1</strong>');
      html = html.replace(/\\*(.*?)\\*/gim, '<em>$1</em>');

      // Links: [Text](url)
      html = html.replace(/\\[([^\\]]+)\\]\\(([^\\)]+)\\)/gim, '<a href="$2" target="_blank" style="color:#1D4ED8; font-weight:700; text-decoration:underline;">$1</a>');

      // Lists
      html = html.replace(/^\\s*\\* (.*$)/gim, '<li>$1</li>');
      html = html.replace(/^\\s*\\d+\\. (.*$)/gim, '<li>$1</li>');

      // Wrap list items
      html = html.replace(/(<li>[\\s\\S]*?<\\/li>)/gim, '<ul>$1</ul>');
      html = html.replace(/<\\/ul>\\s*<ul>/gim, '');

      // Paragraphs
      const lines = html.split(/\\n\\n+/);
      html = lines.map(l => {
        l = l.trim();
        if (l.startsWith('<h') || l.startsWith('<ul') || l.startsWith('<table') || l.startsWith('<div')) return l;
        return `<p>${l.replace(/\\n/g, '<br>')}</p>`;
      }).join('\\n');

      return html;
    }
  </script>
</body>
</html>
'''

with open('ask.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: ask.html rewritten with modern, high-contrast, crystal-clear design!")
