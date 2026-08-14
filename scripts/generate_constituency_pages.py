"""
Karnata — generate_constituency_pages.py
Generates standalone HTML pages in both mla/ and constituencies/ directories for all 224 Assembly Seats.
Includes full Kannada Data Normalization, 250-word Factual Kannada News Story, Sources, Update Dates, and Kannada SEO.
"""

import os
import sys
import json
import re
import base64
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DATA_PATH = ROOT_DIR / "data" / "elections_data.json"
ARTICLES_PATH = ROOT_DIR / "data" / "constituency_articles.json"
GEOJSON_PATH = ROOT_DIR / "karnataka_assembly_224.json"

MLA_DIR = ROOT_DIR / "mla"
MLA_DIR.mkdir(exist_ok=True)

CONST_DIR = ROOT_DIR / "constituencies"
CONST_DIR.mkdir(exist_ok=True)

sys.path.append(str(ROOT_DIR / "scripts"))
from kannada_dictionary import get_party_kn, get_district_kn, get_term_kn

with open(DATA_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)
    if "payload" in raw_data:
        SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"
        b_str = base64.b64decode(raw_data["payload"])
        dec_bytes = bytes([b_str[i] ^ ord(SECRET_KEY[i % len(SECRET_KEY)]) for i in range(len(b_str))])
        elections_json = json.loads(dec_bytes.decode("utf-8"))
    else:
        elections_json = raw_data

records_by_year = elections_json["records"]

articles_db = {}
if ARTICLES_PATH.exists():
    with open(ARTICLES_PATH, "r", encoding="utf-8") as f:
        raw_art = json.load(f)
        articles_db = raw_art.get("articles", {})

with open(GEOJSON_PATH, "r", encoding="utf-8") as f:
    geojson_raw = json.load(f)

constituency_history = {}
for yr_str, rec_list in records_by_year.items():
    for r in rec_list:
        ac_no = r["ac_no"]
        constituency_history.setdefault(ac_no, []).append(r)

for ac_no in constituency_history:
    constituency_history[ac_no].sort(key=lambda x: x["year"], reverse=True)

def clean_str(val):
    if not val:
        return ""
    s = str(val).lower()
    s = re.sub(r'\s*\((sc|st)\)', '', s)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

