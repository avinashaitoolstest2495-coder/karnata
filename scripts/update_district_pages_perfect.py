# -*- coding: utf-8 -*-
"""
Karnata — scripts/update_district_pages_perfect.py
Addresses user request:
1. Fix Petrol, Diesel, Gold, Silver & Dam water levels to show live rates.
2. Remove MP and MLA photos completely from district pages.
3. Make it possible to take/copy the present MLAs and MP list from each district page.
"""

import os
import glob
import re
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"

# 1. Load Data Sources
with open(ROOT_DIR / "data" / "gold_rates.json", "r", encoding="utf-8") as f:
    gold_data = json.load(f)

with open(ROOT_DIR / "data" / "petrol_rates.json", "r", encoding="utf-8") as f:
    petrol_data = json.load(f)

with open(ROOT_DIR / "data" / "dam_levels.json", "r", encoding="utf-8") as f:
    dam_data = json.load(f)

# Gold & Silver reference rates
GOLD_24K = gold_data.get("baseGold", {}).get("24", 13893)
GOLD_22K = gold_data.get("baseGold", {}).get("22", 12730)
SILVER_RATE = gold_data.get("baseSilver", {}).get("999", 264.86)

# Dam associations for all 31 districts
DISTRICT_DAM_MAP = {
    "bengaluru-urban": "krs",
    "bengaluru-rural": "krs",
    "ramanagara": "krs",
    "chikkaballapura": "krs",
    "kolar": "krs",
    "tumakuru": "krs",
    "mandya": "krs",
    "mysuru": "kabini",
    "chamarajanagara": "kabini",
    "hassan": "hemavathi",
    "kodagu": "harangi",
    "chikkamagaluru": "bhadra",
    "shivamogga": "linganamakki",
    "dakshina-kannada": "supa",
    "udupi": "supa",
    "uttara-kannada": "supa",
    "belagavi": "ghataprabha",
    "dharwad": "malaprabha",
    "gadag": "malaprabha",
    "haveri": "tungabhadra",
    "bagalkote": "almatti",
    "vijayapura": "almatti",
    "kalaburagi": "narayanapura",
    "yadgir": "narayanapura",
    "bidar": "narayanapura",
    "raichur": "narayanapura",
    "koppal": "tungabhadra",
    "ballari": "tungabhadra",
    "vijayanagara": "tungabhadra",
    "davangere": "bhadra",
    "davanagere": "bhadra",
    "chitradurga": "vanivilasa"
}

# District slug to petrol district key mapping
DISTRICT_PETROL_KEY = {
    "bengaluru-urban": "bengaluru_urban",
    "bengaluru-rural": "bengaluru_rural",
    "ramanagara": "ramanagara",
    "chikkaballapura": "chikkaballapur",
    "kolar": "kolar",
    "tumakuru": "tumakuru",
    "mandya": "mandya",
    "mysuru": "mysuru",
    "chamarajanagara": "chamarajanagar",
    "hassan": "hassan",
    "kodagu": "kodagu",
    "chikkamagaluru": "chikkamagaluru",
    "shivamogga": "shivamogga",
    "dakshina-kannada": "dakshina_kannada",
    "udupi": "udupi",
    "uttara-kannada": "uttara_kannada",
    "belagavi": "belagavi",
    "dharwad": "dharwad",
    "gadag": "gadag",
    "haveri": "haveri",
    "bagalkote": "bagalkot",
    "vijayapura": "vijayapura",
    "kalaburagi": "kalaburagi",
    "yadgir": "yadgir",
    "bidar": "bidar",
    "raichur": "raichur",
    "koppal": "koppal",
    "ballari": "ballari",
    "vijayanagara": "vijayanagara",
    "davangere": "davanagere",
    "chitradurga": "chitradurga"
}

def get_fuel_rates(slug):
    pkey = DISTRICT_PETROL_KEY.get(slug, slug.replace("-", "_"))
    dist_obj = petrol_data.get("districts", {}).get(pkey, {})
    taluks = dist_obj.get("taluks", {})
    if taluks:
        first = list(taluks.values())[0]
        return first.get("petrol", 110.89), first.get("diesel", 98.80)
    # Check cities fallback
    city_key = slug.split("-")[0]
    if city_key in petrol_data.get("cities", {}):
        c_obj = petrol_data["cities"][city_key]
        return c_obj.get("petrol", 110.89), c_obj.get("diesel", 98.80)
    return 110.89, 98.80

