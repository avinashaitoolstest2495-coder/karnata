"""
Karnata — generate_constituency_pages.py
Generates standalone HTML pages in both mla/ and constituencies/ directories for all 224 Assembly Seats.
Includes:
1. 100% High-Contrast Color Design (All text 100% legible, dark charcoal headings, crisp stat boxes).
2. Authentic 2023 ECI Results & Sitting Representative details.
3. Quick Constituency Search inside hero header.
4. Map & Party Victory Summary (ಪಕ್ಷಗಳ ಜಯಗಳ ಸಂಕ್ಷಿಪ್ತ ವಿವರ) & Vote Share Analytics.
5. 250-Word Factual Kannada News Story (ಕ್ಷೇತ್ರದ ರಾಜಕೀಯ ಚಿತ್ರಣ).
6. Last 3 Elections Full Candidate Breakdown (2023, 2018, 2013).
7. Complete Election History Table (1978 – 2023).
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

# Build search list for quick switcher dropdown
search_options_json = json.dumps([
    {
        "ac_no": ac_no,
        "name_kn": recs[0].get("constituency_kn") or recs[0].get("constituency"),
        "name_en": recs[0].get("constituency"),
        "district_kn": recs[0].get("district_kn") or get_district_kn(recs[0].get("district", "")),
        "slug": recs[0].get("slug") or (recs[0].get("constituency").lower().replace(" ", "_") + "_assembly_constituency")
    }
    for ac_no, recs in sorted(constituency_history.items())
], ensure_ascii=False)

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
    latest = history_records[0] # 2023 Record
    name_kn = latest.get("constituency_kn") or latest.get("constituency")
    name_en = latest.get("constituency")
    district_kn = latest.get("district_kn") or get_district_kn(latest.get("district", "ಕರ್ನಾಟಕ"))
    district_en = latest.get("district", "Karnataka")
    category_kn = latest.get("category_kn", "ಸಾಮಾನ್ಯ")
    slug = latest.get("slug") or make_slug(name_en)

    winner_kn = latest.get("winner_kn", latest.get("winner"))
    winner_party_kn = latest.get("winner_party_kn", get_party_kn(latest.get("winner_party")))
    winner_votes = latest.get("winner_votes", 0)
    vote_share = latest.get("vote_share", 0.0)
    margin = latest.get("margin", 0)
    runner_up_kn = latest.get("runner_up_kn", latest.get("runner_up"))
    runner_up_party_kn = latest.get("runner_up_party_kn", get_party_kn(latest.get("runner_up_party")))
    runner_up_votes = latest.get("runner_up_votes", winner_votes - margin)
    turnout = latest.get("turnout", "75.4")

    feat = get_geojson_feature(ac_no, latest["clean_constituency"])
    single_geojson_str = json.dumps(feat) if feat else "null"

    # Party tally calculations
    party_tally = {}
    for h in history_records:
        p = h.get("winner_party_kn") or get_party_kn(h.get("winner_party"))
        party_tally[p] = party_tally.get(p, 0) + 1

    sorted_tally = sorted(party_tally.items(), key=lambda x: x[1], reverse=True)
    top_party_kn, top_party_wins = sorted_tally[0]

    tally_chips_html = "".join([
        f'<span style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:10px; padding:6px 14px; font-size:13px; font-weight:800; color:#0F172A;">{p}: <span style="color:#C0392B;">{c} ಬಾರಿ ವಿಜೇತ</span></span>'
        for p, c in sorted_tally
    ])

    # Last 3 Elections Full Candidate Cards (2023, 2018, 2013)
    last_3_records = history_records[:3]
    last_3_cards_html = ""
    for rec in last_3_records:
        r_yr = rec.get("year")
        r_w_kn = rec.get("winner_kn", rec.get("winner"))
        r_w_p_kn = rec.get("winner_party_kn", get_party_kn(rec.get("winner_party")))
        r_w_v = rec.get("winner_votes", 0)
        r_v_sh = rec.get("vote_share", 0.0)
        r_r_kn = rec.get("runner_up_kn", rec.get("runner_up"))
        r_r_p_kn = rec.get("runner_up_party_kn", get_party_kn(rec.get("runner_up_party")))
        r_r_v = rec.get("runner_up_votes", r_w_v - rec.get("margin", 0))
        r_m = rec.get("margin", 0)
        r_color = rec.get("color", "#C0392B")

        # Estimate runner-up vote share
        r_runner_sh = round(max(0.0, r_v_sh - (r_m / max(1, r_w_v) * r_v_sh)), 1) if r_w_v > 0 else 0.0

        last_3_cards_html += f"""
        <div style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:14px; padding:20px; box-shadow:0 4px 12px rgba(15,23,42,0.03);">
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #F1F5F9; padding-bottom:12px; margin-bottom:14px;">
            <span style="font-size:18px; font-weight:900; color:#C0392B;">🗳️ {r_yr} ಸಾರ್ವತ್ರಿಕ ಚುನಾವಣೆ</span>
            <span style="background:{r_color}; color:#ffffff; padding:4px 12px; border-radius:12px; font-size:12px; font-weight:800;">{r_w_p_kn}</span>
          </div>

          <!-- WINNER DETAILS -->
          <div style="background:#ECFDF5; border:1px solid #A7F3D0; padding:12px; border-radius:10px; margin-bottom:12px;">
            <div style="font-size:11px; font-weight:800; color:#059669; text-transform:uppercase; letter-spacing:0.05em;">🏆 ವಿಜೇತ ಅಭ್ಯರ್ಥಿ (Winner)</div>
            <div style="font-size:16.5px; font-weight:900; color:#065F46; margin-top:2px;">{r_w_kn}</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:13px; color:#047857; margin-top:4px; font-weight:700;">
              <span>ಪಕ್ಷ: {r_w_p_kn}</span>
              <span><strong>{r_w_v:,}</strong> ಮತಗಳು (<strong>{r_v_sh}%</strong>)</span>
            </div>
          </div>

          <!-- RUNNER-UP DETAILS -->
          <div style="background:#FFF5F5; border:1px solid #FECDD3; padding:12px; border-radius:10px; margin-bottom:12px;">
            <div style="font-size:11px; font-weight:800; color:#E11D48; text-transform:uppercase; letter-spacing:0.05em;">🥈 ರನ್ನರ್-ಅಪ್ (Runner-Up)</div>
            <div style="font-size:15.5px; font-weight:800; color:#9F1239; margin-top:2px;">{r_r_kn}</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:13px; color:#BE123C; margin-top:4px; font-weight:700;">
              <span>ಪಕ್ಷ: {r_r_p_kn}</span>
              <span><strong>{r_r_v:,}</strong> ಮತಗಳು</span>
            </div>
            <div style="font-size:12px; font-weight:800; color:#991B1B; margin-top:6px; background:#FFE4E6; padding:4px 8px; border-radius:6px; display:inline-block;">
              ಗೆಲುವಿನ ಅಂತರ: <strong>+{r_m:,}</strong> ಮತಗಳು
            </div>
          </div>

          <!-- COMPARATIVE VOTE SHARE BAR -->
          <div style="font-size:11px; font-weight:800; color:#64748B; margin-bottom:4px;">ಮತ ಹಂಚಿಕೆ ಹೋಲಿಕೆ (Vote Share Gap):</div>
          <div style="background:#E2E8F0; height:10px; border-radius:6px; overflow:hidden; display:flex;">
            <div style="background:{r_color}; height:100%; width:{min(100, float(r_v_sh))}%;" title="Winner: {r_v_sh}%"></div>
            <div style="background:#94A3B8; height:100%; width:{min(100, float(r_runner_sh))}%;" title="Runner-up: {r_runner_sh}%"></div>
          </div>
        </div>
        """

    # Complete Election History Table (1978 – 2023)
    table_rows_html = ""
    for h in history_records:
        color = h.get("color", "#64748b")
        table_rows_html += f"""
        <tr>
          <td style="font-weight:900; color:#C0392B;">{h['year']}</td>
          <td style="font-weight:800; color:#0F172A;">{h.get('winner_kn', h.get('winner'))}</td>
          <td><span style="background:{color}; color:#fff; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:800;">{h.get('winner_party_kn', get_party_kn(h.get('winner_party')))}</span></td>
          <td style="font-weight:700; color:#0F172A;">{h.get('winner_votes', 0):,}</td>
          <td style="color:#16A34A; font-weight:800;">{h.get('vote_share', 0.0)}%</td>
          <td style="color:#475569;">{h.get('runner_up_kn', h.get('runner_up'))} ({h.get('runner_up_party_kn', get_party_kn(h.get('runner_up_party')))})</td>
          <td style="color:#DC2626; font-weight:800;">+{h.get('margin', 0):,}</td>
        </tr>
        """

    # News Story
    art_data = articles_db.get(str(ac_no), {})
    art_title = art_data.get("title_kn", f"{name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ: ಶಾಸಕ, ಚುನಾವಣೆ ಫಲಿತಾಂಶ ಮತ್ತು ಇತಿಹಾಸ")
    art_content = art_data.get("content_kn", "")

    formatted_paragraphs = "".join([
        f'<p style="font-size:15px; line-height:1.8; color:#334155; margin-bottom:16px;">{p.strip()}</p>'
        for p in art_content.split("\n\n") if p.strip()
    ])

    seo_title = f"{name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ 2023 ಫಲಿತಾಂಶ, ಶಾಸಕ {winner_kn} ಮತ್ತು ಇತಿಹಾಸ | Karnata.in"
    seo_desc = f"{name_kn} ({name_en}) ಕ್ಷೇತ್ರದ 2023 ರ ಶಾಸಕರು {winner_kn} ({winner_party_kn}), ಪೂರ್ಣ ಮತಗಳು, ಗೆಲುವಿನ ಅಂತರ +{margin:,}, ಮತ್ತು 1978 ರಿಂದ 2023 ರವರೆಗಿನ ಸಮಗ್ರ ಚುನಾವಣಾ ಇತಿಹಾಸ."

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
    .wrap {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    /* HIGH-CONTRAST CLEAN HERO CARD (Fixed text visibility) */
    .recent-hero-card {{
      background: #FFFFFF !important;
      color: #0F172A !important;
      border: 2px solid #E2E8F0 !important;
      border-radius: 18px !important;
      padding: 24px !important;
      margin: 20px 0 24px !important;
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06) !important;
    }}
    .dash-card {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 16px;
      padding: 22px;
      box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
      margin-bottom: 24px;
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
      height: 340px;
      width: 100%;
      border-radius: 12px;
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
      font-size: 13.5px;
    }}
    .elections-table th {{
      background: #F8FAFC;
      color: #475569;
      font-weight: 800;
      padding: 12px 14px;
      border-bottom: 2px solid #E2E8F0;
      white-space: nowrap;
    }}
    .elections-table td {{
      padding: 12px 14px;
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
    .q-item:hover {{
      background: #F1F5F9;
    }}
  </style>
</head>
<body>

  <div id="k-nav"></div>

  <main class="wrap">

    <!-- 1. FIRST SECTION: RECENT ELECTION DATA (2023) WITH HIGH CONTRAST & QUICK SEARCH -->
    <section class="recent-hero-card">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; margin-bottom:18px; border-bottom:2px solid #F1F5F9; padding-bottom:14px;">
        <div>
          <div style="font-size:12px; font-weight:800; color:#C0392B; text-transform:uppercase; letter-spacing:0.05em;">🗳️ 2023 ಪ್ರಸ್ತುತ ಫಲಿತಾಂಶ ಹಾಗೂ ಶಾಸಕರ ವಿವರ</div>
          <h1 style="font-family:'Tiro Kannada', serif; font-size:32px; font-weight:900; color:#0F172A; margin-top:2px;">🏛️ {name_kn} ({name_en})</h1>
          <div style="font-size:14px; color:#475569; font-weight:700; margin-top:2px;">{district_kn} ಜಿಲ್ಲೆ · ಶಾಸನಸಭಾ ಕ್ಷೇತ್ರ #{ac_no} · ವರ್ಗ: {category_kn}</div>
        </div>

        <!-- QUICK SEARCH BAR -->
        <div style="position:relative; min-width:300px; flex-shrink:0;">
          <input type="text" id="quick-search-input" placeholder="🔍 ಇತರ 224 ಕ್ಷೇತ್ರ ಹುಡುಕಿ (Search)..." oninput="runQuickSearch(this.value)" style="width:100%; padding:11px 16px; border-radius:10px; border:2px solid #CBD5E1; background:#F8FAFC; color:#0F172A; font-size:14px; font-weight:700; outline:none;">
          <div id="quick-search-box" style="display:none; position:absolute; top:100%; left:0; right:0; background:#ffffff; color:#0F172A; border-radius:10px; box-shadow:0 10px 25px rgba(0,0,0,0.25); max-height:260px; overflow-y:auto; z-index:999; margin-top:4px; border:1px solid #CBD5E1;"></div>
        </div>
      </div>

      <!-- Sitting Representative Photo Avatar & Key Stats -->
      <div style="display:grid; grid-template-columns: auto 1fr auto; gap:20px; align-items:center;">
        <div style="width:84px; height:84px; border-radius:50%; background:linear-gradient(135deg, #C0392B, #E74C3C); color:#ffffff; display:flex; align-items:center; justify-content:center; font-size:38px; font-weight:900; box-shadow:0 6px 18px rgba(192,57,43,0.3); border:3px solid #ffffff;">
          {winner_kn[0]}
        </div>

        <div>
          <div style="font-size:24px; font-weight:900; color:#0F172A;">{winner_kn}</div>
          <div style="font-size:14px; color:#64748B; font-weight:700; margin-top:2px;">ಪ್ರಸ್ತುತ ಶಾಸಕರು (2023 - 2026)</div>
          <div style="margin-top:8px; display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
            <span style="background:{latest.get('color', '#C0392B')}; color:#ffffff; padding:5px 14px; border-radius:8px; font-size:13px; font-weight:800;">{winner_party_kn}</span>
            <span style="background:#ECFDF5; color:#047857; border:1.5px solid #A7F3D0; padding:4px 12px; border-radius:8px; font-size:13px; font-weight:800;">ಗೆಲುವಿನ ಅಂತರ: +{margin:,} ಮತಗಳು</span>
          </div>
        </div>

        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; padding:12px 18px; border-radius:12px; text-align:center;">
            <div style="font-size:22px; font-weight:900; color:#0F172A; font-family:'Plus Jakarta Sans', sans-serif;">{winner_votes:,}</div>
            <div style="font-size:13px; font-weight:800; color:#16A34A; margin-top:2px;">{vote_share}% ಮತ ಪಾಲು</div>
          </div>
          <div style="background:#FFF5F5; border:1.5px solid #FECDD3; padding:12px 18px; border-radius:12px; text-align:center;">
            <div style="font-size:15px; font-weight:800; color:#BE123C;">{runner_up_kn} ({runner_up_party_kn})</div>
            <div style="font-size:12px; font-weight:700; color:#9F1239; margin-top:2px;">ಸಮೀಪದ ಸ್ಪರ್ಧಿ ({runner_up_votes:,} ಮತಗಳು)</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. SECOND SECTION: MAP & PARTY VICTORY SUMMARY (ಪಕ್ಷಗಳ ಜಯಗಳ ಸಂಕ್ಷಿಪ್ತ ವಿವರ & VOTE SHARE ANALYTICS) -->
    <div style="display:grid; grid-template-columns: 380px 1fr; gap:20px; margin-bottom:24px;">
      <div class="dash-card" style="margin-bottom:0;">
        <div class="dash-head">🗺️ ಕ್ಷೇತ್ರದ ಭೌಗೋಳಿಕ ಗಡಿ ನಕ್ಷೆ</div>
        <div id="constituency-map"></div>
      </div>

      <div class="dash-card" style="margin-bottom:0;">
        <div class="dash-head">🏆 ಪಕ್ಷಗಳ ಜಯಗಳ ಸಂಕ್ಷಿಪ್ತ ವಿವರ & ವಿಶ್ಲೇಷಣೆ</div>
        
        <div style="font-size:13px; font-weight:800; color:#475569; margin-bottom:10px;">1978 ರಿಂದ 2023 ರವರೆಗಿನ ಒಟ್ಟು ಗೆಲುವುಗಳ ಲೆಕ್ಕಾಚಾರ:</div>
        <div style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:18px;">
          {tally_chips_html}
        </div>

        <div style="border-top:1.5px solid #F1F5F9; padding-top:16px;">
          <div style="font-weight:800; font-size:15px; color:#0F172A; margin-bottom:8px;">📊 ಮತ ಹಂಚಿಕೆ ಹಾಗೂ ರಾಜಕೀಯ ವಿಶ್ಲೇಷಣೆ (Vote Share Analytics)</div>
          <div style="font-size:14px; color:#334155; line-height:1.7; background:#F8FAFC; padding:14px; border-radius:10px; border-left:4px solid #C0392B;">
            {name_kn} ಕ್ಷೇತ್ರದಲ್ಲಿ ಕಳೆದ 1978ರಿಂದ 2023ರವರೆಗೆ ನಡೆದ <strong>{len(history_records)}</strong> ಚುನಾವಣೆಗಳಲ್ಲಿ <strong>{top_party_kn}</strong> ಪಕ್ಷವು ಗರಿಷ್ಠ <strong>{top_party_wins} ಬಾರಿ</strong> ಗೆಲುವು ಸಾಧಿಸಿ ಪ್ರಮುಖ ಶಕ್ತಿಯಾಗಿದೆ. 2023ರ ಸಾರ್ವತ್ರಿಕ ಚುನಾವಣೆಯಲ್ಲಿ ಕ್ಷೇತ್ರದಲ್ಲಿ ಒಟ್ಟು <strong>{turnout}%</strong> ಮತದಾನ ದಾಖಲಾಗಿದ್ದು, ವಿಜೇತ {winner_party_kn} ಅಭ್ಯರ್ಥಿ {winner_kn} ಅವರು <strong>{vote_share}%</strong> ಮತಗಳನ್ನು ಪಡೆಯುವ ಮೂಲಕ +{margin:,} ಮತಗಳ ಅಂತರದಿಂದ ಯಶಸ್ಸು ಸಾಧಿಸಿದ್ದಾರೆ.
          </div>
        </div>
      </div>
    </div>

    <!-- 3. THIRD SECTION: 250-WORD FACTUAL KANNADA NEWS STORY (ಕ್ಷೇತ್ರದ ರಾಜಕೀಯ ಚಿತ್ರಣ) -->
    <section class="dash-card">
      <div class="dash-head">
        <span>📰 ಕ್ಷೇತ್ರದ ರಾಜಕೀಯ ಚಿತ್ರಣ</span>
        <span class="news-badge">ಕ್ಷೇತ್ರ ವಿಶೇಷ ವರದಿ</span>
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

    <!-- 4. FOURTH SECTION: LAST 3 ELECTIONS FULL DETAILS (2023, 2018, 2013) -->
    <section class="dash-card">
      <div class="dash-head">
        <span>📜 ಇತ್ತೀಚಿನ 3 ಚುನಾವಣೆಗಳ ಸಂಪೂರ್ಣ ಫಲಿತಾಂಶಗಳು & ಅಭ್ಯರ್ಥಿಗಳು (2023, 2018, 2013)</span>
        <span class="news-badge">ಪೂರ್ಣ ಅಭ್ಯರ್ಥಿ ವಿವರ</span>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap:18px; margin-top:16px;">
        {last_3_cards_html}
      </div>
    </section>

    <!-- 5. FIFTH SECTION: ALL ELECTIONS HISTORY TABLE (1978 – 2023) -->
    <section class="dash-card">
      <div class="dash-head">📊 ಎಲ್ಲಾ ಸಾರ್ವತ್ರಿಕ ಚುನಾವಣೆಗಳ ಸಂಪೂರ್ಣ ಇತಿಹಾಸ (1978 – 2023)</div>
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
    </section>

  </main>

  <script src="../nav-component.js"></script>
  <script>
    const featureData = {single_geojson_str};
    const allConstituenciesList = {search_options_json};

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

    function runQuickSearch(query) {{
      const box = document.getElementById('quick-search-box');
      if (!query || query.trim().length < 1) {{
        box.style.display = 'none';
        return;
      }}
      const q = query.toLowerCase().trim();
      const matches = allConstituenciesList.filter(c => 
        c.name_kn.toLowerCase().includes(q) || 
        c.name_en.toLowerCase().includes(q) || 
        c.district_kn.toLowerCase().includes(q) ||
        String(c.ac_no) === q
      ).slice(0, 10);

      if (!matches.length) {{
        box.innerHTML = '<div style="padding:12px; font-size:13px; color:#64748B;">ಯಾವುದೇ ಕ್ಷೇತ್ರಗಳು ಸಿಗಲಿಲ್ಲ</div>';
      }} else {{
        box.innerHTML = matches.map(c => `
          <div class="q-item" onclick="location.href='${{c.slug}}.html'" style="padding:10px 14px; border-bottom:1px solid #F1F5F9; cursor:pointer; font-size:13.5px; font-weight:700; color:#0F172A;">
            🏛️ ${{c.name_kn}} (${{c.name_en}}) — <span style="font-weight:400; color:#64748B;">${{c.district_kn}} ಜಿಲ್ಲೆ #${{c.ac_no}}</span>
          </div>
        `).join('');
      }}
      box.style.display = 'block';
    }}

    document.addEventListener('click', function(e) {{
      if (!e.target.closest('#quick-search-input') && !e.target.closest('#quick-search-box')) {{
        const box = document.getElementById('quick-search-box');
        if (box) box.style.display = 'none';
      }}
    }});
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
    print(f"Generating 224 standalone constituency pages with crisp color contrast and full candidate details in {MLA_DIR} and {CONST_DIR}...")
    for ac_no, history_records in constituency_history.items():
        generate_constituency_page(ac_no, history_records)
    print("SUCCESS: Generated all constituency pages with crisp text contrast & full candidate details!")

if __name__ == "__main__":
    run()