def make_slug(val):
    if not val:
        return ""
    s = str(val).lower()
    s = re.sub(r'[^a-z0-9\s_]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    if not s.endswith('_assembly_constituency'):
        s = s + '_assembly_constituency'
    return s

def get_geojson_feature(ac_no, clean_name):
    for feat in geojson_raw["features"]:
        props = feat["properties"]
        raw_ac = props.get("AC_NO") or props.get("ac_no") or props.get("AC_NUM")
        if raw_ac and int(float(str(raw_ac))) == ac_no:
            return feat
    for feat in geojson_raw["features"]:
        props = feat["properties"]
        raw_name = props.get("AC_NAME") or props.get("ac_name") or ""
        if clean_str(raw_name) == clean_name:
            return feat
    return None

def generate_constituency_page(ac_no, history_records):
    latest = history_records[0]
    name_kn = latest.get("constituency_kn") or latest.get("constituency")
    name_en = latest.get("constituency")
    district_kn = latest.get("district_kn") or get_district_kn(latest.get("district", "ಕರ್ನಾಟಕ"))
    district_en = latest.get("district", "Karnataka")
    category_kn = latest.get("category_kn", "ಸಾಮಾನ್ಯ")
    slug = latest.get("slug") or make_slug(name_en)

    feat = get_geojson_feature(ac_no, latest["clean_constituency"])
    single_geojson_str = json.dumps(feat) if feat else "null"

    party_tally = {}
    for h in history_records:
        p = h.get("winner_party_kn") or get_party_kn(h.get("winner_party"))
        party_tally[p] = party_tally.get(p, 0) + 1

    tally_chips_html = "".join([
        f'<span style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:8px; padding:6px 12px; font-size:12.5px; font-weight:800; color:#0F172A;">{p}: <span style="color:#C0392B;">{c} ಜಯ</span></span>'
        for p, c in sorted(party_tally.items(), key=lambda x: x[1], reverse=True)
    ])

    table_rows_html = ""
    for h in history_records:
        color = h.get("color", "#64748b")
        table_rows_html += f"""
        <tr>
          <td style="font-weight:900; color:#C0392B;">{h['year']}</td>
          <td style="font-weight:800; color:#0F172A;">{h.get('winner_kn', h.get('winner'))}</td>
          <td><span style="background:{color}; color:#fff; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:800; box-shadow:0 2px 4px rgba(0,0,0,0.1);">{h.get('winner_party_kn', get_party_kn(h.get('winner_party')))}</span></td>
          <td style="font-weight:700; color:#0F172A;">{h.get('winner_votes', 0):,}</td>
          <td style="color:#16A34A; font-weight:800;">{h.get('vote_share', 0.0)}%</td>
          <td style="color:#475569;">{h.get('runner_up_kn', h.get('runner_up'))} ({h.get('runner_up_party_kn', get_party_kn(h.get('runner_up_party')))})</td>
          <td style="color:#DC2626; font-weight:800;">+{h.get('margin', 0):,}</td>
        </tr>
        """

    # Fetch 250-word news article
    art_data = articles_db.get(str(ac_no), {})
    art_title = art_data.get("title_kn", f"{name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ: ಶಾಸಕ, ಚುನಾವಣೆ ಫಲಿತಾಂಶ ಮತ್ತು ಇತಿಹಾಸ")
    art_content = art_data.get("content_kn", "")
    art_word_count = art_data.get("word_count", 250)

    formatted_paragraphs = "".join([
        f'<p style="font-size:15px; line-height:1.75; color:#334155; margin-bottom:16px;">{p.strip()}</p>'
        for p in art_content.split("\n\n") if p.strip()
    ])

    seo_title = f"{name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ: ಶಾಸಕ, ಚುನಾವಣೆ ಫಲಿತಾಂಶ, ಮತ ಹಂಚಿಕೆ ಮತ್ತು ಇತಿಹಾಸ | Karnata.in"
    seo_desc = f"{name_kn} ({name_en}) ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರದ ಪ್ರಸ್ತುತ ಶಾಸಕ {latest.get('winner_kn')}, ಪಕ್ಷ {latest.get('winner_party_kn')}, ಚುನಾವಣಾ ಫಲಿತಾಂಶ, ಅಭ್ಯರ್ಥಿಗಳ ಮತಗಳು, ಗೆಲುವಿನ ಅಂತರ ಮತ್ತು 1978 ರಿಂದ 2023 ರವರೆಗಿನ ಸಂಪೂರ್ಣ ಇತಿಹಾಸ."

    page_html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{seo_title}</title>
  <meta name="description" content="{seo_desc}">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{seo_title}">
  <meta property="og:description" content="{seo_desc}">
  <meta property="og:site_name" content="Karnata.in">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Kannada:ital@0;1&family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../karnata-theme.css">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>

  <style>
    body {{
      background-color: #F8FAFC;
      color: #0F172A;
      font-family: 'Plus Jakarta Sans', 'Tiro Kannada', sans-serif;
    }}
    .hero-minimal {{
      background: #FFFFFF;
      border-bottom: 2px solid #E2E8F0;
      padding: 24px 16px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(15, 23, 42, 0.03);
    }}
    .seat-title {{
      font-family: 'Tiro Kannada', serif;
      font-size: 28px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 4px;
    }}
    .seat-subtitle {{
      font-size: 14px;
      color: #64748B;
      margin-bottom: 14px;
    }}
    .chip-bar {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .chip {{
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      padding: 5px 12px;
      border-radius: 16px;
      font-size: 12.5px;
      font-weight: 700;
      color: #0F172A;
    }}
    .grid-layout {{
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}
    @media(max-width: 900px) {{
      .grid-layout {{ grid-template-columns: 1fr; }}
    }}
    .dash-card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
      margin-bottom: 20px;
    }}
    .dash-head {{
      font-family: 'Tiro Kannada', serif;
      font-size: 20px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 16px;
      border-bottom: 2px solid #F1F5F9;
      padding-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    #constituency-map {{
      height: 360px;
      width: 100%;
      border-radius: 10px;
      border: 1px solid #CBD5E1;
      background: #F1F5F9;
    }}
    .table-wrapper {{
      overflow-x: auto;
      border-radius: 10px;
      border: 1px solid #E2E8F0;
    }}
    .elections-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .elections-table th {{
      background: #F8FAFC;
      color: #475569;
      font-weight: 800;
      padding: 10px 12px;
      border-bottom: 2px solid #E2E8F0;
      white-space: nowrap;
    }}
    .elections-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid #F1F5F9;
      white-space: nowrap;
    }}
    .elections-table tr:hover {{
      background: #F1F5F9;
    }}
    .news-badge {{
      background: #EFF6FF;
      color: #1D4ED8;
      border: 1px solid #BFDBFE;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
    }}
    .source-meta {{
      margin-top: 20px;
      padding-top: 14px;
      border-top: 1px solid #E2E8F0;
      font-size: 12.5px;
      color: #64748B;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 10px;
    }}
  </style>