def get_dam_info(slug):
    dkey = DISTRICT_DAM_MAP.get(slug, "krs")
    dams = dam_data.get("dams", {})
    dam_obj = dams.get(dkey, {})
    name_kn = dam_obj.get("name_kn", "ಕೃಷ್ಣರಾಜ ಸಾಗರ (K.R.S)")
    pct = dam_obj.get("storage_pct", 50.0)
    cur_tmc = dam_obj.get("present_storage_tmc") or dam_obj.get("storage_tmc") or dam_obj.get("gross_storage_tmc") or 24.2
    max_tmc = dam_obj.get("max_storage_tmc") or dam_obj.get("design_capacity") or 49.4
    inflow = dam_obj.get("inflow_cusecs", 0.0)
    outflow = dam_obj.get("outflow_cusecs", 0.0)
    
    # Status color
    if pct >= 80:
        color = "#16A34A" # Green
    elif pct >= 40:
        color = "#0284C7" # Blue
    else:
        color = "#D97706" # Amber
        
    return {
        "key": dkey,
        "name_kn": name_kn,
        "pct": f"{pct:.1f}",
        "pct_num": pct,
        "cur_tmc": f"{float(cur_tmc):.2f}",
        "max_tmc": f"{float(max_tmc):.2f}",
        "inflow": f"{int(inflow):,}",
        "color": color
    }

