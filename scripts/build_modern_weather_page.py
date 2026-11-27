# -*- coding: utf-8 -*-
"""
Karnata — build_modern_weather_page.py
Builds the ultra-creative, meteorological-grade Karnataka Weather Dashboard (weather.html):
- Auto Geolocation (GPS + IP fallback) working from ANY location with live hyper-local Open-Meteo weather, AQI, Sunrise/Sunset & nearest Karnataka district map sync
- Creative Bento Cards: Live AQI Gauge (PM2.5/PM10/UV) + Interactive Sunrise/Sunset Solar Arc
- KSNDMC Live Top-5 Leaderboards: Top 5 Rainfall, Top 5 Max Temp, Top 5 Min Temp
- Precision 31-District Official IMD Karnataka Interactive SVG Warnings Map (Nowcast + 5-Day Forecast)
- 24-Hour Hourly + 7-Day Outlook + 31-District Telemetry Grid
- Rich Kannada Editorial Weather Article, Alert Guide, AQI Guide & Monsoon Science below
- Full compatibility with sync_weather_page.py and sync_all_static_dom.py
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
import math
from pathlib import Path
from shapely.geometry import shape

ROOT_DIR = Path(__file__).resolve().parent.parent

IMD_MAP_DIST_INFO = {
    'BAGALKOT': ('bagalkote', 'ಬಾಗಲಕೋಟೆ', 'Bagalkote', 'ಬಾಗಲಕೋಟೆ', 16.1831, 75.6965),
    'BALLARI': ('ballari', 'ಬಳ್ಳಾರಿ', 'Ballari', 'ಬಳ್ಳಾರಿ', 15.1394, 76.9214),
    'BELAGAVI': ('belagavi', 'ಬೆಳಗಾವಿ', 'Belagavi', 'ಬೆಳಗಾವಿ', 15.8497, 74.4977),
    'BENGALURU RURAL': ('bengaluru_rural', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 'Bengaluru Rural', 'ಬೆಂ.ಗ್ರಾಮಾಂತರ', 13.0072, 77.5673),
    'BENGALURU URBAN': ('bengaluru_urban', 'ಬೆಂಗಳೂರು ನಗರ', 'Bengaluru Urban', 'ಬೆಂಗಳೂರು', 12.9716, 77.5946),
    'BIDAR': ('bidar', 'ಬೀದರ್', 'Bidar', 'ಬೀದರ್', 17.9104, 77.5199),
    'CHAMARAJANAGAR': ('chamarajanagara', 'ಚಾಮರಾಜನಗರ', 'Chamarajanagar', 'ಚಾಮರಾಜನಗರ', 11.9261, 76.9439),
    'CHIK BALLAPUR': ('chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 'Chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 13.4356, 77.7310),
    'CHIKKAMAGALURU': ('chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು', 'Chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು', 13.3153, 75.7754),
    'CHITRADURGA': ('chitradurga', 'ಚಿತ್ರದುರ್ಗ', 'Chitradurga', 'ಚಿತ್ರದುರ್ಗ', 14.2226, 76.3984),
    'DAKSHINA  KANNADA': ('dakshina_kannada', 'ದಕ್ಷಿಣ ಕನ್ನಡ', 'Dakshina Kannada', 'ದ.ಕನ್ನಡ', 12.8438, 74.9919),
    'DAVANGERE': ('davanagere', 'ದಾವಣಗೆರೆ', 'Davanagere', 'ದಾವಣಗೆರೆ', 14.4644, 75.9218),
    'DHARWAD': ('dharwad', 'ಧಾರವಾಡ', 'Dharwad', 'ಧಾರವಾಡ', 15.4589, 75.0078),
    'GADAG': ('gadag', 'ಗದಗ', 'Gadag', 'ಗದಗ', 15.4167, 75.6167),
    'HASSAN': ('hassan', 'ಹಾಸನ', 'Hassan', 'ಹಾಸನ', 13.0068, 76.1003),
    'HAVERI': ('haveri', 'ಹಾವೇರಿ', 'Haveri', 'ಹಾವೇರಿ', 14.7957, 75.3998),
    'KALABURAGI': ('kalaburagi', 'ಕಲಬುರಗಿ', 'Kalaburagi', 'ಕಲಬುರಗಿ', 17.3297, 76.8343),
    'KODAGU': ('kodagu', 'ಕೊಡಗು', 'Kodagu', 'ಕೊಡಗು', 12.3375, 75.8069),
    'KOLAR': ('kolar', 'ಕೋಲಾರ', 'Kolar', 'ಕೋಲಾರ', 13.1363, 78.1294),
    'KOPPAL': ('koppal', 'ಕೊಪ್ಪಳ', 'Koppal', 'ಕೊಪ್ಪಳ', 15.3474, 76.1547),
    'MANDYA': ('mandya', 'ಮಂಡ್ಯ', 'Mandya', 'ಮಂಡ್ಯ', 12.5220, 76.8951),
    'MYSURU': ('mysuru', 'ಮೈಸೂರು', 'Mysuru', 'ಮೈಸೂರು', 12.2958, 76.6394),
    'RAICHUR': ('raichur', 'ರಾಯಚೂರು', 'Raichur', 'ರಾಯಚೂರು', 16.2120, 77.3439),
    'RAMANAGARAM': ('ramanagara', 'ರಾಮನಗರ', 'Ramanagara', 'ರಾಮನಗರ', 12.7156, 77.2817),
    'SHIVAMOGGA': ('shivamogga', 'ಶಿವಮೊಗ್ಗ', 'Shivamogga', 'ಶಿವಮೊಗ್ಗ', 13.9299, 75.5681),
    'TUMAKURU': ('tumakuru', 'ತುಮಕೂರು', 'Tumakuru', 'ತುಮಕೂರು', 13.3379, 77.1173),
    'UDUPI': ('udupi', 'ಉಡುಪಿ', 'Udupi', 'ಉಡುಪಿ', 13.3409, 74.7421),
    'UTTARA  KANNADA': ('uttara_kannada', 'ಉತ್ತರ ಕನ್ನಡ', 'Uttara Kannada', 'ಉ.ಕನ್ನಡ', 14.7941, 74.6561),
    'VIJAYAPURA': ('vijayapura', 'ವಿಜಯಪುರ', 'Vijayapura', 'ವಿಜಯಪುರ', 16.8302, 75.7100),
    'VIJAYANAGARA': ('vijayanagara', 'ವಿಜಯನಗರ', 'Vijayanagara', 'ವಿಜಯನಗರ', 15.1720, 76.4560),
    'YADGIR': ('yadgir', 'ಯಾದಗಿರಿ', 'Yadgir', 'ಯಾದಗಿರಿ', 16.7620, 77.1382)
}

LABEL_OFFSETS = {
    'bengaluru_urban': (2, 2),
    'bengaluru_rural': (20, -18),
    'ramanagara': (-8, 10),
    'kolar': (8, 0),
    'chikkaballapura': (6, -6),
    'tumakuru': (6, 0),
    'chamarajanagara': (8, 8),
    'dakshina_kannada': (4, 4),
    'udupi': (-4, 0),
    'uttara_kannada': (6, 0),
    'vijayanagara': (-4, 2),
    'dharwad': (-4, 2),
    'gadag': (4, 0),
    'mandya': (0, 2),
}


def build_svg_districts():
    """Generates lightweight, precision 31-district SVG paths from official IMD GeoJSON."""
    geo_path = ROOT_DIR / "data" / "gis" / "imd_karnataka_districts.geojson"
    with open(geo_path, "r", encoding="utf-8") as f:
        geo = json.load(f)

    min_lon, min_lat, max_lon, max_lat = 180, 90, -180, -90
    geoms = {}
    for feat in geo["features"]:
        dname = feat["properties"]["DISTRICT"]
        g = shape(feat["geometry"]).simplify(0.008, preserve_topology=True)
        geoms[dname] = g
        b = g.bounds
        min_lon = min(min_lon, b[0])
        min_lat = min(min_lat, b[1])
        max_lon = max(max_lon, b[2])
        max_lat = max(max_lat, b[3])

    view_w, view_h, pad = 620, 840, 18
    usable_w = view_w - 2 * pad
    usable_h = view_h - 2 * pad
    mid_lat = (min_lat + max_lat) / 2.0
    cos_lat = math.cos(math.radians(mid_lat))
    geo_w = (max_lon - min_lon) * cos_lat
    geo_h = max_lat - min_lat
    scale = min(usable_w / geo_w, usable_h / geo_h)
    offset_x = pad + (usable_w - geo_w * scale) / 2.0
    offset_y = pad + (usable_h - geo_h * scale) / 2.0

    def project(lon, lat):
        x = offset_x + (lon - min_lon) * cos_lat * scale
        y = offset_y + (max_lat - lat) * scale
        return round(x, 1), round(y, 1)

    def geom_to_path(g):
        parts = []
        polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
        for p in polys:
            coords = list(p.exterior.coords)
            if len(coords) < 3:
                continue
            pts = [project(lon, lat) for lon, lat in coords]
            parts.append("M" + "L".join(f"{x},{y}" for x, y in pts) + "Z")
        return "".join(parts)

    paths_html = []
    labels_html = []
    coords_map = {}
    for dname, g in geoms.items():
        info = IMD_MAP_DIST_INFO.get(dname)
        if not info:
            continue
        dist_id, dist_kn, dist_en, short_lbl, lat, lon = info
        coords_map[dist_id] = {"lat": lat, "lon": lon, "kn": dist_kn, "en": dist_en}
        d_str = geom_to_path(g)
        rep = g.representative_point()
        cx, cy = project(rep.x, rep.y)
        ox, oy = LABEL_OFFSETS.get(dist_id, (0, 0))
        cx = round(cx + ox, 1)
        cy = round(cy + oy, 1)

        paths_html.append(
            f'<path id="map-dist-{dist_id}" class="ka-dist-path level-green" '
            f'data-district="{dist_id}" data-name-kn="{dist_kn}" data-name-en="{dist_en}" '
            f'tabindex="0" role="button" aria-label="{dist_kn} ({dist_en})" '
            f'd="{d_str}"/>'
        )
        labels_html.append(
            f'<text class="ka-dist-label" data-district="{dist_id}" x="{cx}" y="{cy}">{short_lbl}</text>'
        )

    svg_markup = (
        f'<svg id="karnataka-warnings-svg" viewBox="0 0 {view_w} {view_h}" '
        f'role="img" aria-label="ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ (Karnataka 31 Districts Weather Warnings Map)">\n'
        f'  <defs>\n'
        f'    <filter id="distShadow" x="-10%" y="-10%" width="120%" height="120%">\n'
        f'      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.16"/>\n'
        f'    </filter>\n'
        f'  </defs>\n'
        f'  <g id="ka-districts-layer" filter="url(#distShadow)">\n    '
        + "\n    ".join(paths_html)
        + "\n  </g>\n  <g id=\"ka-labels-layer\" pointer-events=\"none\">\n    "
        + "\n    ".join(labels_html)
        + "\n  </g>\n</svg>"
    )
    print(f"Built precision 31-district SVG ({len(paths_html)} districts, {len(svg_markup):,} bytes)")
    return svg_markup, coords_map


def build_weather_html():
    svg_map, coords_map = build_svg_districts()
    coords_json = json.dumps(coords_map, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="geo.region" content="IN-KA">
  <meta name="geo.placename" content="Karnataka, India">
  <meta name="geo.position" content="12.9716;77.5946">
  <meta name="ICBM" content="12.9716, 77.5946">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large">
  <script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478"></script>

  <title>ಕರ್ನಾಟಕ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ, AQI, ಸೂರ್ಯೋದಯ &amp; 31 ಜಿಲ್ಲೆಗಳ ಮಳೆ ನಕ್ಷೆ | Karnataka Live Weather — Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ ನಕ್ಷೆ, ನಿಮ್ಮ ಸ್ಥಳದ GPS ಲೈವ್ ಹವಾಮಾನ, AQI ವಾಯು ಗುಣಮಟ್ಟ, ಸೂರ್ಯೋದಯ-ಸೂರ್ಯಾಸ್ತ ಸಮಯ, KSNDMC ಟಾಪ್-5 ಮಳೆ &amp; ತಾಪಮಾನ, IMD ನೌಕಾಸ್ಟ್ ಮತ್ತು 5 ದಿನಗಳ ಎಚ್ಚರಿಕೆ.">
  <meta name="keywords" content="Karnataka weather today, IMD Karnataka district warnings map, live AQI Karnataka, sunrise sunset time Bengaluru, KSNDMC top 5 rainfall, GPS weather near me">
  <link rel="canonical" href="https://karnata.in/weather">
  <link rel="alternate" hreflang="kn-IN" href="https://karnata.in/weather">
  <link rel="alternate" hreflang="en-IN" href="https://karnata.in/weather">
  <link rel="alternate" hreflang="x-default" href="https://karnata.in/weather">

  <!-- Open Graph & Twitter -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ, AQI &amp; IMD ಮಳೆ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ — Karnata.in">
  <meta property="og:description" content="ನಿಮ್ಮ ಸ್ಥಳದ ಲೈವ್ ಹವಾಮಾನ, AQI, ಸೂರ್ಯೋದಯ-ಸೂರ್ಯಾಸ್ತ, KSNDMC ಟಾಪ್-5 ಮಳೆ/ತಾಪಮಾನ ಮತ್ತು IMD 31 ಜಿಲ್ಲೆಗಳ ನೌಕಾಸ್ಟ್ &amp; 5 ದಿನಗಳ ನಕ್ಷೆ.">
  <meta property="og:url" content="https://karnata.in/weather">
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in">
  <meta property="og:locale" content="kn_IN">
  <meta property="og:image" content="https://karnata.in/assets/social-cards/weather_nowcast_map.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ, AQI &amp; IMD ಮಳೆ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ — Karnata.in">
  <meta name="twitter:description" content="GPS ಲೈವ್ ಹವಾಮಾನ, AQI, ಸೂರ್ಯೋದಯ-ಸೂರ್ಯಾಸ್ತ, ಟಾಪ್-5 ಮಳೆ/ತಾಪಮಾನ ಮತ್ತು IMD 31 ಜಿಲ್ಲೆಗಳ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ.">
  <meta name="twitter:image" content="https://karnata.in/assets/social-cards/weather_nowcast_map.png">

  <!-- JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ, AQI & IMD ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ",
    "applicationCategory": "UtilityApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/weather",
    "description": "Hyper-local geolocation live weather, Air Quality Index (AQI), Sunrise & Sunset solar tracker, KSNDMC Top-5 rainfall & temperature leaderboards, and official 31-district IMD Karnataka warnings map."
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  <script src="/data-loader.js"></script>
  <script src="/nav-component.js?v=20260830_v6"></script>

  <style>
    :root {{
      --wx-ink: #0F172A;
      --wx-muted: #64748B;
      --wx-bg: #F1F5F9;
      --wx-card: #FFFFFF;
      --wx-border: #E2E8F0;
      --wx-blue: #0284C7;
      --wx-blue-dark: #0369A1;
      --wx-red: #DC2626;
      --wx-red-bg: #FEF2F2;
      --wx-orange: #EA580C;
      --wx-orange-bg: #FFF7ED;
      --wx-yellow: #CA8A04;
      --wx-yellow-bg: #FEFCE8;
      --wx-green: #16A34A;
      --wx-green-bg: #F0FDF4;
      --wx-radius: 20px;
      --wx-shadow: 0 12px 32px -12px rgba(15, 23, 42, 0.09);
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Anek Kannada', 'Inter', system-ui, sans-serif;
      background: var(--wx-bg);
      color: var(--wx-ink);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    .wx-wrap {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 16px;
    }}

    /* ═══ ATMOSPHERIC HERO BANNER WITH LIVE GEOLOCATION ═══ */
    .wx-hero {{
      background:
        radial-gradient(circle at 84% 16%, rgba(56, 189, 248, 0.28) 0%, transparent 48%),
        radial-gradient(circle at 12% 88%, rgba(251, 191, 36, 0.16) 0%, transparent 45%),
        linear-gradient(135deg, #06101F 0%, #0C2340 48%, #0F355E 100%);
      color: #F8FAFC;
      padding: 26px 0 74px;
      position: relative;
      overflow: hidden;
    }}
    .wx-hero-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .wx-live-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(15, 23, 42, 0.58);
      border: 1px solid rgba(148, 163, 184, 0.3);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 700;
      color: #E0F2FE;
      backdrop-filter: blur(10px);
    }}
    .wx-live-dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #22C55E;
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
      animation: wxPulse 1.8s infinite;
    }}
    @keyframes wxPulse {{
      0% {{ box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }}
      70% {{ box-shadow: 0 0 0 9px rgba(34, 197, 94, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }}
    }}

    .wx-district-picker {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .wx-select {{
      background: rgba(255, 255, 255, 0.12);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.28);
      border-radius: 12px;
      padding: 9px 14px;
      font-family: inherit;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      min-width: 215px;
      backdrop-filter: blur(8px);
    }}
    .wx-select option {{ background: #0F172A; color: #F8FAFC; }}
    .wx-gps-btn {{
      background: linear-gradient(135deg, #0EA5E9, #0284C7);
      color: #FFFFFF;
      border: none;
      border-radius: 12px;
      padding: 9px 15px;
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 6px 16px rgba(14, 165, 233, 0.35);
      transition: transform 0.15s, filter 0.15s;
    }}
    .wx-gps-btn:hover {{ filter: brightness(1.08); transform: translateY(-1px); }}

    .wx-geo-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.18);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: #A7F3D0;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 11px;
      border-radius: 999px;
      margin-bottom: 10px;
    }}

    .wx-hero-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr);
      gap: 22px;
      align-items: center;
    }}
    @media (max-width: 860px) {{ .wx-hero-grid {{ grid-template-columns: 1fr; }} }}

    .wx-hero-title {{
      font-size: clamp(1.35rem, 1.05rem + 1.3vw, 2.05rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #FFFFFF;
      margin-bottom: 6px;
    }}
    .wx-hero-sub {{
      font-size: 13.5px;
      color: #BAE6FD;
      margin-bottom: 16px;
    }}
    .wx-temp-row {{
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }}
    .wx-temp-big {{
      font-family: 'Inter', sans-serif;
      font-size: clamp(2.8rem, 2.2rem + 2.4vw, 4.3rem);
      font-weight: 900;
      line-height: 1;
      color: #FFFFFF;
    }}
    .wx-cond-desc {{ font-size: 18px; font-weight: 800; color: #FDE68A; }}
    .wx-cond-loc {{ font-size: 14px; color: #CBD5E1; font-weight: 600; }}

    .wx-hero-metrics {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}
    .wx-m-pill {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 14px;
      padding: 12px 14px;
      backdrop-filter: blur(8px);
    }}
    .wx-m-lbl {{ font-size: 11.5px; color: #94A3B8; font-weight: 700; margin-bottom: 2px; }}
    .wx-m-val {{ font-family: 'Inter', 'Anek Kannada', sans-serif; font-size: 18px; font-weight: 800; color: #FFFFFF; }}

    /* ═══ FLOATING KSNDMC EXTREMES STRIP ═══ */
    .wx-extremes-strip {{
      margin-top: -46px;
      position: relative;
      z-index: 5;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 22px;
    }}
    @media (max-width: 760px) {{ .wx-extremes-strip {{ grid-template-columns: 1fr; margin-top: -36px; }} }}
    .wx-ext-card {{
      background: var(--wx-card);
      border: 1px solid var(--wx-border);
      border-radius: 16px;
      padding: 14px 18px;
      box-shadow: var(--wx-shadow);
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .wx-ext-icon {{
      width: 46px; height: 46px; border-radius: 13px;
      display: flex; align-items: center; justify-content: center;
      font-size: 22px; flex-shrink: 0;
    }}
    .wx-ext-icon.rain {{ background: #E0F2FE; }}
    .wx-ext-icon.hot {{ background: #FEF2F2; }}
    .wx-ext-icon.cold {{ background: #EEF2FF; }}
    .wx-ext-title {{ font-size: 11.5px; font-weight: 700; color: var(--wx-muted); }}
    .wx-ext-val {{ font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 900; color: var(--wx-ink); line-height: 1.2; }}
    .wx-ext-loc {{ font-size: 12.5px; font-weight: 700; color: var(--wx-blue-dark); }}

    /* ═══ CREATIVE BENTO: LIVE AQI GAUGE + SUNRISE/SUNSET SOLAR ARC ═══ */
    .wx-bento-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
      margin-bottom: 22px;
    }}
    @media (max-width: 820px) {{ .wx-bento-grid {{ grid-template-columns: 1fr; }} }}

    .wx-bento-card {{
      background: var(--wx-card);
      border: 1px solid var(--wx-border);
      border-radius: var(--wx-radius);
      padding: 20px;
      box-shadow: var(--wx-shadow);
      position: relative;
      overflow: hidden;
    }}
    .wx-bento-card.sun-card {{
      background: linear-gradient(145deg, #FFFBEB 0%, #FFFFFF 55%, #EFF6FF 100%);
      border-color: #FDE68A;
    }}
    .wx-bento-card.aqi-card {{
      background: linear-gradient(145deg, #F0FDF4 0%, #FFFFFF 55%, #F8FAFC 100%);
      border-color: #CBD5E1;
    }}
    .wx-bento-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
    }}
    .wx-bento-title {{ font-size: 16px; font-weight: 900; color: #0F172A; }}
    .wx-bento-tag {{
      font-size: 11.5px; font-weight: 800; padding: 4px 10px; border-radius: 999px;
      background: #0F172A; color: #FFFFFF;
    }}

    /* AQI Meter */
    .wx-aqi-main {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 14px;
    }}
    .wx-aqi-score-wrap {{
      display: flex;
      align-items: baseline;
      gap: 10px;
    }}
    .wx-aqi-num {{
      font-family: 'Inter', sans-serif;
      font-size: 42px;
      font-weight: 900;
      line-height: 1;
      color: #16A34A;
    }}
    .wx-aqi-status {{
      font-size: 16px;
      font-weight: 900;
      color: #15803D;
    }}
    .wx-aqi-bar-track {{
      height: 10px;
      border-radius: 999px;
      background: linear-gradient(90deg, #22C55E 0%, #84CC16 20%, #EAB308 42%, #F97316 64%, #EF4444 82%, #7E22CE 100%);
      position: relative;
      margin-bottom: 14px;
    }}
    .wx-aqi-marker {{
      position: absolute;
      top: 50%;
      left: 18%;
      transform: translate(-50%, -50%);
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 4px solid #0F172A;
      box-shadow: 0 2px 8px rgba(0,0,0,0.28);
      transition: left 0.45s ease;
    }}
    .wx-aqi-subgrid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }}
    .wx-aqi-mini {{
      background: rgba(255,255,255,0.88);
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 9px 10px;
      text-align: center;
    }}
    .wx-aqi-mini-lbl {{ font-size: 11px; color: #64748B; font-weight: 700; }}
    .wx-aqi-mini-val {{ font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 900; color: #0F172A; }}

    /* Sunrise & Sunset Solar Arc */
    .wx-sun-arc-wrap {{
      position: relative;
      max-width: 340px;
      margin: 4px auto 12px;
    }}
    .wx-sun-times {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }}
    .wx-sun-pill {{
      background: rgba(255,255,255,0.9);
      border: 1px solid #FDE68A;
      border-radius: 12px;
      padding: 10px;
      text-align: center;
    }}
    .wx-sun-pill-lbl {{ font-size: 11px; font-weight: 700; color: #92400E; }}
    .wx-sun-pill-val {{ font-family: 'Inter', sans-serif; font-size: 15.5px; font-weight: 900; color: #0F172A; }}

    /* ═══ TOP 5 LEADERBOARDS (RAIN, MAX TEMP, MIN TEMP) ═══ */
    .wx-top5-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    @media (max-width: 960px) {{ .wx-top5-grid {{ grid-template-columns: 1fr; }} }}
    .wx-t5-card {{
      background: var(--wx-card);
      border: 1px solid var(--wx-border);
      border-radius: var(--wx-radius);
      padding: 18px;
      box-shadow: var(--wx-shadow);
    }}
    .wx-t5-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1.5px solid #F1F5F9;
    }}
    .wx-t5-title {{ font-size: 15px; font-weight: 900; color: #0F172A; }}
    .wx-t5-list {{ display: flex; flex-direction: column; gap: 9px; }}
    .wx-t5-row {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      padding: 8px 10px;
      border-radius: 12px;
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
    }}
    .wx-t5-row-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}
    .wx-t5-rank {{
      display: inline-flex; align-items: center; justify-content: center;
      width: 22px; height: 22px; border-radius: 50%;
      font-family: 'Inter', sans-serif; font-size: 11.5px; font-weight: 900;
      background: #0F172A; color: #FFFFFF; flex-shrink: 0;
    }}
    .wx-t5-row:first-child .wx-t5-rank {{ background: #F59E0B; color: #0F172A; }}
    .wx-t5-place {{ flex: 1; min-width: 0; }}
    .wx-t5-dist {{ font-size: 13.5px; font-weight: 800; color: #0F172A; display: block; }}
    .wx-t5-stn {{ font-size: 11.5px; color: #64748B; font-weight: 600; }}
    .wx-t5-val {{ font-family: 'Inter', sans-serif; font-size: 14.5px; font-weight: 900; white-space: nowrap; }}
    .wx-t5-val.rain {{ color: #0284C7; }}
    .wx-t5-val.hot {{ color: #DC2626; }}
    .wx-t5-val.cold {{ color: #2563EB; }}
    .wx-t5-bar {{ height: 5px; border-radius: 999px; background: #E2E8F0; overflow: hidden; }}
    .wx-t5-fill {{ height: 100%; border-radius: 999px; }}
    .wx-t5-fill.rain {{ background: linear-gradient(90deg, #38BDF8, #0284C7); }}
    .wx-t5-fill.hot {{ background: linear-gradient(90deg, #FB923C, #DC2626); }}
    .wx-t5-fill.cold {{ background: linear-gradient(90deg, #60A5FA, #1D4ED8); }}

    /* ═══ MAIN SECTIONS & CARDS ═══ */
    .wx-section {{
      background: var(--wx-card);
      border: 1px solid var(--wx-border);
      border-radius: var(--wx-radius);
      padding: 22px;
      box-shadow: var(--wx-shadow);
      margin-bottom: 24px;
      container-type: inline-size;
    }}
    .wx-sec-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .wx-sec-title {{
      font-size: clamp(1.1rem, 0.95rem + 0.7vw, 1.4rem);
      font-weight: 800;
      color: var(--wx-ink);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .wx-sec-sub {{ font-size: 13px; color: var(--wx-muted); margin-top: 2px; }}

    /* ═══ ACCESSIBLE SINGLE-ROW SCROLLABLE TABS (NOWCAST + 5 DAYS) ═══ */
    .wx-tablist {{
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      gap: 8px;
      padding: 4px 2px 10px;
      margin-bottom: 14px;
      border-bottom: 1.5px solid #E2E8F0;
      scroll-snap-type: inline proximity;
      scrollbar-width: none;
    }}
    .wx-tablist::-webkit-scrollbar {{ display: none; }}
    .wd-tab {{
      flex: none;
      scroll-snap-align: start;
      position: relative;
      background: #F8FAFC;
      color: #334155;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 9px 15px;
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: background 0.18s, color 0.18s, border-color 0.18s;
    }}
    .wd-tab:hover {{ background: #EFF6FF; border-color: #93C5FD; }}
    .wd-tab[aria-selected="true"], .wd-tab.active {{
      background: #0F172A;
      color: #FFFFFF;
      border-color: #0F172A;
    }}
    .wd-tab[aria-selected="true"]::after, .wd-tab.active::after {{
      content: "";
      position: absolute;
      inset: auto 10px -11px 10px;
      border-block-end: 3px solid #0284C7;
      border-radius: 3px;
    }}

    /* ═══ SEVERITY SUMMARY FILTER BAR ═══ */
    .wx-severity-bar {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }}
    .wx-sev-pill {{
      display: inline-flex; align-items: center; gap: 7px;
      padding: 7px 13px; border-radius: 999px; border: 1.5px solid transparent;
      font-family: inherit; font-size: 13px; font-weight: 800; cursor: pointer;
      transition: transform 0.15s, box-shadow 0.15s;
    }}
    .wx-sev-pill:hover {{ transform: translateY(-1px); }}
    .wx-sev-pill.all {{ background: #F1F5F9; color: #0F172A; border-color: #CBD5E1; }}
    .wx-sev-pill.red {{ background: var(--wx-red-bg); color: #B91C1C; border-color: #FECACA; }}
    .wx-sev-pill.orange {{ background: var(--wx-orange-bg); color: #C2410C; border-color: #FED7AA; }}
    .wx-sev-pill.yellow {{ background: var(--wx-yellow-bg); color: #A16207; border-color: #FEF08A; }}
    .wx-sev-pill.green {{ background: var(--wx-green-bg); color: #15803D; border-color: #BBF7D0; }}
    .wx-sev-pill.active-filter {{ box-shadow: 0 0 0 2.5px #0F172A; }}
    .wx-sev-count {{
      font-family: 'Inter', sans-serif; background: rgba(255,255,255,0.85);
      padding: 1px 7px; border-radius: 999px; font-size: 12px; font-weight: 900;
    }}

    /* ═══ 31-DISTRICT INTERACTIVE MAP + INSPECTOR LAYOUT ═══ */
    .wx-map-layout {{
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.95fr);
      gap: 20px;
      align-items: start;
      margin-bottom: 22px;
    }}
    @container (max-width: 820px) {{ .wx-map-layout {{ grid-template-columns: 1fr; }} }}
    @media (max-width: 860px) {{ .wx-map-layout {{ grid-template-columns: 1fr; }} }}

    .wx-map-stage {{
      position: relative;
      background: radial-gradient(circle at 50% 42%, #FFFFFF 0%, #EFF6FF 65%, #E2E8F0 100%);
      border: 1.5px solid #CBD5E1;
      border-radius: 16px;
      padding: 14px;
      overflow: hidden;
    }}
    .wx-map-stage-head {{
      display: flex; justify-content: space-between; align-items: center;
      flex-wrap: wrap; gap: 8px; margin-bottom: 8px;
    }}
    .wx-map-tab-tag {{ font-size: 12.5px; font-weight: 800; color: #0369A1; background: #E0F2FE; padding: 4px 10px; border-radius: 8px; }}
    .wx-map-hint {{ font-size: 11.5px; color: #475569; font-weight: 600; }}

    #karnataka-warnings-svg {{ width: 100%; max-height: 620px; height: auto; display: block; margin: 0 auto; user-select: none; }}
    .ka-dist-path {{ stroke: #FFFFFF; stroke-width: 1.6; stroke-linejoin: round; cursor: pointer; transition: fill 0.25s ease, opacity 0.2s ease, stroke-width 0.18s ease; }}
    .ka-dist-path.level-red {{ fill: #EF4444; }}
    .ka-dist-path.level-orange {{ fill: #F97316; }}
    .ka-dist-path.level-yellow {{ fill: #FACC15; }}
    .ka-dist-path.level-green {{ fill: #4ADE80; }}
    .ka-dist-path:hover, .ka-dist-path:focus-visible {{ stroke: #0F172A; stroke-width: 3; filter: brightness(0.95); outline: none; }}
    .ka-dist-path.selected {{ stroke: #0F172A; stroke-width: 3.6; filter: drop-shadow(0 0 6px rgba(15, 23, 42, 0.45)); }}
    .ka-dist-path.dimmed {{ opacity: 0.24; }}
    .ka-dist-label {{
      font-family: 'Anek Kannada', sans-serif; font-size: 11.5px; font-weight: 800; fill: #0F172A;
      text-anchor: middle; dominant-baseline: central; paint-order: stroke;
      stroke: rgba(255, 255, 255, 0.92); stroke-width: 3px; stroke-linejoin: round;
    }}
    .wx-map-legend {{
      display: flex; justify-content: center; flex-wrap: wrap; gap: 14px;
      margin-top: 10px; padding-top: 10px; border-top: 1px dashed #CBD5E1;
      font-size: 12px; font-weight: 700; color: #334155;
    }}
    .wx-leg-item {{ display: inline-flex; align-items: center; gap: 6px; }}
    .wx-leg-swatch {{ width: 13px; height: 13px; border-radius: 4px; border: 1px solid rgba(15,23,42,0.15); }}

    .wx-map-tooltip {{
      position: absolute; z-index: 30; pointer-events: none;
      background: rgba(15, 23, 42, 0.95); color: #F8FAFC;
      padding: 10px 13px; border-radius: 12px; font-size: 12.5px;
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25); max-width: 240px;
      opacity: 0; transform: translateY(4px); transition: opacity 0.14s ease, transform 0.14s ease;
    }}
    .wx-map-tooltip.visible {{ opacity: 1; transform: translateY(0); }}

    /* Inspector Panel */
    .wx-inspector {{ display: flex; flex-direction: column; gap: 14px; }}
    .wx-insp-card {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 16px; padding: 18px; }}
    .wx-insp-head {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; margin-bottom: 12px; }}
    .wx-insp-dist-kn {{ font-size: 22px; font-weight: 900; color: #0F172A; line-height: 1.2; }}
    .wx-insp-dist-en {{ font-size: 12.5px; color: #64748B; font-weight: 700; font-family: 'Inter', sans-serif; }}
    .wx-insp-badge {{ padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 800; white-space: nowrap; }}
    .wx-insp-badge.red {{ background: #FEE2E2; color: #B91C1C; }}
    .wx-insp-badge.orange {{ background: #FFEDD5; color: #C2410C; }}
    .wx-insp-badge.yellow {{ background: #FEF9C3; color: #A16207; }}
    .wx-insp-badge.green {{ background: #DCFCE7; color: #15803D; }}
    .wx-insp-advice {{ background: #FFFFFF; border-left: 4px solid #0284C7; padding: 11px 13px; border-radius: 10px; font-size: 13.5px; font-weight: 600; color: #1E293B; margin-bottom: 14px; }}
    .wx-insp-mini-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 14px; }}
    .wx-insp-mini {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 9px 10px; text-align: center; }}
    .wx-insp-mini-lbl {{ font-size: 11px; color: #64748B; font-weight: 700; }}
    .wx-insp-mini-val {{ font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 900; color: #0F172A; }}
    .wx-5d-strip-title {{ font-size: 12.5px; font-weight: 800; color: #334155; margin-bottom: 8px; }}
    .wx-5d-strip {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; }}
    .wx-5d-chip {{ border-radius: 10px; padding: 8px 9px; font-size: 11.5px; font-weight: 800; border: 1px solid transparent; cursor: pointer; text-align: left; transition: transform 0.14s; }}
    .wx-5d-chip:hover {{ transform: translateY(-1px); }}
    .wx-5d-chip.red {{ background: #FEF2F2; color: #B91C1C; border-color: #FECACA; }}
    .wx-5d-chip.orange {{ background: #FFF7ED; color: #C2410C; border-color: #FED7AA; }}
    .wx-5d-chip.yellow {{ background: #FEFCE8; color: #A16207; border-color: #FEF08A; }}
    .wx-5d-chip.green {{ background: #F0FDF4; color: #15803D; border-color: #BBF7D0; }}
    .wx-5d-chip-day {{ display: block; font-size: 11px; opacity: 0.85; }}

    .wx-active-alerts-box {{ background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 16px; padding: 16px; }}
    .wx-active-alerts-list {{ display: flex; flex-wrap: wrap; gap: 7px; margin-top: 10px; max-height: 170px; overflow-y: auto; }}
    .wx-alert-chip-btn {{ border: 1px solid #E2E8F0; border-radius: 999px; padding: 5px 11px; font-family: inherit; font-size: 12px; font-weight: 800; cursor: pointer; }}
    .wx-alert-chip-btn.red {{ background: #FEE2E2; color: #B91C1C; border-color: #FCA5A5; }}
    .wx-alert-chip-btn.orange {{ background: #FFEDD5; color: #C2410C; border-color: #FDBA74; }}
    .wx-alert-chip-btn.yellow {{ background: #FEF9C3; color: #A16207; border-color: #FDE047; }}

    /* Warning Cards Grid */
    .wx-filter-row {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 14px; }}
    .wx-region-pills {{ display: flex; gap: 6px; flex-wrap: wrap; }}
    .wx-reg-btn {{ background: #F1F5F9; color: #334155; border: 1px solid #E2E8F0; border-radius: 999px; padding: 6px 13px; font-family: inherit; font-size: 12.5px; font-weight: 700; cursor: pointer; }}
    .wx-reg-btn.active {{ background: #0284C7; color: #FFFFFF; border-color: #0284C7; }}
    .wx-search-input {{ padding: 8px 14px; border: 1.5px solid #CBD5E1; border-radius: 10px; font-family: inherit; font-size: 13.5px; min-width: 220px; }}
    .dw-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(235px, 1fr)); gap: 12px; }}
    .dw-card {{ border-radius: 14px; padding: 14px; border: 1.5px solid #E2E8F0; background: #FFFFFF; display: flex; flex-direction: column; justify-content: space-between; gap: 8px; cursor: pointer; transition: transform 0.16s, box-shadow 0.16s; }}
    .dw-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08); }}
    .dw-card.red {{ border-color: #FCA5A5; background: #FFF1F2; }}
    .dw-card.orange {{ border-color: #FDBA74; background: #FFF7ED; }}
    .dw-card.yellow {{ border-color: #FDE047; background: #FEFCE8; }}
    .dw-card.green {{ border-color: #BBF7D0; background: #F0FDF4; }}
    .dw-header {{ display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-bottom: 6px; }}
    .dw-level-pill {{ font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 999px; background: rgba(255,255,255,0.85); color: #0F172A; }}
    .dw-region-tag {{ font-size: 11px; font-weight: 700; color: #64748B; }}
    .dw-name-row {{ display: flex; align-items: baseline; gap: 6px; flex-wrap: wrap; }}
    .dw-name-kn {{ font-size: 16px; font-weight: 900; color: #0F172A; }}
    .dw-name-en {{ font-size: 11.5px; color: #64748B; font-family: 'Inter', sans-serif; font-weight: 600; }}
    .dw-hazard-tag {{ font-size: 12.5px; font-weight: 800; color: #1E293B; margin-top: 4px; }}
    .dw-advice {{ font-size: 12px; color: #475569; border-top: 1px dashed rgba(15,23,42,0.12); padding-top: 6px; }}

    /* Hourly & 7-Day */
    .wx-hscroll {{ display: flex; gap: 10px; overflow-x: auto; padding: 4px 2px 10px; scroll-snap-type: inline proximity; }}
    .wx-hour-card {{ flex: 0 0 88px; scroll-snap-align: start; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 12px 8px; text-align: center; }}
    .wx-hour-card.now {{ background: #0F172A; color: #FFFFFF; border-color: #0F172A; }}
    .hi-time {{ font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; opacity: 0.8; }}
    .hi-icon {{ font-size: 24px; margin: 6px 0; }}
    .hi-temp {{ font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 900; }}
    .hi-rain {{ font-size: 11.5px; font-weight: 700; color: #0284C7; margin-top: 4px; }}
    .wx-hour-card.now .hi-rain {{ color: #38BDF8; }}

    .forecast-horizontal-scroll {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)); gap: 10px; }}
    .forecast-h-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px 12px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 5px; }}
    .forecast-h-card.today {{ background: linear-gradient(180deg, #E0F2FE 0%, #F0F9FF 100%); border-color: #38BDF8; }}
    .fhc-day {{ font-size: 14px; font-weight: 900; color: #0F172A; }}
    .fhc-date {{ font-family: 'Inter', sans-serif; font-size: 11.5px; color: #64748B; font-weight: 700; }}
    .fhc-icon {{ font-size: 28px; margin: 4px 0; }}
    .fhc-desc {{ font-size: 12px; font-weight: 700; color: #334155; min-height: 32px; }}
    .fhc-rain-pill {{ background: #E0F2FE; color: #0369A1; font-size: 11.5px; font-weight: 800; padding: 2px 9px; border-radius: 999px; }}
    .fhc-temp-row {{ display: flex; gap: 8px; font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 900; margin-top: 2px; }}
    .fhc-max {{ color: #DC2626; }}
    .fhc-min {{ color: #2563EB; }}

    /* 31-District Telemetry Grid */
    .wx-dist-telemetry-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 10px; }}
    .wx-dt-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 13px; padding: 12px 14px; cursor: pointer; transition: border-color 0.16s, transform 0.14s; }}
    .wx-dt-card:hover {{ border-color: #0284C7; transform: translateY(-2px); }}
    .wx-dt-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }}
    .wx-dt-name {{ font-size: 15px; font-weight: 800; color: #0F172A; }}
    .wx-dt-temp {{ font-family: 'Inter', sans-serif; font-size: 17px; font-weight: 900; color: #0369A1; }}
    .wx-dt-meta {{ font-size: 12px; color: #64748B; display: flex; justify-content: space-between; }}

    /* ═══ EDITORIAL KANNADA WEATHER ARTICLE SECTION ═══ */
    .wx-article {{
      background: var(--wx-card);
      border: 1px solid var(--wx-border);
      border-radius: var(--wx-radius);
      padding: 28px 26px;
      box-shadow: var(--wx-shadow);
      margin-bottom: 32px;
    }}
    .wx-article h2 {{
      font-size: clamp(1.25rem, 1.05rem + 0.8vw, 1.65rem);
      font-weight: 900;
      color: #0F172A;
      margin-bottom: 12px;
      border-bottom: 2px solid #E2E8F0;
      padding-bottom: 10px;
    }}
    .wx-article h3 {{
      font-size: 17px;
      font-weight: 800;
      color: #0369A1;
      margin: 22px 0 8px;
    }}
    .wx-article p {{
      font-size: 15px;
      color: #334155;
      line-height: 1.85;
      margin-bottom: 12px;
    }}
    .wx-article-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 12px;
      margin: 14px 0 18px;
    }}
    .wx-art-box {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 14px 16px;
    }}
    .wx-art-box strong {{ display: block; font-size: 14.5px; color: #0F172A; margin-bottom: 4px; }}
    .wx-art-box span {{ font-size: 13.5px; color: #475569; line-height: 1.65; }}
    .wx-aqi-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 18px;
      font-size: 13.5px;
    }}
    .wx-aqi-table th, .wx-aqi-table td {{
      padding: 10px 12px;
      border: 1px solid #E2E8F0;
      text-align: left;
    }}
    .wx-aqi-table th {{ background: #F1F5F9; font-weight: 800; color: #0F172A; }}
  </style>
</head>
<body>
  <div id="site-nav"></div>

  <!-- ═══ HERO WEATHER COMMAND BANNER (AUTO-GEOLOCATION ENABLED) ═══ -->
  <section class="wx-hero" id="heroWeatherSec">
    <div class="wx-wrap">
      <div class="wx-hero-top">
        <div class="wx-live-badge">
          <span class="wx-live-dot"></span>
          <span id="hero-update-badge">IMD &amp; KSNDMC ಲೈವ್ ಟೆಲಿಮೆಟ್ರಿ — 31 ಜಿಲ್ಲೆಗಳು</span>
        </div>
        <div class="wx-district-picker">
          <select id="heroDistrictSelect" class="wx-select" aria-label="ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ" onchange="selectDistrict(this.value, false)">
            <option value="bengaluru_urban">ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban)</option>
          </select>
          <button type="button" class="wx-gps-btn" id="gpsDetectBtn" onclick="detectUserLocation(true)">📍 ನನ್ನ ಸ್ಥಳ (GPS Live)</button>
        </div>
      </div>

      <div class="wx-geo-pill" id="geoStatusPill">📡 ನಿಮ್ಮ ಸ್ಥಳದ ಲೈವ್ ಹವಾಮಾನ ಪತ್ತೆಹಚ್ಚಲಾಗುತ್ತಿದೆ...</div>

      <div class="wx-hero-grid">
        <div>
          <h1 class="wx-hero-title">ಕರ್ನಾಟಕ ಲೈವ್ ಹವಾಮಾನ, AQI &amp; 31 ಜಿಲ್ಲೆಗಳ ಮಳೆ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ</h1>
          <p class="wx-hero-sub">ನೀವು ಎಲ್ಲೇ ಇದ್ದರೂ ಆ ಸ್ಥಳದ ನೈಜ ಹವಾಮಾನ, AQI, ಸೂರ್ಯೋದಯ-ಸೂರ್ಯಾಸ್ತ, KSNDMC ಟಾಪ್-5 ದಾಖಲೆ ಮತ್ತು IMD 31 ಜಿಲ್ಲೆಗಳ ನಕ್ಷೆ.</p>
          <div class="wx-temp-row">
            <div class="wx-temp-big" id="hero-temp">24.0°C</div>
            <div>
              <div class="wx-cond-desc" id="hero-desc">ಭಾಗಶಃ ಮೋಡ ⛅</div>
              <div class="wx-cond-loc" id="hero-loc">📍 ಬೆಂಗಳೂರು ನಗರ (Bengaluru)</div>
            </div>
          </div>
        </div>

        <div class="wx-hero-metrics">
          <div class="wx-m-pill">
            <div class="wx-m-lbl">🌡️ ಅನುಭವವಾಗುವ ತಾಪಮಾನ</div>
            <div class="wx-m-val" id="hero-feels">24.0°C</div>
          </div>
          <div class="wx-m-pill">
            <div class="wx-m-lbl">💧 ತೇವಾಂಶ (Humidity)</div>
            <div class="wx-m-val" id="hero-humidity">65%</div>
          </div>
          <div class="wx-m-pill">
            <div class="wx-m-lbl">💨 ಗಾಳಿಯ ವೇಗ (Wind)</div>
            <div class="wx-m-val" id="hero-wind">12 km/h</div>
          </div>
          <div class="wx-m-pill">
            <div class="wx-m-lbl">🌧️ ಕಳೆದ 24 ಗಂಟೆ ಮಳೆ</div>
            <div class="wx-m-val" id="hero-rain">0.0 mm</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <main class="wx-wrap">
    <!-- ═══ KSNDMC STATE EXTREMES FLOATING STRIP ═══ -->
    <div class="wx-extremes-strip">
      <div class="wx-ext-card">
        <div class="wx-ext-icon rain">🌧️</div>
        <div>
          <div class="wx-ext-title">ರಾಜ್ಯದ ಗರಿಷ್ಠ ಮಳೆ (24 ಗಂಟೆ · KSNDMC)</div>
          <div class="wx-ext-val" id="cc-rain-val">-- mm</div>
          <div class="wx-ext-loc" id="cc-rain-loc">ಕರ್ನಾಟಕ</div>
        </div>
      </div>
      <div class="wx-ext-card">
        <div class="wx-ext-icon hot">🔥</div>
        <div>
          <div class="wx-ext-title">ರಾಜ್ಯದ ಗರಿಷ್ಠ ತಾಪಮಾನ (Max Temp)</div>
          <div class="wx-ext-val" id="cc-max-temp-val">--°C</div>
          <div class="wx-ext-loc" id="cc-max-temp-loc">ಕರ್ನಾಟಕ</div>
        </div>
      </div>
      <div class="wx-ext-card">
        <div class="wx-ext-icon cold">❄️</div>
        <div>
          <div class="wx-ext-title">ರಾಜ್ಯದ ಕನಿಷ್ಠ ತಾಪಮಾನ (Min Temp)</div>
          <div class="wx-ext-val" id="cc-min-temp-val">--°C</div>
          <div class="wx-ext-loc" id="cc-min-temp-loc">ಕರ್ನಾಟಕ</div>
        </div>
      </div>
    </div>

    <!-- ═══ CREATIVE BENTO: LIVE AQI GAUGE + SUNRISE / SUNSET SOLAR ARC ═══ -->
    <div class="wx-bento-grid">
      <!-- LIVE AQI CARD -->
      <div class="wx-bento-card aqi-card">
        <div class="wx-bento-head">
          <div class="wx-bento-title">🍃 ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (Live AQI)</div>
          <span class="wx-bento-tag" id="aqi-loc-tag">ಬೆಂಗಳೂರು</span>
        </div>
        <div class="wx-aqi-main">
          <div class="wx-aqi-score-wrap">
            <div class="wx-aqi-num" id="aqi-val">--</div>
            <div>
              <div class="wx-aqi-status" id="aqi-status">ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>
              <div style="font-size:12px; color:#64748B; font-weight:600;" id="aqi-advice">US/Indian AQI ನೈಜ ಮಾಪನ</div>
            </div>
          </div>
          <div style="font-size:36px;" id="aqi-emoji">🌿</div>
        </div>
        <div class="wx-aqi-bar-track">
          <div class="wx-aqi-marker" id="aqi-marker"></div>
        </div>
        <div class="wx-aqi-subgrid">
          <div class="wx-aqi-mini">
            <div class="wx-aqi-mini-lbl">PM2.5 (µg/m³)</div>
            <div class="wx-aqi-mini-val" id="aqi-pm25">--</div>
          </div>
          <div class="wx-aqi-mini">
            <div class="wx-aqi-mini-lbl">PM10 (µg/m³)</div>
            <div class="wx-aqi-mini-val" id="aqi-pm10">--</div>
          </div>
          <div class="wx-aqi-mini">
            <div class="wx-aqi-mini-lbl">☀️ UV ಸೂಚ್ಯಂಕ</div>
            <div class="wx-aqi-mini-val" id="aqi-uv">--</div>
          </div>
        </div>
      </div>

      <!-- SUNRISE & SUNSET SOLAR ARC CARD -->
      <div class="wx-bento-card sun-card">
        <div class="wx-bento-head">
          <div class="wx-bento-title">🌅 ಸೂರ್ಯೋದಯ &amp; ಸೂರ್ಯಾಸ್ತ (Sunrise &amp; Sunset)</div>
          <span class="wx-bento-tag" style="background:#D97706;" id="sun-daylight-tag">ಹಗಲು -- ಗಂ</span>
        </div>
        <div class="wx-sun-arc-wrap">
          <svg viewBox="0 0 320 130" style="width:100%; height:auto; display:block;" aria-label="ಸೂರ್ಯೋದಯ ಮತ್ತು ಸೂರ್ಯಾಸ್ತ ಪಥ">
            <defs>
              <linearGradient id="sunArcGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#F59E0B"/>
                <stop offset="50%" stop-color="#FACC15"/>
                <stop offset="100%" stop-color="#EA580C"/>
              </linearGradient>
            </defs>
            <line x1="16" y1="112" x2="304" y2="112" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="4 4"/>
            <path d="M 28 112 A 132 100 0 0 1 292 112" fill="none" stroke="#E2E8F0" stroke-width="6" stroke-linecap="round"/>
            <path id="sunProgressArc" d="M 28 112 A 132 100 0 0 1 292 112" fill="none" stroke="url(#sunArcGrad)" stroke-width="6" stroke-linecap="round" stroke-dasharray="365" stroke-dashoffset="180"/>
            <g id="sunOrbGroup" transform="translate(160, 14)">
              <circle r="13" fill="rgba(250, 204, 21, 0.35)"/>
              <circle r="7.5" fill="#F59E0B" stroke="#FFFFFF" stroke-width="2"/>
            </g>
            <text x="28" y="126" font-size="10.5" font-weight="800" fill="#92400E" text-anchor="middle">🌅 ಸೂರ್ಯೋದಯ</text>
            <text x="292" y="126" font-size="10.5" font-weight="800" fill="#9A3412" text-anchor="middle">🌇 ಸೂರ್ಯಾಸ್ತ</text>
          </svg>
        </div>
        <div class="wx-sun-times">
          <div class="wx-sun-pill">
            <div class="wx-sun-pill-lbl">🌅 ಸೂರ್ಯೋದಯ</div>
            <div class="wx-sun-pill-val" id="sun-rise-val">06:24 AM</div>
          </div>
          <div class="wx-sun-pill">
            <div class="wx-sun-pill-lbl">☀️ ಮಧ್ಯಾಹ್ನ</div>
            <div class="wx-sun-pill-val" id="sun-noon-val">12:08 PM</div>
          </div>
          <div class="wx-sun-pill">
            <div class="wx-sun-pill-lbl">🌇 ಸೂರ್ಯಾಸ್ತ</div>
            <div class="wx-sun-pill-val" id="sun-set-val">05:52 PM</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ TOP 5 LEADERBOARDS (RAIN, MAX TEMP, MIN TEMP — KSNDMC LIVE) ═══ -->
    <div class="wx-top5-grid">
      <div class="wx-t5-card">
        <div class="wx-t5-head">
          <div class="wx-t5-title">🌧️ ಟಾಪ್-5 ಗರಿಷ್ಠ ಮಳೆ (Top 5 Rain)</div>
          <span style="font-size:11px; font-weight:800; color:#0284C7;">KSNDMC 24h</span>
        </div>
        <div class="wx-t5-list" id="top5-rain-list"></div>
      </div>

      <div class="wx-t5-card">
        <div class="wx-t5-head">
          <div class="wx-t5-title">🔥 ಟಾಪ್-5 ಗರಿಷ್ಠ ತಾಪಮಾನ (Top 5 Hot)</div>
          <span style="font-size:11px; font-weight:800; color:#DC2626;">KSNDMC Max</span>
        </div>
        <div class="wx-t5-list" id="top5-max-temp-list"></div>
      </div>

      <div class="wx-t5-card">
        <div class="wx-t5-head">
          <div class="wx-t5-title">❄️ ಟಾಪ್-5 ಕನಿಷ್ಠ ತಾಪಮಾನ (Top 5 Cold)</div>
          <span style="font-size:11px; font-weight:800; color:#2563EB;">KSNDMC Min</span>
        </div>
        <div class="wx-t5-list" id="top5-min-temp-list"></div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════
         INTERACTIVE 31-DISTRICT KARNATAKA WEATHER WARNINGS MAP (NOWCAST + 5 DAYS)
         ══════════════════════════════════════════════════════════════════ -->
    <section class="wx-section" id="district-warnings-section">
      <div class="wx-sec-header">
        <div>
          <h2 class="wx-sec-title">🗺️ ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ (IMD Nowcast &amp; 5-Day Forecast)</h2>
          <p class="wx-sec-sub">ನಕ್ಷೆಯಲ್ಲಿ ಯಾವುದೇ ಜಿಲ್ಲೆಯ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ — 3-ಗಂಟೆ ಲೈವ್ ನೌಕಾಸ್ಟ್ ಮತ್ತು ಮುಂದಿನ 5 ದಿನಗಳ ಎಚ್ಚರಿಕೆಗಳನ್ನು ನೋಡಿ.</p>
        </div>
      </div>

      <div class="wx-tablist" id="warningDayTabs" role="tablist" aria-label="ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ದಿನಗಳ ಆಯ್ಕೆ">
        <button type="button" role="tab" aria-selected="true" class="wd-tab active" onclick="switchWarningDay('Nowcast', this)">⚡ 3-ಗಂಟೆ ಲೈವ್ ನೌಕಾಸ್ಟ್</button>
        <button type="button" role="tab" aria-selected="false" class="wd-tab" onclick="switchWarningDay('Day_1', this)">📅 ಇಂದು</button>
        <button type="button" role="tab" aria-selected="false" class="wd-tab" onclick="switchWarningDay('Day_2', this)">📅 ನಾಳೆ</button>
        <button type="button" role="tab" aria-selected="false" class="wd-tab" onclick="switchWarningDay('Day_3', this)">📅 ದಿನ 3</button>
        <button type="button" role="tab" aria-selected="false" class="wd-tab" onclick="switchWarningDay('Day_4', this)">📅 ದಿನ 4</button>
        <button type="button" role="tab" aria-selected="false" class="wd-tab" onclick="switchWarningDay('Day_5', this)">📅 ದಿನ 5</button>
      </div>

      <div class="wx-severity-bar" id="severityFilterBar">
        <button type="button" class="wx-sev-pill all active-filter" data-sev="all" onclick="filterBySeverity('all', this)">🗺️ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳು <span class="wx-sev-count" id="ws-count-all">31</span></button>
        <button type="button" class="wx-sev-pill red" data-sev="red" onclick="filterBySeverity('red', this)">🔴 ಕೆಂಪು ಎಚ್ಚರಿಕೆ <span class="wx-sev-count" id="ws-count-red">0</span></button>
        <button type="button" class="wx-sev-pill orange" data-sev="orange" onclick="filterBySeverity('orange', this)">🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ <span class="wx-sev-count" id="ws-count-orange">0</span></button>
        <button type="button" class="wx-sev-pill yellow" data-sev="yellow" onclick="filterBySeverity('yellow', this)">🟡 ಹಳದಿ ನಿಗಾ <span class="wx-sev-count" id="ws-count-yellow">0</span></button>
        <button type="button" class="wx-sev-pill green" data-sev="green" onclick="filterBySeverity('green', this)">🟢 ಸಾಮಾನ್ಯ <span class="wx-sev-count" id="ws-count-green">31</span></button>
      </div>

      <div class="wx-map-layout">
        <div class="wx-map-stage" id="karnata-weather-map">
          <div class="wx-map-stage-head">
            <span class="wx-map-tab-tag" id="map-active-tab-label">⚡ 3-ಗಂಟೆ ಲೈವ್ ನೌಕಾಸ್ಟ್</span>
            <span class="wx-map-hint">👆 ಜಿಲ್ಲೆಯ ಮೇಲೆ ಟ್ಯಾಪ್/ಕ್ಲಿಕ್ ಮಾಡಿ</span>
          </div>
          {svg_map}
          <div class="wx-map-tooltip" id="wxMapTooltip" aria-hidden="true"></div>
          <div class="wx-map-legend">
            <span class="wx-leg-item"><span class="wx-leg-swatch" style="background:#EF4444;"></span> ಕೆಂಪು (Red Alert)</span>
            <span class="wx-leg-item"><span class="wx-leg-swatch" style="background:#F97316;"></span> ಕಿತ್ತಳೆ (Orange Alert)</span>
            <span class="wx-leg-item"><span class="wx-leg-swatch" style="background:#FACC15;"></span> ಹಳದಿ (Yellow Watch)</span>
            <span class="wx-leg-item"><span class="wx-leg-swatch" style="background:#4ADE80;"></span> ಸಾಮಾನ್ಯ (No Warning)</span>
          </div>
        </div>

        <div class="wx-inspector">
          <div class="wx-insp-card" id="districtInspectorCard">
            <div class="wx-insp-head">
              <div>
                <div class="wx-insp-dist-kn" id="insp-name-kn">ಬೆಂಗಳೂರು ನಗರ</div>
                <div class="wx-insp-dist-en" id="insp-name-en">Bengaluru Urban · ದಕ್ಷಿಣ ಒಳನಾಡು</div>
              </div>
              <span class="wx-insp-badge green" id="insp-badge">🟢 ಸಾಮಾನ್ಯ</span>
            </div>
            <div class="wx-insp-advice" id="insp-advice">ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).</div>
            <div class="wx-insp-mini-grid">
              <div class="wx-insp-mini">
                <div class="wx-insp-mini-lbl">🌡️ ತಾಪಮಾನ</div>
                <div class="wx-insp-mini-val" id="insp-temp">--°C</div>
              </div>
              <div class="wx-insp-mini">
                <div class="wx-insp-mini-lbl">💧 ತೇವಾಂಶ</div>
                <div class="wx-insp-mini-val" id="insp-hum">--%</div>
              </div>
              <div class="wx-insp-mini">
                <div class="wx-insp-mini-lbl">🌧️ ಮಳೆ ಸಾಧ್ಯತೆ</div>
                <div class="wx-insp-mini-val" id="insp-rain">--%</div>
              </div>
            </div>
            <div class="wx-5d-strip-title">📅 ಈ ಜಿಲ್ಲೆಯ ನೌಕಾಸ್ಟ್ &amp; 5 ದಿನಗಳ ಎಚ್ಚರಿಕೆ ವಿವರ:</div>
            <div class="wx-5d-strip" id="insp-5d-strip"></div>
          </div>

          <div class="wx-active-alerts-box">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <strong style="font-size:14px; color:#0F172A;">🚨 ಈ ಅವಧಿಯಲ್ಲಿ ಎಚ್ಚರಿಕೆ ಇರುವ ಜಿಲ್ಲೆಗಳು</strong>
              <span id="active-alerts-count-lbl" style="font-size:12px; font-weight:800; color:#DC2626;">0 ಜಿಲ್ಲೆಗಳು</span>
            </div>
            <div class="wx-active-alerts-list" id="active-alerts-list">
              <span style="font-size:12.5px; color:#15803D; font-weight:700;">✅ ಪ್ರಸ್ತುತ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಶಾಂತ ವಾತಾವರಣವಿದೆ.</span>
            </div>
          </div>
        </div>
      </div>

      <div class="wx-filter-row">
        <div class="wx-region-pills" id="warningRegionTabs">
          <button type="button" class="wx-reg-btn active" onclick="filterWarningRegion('all', this)">ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು</button>
          <button type="button" class="wx-reg-btn" onclick="filterWarningRegion('coastal', this)">🌊 ಕರಾವಳಿ</button>
          <button type="button" class="wx-reg-btn" onclick="filterWarningRegion('malnad', this)">⛰️ ಮಲೆನಾಡು</button>
          <button type="button" class="wx-reg-btn" onclick="filterWarningRegion('south', this)">🏙️ ದಕ್ಷಿಣ ಒಳನಾಡು</button>
          <button type="button" class="wx-reg-btn" onclick="filterWarningRegion('central', this)">🌾 ಮಧ್ಯ ಕರ್ನಾಟಕ</button>
          <button type="button" class="wx-reg-btn" onclick="filterWarningRegion('north', this)">☀️ ಉತ್ತರ ಒಳನಾಡು</button>
        </div>
        <input type="search" id="district-search" class="wx-search-input" placeholder="🔍 ಜಿಲ್ಲೆ ಹುಡುಕಿ (ಉದಾ: ಮೈಸೂರು, ಉಡುಪಿ)..." oninput="renderWarningCards()">
      </div>
      <div class="dw-grid" id="district-warnings-grid"></div>
    </section>

    <!-- ═══ 24-HOUR HOURLY FORECAST ═══ -->
    <section class="wx-section">
      <div class="wx-sec-header">
        <div>
          <h2 class="wx-sec-title" id="hourly-title">🕒 ಮುಂದಿನ 24 ಗಂಟೆಗಳ ಹವಾಮಾನ (Hourly Forecast)</h2>
          <p class="wx-sec-sub">ನಿಮ್ಮ ಸ್ಥಳ ಅಥವಾ ಆಯ್ಕೆಮಾಡಿದ ಜಿಲ್ಲೆಯ ಗಂಟೆವಾರು ತಾಪಮಾನ ಮತ್ತು ಮಳೆ ಸಾಧ್ಯತೆ.</p>
        </div>
      </div>
      <div class="wx-hscroll" id="hourly-scroll"></div>
    </section>

    <!-- ═══ 7-DAY FORECAST ═══ -->
    <section class="wx-section">
      <div class="wx-sec-header">
        <div>
          <h2 class="wx-sec-title" id="forecast-title">📅 ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (7-Day Outlook)</h2>
          <p class="wx-sec-sub">ಗರಿಷ್ಠ/ಕನಿಷ್ಠ ತಾಪಮಾನ ಮತ್ತು ದೈನಂದಿನ ಮಳೆ ಮುನ್ಸೂಚನೆ.</p>
        </div>
      </div>
      <div class="forecast-horizontal-scroll" id="forecast-h-scroll"></div>
    </section>

    <!-- ═══ ALL 31 DISTRICTS LIVE TELEMETRY OVERVIEW ═══ -->
    <section class="wx-section">
      <div class="wx-sec-header">
        <div>
          <h2 class="wx-sec-title">🌡️ ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ತಾಪಮಾನ &amp; ಮಳೆ</h2>
          <p class="wx-sec-sub">ಯಾವುದೇ ಜಿಲ್ಲೆಯ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ ಅದರ ಸಂಪೂರ್ಣ ಹವಾಮಾನ, AQI, ಸೂರ್ಯೋದಯ ಮತ್ತು ಎಚ್ಚರಿಕೆಗಳನ್ನು ನೋಡಿ.</p>
        </div>
      </div>
      <div class="wx-dist-telemetry-grid" id="district-grid"></div>
    </section>

    <!-- ═══ EDITORIAL KANNADA WEATHER ARTICLE & SCIENTIFIC GUIDE ═══ -->
    <article class="wx-article" id="weather-editorial-article">
      <h2>📚 ಕರ್ನಾಟಕ ಹವಾಮಾನ ಮಾರ್ಗದರ್ಶಿ — IMD ಎಚ್ಚರಿಕೆಗಳು, AQI, KSNDMC ಮಳೆ ಮಾಪನ &amp; ಕೃಷಿ ಸಲಹೆ</h2>
      <p>
        ಕರ್ನಾಟಕವು ಭೌಗೋಳಿಕವಾಗಿ ಅತ್ಯಂತ ವೈವಿಧ್ಯಮಯ ಹವಾಮಾನ ವಲಯಗಳನ್ನು ಹೊಂದಿರುವ ರಾಜ್ಯವಾಗಿದೆ. ಪಶ್ಚಿಮದಲ್ಲಿ ಅರಬ್ಬೀ ಸಮುದ್ರದ ತೀರದ <strong>ಕರಾವಳಿ (Coastal)</strong>, ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ದಟ್ಟ ಅರಣ್ಯದ <strong>ಮಲೆನಾಡು (Malnad)</strong>, ಮಧ್ಯಮ ತಾಪಮಾನದ <strong>ದಕ್ಷಿಣ ಒಳನಾಡು (South Interior)</strong> ಮತ್ತು ಬಿಸಿಲು ಹೆಚ್ಚಿರುವ <strong>ಉತ್ತರ ಒಳನಾಡು (North Interior)</strong> — ಹೀಗೆ ಪ್ರತಿಯೊಂದು ಪ್ರದೇಶದಲ್ಲೂ ಮಳೆ, ತಾಪಮಾನ ಮತ್ತು ಗಾಳಿಯ ವೇಗ ಭಿನ್ನವಾಗಿರುತ್ತದೆ. <strong>Karnata.in</strong> ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೀವು ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ (IMD Bengaluru) ಹಾಗೂ ಕರ್ನಾಟಕ ರಾಜ್ಯ ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಉಸ್ತುವಾರಿ ಕೇಂದ್ರದ (KSNDMC) ಅಧಿಕೃತ ದತ್ತಾಂಶವನ್ನು ಪ್ರತಿ 30 ನಿಮಿಷಕ್ಕೊಮ್ಮೆ ಲೈವ್ ಆಗಿ ವೀಕ್ಷಿಸಬಹುದು.
      </p>

      <h3>🚨 IMD ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಬಣ್ಣಗಳ ಅರ್ಥವೇನು? (Red, Orange, Yellow, Green Alert)</h3>
      <div class="wx-article-grid">
        <div class="wx-art-box" style="border-left:4px solid #EF4444;">
          <strong>🔴 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert — Take Action)</strong>
          <span>24 ಗಂಟೆಗಳಲ್ಲಿ 204.5 mm ಗಿಂತ ಹೆಚ್ಚು ಅತಿ ಭಾರೀ ಮಳೆ, ಭೂಕುಸಿತ ಅಥವಾ ಪ್ರವಾಹದ ಗಂಭೀರ ಅಪಾಯ. ಅನಗತ್ಯ ಪ್ರಯಾಣವನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತಪ್ಪಿಸಿ ಸುರಕ್ಷಿತ ಸ್ಥಳಗಳಲ್ಲಿರಿ.</span>
        </div>
        <div class="wx-art-box" style="border-left:4px solid #F97316;">
          <strong>🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert — Be Prepared)</strong>
          <span>115.6 mm ರಿಂದ 204.4 mm ವರೆಗೆ ಭಾರೀ ಮಳೆ ಮತ್ತು ಗುಡುಗು-ಬಿರುಗಾಳಿ ಸಾಧ್ಯತೆ. ತಗ್ಗು ಪ್ರದೇಶಗಳ ನಿವಾಸಿಗಳು ಮತ್ತು ರೈತರು ಮುಂಜಾಗ್ರತಾ ಕ್ರಮ ವಹಿಸಬೇಕು.</span>
        </div>
        <div class="wx-art-box" style="border-left:4px solid #EAB308;">
          <strong>🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch — Be Aware)</strong>
          <span>64.5 mm ರಿಂದ 115.5 mm ವರೆಗೆ ಸಾಧಾರಣದಿಂದ ಭಾರೀ ಮಳೆ ಸಂಭವ. ಹವಾಮಾನದ ಬದಲಾವಣೆಗಳ ಮೇಲೆ ನಿರಂತರ ಗಮನವಿರಲಿ.</span>
        </div>
        <div class="wx-art-box" style="border-left:4px solid #22C55E;">
          <strong>🟢 ಹಸಿರು (Green — No Warning)</strong>
          <span>ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ. ಕೃಷಿ ಚಟುವಟಿಕೆಗಳು ಮತ್ತು ಪ್ರಯಾಣಕ್ಕೆ ಅನುಕೂಲಕರ ಶಾಂತ ವಾತಾವರಣ.</span>
        </div>
      </div>

      <h3>🍃 ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (AQI) ಮತ್ತು ಆರೋಗ್ಯ ಸುರಕ್ಷತೆ</h3>
      <p>
        ನಗರ ಪ್ರದೇಶಗಳಲ್ಲಿ ವಾಯು ಮಾಲಿನ್ಯದ ಪ್ರಮಾಣವನ್ನು ಅಳೆಯಲು <strong>AQI (Air Quality Index)</strong> ಬಳಸಲಾಗುತ್ತದೆ. ವಿಶೇಷವಾಗಿ PM2.5 ಮತ್ತು PM10 ಸೂಕ್ಷ್ಮ ಧೂಳಿನ ಕಣಗಳು ಉಸಿರಾಟದ ಆರೋಗ್ಯದ ಮೇಲೆ ನೇರ ಪರಿಣಾಮ ಬೀರುತ್ತವೆ:
      </p>
      <table class="wx-aqi-table">
        <thead>
          <tr><th>AQI ಮಟ್ಟ</th><th>ವರ್ಗ (Category)</th><th>ಆರೋಗ್ಯ ಸಲಹೆ (Health Advisory)</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>0 – 50</strong></td><td style="color:#15803D; font-weight:800;">🟢 ಉತ್ತಮ (Good)</td><td>ಶುದ್ಧ ಗಾಳಿ — ಹೊರಾಂಗಣ ವ್ಯಾಯಾಮ ಮತ್ತು ನಡಿಗೆಗೆ ಅತ್ಯುತ್ತಮ.</td></tr>
          <tr><td><strong>51 – 100</strong></td><td style="color:#A16207; font-weight:800;">🟡 ಮಧ್ಯಮ (Moderate)</td><td>ಸಾಮಾನ್ಯ ಜನರಿಗೆ ಸುರಕ್ಷಿತ; ಅಸ್ತಮಾ ಇರುವವರು ಎಚ್ಚರಿಕೆ ವಹಿಸಿ.</td></tr>
          <tr><td><strong>101 – 200</strong></td><td style="color:#C2410C; font-weight:800;">🟠 ಅನಾರೋಗ್ಯಕರ (Poor)</td><td>ಮಕ್ಕಳು, ವೃದ್ಧರು ಮತ್ತು ಶ್ವಾಸಕೋಶ ಸಮಸ್ಯೆ ಇರುವವರು ಮಾಸ್ಕ್ ಬಳಸಿ.</td></tr>
          <tr><td><strong>201+</strong></td><td style="color:#B91C1C; font-weight:800;">🔴 ಅಪಾಯಕಾರಿ (Very Poor)</td><td>ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆ ಕಡಿಮೆ ಮಾಡಿ, N95 ಮಾಸ್ಕ್ ಧರಿಸಿ.</td></tr>
        </tbody>
      </table>

      <h3>🌾 ಕರ್ನಾಟಕದ ರೈತರಿಗೆ KSNDMC ಮಳೆ ಮಾಪನ &amp; ಸೂರ್ಯೋದಯ ಸಮಯದ ಮಹತ್ವ</h3>
      <p>
        ಕರ್ನಾಟಕದ ಪ್ರತಿಯೊಂದು ಗ್ರಾಮ ಪಂಚಾಯತಿ ಮಟ್ಟದಲ್ಲೂ KSNDMC ಸ್ವಯಂಚಾಲಿತ ಮಳೆ ಮಾಪನ ಕೇಂದ್ರಗಳನ್ನು (Telemetric Rain Gauges) ಸ್ಥಾಪಿಸಿದೆ. ಈ ಪುಟದಲ್ಲಿ ಕಾಣಿಸುವ <strong>ಟಾಪ್-5 ಮಳೆ ಮತ್ತು ತಾಪಮಾನ ದಾಖಲೆಗಳು</strong> ನೇರವಾಗಿ KSNDMC ಅಧಿಕೃತ ಜಾಲತಾಣದಿಂದ ಪಡೆಯಲಾದ ನಿಖರ ಅಂಕಿ-ಅಂಶಗಳಾಗಿವೆ. ಬೆಳಿಗ್ಗೆ ಸೂರ್ಯೋದಯದ ನಂತರ ಮತ್ತು ಸೂರ್ಯಾಸ್ತದ ಮುನ್ನ ಔಷಧ ಸಿಂಪಡಣೆ, ಬಿತ್ತನೆ ಹಾಗೂ ಕೊಯ್ಲು ಯೋಜನೆ ರೂಪಿಸಲು 24-ಗಂಟೆ ಗಂಟೆವಾರು ಮಳೆ ಮುನ್ಸೂಚನೆ ಮತ್ತು 3-ಗಂಟೆ IMD ನೌಕಾಸ್ಟ್ ರೈತರಿಗೆ ಅತ್ಯಂತ ಉಪಯುಕ್ತವಾಗಿದೆ.
      </p>
    </article>
  </main>

  <div id="site-footer"></div>
  <script src="/footer-component.js"></script>
  <script src="/assets/js/karnata-push-client.js"></script>

  <script>
    window.districtWarnings5D = {{}};
    const KA_DISTRICT_COORDS = {coords_json};
    let WEATHER_DATA = null;
    let ACTIVE_DAY = 'Nowcast';
    let ACTIVE_SEVERITY = 'all';
    let ACTIVE_REGION = 'all';
    let SELECTED_DISTRICT = 'bengaluru_urban';
    let CUSTOM_GEO_LABEL = null;

    const REGION_LABELS_KN = {{
      coastal: 'ಕರಾವಳಿ', malnad: 'ಮಲೆನಾಡು', south: 'ದಕ್ಷಿಣ ಒಳನಾಡು',
      central: 'ಮಧ್ಯ ಕರ್ನಾಟಕ', north: 'ಉತ್ತರ ಒಳನಾಡು'
    }};
    const DAY_ORDER = ['Nowcast', 'Day_1', 'Day_2', 'Day_3', 'Day_4', 'Day_5'];
    const WMO_KN = {{
      0: ['ಶುಭ ಹವಾಮಾನ ☀️', '☀️'], 1: ['ಹೆಚ್ಚಾಗಿ ಶುಭ 🌤️', '🌤️'], 2: ['ಭಾಗಶಃ ಮೋಡ ⛅', '⛅'],
      3: ['ಮೋಡ ಕವಿದ ವಾತಾವರಣ ☁️', '☁️'], 45: ['ಮಂಜು 🌫️', '🌫️'], 48: ['ದಟ್ಟ ಮಂಜು 🌫️', '🌫️'],
      51: ['ಹಗುರ ತುಂತುರು 🌦️', '🌦️'], 53: ['ಮಧ್ಯಮ ತುಂತುರು 🌦️', '🌦️'], 55: ['ಭಾರೀ ತುಂತುರು 🌧️', '🌧️'],
      61: ['ಹಗುರ ಮಳೆ 🌧️', '🌧️'], 63: ['ಮಧ್ಯಮ ಮಳೆ 🌧️', '🌧️'], 65: ['ಭಾರೀ ಮಳೆ 🌧️', '🌧️'],
      80: ['ಮಳೆ ಸಾಧ್ಯತೆ 🌦️', '🌦️'], 81: ['ಸಾಧಾರಣ ಮಳೆ 🌧️', '🌧️'], 82: ['ಭಾರೀ ಮಳೆ 🌧️', '🌧️'],
      95: ['ಗುಡುಗು ಮಳೆ ⛈️', '⛈️'], 96: ['ಆಲಿಕಲ್ಲು ಮಳೆ ⛈️', '⛈️'], 99: ['ತೀವ್ರ ಗುಡುಗು ⚠️⛈️', '⛈️']
    }};
    const KN_DAYS = ['ಭಾನು', 'ಸೋಮ', 'ಮಂಗಳ', 'ಬುಧ', 'ಗುರು', 'ಶುಕ್ರ', 'ಶನಿ'];

    function decodeWeatherPayload(raw) {{
      if (raw && raw.payload && typeof raw.payload === 'string') {{
        const key = 'NK_SECURE_KEY_2026_KARNATA';
        const binStr = atob(raw.payload);
        const bytes = new Uint8Array(binStr.length);
        for (let i = 0; i < binStr.length; i++) bytes[i] = binStr.charCodeAt(i) ^ key.charCodeAt(i % key.length);
        return JSON.parse(new TextDecoder('utf-8').decode(bytes));
      }}
      return raw;
    }}

    function findNearestKarnatakaDistrict(lat, lon) {{
      let bestKey = 'bengaluru_urban';
      let bestDist = Infinity;
      for (const [k, c] of Object.entries(KA_DISTRICT_COORDS)) {{
        const d = Math.hypot(lat - c.lat, lon - c.lon);
        if (d < bestDist) {{ bestDist = d; bestKey = k; }}
      }}
      return bestKey;
    }}

    function formatTime12h(isoStr) {{
      if (!isoStr) return '--:--';
      const part = isoStr.includes('T') ? isoStr.split('T')[1].slice(0, 5) : isoStr.slice(0, 5);
      const [hRaw, mRaw] = part.split(':').map(Number);
      const ampm = hRaw >= 12 ? 'PM' : 'AM';
      const h12 = (hRaw % 12) || 12;
      return `${{String(h12).padStart(2, '0')}}:${{String(mRaw).padStart(2, '0')}} ${{ampm}}`;
    }}

    function updateSunArc(sunriseIso, sunsetIso) {{
      if (!sunriseIso || !sunsetIso) return;
      document.getElementById('sun-rise-val').textContent = formatTime12h(sunriseIso);
      document.getElementById('sun-set-val').textContent = formatTime12h(sunsetIso);

      const sr = new Date(sunriseIso);
      const ss = new Date(sunsetIso);
      if (isNaN(sr) || isNaN(ss)) return;

      const midMs = (sr.getTime() + ss.getTime()) / 2;
      const midDate = new Date(midMs);
      const noonIso = `${{String(midDate.getHours()).padStart(2,'0')}}:${{String(midDate.getMinutes()).padStart(2,'0')}}`;
      document.getElementById('sun-noon-val').textContent = formatTime12h(noonIso);

      const diffMin = Math.max(0, Math.round((ss - sr) / 60000));
      const hrs = Math.floor(diffMin / 60);
      const mins = diffMin % 60;
      document.getElementById('sun-daylight-tag').textContent = `ಹಗಲು ${{hrs}} ಗಂ ${{mins}} ನಿ`;

      const now = Date.now();
      const pct = Math.max(0, Math.min(1, (now - sr.getTime()) / Math.max(1, ss.getTime() - sr.getTime())));
      const arc = document.getElementById('sunProgressArc');
      if (arc) arc.setAttribute('stroke-dashoffset', String(Math.round(365 * (1 - pct))));

      const angle = Math.PI * (1 - pct);
      const cx = 160 + 132 * Math.cos(angle);
      const cy = 112 - 100 * Math.sin(angle);
      const orb = document.getElementById('sunOrbGroup');
      if (orb) orb.setAttribute('transform', `translate(${{cx.toFixed(1)}}, ${{cy.toFixed(1)}})`);
    }}

    async function fetchLiveAqiAndSun(lat, lon, labelKn) {{
      if (labelKn) document.getElementById('aqi-loc-tag').textContent = labelKn;
      try {{
        const aqiUrl = `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=${{lat}}&longitude=${{lon}}&current=us_aqi,pm2_5,pm10,uv_index&timezone=auto`;
        const r = await fetch(aqiUrl);
        if (r.ok) {{
          const data = await r.json();
          const c = data.current || {{}};
          const aqi = Math.round(c.us_aqi ?? 42);
          const pm25 = c.pm2_5 != null ? Number(c.pm2_5).toFixed(1) : '--';
          const pm10 = c.pm10 != null ? Number(c.pm10).toFixed(1) : '--';
          const uv = c.uv_index != null ? Number(c.uv_index).toFixed(1) : '--';

          let status = 'ಉತ್ತಮ (Good)', color = '#16A34A', emoji = '🌿', advice = 'ಶುದ್ಧ ಗಾಳಿ — ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆಗೆ ಅತ್ಯುತ್ತಮ';
          if (aqi > 200) {{ status = 'ಅಪಾಯಕಾರಿ (Very Poor)'; color = '#B91C1C'; emoji = '😷'; advice = 'ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆ ಕಡಿಮೆ ಮಾಡಿ, ಮಾಸ್ಕ್ ಧರಿಸಿ'; }}
          else if (aqi > 150) {{ status = 'ಅನಾರೋಗ್ಯಕರ (Unhealthy)'; color = '#DC2626'; emoji = '⚠️'; advice = 'ಸೂಕ್ಷ್ಮ ಆರೋಗ್ಯದವರು ಎಚ್ಚರಿಕೆ ವಹಿಸಿ'; }}
          else if (aqi > 100) {{ status = 'ಸಾಧಾರಣ ಕೆಟ್ಟ (Moderate-Poor)'; color = '#EA580C'; emoji = '🟠'; advice = 'ಅಸ್ತಮಾ ಇರುವವರು ಮಾಸ್ಕ್ ಬಳಸುವುದು ಉತ್ತಮ'; }}
          else if (aqi > 50) {{ status = 'ಮಧ್ಯಮ (Moderate)'; color = '#CA8A04'; emoji = '🌤️'; advice = 'ಸಾಮಾನ್ಯ ಜನರಿಗೆ ಸುರಕ್ಷಿತ ವಾತಾವರಣ'; }}

          const numEl = document.getElementById('aqi-val');
          numEl.textContent = aqi;
          numEl.style.color = color;
          const stEl = document.getElementById('aqi-status');
          stEl.textContent = status;
          stEl.style.color = color;
          document.getElementById('aqi-emoji').textContent = emoji;
          document.getElementById('aqi-advice').textContent = advice;
          document.getElementById('aqi-pm25').textContent = pm25;
          document.getElementById('aqi-pm10').textContent = pm10;
          document.getElementById('aqi-uv').textContent = uv;
          const marker = document.getElementById('aqi-marker');
          if (marker) marker.style.left = Math.max(4, Math.min(96, (aqi / 300) * 100)) + '%';
        }}
      }} catch (e) {{ console.warn('AQI fetch notice:', e); }}

      try {{
        const sunUrl = `https://api.open-meteo.com/v1/forecast?latitude=${{lat}}&longitude=${{lon}}&daily=sunrise,sunset&forecast_days=1&timezone=auto`;
        const sr = await fetch(sunUrl);
        if (sr.ok) {{
          const sd = await sr.json();
          const rises = sd.daily?.sunrise || [];
          const sets = sd.daily?.sunset || [];
          if (rises[0] && sets[0]) updateSunArc(rises[0], sets[0]);
        }}
      }} catch (e) {{ console.warn('Sun fetch notice:', e); }}
    }}

    async function fetchHyperLocalWeather(lat, lon, placeLabel) {{
      try {{
        const url = `https://api.open-meteo.com/v1/forecast?latitude=${{lat}}&longitude=${{lon}}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,precipitation_probability&hourly=temperature_2m,precipitation_probability,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset&forecast_days=7&timezone=auto`;
        const res = await fetch(url);
        if (!res.ok) return;
        const data = await res.json();
        const cur = data.current || {{}};
        const wmo = WMO_KN[cur.weather_code] || ['ಭಾಗಶಃ ಮೋಡ ⛅', '⛅'];

        document.getElementById('hero-temp').textContent = `${{Number(cur.temperature_2m ?? 24).toFixed(1)}}°C`;
        document.getElementById('hero-desc').textContent = wmo[0];
        document.getElementById('hero-loc').textContent = `📍 ${{placeLabel}}`;
        document.getElementById('hero-feels').textContent = `${{Number(cur.apparent_temperature ?? cur.temperature_2m ?? 24).toFixed(1)}}°C`;
        document.getElementById('hero-humidity').textContent = `${{cur.relative_humidity_2m ?? '--'}}%`;
        document.getElementById('hero-wind').textContent = `${{Number(cur.wind_speed_10m ?? 0).toFixed(1)}} km/h`;
        document.getElementById('hero-rain').textContent = `${{Number(cur.precipitation ?? 0).toFixed(1)}} mm`;

        if (data.daily?.sunrise?.[0] && data.daily?.sunset?.[0]) {{
          updateSunArc(data.daily.sunrise[0], data.daily.sunset[0]);
        }}

        // Render 24h Hourly for exact user location
        const hBox = document.getElementById('hourly-scroll');
        const hTitle = document.getElementById('hourly-title');
        if (hTitle) hTitle.textContent = `🕒 ${{placeLabel}} — ಮುಂದಿನ 24 ಗಂಟೆಗಳ ಹವಾಮಾನ (Live GPS)`;
        if (hBox && data.hourly?.time) {{
          const nowH = new Date().toISOString().slice(0, 13);
          let startIdx = data.hourly.time.findIndex(t => t >= nowH);
          if (startIdx < 0) startIdx = 0;
          const cards = [];
          for (let i = startIdx; i < Math.min(startIdx + 24, data.hourly.time.length); i++) {{
            const wm = WMO_KN[data.hourly.weather_code[i]] || ['⛅', '⛅'];
            cards.push(`
              <div class="wx-hour-card ${{i === startIdx ? 'now' : ''}}">
                <div class="hi-time">${{i === startIdx ? 'ಈಗ' : data.hourly.time[i].slice(11, 16)}}</div>
                <div class="hi-icon">${{wm[1]}}</div>
                <div class="hi-temp">${{Math.round(data.hourly.temperature_2m[i])}}°</div>
                <div class="hi-rain">💧 ${{data.hourly.precipitation_probability[i] ?? 0}}%</div>
              </div>`);
          }}
          hBox.innerHTML = cards.join('');
        }}

        // Render 7-Day Forecast for exact user location
        const fBox = document.getElementById('forecast-h-scroll');
        const fTitle = document.getElementById('forecast-title');
        if (fTitle) fTitle.textContent = `📅 ${{placeLabel}} — ಮುಂದಿನ 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ (Live GPS)`;
        if (fBox && data.daily?.time) {{
          fBox.innerHTML = data.daily.time.map((dtStr, i) => {{
            const wm = WMO_KN[data.daily.weather_code[i]] || ['ಭಾಗಶಃ ಮೋಡ ⛅', '⛅'];
            const dObj = new Date(dtStr + 'T00:00:00');
            const dayLbl = i === 0 ? 'ಇಂದು' : KN_DAYS[dObj.getDay()];
            return `
              <div class="forecast-h-card ${{i === 0 ? 'today' : ''}}">
                <div class="fhc-day">${{dayLbl}}</div>
                <div class="fhc-date">${{dtStr}}</div>
                <div class="fhc-icon">${{wm[1]}}</div>
                <div class="fhc-desc">${{wm[0]}}</div>
                <div class="fhc-rain-pill">💧 ${{data.daily.precipitation_probability_max[i] ?? 0}}%</div>
                <div class="fhc-temp-row">
                  <span class="fhc-max">${{Math.round(data.daily.temperature_2m_max[i])}}°</span>
                  <span class="fhc-min">${{Math.round(data.daily.temperature_2m_min[i])}}°</span>
                </div>
              </div>`;
          }}).join('');
        }}
      }} catch (e) {{ console.warn('Hyper-local weather fetch notice:', e); }}
    }}

    async function applyCoordinatesWeather(lat, lon, sourceLabel) {{
      let placeName = sourceLabel || `${{lat.toFixed(2)}}, ${{lon.toFixed(2)}}`;
      try {{
        const rg = await fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${{lat}}&longitude=${{lon}}&localityLanguage=en`);
        if (rg.ok) {{
          const rj = await rg.json();
          const loc = rj.locality || rj.city || rj.principalSubdivision || '';
          const state = rj.principalSubdivision || '';
          if (loc) placeName = state && state !== loc ? `${{loc}}, ${{state}}` : loc;
        }}
      }} catch (e) {{}}

      CUSTOM_GEO_LABEL = placeName;
      const pill = document.getElementById('geoStatusPill');
      if (pill) pill.textContent = `📍 ನಿಮ್ಮ ಸ್ಥಳದ ಲೈವ್ ಹವಾಮಾನ: ${{placeName}} (${{sourceLabel}})`;

      // Sync nearest Karnataka district on the 31-district map too
      const nearestDist = findNearestKarnatakaDistrict(lat, lon);
      SELECTED_DISTRICT = nearestDist;
      const sel = document.getElementById('heroDistrictSelect');
      if (sel) sel.value = nearestDist;
      updateMapColors();
      renderDistrictInspector(nearestDist);

      // Fetch exact hyper-local weather, AQI & Sunrise/Sunset for the user's coordinates
      await Promise.all([
        fetchHyperLocalWeather(lat, lon, placeName),
        fetchLiveAqiAndSun(lat, lon, placeName)
      ]);
    }}

    async function detectUserLocation(explicitClick) {{
      const pill = document.getElementById('geoStatusPill');
      if (pill) pill.textContent = '📡 ನಿಮ್ಮ ನಿಖರ GPS ಸ್ಥಳ ಪತ್ತೆಹಚ್ಚಲಾಗುತ್ತಿದೆ...';

      if (navigator.geolocation) {{
        navigator.geolocation.getCurrentPosition(
          (pos) => {{
            applyCoordinatesWeather(pos.coords.latitude, pos.coords.longitude, 'GPS Live');
          }},
          async () => {{
            // Seamless IP geolocation fallback so page ALWAYS shows user's real location even without GPS prompt approval
            try {{
              const ipr = await fetch('https://ipapi.co/json/');
              if (ipr.ok) {{
                const ipd = await ipr.json();
                if (ipd.latitude && ipd.longitude) {{
                  const lbl = [ipd.city, ipd.region].filter(Boolean).join(', ') || 'Auto Location';
                  applyCoordinatesWeather(ipd.latitude, ipd.longitude, 'Auto Location');
                  return;
                }}
              }}
            }} catch (e) {{}}
            if (pill) pill.textContent = explicitClick
              ? '⚠️ GPS ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ — ಮೇಲಿನ ಪಟ್ಟಿಯಿಂದ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ.'
              : '📍 ಬೆಂಗಳೂರು ನಗರ (ಡೀಫಾಲ್ಟ್) — ನಿಖರ ಸ್ಥಳಕ್ಕಾಗಿ "ನನ್ನ ಸ್ಥಳ" ಕ್ಲಿಕ್ ಮಾಡಿ';
          }},
          {{ enableHighAccuracy: true, timeout: 7000, maximumAge: 300000 }}
        );
      }}
    }}

    function renderTop5Leaderboards(se) {{
      if (!se) return;
      const rainList = se.top_rainfall_locations || se.heavy_rain_locations || [];
      const hotList = se.top_max_temp_locations || [];
      const coldList = se.top_min_temp_locations || [];

      const rEl = document.getElementById('top5-rain-list');
      if (rEl && rainList.length) {{
        const maxR = Math.max(...rainList.map(x => Number(x.rainfall_mm ?? x.rain_mm ?? 0)), 1);
        rEl.innerHTML = rainList.slice(0, 5).map((item, i) => {{
          const val = Number(item.rainfall_mm ?? item.rain_mm ?? 0);
          const pct = Math.max(8, Math.round((val / maxR) * 100));
          return `
            <div class="wx-t5-row">
              <div class="wx-t5-row-top">
                <span class="wx-t5-rank">${{i + 1}}</span>
                <div class="wx-t5-place">
                  <span class="wx-t5-dist">${{item.district_kn || item.name_kn || item.district_en}}</span>
                  <span class="wx-t5-stn">${{item.gp_name || item.station || ''}}</span>
                </div>
                <span class="wx-t5-val rain">${{val.toFixed(1)}} mm</span>
              </div>
              <div class="wx-t5-bar"><div class="wx-t5-fill rain" style="width:${{pct}}%"></div></div>
            </div>`;
        }}).join('');
      }}

      const hEl = document.getElementById('top5-max-temp-list');
      if (hEl && hotList.length) {{
        const maxT = Math.max(...hotList.map(x => Number(x.temp_c || 0)), 40);
        hEl.innerHTML = hotList.slice(0, 5).map((item, i) => {{
          const val = Number(item.temp_c || 0);
          const pct = Math.max(15, Math.round((val / maxT) * 100));
          return `
            <div class="wx-t5-row">
              <div class="wx-t5-row-top">
                <span class="wx-t5-rank">${{i + 1}}</span>
                <div class="wx-t5-place">
                  <span class="wx-t5-dist">${{item.district_kn || item.district_en}}</span>
                  <span class="wx-t5-stn">${{item.hobli || item.station || ''}}</span>
                </div>
                <span class="wx-t5-val hot">${{val.toFixed(1)}}°C</span>
              </div>
              <div class="wx-t5-bar"><div class="wx-t5-fill hot" style="width:${{pct}}%"></div></div>
            </div>`;
        }}).join('');
      }}

      const cEl = document.getElementById('top5-min-temp-list');
      if (cEl && coldList.length) {{
        cEl.innerHTML = coldList.slice(0, 5).map((item, i) => {{
          const val = Number(item.temp_c || 0);
          const pct = Math.max(15, Math.min(100, Math.round(((30 - val) / 25) * 100)));
          return `
            <div class="wx-t5-row">
              <div class="wx-t5-row-top">
                <span class="wx-t5-rank">${{i + 1}}</span>
                <div class="wx-t5-place">
                  <span class="wx-t5-dist">${{item.district_kn || item.district_en}}</span>
                  <span class="wx-t5-stn">${{item.hobli || item.station || ''}}</span>
                </div>
                <span class="wx-t5-val cold">${{val.toFixed(1)}}°C</span>
              </div>
              <div class="wx-t5-bar"><div class="wx-t5-fill cold" style="width:${{pct}}%"></div></div>
            </div>`;
        }}).join('');
      }}
    }}

    async function initWeatherDashboard() {{
      const params = new URLSearchParams(window.location.search);
      const qDist = params.get('district');
      if (qDist) SELECTED_DISTRICT = qDist.toLowerCase();

      if (window.districtWarnings5D && window.districtWarnings5D.Nowcast) {{
        renderWarningsForDay('Nowcast');
      }}
      bindMapInteractions();

      try {{
        const res = await fetch('/data/weather.json?v=' + Date.now());
        if (res.ok) {{
          const raw = await res.json();
          WEATHER_DATA = decodeWeatherPayload(raw);
          if (WEATHER_DATA.districtWarnings5D) window.districtWarnings5D = WEATHER_DATA.districtWarnings5D;
          hydrateAllFromLiveData();
        }}
      }} catch (err) {{ console.warn('Live weather fetch notice:', err); }}

      // Auto-detect user's location unless a specific ?district= query param was explicitly passed
      if (!qDist) {{
        detectUserLocation(false);
      }}
    }}

    function hydrateAllFromLiveData() {{
      if (!WEATHER_DATA) return;
      const dists = WEATHER_DATA.districts || {{}};

      const upd = WEATHER_DATA.updated_at || WEATHER_DATA.date || '';
      const badgeEl = document.getElementById('hero-update-badge');
      if (badgeEl && upd) badgeEl.textContent = `IMD & KSNDMC ಲೈವ್ ನವೀಕರಣ: ${{upd.replace('T', ' ').slice(0, 16)}} IST`;

      const sel = document.getElementById('heroDistrictSelect');
      if (sel && Object.keys(dists).length > 0) {{
        sel.innerHTML = Object.values(dists)
          .sort((a, b) => (a.name_kn || '').localeCompare(b.name_kn || ''))
          .map(d => `<option value="${{d.key}}">${{d.name_kn}} (${{d.hq || d.key}})</option>`)
          .join('');
        if (dists[SELECTED_DISTRICT]) sel.value = SELECTED_DISTRICT;
        else SELECTED_DISTRICT = 'bengaluru_urban';
      }}

      const se = WEATHER_DATA.state_extremes || {{}};
      if (se.highest_past_24h_rain) {{
        const r = se.highest_past_24h_rain;
        document.getElementById('cc-rain-val').textContent = `${{Number(r.rain_mm || 0).toFixed(1)}} mm`;
        document.getElementById('cc-rain-loc').textContent = `${{r.name_kn || ''}} (${{r.station || ''}})`;
      }}
      if (se.max_temp_district) {{
        const mx = se.max_temp_district;
        document.getElementById('cc-max-temp-val').textContent = `${{Number(mx.temp_c || 0).toFixed(1)}}°C`;
        document.getElementById('cc-max-temp-loc').textContent = `${{mx.name_kn || ''}} (${{mx.station || ''}})`;
      }}
      if (se.min_temp_district) {{
        const mn = se.min_temp_district;
        document.getElementById('cc-min-temp-val').textContent = `${{Number(mn.temp_c || 0).toFixed(1)}}°C`;
        document.getElementById('cc-min-temp-loc').textContent = `${{mn.name_kn || ''}} (${{mn.station || ''}})`;
      }}

      renderTop5Leaderboards(se);
      renderAllDistrictsTelemetry(dists);
      renderWarningsForDay(ACTIVE_DAY);
      if (!CUSTOM_GEO_LABEL) selectDistrict(SELECTED_DISTRICT, false);
    }}

    function switchWarningDay(dayCode, btnEl) {{
      ACTIVE_DAY = dayCode;
      document.querySelectorAll('#warningDayTabs .wd-tab').forEach(t => {{
        const isSel = btnEl ? (t === btnEl) : (t.getAttribute('onclick') || '').includes(`'${{dayCode}}'`);
        t.classList.toggle('active', isSel);
        t.setAttribute('aria-selected', isSel ? 'true' : 'false');
        if (isSel) t.scrollIntoView({{ block: 'nearest', inline: 'nearest' }});
      }});
      renderWarningsForDay(dayCode);
    }}

    function filterBySeverity(sev, btnEl) {{
      ACTIVE_SEVERITY = sev;
      document.querySelectorAll('#severityFilterBar .wx-sev-pill').forEach(b => b.classList.remove('active-filter'));
      if (btnEl) btnEl.classList.add('active-filter');
      updateMapColors();
      renderWarningCards();
    }}

    function filterWarningRegion(region, btnEl) {{
      ACTIVE_REGION = region;
      document.querySelectorAll('#warningRegionTabs .wx-reg-btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      renderWarningCards();
    }}

    function renderWarningsForDay(dayCode) {{
      const dayObj = (window.districtWarnings5D || {{}})[dayCode];
      if (!dayObj) return;
      const sum = dayObj.summary || {{ red: 0, orange: 0, yellow: 0, green: 31 }};
      document.getElementById('ws-count-red').textContent = sum.red ?? 0;
      document.getElementById('ws-count-orange').textContent = sum.orange ?? 0;
      document.getElementById('ws-count-yellow').textContent = sum.yellow ?? 0;
      document.getElementById('ws-count-green').textContent = sum.green ?? 31;
      document.getElementById('ws-count-all').textContent = Object.keys(dayObj.districts || {{}}).length || 31;
      const tabLbl = document.getElementById('map-active-tab-label');
      if (tabLbl) tabLbl.textContent = dayObj.tab_label_kn || dayCode;

      updateMapColors();
      renderActiveAlertsQuickList(dayObj);
      renderDistrictInspector(SELECTED_DISTRICT);
      renderWarningCards();
    }}

    function updateMapColors() {{
      const dayObj = (window.districtWarnings5D || {{}})[ACTIVE_DAY];
      if (!dayObj || !dayObj.districts) return;
      const dMap = dayObj.districts;
      document.querySelectorAll('.ka-dist-path').forEach(path => {{
        const key = path.dataset.district;
        const info = dMap[key];
        const lvl = (info && info.level ? info.level : 'green').toLowerCase();
        path.classList.remove('level-red', 'level-orange', 'level-yellow', 'level-green', 'dimmed', 'selected');
        path.classList.add('level-' + lvl);
        if (ACTIVE_SEVERITY !== 'all' && lvl !== ACTIVE_SEVERITY) path.classList.add('dimmed');
        if (key === SELECTED_DISTRICT) path.classList.add('selected');
      }});
    }}

    function renderActiveAlertsQuickList(dayObj) {{
      const listEl = document.getElementById('active-alerts-list');
      const cntEl = document.getElementById('active-alerts-count-lbl');
      if (!listEl || !dayObj || !dayObj.districts) return;
      const alerted = Object.values(dayObj.districts).filter(d => d.level && d.level !== 'green');
      const order = {{ red: 0, orange: 1, yellow: 2 }};
      alerted.sort((a, b) => (order[a.level] ?? 9) - (order[b.level] ?? 9));
      if (cntEl) cntEl.textContent = `${{alerted.length}} ಜಿಲ್ಲೆಗಳು`;
      if (alerted.length === 0) {{
        listEl.innerHTML = '<span style="font-size:12.5px; color:#15803D; font-weight:700;">✅ ಈ ಅವಧಿಯಲ್ಲಿ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಶಾಂತ ವಾತಾವರಣವಿದೆ.</span>';
        return;
      }}
      listEl.innerHTML = alerted.map(d => {{
        const dot = d.level === 'red' ? '🔴' : (d.level === 'orange' ? '🟠' : '🟡');
        return `<button type="button" class="wx-alert-chip-btn ${{d.level}}" onclick="selectDistrict('${{d.district_key}}', false)">${{dot}} ${{d.name_kn}}</button>`;
      }}).join('');
    }}

    function renderDistrictInspector(distKey) {{
      const dayObj = (window.districtWarnings5D || {{}})[ACTIVE_DAY];
      const dWarn = dayObj && dayObj.districts ? dayObj.districts[distKey] : null;
      const dLive = WEATHER_DATA && WEATHER_DATA.districts ? WEATHER_DATA.districts[distKey] : null;

      if (dWarn) {{
        const regKn = REGION_LABELS_KN[dWarn.region] || 'ಕರ್ನಾಟಕ';
        document.getElementById('insp-name-kn').textContent = dWarn.name_kn || distKey;
        document.getElementById('insp-name-en').textContent = `${{dWarn.name_en || distKey}} · ${{regKn}}`;
        const badge = document.getElementById('insp-badge');
        badge.className = 'wx-insp-badge ' + (dWarn.level || 'green');
        badge.textContent = dWarn.level_label_kn || '🟢 ಸಾಮಾನ್ಯ';
        const adv = document.getElementById('insp-advice');
        adv.textContent = `${{dWarn.hazard_kn ? dWarn.hazard_kn + ' — ' : ''}}${{dWarn.advice_kn || ''}}`;
        adv.style.borderLeftColor = dWarn.accent_color || '#0284C7';
      }}
      if (dLive && dLive.current) {{
        document.getElementById('insp-temp').textContent = `${{dLive.current.temp_c}}°C`;
        document.getElementById('insp-hum').textContent = `${{dLive.current.humidity}}%`;
        document.getElementById('insp-rain').textContent = `${{dLive.current.rain_chance ?? dLive.current.precip_prob ?? 0}}%`;
      }}
      const strip = document.getElementById('insp-5d-strip');
      if (strip && window.districtWarnings5D) {{
        strip.innerHTML = DAY_ORDER.map(dc => {{
          const obj = window.districtWarnings5D[dc];
          if (!obj || !obj.districts || !obj.districts[distKey]) return '';
          const w = obj.districts[distKey];
          const shortDay = dc === 'Nowcast' ? '⚡ ನೌಕಾಸ್ಟ್' : (obj.tab_label_kn || dc).replace('📅 ', '');
          const icon = w.level === 'red' ? '🔴 ಕೆಂಪು' : (w.level === 'orange' ? '🟠 ಕಿತ್ತಳೆ' : (w.level === 'yellow' ? '🟡 ಹಳದಿ' : '🟢 ಸಾಮಾನ್ಯ'));
          return `<button type="button" class="wx-5d-chip ${{w.level}}" onclick="switchWarningDay('${{dc}}')"><span class="wx-5d-chip-day">${{shortDay}}</span>${{icon}}</button>`;
        }}).join('');
      }}
    }}

    function renderWarningCards() {{
      const grid = document.getElementById('district-warnings-grid');
      const dayObj = (window.districtWarnings5D || {{}})[ACTIVE_DAY];
      if (!grid || !dayObj || !dayObj.districts) return;
      const q = (document.getElementById('district-search')?.value || '').trim().toLowerCase();
      const order = {{ red: 0, orange: 1, yellow: 2, green: 3 }};
      const items = Object.values(dayObj.districts)
        .filter(d => {{
          if (ACTIVE_SEVERITY !== 'all' && d.level !== ACTIVE_SEVERITY) return false;
          if (ACTIVE_REGION !== 'all' && d.region !== ACTIVE_REGION) return false;
          if (q && !(d.name_kn || '').toLowerCase().includes(q) && !(d.name_en || '').toLowerCase().includes(q) && !(d.district_key || '').includes(q)) return false;
          return true;
        }})
        .sort((a, b) => (order[a.level] ?? 9) - (order[b.level] ?? 9));

      if (items.length === 0) {{
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:24px; color:#64748B; font-weight:700;">ಆಯ್ಕೆಮಾಡಿದ ಫಿಲ್ಟರ್‌ಗೆ ಯಾವುದೇ ಜಿಲ್ಲೆ ಕಂಡುಬಂದಿಲ್ಲ.</div>';
        return;
      }}
      grid.innerHTML = items.map(d => {{
        const regKn = REGION_LABELS_KN[d.region] || 'ಕರ್ನಾಟಕ';
        return `
          <div class="dw-card ${{d.level}}" data-district="${{d.district_key}}" onclick="selectDistrict('${{d.district_key}}', true)">
            <div>
              <div class="dw-header">
                <span class="dw-level-pill">${{d.level_label_kn}}</span>
                <span class="dw-region-tag">${{regKn}}</span>
              </div>
              <div class="dw-name-row">
                <div class="dw-name-kn">${{d.name_kn}}</div>
                <div class="dw-name-en">${{d.name_en}}</div>
              </div>
              <div class="dw-hazard-tag">${{d.hazard_kn}}</div>
            </div>
            <div class="dw-advice">ℹ️ ${{d.advice_kn}}</div>
          </div>`;
      }}).join('');
    }}

    function selectDistrict(distKey, scrollToMap) {{
      SELECTED_DISTRICT = distKey;
      CUSTOM_GEO_LABEL = null;
      const sel = document.getElementById('heroDistrictSelect');
      if (sel && sel.value !== distKey) sel.value = distKey;

      updateMapColors();
      renderDistrictInspector(distKey);

      const coord = KA_DISTRICT_COORDS[distKey];
      if (coord) {{
        fetchLiveAqiAndSun(coord.lat, coord.lon, coord.kn);
      }}

      if (WEATHER_DATA && WEATHER_DATA.districts && WEATHER_DATA.districts[distKey]) {{
        const d = WEATHER_DATA.districts[distKey];
        const c = d.current || {{}};
        document.getElementById('hero-temp').textContent = `${{c.temp_c ?? '--'}}°C`;
        document.getElementById('hero-desc').textContent = c.desc_kn || 'ಭಾಗಶಃ ಮೋಡ ⛅';
        document.getElementById('hero-loc').textContent = `📍 ${{d.name_kn}} (${{d.hq || ''}})`;
        document.getElementById('hero-feels').textContent = `${{c.feels_like_c ?? c.temp_c ?? '--'}}°C`;
        document.getElementById('hero-humidity').textContent = `${{c.humidity ?? '--'}}%`;
        document.getElementById('hero-wind').textContent = `${{c.wind_kmh ?? '--'}} km/h`;
        document.getElementById('hero-rain').textContent = `${{c.past_24h_rain_mm ?? c.precip_mm ?? 0}} mm`;

        const hTitle = document.getElementById('hourly-title');
        if (hTitle) hTitle.textContent = `🕒 ${{d.name_kn}} — ಮುಂದಿನ 24 ಗಂಟೆಗಳ ಹವಾಮಾನ (Hourly)`;
        const hBox = document.getElementById('hourly-scroll');
        if (hBox && Array.isArray(d.hourly_24h)) {{
          hBox.innerHTML = d.hourly_24h.map((h, i) => `
            <div class="wx-hour-card ${{i === 0 ? 'now' : ''}}">
              <div class="hi-time">${{i === 0 ? 'ಈಗ' : h.time}}</div>
              <div class="hi-icon">${{h.icon || '⛅'}}</div>
              <div class="hi-temp">${{Math.round(h.temp_c)}}°</div>
              <div class="hi-rain">💧 ${{h.precip_prob ?? h.rain_chance ?? 0}}%</div>
            </div>`).join('');
        }}

        const fTitle = document.getElementById('forecast-title');
        if (fTitle) fTitle.textContent = `📅 ${{d.name_kn}} — ಮುಂದಿನ 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ (7-Day Outlook)`;
        const fBox = document.getElementById('forecast-h-scroll');
        if (fBox && Array.isArray(d.forecast_7d)) {{
          fBox.innerHTML = d.forecast_7d.map((f, i) => `
            <div class="forecast-h-card ${{i === 0 ? 'today' : ''}}">
              <div class="fhc-day">${{f.day_kn || ''}}</div>
              <div class="fhc-date">${{f.date || ''}}</div>
              <div class="fhc-icon">${{f.icon || '⛅'}}</div>
              <div class="fhc-desc">${{f.desc_kn || ''}}</div>
              <div class="fhc-rain-pill">💧 ${{f.precip_prob ?? 0}}%</div>
              <div class="fhc-temp-row">
                <span class="fhc-max">${{Math.round(f.temp_max)}}°</span>
                <span class="fhc-min">${{Math.round(f.temp_min)}}°</span>
              </div>
            </div>`).join('');
        }}
      }}
      if (scrollToMap) document.getElementById('district-warnings-section')?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}

    function renderAllDistrictsTelemetry(dists) {{
      const grid = document.getElementById('district-grid');
      if (!grid) return;
      grid.innerHTML = Object.values(dists)
        .sort((a, b) => (a.name_kn || '').localeCompare(b.name_kn || ''))
        .map(d => {{
          const c = d.current || {{}};
          return `
            <div class="wx-dt-card" onclick="selectDistrict('${{d.key}}', true)">
              <div class="wx-dt-top">
                <span class="wx-dt-name">${{c.icon || '⛅'}} ${{d.name_kn}}</span>
                <span class="wx-dt-temp">${{c.temp_c ?? '--'}}°C</span>
              </div>
              <div class="wx-dt-meta">
                <span>💧 ${{c.humidity ?? '--'}}%</span>
                <span>🌧️ ${{c.rain_chance ?? c.precip_prob ?? 0}}%</span>
                <span>💨 ${{c.wind_kmh ?? '--'}} km/h</span>
              </div>
            </div>`;
        }}).join('');
    }}

    function bindMapInteractions() {{
      const stage = document.getElementById('karnata-weather-map');
      const tip = document.getElementById('wxMapTooltip');
      if (!stage || !tip) return;
      document.querySelectorAll('.ka-dist-path').forEach(path => {{
        const showTip = (ev) => {{
          const key = path.dataset.district;
          const dayObj = (window.districtWarnings5D || {{}})[ACTIVE_DAY];
          const w = dayObj && dayObj.districts ? dayObj.districts[key] : null;
          const live = WEATHER_DATA && WEATHER_DATA.districts ? WEATHER_DATA.districts[key] : null;
          const tempStr = live && live.current ? ` · 🌡️ ${{live.current.temp_c}}°C` : '';
          tip.innerHTML = `
            <div style="font-weight:900; font-size:14px; margin-bottom:2px;">${{path.dataset.nameKn}} (${{path.dataset.nameEn}})</div>
            <div style="font-weight:800; color:#FDE047;">${{w ? w.level_label_kn : '🟢 ಸಾಮಾನ್ಯ'}}${{tempStr}}</div>
            <div style="font-size:11.5px; color:#CBD5E1; margin-top:3px;">${{w ? w.hazard_kn : ''}}</div>`;
          const rect = stage.getBoundingClientRect();
          const x = Math.min(rect.width - 230, Math.max(10, (ev.clientX || rect.left + 80) - rect.left + 14));
          const y = Math.min(rect.height - 95, Math.max(10, (ev.clientY || rect.top + 80) - rect.top - 10));
          tip.style.left = x + 'px';
          tip.style.top = y + 'px';
          tip.classList.add('visible');
        }};
        path.addEventListener('mousemove', showTip);
        path.addEventListener('mouseenter', showTip);
        path.addEventListener('mouseleave', () => tip.classList.remove('visible'));
        path.addEventListener('click', () => selectDistrict(path.dataset.district, false));
        path.addEventListener('keydown', (e) => {{
          if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); selectDistrict(path.dataset.district, false); }}
        }});
      }});
    }}

    document.addEventListener('DOMContentLoaded', initWeatherDashboard);
  </script>
</body>
</html>
'''

    out_root = ROOT_DIR / "weather.html"
    out_nk = ROOT_DIR / "namma-karnataka" / "weather.html"
    out_root.write_text(html, encoding="utf-8")
    if out_nk.parent.exists():
        out_nk.write_text(html, encoding="utf-8")
    print(f"✅ Wrote upgraded creative weather.html ({len(html):,} chars) with AQI, Sunrise/Sunset, Top-5, GPS & Article!")


if __name__ == "__main__":
    build_weather_html()
