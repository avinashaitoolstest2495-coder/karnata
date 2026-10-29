import json, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

with open('data/gis/bengaluru_wards.geojson', 'r', encoding='utf-8') as f:
    geo = json.load(f)

corp_files = {
    'central': 'gba-central.html',
    'east': 'gba-east.html',
    'north': 'gba-north.html',
    'south': 'gba-south.html',
    'west': 'gba-west.html',
}

for corp_key, filename in corp_files.items():
    if not os.path.exists(filename):
        continue

    features = [f for f in geo['features'] if (f['properties'].get('corporation_short_en') or '').lower() == corp_key]
    features.sort(key=lambda x: int(x['properties'].get('ward_number', 0)))

    ward_rows = []
    first_ward = True
    for f in features:
        p = f['properties']
        wno = p.get('ward_number')
        wkn = p.get('ward_name_kn', '')
        wen = p.get('ward_name_en', '')
        ackn = p.get('ac_name_kn', '')
        pop = f"{int(p['population']):,}" if p.get('population') else '—'
        corp_short = p.get('corporation_short_en', corp_key.capitalize())

        active_cls = ' class="active"' if first_ward else ''
        first_ward = False

        row = f"""          <tr id="ward_row_{corp_short}_{wno}"{active_cls} onclick="selectWardByNum('{corp_short}', {wno})">
            <td><span class="badge-ward-no">{wno}</span></td>
            <td><b>{wkn}</b><br><span style="font-size:11px;color:#64748B;">{wen}</span></td>
            <td><span style="font-size:12px;font-weight:700;color:#1E40AF;">{ackn}</span></td>
            <td>{pop}</td>
          </tr>"""
        ward_rows.append(row)

    ward_rows_str = "\n".join(ward_rows)

    with open(filename, 'r', encoding='utf-8') as fp:
        html = fp.read()

    old_tbody = '<tbody id="wardTableBody"></tbody>'
    new_tbody = f'<tbody id="wardTableBody">\n{ward_rows_str}\n        </tbody>'

    if old_tbody in html:
        html = html.replace(old_tbody, new_tbody)
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(html)
        print(f"Pre-rendered {len(ward_rows)} wards into {filename}.")
    else:
        print(f"old_tbody not found in {filename}")