</head>
<body>

  <div id="k-nav"></div>

  <header class="hero-minimal">
    <div class="wrap">
      <div style="font-size: 12px; font-weight: 800; color: #C0392B; letter-spacing: 0.05em; margin-bottom: 2px;">ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ #{ac_no} • {district_kn} ಜಿಲ್ಲೆ</div>
      <h1 class="seat-title">🏛️ {name_kn} ({name_en})</h1>
      <p class="seat-subtitle">ಕರ್ನಾಟಕ ಶಾಸನಸಭೆ ಚುನಾವಣಾ ಇತಿಹಾಸ (1978 – 2023)</p>

      <div class="chip-bar">
        <span class="chip">ವರ್ಗ: {category_kn}</span>
        <span class="chip" style="border-color:#16A34A; color:#16A34A;">2023 ಶಾಸಕರು: {latest.get('winner_kn')} ({latest.get('winner_party_kn', get_party_kn(latest.get('winner_party')))})</span>
        <span class="chip" style="border-color:#C0392B; color:#C0392B;">ಅಂತರ: +{latest.get('margin', 0):,}</span>
      </div>
    </div>
  </header>

  <main class="wrap" style="padding: 0 16px 24px;">

    <div class="grid-layout">
      <!-- MAP & WINNER SUMMARY -->
      <div>
        <div class="dash-card">
          <div class="dash-head">🗺️ ಕ್ಷೇತ್ರದ ಭೌಗೋಳಿಕ ಗಡಿ ನಕ್ಷೆ</div>
          <div id="constituency-map"></div>
        </div>

        <div class="dash-card">
          <div class="dash-head">🏆 ಪಕ್ಷಗಳ ಜಯಗಳ ಸಂಕ್ಷಿಪ್ತ ವಿವರ</div>
          <div style="display:flex; flex-wrap:wrap; gap:8px;">
            {tally_chips_html}
          </div>
        </div>
      </div>

      <!-- ELECTION HISTORY TABLE -->
      <div>
        <div class="dash-card">
          <div class="dash-head">📊 ಚುನಾವಣಾ ಇತಿಹಾಸ (1978 – 2023)</div>
          <div class="table-wrapper">
            <table class="elections-table">
              <thead>
                <tr>
                  <th>ವರ್ಷ</th>
                  <th>ವಿಜೇತ ಅಭ್ಯರ್ಥಿ</th>
                  <th>ಪಕ್ಷ</th>
                  <th>ಮತಗಳು</th>
                  <th>ಪಾಲು (%)</th>
                  <th>ಸಮೀಪದ ಸ್ಪರ್ಧಿ</th>
                  <th>ಅಂತರ</th>
                </tr>
              </thead>
              <tbody>
                {table_rows_html}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 250-WORD FACTUAL KANNADA NEWS STORY SECTION -->
    <section class="dash-card" style="margin-top: 10px;">
      <div class="dash-head">
        <span>📰 ಕ್ಷೇತ್ರದ ರಾಜಕೀಯ ಚಿತ್ರಣ</span>
        <span class="news-badge">ಕ್ಷೇತ್ರ ಮಾಹಿತಿ</span>
      </div>

      <h2 style="font-family:'Tiro Kannada', serif; font-size:22px; font-weight:800; color:#0F172A; margin-bottom:16px; line-height:1.4;">{art_title}</h2>

      <div class="article-body">
        {formatted_paragraphs}
      </div>

      <div class="source-meta">
        <div><strong>ಮಾಹಿತಿಯ ಮೂಲಗಳು:</strong> ಚುನಾವಣಾ ಆಯೋಗ, ಸಂಬಂಧಿತ ಅಧಿಕೃತ ಮೂಲಗಳು</div>
        <div><strong>ನವೀಕರಿಸಿದ ದಿನಾಂಕ:</strong> 14 ಆಗಸ್ಟ್ 2026</div>
      </div>
    </section>

  </main>

  <script src="../nav-component.js"></script>
  <script>
    const featureData = {single_geojson_str};

    if (featureData) {{
      const map = L.map('constituency-map', {{
        zoomControl: true,
        scrollWheelZoom: false
      }});

      L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png', {{
        attribution: '&copy; OpenStreetMap &copy; CARTO'
      }}).addTo(map);

      const layer = L.geoJson(featureData, {{
        style: {{
          fillColor: '{latest.get("color", "#C0392B")}',
          weight: 2,
          opacity: 1,
          color: '#C0392B',
          fillOpacity: 0.65
        }}
      }}).addTo(map);

      map.fitBounds(layer.getBounds(), {{ padding: [20, 20] }});
    }} else {{
      document.getElementById('constituency-map').innerHTML = '<div style="text-align:center; padding:50px; color:#94A3B8;">ನಕ್ಷೆಯ ಗಡಿ ವಿವರ ಲಭ್ಯವಿಲ್ಲ</div>';
    }}
  </script>
</body>
</html>"""

    # Save canonical file in mla/
    with open(MLA_DIR / f"{slug}.html", "w", encoding="utf-8") as f:
        f.write(page_html)

    # Save in constituencies/
    clean_name_slug = slug.replace('_assembly_constituency', '')
    with open(CONST_DIR / f"{clean_name_slug}.html", "w", encoding="utf-8") as f:
        f.write(page_html)
    with open(CONST_DIR / f"{ac_no}.html", "w", encoding="utf-8") as f:
        f.write(page_html)

    # Save number redirect in mla/
    num_redirect_html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={slug}.html">
  <title>{name_kn} ({name_en})</title>
</head>
<body>
  <p>Redirecting to <a href="{slug}.html">{name_kn}</a>...</p>
</body>
</html>"""

    with open(MLA_DIR / f"{ac_no}.html", "w", encoding="utf-8") as f:
        f.write(num_redirect_html)

def run():
    print(f"Generating 224 standalone constituency pages with 250-word Kannada news stories in {MLA_DIR} and {CONST_DIR}...")
    for ac_no, history_records in constituency_history.items():
        generate_constituency_page(ac_no, history_records)
    print("SUCCESS: Generated all constituency pages with news section!")

if __name__ == "__main__":
    run()