def update_district_html(html, slug):
    petrol, diesel = get_fuel_rates(slug)
    dam = get_dam_info(slug)
    
    # Extract district kannada name from title
    m_title = re.search(r'<title>([^<\(]+)', html)
    dist_kn = m_title.group(1).strip() if m_title else slug.title()
    
    # ----------------------------------------------------
    # 1. Update Market & Dam Section with Live Values & IDs
    # ----------------------------------------------------
    # Match the section from <!-- RIGHT: LIVE RATES, DAM & APMC CROPS CARD --> to </section>
    market_sec_pat = re.compile(
        r'(<!-- RIGHT: LIVE RATES, DAM & APMC CROPS CARD -->[\s\S]*?<section[^>]*class="d-sec"[^>]*>[\s\S]*?)(</section>)',
        re.IGNORECASE
    )
    
    # Find existing APMC crop description text if any
    apmc_desc = f"{dist_kn} ಕೃಷಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ನಿತ್ಯವೂ ಭತ್ತ, ರಾಗಿ, ತೊಗರಿ, ಮೆಕ್ಕೆಜೋಳ, ಹತ್ತಿ ಹಾಗೂ ತರಕಾರಿಗಳ ಅಧಿಕೃತ APMC ವಹಿವಾಟು ನಡೆಯುತ್ತದೆ."
    m_apmc = re.search(r'<span>🌾</span>\s*([^<]+)<[\s\S]*?<div style="font-size:12px; color:#475569; line-height:1.5;">([\s\S]*?)</div>', html)
    if m_apmc:
        apmc_desc = m_apmc.group(2).strip()

    new_market_sec = f'''<!-- RIGHT: LIVE RATES, DAM & APMC CROPS CARD -->
      <section class="d-sec" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:18px; padding:20px 22px; box-shadow:0 10px 25px rgba(15,23,42,0.05); display:flex; flex-direction:column; justify-content:space-between; margin-bottom:0; border-left: 5px solid var(--k-crimson);">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #F1F5F9; padding-bottom:12px; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:20px;">⚡</span>
              <h2 style="font-size:18px; font-weight:900; color:#0F172A; margin:0;">
                ಲೈವ್ ಮಾರುಕಟ್ಟೆ &amp; ಜಲಾಶಯ
              </h2>
            </div>
            <span style="font-size:11.5px; font-weight:800; color:#15803D; background:#DCFCE7; padding:3px 10px; border-radius:20px; border:1px solid #86EFAC;">
              🟢 ಲೈವ್ ದರಗಳು
            </span>
          </div>

          <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:14px;">
            <!-- GOLD & FUEL RATES -->
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
              <div style="background:#FFFBEB; border:1px solid #FDE68A; border-radius:12px; padding:10px 12px;">
                <div style="font-size:11.5px; font-weight:900; color:#D97706;">🥇 ಚಿನ್ನ (24K/22K)</div>
                <div style="font-size:15.5px; font-weight:900; color:#92400E; font-family:var(--font-en); margin-top:2px;" id="dist-gold-24k">₹{GOLD_24K:,} /g</div>
                <div style="font-size:10.5px; color:#B45309;" id="dist-silver">ಬೆಳ್ಳಿ: ₹{SILVER_RATE:.2f} /g</div>
              </div>
              <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:12px; padding:10px 12px;">
                <div style="font-size:11.5px; font-weight:900; color:#15803D;">⛽ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್</div>
                <div style="font-size:15.5px; font-weight:900; color:#14532D; font-family:var(--font-en); margin-top:2px;" id="dist-petrol">₹{petrol:.2f}</div>
                <div style="font-size:10.5px; color:#15803D;" id="dist-diesel">ಡೀಸೆಲ್: ₹{diesel:.2f}</div>
              </div>
            </div>

            <!-- DAM WATER LEVEL METRIC -->
            <div style="background:linear-gradient(135deg, #1E293B 0%, #0F172A 100%); color:#FFF; border-radius:14px; padding:14px 16px; border:1px solid #334155;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="display:flex; align-items:center; gap:6px;">
                  <span style="font-size:18px;">🌊</span>
                  <div style="font-size:13.5px; font-weight:800; color:#F8FAFC;" id="dist-dam-name">
                    {dam['name_kn']}
                  </div>
                </div>
                <span style="background:{dam['color']}; color:#FFF; font-size:11px; font-weight:900; padding:2px 8px; border-radius:12px;" id="dist-dam-pct">
                  {dam['pct']}% ಭರ್ತಿ
                </span>
              </div>
              <!-- Storage Bar -->
              <div style="background:#334155; border-radius:10px; height:8px; overflow:hidden; margin-bottom:8px;">
                <div id="dist-dam-bar" style="background:linear-gradient(90deg, #38BDF8, #0284C7); width:{dam['pct']}%; height:100%; border-radius:10px;"></div>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:11px; color:#94A3B8;">
                <span id="dist-dam-storage">ಸಂಗ್ರಹ: <strong style="color:#FFF; font-family:var(--font-en);">{dam['cur_tmc']} TMC</strong> / {dam['max_tmc']} TMC</span>
                <span id="dist-dam-inflow">ಒಳಹರಿವು: <strong style="color:#34D399; font-family:var(--font-en);">{dam['inflow']} cusecs</strong></span>
              </div>
            </div>

            <!-- APMC CROPS SUMMARY -->
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:10px 14px;">
              <div style="font-size:13px; font-weight:900; color:#0F172A; margin-bottom:4px; display:flex; align-items:center; gap:6px;">
                <span>🌾</span> {dist_kn} ಪ್ರಮುಖ APMC ಬೆಳೆಗಳು:
              </div>
              <div style="font-size:12px; color:#475569; line-height:1.5;">
                {apmc_desc}
              </div>
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:4px; border-top:1px solid #F1F5F9; font-size:12.5px; font-weight:800;">
          <a href="/dam-levels.html" style="color:#0284C7; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
            🌊 ಎಲ್ಲಾ 14 ಜಲಾಶಯಗಳು →
          </a>
          <a href="/apmc-prices.html" style="color:var(--k-crimson); text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
            🌾 APMC ದರಗಳು →
          </a>
        </div>
      </section>'''

    html = market_sec_pat.sub(new_market_sec, html)

    # ----------------------------------------------------
    # 2. Remove MP & MLA Photos from Representation Cards
    # ----------------------------------------------------
    # Pattern A: MP Photo Grid (82px)
    # <div style="display:grid; grid-template-columns: 82px 1fr; gap: 14px; align-items: center; margin-bottom:12px;">
    #   <div style="position:relative; width:82px; ...">...</div>
    #   <div>
    #     <div style="font-size:18px; ...">{name}</div>
    #     <div style="font-size:13px; ...">{role}</div>
    #     <div style="font-size:12px; ...">{sub}</div>
    #   </div>
    # </div>
    mp_photo_pat = re.compile(
        r'<div style="display:grid; grid-template-columns:\s*82px\s*1fr;\s*gap:\s*14px;\s*align-items:\s*center;\s*margin-bottom:12px;">\s*'
        r'<div style="position:relative;\s*width:82px;[\s\S]*?</div>\s*</div>\s*'
        r'<div>\s*'
        r'(<div style="font-size:18px;[\s\S]*?</div>)\s*'
        r'(<div style="font-size:13px;[\s\S]*?</div>)\s*'
        r'(<div style="font-size:12px;[\s\S]*?</div>)\s*'
        r'</div>\s*</div>',
        re.IGNORECASE
    )
    def repl_mp(m):
        name_div = m.group(1)
        role_div = m.group(2)
        sub_div = m.group(3)
        return (
            f'<div style="margin-bottom:12px;">\n'
            f'  {name_div}\n'
            f'  <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-top:4px;">\n'
            f'    <span style="font-size:12px; font-weight:800; color:#0284C7; background:#E0F2FE; border:1px solid #BAE6FD; padding:3px 10px; border-radius:6px;">🗳️ ಲೋಕಸಭಾ ಸಂಸದರು (MP)</span>\n'
            f'    {sub_div}\n'
            f'  </div>\n'
            f'</div>'
        )
    html = mp_photo_pat.sub(repl_mp, html)

    # Pattern B: MLA Photo Grid (78px)
    mla_photo_pat = re.compile(
        r'<div style="display:grid; grid-template-columns:\s*78px\s*1fr;\s*gap:\s*14px;\s*align-items:\s*center;\s*margin-bottom:12px;">\s*'
        r'<div style="position:relative;\s*width:78px;[\s\S]*?</div>\s*</div>\s*'
        r'<div>\s*'
        r'(<div style="font-size:17\.5px;[\s\S]*?</div>)\s*'
        r'(<div style="font-size:12\.5px;[\s\S]*?</div>)\s*'
        r'(<div style="font-size:11\.5px;[\s\S]*?</div>)\s*'
        r'</div>\s*</div>',
        re.IGNORECASE
    )
    def repl_mla(m):
        name_div = m.group(1)
        role_div = m.group(2)
        sub_div = m.group(3)
        return (
            f'<div style="margin-bottom:12px;">\n'
            f'  {name_div}\n'
            f'  <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-top:4px;">\n'
            f'    <span style="font-size:12px; font-weight:800; color:#0284C7; background:#E0F2FE; border:1px solid #BAE6FD; padding:3px 10px; border-radius:6px;">🏛️ ವಿಧಾನಸಭಾ ಸದಸ್ಯರು (MLA)</span>\n'
            f'    {sub_div}\n'
            f'  </div>\n'
            f'</div>'
        )
    html = mla_photo_pat.sub(repl_mla, html)

    # Also catch any residual img tags inside d-big-rep-card just in case
    html = re.sub(r'<img[^>]+src=["\']/assets/images/(?:mps|mlas)/[^"\']+["\'][^>]*>', '', html)

    # ----------------------------------------------------
    # 3. Add "📋 ಪಟ್ಟಿ ಕಾಪಿ ಮಾಡಿ (Copy MLAs & MP List)" Bar
    # ----------------------------------------------------
    # Extract MP and MLA names and constituencies for clipboard copy
    mp_names = re.findall(r'<div style="font-size:18px;[^"]*">([^<]+)</div>', html)
    mp_parties = re.findall(r'🗳️ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ:[^<]*<span class="d-party-tag [^"]*">([^<]+)</span>', html)
    mp_consts = re.findall(r'🗳️ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ:\s*([^<\n]+)', html)

    mla_names = re.findall(r'<div style="font-size:17\.5px;[^"]*">([^<]+)</div>', html)
    mla_parties = re.findall(r'<span class="d-party-tag [^"]*">([^<]+)</span>', html)
    mla_consts = re.findall(r'🏛️\s*([^<\n]+)(?:<span[\s\S]*?</span>)?\s*</div>', html)

    # Build clipboard payload text
    clip_lines = [f"{dist_kn} ಜಿಲ್ಲೆಯ ಪ್ರಸ್ತುತ ಸಂಸದರು & ಶಾಸಕರ ಅಧಿಕೃತ ಪಟ್ಟಿ (2026):", ""]
    clip_lines.append("🗳️ ಲೋಕಸಭಾ ಸಂಸದರು (MP):")
    for i, mn in enumerate(mp_names):
        mparty = mp_parties[i] if i < len(mp_parties) else ""
        mconst = mp_consts[i].strip() if i < len(mp_consts) else ""
        clip_lines.append(f"  {i+1}. {mn.strip()} ({mparty}) - {mconst}")
    
    clip_lines.append("")
    clip_lines.append("🏛️ ವಿಧಾನಸಭಾ ಶಾಸಕರು (MLAs):")
    for j, an in enumerate(mla_names):
        # Party list starts after MPs
        pidx = len(mp_parties) + j
        aparty = mla_parties[pidx] if pidx < len(mla_parties) else ""
        aconst = mla_consts[j].strip() if j < len(mla_consts) else ""
        clip_lines.append(f"  {j+1}. {an.strip()} ({aparty}) - {aconst}")

    clip_lines.append("")
    clip_lines.append("ಮೂಲ: ಕರ್ನಾಟ — https://karnata.in")
    clipboard_text = "\\n".join(clip_lines).replace('"', '\\"').replace("'", "\\'")

    copy_bar_html = f'''<!-- 2. REPRESENTATIVES: MPS & MLAS -->
    <div style="background:linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%); border:1.5px solid #86EFAC; border-radius:14px; padding:12px 18px; margin-bottom:18px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
      <div>
        <div style="font-size:14.5px; font-weight:900; color:#14532D; display:flex; align-items:center; gap:6px;">
          <span>📋</span> {dist_kn} ಜಿಲ್ಲೆಯ ಜನಪ್ರತಿನಿಧಿಗಳ ಅಧಿಕೃತ ಪಟ್ಟಿ (2026)
        </div>
        <div style="font-size:12px; color:#166534; margin-top:2px;">
          {len(mp_names)} ಲೋಕಸಭಾ ಸಂಸದರು &amp; {len(mla_names)} ವಿಧಾನಸಭಾ ಶಾಸಕರ ಪೂರ್ಣ ವಿವರಗಳು
        </div>
      </div>
      <button onclick="copyDistrictRepsList()" id="btn-copy-reps" style="background:#15803D; color:#FFF; border:none; border-radius:10px; padding:8px 16px; font-size:12.5px; font-weight:800; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 3px 10px rgba(21,128,61,0.25); transition:all 0.2s ease;">
        📋 ಪಟ್ಟಿ ಕಾಪಿ ಮಾಡಿ (Copy List)
      </button>
    </div>'''

    # Insert copy bar right after <!-- 2. REPRESENTATIVES: MPS & MLAS -->
    if 'id="btn-copy-reps"' not in html:
        html = html.replace('<!-- 2. REPRESENTATIVES: MPS & MLAS -->', copy_bar_html)

    # ----------------------------------------------------
    # 4. Inject Dynamic Client-Side Live Sync & Copy Script
    # ----------------------------------------------------
    sync_script = f'''
<!-- DYNAMIC DISTRICT LIVE RATES & CLIPBOARD SCRIPT -->
<script>
window.CURRENT_DISTRICT_DAM_KEY = "{dam['key']}";
window.DISTRICT_REPS_TEXT = "{clipboard_text}";

function copyDistrictRepsList() {{
  if (navigator.clipboard && window.DISTRICT_REPS_TEXT) {{
    navigator.clipboard.writeText(window.DISTRICT_REPS_TEXT).then(() => {{
      const btn = document.getElementById('btn-copy-reps');
      if (btn) {{
        const orig = btn.innerHTML;
        btn.innerHTML = '✅ ಪಟ್ಟಿ ಕಾಪಿ ಆಯಿತು!';
        btn.style.background = '#047857';
        setTimeout(() => {{ btn.innerHTML = orig; btn.style.background = '#15803D'; }}, 2500);
      }}
    }}).catch(() => {{
      alert(window.DISTRICT_REPS_TEXT);
    }});
  }}
}}

async function syncDistrictRates() {{
  try {{
    // 1. Gold & Silver
    const gRes = await fetch('/data/gold_rates.json?v=' + Date.now()).catch(() => null);
    if (gRes && gRes.ok) {{
      const g = await gRes.json();
      if (g && g.baseGold && g.baseGold['24']) {{
        const g24 = g.baseGold['24'];
        const silv = (g.baseSilver && g.baseSilver['999']) ? g.baseSilver['999'] : (g.silver && g.silver['999_per_gram']) || {SILVER_RATE};
        const elG = document.getElementById('dist-gold-24k');
        if (elG) elG.textContent = `₹${{g24.toLocaleString('en-IN')}} /g`;
        const elS = document.getElementById('dist-silver');
        if (elS) elS.textContent = `ಬೆಳ್ಳಿ: ₹${{typeof silv === 'number' ? silv.toFixed(2) : silv}} /g`;
      }}
    }}

    // 2. Petrol & Diesel
    const pRes = await fetch('/data/petrol_rates.json?v=' + Date.now()).catch(() => null);
    if (pRes && pRes.ok) {{
      const p = await pRes.json();
      const slug = window.location.pathname.split('/').pop().replace('.html', '').replace(/-/g, '_');
      let pet = null, die = null;
      if (p.districts && p.districts[slug]) {{
        const taluks = p.districts[slug].taluks || {{}};
        const first = Object.values(taluks)[0];
        if (first) {{ pet = first.petrol; die = first.diesel; }}
      }}
      if (pet) {{
        const elP = document.getElementById('dist-petrol');
        if (elP) elP.textContent = `₹${{pet.toFixed(2)}}`;
      }}
      if (die) {{
        const elD = document.getElementById('dist-diesel');
        if (elD) elD.textContent = `ಡೀಸೆಲ್: ₹${{die.toFixed(2)}}`;
      }}
    }}

    // 3. Dam Level
    const dRes = await fetch('/data/dam_levels.json?v=' + Date.now()).catch(() => null);
    if (dRes && dRes.ok) {{
      const d = await dRes.json();
      const damKey = window.CURRENT_DISTRICT_DAM_KEY;
      if (damKey && d.dams && d.dams[damKey]) {{
        const dm = d.dams[damKey];
        const pct = dm.storage_pct || 0;
        const curTmc = (dm.present_storage_tmc || dm.storage_tmc || dm.gross_storage_tmc || 0).toFixed(2);
        const maxTmc = (dm.max_storage_tmc || dm.design_capacity || 0).toFixed(2);
        const inflow = (dm.inflow_cusecs || 0).toLocaleString('en-IN');
        
        const elPct = document.getElementById('dist-dam-pct');
        if (elPct) elPct.textContent = `${{pct}}% ಭರ್ತಿ`;
        const elBar = document.getElementById('dist-dam-bar');
        if (elBar) elBar.style.width = `${{pct}}%`;
        const elStore = document.getElementById('dist-dam-storage');
        if (elStore) elStore.innerHTML = `ಸಂಗ್ರಹ: <strong style="color:#FFF; font-family:var(--font-en);">${{curTmc}} TMC</strong> / ${{maxTmc}} TMC`;
        const elInf = document.getElementById('dist-dam-inflow');
        if (elInf) elInf.innerHTML = `ಒಳಹರಿವು: <strong style="color:#34D399; font-family:var(--font-en);">${{inflow}} cusecs</strong>`;
      }}
    }}
  }} catch (e) {{
    console.warn('Live rates sync:', e);
  }}
}}

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', syncDistrictRates);
}} else {{
  syncDistrictRates();
}}
</script>
</body>
</html>
'''
    # Clean any old syncDistrictRates script and safely append script with closing tags
    html = re.sub(r'<!-- DYNAMIC DISTRICT LIVE RATES & CLIPBOARD SCRIPT -->[\s\S]*?</script>', '', html)
    html = re.sub(r'</body>\s*</html>\s*$', '', html.strip(), flags=re.IGNORECASE)
    html = html.strip() + "\n\n" + sync_script.strip() + "\n"

    return html

def process_all_districts():
    files = sorted(glob.glob(str(ROOT_DIR / "districts" / "*.html")))
    print(f"Processing {len(files)} files in districts/ ...")
    
    updated = 0
    for fpath in files:
        fname = os.path.basename(fpath)
        if fname in ['index.html']:
            continue
        slug = fname.replace('.html', '')
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = update_district_html(content, slug)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        # Also sync to namma-karnataka/districts/
        nk_target = NK_DIR / "districts" / fname
        if nk_target.parent.exists():
            with open(nk_target, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
        updated += 1
        print(f"  -> Updated {fname}: live rates, dam {DISTRICT_DAM_MAP.get(slug)}, photos removed, copy list added.")
        
    print(f"\nSUCCESS: All {updated} district pages upgraded with live rates, removed photos & MLA/MP copy action!")

if __name__ == "__main__":
    process_all_districts()
