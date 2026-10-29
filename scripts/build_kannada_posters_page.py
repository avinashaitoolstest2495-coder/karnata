# -*- coding: utf-8 -*-
"""
build_kannada_posters_page.py
Generates `kannada-posters.html` — Kannada Posters Gallery, Custom Name/Photo Editor & Poster Maker Studio
with 1-Click Share to Instagram, Facebook, WhatsApp, Telegram, X, Clipboard & HD Download.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
OUT_FILE = ROOT / "kannada-posters.html"

HTML = r"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ಕನ್ನಡ ಪೋಸ್ಟರ್ ಸ್ಟುಡಿಯೋ & ರಾಜ್ಯೋತ್ಸವ ಪೋಸ್ಟರ್ ಮೇಕರ್ | Kannada Posters Maker, Edit & Share — Karnata.in</title>
<meta name="description" content="ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ, ನಾಡಹಬ್ಬ, ಕವಿ ನುಡಿಮುತ್ತು ಮತ್ತು ಶುಭಾಶಯಗಳ HD ಪೋಸ್ಟರ್‌ಗಳನ್ನು ಉಚಿತವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ, ನಿಮ್ಮ ಹೆಸರು ಮತ್ತು ಫೋಟೋ ಸೇರಿಸಿ ಎಡಿಟ್ ಮಾಡಿ ಹಾಗೂ WhatsApp, Instagram, Facebook ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ.">
<meta name="keywords" content="Kannada Posters, Kannada Rajyotsava Posters, ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಪೋಸ್ಟರ್, Kannada Poster Maker Online, Kannada Quote Maker, Kannada Status Maker, WhatsApp Status Kannada, Instagram Kannada Posters, Bhuvaneshwari Poster, Karnataka Rajyotsava Wishes with Name and Photo">
<link rel="canonical" href="https://karnata.in/kannada-posters">

<!-- Open Graph / Social Media -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://karnata.in/kannada-posters">
<meta property="og:title" content="🎨 ಕನ್ನಡ ಪೋಸ್ಟರ್ ಸ್ಟುಡಿಯೋ — HD ಪೋಸ್ಟರ್ ಮೇಕರ್, ಎಡಿಟ್ & ಶೇರ್ | Karnata.in">
<meta property="og:description" content="ನಿಮ್ಮ ಹೆಸರು, ಫೋಟೋ ಮತ್ತು ಕನ್ನಡ ಶುಭಾಶಯಗಳೊಂದಿಗೆ ಆಕರ್ಷಕ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಹಾಗೂ ನುಡಿಮುತ್ತು ಪೋಸ್ಟರ್‌ಗಳನ್ನು ಸೆಕೆಂಡುಗಳಲ್ಲಿ ರಚಿಸಿ — Instagram, WhatsApp, Facebook ನಲ್ಲಿ ಶೇರ್ ಮಾಡಿ!">
<meta property="og:image" content="https://karnata.in/assets/images/kannada-posters/poster-1.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="🎨 ಕನ್ನಡ ಪೋಸ್ಟರ್ ಸ್ಟುಡಿಯೋ — HD ಪೋಸ್ಟರ್ ಮೇಕರ್, ಎಡಿಟ್ & ಶೇರ್">
<meta name="twitter:description" content="ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಮತ್ತು ನುಡಿಮುತ್ತು HD ಪೋಸ್ಟರ್ ಗ್ಯಾಲರಿ + ಲೈವ್ ಪೋಸ್ಟರ್ ಎಡಿಟಿಂಗ್ ಸ್ಟುಡಿಯೋ.">
<meta name="twitter:image" content="https://karnata.in/assets/images/kannada-posters/poster-1.jpg">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Hubballi&family=Noto+Serif+Kannada:wght@600;700;900&family=Tiro+Kannada:ital@0;1&display=swap" rel="stylesheet">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "ಕನ್ನಡ ಪೋಸ್ಟರ್ ಸ್ಟುಡಿಯೋ & ಪೋಸ್ಟರ್ ಮೇಕರ್ (Kannada Poster Maker Studio)",
      "url": "https://karnata.in/kannada-posters",
      "applicationCategory": "DesignApplication",
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      },
      "description": "Create, customize, download, and share HD Kannada Rajyotsava posters, Karnataka heritage greetings, and Kannada quote posters with custom name, photo, and phonetic Kannada typing."
    },
    {
      "@type": "ImageGallery",
      "name": "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ HD ಪೋಸ್ಟರ್ ಗ್ಯಾಲರಿ",
      "url": "https://karnata.in/kannada-posters#gallery",
      "image": [
        "https://karnata.in/assets/images/kannada-posters/poster-1.jpg",
        "https://karnata.in/assets/images/kannada-posters/poster-2.jpg",
        "https://karnata.in/assets/images/kannada-posters/poster-3.jpg",
        "https://karnata.in/assets/images/kannada-posters/poster-4.jpg",
        "https://karnata.in/assets/images/kannada-posters/poster-5.jpg"
      ]
    }
  ]
}
</script>

<style>
:root {
  --font-kn: 'Anek Kannada', system-ui, -apple-system, sans-serif;
  --bg-dark: #090D16;
  --bg-card: #111827;
  --bg-light: #F8FAFC;
  --gold: #F59E0B;
  --gold-lt: #FDE68A;
  --red: #DC2626;
  --red-dk: #991B1B;
  --emerald: #10B981;
  --indigo: #4F46E5;
  --ink: #0F172A;
  --ink-muted: #475569;
  --border: #E2E8F0;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body, button, input, select, textarea {
  font-family: var(--font-kn) !important;
}

body {
  background: var(--bg-light);
  color: var(--ink);
  line-height: 1.6;
  overflow-x: hidden;
}

/* ── HERO SECTION ── */
.kp-hero {
  background: radial-gradient(circle at 15% 20%, rgba(245, 158, 11, 0.25) 0%, transparent 45%),
              radial-gradient(circle at 85% 80%, rgba(220, 38, 38, 0.28) 0%, transparent 50%),
              linear-gradient(135deg, #090D16 0%, #171028 50%, #2A0A10 100%);
  color: #FFFFFF;
  padding: 36px 20px 44px;
  position: relative;
  overflow: hidden;
  border-bottom: 4px solid var(--gold);
}

.kp-hero::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 5px;
  background: linear-gradient(90deg, #FACC15 0%, #FACC15 50%, #DC2626 50%, #DC2626 100%);
}

.kp-container {
  max-width: 1280px;
  margin: 0 auto;
}

.kp-hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 32px;
  align-items: center;
}

@media (max-width: 960px) {
  .kp-hero-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }
}

.kp-badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
}

@media (max-width: 960px) {
  .kp-badge-row {
    justify-content: center;
  }
}

.kp-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 13px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.02em;
}

.kp-pill-gold {
  background: rgba(250, 204, 21, 0.16);
  color: #FDE047;
  border: 1px solid rgba(250, 204, 21, 0.4);
}

.kp-pill-red {
  background: rgba(220, 38, 38, 0.25);
  color: #FCA5A5;
  border: 1px solid rgba(248, 113, 113, 0.4);
}

.kp-pill-green {
  background: rgba(16, 185, 129, 0.2);
  color: #6EE7B7;
  border: 1px solid rgba(52, 211, 153, 0.35);
}

.kp-hero-title {
  font-size: clamp(28px, 4.2vw, 46px);
  font-weight: 900;
  line-height: 1.18;
  margin-bottom: 14px;
  background: linear-gradient(95deg, #FFFFFF 0%, #FDE047 55%, #FB923C 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.kp-hero-points {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));
  gap: 10px;
  margin-bottom: 22px;
  text-align: left;
}

.kp-hero-points li {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  padding: 10px 14px;
  font-size: 14px;
  font-weight: 600;
  color: #E2E8F0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.kp-hero-cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

@media (max-width: 960px) {
  .kp-hero-cta-row {
    justify-content: center;
  }
}

.kp-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 22px;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 800;
  text-decoration: none;
  cursor: pointer;
  border: none;
  transition: all 0.2s ease;
}

.kp-btn-primary {
  background: linear-gradient(135deg, #FACC15 0%, #F59E0B 50%, #DC2626 100%);
  color: #090D16;
  box-shadow: 0 10px 25px rgba(245, 158, 11, 0.35);
}

.kp-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px rgba(245, 158, 11, 0.5);
}

.kp-btn-glass {
  background: rgba(255, 255, 255, 0.1);
  color: #FFFFFF;
  border: 1.5px solid rgba(255, 255, 255, 0.24);
  backdrop-filter: blur(8px);
}

.kp-btn-glass:hover {
  background: rgba(255, 255, 255, 0.18);
  transform: translateY(-2px);
}

/* Hero Fan Showcase */
.kp-hero-fan {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  perspective: 1000px;
}

.kp-fan-card {
  width: 135px;
  height: 170px;
  border-radius: 16px;
  overflow: hidden;
  border: 2.5px solid #FACC15;
  box-shadow: 0 16px 35px rgba(0, 0, 0, 0.6);
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  background: #000;
}

.kp-fan-card:nth-child(1) { transform: rotate(-8deg) translateY(10px); }
.kp-fan-card:nth-child(2) { width: 160px; height: 200px; z-index: 3; border-color: #FFFFFF; box-shadow: 0 20px 45px rgba(245,158,11,0.45); }
.kp-fan-card:nth-child(3) { transform: rotate(8deg) translateY(10px); }

.kp-fan-card:hover {
  transform: scale(1.08) rotate(0deg) !important;
  z-index: 5;
}

.kp-fan-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* ── QUICK NAVIGATION TABS ── */
.kp-mode-nav {
  background: #FFFFFF;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 80px;
  z-index: 90;
  box-shadow: 0 4px 15px rgba(15, 23, 42, 0.05);
}

.kp-mode-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  overflow-x: auto;
}

.kp-nav-pills {
  display: flex;
  gap: 8px;
}

.kp-nav-tab {
  padding: 9px 18px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 800;
  border: 1.5px solid var(--border);
  background: #F8FAFC;
  color: var(--ink-muted);
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.kp-nav-tab.active, .kp-nav-tab:hover {
  background: #FEF2F2;
  color: var(--red);
  border-color: #FECACA;
}

/* ── SECTION HEADERS ── */
.kp-section {
  padding: 40px 20px;
  max-width: 1280px;
  margin: 0 auto;
}

.kp-sec-head {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-end;
  gap: 16px;
  margin-bottom: 24px;
}

.kp-sec-title {
  font-size: clamp(22px, 3vw, 32px);
  font-weight: 900;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 10px;
}

.kp-sec-sub {
  font-size: 15px;
  color: var(--ink-muted);
  font-weight: 600;
}

/* ── GALLERY GRID (5 READY HD POSTERS + TEMPLATES) ── */
.kp-filter-bar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.kp-filter-chip {
  padding: 7px 16px;
  border-radius: 999px;
  font-size: 13.5px;
  font-weight: 800;
  background: #FFFFFF;
  border: 1.5px solid #CBD5E1;
  color: #334155;
  cursor: pointer;
  transition: all 0.15s;
}

.kp-filter-chip.active, .kp-filter-chip:hover {
  background: var(--ink);
  color: #FACC15;
  border-color: var(--ink);
}

.kp-gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.kp-poster-card {
  background: #FFFFFF;
  border-radius: 20px;
  border: 1.5px solid #E2E8F0;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.kp-poster-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.13);
  border-color: #F59E0B;
}

.kp-poster-img-wrap {
  position: relative;
  aspect-ratio: 4 / 5;
  background: #0F172A;
  overflow: hidden;
}

.kp-poster-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.35s ease;
}

.kp-poster-card:hover .kp-poster-img-wrap img {
  transform: scale(1.03);
}

.kp-card-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(9, 13, 22, 0.85);
  color: #FACC15;
  border: 1px solid rgba(250, 204, 21, 0.5);
  padding: 4px 11px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 800;
  backdrop-filter: blur(6px);
}

.kp-zoom-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(9, 13, 22, 0.8);
  color: #FFFFFF;
  border: 1px solid rgba(255,255,255,0.25);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  transition: all 0.2s;
}

.kp-zoom-btn:hover {
  background: var(--gold);
  color: #000;
}

.kp-poster-body {
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

.kp-poster-title {
  font-size: 18px;
  font-weight: 900;
  color: var(--ink);
  line-height: 1.3;
}

.kp-poster-points {
  list-style: none;
  font-size: 13px;
  color: var(--ink-muted);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.kp-poster-points li::before {
  content: "• ";
  color: var(--red);
  font-weight: 900;
}

/* Primary Edit & Download Actions */
.kp-card-actions-main {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 8px;
  margin-top: auto;
}

.kp-act-btn {
  padding: 10px 12px;
  border-radius: 12px;
  font-size: 13.5px;
  font-weight: 800;
  cursor: pointer;
  border: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.2s;
  text-decoration: none;
}

.kp-act-edit {
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
  color: #090D16;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
}

.kp-act-edit:hover {
  background: linear-gradient(135deg, #FBBF24 0%, #B45309 100%);
  transform: translateY(-1px);
}

.kp-act-save {
  background: #0F172A;
  color: #FFFFFF;
}

.kp-act-save:hover {
  background: #1E293B;
  transform: translateY(-1px);
}

/* Social Share Row */
.kp-share-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding-top: 10px;
  border-top: 1px dashed #E2E8F0;
}

.kp-share-label {
  font-size: 11.5px;
  font-weight: 800;
  color: #64748B;
}

.kp-social-btns {
  display: flex;
  gap: 6px;
}

.kp-soc-btn {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  border: 1px solid #E2E8F0;
  background: #F8FAFC;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  font-weight: 800;
  transition: all 0.18s;
  color: #1E293B;
}

.kp-soc-btn:hover {
  transform: translateY(-2px);
}

.kp-soc-wa { background: #DCFCE7; color: #15803D; border-color: #86EFAC; }
.kp-soc-wa:hover { background: #22C55E; color: #FFFFFF; }

.kp-soc-ig { background: #FCE7F3; color: #BE185D; border-color: #F9A8D4; }
.kp-soc-ig:hover { background: linear-gradient(45deg, #F58529, #DD2A7B, #8134AF); color: #FFFFFF; }

.kp-soc-fb { background: #DBEAFE; color: #1D4ED8; border-color: #93C5FD; }
.kp-soc-fb:hover { background: #2563EB; color: #FFFFFF; }

.kp-soc-tg { background: #E0F2FE; color: #0369A1; border-color: #7DD3FC; }
.kp-soc-tg:hover { background: #0284C7; color: #FFFFFF; }

.kp-soc-cp { background: #F1F5F9; color: #334155; border-color: #CBD5E1; }
.kp-soc-cp:hover { background: #334155; color: #FFFFFF; }

/* ── INTERACTIVE POSTER MAKER & EDITOR STUDIO ── */
.kp-studio-wrap {
  background: linear-gradient(145deg, #090D16 0%, #111827 60%, #1E1B4B 100%);
  border-radius: 28px;
  border: 2px solid rgba(250, 204, 21, 0.4);
  padding: 28px;
  color: #FFFFFF;
  box-shadow: 0 25px 60px rgba(9, 13, 22, 0.35);
  margin-top: 16px;
}

@media (max-width: 768px) {
  .kp-studio-wrap {
    padding: 18px 14px;
    border-radius: 20px;
  }
}

.kp-studio-grid {
  display: grid;
  grid-template-columns: 440px 1fr;
  gap: 28px;
  align-items: start;
}

@media (max-width: 1040px) {
  .kp-studio-grid {
    grid-template-columns: 1fr;
  }
}

/* Left Column: Sticky Live Canvas Preview + Export Bar */
.kp-canvas-panel {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 22px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: sticky;
  top: 140px;
}

@media (max-width: 1040px) {
  .kp-canvas-panel {
    position: static;
  }
}

.kp-canvas-stage {
  width: 100%;
  max-width: 390px;
  border-radius: 16px;
  overflow: hidden;
  border: 3px solid #FACC15;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.65);
  background: #000000;
  position: relative;
  touch-action: none;
}

#posterCanvas {
  width: 100%;
  height: auto;
  display: block;
  cursor: grab;
}

#posterCanvas:active {
  cursor: grabbing;
}

.kp-canvas-hint {
  margin-top: 10px;
  font-size: 12.5px;
  color: #FDE047;
  font-weight: 700;
  text-align: center;
  background: rgba(250, 204, 21, 0.12);
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid rgba(250, 204, 21, 0.3);
}

/* Studio Export & Share Matrix */
.kp-studio-export-grid {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 16px;
}

.kp-exp-btn {
  padding: 12px 14px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 800;
  cursor: pointer;
  border: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s;
}

.kp-exp-png {
  background: linear-gradient(135deg, #FACC15 0%, #F59E0B 100%);
  color: #090D16;
  grid-column: span 2;
  font-size: 15.5px;
  box-shadow: 0 8px 22px rgba(245, 158, 11, 0.35);
}

.kp-exp-png:hover {
  transform: translateY(-2px);
}

.kp-exp-wa {
  background: #16A34A;
  color: #FFFFFF;
}

.kp-exp-ig {
  background: linear-gradient(45deg, #F58529, #DD2A7B, #8134AF);
  color: #FFFFFF;
}

.kp-exp-fb {
  background: #2563EB;
  color: #FFFFFF;
}

.kp-exp-copy {
  background: rgba(255, 255, 255, 0.14);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.25);
}

/* Right Column: Controls & Tabs */
.kp-controls-panel {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.kp-ctrl-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: 18px;
}

.kp-ctrl-title {
  font-size: 16px;
  font-weight: 900;
  color: #FDE047;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

/* Background Thumbnail Selector */
.kp-bg-strip {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(74px, 1fr));
  gap: 10px;
}

.kp-bg-thumb {
  height: 82px;
  border-radius: 12px;
  overflow: hidden;
  border: 2.5px solid rgba(255, 255, 255, 0.2);
  cursor: pointer;
  position: relative;
  transition: all 0.2s;
  background: #0F172A;
}

.kp-bg-thumb.active, .kp-bg-thumb:hover {
  border-color: #FACC15;
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(250, 204, 21, 0.4);
}

.kp-bg-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.kp-bg-thumb-label {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  background: rgba(0, 0, 0, 0.75);
  color: #FFF;
  font-size: 10px;
  font-weight: 700;
  text-align: center;
  padding: 2px 3px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Form Controls */
.kp-input-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}

.kp-label {
  font-size: 13px;
  font-weight: 800;
  color: #CBD5E1;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.kp-input, .kp-textarea, .kp-select {
  width: 100%;
  background: rgba(15, 23, 42, 0.85);
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 10px 14px;
  color: #FFFFFF;
  font-size: 15px;
  font-weight: 600;
  outline: none;
  transition: border-color 0.2s;
}

.kp-input:focus, .kp-textarea:focus, .kp-select:focus {
  border-color: #FACC15;
}

.kp-textarea {
  min-height: 82px;
  resize: vertical;
}

.kp-row-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

@media (max-width: 600px) {
  .kp-row-2 {
    grid-template-columns: 1fr;
  }
}

.kp-row-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

/* Quote Preset Chips */
.kp-quote-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
  margin-bottom: 10px;
}

.kp-quote-chip {
  padding: 6px 13px;
  border-radius: 999px;
  background: rgba(250, 204, 21, 0.14);
  border: 1px solid rgba(250, 204, 21, 0.35);
  color: #FDE047;
  font-size: 12.5px;
  font-weight: 700;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.15s;
}

.kp-quote-chip:hover {
  background: #FACC15;
  color: #090D16;
}

/* Phonetic Toggle Pill */
.kp-phonetic-toggle {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid rgba(16, 185, 129, 0.45);
  color: #6EE7B7;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 800;
  cursor: pointer;
}

/* Toast Notification */
.kp-toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #0F172A;
  color: #FFFFFF;
  border: 2px solid #FACC15;
  padding: 14px 20px;
  border-radius: 16px;
  font-size: 14px;
  font-weight: 800;
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
  z-index: 999999;
  display: none;
  align-items: center;
  gap: 10px;
  max-width: 90vw;
}

/* Fullscreen Lightbox */
.kp-lightbox {
  position: fixed;
  inset: 0;
  background: rgba(9, 13, 22, 0.92);
  backdrop-filter: blur(10px);
  z-index: 999998;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.kp-lightbox.open {
  display: flex;
}

.kp-lb-inner {
  max-width: 520px;
  width: 100%;
  background: #111827;
  border: 2px solid #FACC15;
  border-radius: 22px;
  overflow: hidden;
  position: relative;
}

.kp-lb-close {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #DC2626;
  color: #FFF;
  border: none;
  font-size: 18px;
  font-weight: 900;
  cursor: pointer;
  z-index: 2;
}
</style>
<script src="/nav-component.js" defer></script>
</head>
<body>

<!-- ── HERO SECTION ── -->
<section class="kp-hero">
  <div class="kp-container">
    <div class="kp-hero-grid">
      <div>
        <div class="kp-badge-row">
          <span class="kp-pill kp-pill-gold">💛❤️ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ & ನಾಡಹಬ್ಬ ವಿಶೇಷ</span>
          <span class="kp-pill kp-pill-green">✨ ನಿಮ್ಮ ಹೆಸರು & ಫೋಟೋ ಎಡಿಟರ್</span>
          <span class="kp-pill kp-pill-red">📲 1-Click WhatsApp · Insta · FB Share</span>
        </div>
        <h1 class="kp-hero-title">ಕನ್ನಡ ಪೋಸ್ಟರ್ ಸ್ಟುಡಿಯೋ — ಎಡಿಟ್, ಡೌನ್‌ಲೋಡ್ & ಶೇರ್</h1>
        <ul class="kp-hero-points">
          <li>🎨 <strong>5 HD ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಪೋಸ್ಟರ್‌ಗಳು:</strong> ಉಚಿತ ಡೌನ್‌ಲೋಡ್ ಮತ್ತು ಕಸ್ಟಮೈಸ್</li>
          <li>👤 <strong>ನಿಮ್ಮ ಹೆಸರು & ಫೋಟೋ ಸೇರಿಸಿ:</strong> ಪೋಸ್ಟರ್ ಕೆಳಭಾಗದಲ್ಲಿ ಆಕರ್ಷಕ ಗುರುತಿನ ಬ್ಯಾನರ್</li>
          <li>⌨️ <strong>ಫೋನೆಟಿಕ್ ಕನ್ನಡ ಟೈಪಿಂಗ್:</strong> ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಟೈಪ್ ಮಾಡಿದರೆ ತಕ್ಷಣ ಕನ್ನಡ ಅಕ್ಷರ</li>
          <li>📲 <strong>ನೇರ ಶೇರ್ (Direct Share):</strong> Instagram, WhatsApp Status, Facebook, Telegram</li>
        </ul>
        <div class="kp-hero-cta-row">
          <a href="#poster-studio" class="kp-btn kp-btn-primary">🖌️ ಹೊಸ ಪೋಸ್ಟರ್ ರಚಿಸಿ / ಎಡಿಟ್ ಮಾಡಿ →</a>
          <a href="#poster-gallery" class="kp-btn kp-btn-glass">🖼️ HD ಪೋಸ್ಟರ್ ಗ್ಯಾಲರಿ ನೋಡಿ (5+)</a>
        </div>
      </div>

      <div class="kp-hero-fan">
        <div class="kp-fan-card" onclick="loadPosterIntoStudio(0)" title="ಕ್ಲಿಕ್ ಮಾಡಿ ಎಡಿಟ್ ಮಾಡಿ">
          <img src="/assets/images/kannada-posters/poster-1.jpg" alt="ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಪರಂಪರೆ ಪೋಸ್ಟರ್" fetchpriority="high">
        </div>
        <div class="kp-fan-card" onclick="loadPosterIntoStudio(3)" title="ತಾಯಿ ಭುವನೇಶ್ವರಿ ಪೋಸ್ಟರ್ ಎಡಿಟ್ ಮಾಡಿ">
          <img src="/assets/images/kannada-posters/poster-4.jpg" alt="ತಾಯಿ ಭುವನೇಶ್ವರಿ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಪೋಸ್ಟರ್">
        </div>
        <div class="kp-fan-card" onclick="loadPosterIntoStudio(4)" title="ಕನ್ನಡ ಜನೋತ್ಸವ ಪೋಸ್ಟರ್ ಎಡಿಟ್ ಮಾಡಿ">
          <img src="/assets/images/kannada-posters/poster-5.jpg" alt="ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಜನೋತ್ಸವ ಪೋಸ್ಟರ್">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── STICKY MODE BAR ── -->
<div class="kp-mode-nav">
  <div class="kp-mode-inner">
    <div class="kp-nav-pills">
      <a href="#poster-gallery" class="kp-nav-tab active">🖼️ HD ಪೋಸ್ಟರ್ ಗ್ಯಾಲರಿ (Save & Share)</a>
      <a href="#poster-studio" class="kp-nav-tab">🖌️ ಲೈವ್ ಪೋಸ್ಟರ್ ಮೇಕರ್ & ಎಡಿಟರ್ ಸ್ಟುಡಿಯೋ</a>
      <a href="#quotes-bank" class="kp-nav-tab">📜 ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಶುಭಾಶಯ & ನುಡಿಮುತ್ತುಗಳು</a>
      <a href="/sahitya-kannada-keyboard" class="kp-nav-tab">⌨️ ಸಾಹಿತ್ಯ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ ಆ್ಯಪ್</a>
    </div>
  </div>
</div>

<!-- ── SECTION 1: READY HD KANNADA POSTERS GALLERY ── -->
<section class="kp-section" id="poster-gallery">
  <div class="kp-sec-head">
    <div>
      <h2 class="kp-sec-title">🖼️ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಮತ್ತು ನಾಡಿನ ಹಿರಿಮೆಯ HD ಪೋಸ್ಟರ್ ಗ್ಯಾಲರಿ</h2>
      <p class="kp-sec-sub">ಯಾವುದೇ ಪೋಸ್ಟರ್ ಅನ್ನು ನೇರವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ, ಸೋಶಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ ಶೇರ್ ಮಾಡಿ ಅಥವಾ <strong>"✏️ ಎಡಿಟ್ ಮಾಡಿ"</strong> ಒತ್ತಿ ನಿಮ್ಮ ಹೆಸರು, ಫೋಟೋ ಮತ್ತು ಶುಭಾಶಯ ಸೇರಿಸಿ!</p>
    </div>
  </div>

  <div class="kp-filter-bar">
    <button class="kp-filter-chip active" onclick="filterGallery('all', this)">✨ ಎಲ್ಲಾ ಪೋಸ್ಟರ್‌ಗಳು (All)</button>
    <button class="kp-filter-chip" onclick="filterGallery('heritage', this)">🏛️ ಕರ್ನಾಟಕ ಪರಂಪರೆ & ಹಂಪಿ</button>
    <button class="kp-filter-chip" onclick="filterGallery('bhuvaneshwari', this)">👑 ತಾಯಿ ಭುವನೇಶ್ವರಿ</button>
    <button class="kp-filter-chip" onclick="filterGallery('celebration', this)">🎉 ಜನೋತ್ಸವ & ಸಂಸ್ಕೃತಿ</button>
  </div>

  <div class="kp-gallery-grid" id="galleryGrid"></div>
</section>

<!-- ── SECTION 2: LIVE INTERACTIVE KANNADA POSTER MAKER & EDITOR STUDIO ── -->
<section class="kp-section" id="poster-studio">
  <div class="kp-sec-head">
    <div>
      <h2 class="kp-sec-title">🖌️ ಲೈವ್ ಕನ್ನಡ ಪೋಸ್ಟರ್ ಮೇಕರ್ & ಎಡಿಟಿಂಗ್ ಸ್ಟುಡಿಯೋ (Pro Editor)</h2>
      <p class="kp-sec-sub">ಪೋಸ್ಟರ್ ಮೇಲಿನ ಬರಹ ಅಥವಾ ನಿಮ್ಮ ಹೆಸರಿನ ಬ್ಯಾಡ್ಜ್ ಅನ್ನು ಬೆರಳಿನಿಂದ / ಮೌಸ್‌ನಿಂದ ಎಲ್ಲಿಗೆ ಬೇಕಾದರೂ ಎಳೆದು ಜೋಡಿಸಿ (Drag & Move)!</p>
    </div>
  </div>

  <div class="kp-studio-wrap">
    <div class="kp-studio-grid">
      <!-- LEFT: LIVE CANVAS PREVIEW & SHARE/SAVE BUTTONS -->
      <div class="kp-canvas-panel">
        <div class="kp-canvas-stage" id="canvasStage">
          <canvas id="posterCanvas" width="1080" height="1350"></canvas>
        </div>
        <div class="kp-canvas-hint">💡 ಟಿಪ್: ಪೋಸ್ಟರ್ ಮೇಲಿರುವ ಕನ್ನಡ ಬರಹವನ್ನು ಮೌಸ್ ಅಥವಾ ಬೆರಳಿನಿಂದ ಎಳೆದು (Drag) ಬೇಕಾದ ಜಾಗದಲ್ಲಿ ಇಡಿ</div>

        <div class="kp-studio-export-grid">
          <button class="kp-exp-btn kp-exp-png" onclick="downloadStudioPoster('png')">
            ⬇️ HD ಪೋಸ್ಟರ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ (Save PNG)
          </button>
          <button class="kp-exp-btn kp-exp-wa" onclick="shareStudioPoster('whatsapp')">
            📲 WhatsApp ಶೇರ್
          </button>
          <button class="kp-exp-btn kp-exp-ig" onclick="shareStudioPoster('instagram')">
            📸 Instagram ಶೇರ್
          </button>
          <button class="kp-exp-btn kp-exp-fb" onclick="shareStudioPoster('facebook')">
            📘 Facebook ಶೇರ್
          </button>
          <button class="kp-exp-btn kp-exp-copy" onclick="copyStudioPosterToClipboard()">
            📋 ಕಾಪಿ ಇಮೇಜ್ (Copy)
          </button>
        </div>

        <div style="display:flex; gap:8px; width:100%; margin-top:10px; justify-content:center; flex-wrap:wrap;">
          <button class="kp-soc-btn kp-soc-tg" style="width:auto; padding:6px 12px; font-size:12.5px;" onclick="shareStudioPoster('telegram')">✈️ Telegram</button>
          <button class="kp-soc-btn" style="width:auto; padding:6px 12px; font-size:12.5px; background:#000; color:#FFF;" onclick="shareStudioPoster('twitter')">𝕏 Twitter/X</button>
          <button class="kp-soc-btn" style="width:auto; padding:6px 12px; font-size:12.5px;" onclick="downloadStudioPoster('jpg')">🖼️ Save JPG</button>
          <button class="kp-soc-btn" style="width:auto; padding:6px 12px; font-size:12.5px;" onclick="resetStudioLayout()">🔄 ರೀಸೆಟ್ (Reset)</button>
        </div>
      </div>

      <!-- RIGHT: MULTI-LAYER CONTROLS -->
      <div class="kp-controls-panel">

        <!-- STEP 1: CHOOSE POSTER TEMPLATE OR ROYAL GRADIENT OR UPLOAD PHOTO -->
        <div class="kp-ctrl-card">
          <div class="kp-ctrl-title">
            <span>1️⃣ ಹಿನ್ನೆಲೆ ಪೋಸ್ಟರ್ ಆಯ್ಕೆ ಮಾಡಿ (Choose Poster / Background)</span>
            <label style="background:#FACC15; color:#090D16; padding:5px 12px; border-radius:999px; font-size:12px; cursor:pointer; font-weight:900;">
              📷 ನಿಮ್ಮ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ
              <input type="file" id="bgUploadInput" accept="image/*" style="display:none" onchange="handleCustomBgUpload(event)">
            </label>
          </div>
          <div class="kp-bg-strip" id="studioBgStrip"></div>

          <div class="kp-row-3" style="margin-top:14px;">
            <div>
              <label class="kp-label">📐 ಪೋಸ್ಟರ್ ಅಳತೆ (Size)</label>
              <select class="kp-select" id="aspectSelect" onchange="changeCanvasAspect(this.value)">
                <option value="4:5">4:5 (Insta / FB Portrait)</option>
                <option value="1:1">1:1 (Square Post)</option>
                <option value="9:16">9:16 (WhatsApp Status / Story)</option>
              </select>
            </div>
            <div>
              <label class="kp-label">🌑 ಹಿನ್ನೆಲೆ ಡಾರ್ಕ್ ಶೇಡ್ (Dim)</label>
              <input type="range" id="bgDimSlider" min="0" max="75" value="10" style="width:100%; accent-color:#FACC15; margin-top:10px;" oninput="renderStudioCanvas()">
            </div>
            <div>
              <label class="kp-label">🎏 ಕನ್ನಡ ಧ್ವಜ ಬಾರ್ಡರ್</label>
              <select class="kp-select" id="borderStyleSelect" onchange="renderStudioCanvas()">
                <option value="gold-red">💛❤️ ಕನ್ನಡ ಧ್ವಜ + ಚಿನ್ನದ ಫ್ರೇಮ್</option>
                <option value="royal-gold">✨ ರಾಯಲ್ ಗೋಲ್ಡ್ ಫ್ರೇಮ್</option>
                <option value="none">🚫 ಬಾರ್ಡರ್ ಬೇಡ (Clean)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- STEP 2: KANNADA GREETING / QUOTE TEXT LAYER -->
        <div class="kp-ctrl-card">
          <div class="kp-ctrl-title">
            <span>2️⃣ ಕನ್ನಡ ಶುಭಾಶಯ ಸಂದೇಶ / ನುಡಿಮುತ್ತು ಬರೆಯಿರಿ</span>
            <label class="kp-phonetic-toggle" title="ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ ಸ್ಪೇಸ್ ಒತ್ತಿದರೆ ಕನ್ನಡವಾಗುತ್ತದೆ">
              <input type="checkbox" id="phoneticToggle" checked>
              ⌨️ ಇಂಗ್ಲಿಷ್ → ಕನ್ನಡ ಟೈಪಿಂಗ್ ON
            </label>
          </div>

          <div class="kp-quote-chips" id="studioQuoteChips"></div>

          <div class="kp-input-group">
            <label class="kp-label">
              <span>✨ ಮುಖ್ಯ ಶೀರ್ಷಿಕೆ / ಮೇಲಿನ ಸಾಲು (Header Badge - ಐಚ್ಛಿಕ)</span>
              <button type="button" onclick="document.getElementById('headerTextInput').value=''; renderStudioCanvas();" style="background:none;border:none;color:#FCA5A5;font-size:11.5px;cursor:pointer;font-weight:800;">ಅಳಿಸಿ (Clear)</button>
            </label>
            <input type="text" id="headerTextInput" class="kp-input phonetic-field" value="💛❤️ ನಾಡಿನ ಸಮಸ್ತ ಜನತೆಗೆ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಹಾರ್ದಿಕ ಶುಭಾಶಯಗಳು" placeholder="ಉದಾ: ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಹಾರ್ದಿಕ ಶುಭಾಶಯಗಳು..." oninput="renderStudioCanvas()">
          </div>

          <div class="kp-input-group">
            <label class="kp-label">
              <span>📝 ಶುಭಾಶಯ ಪಠ್ಯ / ಕವನ / ನುಡಿಮುತ್ತು (Main Poster Quote)</span>
              <button type="button" onclick="document.getElementById('quoteTextInput').value=''; renderStudioCanvas();" style="background:none;border:none;color:#FCA5A5;font-size:11.5px;cursor:pointer;font-weight:800;">ಅಳಿಸಿ (Clear)</button>
            </label>
            <textarea id="quoteTextInput" class="kp-textarea phonetic-field" placeholder="ನಿಮ್ಮ ಸಂದೇಶವನ್ನು ಇಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ (ಉದಾ: elladaru iru entadaru iru endendigu nee kannadavagiru)..." oninput="renderStudioCanvas()">ಎಲ್ಲಾದರೂ ಇರು ಎಂತಾದರೂ ಇರು
ಎಂದೆಂದಿಗೂ ನೀ ಕನ್ನಡವಾಗಿರು
ಕನ್ನಡವೇ ಸತ್ಯ, ಕನ್ನಡವೇ ನಿತ್ಯ!</textarea>
          </div>

          <div class="kp-row-3">
            <div>
              <label class="kp-label">🔤 ಕನ್ನಡ ಫಾಂಟ್ ಶೈಲಿ</label>
              <select class="kp-select" id="fontFamilySelect" onchange="renderStudioCanvas()">
                <option value="'Anek Kannada', sans-serif">Anek Kannada (ಆಧುನಿಕ ಬೋಲ್ಡ್)</option>
                <option value="'Noto Serif Kannada', serif">Noto Serif (ಸಾಂಪ್ರದಾಯಿಕ)</option>
                <option value="'Tiro Kannada', serif">Tiro Kannada (ಸಾಹಿತ್ಯ ಶೈಲಿ)</option>
                <option value="'Hubballi', sans-serif">Hubballi (ಸರಳ ಸುಂದರ)</option>
              </select>
            </div>
            <div>
              <label class="kp-label">📏 ಅಕ್ಷರ ಗಾತ್ರ (Font Size)</label>
              <input type="range" id="fontSizeSlider" min="26" max="76" value="44" style="width:100%; accent-color:#FACC15; margin-top:10px;" oninput="renderStudioCanvas()">
            </div>
            <div>
              <label class="kp-label">🎨 ಅಕ್ಷರ ಬಣ್ಣ (Text Color)</label>
              <select class="kp-select" id="textColorSelect" onchange="renderStudioCanvas()">
                <option value="#FFFFFF">⚪ ಶ್ವೇತ ಬಿಳಿ (Pure White)</option>
                <option value="#FDE047">🟡 ಸುವರ್ಣ ಹಳದಿ (Kannada Gold)</option>
                <option value="#FEF08A">✨ ಕ್ರೀಮ್ ಗೋಲ್ಡ್ (Warm Cream)</option>
                <option value="#FCA5A5">🔴 ಕೆಂಪು ಪ್ರಭೆ (Soft Red)</option>
                <option value="#0F172A">⚫ ಕಪ್ಪು ಅಕ್ಷರ (Dark Ink)</option>
              </select>
            </div>
          </div>

          <div class="kp-row-3" style="margin-top:10px;">
            <div>
              <label class="kp-label">📍 ಬರಹದ ಸ್ಥಾನ (Quick Position)</label>
              <select class="kp-select" id="textPosPreset" onchange="applyTextPositionPreset(this.value)">
                <option value="bottom" selected>⬇️ ಕೆಳಭಾಗ (Bottom Above Name)</option>
                <option value="center">⏺️ ಮಧ್ಯಭಾಗ (Center)</option>
                <option value="top">⬆️ ಮೇಲ್ಭಾಗ (Top)</option>
              </select>
            </div>
            <div>
              <label class="kp-label">🛡️ ಬರಹದ ಹಿಂದೆ ಬಾಕ್ಸ್ (Backdrop)</label>
              <select class="kp-select" id="textBoxStyle" onchange="renderStudioCanvas()">
                <option value="glass-dark" selected>🌑 ಡಾರ್ಕ್ ಗ್ಲಾಸ್ ಬಾಕ್ಸ್ (Readable)</option>
                <option value="royal-red">🔴 ಕೆಂಪು-ಚಿನ್ನದ ಬ್ಯಾನರ್</option>
                <option value="shadow-only">✨ ಕೇವಲ 3D ಶ್ಯಾಡೋ (No Box)</option>
              </select>
            </div>
            <div>
              <label class="kp-label">✍️ ಕವಿ / ಲೇಖಕರ ಹೆಸರು (ಐಚ್ಛಿಕ)</label>
              <input type="text" id="authorTextInput" class="kp-input phonetic-field" value="— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು" placeholder="ಉದಾ: — ಕುವೆಂಪು" oninput="renderStudioCanvas()">
            </div>
          </div>
        </div>

        <!-- STEP 3: SENDER NAME, DESIGNATION & PHOTO BANNER (PERSONALIZATION) -->
        <div class="kp-ctrl-card">
          <div class="kp-ctrl-title">
            <span>3️⃣ ನಿಮ್ಮ ಹೆಸರು, ಪದವಿ & ಫೋಟೋ ಸೇರಿಸಿ (Personal Footer Banner)</span>
            <label style="display:inline-flex;align-items:center;gap:6px;font-size:12.5px;color:#6EE7B7;cursor:pointer;">
              <input type="checkbox" id="showFooterToggle" checked onchange="renderStudioCanvas()">
              ✅ ಹೆಸರಿನ ಪಟ್ಟಿ ತೋರಿಸಿ
            </label>
          </div>

          <div class="kp-row-2">
            <div class="kp-input-group">
              <label class="kp-label">👤 ನಿಮ್ಮ ಹೆಸರು (Your Name)</label>
              <input type="text" id="senderNameInput" class="kp-input phonetic-field" value="" placeholder="ಇಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು ಬರೆಯಿರಿ (ಉದಾ: ಶಿವಕುಮಾರ್ ಬಿ. ಆರ್.)" oninput="renderStudioCanvas()">
            </div>
            <div class="kp-input-group">
              <label class="kp-label">🏛️ ಪದವಿ / ಸಂಸ್ಥೆ / ಊರು (Subtitle / City)</label>
              <input type="text" id="senderRoleInput" class="kp-input phonetic-field" value="" placeholder="ಉದಾ: ಕನ್ನಡಾಭಿಮಾನಿ · ಬೆಂಗಳೂರು" oninput="renderStudioCanvas()">
            </div>
          </div>

          <div class="kp-row-2" style="align-items:center;">
            <div>
              <label class="kp-label">🤳 ನಿಮ್ಮ ಫೋಟೋ / ಲೋಗೋ ಸೇರಿಸಿ (Profile Photo)</label>
              <div style="display:flex; gap:8px; align-items:center; margin-top:4px;">
                <label class="kp-btn" style="background:#2563EB; color:#FFF; padding:8px 14px; font-size:13px; border-radius:10px;">
                  📸 ಫೋಟೋ ಆಯ್ಕೆ ಮಾಡಿ
                  <input type="file" id="avatarUploadInput" accept="image/*" style="display:none" onchange="handleAvatarUpload(event)">
                </label>
                <button type="button" onclick="clearAvatarPhoto()" style="background:rgba(255,255,255,0.1); color:#FCA5A5; border:1px solid rgba(248,113,113,0.3); padding:8px 12px; border-radius:10px; font-size:12.5px; font-weight:700; cursor:pointer;">🗑️ ಫೋಟೋ ತೆಗೆಯಿರಿ</button>
              </div>
            </div>
            <div>
              <label class="kp-label">🎗️ ಫೂಟರ್ ಬ್ಯಾನರ್ ವಿನ್ಯಾಸ (Banner Theme)</label>
              <select class="kp-select" id="footerThemeSelect" onchange="renderStudioCanvas()">
                <option value="royal-gold">👑 ರಾಯಲ್ ಗೋಲ್ಡ್ & ಕೆಂಪು ಪಟ್ಟಿ</option>
                <option value="dark-glass">🌑 ಮಾಡರ್ನ್ ಡಾರ್ಕ್ ಗ್ಲಾಸ್ ಪಟ್ಟಿ</option>
                <option value="white-clean">⚪ ಕ್ಲಾಸಿಕ್ ವೈಟ್ ಕಾರ್ಡ್</option>
              </select>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>

<!-- ── SECTION 3: READY-TO-USE KANNADA QUOTES & WISHES BANK ── -->
<section class="kp-section" id="quotes-bank">
  <div class="kp-sec-head">
    <div>
      <h2 class="kp-sec-title">📜 ಜನಪ್ರಿಯ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಶುಭಾಶಯಗಳು & ಕವಿ ನುಡಿಮುತ್ತುಗಳು</h2>
      <p class="kp-sec-sub">ಯಾವುದೇ ನುಡಿಮುತ್ತಿನ ಮೇಲಿರುವ <strong>"🎨 ಪೋಸ್ಟರ್‌ಗೆ ಹಾಕಿ"</strong> ಬಟನ್ ಒತ್ತಿ ತಕ್ಷಣ ಪೋಸ್ಟರ್ ರಚಿಸಿ ಅಥವಾ ಕಾಪಿ ಮಾಡಿಕೊಳ್ಳಿ.</p>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:16px;" id="quotesBankGrid"></div>
</section>

<!-- ── LIGHTBOX MODAL ── -->
<div class="kp-lightbox" id="kpLightbox" onclick="if(event.target===this) closeLightbox()">
  <div class="kp-lb-inner">
    <button class="kp-lb-close" onclick="closeLightbox()">✕</button>
    <img id="lbImage" src="" alt="Kannada Poster Preview" style="width:100%; height:auto; display:block;">
    <div style="padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:10px; background:#090D16;">
      <span id="lbTitle" style="color:#FDE047; font-weight:800; font-size:15px;"></span>
      <button class="kp-act-btn kp-act-edit" id="lbEditBtn">✏️ ಈ ಪೋಸ್ಟರ್ ಎಡಿಟ್ ಮಾಡಿ</button>
    </div>
  </div>
</div>

<!-- ── TOAST ── -->
<div class="kp-toast" id="kpToast"></div>

<script>
// ── 1. POSTER DATASET (5 UPLOADED HD POSTERS + RICH KANNADA ARTWORK TEMPLATES) ──
const POSTERS_DATA = [
  {
    id: 0,
    title: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ — ಕರ್ನಾಟಕ ಪರಂಪರೆ ಮತ್ತು ವೈಭವ",
    category: "heritage",
    badge: "🏛️ ಹಂಪಿ ರಥ & ವಿಧಾನಸೌಧ HD",
    src: "/assets/images/kannada-posters/poster-1.jpg",
    defaultHeader: "💛❤️ ನಾಡಿನ ಸಮಸ್ತ ಜನತೆಗೆ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಹಾರ್ದಿಕ ಶುಭಾಶಯಗಳು",
    defaultQuote: "ಎಲ್ಲಾದರೂ ಇರು ಎಂತಾದರೂ ಇರು\nಎಂದೆಂದಿಗೂ ನೀ ಕನ್ನಡವಾಗಿರು!",
    defaultAuthor: "— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
    defaultPos: "bottom",
    points: [
      "ಹಂಪಿಯ ಕಲ್ಲಿನ ರಥ, ವಿಧಾನಸೌಧ ಮತ್ತು ನಂದಿ ಶಿಲ್ಪದ ಭವ್ಯ ಸಂಯೋಜನೆ",
      "ಸುವರ್ಣ ಕರ್ನಾಟಕ ಭೂಪಟ ಮತ್ತು ಹಾರಾಡುವ ಹಳದಿ-ಕೆಂಪು ಕನ್ನಡ ಧ್ವಜ",
      "WhatsApp Status, Instagram Post ಹಾಗೂ ಫೇಸ್‌ಬುಕ್ ಶೇರ್‌ಗೆ ಅತ್ಯುತ್ತಮ (4:5 HD)"
    ]
  },
  {
    id: 1,
    title: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ — 3D ಸುವರ್ಣ ಅಕ್ಷರ ಮತ್ತು ಭವ್ಯ ಉತ್ಸವ",
    category: "celebration",
    badge: "🎆 3D ರಾಜ ವೈಭವ ಆವೃತ್ತಿ",
    src: "/assets/images/kannada-posters/poster-2.jpg",
    defaultHeader: "🎉 71ನೇ ಕರ್ನಾಟಕ ರಾಜ್ಯೋತ್ಸವದ ಶುಭಾಶಯಗಳು",
    defaultQuote: "ಹಚ್ಚೇವು ಕನ್ನಡದ ದೀಪ\nಕರುನಾಡ ದೀಪ ಸಿರಿನುಡಿಯ ದೀಪ!",
    defaultAuthor: "— ದ. ಎಸ್. ಕರ್ಕಿ",
    defaultPos: "bottom",
    points: [
      "ಆಕರ್ಷಕ 3D ಹಳದಿ-ಕೆಂಪು 'ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ' ಅಕ್ಷರ ವಿನ್ಯಾಸ",
      "ಶ್ರವಣಬೆಳಗೊಳದ ಬಾಹುಬಲಿ, ಹಂಪಿ ರಥ ಮತ್ತು ವಿಧಾನಸೌಧದ ಹಿನ್ನೆಲೆ",
      "ನಿಮ್ಮ ಹೆಸರು ಮತ್ತು ಫೋಟೋ ಸೇರಿಸಿ ಶೇರ್ ಮಾಡಲು ಹೇಳಿಮಾಡಿಸಿದ ವಿನ್ಯಾಸ"
    ]
  },
  {
    id: 2,
    title: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ — ಸಂಸ್ಕೃತಿ, ಮೈಸೂರು ಅರಮನೆ ಮತ್ತು ಹೂವಿನ ರಂಗೋಲಿ",
    category: "heritage",
    badge: "🌸 ಸಾಂಸ್ಕೃತಿಕ ರಾಜಮುದ್ರೆ",
    src: "/assets/images/kannada-posters/poster-3.jpg",
    defaultHeader: "🌸 ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ · ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ",
    defaultQuote: "ಕನ್ನಡ ಎನೆ ಕುಣಿದಾಡುವುದೆನ್ನೆದೆ\nಕನ್ನಡ ಎನೆ ಕಿವಿ ನಿಮಿರುವುದು!",
    defaultAuthor: "— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
    defaultPos: "bottom",
    points: [
      "ಮೈಸೂರು ಅರಮನೆ, ಹಂಪಿ ಕಲ್ಲಿನ ರಥ ಮತ್ತು ಚಿನ್ನದ ಕರ್ನಾಟಕ ನಕ್ಷೆ",
      "ಕೆಳಭಾಗದಲ್ಲಿ ಸಾಂಪ್ರದಾಯಿಕ ಕೆಂಪು-ಹಳದಿ ಹೂವಿನ ರಂಗೋಲಿ ಅಲಂಕಾರ",
      "ಶಾಲಾ-ಕಾಲೇಜು, ಕಚೇರಿ ಮತ್ತು ಸಂಘ-ಸಂಸ್ಥೆಗಳ ಶುಭಾಶಯಕ್ಕೆ ಶ್ರೇಷ್ಠ ಆಯ್ಕೆ"
    ]
  },
  {
    id: 3,
    title: "ತಾಯಿ ಭುವನೇಶ್ವರಿ — ಸುವರ್ಣ ಕರ್ನಾಟಕ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ",
    category: "bhuvaneshwari",
    badge: "👑 ತಾಯಿ ಭುವನೇಶ್ವರಿ ವಿಶೇಷ",
    src: "/assets/images/kannada-posters/poster-4.jpg",
    defaultHeader: "🙏 ಜೈ ಭುವನೇಶ್ವರಿ · ಜೈ ಕರ್ನಾಟಕ ಮಾತೆ",
    defaultQuote: "ನಮೋ ನಮೋ ಕರುನಾಡ ದೇವಿ\nಭುವನೇಶ್ವರಿ ತಾಯೇ ನಿನಗೆ ಕೋಟಿ ನಮನ!",
    defaultAuthor: "— ಕನ್ನಡಾಭಿಮಾನಿ",
    defaultPos: "top",
    points: [
      "ಕರ್ನಾಟಕದ ಭೂಪಟದೊಳಗೆ ಕಂಗೊಳಿಸುವ ನಾಡದೇವಿ ತಾಯಿ ಭುವನೇಶ್ವರಿ",
      "ಜೋಗ ಜಲಪಾತ, ಹಂಪಿ ದೇಗುಲ ಗೋಪುರಗಳು ಮತ್ತು ಸೇವಂತಿಗೆ ಹೂವಿನ ಮಾಲೆ",
      "ಭಕ್ತಿಪೂರ್ವಕ ರಾಜ್ಯೋತ್ಸವ ಶುಭಾಶಯ ಕೋರಲು ಅತಿ ಹೆಚ್ಚು ಜನಪ್ರಿಯ ಪೋಸ್ಟರ್"
    ]
  },
  {
    id: 4,
    title: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ — ಡೊಳ್ಳು ಕುಣಿತ ಮತ್ತು ಜನೋತ್ಸವ ಸಂಭ್ರಮ",
    category: "celebration",
    badge: "🥁 ಜಾನಪದ ಜನೋತ್ಸವ",
    src: "/assets/images/kannada-posters/poster-5.jpg",
    defaultHeader: "🥁 ಕರುನಾಡ ಜನತೆಗೆ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಶುಭಾಶಯಗಳು",
    defaultQuote: "ಬಾರಿಸು ಕನ್ನಡ ಡಿಂಡಿಮವ\nಓ ಕರ್ನಾಟಕ ಹೃದಯ ಶಿವ!",
    defaultAuthor: "— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
    defaultPos: "bottom",
    points: [
      "ವಿಧಾನಸೌಧದ ಮುಂದೆ ಡೊಳ್ಳು ಕುಣಿತ ಮತ್ತು ಕನ್ನಡ ಬಾವುಟಗಳ ಸಂಭ್ರಮ",
      "ಯುವಜನತೆ, ಸಾಂಸ್ಕೃತಿಕ ತಂಡಗಳು ಮತ್ತು ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್ ರೀಲ್ಸ್/ಸ್ಟೋರಿಗೆ ಸೂಕ್ತ",
      "ಗರಿಷ್ಠ ಸ್ಪಷ್ಟತೆಯ (High Contrast) ಬಣ್ಣಗಳು ಮತ್ತು ಉತ್ಸಾಹಭರಿತ ಚಿತ್ರಣ"
    ]
  }
];

// Additional procedural royal backgrounds for general Kannada quote making
const GRADIENT_THEMES = [
  { id: "grad-rajyotsava", name: "💛❤️ ಕನ್ನಡ ಧ್ವಜ ಸಿಲ್ಕ್", colors: ["#7F1D1D", "#B91C1C", "#F59E0B"] },
  { id: "grad-royal", name: "👑 ಮೈಸೂರು ರಾಯಲ್", colors: ["#090D16", "#1E1B4B", "#4C1D95"] },
  { id: "grad-emerald", name: "🌿 ಸಹ್ಯಾದ್ರಿ ಹಸಿರು", colors: ["#022C22", "#065F46", "#0D9488"] },
  { id: "grad-sunset", name: "🌅 ಹಂಪಿ ಸೂರ್ಯಾಸ್ತ", colors: ["#451A03", "#9A3412", "#D97706"] }
];

const QUOTES_LIST = [
  {
    tag: "💛❤️ ರಾಜ್ಯೋತ್ಸವ",
    header: "ನಾಡಿನ ಸಮಸ್ತ ಜನತೆಗೆ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಹಾರ್ದಿಕ ಶುಭಾಶಯಗಳು",
    quote: "ಎಲ್ಲಾದರೂ ಇರು ಎಂತಾದರೂ ಇರು\nಎಂದೆಂದಿಗೂ ನೀ ಕನ್ನಡವಾಗಿರು\nಕನ್ನಡವೇ ಸತ್ಯ, ಕನ್ನಡವೇ ನಿತ್ಯ!",
    author: "— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು"
  },
  {
    tag: "🔥 ಡಿಂಡಿಮ",
    header: "ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ · ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ",
    quote: "ಬಾರಿಸು ಕನ್ನಡ ಡಿಂಡಿಮವ\nಓ ಕರ್ನಾಟಕ ಹೃದಯ ಶಿವ\nಸತ್ತಂತಿಹರನು ಬಡಿದೆಚ್ಚರಿಸು!",
    author: "— ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು"
  },
  {
    tag: "🪔 ಕನ್ನಡದ ದೀಪ",
    header: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಶುಭಾಶಯಗಳು",
    quote: "ಹಚ್ಚೇವು ಕನ್ನಡದ ದೀಪ\nಕರುನಾಡ ದೀಪ ಸಿರಿನುಡಿಯ ದೀಪ\nಒಲವೆತ್ತಿ ತೋರುವ ದೀಪ!",
    author: "— ದ. ಎಸ್. ಕರ್ಕಿ"
  },
  {
    tag: "👑 ಅಭಿಮಾನ",
    header: "ಜೈ ಕರ್ನಾಟಕ ಮಾತೆ · ಜೈ ಭುವನೇಶ್ವರಿ",
    quote: "ಮಾನವ ಜನ್ಮ ದೊಡ್ಡದು\nಅದರಲ್ಲೂ ಕನ್ನಡಿಗನಾಗಿ ಹುಟ್ಟುವುದು\nಏಳು ಜನ್ಮದ ಪುಣ್ಯ!",
    author: "— ಕನ್ನಡ ನುಡಿಮುತ್ತು"
  },
  {
    tag: "🌸 ಬೇಂದ್ರೆ ನುಡಿ",
    header: "ಕನ್ನಡ ನಾಡು-ನುಡಿಯ ಹಬ್ಬದ ಶುಭಾಶಯಗಳು",
    quote: "ಒಂದೇ ಒಂದೇ ಕರ್ನಾಟಕ ಒಂದೇ\nಹಿಂದೆ ಮುಂದೆ ಎಂದೆಂದೂ ಒಂದೇ\nಜಗದೇಳಿಗೆಯಾಗುವುದಿದರಿಂದೇ!",
    author: "— ದ. ರಾ. ಬೇಂದ್ರೆ"
  },
  {
    tag: "📿 ಬಸವಣ್ಣ ವಚನ",
    header: "ಇಂದಿನ ಶುಭ ನುಡಿಮುತ್ತು",
    quote: "ಕಳಬೇಡ ಕೊಲಬೇಡ ಹುಸಿಯ ನುಡಿಯಲು ಬೇಡ\nಇದೇ ಅಂತರಂಗ ಶುದ್ಧಿ, ಇದೇ ಬಹಿರಂಗ ಶುದ್ಧಿ!",
    author: "— ವಿಶ್ವಗುರು ಬಸವಣ್ಣ"
  },
  {
    tag: "✨ ಡಿ.ವಿ.ಜಿ ಮಂಕುತಿಮ್ಮ",
    header: "ಜೀವನದ ನುಡಿಮುತ್ತು",
    quote: "ಹುಲ್ಲಾಗು ಬೆಟ್ಟದಡಿ, ಮನೆಗೆ ಮಲ್ಲಿಗೆಯಾಗು\nಕಲ್ಲಾಗು ಕಷ್ಟಗಳ ಮಳೆಯ ವಿಧಿ ಸುರಿಯೆ — ಮಂಕುತಿಮ್ಮ",
    author: "— ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)"
  },
  {
    tag: "🌅 ಶುಭೋದಯ",
    header: "🌅 ಶುಭೋದಯ ಕರ್ನಾಟಕ — ಶುಭ ದಿನವಾಗಲಿ",
    quote: "ಪ್ರತಿಯೊಂದು ಹೊಸ ಬೆಳಗು ಹೊಸ ಭರವಸೆಯನ್ನು ತರುತ್ತದೆ.\nನಂಬಿಕೆ ಮತ್ತು ಪರಿಶ್ರಮವಿದ್ದರೆ ಗೆಲುವು ನಿಶ್ಚಿತ!",
    author: "— ಪ್ರೇರಣಾದಾಯಕ ನುಡಿ"
  }
];

// ── 2. RENDER GALLERY CARDS ──
function renderGallery(filter = "all") {
  const grid = document.getElementById("galleryGrid");
  const items = filter === "all" ? POSTERS_DATA : POSTERS_DATA.filter(p => p.category === filter);
  grid.innerHTML = items.map(p => `
    <article class="kp-poster-card" data-category="${p.category}">
      <div class="kp-poster-img-wrap">
        <img src="${p.src}" alt="${p.title}" loading="lazy">
        <span class="kp-card-badge">${p.badge}</span>
        <button class="kp-zoom-btn" onclick="openLightbox(${p.id})" title="ಪೂರ್ಣ ಪರದೆಯಲ್ಲಿ ನೋಡಿ">🔍</button>
      </div>
      <div class="kp-poster-body">
        <h3 class="kp-poster-title">${p.title}</h3>
        <ul class="kp-poster-points">
          ${p.points.map(pt => `<li>${pt}</li>`).join("")}
        </ul>
        <div class="kp-card-actions-main">
          <button class="kp-act-btn kp-act-edit" onclick="loadPosterIntoStudio(${p.id})">
            ✏️ ಎಡಿಟ್ / ಹೆಸರು ಸೇರಿಸಿ
          </button>
          <button class="kp-act-btn kp-act-save" onclick="downloadDirectPoster(${p.id})">
            ⬇️ ಡೌನ್‌ಲೋಡ್ HD
          </button>
        </div>
        <div class="kp-share-strip">
          <span class="kp-share-label">ನೇರ ಶೇರ್:</span>
          <div class="kp-social-btns">
            <button class="kp-soc-btn kp-soc-wa" onclick="shareDirectPoster(${p.id}, 'whatsapp')" title="WhatsApp ನಲ್ಲಿ ಶೇರ್ ಮಾಡಿ">WA</button>
            <button class="kp-soc-btn kp-soc-ig" onclick="shareDirectPoster(${p.id}, 'instagram')" title="Instagram ನಲ್ಲಿ ಶೇರ್ ಮಾಡಿ">IG</button>
            <button class="kp-soc-btn kp-soc-fb" onclick="shareDirectPoster(${p.id}, 'facebook')" title="Facebook ನಲ್ಲಿ ಶೇರ್ ಮಾಡಿ">FB</button>
            <button class="kp-soc-btn kp-soc-tg" onclick="shareDirectPoster(${p.id}, 'telegram')" title="Telegram ನಲ್ಲಿ ಶೇರ್ ಮಾಡಿ">TG</button>
            <button class="kp-soc-btn kp-soc-cp" onclick="copyDirectPosterImage(${p.id})" title="ಇಮೇಜ್ ಕಾಪಿ ಮಾಡಿ (Copy Image)">📋</button>
          </div>
        </div>
      </div>
    </article>
  `).join("");
}

function filterGallery(cat, btn) {
  document.querySelectorAll(".kp-filter-chip").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  renderGallery(cat);
}

// ── 3. STUDIO CANVAS STATE & ENGINE ──
const canvas = document.getElementById("posterCanvas");
const ctx = canvas.getContext("2d");

let studioState = {
  bgType: "image", // 'image' | 'gradient' | 'custom'
  bgIndex: 0,
  gradIndex: 0,
  customBgImg: null,
  avatarImg: null,
  loadedImages: {},
  // Normalized text box center coordinates (0.0 to 1.0)
  quoteX: 0.5,
  quoteY: 0.72,
  isDragging: false,
  dragStartX: 0,
  dragStartY: 0
};

function preloadImages() {
  POSTERS_DATA.forEach((p, idx) => {
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      studioState.loadedImages[idx] = img;
      if (idx === studioState.bgIndex) renderStudioCanvas();
    };
    img.src = p.src;
  });
}

function initStudioControls() {
  // Background strip
  const strip = document.getElementById("studioBgStrip");
  let html = POSTERS_DATA.map((p, idx) => `
    <div class="kp-bg-thumb ${idx === 0 ? 'active' : ''}" id="bgThumb-img-${idx}" onclick="selectStudioBgImage(${idx})">
      <img src="${p.src}" alt="Poster ${idx+1}">
      <span class="kp-bg-thumb-label">ಪೋಸ್ಟರ್ ${idx+1}</span>
    </div>
  `).join("");

  html += GRADIENT_THEMES.map((g, idx) => `
    <div class="kp-bg-thumb" id="bgThumb-grad-${idx}" onclick="selectStudioBgGradient(${idx})" style="background:linear-gradient(135deg, ${g.colors[0]}, ${g.colors[1]}, ${g.colors[2]});">
      <span class="kp-bg-thumb-label">${g.name}</span>
    </div>
  `).join("");
  strip.innerHTML = html;

  // Quote Chips
  const qChips = document.getElementById("studioQuoteChips");
  qChips.innerHTML = QUOTES_LIST.map((q, idx) => `
    <button type="button" class="kp-quote-chip" onclick="applyPresetQuote(${idx})">${q.tag}</button>
  `).join("");

  // Quotes Bank Section
  const bankGrid = document.getElementById("quotesBankGrid");
  bankGrid.innerHTML = QUOTES_LIST.map((q, idx) => `
    <div style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; gap:12px; box-shadow:0 6px 18px rgba(15,23,42,0.04);">
      <div>
        <span style="display:inline-block; background:#FEF3C7; color:#B45309; font-size:11.5px; font-weight:800; padding:3px 10px; border-radius:999px; margin-bottom:8px;">${q.tag}</span>
        <p style="font-size:16px; font-weight:800; color:#0F172A; white-space:pre-line; line-height:1.55;">"${q.quote}"</p>
        <div style="font-size:13px; font-weight:700; color:#64748B; margin-top:6px;">${q.author}</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="kp-act-btn kp-act-edit" style="flex:1; padding:8px 12px; font-size:12.5px;" onclick="applyPresetQuote(${idx}, true)">🎨 ಪೋಸ್ಟರ್‌ಗೆ ಹಾಕಿ</button>
        <button class="kp-act-btn" style="background:#F1F5F9; color:#334155; padding:8px 12px; font-size:12.5px;" onclick="navigator.clipboard.writeText(\`${q.quote}\\n${q.author}\`); showToast('📋 ನುಡಿಮುತ್ತು ಕಾಪಿ ಆಗಿದೆ!');">📋 ಕಾಪಿ</button>
      </div>
    </div>
  `).join("");
}

function selectStudioBgImage(idx) {
  studioState.bgType = "image";
  studioState.bgIndex = idx;
  document.querySelectorAll(".kp-bg-thumb").forEach(el => el.classList.remove("active"));
  const el = document.getElementById(`bgThumb-img-${idx}`);
  if (el) el.classList.add("active");
  renderStudioCanvas();
}

function selectStudioBgGradient(idx) {
  studioState.bgType = "gradient";
  studioState.gradIndex = idx;
  document.querySelectorAll(".kp-bg-thumb").forEach(el => el.classList.remove("active"));
  const el = document.getElementById(`bgThumb-grad-${idx}`);
  if (el) el.classList.add("active");
  renderStudioCanvas();
}

function handleCustomBgUpload(e) {
  const file = e.target.files && e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const img = new Image();
    img.onload = () => {
      studioState.customBgImg = img;
      studioState.bgType = "custom";
      document.querySelectorAll(".kp-bg-thumb").forEach(el => el.classList.remove("active"));
      renderStudioCanvas();
      showToast("📷 ನಿಮ್ಮ ಹಿನ್ನೆಲೆ ಫೋಟೋ ಸೇರಿಸಲಾಗಿದೆ!");
    };
    img.src = ev.target.result;
  };
  reader.readAsDataURL(file);
}

function handleAvatarUpload(e) {
  const file = e.target.files && e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const img = new Image();
    img.onload = () => {
      studioState.avatarImg = img;
      document.getElementById("showFooterToggle").checked = true;
      renderStudioCanvas();
      showToast("🤳 ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಫೋಟೋ ಪೋಸ್ಟರ್‌ಗೆ ಸೇರಿಸಲಾಗಿದೆ!");
    };
    img.src = ev.target.result;
  };
  reader.readAsDataURL(file);
}

function clearAvatarPhoto() {
  studioState.avatarImg = null;
  document.getElementById("avatarUploadInput").value = "";
  renderStudioCanvas();
}

function loadPosterIntoStudio(posterId) {
  const p = POSTERS_DATA[posterId];
  if (!p) return;
  selectStudioBgImage(posterId);
  document.getElementById("headerTextInput").value = p.defaultHeader;
  document.getElementById("quoteTextInput").value = p.defaultQuote;
  document.getElementById("authorTextInput").value = p.defaultAuthor;
  document.getElementById("textPosPreset").value = p.defaultPos;
  applyTextPositionPreset(p.defaultPos);
  document.getElementById("poster-studio").scrollIntoView({ behavior: "smooth" });
  showToast(`🖌️ "${p.title}" ಎಡಿಟಿಂಗ್ ಸ್ಟುಡಿಯೋದಲ್ಲಿ ತೆರೆಯಲಾಗಿದೆ!`);
}

function applyPresetQuote(idx, scrollToStudio = false) {
  const q = QUOTES_LIST[idx];
  if (!q) return;
  document.getElementById("headerTextInput").value = q.header;
  document.getElementById("quoteTextInput").value = q.quote;
  document.getElementById("authorTextInput").value = q.author;
  renderStudioCanvas();
  if (scrollToStudio) {
    document.getElementById("poster-studio").scrollIntoView({ behavior: "smooth" });
  }
  showToast("✨ ನುಡಿಮುತ್ತು ಪೋಸ್ಟರ್‌ಗೆ ಅನ್ವಯಿಸಲಾಗಿದೆ!");
}

function changeCanvasAspect(ratio) {
  if (ratio === "1:1") {
    canvas.width = 1080;
    canvas.height = 1080;
  } else if (ratio === "9:16") {
    canvas.width = 1080;
    canvas.height = 1920;
  } else {
    canvas.width = 1080;
    canvas.height = 1350;
  }
  renderStudioCanvas();
}

function applyTextPositionPreset(pos) {
  if (pos === "top") {
    studioState.quoteX = 0.5;
    studioState.quoteY = 0.25;
  } else if (pos === "center") {
    studioState.quoteX = 0.5;
    studioState.quoteY = 0.50;
  } else {
    studioState.quoteX = 0.5;
    studioState.quoteY = 0.72;
  }
  renderStudioCanvas();
}

function resetStudioLayout() {
  studioState.quoteX = 0.5;
  studioState.quoteY = 0.72;
  document.getElementById("bgDimSlider").value = 10;
  document.getElementById("fontSizeSlider").value = 44;
  renderStudioCanvas();
  showToast("🔄 ಪೋಸ್ಟರ್ ವಿನ್ಯಾಸ ರೀಸೆಟ್ ಮಾಡಲಾಗಿದೆ");
}

// Helper: Draw rounded rectangle
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

// Helper: Word wrap Kannada lines cleanly
function wrapLines(ctx, text, maxWidth) {
  const rawLines = text.split("\n");
  const lines = [];
  rawLines.forEach(raw => {
    const words = raw.trim().split(/\s+/);
    if (!words.length || !words[0]) return;
    let currentLine = words[0];
    for (let i = 1; i < words.length; i++) {
      const testLine = currentLine + " " + words[i];
      if (ctx.measureText(testLine).width <= maxWidth) {
        currentLine = testLine;
      } else {
        lines.push(currentLine);
        currentLine = words[i];
      }
    }
    lines.push(currentLine);
  });
  return lines;
}

// ── CORE HIGH-DPI CANVAS RENDERER ──
function renderStudioCanvas() {
  const W = canvas.width;
  const H = canvas.height;
  ctx.clearRect(0, 0, W, H);

  // 1. Draw Background (Image Cover or Gradient)
  let bgImg = null;
  if (studioState.bgType === "custom" && studioState.customBgImg) {
    bgImg = studioState.customBgImg;
  } else if (studioState.bgType === "image") {
    bgImg = studioState.loadedImages[studioState.bgIndex];
  }

  if (bgImg) {
    const imgRatio = bgImg.width / bgImg.height;
    const canvasRatio = W / H;
    let drawW, drawH, offsetX, offsetY;
    if (imgRatio > canvasRatio) {
      drawH = H;
      drawW = H * imgRatio;
      offsetX = (W - drawW) / 2;
      offsetY = 0;
    } else {
      drawW = W;
      drawH = W / imgRatio;
      offsetX = 0;
      offsetY = (H - drawH) / 2;
    }
    ctx.drawImage(bgImg, offsetX, offsetY, drawW, drawH);
  } else {
    const gTheme = GRADIENT_THEMES[studioState.gradIndex] || GRADIENT_THEMES[0];
    const grad = ctx.createLinearGradient(0, 0, W, H);
    grad.addColorStop(0, gTheme.colors[0]);
    grad.addColorStop(0.55, gTheme.colors[1]);
    grad.addColorStop(1, gTheme.colors[2]);
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, W, H);

    // Subtle decorative mandala glow for gradient templates
    const rad = ctx.createRadialGradient(W * 0.5, H * 0.35, 30, W * 0.5, H * 0.35, W * 0.55);
    rad.addColorStop(0, "rgba(250, 204, 21, 0.22)");
    rad.addColorStop(1, "transparent");
    ctx.fillStyle = rad;
    ctx.fillRect(0, 0, W, H);
  }

  // 2. Background Dimmer Overlay
  const dimVal = parseInt(document.getElementById("bgDimSlider").value || "10", 10) / 100;
  if (dimVal > 0) {
    ctx.fillStyle = `rgba(9, 13, 22, ${dimVal})`;
    ctx.fillRect(0, 0, W, H);
  }

  // 3. Top Header Greeting Pill (if present)
  const headerText = document.getElementById("headerTextInput").value.trim();
  const fontFam = document.getElementById("fontFamilySelect").value;
  if (headerText) {
    ctx.save();
    ctx.font = `800 28px ${fontFam}`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const hLines = wrapLines(ctx, headerText, W - 140);
    const pillPadX = 34;
    const pillH = hLines.length * 38 + 24;
    let maxLineW = 0;
    hLines.forEach(l => {
      const m = ctx.measureText(l).width;
      if (m > maxLineW) maxLineW = m;
    });
    const pillW = Math.min(W - 60, maxLineW + pillPadX * 2);
    const pillX = (W - pillW) / 2;
    const pillY = 38;

    ctx.fillStyle = "rgba(9, 13, 22, 0.84)";
    roundRect(ctx, pillX, pillY, pillW, pillH, 24);
    ctx.fill();
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = "#FACC15";
    ctx.stroke();

    ctx.fillStyle = "#FDE047";
    hLines.forEach((line, idx) => {
      ctx.fillText(line, W / 2, pillY + 30 + idx * 38);
    });
    ctx.restore();
  }

  // 4. Main Quote & Author Block (Draggable!)
  const quoteText = document.getElementById("quoteTextInput").value.trim();
  const authorText = document.getElementById("authorTextInput").value.trim();
  const fontSize = parseInt(document.getElementById("fontSizeSlider").value || "44", 10);
  const textColor = document.getElementById("textColorSelect").value;
  const boxStyle = document.getElementById("textBoxStyle").value;

  if (quoteText) {
    ctx.save();
    ctx.font = `800 ${fontSize}px ${fontFam}`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    const maxTextW = W - 140;
    const lines = wrapLines(ctx, quoteText, maxTextW);
    const lineHeight = Math.round(fontSize * 1.42);
    const authorHeight = authorText ? 46 : 0;
    const totalTextH = lines.length * lineHeight + authorHeight;

    let maxW = 0;
    lines.forEach(l => {
      const w = ctx.measureText(l).width;
      if (w > maxW) maxW = w;
    });
    const boxW = Math.min(W - 64, Math.max(maxW + 84, 420));
    const boxH = totalTextH + 56;
    const centerX = W * studioState.quoteX;
    const centerY = H * studioState.quoteY;
    const boxX = Math.max(24, Math.min(W - boxW - 24, centerX - boxW / 2));
    const boxY = Math.max(24, Math.min(H - boxH - 24, centerY - boxH / 2));

    if (boxStyle === "glass-dark") {
      ctx.fillStyle = "rgba(9, 13, 22, 0.78)";
      roundRect(ctx, boxX, boxY, boxW, boxH, 28);
      ctx.fill();
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = "rgba(250, 204, 21, 0.75)";
      ctx.stroke();
    } else if (boxStyle === "royal-red") {
      const rGrad = ctx.createLinearGradient(boxX, boxY, boxX + boxW, boxY + boxH);
      rGrad.addColorStop(0, "rgba(127, 29, 29, 0.92)");
      rGrad.addColorStop(1, "rgba(69, 10, 10, 0.94)");
      ctx.fillStyle = rGrad;
      roundRect(ctx, boxX, boxY, boxW, boxH, 28);
      ctx.fill();
      ctx.lineWidth = 3;
      ctx.strokeStyle = "#FACC15";
      ctx.stroke();
    }

    // Draw quote lines with crisp shadow
    ctx.shadowColor = "rgba(0, 0, 0, 0.85)";
    ctx.shadowBlur = 12;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 3;
    ctx.fillStyle = textColor;

    const startY = boxY + 34 + lineHeight / 2;
    lines.forEach((line, i) => {
      ctx.fillText(line, boxX + boxW / 2, startY + i * lineHeight);
    });

    if (authorText) {
      ctx.font = `700 ${Math.max(24, Math.round(fontSize * 0.62))}px ${fontFam}`;
      ctx.fillStyle = "#FDE047";
      ctx.fillText(authorText, boxX + boxW / 2, startY + lines.length * lineHeight + 10);
    }
    ctx.restore();
  }

  // 5. Personal Sender Footer Bar (Name, Role & Avatar Photo)
  const showFooter = document.getElementById("showFooterToggle").checked;
  const senderName = document.getElementById("senderNameInput").value.trim();
  const senderRole = document.getElementById("senderRoleInput").value.trim();
  const footerTheme = document.getElementById("footerThemeSelect").value;

  if (showFooter && (senderName || senderRole || studioState.avatarImg)) {
    ctx.save();
    const fH = 148;
    const fY = H - fH - 22;
    const fX = 28;
    const fW = W - 56;

    if (footerTheme === "royal-gold") {
      const fGrad = ctx.createLinearGradient(fX, fY, fX + fW, fY + fH);
      fGrad.addColorStop(0, "rgba(20, 14, 8, 0.94)");
      fGrad.addColorStop(0.6, "rgba(69, 10, 10, 0.95)");
      fGrad.addColorStop(1, "rgba(120, 53, 15, 0.95)");
      ctx.fillStyle = fGrad;
      roundRect(ctx, fX, fY, fW, fH, 26);
      ctx.fill();
      ctx.lineWidth = 3.5;
      ctx.strokeStyle = "#FACC15";
      ctx.stroke();
    } else if (footerTheme === "white-clean") {
      ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
      roundRect(ctx, fX, fY, fW, fH, 26);
      ctx.fill();
      ctx.lineWidth = 3;
      ctx.strokeStyle = "#DC2626";
      ctx.stroke();
    } else {
      ctx.fillStyle = "rgba(9, 13, 22, 0.9)";
      roundRect(ctx, fX, fY, fW, fH, 26);
      ctx.fill();
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
      ctx.stroke();
    }

    let textStartX = fX + 36;
    if (studioState.avatarImg) {
      const avSize = 112;
      const avX = fX + 24;
      const avY = fY + (fH - avSize) / 2;
      ctx.save();
      ctx.beginPath();
      ctx.arc(avX + avSize / 2, avY + avSize / 2, avSize / 2, 0, Math.PI * 2);
      ctx.closePath();
      ctx.clip();
      ctx.drawImage(studioState.avatarImg, avX, avY, avSize, avSize);
      ctx.restore();

      ctx.beginPath();
      ctx.arc(avX + avSize / 2, avY + avSize / 2, avSize / 2, 0, Math.PI * 2);
      ctx.lineWidth = 4;
      ctx.strokeStyle = "#FACC15";
      ctx.stroke();
      textStartX = avX + avSize + 26;
    }

    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    const isLight = footerTheme === "white-clean";
    if (senderName) {
      ctx.font = `900 38px ${fontFam}`;
      ctx.fillStyle = isLight ? "#0F172A" : "#FDE047";
      ctx.fillText(senderName, textStartX, fY + (senderRole ? 54 : 74));
    }
    if (senderRole) {
      ctx.font = `700 26px ${fontFam}`;
      ctx.fillStyle = isLight ? "#B91C1C" : "#FFFFFF";
      ctx.fillText(senderRole, textStartX, fY + (senderName ? 100 : 74));
    }

    // Small Karnata badge on right side of footer
    ctx.textAlign = "right";
    ctx.font = `800 20px ${fontFam}`;
    ctx.fillStyle = isLight ? "#64748B" : "rgba(253, 224, 71, 0.85)";
    ctx.fillText("💛❤️ karnata.in", fX + fW - 26, fY + fH - 28);
    ctx.restore();
  }

  // 6. Decorative Kannada Flag & Royal Frame Border
  const borderStyle = document.getElementById("borderStyleSelect").value;
  if (borderStyle === "gold-red") {
    ctx.save();
    // Top Kannada flag bar (Yellow & Red)
    ctx.fillStyle = "#FACC15";
    ctx.fillRect(0, 0, W / 2, 12);
    ctx.fillStyle = "#DC2626";
    ctx.fillRect(W / 2, 0, W / 2, 12);
    // Outer frame
    ctx.strokeStyle = "rgba(250, 204, 21, 0.7)";
    ctx.lineWidth = 4;
    ctx.strokeRect(14, 14, W - 28, H - 28);
    ctx.restore();
  } else if (borderStyle === "royal-gold") {
    ctx.save();
    ctx.strokeStyle = "#FACC15";
    ctx.lineWidth = 6;
    ctx.strokeRect(16, 16, W - 32, H - 32);
    ctx.restore();
  }
}

// ── 4. DRAG-TO-MOVE QUOTE ON CANVAS (MOUSE & TOUCH) ──
function getCanvasRelativeCoords(e) {
  const rect = canvas.getBoundingClientRect();
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  return {
    x: (clientX - rect.left) / rect.width,
    y: (clientY - rect.top) / rect.height
  };
}

canvas.addEventListener("mousedown", e => {
  studioState.isDragging = true;
  const pt = getCanvasRelativeCoords(e);
  studioState.quoteX = Math.max(0.15, Math.min(0.85, pt.x));
  studioState.quoteY = Math.max(0.12, Math.min(0.85, pt.y));
  renderStudioCanvas();
});

window.addEventListener("mousemove", e => {
  if (!studioState.isDragging) return;
  const pt = getCanvasRelativeCoords(e);
  studioState.quoteX = Math.max(0.15, Math.min(0.85, pt.x));
  studioState.quoteY = Math.max(0.12, Math.min(0.85, pt.y));
  renderStudioCanvas();
});

window.addEventListener("mouseup", () => {
  studioState.isDragging = false;
});

canvas.addEventListener("touchstart", e => {
  if (e.touches.length === 1) {
    studioState.isDragging = true;
    const pt = getCanvasRelativeCoords(e);
    studioState.quoteX = Math.max(0.15, Math.min(0.85, pt.x));
    studioState.quoteY = Math.max(0.12, Math.min(0.85, pt.y));
    renderStudioCanvas();
  }
}, { passive: true });

canvas.addEventListener("touchmove", e => {
  if (!studioState.isDragging) return;
  e.preventDefault();
  const pt = getCanvasRelativeCoords(e);
  studioState.quoteX = Math.max(0.15, Math.min(0.85, pt.x));
  studioState.quoteY = Math.max(0.12, Math.min(0.85, pt.y));
  renderStudioCanvas();
}, { passive: false });

canvas.addEventListener("touchend", () => {
  studioState.isDragging = false;
});

// ── 5. ENGLISH-TO-KANNADA PHONETIC TRANSLITERATION IN STUDIO INPUTS ──
async function transliterateWordToKannada(word) {
  try {
    const url = `https://inputtools.google.com/request?text=${encodeURIComponent(word)}&itc=kn-t-i0-und&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8`;
    const res = await fetch(url);
    const data = await res.json();
    if (data && data[0] === "SUCCESS" && data[1] && data[1][0] && data[1][0][1] && data[1][0][1][0]) {
      return data[1][0][1][0];
    }
  } catch (err) {}
  return word;
}

document.querySelectorAll(".phonetic-field").forEach(field => {
  field.addEventListener("keydown", async function(e) {
    const enabled = document.getElementById("phoneticToggle").checked;
    if (!enabled) return;
    if (e.key === " " || e.key === "Enter") {
      const val = this.value;
      const selStart = this.selectionStart;
      const before = val.slice(0, selStart);
      const after = val.slice(selStart);
      const match = before.match(/([a-zA-Z]+)$/);
      if (match) {
        const engWord = match[1];
        const knWord = await transliterateWordToKannada(engWord);
        if (knWord && knWord !== engWord) {
          const newBefore = before.slice(0, before.length - engWord.length) + knWord + (e.key === " " ? " " : "\n");
          this.value = newBefore + after;
          this.selectionStart = this.selectionEnd = newBefore.length;
          e.preventDefault();
          renderStudioCanvas();
        }
      }
    }
  });
});

// ── 6. DOWNLOAD & MULTI-PLATFORM SHARE LOGIC (STUDIO & DIRECT GALLERY) ──
function downloadStudioPoster(format = "png") {
  renderStudioCanvas();
  const mime = format === "jpg" ? "image/jpeg" : "image/png";
  const dataUrl = canvas.toDataURL(mime, 0.95);
  const link = document.createElement("a");
  link.download = `kannada-poster-karnata.${format}`;
  link.href = dataUrl;
  document.body.appendChild(link);
  link.click();
  link.remove();
  showToast(`✅ HD ಕನ್ನಡ ಪೋಸ್ಟರ್ (${format.toUpperCase()}) ಡೌನ್‌ಲೋಡ್ ಆಗಿದೆ!`);
}

async function copyStudioPosterToClipboard() {
  renderStudioCanvas();
  try {
    const blob = await new Promise(resolve => canvas.toBlob(resolve, "image/png"));
    await navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]);
    showToast("📋 ಪೋಸ್ಟರ್ ಇಮೇಜ್ ಕಾಪಿ ಆಗಿದೆ! WhatsApp / Instagram / FB ಯಲ್ಲಿ Paste ಮಾಡಿ.");
  } catch (err) {
    downloadStudioPoster("png");
  }
}

async function shareStudioPoster(platform) {
  renderStudioCanvas();
  const quote = document.getElementById("quoteTextInput").value.trim() || "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವದ ಹಾರ್ದಿಕ ಶುಭಾಶಯಗಳು!";
  const shareText = `💛❤️ ${quote}\n\n🎨 ನಿಮ್ಮ ಹೆಸರಿನ ಕನ್ನಡ ಪೋಸ್ಟರ್ ರಚಿಸಿ: https://karnata.in/kannada-posters\n#KannadaRajyotsava #ಕನ್ನಡರಾಜ್ಯೋತ್ಸವ #Karnataka #Karnata`;

  try {
    const blob = await new Promise(resolve => canvas.toBlob(resolve, "image/png"));
    const file = new File([blob], "kannada-poster-karnata.png", { type: "image/png" });

    // Try native Web Share API with actual image file attachment first (works great on Android/iOS for WhatsApp, Instagram, FB, Telegram)
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      await navigator.share({
        title: "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಪೋಸ್ಟರ್ — Karnata.in",
        text: shareText,
        files: [file]
      });
      showToast("📲 ಪೋಸ್ಟರ್ ಶೇರ್ ಸಿದ್ಧವಾಗಿದೆ!");
      return;
    }
  } catch (err) {
    if (err && err.name === "AbortError") return;
  }

  // Desktop / Fallback platform-specific share + auto-copy/download image
  try {
    const blob = await new Promise(resolve => canvas.toBlob(resolve, "image/png"));
    if (navigator.clipboard && window.ClipboardItem) {
      await navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]);
    }
  } catch (e) {}

  const encodedText = encodeURIComponent(shareText);
  const encodedUrl = encodeURIComponent("https://karnata.in/kannada-posters");

  if (platform === "whatsapp") {
    window.open(`https://api.whatsapp.com/send?text=${encodedText}`, "_blank", "noopener");
    showToast("📲 ಪೋಸ್ಟರ್ ಇಮೇಜ್ ಕ್ಲಿಪ್‌ಬೋರ್ಡ್‌ಗೆ ಕಾಪಿ ಆಗಿದೆ! WhatsApp ನಲ್ಲಿ Ctrl+V ಒತ್ತಿ ಪೇಸ್ಟ್ ಮಾಡಿ.");
  } else if (platform === "facebook") {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}&quote=${encodedText}`, "_blank", "noopener");
    showToast("📘 ಪೋಸ್ಟರ್ ಕಾಪಿ ಆಗಿದೆ! Facebook ಪೋಸ್ಟ್‌ನಲ್ಲಿ Ctrl+V ಒತ್ತಿ ಪೇಸ್ಟ್ ಮಾಡಿ.");
  } else if (platform === "telegram") {
    window.open(`https://t.me/share/url?url=${encodedUrl}&text=${encodedText}`, "_blank", "noopener");
    showToast("✈️ Telegram ಶೇರ್ ತೆರೆಯಲಾಗಿದೆ (ಪೋಸ್ಟರ್ ಕ್ಲಿಪ್‌ಬೋರ್ಡ್‌ನಲ್ಲಿ ಕಾಪಿ ಆಗಿದೆ)!");
  } else if (platform === "twitter") {
    window.open(`https://twitter.com/intent/tweet?text=${encodedText}`, "_blank", "noopener");
    showToast("𝕏 ಪೋಸ್ಟರ್ ಕಾಪಿ ಆಗಿದೆ! ಟ್ವೀಟ್‌ನಲ್ಲಿ Ctrl+V ಒತ್ತಿ ಪೇಸ್ಟ್ ಮಾಡಿ.");
  } else if (platform === "instagram") {
    downloadStudioPoster("png");
    navigator.clipboard.writeText(shareText).catch(() => {});
    showToast("📸 HD ಪೋಸ್ಟರ್ ಡೌನ್‌ಲೋಡ್ ಆಗಿದೆ ಮತ್ತು ಕ್ಯಾಪ್ಷನ್ ಕಾಪಿ ಆಗಿದೆ — Instagram ನಲ್ಲಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ!");
  }
}

// Direct gallery card download & share
async function downloadDirectPoster(posterId) {
  const p = POSTERS_DATA[posterId];
  if (!p) return;
  const link = document.createElement("a");
  link.href = p.src;
  link.download = `kannada-rajyotsava-poster-${posterId + 1}.jpg`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  showToast(`⬇️ "${p.title}" ಡೌನ್‌ಲೋಡ್ ಆಗಿದೆ!`);
}

async function copyDirectPosterImage(posterId) {
  const p = POSTERS_DATA[posterId];
  if (!p) return;
  try {
    const img = studioState.loadedImages[posterId];
    const tmpCanvas = document.createElement("canvas");
    tmpCanvas.width = img.naturalWidth || 1080;
    tmpCanvas.height = img.naturalHeight || 1350;
    tmpCanvas.getContext("2d").drawImage(img, 0, 0);
    const blob = await new Promise(r => tmpCanvas.toBlob(r, "image/png"));
    await navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]);
    showToast("📋 ಪೋಸ್ಟರ್ ಇಮೇಜ್ ಕಾಪಿ ಆಗಿದೆ! WhatsApp / Instagram / FB ಯಲ್ಲಿ Paste ಮಾಡಿ.");
  } catch (e) {
    downloadDirectPoster(posterId);
  }
}

async function shareDirectPoster(posterId, platform) {
  const p = POSTERS_DATA[posterId];
  if (!p) return;
  const shareText = `💛❤️ ${p.title}\n${p.defaultQuote}\n\n🎨 HD ಕನ್ನಡ ಪೋಸ್ಟರ್‌ಗಳು ಮತ್ತು ಎಡಿಟರ್: https://karnata.in/kannada-posters`;

  try {
    const res = await fetch(p.src);
    const blob = await res.blob();
    const file = new File([blob], `kannada-poster-${posterId + 1}.jpg`, { type: "image/jpeg" });
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      await navigator.share({
        title: p.title,
        text: shareText,
        files: [file]
      });
      return;
    }
  } catch (err) {
    if (err && err.name === "AbortError") return;
  }

  await copyDirectPosterImage(posterId);
  const encText = encodeURIComponent(shareText);
  const encUrl = encodeURIComponent("https://karnata.in/kannada-posters");
  if (platform === "whatsapp") {
    window.open(`https://api.whatsapp.com/send?text=${encText}`, "_blank", "noopener");
  } else if (platform === "facebook") {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encUrl}&quote=${encText}`, "_blank", "noopener");
  } else if (platform === "telegram") {
    window.open(`https://t.me/share/url?url=${encUrl}&text=${encText}`, "_blank", "noopener");
  } else if (platform === "instagram") {
    downloadDirectPoster(posterId);
    showToast("📸 Instagram ಗಾಗಿ ಪೋಸ್ಟರ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಲಾಗಿದೆ!");
  }
}

// Lightbox
function openLightbox(posterId) {
  const p = POSTERS_DATA[posterId];
  if (!p) return;
  document.getElementById("lbImage").src = p.src;
  document.getElementById("lbTitle").textContent = p.title;
  document.getElementById("lbEditBtn").onclick = () => {
    closeLightbox();
    loadPosterIntoStudio(posterId);
  };
  document.getElementById("kpLightbox").classList.add("open");
}

function closeLightbox() {
  document.getElementById("kpLightbox").classList.remove("open");
}

// Toast
let toastTimer = null;
function showToast(msg) {
  const t = document.getElementById("kpToast");
  t.textContent = msg;
  t.style.display = "flex";
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    t.style.display = "none";
  }, 4200);
}

// Initialize
window.addEventListener("DOMContentLoaded", () => {
  renderGallery("all");
  initStudioControls();
  preloadImages();
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(() => renderStudioCanvas());
  }
});
</script>
</body>
</html>
"""

OUT_FILE.write_text(HTML, encoding="utf-8")
print(f"Successfully generated {OUT_FILE.name} ({len(HTML):,} bytes)")
