import json, base64, sys, re
sys.stdout.reconfigure(encoding='utf-8')

SECRET = 'NK_SECURE_KEY_2026_KARNATA'
with open('data/dam_levels.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

if 'payload' in raw:
    payload = base64.b64decode(raw['payload'])
    decoded = bytearray(len(payload))
    for i in range(len(payload)):
        decoded[i] = payload[i] ^ ord(SECRET[i % len(SECRET)])
    data = json.loads(decoded.decode('utf-8'))
else:
    data = raw

dams = data.get('dams', {})

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    html = f.read()

def update_row(match):
    key = match.group(1)
    inner = match.group(2)
    d = dams.get(key)
    if not d:
        return match.group(0)

    pct = d.get('storage_pct', 0)
    storage = d.get('present_storage_tmc', d.get('storage_tmc', 0))
    inflow = int(d.get('inflow_cusecs', 0))
    outflow = int(d.get('outflow_cusecs', 0))

    bg = '#dcfce7' if pct >= 90 else ('#e0f2fe' if pct >= 75 else ('#fef3c7' if pct >= 50 else '#fee2e2'))
    col = '#166534' if pct >= 90 else ('#0369a1' if pct >= 75 else ('#92400e' if pct >= 50 else '#991b1b'))

    new_storage_cell = f'<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-storage-cell"><strong>{storage} TMC</strong> <span style="background:{bg}; color:{col}; padding:2px 6px; border-radius:4px; font-size:12px; font-weight:700;">{pct}%</span></td>'
    new_flow_cell = f'<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-flow-cell"><span style="color:#16a34a; font-weight:600;">⬇️ {inflow:,}</span> / <span style="color:#2563eb; font-weight:600;">⬆️ {outflow:,}</span></td>'

    inner = re.sub(r'<td style="[^"]*" class="tbl-storage-cell">[\s\S]*?</td>', new_storage_cell, inner)
    inner = re.sub(r'<td style="[^"]*" class="tbl-flow-cell">[\s\S]*?</td>', new_flow_cell, inner)

    return f'<tr data-dam-key="{key}">{inner}</tr>'

new_html = re.sub(r'<tr data-dam-key="([^"]+)">([\s\S]*?)</tr>', update_row, html)

with open('dam-levels.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated dam-levels.html #dam-profile-tbody rows successfully.")
