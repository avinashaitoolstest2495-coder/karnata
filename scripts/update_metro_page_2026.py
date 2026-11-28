#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updates Namma Metro page (bengaluru-metro.html) and JSON data files
(data/metro_data.json, metro_data_kn.json) with November 2026 live status:
  1. Pink Line Phase-1 (Kalena Agrahara <-> Tavarekere, 7.5 km, 6 elevated stations)
     partially running since Nov 14, 2026 (inaugurated Nov 13, 2026).
  2. Accurate network KPIs: 103.65 km, 4 active lines (Purple, Green, Yellow, Pink Partial),
     91 active stations (+41 under construction), 10.5+ lakh daily riders (11.19L record).
  3. Updated BMRCL revised fare chart (₹10–₹90, Pink Line stretch ₹10–₹30, Smart Card/NCMC
     5% peak & 10% off-peak/Sunday discounts, peak/off-peak hours, ₹90 min balance).
  4. Detailed line-wise train timings & frequencies (Purple/Green/Yellow + Pink Line exact
     Mon/Tue-Sat/Sun first & last trains and 8-min peak / 10-min off-peak frequency).
  5. Updated Pink Line station status badges, Expansion Timeline, FAQPage schema, and
     editorial article.
"""
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\avina\Downloads\karnata-site-with-cms")
METRO_HTML = ROOT / "bengaluru-metro.html"
METRO_JSONS = [ROOT / "data" / "metro_data.json", ROOT / "metro_data_kn.json"]

PINK_ACTIVE_STATIONS = {
    "Kalena Agrahara",
    "Hulimavu",
    "IIMB",
    "JP Nagar 4th Phase",
    "Jayadeva Hospital",
    "Tavarekere",
}


def update_metro_json_obj(data: dict) -> dict:
    # Update Yellow line frequency
    if "yellow" in data.get("lines", {}):
        data["lines"]["yellow"]["train_interval_kn"] = "ಪ್ರತಿ 7–10 ನಿಮಿಷಕ್ಕೆ (CBTC)"
        data["lines"]["yellow"]["daily_riders_kn"] = "~1.5+ ಲಕ್ಷ"

    # Update Pink line to Partially Operational (Phase 1 Running since Nov 14, 2026)
    if "pink" in data.get("lines", {}):
        pk = data["lines"]["pink"]
        pk["terminals_kn"] = "ಕಾಳೇನ ಅಗ್ರಹಾರ ↔ ತಾವರೆಕೆರೆ (ಸಕ್ರಿಯ) · ನಾಗವಾರ (2027)"
        pk["terminals_en"] = "Kalena Agrahara ↔ Tavarekere (Running) · Nagawara (2027)"
        pk["length"] = "7.5 ಕಿ.ಮೀ ಸಕ್ರಿಯ / 21.26 ಕಿ.ಮೀ"
        pk["status_kn"] = "ಭಾಗಶಃ ಸಕ್ರಿಯ (6 ನಿಲ್ದಾಣಗಳು · ನವೆಂಬರ್ 14, 2026)"
        pk["status_en"] = "Partially Operational (6 Stations)"
        pk["status_type"] = "partial"
        pk["opened_kn"] = "ಹಂತ 1: 14 ನವೆಂಬರ್ 2026 · ಭೂಗತ: 2027"
        pk["train_interval_kn"] = "ಪೀಕ್: 8 ನಿಮಿಷ · ಆಫ್-ಪೀಕ್: 10 ನಿಮಿಷ"
        pk["daily_riders_kn"] = "ಹಂತ 1 ಸಕ್ರಿಯ"
        pk["operational_stations"] = 6
        pk["first_train_kn"] = "ಸೋಮ 04:55 AM · ಮಂಗಳ–ಶನಿ 06:00 AM · ಭಾನು 07:00 AM"
        pk["last_train_kn"] = "10:50 PM (ಕಾಳೇನ ಅಗ್ರಹಾರ) · 10:54 PM (ತಾವರೆಕೆರೆ)"
        pk["fare_range_kn"] = "₹10 – ₹30 (ಹಂತ 1)"

    # Mark each Pink Line station as operational vs under_construction
    for stn in data.get("stations", {}).get("pink", []):
        if stn.get("name_en") in PINK_ACTIVE_STATIONS:
            stn["operational"] = True
            if stn["name_en"] == "Tavarekere":
                stn["note_kn"] = "✅ ಹಂತ 1 ಉತ್ತರ ಟರ್ಮಿನಲ್ (S.G. ಪಾಳ್ಯ · ಸಕ್ರಿಯ)"
                stn["note_en"] = "Phase-1 Northern Terminus (Operational)"
            elif stn["name_en"] == "Jayadeva Hospital":
                stn["note_kn"] = "🌟 ಗುಲಾಬಿ ↔ ಹಳದಿ ಇಂಟರ್‌ಚೇಂಜ್ (ಸಕ್ರಿಯ)"
                stn["note_en"] = "Pink↔Yellow Interchange (Operational)"
            elif not stn.get("note_kn", "").startswith("✅"):
                stn["note_kn"] = f"✅ ಸಕ್ರಿಯ · {stn.get('note_kn', '')}".strip(" ·")
        else:
            stn["operational"] = False
            if not stn.get("note_kn", "").startswith("🚧"):
                stn["note_kn"] = f"🚧 ಭೂಗತ ನಿರ್ಮಾಣ (2027) · {stn.get('note_kn', '')}".strip(" ·")

    return data


def main():
    # 1. Update metro_data.json and metro_data_kn.json
    updated_metro_data = None
    for jp in METRO_JSONS:
        if jp.exists():
            obj = json.loads(jp.read_text(encoding="utf-8"))
            obj = update_metro_json_obj(obj)
            jp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
            if jp.name == "metro_data.json":
                updated_metro_data = obj
            print(f"Updated {jp.relative_to(ROOT)}")

    assert updated_metro_data is not None

    # 2. Update bengaluru-metro.html
    s = METRO_HTML.read_text(encoding="utf-8")

    # 2a. Update FAQPage JSON-LD timings & fare answers
    s = s.replace(
        "ನಮ್ಮ ಮೆಟ್ರೋ ರೈಲುಗಳು ಸೋಮವಾರದಿಂದ ಶನಿವಾರದವರೆಗೆ ಬೆಳಿಗ್ಗೆ 5:00 ರಿಂದ ರಾತ್ರಿ 11:00 ಗಂಟೆಯವರೆಗೆ ಚಲಿಸುತ್ತವೆ. ಭಾನುವಾರ ಬೆಳಿಗ್ಗೆ 7:00 ಗಂಟೆಗೆ ಮೊದಲ ರೈಲು ಆರಂಭವಾಗುತ್ತದೆ. ಪೀಕ್ ಅವಧಿಯಲ್ಲಿ ಪ್ರತಿ 3 ರಿಂದ 5 ನಿಮಿಷಕ್ಕೆ ರೈಲುಗಳು ಲಭ್ಯವಿರುತ್ತವೆ.",
        "ನೇರಳೆ, ಹಸಿರು ಮತ್ತು ಹಳದಿ ಮಾರ್ಗಗಳಲ್ಲಿ ಸೋಮವಾರ–ಶನಿವಾರ ಬೆಳಿಗ್ಗೆ 5:00 ರಿಂದ ರಾತ್ರಿ 11:00 ವರೆಗೆ (ಭಾನುವಾರ 7:00 AM) ರೈಲುಗಳು ಚಲಿಸುತ್ತವೆ. ಗುಲಾಬಿ ಮಾರ್ಗದಲ್ಲಿ (ಕಾಳೇನ ಅಗ್ರಹಾರ–ತಾವರೆಕೆರೆ) ಸೋಮವಾರ 4:55 AM, ಮಂಗಳವಾರ–ಶನಿವಾರ 6:00 AM ಮತ್ತು ಭಾನುವಾರ 7:00 AM ರಿಂದ ರಾತ್ರಿ 10:50/10:54 PM ವರೆಗೆ ಪ್ರತಿ 8–10 ನಿಮಿಷಕ್ಕೊಮ್ಮೆ ರೈಲುಗಳು ಲಭ್ಯವಿವೆ.",
    )
    s = s.replace(
        "BMRCL ಪರಿಷ್ಕೃತ ದರ ಪಟ್ಟಿಯ ಪ್ರಕಾರ ಕನಿಷ್ಠ ಟೋಕನ್ ದರ ₹10 ಮತ್ತು ಗರಿಷ್ಠ ₹90 ಇರುತ್ತದೆ. ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಮತ್ತು ಕ್ಯೂಆರ್ ಕೋಡ್ ಟಿಕೆಟ್‌ಗಳಿಗೆ ಶೇ. 5 ರಿಂದ 10 ರಷ್ಟು ರಿಯಾಯಿತಿ ದೊರೆಯುತ್ತದೆ.",
        "BMRCL ಪರಿಷ್ಕೃತ ದರ ಪಟ್ಟಿಯ ಪ್ರಕಾರ ಕನಿಷ್ಠ ಟೋಕನ್ ದರ ₹10 ಮತ್ತು ಗರಿಷ್ಠ ₹90 ಇರುತ್ತದೆ (ಗುಲಾಬಿ ಮಾರ್ಗ ಹಂತ 1: ₹10–₹30). ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ / NCMC ಬಳಕೆದಾರರಿಗೆ ಪೀಕ್ ಅವಧಿಯಲ್ಲಿ 5% ಹಾಗೂ ಆಫ್-ಪೀಕ್ ಮತ್ತು ಭಾನುವಾರ/ರಾಷ್ಟ್ರೀಯ ರಜಾದಿನಗಳಲ್ಲಿ 10% ರಿಯಾಯಿತಿ ದೊರೆಯುತ್ತದೆ.",
    )

    # 2b. Update KPI Cards
    s = s.replace('<div class="kpi-val">96.15 ಕಿ.ಮೀ</div>', '<div class="kpi-val">103.65 ಕಿ.ಮೀ</div>')
    s = s.replace(
        '<div class="kpi-sub">3 ಸಕ್ರಿಯ ಮಾರ್ಗಗಳು (Purple, Green, Yellow)</div>',
        '<div class="kpi-sub">4 ಸಕ್ರಿಯ ಮಾರ್ಗಗಳು (Purple, Green, Yellow, Pink ಭಾಗಶಃ)</div>',
    )
    s = s.replace('<div class="kpi-val">86 ಸಕ್ರಿಯ</div>', '<div class="kpi-val">91 ಸಕ್ರಿಯ</div>')
    s = s.replace(
        '<div class="kpi-sub">+46 ನಿಲ್ದಾಣಗಳು ನಿರ್ಮಾಣ ಹಂತದಲ್ಲಿವೆ</div>',
        '<div class="kpi-sub">Pink 6 ಸಕ್ರಿಯ · +41 ನಿರ್ಮಾಣ ಹಂತದಲ್ಲಿವೆ</div>',
    )
    s = s.replace('<div class="kpi-val">9.16 ಲಕ್ಷ</div>', '<div class="kpi-val">10.5+ ಲಕ್ಷ</div>')
    s = s.replace(
        '<div class="kpi-sub">ದಾಖಲೆಯ ದಿನ: 10.48 ಲಕ್ಷ (Aug 2025)</div>',
        '<div class="kpi-sub">ದಾಖಲೆಯ ದಿನ: 11.19 ಲಕ್ಷ (Aug 2026)</div>',
    )

    # 2c. Update Map Legend & Lines at a Glance subtitle
    s = s.replace(
        '<div class="leg-item"><span class="leg-badge" style="background:var(--pink-metro); opacity:0.75;"></span> ಗುಲಾಬಿ ಮಾರ್ಗ (Pink · 18 ನಿಲ್ದಾಣಗಳು - ಶೀಘ್ರವೇ)</div>',
        '<div class="leg-item"><span class="leg-badge" style="background:var(--pink-metro);"></span> ಗುಲಾಬಿ ಮಾರ್ಗ (Pink · 6 ಸಕ್ರಿಯ + 12 ಭೂಗತ ನಿರ್ಮಾಣ)</div>',
    )
    s = s.replace(
        '<p class="sec-desc">3 ಕಾರ್ಯಾಚರಣೆಯ ಮಾರ್ಗಗಳು ಮತ್ತು 2 ನಿರ್ಮಾಣ ಹಂತದಲ್ಲಿರುವ ಮಾರ್ಗಗಳ ಸಂಪೂರ್ಣ ವಿವರ</p>',
        '<p class="sec-desc">4 ಸಕ್ರಿಯ ಮಾರ್ಗಗಳು (Pink ಭಾಗಶಃ ಸಕ್ರಿಯ) ಮತ್ತು ನಿರ್ಮಾಣ ಹಂತದ ಮಾರ್ಗಗಳ ಸಂಪೂರ್ಣ ವಿವರ</p>',
    )
    s = s.replace(
        '<p class="sec-desc">BMRCL ಅಧಿಕೃತ ಪರಿಷ್ಕೃತ ದರ ಪಟ್ಟಿ (ಫೆಬ್ರವರಿ 2025) ಪ್ರಕಾರ ನಿಖರ ದರ ಶೋಧಕ</p>',
        '<p class="sec-desc">BMRCL ಪರಿಷ್ಕೃತ ದರ ಪಟ್ಟಿ (2025–2026 · ₹10–₹90) &amp; ಗುಲಾಬಿ ಮಾರ್ಗ (₹10–₹30) ನಿಖರ ದರ ಶೋಧಕ</p>',
    )

    # 2d. Upgrade Train Timings & Schedule Card with Pink Line exact timings + Peak/Off-Peak discount windows
    old_ttc = re.compile(
        r'<!-- Train Timings & Schedule Status Card -->\s*<div class="train-timing-card">.*?</div>\s*</div>\s*</div>',
        re.S,
    )
    new_ttc = '''<!-- Train Timings & Schedule Status Card -->
        <div class="train-timing-card">
          <div class="ttc-header">
            <span>⏰ ಮೆಟ್ರೋ ರೈಲು ಕಾರ್ಯಾಚರಣೆ ವೇಳಾಪಟ್ಟಿ (2026)</span>
            <span style="color:#16A34A; font-weight:900;">● 4 ಮಾರ್ಗಗಳು ಸಕ್ರಿಯ</span>
          </div>
          <div class="ttc-grid">
            <div class="ttc-item">
              <div class="lbl">ನೇರಳೆ / ಹಸಿರು / ಹಳದಿ ಮಾರ್ಗ</div>
              <div class="val">05:00 AM – 11:00 PM</div>
              <div style="font-size:10.5px; color:#64748B; font-weight:700;">ಭಾನು: 07:00 AM · ಪೀಕ್ 3–7 ನಿಮಿಷ</div>
            </div>
            <div class="ttc-item" style="border-color:#F9A8D4; background:#FDF2F8;">
              <div class="lbl" style="color:#BE185D;">🌸 ಗುಲಾಬಿ ಮಾರ್ಗ (ಕಾಳೇನ ಅಗ್ರಹಾರ ↔ ತಾವರೆಕೆರೆ)</div>
              <div class="val" style="color:#9D174D; font-size:14.5px;">06:00 AM – 10:54 PM</div>
              <div style="font-size:10.5px; color:#831843; font-weight:700;">ಸೋಮ: 04:55 AM · ಭಾನು: 07:00 AM · ಪ್ರತಿ 8–10 ನಿಮಿಷ</div>
            </div>
          </div>
          <div style="margin-top:10px; padding:9px 11px; border-radius:10px; background:#F8FAFC; border:1px solid #E2E8F0; font-size:11.5px; color:#334155; line-height:1.55;">
            <div><b>💳 ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ / NCMC ರಿಯಾಯಿತಿ ಸಮಯ:</b></div>
            <div>• <b>10% ರಿಯಾಯಿತಿ (Off-Peak):</b> ಆರಂಭ–8:00 AM · 12:00 PM–4:00 PM · 9:00 PM–ಅಂತ್ಯ &amp; ಭಾನುವಾರ/ರಜಾದಿನ ಪೂರ್ತಿ</div>
            <div>• <b>5% ರಿಯಾಯಿತಿ (Peak):</b> 8:00 AM–12:00 PM &amp; 4:00 PM–9:00 PM · ಕನಿಷ್ಠ ಬ್ಯಾಲೆನ್ಸ್ <b>₹90</b> · ಕಾರ್ಡ್ ದರ <b>₹50</b></div>
            <div style="color:#BE185D; font-weight:800; margin-top:3px;">🌸 Pink Line ಹಂತ 1 ದರ: ₹10 – ₹30 (ಜಯದೇವ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಹಳದಿ ಮಾರ್ಗಕ್ಕೆ ಉಚಿತ ಇಂಟರ್‌ಚೇಂಜ್)</div>
          </div>
        </div>
      </div>'''
    s, n_ttc = old_ttc.subn(new_ttc, s, count=1)
    assert n_ttc == 1, "Failed to update train-timing-card"

    # 2e. Update Editorial Article Pink Line section (now operational since Nov 14, 2026)
    s = s.replace(
        "🌸 ಕುತೂಹಲ ಕೆರಳಿಸಿರುವ ಗುಲಾಬಿ ಮಾರ್ಗ (Pink Line): ಜಯದೇವ ಅತಿದೊಡ್ಡ ಹಬ್",
        "🌸 ಭಾಗಶಃ ಸಾರ್ವಜನಿಕ ಸೇವೆಗೆ ಮುಕ್ತವಾದ ಗುಲಾಬಿ ಮಾರ್ಗ (Pink Line): ಕಾಳೇನ ಅಗ್ರಹಾರ ↔ ತಾವರೆಕೆರೆ",
    )
    old_pink_para = (
        "2026ರ ಇತ್ತೀಚಿನ ಮಾಹಿತಿಯ ಪ್ರಕಾರ, ಈ ಪಿಂಕ್ ಲೈನ್‌ನ 7.5 ಕಿಲೋಮೀಟರ್ ಉದ್ದದ ಎಲಿವೇಟೆಡ್ ಮಾರ್ಗ ಅಂದರೆ ಕಳೇನ ಅಗ್ರಹಾರದಿಂದ ತಾವರೆಕೆರೆವರೆಗಿನ "
        "(ಜಯದೇವ ಆಸ್ಪತ್ರೆ ಮೂಲಕ) ಭಾಗ ಉದ್ಘಾಟನೆಗೆ ಸಂಪೂರ್ಣವಾಗಿ ಸಿದ್ಧವಾಗಿದೆ. ಇತ್ತೀಚೆಗಷ್ಟೇ ಬೆಂಗಳೂರು ಅಭಿವೃದ್ಧಿ ಸಚಿವ ಕೃಷ್ಣ ಬೈರೇಗೌಡ, "
        "ಸಂಸದ ತೇಜಸ್ವಿ ಸೂರ್ಯ ಮತ್ತು ಬಿಎಂಆರ್‌ಸಿಎಲ್ ಎಂಡಿ ಪಿ.ಸಿ. ಜಾಫರ್ ಅವರು ಈ ಮಾರ್ಗದಲ್ಲಿ ಪ್ರಾಯೋಗಿಕ ಸಂಚಾರ (Trial run) ಕೂಡ ಮಾಡಿದ್ದಾರೆ. "
        "2026ರ ಸೆಪ್ಟೆಂಬರ್ ಅಂತ್ಯದೊಳಗೆ ಈ ಮಾರ್ಗ ಸಾರ್ವಜನಿಕರ ಬಳಕೆಗೆ ಮುಕ್ತವಾಗುವ ನಿರೀಕ್ಷೆ ಇದೆ. ಇದರಲ್ಲಿ ಬರುವ "
        "<strong>'ಜಯದೇವ ಆಸ್ಪತ್ರೆ' ಮೆಟ್ರೋ ನಿಲ್ದಾಣವಂತೂ</strong> ಭವಿಷ್ಯದಲ್ಲಿ ಭಾರತದ ಅತಿ ದೊಡ್ಡ ಇಂಟರ್‌ಚೇಂಜ್ ನಿಲ್ದಾಣಗಳಲ್ಲಿ ಒಂದಾಗಲಿದ್ದು, "
        "ಇಲ್ಲಿ ಹಳದಿ ಮತ್ತು ಗುಲಾಬಿ ಮಾರ್ಗಗಳು ಒಂದಕ್ಕೊಂದು ಸಂಧಿಸಲಿವೆ."
    )
    new_pink_para = (
        "<strong>2026ರ ನವೆಂಬರ್ 13ರಂದು</strong> ಪ್ರಧಾನಿ ನರೇಂದ್ರ ಮೋದಿಯವರು ಉದ್ಘಾಟಿಸಿದ ಈ ಪಿಂಕ್ ಲೈನ್‌ನ 7.5 ಕಿಲೋಮೀಟರ್ ಉದ್ದದ ಎಲಿವೇಟೆಡ್ ಮಾರ್ಗ "
        "(<strong>ಕಾಳೇನ ಅಗ್ರಹಾರ, ಹುಳಿಮಾವು, ಐಐಎಂ ಬೆಂಗಳೂರು, ಜೆ.ಪಿ. ನಗರ 4ನೇ ಹಂತ, ಜಯದೇವ ಆಸ್ಪತ್ರೆ ಮತ್ತು ತಾವರೆಕೆರೆ</strong>) "
        "<strong>ನವೆಂಬರ್ 14, 2026ರಿಂದ</strong> ಸಾರ್ವಜನಿಕ ಪ್ರಯಾಣಿಕರ ಸೇವೆಗೆ ಅಧಿಕೃತವಾಗಿ ಮುಕ್ತವಾಗಿದೆ! ಬನ್ನೇರುಘಟ್ಟ ರಸ್ತೆಯ ಪ್ರಯಾಣಿಕರಿಗೆ ₹10 ರಿಂದ ₹30 ದರದಲ್ಲಿ "
        "ವೇಗದ ಪ್ರಯಾಣ ದೊರೆತಿದ್ದು, <strong>'ಜಯದೇವ ಆಸ್ಪತ್ರೆ' ಬಹು-ಹಂತದ ಇಂಟರ್‌ಚೇಂಜ್ ನಿಲ್ದಾಣದ</strong> ಮೂಲಕ ಹಳದಿ ಮಾರ್ಗಕ್ಕೂ (ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ / ಆರ್.ವಿ. ರಸ್ತೆ) "
        "ನೇರವಾಗಿ ಸಂಪರ್ಕ ಸಾಧಿಸಬಹುದು. ಇನ್ನುಳಿದ ಡೈರಿ ಸರ್ಕಲ್‌ನಿಂದ ನಾಗವಾರವರೆಗಿನ 12 ಭೂಗತ ನಿಲ್ದಾಣಗಳ ಕಾಮಗಾರಿ ಭರದಿಂದ ಸಾಗಿದ್ದು 2027ರಲ್ಲಿ ಪೂರ್ಣಗೊಳ್ಳುವ ಗುರಿ ಇದೆ."
    )
    assert old_pink_para in s, "Could not find old Pink Line paragraph"
    s = s.replace(old_pink_para, new_pink_para, 1)

    s = s.replace(
        "ಸದ್ಯಕ್ಕೆ 96 ಕಿಲೋಮೀಟರ್‌ಗಿಂತಲೂ ಹೆಚ್ಚು ಉದ್ದದ ಕಾರ್ಯಾಚರಣೆಯ ಜಾಲವನ್ನು ಹೊಂದಿರುವ ನಮ್ಮ ಮೆಟ್ರೋ",
        "ಸದ್ಯಕ್ಕೆ 103.65 ಕಿಲೋಮೀಟರ್‌ಗೂ ಹೆಚ್ಚು ಉದ್ದದ ಕಾರ್ಯಾಚರಣೆಯ ಜಾಲವನ್ನು ಹೊಂದಿರುವ ನಮ್ಮ ಮೆಟ್ರೋ",
    )

    # 2f. Update inline METRO_DATA JSON object inside bengaluru-metro.html
    metro_data_pattern = re.compile(r"let METRO_DATA = \{.*?\n\};", re.S)
    new_inline_json = "let METRO_DATA = " + json.dumps(updated_metro_data, ensure_ascii=False, indent=2) + ";"
    s, n_md = metro_data_pattern.subn(lambda _: new_inline_json, s, count=1)
    assert n_md == 1, "Failed to update inline METRO_DATA"

    # 2g. Update EXPANSION_TIMELINE Pink Line entries
    s = s.replace(
        "{ date: 'ಸೆಪ್ಟೆಂಬರ್ 2026', title: 'ಗುಲಾಬಿ ಮಾರ್ಗ ಹಂತ 1 (ಕಾಳೇನ ಅಗ್ರಹಾರ ↔ ತಾವರೆಕೆರೆ)', desc: 'ಬನ್ನೇರುಘಟ್ಟ ರಸ್ತೆಯ 7.5 ಕಿ.ಮೀ ಮೇಲ್ಸೇತುವೆ ಮಾರ್ಗ. CMRS ಸುರಕ್ಷತಾ ತಪಾಸಣೆ ಯಶಸ್ವಿಯಾಗಿ ಪೂರ್ಣ.', status: 'current' },",
        "{ date: '14 ನವೆಂಬರ್ 2026', title: 'ಗುಲಾಬಿ ಮಾರ್ಗ ಹಂತ 1 ಸಾರ್ವಜನಿಕ ಸೇವೆ ಆರಂಭ (ಕಾಳೇನ ಅಗ್ರಹಾರ ↔ ತಾವರೆಕೆರೆ)', desc: 'ಬನ್ನೇರುಘಟ್ಟ ರಸ್ತೆಯ 7.5 ಕಿ.ಮೀ ಎಲಿವೇಟೆಡ್ ಮಾರ್ಗ (6 ನಿಲ್ದಾಣಗಳು) ಮತ್ತು ಜಯದೇವ ಹಳದಿ–ಗುಲಾಬಿ ಇಂಟರ್‌ಚೇಂಜ್ ಕಾರ್ಯಾರಂಭ. ಟಿಕೆಟ್ ದರ ₹10–₹30.', status: 'done' },",
    )
    s = s.replace(
        "{ date: 'ಮಾರ್ಚ್ 2027', title: 'ಗುಲಾಬಿ ಮಾರ್ಗ ಹಂತ 2 ಭೂಗತ ವಿಭಾಗ (ಡೈರಿ ಸರ್ಕಲ್ ↔ ನಾಗವಾರ)', desc: '13.76 ಕಿ.ಮೀ ಭೂಗತ ಸುರಂಗ ಮಾರ್ಗ, ಎಂ.ಜಿ. ರಸ್ತೆ ಹಾಗೂ ಕಂಟೋನ್ಮೆಂಟ್ ರೈಲ್ವೆ ಇಂಟರ್‌ಚೇಂಜ್.', status: 'pending' },",
        "{ date: '2027 (ನಿರೀಕ್ಷಿತ)', title: 'ಗುಲಾಬಿ ಮಾರ್ಗ ಹಂತ 2 ಭೂಗತ ವಿಭಾಗ (ಡೈರಿ ಸರ್ಕಲ್ ↔ ನಾಗವಾರ)', desc: '13.76 ಕಿ.ಮೀ ಭೂಗತ ಸುರಂಗ ಮಾರ್ಗ (12 ನಿಲ್ದಾಣಗಳು), ಎಂ.ಜಿ. ರಸ್ತೆ ಹಾಗೂ ಕಂಟೋನ್ಮೆಂಟ್ ರೈಲ್ವೆ ಇಂಟರ್‌ಚೇಂಜ್ ಕಾಮಗಾರಿ ಪ್ರಗತಿಯಲ್ಲಿದೆ.', status: 'current' },",
    )

    # 2h. Update renderLineCards() to support 'partial' status badge styling (Pink/Emerald)
    s = s.replace(
        "const isOp = L.status_type === 'operational';",
        "const isOp = L.status_type === 'operational';\n      const isPartial = L.status_type === 'partial';",
    )
    s = s.replace(
        "style=\"background:${isOp ? 'rgba(16,185,129,0.15)' : 'rgba(234,179,8,0.15)'}; color:${isOp ? '#059669' : '#D97706'};\"",
        "style=\"background:${isOp ? 'rgba(16,185,129,0.15)' : (isPartial ? 'rgba(236,72,153,0.14)' : 'rgba(234,179,8,0.15)')}; color:${isOp ? '#059669' : (isPartial ? '#BE185D' : '#D97706')};\"",
    )

    # 2i. Update Pink Line leaflet & SVG rendering so the 6 active stations render solid and 12 underground dashed
    # And add a helpful note in calculateFare() when selecting an under-construction station
    old_fare_desc = "document.getElementById('resFareDesc').textContent = `ಟೋಕನ್ ದರ · ${slab.d} (ಅಂದಾಜು ${stationsTravelled} ನಿಲ್ದಾಣಗಳು)`;"
    new_fare_desc = (
        "const _fromStnObj = (METRO_DATA.stations[fromLine] || [])[fromIdx - 1];\n"
        "    const _toStnObj = (METRO_DATA.stations[toLine] || [])[toIdx - 1];\n"
        "    const _isPlanned = (fromLine === 'blue' || toLine === 'blue' || (_fromStnObj && _fromStnObj.operational === false) || (_toStnObj && _toStnObj.operational === false));\n"
        "    document.getElementById('resFareDesc').textContent = _isPlanned\n"
        "      ? `ಅಂದಾಜು ಟೋಕನ್ ದರ · ${slab.d} (${stationsTravelled} ನಿಲ್ದಾಣಗಳು) · 🚧 ಭೂಗತ/ನೀಲಿ ಮಾರ್ಗ ನಿರ್ಮಾಣ ಹಂತದಲ್ಲಿದೆ`\n"
        "      : `ಟೋಕನ್ ದರ · ${slab.d} (ಅಂದಾಜು ${stationsTravelled} ನಿಲ್ದಾಣಗಳು)`;"
    )
    assert old_fare_desc in s, "Could not find resFareDesc line"
    s = s.replace(old_fare_desc, new_fare_desc, 1)

    # 2j. Update Tariff Slab table smart card column clarity (Peak 5% / Off-Peak 10%)
    s = s.replace("<th>ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್</th>", "<th>ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ (5%–10% Off)</th>")

    # 2k. Cache-bust /data/metro_data.json fetch so browsers get the new Pink Line data immediately
    s = s.replace("fetch('/data/metro_data.json')", "fetch('/data/metro_data.json?v=20261128')")

    METRO_HTML.write_text(s, encoding="utf-8")
    print(f"SUCCESS: Updated bengaluru-metro.html ({len(s):,} bytes) with Pink Line Phase-1 running, BMRCL fares & timings.")


if __name__ == "__main__":
    main()
