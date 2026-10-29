import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('data/panchatantra/panchatantra_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

gps = master['gram_panchayats'][:36]
cards_html = []
for g in gps:
    titleName = g.get('gp_name_kn') or g.get('gp_name_en', '')
    distName = g.get('district_name_kn') or g.get('district_name_en', '')
    talukName = g.get('taluk_name_kn') or g.get('taluk_name_en', '')
    staff_pill = f'<span class="staff-count-pill">👥 {g["total_staff"]} ಸಿಬ್ಬಂದಿ</span>' if g.get('total_staff') else ''
    pdo_row = f"""              <div class="gp-meta-row" style="margin-top:2px;">
                <span class="meta-lbl">PDO ಅಧಿಕಾರಿ:</span>
                <span class="meta-val" style="color:#059669;">{g["pdo_name"]}</span>
              </div>""" if g.get('pdo_name') else ''

    card = f"""      <div class="gp-card">
        <div class="card-top">
          <span class="gp-badge">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್</span>
          {staff_pill}
        </div>

        <h3 class="gp-title">{titleName}</h3>

        <div class="gp-meta">
          <div class="gp-meta-row">
            <span class="meta-lbl">ಜಿಲ್ಲೆ:</span>
            <span class="meta-val">{distName}</span>
          </div>
          <div class="gp-meta-row">
            <span class="meta-lbl">ತಾಲೂಕು:</span>
            <span class="meta-val">{talukName}</span>
          </div>
{pdo_row}
        </div>

        <button class="btn-profile" onclick="openGpModal('{g.get("gp_id")}')">
          👤 PDO & ಸಿಬ್ಬಂದಿ ವಿವರ ನೋಡಿ →
        </button>
      </div>"""
    cards_html.append(card)

cards_str = "\n".join(cards_html)

with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace loading placeholder in gpGrid
old_gpgrid = """    <div class="grid" id="gpGrid">
      <div style="grid-column:1/-1; text-align:center; padding:60px 20px;">
        <div style="font-size:42px; margin-bottom:12px;">⏳</div>
        <h3 style="font-size:20px; font-weight:900;">ಕರ್ನಾಟಕ ಗ್ರಾಮ ಪಂಚಾಯತ್ ದತ್ತಾಂಶ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</h3>
      </div>
    </div>"""

new_gpgrid = f"""    <div class="grid" id="gpGrid">
{cards_str}
    </div>"""

html = html.replace(old_gpgrid, new_gpgrid)

# Update count text
html = html.replace(
    '<div class="results-count" id="resultsCountText">\n        ಲೋಡ್ ಮಾಡಲಾಗುತ್ತಿದೆ...\n      </div>',
    '<div class="results-count" id="resultsCountText">ಒಟ್ಟು 5,935 ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು</div>'
)

# Update pagination bar display style
html = html.replace(
    '<div class="pagination-bar" id="paginationBar" style="display:none;">',
    '<div class="pagination-bar" id="paginationBar" style="display:flex;">'
)

with open('gram-panchayat.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Pre-rendered 36 GP cards into gram-panchayat.html successfully.")
