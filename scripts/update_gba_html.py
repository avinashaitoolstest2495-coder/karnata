import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Load GeoJSON wards for Central
with open('data/gis/bengaluru_wards.geojson', 'r', encoding='utf-8') as f:
    geo = json.load(f)

central_features = [f for f in geo['features'] if (f['properties'].get('corporation_short_en') or '').lower() == 'central']
central_features.sort(key=lambda x: int(x['properties'].get('ward_number', 0)))
print(f"Found {len(central_features)} Central wards.")

ward_rows = []
for f in central_features:
    p = f['properties']
    wno = p.get('ward_number')
    wkn = p.get('ward_name_kn', '')
    wen = p.get('ward_name_en', '')
    ackn = p.get('ac_name_kn', '')
    pop = f"{int(p['population']):,}" if p.get('population') else '—'
    corp_short = p.get('corporation_short_en', 'Central')

    active_cls = ' class="active"' if int(wno) == 4 else ''
    row = f"""          <tr id="ward_row_{corp_short}_{wno}"{active_cls} onclick="selectWardByNum('{corp_short}', {wno})">
            <td><span class="badge-ward-no">{wno}</span></td>
            <td><b>{wkn}</b><br><span style="font-size:11px;color:#64748B;">{wen}</span></td>
            <td><span style="font-size:12px;font-weight:700;color:#1E40AF;">{ackn}</span></td>
            <td>{pop}</td>
          </tr>"""
    ward_rows.append(row)

ward_rows_str = "\n".join(ward_rows)

with open('gba.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace empty tbody
old_tbody = '<tbody id="wardTableBody"></tbody>'
new_tbody = f'<tbody id="wardTableBody">\n{ward_rows_str}\n        </tbody>'

if old_tbody in html:
    html = html.replace(old_tbody, new_tbody)
    print("Pre-rendered 63 ward rows into #wardTableBody.")
else:
    print("Warning: old_tbody not found.")

# 2. Populate BWSSB 3-Tier Hierarchy in gba.html
# Division
html = html.replace(
    '<span id="resBwssbDivName" style="font-size:12px; font-weight:800; color:#1E3A8A;">-</span>',
    '<span id="resBwssbDivName" style="font-size:12px; font-weight:800; color:#1E3A8A;">ಕೇಂದ್ರ 1 ವಿಭಾಗ (Central 1 Division)</span>'
)
html = html.replace(
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbEeName">-</div>',
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbEeName">ನಾಗೇಂದ್ರ ಬಿ.</div>'
)
html = html.replace(
    '<a href="tel:1916" class="call-pill-blue" id="resBwssbEePhoneLink">📞 ಕರೆ ಮಾಡಿ</a>',
    '<a href="tel:9845444078" class="call-pill-blue" id="resBwssbEePhoneLink">📞 9845444078</a>'
)
html = html.replace(
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbEeOffice">📍 ಕಚೇರಿ: -</div>',
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbEeOffice">📍 ಕಚೇರಿ: ಮಿಲ್ಲರ್ಸ್ ರಸ್ತೆ, ಹೈಗ್ರೌಂಡ್ಸ್, ಬೆಂಗಳೂರು - 560052 (080-22945187)</div>'
)

# Sub-Division
html = html.replace(
    '<span id="resBwssbSubdivName" style="font-size:12px; font-weight:800; color:#1E3A8A;">-</span>',
    '<span id="resBwssbSubdivName" style="font-size:12px; font-weight:800; color:#1E3A8A;">ಸಿ-11 ಉಪವಿಭಾಗ (ಚಾಮರಾಜಪೇಟೆ / ಹೈಗ್ರೌಂಡ್ಸ್)</span>'
)
html = html.replace(
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbAeeName">-</div>',
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbAeeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>'
)
html = html.replace(
    '<a href="tel:1916" class="call-pill-blue" id="resBwssbAeePhoneLink">📞 ಕರೆ ಮಾಡಿ</a>',
    '<a href="tel:9900944041" class="call-pill-blue" id="resBwssbAeePhoneLink">📞 9900944041</a>'
)
html = html.replace(
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbAeeOffice">📍 ಕಚೇರಿ: -</div>',
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbAeeOffice">📍 ಕಚೇರಿ: #17, ಪಾರ್ಕ್ ರಸ್ತೆ, ತುಳಸಿ ತೋಟ, ಚಿಕ್ಕಲಾಲ್‌ಬಾಗ್, ಬೆಂಗಳೂರು - 560053 (080-22945188)</div>'
)

# Station
html = html.replace(
    '<span id="resBwssbStationName" style="font-size:12px; font-weight:800; color:#1E3A8A;">-</span>',
    '<span id="resBwssbStationName" style="font-size:12px; font-weight:800; color:#1E3A8A;">ಹೈಗ್ರೌಂಡ್ಸ್ / ಸಂಪಂಗಿರಾಮನಗರ ಸೇವಾ ಠಾಣೆ</span>'
)
html = html.replace(
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbAeName">-</div>',
    '<div style="font-size:13px; font-weight:900; color:#0F172A;" id="resBwssbAeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>'
)
html = html.replace(
    '<a href="tel:1916" class="call-pill-blue" id="resBwssbAePhoneLink">📞 ಕರೆ ಮಾಡಿ</a>',
    '<a href="tel:9900944041" class="call-pill-blue" id="resBwssbAePhoneLink">📞 9900944041</a>'
)
html = html.replace(
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbStationAddress">📍 ಠಾಣೆ: -</div>',
    '<div style="font-size:11px; color:#475569; margin-top:4px;" id="resBwssbStationAddress">📍 ಠಾಣೆ: ಮಿಲ್ಲರ್ಸ್ ರಸ್ತೆ, ಬಸವ ಭವನ ಹತ್ತಿರ, ಹೈಗ್ರೌಂಡ್ಸ್ (ವಿಧಾನಸೌಧ ವ್ಯಾಪ್ತಿ, 080-22945191)</div>'
)

with open('gba.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("gba.html updated successfully.")
