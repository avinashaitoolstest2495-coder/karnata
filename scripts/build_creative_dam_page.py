#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds a creative, hydro-telemetry Karnataka Dam Water Levels page (dam-levels.html):
- Animated SVG Liquid-Wave State Storage Sphere in Hero
- Live KPI Bento Strip (Total TMC, 90%+ Flood Alerts, Peak Inflow Dam, Total Outflow)
- 3 River Basin Interactive Summary Cards (Cauvery, Krishna, Sharavathi & Kali)
- Interactive Leaflet GPS Hydro Map of all 13 Karnataka Reservoirs with liquid-fill markers
- Basin Filter + Sort + Search Bar
- 13 Showstopper Dam Cards: High-res dam photo header + Animated SVG Liquid Tank +
  Inflow/Outflow Cusecs Flow Bar + 1D/7D TMC change badges + Trend Chart & Detail Page links
- Interactive Historical Storage Trend Chart (Chart.js) reading decrypted /data/history/dam_history.json
- Full 13-Dam Comparison Matrix (#dam-profile-tbody compatible with bake_live_data_to_html.js)
- Original Kannada Hydro Engineering Guide (TMC, Cusecs, FRL, River Basins) + FAQPage JSON-LD
"""
import html
import json
from pathlib import Path

ROOT = Path(r"C:\Users\avina\Downloads\karnata-site-with-cms")
DAM_JSON = ROOT / "data" / "dam_levels.json"
OUT_HTML = ROOT / "dam-levels.html"

DISTRICT_KN = {
    "Mandya": "ಮಂಡ್ಯ",
    "Mysuru": "ಮೈಸೂರು",
    "Hassan": "ಹಾಸನ",
    "Kodagu": "ಕೊಡಗು",
    "Vijayapura": "ವಿಜಯಪುರ",
    "Yadgir": "ಯಾದಗಿರಿ",
    "Ballari": "ಬಳ್ಳಾರಿ / ವಿಜಯನಗರ",
    "Vijayanagara": "ವಿಜಯನಗರ",
    "Chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
    "Shivamogga": "ಶಿವಮೊಗ್ಗ",
    "Chitradurga": "ಚಿತ್ರದುರ್ಗ",
    "Belagavi": "ಬೆಳಗಾವಿ",
    "Uttara Kannada": "ಉತ್ತರ ಕನ್ನಡ",
}

BASIN_META = {
    "cauvery": {"kn": "ಕಾವೇರಿ ಕೊಳ್ಳ", "en": "Cauvery Basin", "color": "#0EA5E9", "icon": "🌊"},
    "krishna": {"kn": "ಕೃಷ್ಣಾ ಕೊಳ್ಳ", "en": "Krishna Basin", "color": "#10B981", "icon": "💧"},
    "sharavathi": {"kn": "ಶರಾವತಿ & ಕಾಳಿ", "en": "Sharavathi & Kali", "color": "#8B5CF6", "icon": "⚡"},
}

DAM_FRL_FT = {
    "krs": 2450.0,
    "kabini": 2284.0,
    "hemavathi": 2922.0,
    "harangi": 2859.0,
    "almatti": 1704.7,
    "narayanapura": 1615.0,
    "tungabhadra": 1633.0,
    "bhadra": 2158.0,
    "vanivilasa": 2140.0,
    "ghataprabha": 2175.0,
    "malaprabha": 2079.5,
    "linganamakki": 1819.0,
    "supa": 1850.4,
}

DAM_PAGE_SLUG = {
    "krs": "krs-dam.html",
    "almatti": "almatti-dam.html",
    "kabini": "kabini-dam.html",
    "tungabhadra": "tungabhadra-dam.html",
    "bhadra": "bhadra-dam.html",
    "ghataprabha": "ghataprabha-dam.html",
    "malaprabha": "malaprabha-dam.html",
    "harangi": "harangi-dam.html",
    "hemavathi": "hemavathi-dam.html",
    "linganamakki": "linganamakki-dam.html",
    "narayanapura": "narayanapura-dam.html",
    "supa": "supa-dam.html",
    "vanivilasa": "vanivilasa-dam.html",
}


def fmt_num(n):
    try:
        v = int(round(float(n or 0)))
        return f"{v:,}"
    except Exception:
        return "0"


def build_ssr_table_rows(dams_dict):
    rows = []
    for key, d in dams_dict.items():
        name_kn = html.escape(d.get("name_kn") or key.upper())
        river_kn = html.escape(d.get("river_kn") or "—")
        dist_kn = html.escape(DISTRICT_KN.get(d.get("district_en", ""), d.get("district_en", "ಕರ್ನಾಟಕ")))
        pct = float(d.get("storage_pct") or 0)
        cap = float(d.get("max_storage_tmc") or d.get("design_capacity") or 0)
        stor = float(d.get("storage_tmc") or d.get("present_storage_tmc") or 0)
        lvl = float(d.get("level_ft") or 0)
        inflow = fmt_num(d.get("inflow_cusecs"))
        outflow = fmt_num(d.get("outflow_cusecs"))
        slug = DAM_PAGE_SLUG.get(key, f"{key}-dam.html")
        rows.append(
            f'          <tr data-dam-key="{key}">\n'
            f'            <td><a href="/dam-levels/{slug}" class="tbl-dam-link">{name_kn}</a><div class="tbl-sub">{river_kn} · {dist_kn}</div></td>\n'
            f'            <td class="num">{lvl:.2f} ft</td>\n'
            f'            <td class="num"><b>{stor:.2f}</b> / {cap:.2f}</td>\n'
            f'            <td class="num"><span class="tbl-pct {"high" if pct>=80 else ("mid" if pct>=45 else "low")}">{pct:.1f}%</span></td>\n'
            f'            <td class="num inflow-txt">↓ {inflow}</td>\n'
            f'            <td class="num outflow-txt">↑ {outflow}</td>\n'
            f'            <td><a href="/dam-levels/{slug}" class="tbl-go">ವಿವರ →</a></td>\n'
            f'          </tr>'
        )
    return "\n".join(rows)


def main():
    raw = json.loads(DAM_JSON.read_text(encoding="utf-8"))
    dams_dict = raw.get("dams", {})
    summary = raw.get("summary", {})
    overall_pct = float(summary.get("overall_pct") or 59.3)
    total_stor = float(summary.get("total_storage_tmc") or 514.1)
    total_cap = float(summary.get("total_capacity_tmc") or 866.3)
    updated_at = raw.get("updated_at") or raw.get("date") or "2026-11-28"

    dams_list = list(dams_dict.values())
    total_inflow = sum(float(d.get("inflow_cusecs") or 0) for d in dams_list)
    total_outflow = sum(float(d.get("outflow_cusecs") or 0) for d in dams_list)
    full_cnt = sum(1 for d in dams_list if float(d.get("storage_pct") or 0) >= 85)
    top_inflow_dam = max(dams_list, key=lambda d: float(d.get("inflow_cusecs") or 0)) if dams_list else {}
    top_inflow_name = (top_inflow_dam.get("name_kn") or "ಲಿಂಗನಮಕ್ಕಿ").split("(")[0].strip()
    top_inflow_val = fmt_num(top_inflow_dam.get("inflow_cusecs"))

    # Embedded fallback JSON (stripped of encrypted payload to keep HTML light & fast)
    embedded_data = {
        "date": raw.get("date"),
        "updated_at": updated_at,
        "summary": summary,
        "dams": dams_dict,
    }
    embedded_json = json.dumps(embedded_data, ensure_ascii=False)
    ssr_rows = build_ssr_table_rows(dams_dict)

    page_html = f'''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="geo.region" content="IN-KA">
  <meta name="geo.placename" content="Karnataka, India">
  <meta name="geo.position" content="12.9716;77.5946">
  <meta name="ICBM" content="12.9716, 77.5946">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <title>ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಇಂದು (ಲೈವ್) | Karnataka 13 Dam Water Levels Today — Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ಇಂದಿನ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ (TMC & ಅಡಿ), ಒಳಹರಿವು, ಹೊರಹರಿವು ಮತ್ತು ಐತಿಹಾಸಿಕ ಟ್ರೆಂಡ್: KRS, ಆಲಮಟ್ಟಿ, ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಭದ್ರಾ, ತುಂಗಭದ್ರಾ, ನಾರಾಯಣಪುರ, ಸೂಪ." />
  <link rel="canonical" href="https://karnata.in/dam-levels">
  <link rel="alternate" hreflang="kn-IN" href="https://karnata.in/dam-levels">
  <link rel="alternate" hreflang="en-IN" href="https://karnata.in/dam-levels">
  <link rel="alternate" hreflang="x-default" href="https://karnata.in/dam-levels">

  <meta property="og:type" content="website" />
  <meta property="og:title" content="ಕರ್ನಾಟಕ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ ಇಂದು | Karnataka Dam Water Levels — Karnata.in" />
  <meta property="og:description" content="KRS, ಆಲಮಟ್ಟಿ, ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಭದ್ರಾ, ತುಂಗಭದ್ರಾ ಸೇರಿದಂತೆ ಕರ್ನಾಟಕದ 13 ಜಲಾಶಯಗಳ ಲೈವ್ TMC ಸಂಗ್ರಹ, ಒಳಹರಿವು-ಹೊರಹರಿವು ಮತ್ತು ನಕ್ಷೆ." />
  <meta property="og:url" content="https://karnata.in/dam-levels" />
  <meta property="og:site_name" content="Karnata.in" />
  <meta property="og:image" content="https://karnata.in/assets/social-cards/dam_levels_today.png" />
  <meta name="twitter:card" content="summary_large_image" />

  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "name": "ಕರ್ನಾಟಕ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ (Karnataka Dam Water Levels Live)",
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "All",
        "url": "https://karnata.in/dam-levels",
        "description": "ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ಇಂದಿನ ಪ್ರಸ್ತುತ ನೀರಿನ ಮಟ್ಟ, TMC ಸಂಗ್ರಹ, ಒಳಹರಿವು, ಹೊರಹರಿವು, ನಕ್ಷೆ ಮತ್ತು ಐತಿಹಾಸಿಕ ಚಾರ್ಟ್."
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "1 TMC ಎಂದರೆ ಎಷ್ಟು ಲೀಟರ್ ನೀರು?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "1 TMC (Thousand Million Cubic Feet) ಎಂದರೆ 100 ಕೋಟಿ ಘನ ಅಡಿ ಅಥವಾ ಅಂದಾಜು 2,831.68 ಕೋಟಿ (28.317 ಬಿಲಿಯನ್) ಲೀಟರ್ ನೀರು."
            }}
          }},
          {{
            "@type": "Question",
            "name": "ಕರ್ನಾಟಕದ ಅತಿ ದೊಡ್ಡ ಜಲಾಶಯ ಯಾವುದು?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "ನೀರಿನ ಸಂಗ್ರಹ ಸಾಮರ್ಥ್ಯದ ಆಧಾರದಲ್ಲಿ ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು (151.75 TMC) ಮತ್ತು ಸೂಪ ಅಣೆಕಟ್ಟು (147.54 TMC) ಅತಿ ದೊಡ್ಡ ಜಲಾಶಯಗಳಾಗಿದ್ದು, ನೀರಾವರಿ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಆಲಮಟ್ಟಿ (123.08 TMC) ಮತ್ತು ತುಂಗಭದ್ರಾ (105.79 TMC) ಪ್ರಮುಖವಾಗಿವೆ."
            }}
          }},
          {{
            "@type": "Question",
            "name": "ಕ್ಯೂಸೆಕ್ಸ್ (Cusecs) ಎಂದರೆ ಏನು?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "ಕ್ಯೂಸೆಕ್ಸ್ ಎಂದರೆ ಪ್ರತಿ ಸೆಕೆಂಡಿಗೆ ಹರಿಯುವ ಘನ ಅಡಿ ನೀರು (Cubic Feet per Second). 1 ಕ್ಯೂಸೆಕ್ ಎಂದರೆ ಸೆಕೆಂಡಿಗೆ 28.317 ಲೀಟರ್ ನೀರು. 24 ಗಂಟೆಗಳ ಕಾಲ 11,574 ಕ್ಯೂಸೆಕ್ಸ್ ನೀರು ಹರಿದರೆ ಅದು 1 TMC ಆಗುತ್ತದೆ."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>

  <style>
    :root {{
      --deep: #041322;
      --ocean: #092540;
      --aqua: #0EA5E9;
      --cyan: #22D3EE;
      --emerald: #10B981;
      --amber: #F59E0B;
      --crimson: #EF4444;
      --ink: #0F172A;
      --ink2: #334155;
      --muted: #64748B;
      --surface: #F1F6FA;
      --card: #FFFFFF;
      --border: rgba(15, 23, 42, 0.08);
      --font-kn: 'Anek Kannada', sans-serif;
      --font-en: 'Plus Jakarta Sans', sans-serif;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-kn);
      background:
        radial-gradient(circle at 12% 0%, rgba(14, 165, 233, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 88% 8%, rgba(16, 185, 129, 0.07) 0%, transparent 38%),
        var(--surface);
      color: var(--ink);
      -webkit-font-smoothing: antialiased;
    }}

    /* TOPNAV */
    .topnav {{
      position: sticky; top: 0; z-index: 60;
      background: rgba(4, 19, 34, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(56, 189, 248, 0.16);
      padding: 0 20px; height: 60px;
      display: flex; align-items: center; gap: 14px;
    }}
    .back-btn {{
      display: inline-flex; align-items: center; gap: 6px;
      color: #E0F2FE; text-decoration: none; font-size: 13.5px; font-weight: 700;
      padding: 6px 12px; border-radius: 999px;
      background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12);
      transition: all 0.18s ease;
    }}
    .back-btn:hover {{ background: rgba(14,165,233,0.22); color: #fff; border-color: rgba(56,189,248,0.45); }}
    .nav-brand {{ font-size: 16px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.01em; }}
    .live-pill {{
      margin-left: auto;
      display: inline-flex; align-items: center; gap: 7px;
      background: rgba(16, 185, 129, 0.16); border: 1px solid rgba(52, 211, 153, 0.45);
      color: #6EE7B7; font-size: 11.5px; font-weight: 800;
      padding: 5px 12px; border-radius: 999px;
    }}
    .live-dot {{
      width: 8px; height: 8px; border-radius: 50%; background: #34D399;
      box-shadow: 0 0 10px #34D399; animation: pulseDot 1.4s infinite;
    }}
    @keyframes pulseDot {{ 0%,100%{{ transform:scale(1); opacity:1; }} 50%{{ transform:scale(1.45); opacity:0.5; }} }}

    /* CREATIVE HYDRO HERO */
    .hydro-hero {{
      background:
        radial-gradient(circle at 20% 20%, rgba(14, 165, 233, 0.25) 0%, transparent 45%),
        radial-gradient(circle at 82% 25%, rgba(16, 185, 129, 0.2) 0%, transparent 45%),
        linear-gradient(145deg, #03111E 0%, #07223B 50%, #0B3556 100%);
      color: #FFFFFF;
      padding: 34px 20px 104px;
      position: relative;
      overflow: hidden;
    }}
    .hero-inner {{
      max-width: 1220px; margin: 0 auto;
      display: grid; grid-template-columns: 1.25fr auto; gap: 28px; align-items: center;
      position: relative; z-index: 2;
    }}
    @media (max-width: 860px) {{
      .hero-inner {{ grid-template-columns: 1fr; text-align: center; }}
      .hero-sphere-wrap {{ margin: 0 auto; }}
      .hero-meta-row {{ justify-content: center; }}
    }}
    .hero-eyebrow {{
      display: inline-flex; align-items: center; gap: 7px;
      background: rgba(56, 189, 248, 0.14); border: 1px solid rgba(56, 189, 248, 0.35);
      color: #7DD3FC; font-size: 12px; font-weight: 800;
      padding: 5px 13px; border-radius: 999px; margin-bottom: 12px;
    }}
    .hydro-hero h1 {{
      font-size: clamp(26px, 4vw, 38px); font-weight: 800; line-height: 1.22;
      margin-bottom: 10px;
      background: linear-gradient(180deg, #FFFFFF 0%, #BAE6FD 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-sub {{
      font-size: 14.5px; color: #CBD5E1; line-height: 1.6; max-width: 660px; margin-bottom: 16px;
    }}
    .hero-meta-row {{
      display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
    }}
    .hero-chip {{
      font-size: 12px; font-weight: 700; color: #E0F2FE;
      background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.14);
      padding: 6px 12px; border-radius: 10px;
    }}
    .hero-chip.alert {{
      background: rgba(239, 68, 68, 0.2); border-color: rgba(248, 113, 113, 0.55); color: #FECACA;
    }}

    /* LIQUID SPHERE GAUGE */
    .hero-sphere-wrap {{
      position: relative; width: 196px; height: 196px; flex-shrink: 0;
    }}
    .sphere-ring {{
      position: absolute; inset: -8px; border-radius: 50%;
      border: 2px dashed rgba(56, 189, 248, 0.4);
      animation: spinSlow 28s linear infinite;
    }}
    @keyframes spinSlow {{ to {{ transform: rotate(360deg); }} }}
    .liquid-sphere {{
      width: 196px; height: 196px; border-radius: 50%;
      background: #061C31;
      border: 3px solid rgba(56, 189, 248, 0.65);
      box-shadow: 0 0 38px rgba(14, 165, 233, 0.35), inset 0 0 28px rgba(0, 0, 0, 0.55);
      position: relative; overflow: hidden;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
    }}
    .sphere-water {{
      position: absolute; left: 0; right: 0; bottom: 0;
      height: {overall_pct:.1f}%;
      background: linear-gradient(180deg, rgba(34, 211, 238, 0.85) 0%, rgba(14, 165, 233, 0.92) 55%, rgba(3, 105, 161, 0.98) 100%);
      transition: height 1.2s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .sphere-water::before, .sphere-water::after {{
      content: "";
      position: absolute; width: 200%; height: 26px; left: -50%; top: -13px;
      border-radius: 42%;
      background: rgba(186, 230, 253, 0.45);
      animation: waveSpin 5s linear infinite;
    }}
    .sphere-water::after {{
      top: -9px; background: rgba(34, 211, 238, 0.5);
      animation-duration: 7.5s; animation-direction: reverse;
    }}
    @keyframes waveSpin {{ 0%{{ transform: translateX(0) rotate(0deg); }} 100%{{ transform: translateX(25%) rotate(360deg); }} }}
    .sphere-text {{ position: relative; z-index: 3; text-align: center; text-shadow: 0 2px 10px rgba(0,0,0,0.65); }}
    .sphere-pct {{ font-family: var(--font-en); font-size: 38px; font-weight: 800; color: #FFFFFF; line-height: 1; }}
    .sphere-lbl {{ font-size: 11.5px; font-weight: 800; color: #E0F2FE; margin-top: 4px; }}
    .sphere-tmc {{ font-family: var(--font-en); font-size: 11.5px; font-weight: 700; color: #BAE6FD; margin-top: 2px; }}

    /* HERO BOTTOM WAVE */
    .hero-waves {{
      position: absolute; left: 0; right: 0; bottom: 0; height: 68px; pointer-events: none;
    }}
    .hero-waves svg {{ width: 100%; height: 100%; display: block; }}

    /* MAIN CONTAINER */
    .container {{ max-width: 1220px; margin: -52px auto 40px; padding: 0 18px; position: relative; z-index: 5; }}

    /* KPI BENTO ROW */
    .kpi-grid {{
      display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-bottom: 20px;
    }}
    @media (max-width: 900px) {{ .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 500px) {{ .kpi-grid {{ grid-template-columns: 1fr; }} }}
    .kpi-card {{
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(15, 23, 42, 0.08);
      border-radius: 18px; padding: 16px 18px;
      box-shadow: 0 10px 28px rgba(15, 23, 42, 0.07);
      position: relative; overflow: hidden;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .kpi-card:hover {{ transform: translateY(-3px); box-shadow: 0 16px 34px rgba(15, 23, 42, 0.11); }}
    .kpi-card::before {{
      content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3.5px;
      background: linear-gradient(90deg, var(--aqua), var(--cyan));
    }}
    .kpi-card.k-alert::before {{ background: linear-gradient(90deg, #EF4444, #F59E0B); }}
    .kpi-card.k-in::before {{ background: linear-gradient(90deg, #10B981, #34D399); }}
    .kpi-card.k-out::before {{ background: linear-gradient(90deg, #6366F1, #8B5CF6); }}
    .kpi-top {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }}
    .kpi-lbl {{ font-size: 12.5px; font-weight: 800; color: var(--muted); }}
    .kpi-ic {{ font-size: 20px; }}
    .kpi-val {{ font-family: var(--font-en); font-size: 24px; font-weight: 800; color: var(--ink); line-height: 1.15; }}
    .kpi-sub {{ font-size: 12px; font-weight: 700; color: var(--ink2); margin-top: 4px; }}

    /* BASIN STRIP */
    .basin-grid {{
      display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-bottom: 22px;
    }}
    @media (max-width: 780px) {{ .basin-grid {{ grid-template-columns: 1fr; }} }}
    .basin-card {{
      background: #FFFFFF; border: 1.5px solid rgba(15, 23, 42, 0.08);
      border-radius: 16px; padding: 15px 17px; cursor: pointer;
      box-shadow: 0 6px 18px rgba(15, 23, 42, 0.045);
      transition: all 0.2s ease;
    }}
    .basin-card:hover, .basin-card.active {{
      border-color: var(--aqua); transform: translateY(-2px);
      box-shadow: 0 12px 26px rgba(14, 165, 233, 0.14);
    }}
    .basin-head {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
    .basin-name {{ font-size: 15.5px; font-weight: 800; color: var(--ink); }}
    .basin-pct {{ font-family: var(--font-en); font-size: 17px; font-weight: 800; color: var(--ocean); }}
    .basin-bar {{ height: 8px; border-radius: 999px; background: #E2E8F0; overflow: hidden; margin-bottom: 7px; }}
    .basin-fill {{ height: 100%; border-radius: 999px; transition: width 0.8s ease; }}
    .basin-meta {{ font-size: 12px; color: var(--muted); font-weight: 700; display: flex; justify-content: space-between; }}

    /* SECTION CARD */
    .sec-card {{
      background: #FFFFFF; border: 1px solid rgba(15, 23, 42, 0.08);
      border-radius: 20px; padding: 20px; margin-bottom: 22px;
      box-shadow: 0 8px 26px rgba(15, 23, 42, 0.05);
    }}
    .sec-head {{
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;
      margin-bottom: 16px;
    }}
    .sec-title {{ font-size: 19px; font-weight: 800; color: var(--ink); display: flex; align-items: center; gap: 9px; }}
    .sec-sub {{ font-size: 13px; color: var(--muted); font-weight: 600; margin-top: 2px; }}

    /* MAP */
    #damHydroMap {{
      width: 100%; height: 420px; border-radius: 16px;
      border: 1.5px solid #D8E4F0; z-index: 1;
    }}
    .hydro-pin {{
      width: 44px; height: 44px; border-radius: 50%;
      background: #061C31; border: 3px solid #FFFFFF;
      box-shadow: 0 4px 14px rgba(0,0,0,0.35);
      display: flex; align-items: center; justify-content: center;
      color: #FFFFFF; font-family: var(--font-en); font-size: 11px; font-weight: 800;
      position: relative; overflow: hidden;
    }}
    .hydro-pin.flood {{ border-color: #FCA5A5; box-shadow: 0 0 0 6px rgba(239,68,68,0.28), 0 4px 14px rgba(0,0,0,0.4); }}
    .hydro-pin-fill {{ position: absolute; left: 0; right: 0; bottom: 0; opacity: 0.85; }}
    .hydro-pin span {{ position: relative; z-index: 2; text-shadow: 0 1px 4px rgba(0,0,0,0.85); }}
    .map-legend {{
      display: flex; flex-wrap: wrap; gap: 14px; margin-top: 12px; font-size: 12px; font-weight: 700; color: var(--ink2);
    }}
    .leg-dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 5px; vertical-align: middle; }}

    /* FILTER / SORT TOOLBAR */
    .toolbar {{
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;
      margin-bottom: 18px;
    }}
    .filter-pills {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .fpill {{
      border: 1.5px solid #CBD5E1; background: #FFFFFF; color: var(--ink2);
      padding: 7px 14px; border-radius: 999px; font-size: 12.5px; font-weight: 800;
      cursor: pointer; font-family: inherit; transition: all 0.16s ease;
    }}
    .fpill:hover {{ border-color: var(--aqua); color: var(--ocean); }}
    .fpill.active {{
      background: linear-gradient(135deg, #092540, #0EA5E9); color: #FFFFFF;
      border-color: transparent; box-shadow: 0 6px 16px rgba(14, 165, 233, 0.28);
    }}
    .toolbar-right {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .search-in, .sort-sel {{
      border: 1.5px solid #CBD5E1; border-radius: 11px; padding: 8px 12px;
      font-size: 13px; font-weight: 700; font-family: inherit; background: #FFFFFF; color: var(--ink);
      outline: none;
    }}
    .search-in:focus, .sort-sel:focus {{ border-color: var(--aqua); }}

    /* SHOWSTOPPER CREATIVE DAM CARDS GRID */
    .dam-cards-grid {{
      display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px;
    }}
    @media (max-width: 1020px) {{ .dam-cards-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 660px) {{ .dam-cards-grid {{ grid-template-columns: 1fr; }} }}

    .dam-tile {{
      background: #FFFFFF; border: 1px solid rgba(15, 23, 42, 0.085);
      border-radius: 20px; overflow: hidden;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.055);
      display: flex; flex-direction: column;
      transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.22s ease, border-color 0.22s ease;
    }}
    .dam-tile:hover {{
      transform: translateY(-5px);
      box-shadow: 0 18px 38px rgba(15, 23, 42, 0.12);
      border-color: rgba(14, 165, 233, 0.35);
    }}
    .dam-tile.flood-card {{ border-color: rgba(239, 68, 68, 0.45); }}

    /* Real Photo Header */
    .dt-photo {{
      position: relative; height: 144px; background: #07223B; overflow: hidden;
    }}
    .dt-photo img {{
      width: 100%; height: 100%; object-fit: cover; display: block;
      transition: transform 0.45s ease;
    }}
    .dam-tile:hover .dt-photo img {{ transform: scale(1.06); }}
    .dt-photo::after {{
      content: ""; position: absolute; inset: 0;
      background: linear-gradient(180deg, rgba(4,19,34,0.18) 0%, rgba(4,19,34,0.82) 100%);
    }}
    .dt-badges {{
      position: absolute; top: 10px; left: 10px; right: 10px; z-index: 2;
      display: flex; justify-content: space-between; align-items: center; gap: 6px;
    }}
    .dt-basin-tag {{
      background: rgba(4, 19, 34, 0.78); backdrop-filter: blur(6px);
      color: #BAE6FD; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 999px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    .dt-status-tag {{
      font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 999px;
      background: rgba(16, 185, 129, 0.9); color: #FFFFFF;
    }}
    .dt-status-tag.flood {{ background: #DC2626; animation: pulseDot 1.6s infinite; }}
    .dt-status-tag.mid {{ background: #D97706; }}
    .dt-status-tag.low {{ background: #EA580C; }}
    .dt-title-overlay {{
      position: absolute; left: 14px; right: 14px; bottom: 11px; z-index: 2;
      display: flex; justify-content: space-between; align-items: flex-end; gap: 8px;
    }}
    .dt-name {{ font-size: 17px; font-weight: 800; color: #FFFFFF; line-height: 1.25; }}
    .dt-loc {{ font-size: 11.5px; color: #CBD5E1; font-weight: 600; }}
    .dt-pct-big {{
      font-family: var(--font-en); font-size: 24px; font-weight: 800; color: #FFFFFF;
      line-height: 1; text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }}

    /* Animated Liquid Reservoir Cross-Section Tank */
    .dt-body {{ padding: 14px 15px 15px; display: flex; flex-direction: column; gap: 12px; flex: 1; }}
    .tank-wrap {{
      position: relative; height: 74px; border-radius: 13px;
      background: linear-gradient(180deg, #EFF6FF 0%, #E0F2FE 100%);
      border: 1.5px solid #BAE6FD; overflow: hidden;
    }}
    .tank-frl-line {{
      position: absolute; top: 8px; left: 0; right: 0;
      border-top: 1.5px dashed rgba(15, 23, 42, 0.25); z-index: 2;
    }}
    .tank-frl-lbl {{
      position: absolute; top: 3px; right: 8px; z-index: 3;
      font-family: var(--font-en); font-size: 9.5px; font-weight: 800; color: #475569;
      background: rgba(255,255,255,0.75); padding: 1px 6px; border-radius: 999px;
    }}
    .tank-water {{
      position: absolute; left: 0; right: 0; bottom: 0;
      transition: height 1s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .tank-wave-svg {{
      position: absolute; left: 0; top: -11px; width: 200%; height: 14px;
      animation: tankWaveSlide 5s linear infinite;
    }}
    @keyframes tankWaveSlide {{ 0%{{ transform: translateX(0); }} 100%{{ transform: translateX(-50%); }} }}
    .tank-overlay {{
      position: relative; z-index: 3; height: 100%;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 13px;
    }}
    .tank-tmc {{
      font-family: var(--font-en); font-size: 16px; font-weight: 800; color: #0F172A;
      background: rgba(255, 255, 255, 0.84); backdrop-filter: blur(4px);
      padding: 4px 10px; border-radius: 9px;
    }}
    .tank-lvl {{
      font-family: var(--font-en); font-size: 12px; font-weight: 800; color: #0F172A;
      background: rgba(255, 255, 255, 0.84); padding: 4px 9px; border-radius: 9px;
    }}

    /* Inflow vs Outflow Hydro Strip */
    .flow-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }}
    .flow-box {{
      border-radius: 12px; padding: 9px 11px;
      border: 1px solid rgba(15, 23, 42, 0.07);
    }}
    .flow-box.inflow {{ background: #ECFDF5; border-color: #A7F3D0; }}
    .flow-box.outflow {{ background: #FFF7ED; border-color: #FED7AA; }}
    .flow-lbl {{ font-size: 11px; font-weight: 800; color: var(--ink2); }}
    .flow-val {{ font-family: var(--font-en); font-size: 15.5px; font-weight: 800; margin-top: 2px; }}
    .flow-box.inflow .flow-val {{ color: #047857; }}
    .flow-box.outflow .flow-val {{ color: #C2410C; }}

    .dt-deltas {{
      display: flex; align-items: center; justify-content: space-between; gap: 6px; flex-wrap: wrap;
      font-size: 11.5px; font-weight: 700; color: var(--muted);
    }}
    .delta-pill {{
      padding: 3px 8px; border-radius: 999px; font-family: var(--font-en); font-size: 11px; font-weight: 800;
    }}
    .delta-pill.up {{ background: #DCFCE7; color: #15803D; }}
    .delta-pill.down {{ background: #FEE2E2; color: #B91C1C; }}
    .delta-pill.flat {{ background: #F1F5F9; color: #475569; }}

    .dt-actions {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: auto; padding-top: 4px;
    }}
    .dt-btn {{
      text-align: center; text-decoration: none; border: none; cursor: pointer;
      padding: 9px 10px; border-radius: 11px; font-size: 12.5px; font-weight: 800; font-family: inherit;
      transition: all 0.16s ease;
    }}
    .dt-btn-chart {{ background: #EFF6FF; color: #0369A1; border: 1px solid #BAE6FD; }}
    .dt-btn-chart:hover {{ background: #0284C7; color: #FFFFFF; }}
    .dt-btn-detail {{ background: #092540; color: #FFFFFF; }}
    .dt-btn-detail:hover {{ background: #0EA5E9; }}

    /* CHART SECTION */
    .chart-controls {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
    .tf-btn {{
      border: 1px solid #CBD5E1; background: #F8FAFC; color: var(--ink2);
      padding: 6px 12px; border-radius: 9px; font-size: 12px; font-weight: 800; cursor: pointer;
    }}
    .tf-btn.active {{ background: #092540; color: #FFFFFF; border-color: #092540; }}
    .chart-canvas-wrap {{ position: relative; height: 290px; width: 100%; }}

    /* TABLE */
    .table-wrap {{ overflow-x: auto; }}
    table.dam-table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
    table.dam-table th {{
      text-align: left; padding: 11px 12px; background: #F1F5F9; color: var(--ink2);
      font-size: 12px; font-weight: 800; border-bottom: 1.5px solid #CBD5E1; white-space: nowrap;
    }}
    table.dam-table td {{ padding: 11px 12px; border-bottom: 1px solid #E2E8F0; vertical-align: middle; }}
    table.dam-table tr:hover {{ background: #F8FAFC; }}
    .tbl-dam-link {{ font-weight: 800; color: var(--ocean); text-decoration: none; }}
    .tbl-dam-link:hover {{ color: var(--aqua); text-decoration: underline; }}
    .tbl-sub {{ font-size: 11.5px; color: var(--muted); font-weight: 600; }}
    .num {{ font-family: var(--font-en); font-variant-numeric: tabular-nums; white-space: nowrap; }}
    .tbl-pct {{ padding: 3px 9px; border-radius: 999px; font-weight: 800; font-size: 12px; }}
    .tbl-pct.high {{ background: #DCFCE7; color: #15803D; }}
    .tbl-pct.mid {{ background: #E0F2FE; color: #0369A1; }}
    .tbl-pct.low {{ background: #FEF3C7; color: #B45309; }}
    .inflow-txt {{ color: #047857; font-weight: 800; }}
    .outflow-txt {{ color: #C2410C; font-weight: 800; }}
    .tbl-go {{ font-size: 12px; font-weight: 800; color: #0284C7; text-decoration: none; white-space: nowrap; }}

    /* EDITORIAL GUIDE */
    .guide-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 14px; }}
    @media (max-width: 800px) {{ .guide-grid {{ grid-template-columns: 1fr; }} }}
    .guide-box {{
      background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 15px; padding: 16px;
    }}
    .guide-box h3 {{ font-size: 15.5px; font-weight: 800; color: var(--ocean); margin-bottom: 7px; }}
    .guide-box p {{ font-size: 13.5px; color: var(--ink2); line-height: 1.65; }}
    .disclaimer-note {{
      margin-top: 16px; padding: 12px 15px; border-radius: 12px;
      background: #FFFBEB; border: 1px solid #FDE68A; color: #92400E;
      font-size: 12.5px; line-height: 1.55; font-weight: 600;
    }}
  </style>
</head>
<body>

<nav class="topnav">
  <a href="/" class="back-btn">← ಮುಖಪುಟ</a>
  <div class="nav-brand">💧 ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳು — Karnata.in</div>
  <div class="live-pill"><span class="live-dot"></span> ಲೈವ್ ಟೆಲಿಮೆಟ್ರಿ</div>
</nav>

<header class="hydro-hero">
  <div class="hero-inner">
    <div>
      <div class="hero-eyebrow">🌊 Karnataka Hydro-Telemetry · 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳು</div>
      <h1>ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ</h1>
      <p class="hero-sub">
        ಕಾವೇರಿ, ಕೃಷ್ಣಾ ಹಾಗೂ ಶರಾವತಿ-ಕಾಳಿ ಕೊಳ್ಳಗಳ 13 ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ಇಂದಿನ ನೈಜ ಸಮಯದ TMC ಸಂಗ್ರಹ, ಅಡಿ ಮಟ್ಟ, ಒಳಹರಿವು–ಹೊರಹರಿವು ಕ್ಯೂಸೆಕ್ಸ್, ಜಿಪಿಎಸ್ ನಕ್ಷೆ ಮತ್ತು ಐತಿಹಾಸಿಕ ಟ್ರೆಂಡ್.
      </p>
      <div class="hero-meta-row">
        <span class="hero-chip" id="heroDateChip">🕒 ನವೀಕರಣ: {html.escape(str(updated_at)[:16].replace('T', ' '))}</span>
        <span class="hero-chip">📊 ಮೂಲ: Karnataka WRD / KSNDMC</span>
        <span class="hero-chip alert" id="heroAlertChip">🚨 85%+ ಭರ್ತಿ: {full_cnt} ಜಲಾಶಯಗಳು</span>
      </div>
    </div>

    <div class="hero-sphere-wrap" title="ರಾಜ್ಯದ ಒಟ್ಟು 13 ಜಲಾಶಯಗಳ ಸಂಗ್ರಹ ಶೇಕಡಾವಾರು">
      <div class="sphere-ring"></div>
      <div class="liquid-sphere">
        <div class="sphere-water" id="heroSphereWater" style="height:{overall_pct:.1f}%;"></div>
        <div class="sphere-text">
          <div class="sphere-pct" id="heroSpherePct">{overall_pct:.1f}%</div>
          <div class="sphere-lbl">ರಾಜ್ಯದ ಒಟ್ಟು ಸಂಗ್ರಹ</div>
          <div class="sphere-tmc" id="heroSphereTmc">{total_stor:.1f} / {total_cap:.1f} TMC</div>
        </div>
      </div>
    </div>
  </div>

  <div class="hero-waves">
    <svg viewBox="0 0 1440 70" preserveAspectRatio="none">
      <path fill="rgba(241,246,250,0.35)" d="M0,36 C240,68 480,4 720,36 C960,68 1200,10 1440,38 L1440,70 L0,70 Z"></path>
      <path fill="#F1F6FA" d="M0,48 C300,12 600,72 900,36 C1140,8 1320,44 1440,34 L1440,70 L0,70 Z"></path>
    </svg>
  </div>
</header>

<main class="container">

  <!-- LIVE KPI BENTO -->
  <section class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-top"><span class="kpi-lbl">ಒಟ್ಟು ನೀರಿನ ಸಂಗ್ರಹ</span><span class="kpi-ic">💧</span></div>
      <div class="kpi-val" id="kpiTotalTmc">{total_stor:.1f} TMC</div>
      <div class="kpi-sub" id="kpiTotalCap">ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ: {total_cap:.1f} TMC ({overall_pct:.1f}%)</div>
    </div>
    <div class="kpi-card k-in">
      <div class="kpi-top"><span class="kpi-lbl">ಗರಿಷ್ಠ ಒಳಹರಿವು (Peak Inflow)</span><span class="kpi-ic">🌊</span></div>
      <div class="kpi-val" id="kpiPeakInflow">{top_inflow_val} cfs</div>
      <div class="kpi-sub" id="kpiPeakInflowDam">📍 {html.escape(top_inflow_name)} · ಒಟ್ಟು: {fmt_num(total_inflow)} cfs</div>
    </div>
    <div class="kpi-card k-out">
      <div class="kpi-top"><span class="kpi-lbl">ಒಟ್ಟು ಹೊರಹರಿವು (Outflow)</span><span class="kpi-ic">🚰</span></div>
      <div class="kpi-val" id="kpiTotalOutflow">{fmt_num(total_outflow)} cfs</div>
      <div class="kpi-sub">ಎಲ್ಲಾ 13 ಜಲಾಶಯಗಳಿಂದ ನದಿಗೆ/ಕಾಲುವೆಗೆ</div>
    </div>
    <div class="kpi-card k-alert">
      <div class="kpi-top"><span class="kpi-lbl">ತುಂಬಿರುವ / ಎಚ್ಚರಿಕೆ ಡ್ಯಾಂಗಳು</span><span class="kpi-ic">🚨</span></div>
      <div class="kpi-val" id="kpiFullCount">{full_cnt} / 13</div>
      <div class="kpi-sub" id="kpiFloodNames">85%+ ನೀರಿನ ಮಟ್ಟ ಹೊಂದಿರುವವು</div>
    </div>
  </section>

  <!-- 3 RIVER BASIN SUMMARY STRIP -->
  <section class="basin-grid" id="basinSummaryGrid"></section>

  <!-- INTERACTIVE KARNATAKA HYDRO MAP -->
  <section class="sec-card">
    <div class="sec-head">
      <div>
        <h2 class="sec-title">🗺️ ಕರ್ನಾಟಕ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ಜಿಪಿಎಸ್ ನಕ್ಷೆ</h2>
        <div class="sec-sub">ಯಾವುದೇ ಜಲಾಶಯದ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ ಲೈವ್ TMC, ಒಳಹರಿವು, ಹೊರಹರಿವು ಮತ್ತು ಪೂರ್ಣ ವಿವರ ನೋಡಿ</div>
      </div>
    </div>
    <div id="damHydroMap"></div>
    <div class="map-legend">
      <span><span class="leg-dot" style="background:#DC2626;"></span>90%+ ತುಂಬಿದೆ / ಪ್ರವಾಹ ಎಚ್ಚರಿಕೆ</span>
      <span><span class="leg-dot" style="background:#10B981;"></span>70%–89% ಉತ್ತಮ ಸಂಗ್ರಹ</span>
      <span><span class="leg-dot" style="background:#0EA5E9;"></span>45%–69% ಮಧ್ಯಮ</span>
      <span><span class="leg-dot" style="background:#F59E0B;"></span>45% ಕ್ಕಿಂತ ಕಡಿಮೆ</span>
    </div>
  </section>

  <!-- FILTER / SORT & CREATIVE DAM CARDS -->
  <section class="sec-card">
    <div class="sec-head">
      <div>
        <h2 class="sec-title">🏞️ ಎಲ್ಲಾ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಟ್ಯಾಂಕ್ ಸ್ಥಿತಿ</h2>
        <div class="sec-sub">ಪ್ರತಿ ಜಲಾಶಯದ ನೈಜ ನೀರಿನ ಮಟ್ಟ, ಒಳಹರಿವು–ಹೊರಹರಿವು ಮತ್ತು 7 ದಿನದ ಬದಲಾವಣೆ</div>
      </div>
    </div>

    <div class="toolbar">
      <div class="filter-pills">
        <button class="fpill active" data-basin="all" onclick="setBasinFilter('all', this)">ಎಲ್ಲಾ (13)</button>
        <button class="fpill" data-basin="cauvery" onclick="setBasinFilter('cauvery', this)">🌊 ಕಾವೇರಿ ಕೊಳ್ಳ</button>
        <button class="fpill" data-basin="krishna" onclick="setBasinFilter('krishna', this)">💧 ಕೃಷ್ಣಾ ಕೊಳ್ಳ</button>
        <button class="fpill" data-basin="sharavathi" onclick="setBasinFilter('sharavathi', this)">⚡ ಶರಾವತಿ &amp; ಕಾಳಿ</button>
        <button class="fpill" data-basin="alert" onclick="setBasinFilter('alert', this)">🚨 85%+ ಭರ್ತಿ</button>
      </div>
      <div class="toolbar-right">
        <input type="text" id="damSearch" class="search-in" placeholder="🔍 ಡ್ಯಾಂ ಅಥವಾ ನದಿ ಹುಡುಕಿ..." oninput="renderDamCards()">
        <select id="damSort" class="sort-sel" onchange="renderDamCards()">
          <option value="pct_desc">ಗರಿಷ್ಠ ಶೇಕಡಾವಾರು (%)</option>
          <option value="tmc_desc">ಗರಿಷ್ಠ ಸಂಗ್ರಹ (TMC)</option>
          <option value="inflow_desc">ಗರಿಷ್ಠ ಒಳಹರಿವು (Cusecs)</option>
          <option value="pct_asc">ಕಡಿಮೆ ನೀರು (%)</option>
        </select>
      </div>
    </div>

    <div class="dam-cards-grid" id="dam-cards-grid"></div>
  </section>

  <!-- HISTORICAL STORAGE TREND CHART -->
  <section class="sec-card" id="trendChartSection">
    <div class="sec-head">
      <div>
        <h2 class="sec-title">📈 ಜಲಾಶಯದ ಐತಿಹಾಸಿಕ ನೀರಿನ ಸಂಗ್ರಹ ಟ್ರೆಂಡ್ (TMC Chart)</h2>
        <div class="sec-sub" id="chartSubTitle">ಯಾವುದೇ ಜಲಾಶಯವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ದಿನನಿತ್ಯದ ನೀರಿನ ಮಟ್ಟದ ಏರಿಳಿತ ವೀಕ್ಷಿಸಿ</div>
      </div>
      <div class="chart-controls">
        <select id="chartDamSelect" class="sort-sel" onchange="renderTrendChart()"></select>
        <button class="tf-btn" data-days="7" onclick="setChartDays(7, this)">7D</button>
        <button class="tf-btn active" data-days="30" onclick="setChartDays(30, this)">30D</button>
        <button class="tf-btn" data-days="90" onclick="setChartDays(90, this)">90D</button>
        <button class="tf-btn" data-days="365" onclick="setChartDays(365, this)">All</button>
      </div>
    </div>
    <div class="chart-canvas-wrap">
      <canvas id="damTrendChart"></canvas>
    </div>
  </section>

  <!-- FULL TECHNICAL COMPARISON TABLE (Compatible with bake_live_data_to_html.js) -->
  <section class="sec-card">
    <div class="sec-head">
      <div>
        <h2 class="sec-title">📋 13 ಜಲಾಶಯಗಳ ಸಮಗ್ರ ತುಲನಾತ್ಮಕ ಪಟ್ಟಿ</h2>
        <div class="sec-sub">ಅಡಿ ಮಟ್ಟ, ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ (TMC), ಲೈವ್ ಸಂಗ್ರಹ, ಒಳಹರಿವು &amp; ಹೊರಹರಿವು</div>
      </div>
    </div>
    <div class="table-wrap">
      <table class="dam-table">
        <thead>
          <tr>
            <th>ಜಲಾಶಯ / ನದಿ</th>
            <th>ನೀರಿನ ಮಟ್ಟ</th>
            <th>ಸಂಗ್ರಹ / ಸಾಮರ್ಥ್ಯ (TMC)</th>
            <th>ಭರ್ತಿ %</th>
            <th>ಒಳಹರಿವು (cfs)</th>
            <th>ಹೊರಹರಿವು (cfs)</th>
            <th>ವಿವರ</th>
          </tr>
        </thead>
        <tbody id="dam-profile-tbody">
{ssr_rows}
        </tbody>
      </table>
    </div>
  </section>

  <!-- ORIGINAL KANNADA HYDRO GUIDE -->
  <section class="sec-card">
    <h2 class="sec-title">📚 ಜಲಾಶಯದ ಅಳತೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ (TMC, Cusecs &amp; FRL)</h2>
    <div class="guide-grid">
      <div class="guide-box">
        <h3>💧 1 TMC ಎಂದರೆ ಎಷ್ಟು ನೀರು?</h3>
        <p>TMC ಎಂದರೆ <b>Thousand Million Cubic Feet</b> (100 ಕೋಟಿ ಘನ ಅಡಿ). 1 TMC ನೀರು ಅಂದಾಜು <b>2,831.68 ಕೋಟಿ ಲೀಟರ್</b> ನೀರಿಗೆ ಸಮನಾಗಿರುತ್ತದೆ. ಬೆಂಗಳೂರಿನಂತಹ ಮಹಾನಗರಕ್ಕೆ ತಿಂಗಳಿಗೆ ಸುಮಾರು 1.5–1.8 TMC ಕುಡಿಯುವ ನೀರು ಅಗತ್ಯವಿರುತ್ತದೆ.</p>
      </div>
      <div class="guide-box">
        <h3>🌊 ಕ್ಯೂಸೆಕ್ಸ್ (Cusecs) ಲೆಕ್ಕಾಚಾರ</h3>
        <p>ಒಳಹರಿವು (Inflow) ಮತ್ತು ಹೊರಹರಿವನ್ನು (Outflow) <b>Cusecs</b> (Cubic Feet per Second) ನಲ್ಲಿ ಅಳೆಯಲಾಗುತ್ತದೆ. 1 ಕ್ಯೂಸೆಕ್ ಎಂದರೆ ಪ್ರತಿ ಸೆಕೆಂಡಿಗೆ 28.317 ಲೀಟರ್ ನೀರಿನ ಹರಿವು. <b>11,574 ಕ್ಯೂಸೆಕ್ಸ್</b> ನೀರು 24 ಗಂಟೆ ನಿರಂತರ ಹರಿದರೆ 1 TMC ಸಂಗ್ರಹವಾಗುತ್ತದೆ.</p>
      </div>
      <div class="guide-box">
        <h3>📏 FRL ಮತ್ತು ಲೈವ್ ಸ್ಟೋರೇಜ್</h3>
        <p><b>FRL (Full Reservoir Level)</b> ಎಂದರೆ ಅಣೆಕಟ್ಟಿನ ಗರಿಷ್ಠ ಸುರಕ್ಷಿತ ನೀರಿನ ಮಟ್ಟ. ಒಟ್ಟು ಸಂಗ್ರಹದಲ್ಲಿ (Gross Storage) ಕಾಲುವೆ ಹಾಗೂ ವಿದ್ಯುತ್ ಉತ್ಪಾದನೆಗೆ ಬಳಸಬಹುದಾದ ನೀರನ್ನು <b>Live Storage</b> ಎನ್ನುತ್ತಾರೆ; ಅದರ ಕೆಳಗಿನದನ್ನು Dead Storage ಎನ್ನುತ್ತಾರೆ.</p>
      </div>
    </div>
    <div class="disclaimer-note">
      ℹ️ <b>ಮಾಹಿತಿ ಸೂಚನೆ:</b> Karnata.in ಒಂದು ಸ್ವತಂತ್ರ ನಾಗರಿಕ ಮಾಹಿತಿ ವೇದಿಕೆಯಾಗಿದ್ದು, ಯಾವುದೇ ಸರ್ಕಾರಿ ಇಲಾಖೆಯ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಅಲ್ಲ. ಇಲ್ಲಿನ ಜಲಾಶಯಗಳ ಅಂಕಿಅಂಶಗಳನ್ನು ಕರ್ನಾಟಕ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ (WRD) ಮತ್ತು KSNDMC ಸಾರ್ವಜನಿಕ ಬುಲೆಟಿನ್‌ಗಳಿಂದ ನಿಯಮಿತವಾಗಿ ಸಂಗ್ರಹಿಸಿ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ.
    </div>
  </section>

</main>

<script src="/footer-component.js" defer></script>

<script>
  const SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA";
  const DISTRICT_KN = {json.dumps(DISTRICT_KN, ensure_ascii=False)};
  const BASIN_META = {json.dumps(BASIN_META, ensure_ascii=False)};
  const DAM_FRL_FT = {json.dumps(DAM_FRL_FT, ensure_ascii=False)};
  const DAM_PAGE_SLUG = {json.dumps(DAM_PAGE_SLUG, ensure_ascii=False)};

  let LIVE_DAM_DATA = {embedded_json};
  let HISTORY_DATA = null;
  let currentBasin = 'all';
  let currentChartDays = 30;
  let damMap = null;
  let damMapLayer = null;
  let trendChartInstance = null;

  function decryptPayload(encodedStr) {{
    if (!encodedStr || typeof encodedStr !== 'string') return null;
    try {{
      const binaryStr = atob(encodedStr);
      const bytes = new Uint8Array(binaryStr.length);
      for (let i = 0; i < binaryStr.length; i++) {{
        bytes[i] = binaryStr.charCodeAt(i) ^ SECRET_KEY.charCodeAt(i % SECRET_KEY.length);
      }}
      return JSON.parse(new TextDecoder().decode(bytes));
    }} catch (e) {{
      return null;
    }}
  }}

  function fmtNum(v) {{
    const n = Math.round(Number(v || 0));
    return isNaN(n) ? '0' : n.toLocaleString('en-IN');
  }}

  function getWaterColor(pct) {{
    if (pct >= 90) return {{ fill: 'linear-gradient(180deg,#F87171 0%,#DC2626 100%)', solid: '#DC2626', wave: '#FCA5A5', badge: 'flood', label: '🚨 ತುಂಬಿದೆ / ಎಚ್ಚರಿಕೆ' }};
    if (pct >= 70) return {{ fill: 'linear-gradient(180deg,#34D399 0%,#059669 100%)', solid: '#10B981', wave: '#6EE7B7', badge: 'good', label: '🟢 ಉತ್ತಮ ಸಂಗ್ರಹ' }};
    if (pct >= 45) return {{ fill: 'linear-gradient(180deg,#38BDF8 0%,#0284C7 100%)', solid: '#0EA5E9', wave: '#7DD3FC', badge: 'mid', label: '🔵 ಮಧ್ಯಮ' }};
    return {{ fill: 'linear-gradient(180deg,#FBBF24 0%,#D97706 100%)', solid: '#F59E0B', wave: '#FDE68A', badge: 'low', label: '🟠 ಕಡಿಮೆ' }};
  }}

  function getDamsArray() {{
    const d = LIVE_DAM_DATA?.dams || {{}};
    return Object.entries(d).map(([k, v]) => ({{ ...v, _key: v.key || v.id || k }}));
  }}

  function renderHeroAndKpis() {{
    const arr = getDamsArray();
    const totalStor = arr.reduce((s, d) => s + Number(d.storage_tmc || d.present_storage_tmc || 0), 0);
    const totalCap = arr.reduce((s, d) => s + Number(d.max_storage_tmc || d.design_capacity || 0), 0);
    const pct = totalCap > 0 ? (totalStor / totalCap) * 100 : 0;
    const totalIn = arr.reduce((s, d) => s + Number(d.inflow_cusecs || 0), 0);
    const totalOut = arr.reduce((s, d) => s + Number(d.outflow_cusecs || 0), 0);
    const fullList = arr.filter(d => Number(d.storage_pct || 0) >= 85);
    const peakDam = arr.slice().sort((a, b) => Number(b.inflow_cusecs || 0) - Number(a.inflow_cusecs || 0))[0];

    const set = (id, v) => {{ const e = document.getElementById(id); if (e) e.textContent = v; }};
    set('heroSpherePct', `${{pct.toFixed(1)}}%`);
    set('heroSphereTmc', `${{totalStor.toFixed(1)}} / ${{totalCap.toFixed(1)}} TMC`);
    const sw = document.getElementById('heroSphereWater');
    if (sw) sw.style.height = `${{Math.min(100, Math.max(8, pct)).toFixed(1)}}%`;

    set('kpiTotalTmc', `${{totalStor.toFixed(1)}} TMC`);
    set('kpiTotalCap', `ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ: ${{totalCap.toFixed(1)}} TMC (${{pct.toFixed(1)}}%)`);
    set('kpiPeakInflow', `${{fmtNum(peakDam?.inflow_cusecs)}} cfs`);
    set('kpiPeakInflowDam', `📍 ${{(peakDam?.name_kn || '').split('(')[0].trim()}} · ಒಟ್ಟು: ${{fmtNum(totalIn)}} cfs`);
    set('kpiTotalOutflow', `${{fmtNum(totalOut)}} cfs`);
    set('kpiFullCount', `${{fullList.length}} / ${{arr.length}}`);
    set('kpiFloodNames', fullList.length ? fullList.map(x => x.name_kn.split('(')[0].trim()).join(', ') : 'ಯಾವುದೇ ಪ್ರವಾಹ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ');
    set('heroAlertChip', `🚨 85%+ ಭರ್ತಿ: ${{fullList.length}} ಜಲಾಶಯಗಳು`);
    if (LIVE_DAM_DATA?.updated_at) {{
      set('heroDateChip', `🕒 ನವೀಕರಣ: ${{String(LIVE_DAM_DATA.updated_at).slice(0, 16).replace('T', ' ')}}`);
    }}
  }}

  function renderBasinCards() {{
    const container = document.getElementById('basinSummaryGrid');
    if (!container) return;
    const arr = getDamsArray();
    container.innerHTML = Object.entries(BASIN_META).map(([bKey, meta]) => {{
      const list = arr.filter(d => d.basin === bKey);
      const stor = list.reduce((s, d) => s + Number(d.storage_tmc || 0), 0);
      const cap = list.reduce((s, d) => s + Number(d.max_storage_tmc || d.design_capacity || 0), 0);
      const pct = cap > 0 ? (stor / cap) * 100 : 0;
      const inflow = list.reduce((s, d) => s + Number(d.inflow_cusecs || 0), 0);
      return `
        <div class="basin-card ${{currentBasin === bKey ? 'active' : ''}}" onclick="setBasinFilter('${{bKey}}')">
          <div class="basin-head">
            <span class="basin-name">${{meta.icon}} ${{meta.kn}} (${{list.length}})</span>
            <span class="basin-pct" style="color:${{meta.color}};">${{pct.toFixed(1)}}%</span>
          </div>
          <div class="basin-bar"><div class="basin-fill" style="width:${{pct.toFixed(1)}}%; background:${{meta.color}};"></div></div>
          <div class="basin-meta">
            <span>${{stor.toFixed(1)}} / ${{cap.toFixed(1)}} TMC</span>
            <span>↓ ${{fmtNum(inflow)}} cfs</span>
          </div>
        </div>
      `;
    }}).join('');
  }}

  function setBasinFilter(basin, btn) {{
    currentBasin = basin;
    document.querySelectorAll('.fpill').forEach(p => p.classList.toggle('active', p.dataset.basin === basin));
    renderBasinCards();
    renderDamCards();
  }}

  function renderDamCards() {{
    const grid = document.getElementById('dam-cards-grid');
    if (!grid) return;
    const q = (document.getElementById('damSearch')?.value || '').toLowerCase().trim();
    const sortBy = document.getElementById('damSort')?.value || 'pct_desc';

    let arr = getDamsArray();
    if (currentBasin === 'alert') {{
      arr = arr.filter(d => Number(d.storage_pct || 0) >= 85);
    }} else if (currentBasin !== 'all') {{
      arr = arr.filter(d => d.basin === currentBasin);
    }}

    if (q) {{
      arr = arr.filter(d =>
        (d.name_kn || '').toLowerCase().includes(q) ||
        (d.name_en || '').toLowerCase().includes(q) ||
        (d.river_kn || '').toLowerCase().includes(q) ||
        (d.district_en || '').toLowerCase().includes(q)
      );
    }}

    arr.sort((a, b) => {{
      if (sortBy === 'tmc_desc') return Number(b.storage_tmc || 0) - Number(a.storage_tmc || 0);
      if (sortBy === 'inflow_desc') return Number(b.inflow_cusecs || 0) - Number(a.inflow_cusecs || 0);
      if (sortBy === 'pct_asc') return Number(a.storage_pct || 0) - Number(b.storage_pct || 0);
      return Number(b.storage_pct || 0) - Number(a.storage_pct || 0);
    }});

    if (!arr.length) {{
      grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:32px; color:#64748B; font-weight:700;">ಯಾವುದೇ ಜಲಾಶಯ ಕಂಡುಬಂದಿಲ್ಲ.</div>';
      return;
    }}

    grid.innerHTML = arr.map(d => {{
      const key = d._key;
      const pct = Number(d.storage_pct || 0);
      const stor = Number(d.storage_tmc || d.present_storage_tmc || 0);
      const cap = Number(d.max_storage_tmc || d.design_capacity || 1);
      const lvl = Number(d.level_ft || 0);
      const frl = DAM_FRL_FT[key] || 0;
      const inflow = Number(d.inflow_cusecs || 0);
      const outflow = Number(d.outflow_cusecs || 0);
      const ch7 = Number(d.storage_change_7d || 0);
      const wc = getWaterColor(pct);
      const bMeta = BASIN_META[d.basin] || {{ kn: 'ಕರ್ನಾಟಕ', icon: '💧' }};
      const distKn = DISTRICT_KN[d.district_en] || d.district_en || '';
      const slug = DAM_PAGE_SLUG[key] || `${{key}}-dam.html`;
      const imgUrl = `/images/${{key}}_dam.jpg`;
      const netFlow = inflow > outflow + 50 ? '📈 ನೀರು ಏರಿಕೆ' : (outflow > inflow + 50 ? '📉 ಹೊರಹರಿವು ಹೆಚ್ಚು' : '⚖️ ಸ್ಥಿರ');
      const d7Cls = ch7 > 0.05 ? 'up' : (ch7 < -0.05 ? 'down' : 'flat');
      const d7Txt = ch7 > 0.05 ? `▲ +${{ch7.toFixed(2)}} TMC (7D)` : (ch7 < -0.05 ? `▼ ${{ch7.toFixed(2)}} TMC (7D)` : `● ಸ್ಥಿರ (7D)`);
      const waterH = Math.min(96, Math.max(12, pct));

      return `
        <article class="dam-tile ${{pct >= 90 ? 'flood-card' : ''}}" id="dam-card-${{key}}">
          <div class="dt-photo">
            <img src="${{imgUrl}}" alt="${{d.name_kn}}" loading="lazy" onerror="this.style.display='none'">
            <div class="dt-badges">
              <span class="dt-basin-tag">${{bMeta.icon}} ${{bMeta.kn}}</span>
              <span class="dt-status-tag ${{wc.badge}}">${{wc.label}}</span>
            </div>
            <div class="dt-title-overlay">
              <div>
                <div class="dt-name">${{d.name_kn}}</div>
                <div class="dt-loc">🌊 ${{d.river_kn || ''}} ನದಿ · 📍 ${{distKn}}</div>
              </div>
              <div class="dt-pct-big">${{pct.toFixed(1)}}%</div>
            </div>
          </div>

          <div class="dt-body">
            <div class="tank-wrap">
              <div class="tank-frl-line"></div>
              <span class="tank-frl-lbl">FRL ${{frl ? frl.toFixed(0) + ' ft' : '100%'}}</span>
              <div class="tank-water" style="height:${{waterH}}%; background:${{wc.fill}};">
                <svg class="tank-wave-svg" viewBox="0 0 1200 28" preserveAspectRatio="none">
                  <path fill="${{wc.wave}}" fill-opacity="0.7" d="M0,14 C150,28 300,0 450,14 C600,28 750,0 900,14 C1050,28 1150,4 1200,14 L1200,28 L0,28 Z"></path>
                </svg>
              </div>
              <div class="tank-overlay">
                <span class="tank-tmc">${{stor.toFixed(2)}} / ${{cap.toFixed(2)}} TMC</span>
                <span class="tank-lvl">📏 ${{lvl.toFixed(1)}} ft</span>
              </div>
            </div>

            <div class="flow-grid">
              <div class="flow-box inflow">
                <div class="flow-lbl">↓ ಒಳಹರಿವು (Inflow)</div>
                <div class="flow-val">${{fmtNum(inflow)}} cfs</div>
              </div>
              <div class="flow-box outflow">
                <div class="flow-lbl">↑ ಹೊರಹರಿವು (Outflow)</div>
                <div class="flow-val">${{fmtNum(outflow)}} cfs</div>
              </div>
            </div>

            <div class="dt-deltas">
              <span>${{netFlow}}</span>
              <span class="delta-pill ${{d7Cls}}">${{d7Txt}}</span>
            </div>

            <div class="dt-actions">
              <button class="dt-btn dt-btn-chart" onclick="openDamTrend('${{key}}')">📈 ಟ್ರೆಂಡ್ ಚಾರ್ಟ್</button>
              <a href="/dam-levels/${{slug}}" class="dt-btn dt-btn-detail">ಪೂರ್ಣ ವಿವರ →</a>
            </div>
          </div>
        </article>
      `;
    }}).join('');
  }}

  function initHydroMap() {{
    const el = document.getElementById('damHydroMap');
    if (!el || typeof L === 'undefined') return;
    damMap = L.map('damHydroMap', {{ center: [14.35, 76.15], zoom: 7, scrollWheelZoom: false }});
    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
      maxZoom: 16,
      attribution: '&copy; OpenStreetMap | Karnata.in'
    }}).addTo(damMap);
    damMapLayer = L.layerGroup().addTo(damMap);
    plotDamsOnMap();
  }}

  function plotDamsOnMap() {{
    if (!damMapLayer) return;
    damMapLayer.clearLayers();
    getDamsArray().forEach(d => {{
      if (!d.lat || !d.lon) return;
      const pct = Number(d.storage_pct || 0);
      const wc = getWaterColor(pct);
      const key = d._key;
      const slug = DAM_PAGE_SLUG[key] || `${{key}}-dam.html`;
      const icon = L.divIcon({{
        className: 'hydro-pin-wrap',
        html: `<div class="hydro-pin ${{pct >= 90 ? 'flood' : ''}}"><div class="hydro-pin-fill" style="height:${{Math.min(100, Math.max(12, pct))}}%; background:${{wc.solid}};"></div><span>${{Math.round(pct)}}%</span></div>`,
        iconSize: [44, 44],
        iconAnchor: [22, 22]
      }});
      const m = L.marker([d.lat, d.lon], {{ icon }}).addTo(damMapLayer);
      m.bindPopup(`
        <div style="font-family:'Anek Kannada',sans-serif; min-width:190px;">
          <div style="font-weight:800; font-size:14.5px; color:#092540;">${{d.name_kn}}</div>
          <div style="font-size:12px; color:#475569; margin:3px 0 6px;">🌊 ${{d.river_kn || ''}} · <b>${{pct.toFixed(1)}}%</b> (${{Number(d.storage_tmc||0).toFixed(2)}}/${{Number(d.max_storage_tmc||0).toFixed(2)}} TMC)</div>
          <div style="font-size:12px; color:#047857; font-weight:700;">↓ ಒಳಹರಿವು: ${{fmtNum(d.inflow_cusecs)}} cfs</div>
          <div style="font-size:12px; color:#C2410C; font-weight:700; margin-bottom:8px;">↑ ಹೊರಹರಿವು: ${{fmtNum(d.outflow_cusecs)}} cfs</div>
          <a href="/dam-levels/${{slug}}" style="display:block; text-align:center; background:#092540; color:#fff; padding:6px 10px; border-radius:8px; text-decoration:none; font-size:12px; font-weight:800;">ಪೂರ್ಣ ವಿವರ ನೋಡಿ →</a>
        </div>
      `);
    }});
  }}

  function populateChartSelect() {{
    const sel = document.getElementById('chartDamSelect');
    if (!sel) return;
    const arr = getDamsArray();
    sel.innerHTML = arr.map(d => `<option value="${{d._key}}">${{d.name_kn}}</option>`).join('');
    sel.value = 'krs';
  }}

  function openDamTrend(key) {{
    const sel = document.getElementById('chartDamSelect');
    if (sel) sel.value = key;
    renderTrendChart();
    const sec = document.getElementById('trendChartSection');
    if (sec) sec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }}

  function setChartDays(days, btn) {{
    currentChartDays = days;
    document.querySelectorAll('.tf-btn').forEach(b => b.classList.toggle('active', Number(b.dataset.days) === days));
    renderTrendChart();
  }}

  function renderTrendChart() {{
    const ctx = document.getElementById('damTrendChart');
    if (!ctx || typeof Chart === 'undefined') return;
    const key = document.getElementById('chartDamSelect')?.value || 'krs';
    const dam = LIVE_DAM_DATA?.dams?.[key];
    let points = [];

    if (HISTORY_DATA) {{
      // Support both {{ krs: [...] }} and [{{ date, dams: {{ krs: ... }} }}] history formats
      if (Array.isArray(HISTORY_DATA[key])) {{
        points = HISTORY_DATA[key].map(p => ({{ date: p.date, val: Number(p.storage_tmc ?? p.present_storage_tmc ?? p.tmc ?? 0) }}));
      }} else if (Array.isArray(HISTORY_DATA.records || HISTORY_DATA)) {{
        const list = HISTORY_DATA.records || HISTORY_DATA;
        list.forEach(row => {{
          const entry = row.dams?.[key] || row[key];
          if (entry !== undefined) {{
            const v = typeof entry === 'object' ? Number(entry.storage_tmc ?? entry.present_storage_tmc ?? entry.tmc ?? 0) : Number(entry);
            if (!isNaN(v)) points.push({{ date: row.date, val: v }});
          }}
        }});
      }}
    }}

    if (!points.length && dam) {{
      const cur = Number(dam.storage_tmc || 0);
      const ch7 = Number(dam.storage_change_7d || 0);
      const start = Math.max(0, cur - ch7);
      for (let i = 6; i >= 0; i--) {{
        const dt = new Date(Date.now() - i * 86400000);
        const frac = (6 - i) / 6;
        points.push({{ date: dt.toISOString().slice(5, 10), val: +(start + (cur - start) * frac).toFixed(2) }});
      }}
    }}

    const sliced = points.slice(-currentChartDays);
    const labels = sliced.map(p => String(p.date || '').slice(-5));
    const values = sliced.map(p => p.val);
    const sub = document.getElementById('chartSubTitle');
    if (sub && dam) {{
      sub.textContent = `${{dam.name_kn}} · ಪ್ರಸ್ತುತ: ${{Number(dam.storage_tmc||0).toFixed(2)}} / ${{Number(dam.max_storage_tmc||0).toFixed(2)}} TMC (${{Number(dam.storage_pct||0).toFixed(1)}}%)`;
    }}

    if (trendChartInstance) trendChartInstance.destroy();
    const grad = ctx.getContext('2d').createLinearGradient(0, 0, 0, 280);
    grad.addColorStop(0, 'rgba(14, 165, 233, 0.38)');
    grad.addColorStop(1, 'rgba(14, 165, 233, 0.02)');

    trendChartInstance = new Chart(ctx, {{
      type: 'line',
      data: {{
        labels,
        datasets: [{{
          label: 'ನೀರಿನ ಸಂಗ್ರಹ (TMC)',
          data: values,
          borderColor: '#0284C7',
          backgroundColor: grad,
          borderWidth: 2.8,
          fill: true,
          tension: 0.35,
          pointRadius: sliced.length > 35 ? 0 : 3.5,
          pointBackgroundColor: '#092540'
        }}]
      }},
      options: {{
        responsive: true,
        maintainAspectRatio: false,
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
          x: {{ grid: {{ display: false }}, ticks: {{ maxTicksLimit: 10, font: {{ size: 11 }} }} }},
          y: {{ beginAtZero: false, grid: {{ color: '#E2E8F0' }}, ticks: {{ callback: v => v + ' TMC', font: {{ size: 11 }} }} }}
        }}
      }}
    }});
  }}

  async function refreshLiveData() {{
    try {{
      const r = await fetch('/data/dam_levels.json?v=' + Date.now());
      if (r.ok) {{
        const j = await r.json();
        const dec = j?.payload ? decryptPayload(j.payload) : j;
        if (dec && dec.dams) {{
          LIVE_DAM_DATA = dec;
          renderHeroAndKpis();
          renderBasinCards();
          renderDamCards();
          plotDamsOnMap();
        }}
      }}
    }} catch (e) {{}}

    try {{
      const hr = await fetch('/data/history/dam_history.json?v=' + Date.now());
      if (hr.ok) {{
        const hj = await hr.json();
        HISTORY_DATA = hj?.payload ? decryptPayload(hj.payload) : hj;
        renderTrendChart();
      }}
    }} catch (e) {{}}
  }}

  document.addEventListener('DOMContentLoaded', () => {{
    renderHeroAndKpis();
    renderBasinCards();
    renderDamCards();
    initHydroMap();
    populateChartSelect();
    renderTrendChart();
    refreshLiveData();
  }});
</script>

</body>
</html>
'''

    OUT_HTML.write_text(page_html, encoding="utf-8")
    print(f"SUCCESS: Built creative dam-levels.html ({len(page_html):,} bytes, 13 reservoirs, live Leaflet map, liquid tanks & Chart.js history).")


if __name__ == "__main__":
    main()
