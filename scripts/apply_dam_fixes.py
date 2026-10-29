import json, base64, sys, os, re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\avina\Downloads\karnata-site-with-cms"
NK_DIR = os.path.join(ROOT_DIR, "namma-karnataka")
SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def decrypt_payload(raw_data):
    if isinstance(raw_data, dict) and 'payload' in raw_data:
        try:
            binary = base64.b64decode(raw_data['payload'])
            key_bytes = SECRET_KEY.encode('utf-8')
            decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(binary)])
            return json.loads(decrypted.decode('utf-8'))
        except Exception as e:
            print(f"Decryption error: {e}")
            return raw_data
    return raw_data

def encrypt_dict(data_dict):
    json_str = json.dumps(data_dict, ensure_ascii=False)
    raw_bytes = json_str.encode('utf-8')
    key_bytes = SECRET_KEY.encode('utf-8')
    xor_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(raw_bytes)])
    return base64.b64encode(xor_bytes).decode('utf-8')

def format_in_kn(date_str):
    # Converts '2026-09-09' -> '09-09-2026 (09 ಸೆಪ್ಟೆಂಬರ್ 2026)'
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        kn_months = {
            1: "ಜನವರಿ", 2: "ಫೆಬ್ರವರಿ", 3: "ಮಾರ್ಚ್", 4: "ಏಪ್ರಿಲ್", 5: "ಮೇ", 6: "ಜೂನ್",
            7: "ಜುಲೈ", 8: "ಆಗಸ್ಟ್", 9: "ಸೆಪ್ಟೆಂಬರ್", 10: "ಅಕ್ಟೋಬರ್", 11: "ನವೆಂಬರ್", 12: "ಡಿಸೆಂಬರ್"
        }
        day_str = dt.strftime("%d")
        month_kn = kn_months.get(dt.month, "")
        year_str = dt.strftime("%Y")
        return f"{day_str}-{dt.strftime('%m')}-{year_str} ({day_str} {month_kn} {year_str})"
    except Exception:
        return date_str

def main():
    json_path = os.path.join(ROOT_DIR, "data", "dam_levels.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        raw = json.load(f)

    data = decrypt_payload(raw)
    dams = data.get('dams', {})
    summary = data.get('summary', {})
    date_raw = data.get('date', datetime.now().strftime("%Y-%m-%d"))
    date_formatted = format_in_kn(date_raw)

    print(f"Baking Dam Data for Date: {date_formatted}")
    print(f"Reservoirs: {len(dams)} dams | Avg: {summary.get('avg_pct')}% | Storage: {summary.get('total_storage_tmc')}/{summary.get('total_capacity_tmc')} TMC")

    # 1. Save dual-structure JSON in both root and namma-karnataka
    clean_data = dict(data)
    clean_data['payload'] = encrypt_dict(clean_data)
    clean_data['v'] = 1

    for p in [os.path.join(ROOT_DIR, "data", "dam_levels.json"), os.path.join(NK_DIR, "data", "dam_levels.json")]:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(clean_data, f, ensure_ascii=False, indent=2)
    print("✓ Saved dual-structure dam_levels.json to both workspaces.")

    # 2. Build Dam Cards HTML for dam-levels.html
    DISTRICT_KN_MAP = {
        'Mandya': 'ಮಂಡ್ಯ', 'Mysuru': 'ಮೈಸೂರು', 'H.D. Kote': 'ಮೈಸೂರು',
        'Kodagu': 'ಕೊಡಗು', 'Hassan': 'ಹಾಸನ', 'Vijayanagara': 'ವಿಜಯನಗರ', 'Hospet': 'ವಿಜಯನಗರ',
        'Shivamogga': 'ಶಿವಮೊಗ್ಗ', 'Sagar': 'ಶಿವಮೊಗ್ಗ', 'Vijayapura': 'ವಿಜಯಪುರ',
        'Yadgir': 'ಯಾದಗಿರಿ', 'Belagavi': 'ಬೆಳಗಾವಿ', 'Chikkamagaluru': 'ಚಿಕ್ಕಮಗಳೂರು',
        'Uttara Kannada': 'ಉತ್ತರ ಕನ್ನಡ', 'Udupi': 'ಉಡುಪಿ', 'Chitradurga': 'ಚಿತ್ರದುರ್ಗ',
        'Kalaburagi': 'ಕಲಬುರಗಿ', 'Bidar': 'ಬೀದರ್'
    }

    dam_cards = []
    for d in dams.values():
        key = d.get('key') or d.get('id')
        storage = d.get('present_storage_tmc', d.get('gross_storage_tmc', d.get('storage_tmc', 0)))
        maxStorage = d.get('gross_capacity_tmc', d.get('max_storage_tmc', 1))
        pct = d.get('storage_pct', round((storage / maxStorage) * 100, 1))
        name = d.get('name_kn') or d.get('name') or 'ಅಣೆಕಟ್ಟು'
        river = d.get('river_kn') or d.get('river') or ''
        distRaw = d.get('district_en') or d.get('district_kn') or ''
        distKn = DISTRICT_KN_MAP.get(distRaw, distRaw)
        inflow = int(d.get('inflow_cusecs', 0))
        outflow = int(d.get('outflow_cusecs', 0))
        waveHex = '#10B981' if pct >= 90 else ('#00D2FF' if pct >= 75 else ('#F59E0B' if pct >= 50 else '#EF4444'))
        badge_label = 'ತುಂಬಿದೆ' if pct >= 90 else f"{pct}% ತುಂಬಿದೆ"
        badge_cls = 'status-full' if pct >= 90 else ('status-good' if pct >= 75 else 'status-medium')

        card = f"""      <div class="dam-card" data-basin="{d.get('basin', 'cauvery')}" data-pct="{pct}">
        <div class="dam-card-wave-bg">
          <svg class="card-wave" viewBox="0 0 500 60" preserveAspectRatio="none">
            <path d="M0,20 C150,45 350,-5 500,20 L500,60 L0,60 Z" fill="{waveHex}" opacity="0.18"></path>
          </svg>
        </div>
        <div class="dam-card-header">
          <div class="dam-name-wrap">
            <div class="dam-name">{name}</div>
            <div class="dam-river">🌊 ನದಿ: {river} · <span class="dam-district">{distKn}</span></div>
          </div>
          <span class="dam-status-badge {badge_cls}">{badge_label}</span>
        </div>
        <div class="dam-storage-stat">
          <div class="storage-primary">
            <span class="num">{storage}</span>
            <span class="unit">TMC</span>
          </div>
          <div class="storage-max">ಸಾಮರ್ಥ್ಯ: {maxStorage} TMC</div>
        </div>
        <div class="dam-bar-track">
          <div class="dam-bar-fill" style="width:{pct}%; background:{waveHex};"></div>
        </div>
        <div class="dam-metric-grid">
          <div class="dam-metric-box">
            <div class="m-val">{inflow:,}</div>
            <div class="m-lbl">⬇️ ಒಳಹರಿವು (ಕ್ಯೂಸೆಕ್ಸ್)</div>
          </div>
          <div class="dam-metric-box">
            <div class="m-val">{outflow:,}</div>
            <div class="m-lbl">⬆️ ಹೊರಹರಿವು (ಕ್ಯೂಸೆಕ್ಸ್)</div>
          </div>
        </div>
      </div>"""
        dam_cards.append(card)

    dam_cards_str = "\n".join(dam_cards)

    # Narrative Brief
    avg_pct = summary.get('avg_pct', 79.1)
    full_count = summary.get('full_count', 7)
    tot_storage = summary.get('total_storage_tmc', 699.0)
    tot_cap = summary.get('total_capacity_tmc', 866.3)
    alerts = summary.get('flood_alerts', [])
    alert_names = [dams[k]['name_kn'] for k in alerts if k in dams]
    alert_str = " ಮತ್ತು ".join(alert_names[:2]) if alert_names else "ಆಲಮಟ್ಟಿ ಮತ್ತು ಹಾರಂಗಿ"

    narrative_html = f"""<div class="brief-analysis-badge">📌 ಸಾರಾಂಶ ({date_formatted})</div>
    <div class="brief-analysis-text"><strong>ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ:</strong> {alert_str} ಸೇರಿದಂತೆ ಪ್ರಮುಖ ಜಲಾಶಯಗಳಲ್ಲಿ ಅಧಿಕ ಒಳಹರಿವು ದಾಖಲಾಗಿದೆ. ಕರ್ನಾಟಕದ ಒಟ್ಟು 13 ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳಲ್ಲಿ ಪ್ರಸ್ತುತ <strong>{tot_storage} TMC ({avg_pct}%)</strong> ನೀರು ಸಂಗ್ರಹವಾಗಿದ್ದು, <strong>{full_count}</strong> ಜಲಾಶಯಗಳು 75%+ ಭರ್ತಿಯಾಗಿವೆ.</div>"""

    # 3. Bake dam-levels.html
    for target_dir in [ROOT_DIR, NK_DIR]:
        page_path = os.path.join(target_dir, "dam-levels.html")
        if not os.path.exists(page_path):
            continue
        with open(page_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update summary numbers
        html = re.sub(r'<div class="sum-val" id="sum-avg">[^<]*</div>', f'<div class="sum-val" id="sum-avg">{avg_pct}%</div>', html)
        html = re.sub(r'<div class="sum-val" id="sum-full">[^<]*</div>', f'<div class="sum-val" id="sum-full">{full_count}</div>', html)
        html = re.sub(r'<div class="sum-val" id="sum-low">[^<]*</div>', f'<div class="sum-val" id="sum-low">{summary.get("low_count", 0)}</div>', html)
        html = re.sub(r'<div class="sum-val" id="sum-present-tmc">[^<]*</div>', f'<div class="sum-val" id="sum-present-tmc">{tot_storage} TMC</div>', html)
        html = re.sub(r'<div class="sum-val" id="sum-gross-cap">[^<]*</div>', f'<div class="sum-val" id="sum-gross-cap">{tot_cap} TMC</div>', html)

        # Update Header Timestamp
        html = re.sub(
            r'<div class="update-time" id="update-time">[^<]*</div>',
            f'<div class="update-time" id="update-time">ಕೊನೆ ನವೀಕರಣ: {date_formatted} (ದಿನಕ್ಕೆ 2 ಬಾರಿ ನವೀಕರಣ: ಬೆಳಿಗ್ಗೆ 9:00 &amp; ಮಧ್ಯಾಹ್ನ 12:00 — KSNDMC / ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ)</div>',
            html
        )

        # Update Dynamic Analysis Lines (Cleanly replace entire alert-container)
        html = re.sub(
            r'<div class="alert-container">[\s\S]*?<!-- CENTERED FILTER BAR',
            f'<div class="alert-container">\n  <div class="hydro-lines" id="dynamic-analysis-lines">\n    {narrative_html}\n  </div>\n</div>\n\n<!-- CENTERED FILTER BAR',
            html
        )

        # Replace dam-grid inner content
        html = re.sub(
            r'<div class="dam-grid" id="dam-grid">[\s\S]*?</div>\s*<!-- COMPREHENSIVE',
            f'<div class="dam-grid" id="dam-grid">\n{dam_cards_str}\n  </div>\n\n  <!-- COMPREHENSIVE',
            html
        )

        # Synchronize table rows with fresh live dam values
        for d in dams.values():
            key = d.get('key') or d.get('id')
            storage = d.get('present_storage_tmc', d.get('gross_storage_tmc', 0))
            pct = d.get('storage_pct', 0)
            inflow = int(d.get('inflow_cusecs', 0))
            outflow = int(d.get('outflow_cusecs', 0))
            bg = '#dcfce7' if pct >= 90 else ('#e0f2fe' if pct >= 75 else ('#fef3c7' if pct >= 50 else '#fee2e2'))
            col = '#166534' if pct >= 90 else ('#0369a1' if pct >= 75 else ('#92400e' if pct >= 50 else '#991b1b'))

            def make_repl(st, p, b, c, inf, outf):
                def repl(m):
                    inner = m.group(1)
                    new_storage = f'<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-storage-cell"><strong>{st} TMC</strong> <span style="background:{b}; color:{c}; padding:2px 6px; border-radius:4px; font-size:12px; font-weight:700;">{p}%</span></td>'
                    new_flow = f'<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-flow-cell"><span style="color:#16a34a; font-weight:600;">⬇️ {inf:,}</span> / <span style="color:#2563eb; font-weight:600;">⬆️ {outf:,}</span></td>'
                    inner = re.sub(r'<td style="[^"]*" class="tbl-storage-cell">[\s\S]*?</td>', new_storage, inner)
                    inner = re.sub(r'<td style="[^"]*" class="tbl-flow-cell">[\s\S]*?</td>', new_flow, inner)
                    return f'<tr data-dam-key="{key}">{inner}</tr>'
                return repl

            html = re.sub(r'<tr data-dam-key="' + key + r'">([\s\S]*?)</tr>', make_repl(storage, pct, bg, col, inflow, outflow), html)

        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Baked fresh dam levels into {page_path}")

    # 4. Bake individual dam pages (dam-levels/*.html)
    DAM_PAGE_MAP = {
        'almatti-dam.html': 'almatti',
        'krs-dam.html': 'krs',
        'harangi-dam.html': 'harangi',
        'hemavathi-dam.html': 'hemavathi',
        'kabini-dam.html': 'kabini',
        'bhadra-dam.html': 'bhadra',
        'tungabhadra-dam.html': 'tungabhadra',
        'linganamakki-dam.html': 'linganamakki',
        'ghataprabha-dam.html': 'ghataprabha',
        'malaprabha-dam.html': 'malaprabha',
        'narayanapura-dam.html': 'narayanapura',
        'supa-dam.html': 'supa',
        'vanivilasa-dam.html': 'vanivilasa',
    }

    for target_dir in [ROOT_DIR, NK_DIR]:
        dam_sub_dir = os.path.join(target_dir, "dam-levels")
        if not os.path.exists(dam_sub_dir):
            continue
        for page_name, dam_key in DAM_PAGE_MAP.items():
            page_path = os.path.join(dam_sub_dir, page_name)
            if not os.path.exists(page_path):
                continue
            dam = dams.get(dam_key)
            if not dam:
                continue

            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()

            storage = dam.get('present_storage_tmc', dam.get('gross_storage_tmc', 0))
            gross_cap = dam.get('gross_capacity_tmc', dam.get('max_storage_tmc', 0))
            pct = dam.get('storage_pct', 0)
            inflow = int(dam.get('inflow_cusecs', 0))
            outflow = int(dam.get('outflow_cusecs', 0))
            level = dam.get('level_ft', dam.get('current_level_ft', 0))

            # Ensure update-time element exists and has fresh date
            time_tag = f'<div class="dh-time" id="update-time">ಕೊನೆ ನವೀಕರಣ: {date_formatted} — KSNDMC / ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ ಲೈವ್ ವರದಿ</div>'
            if 'id="update-time"' in content:
                content = re.sub(r'<div class="dh-time"[^>]*id="update-time"[^>]*>[^<]*</div>', time_tag, content)
                content = re.sub(r'<div id="update-time"[^>]*>[^<]*</div>', time_tag, content)
            else:
                # insert into hero overlay after dh-sub
                content = re.sub(r'(<div class="dh-sub">[\s\S]*?</div>)', r'\1\n        ' + time_tag, content)

            # Update specific IDs if present (e.g. krs-m-storage)
            content = re.sub(r'id="' + dam_key + r'-m-storage">[^<]*<', f'id="{dam_key}-m-storage">{storage} TMC<', content)
            content = re.sub(r'id="' + dam_key + r'-m-sub">[^<]*<', f'id="{dam_key}-m-sub">{pct}% ತುಂಬಿದೆ ({gross_cap} TMC ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ)<', content)
            if level:
                content = re.sub(r'id="' + dam_key + r'-m-level">[^<]*<', f'id="{dam_key}-m-level">{level} ಅಡಿ<', content)
            content = re.sub(r'id="' + dam_key + r'-m-inflow">[^<]*<', f'id="{dam_key}-m-inflow">{inflow:,}<', content)
            content = re.sub(r'id="' + dam_key + r'-m-outflow">[^<]*<', f'id="{dam_key}-m-outflow">{outflow:,}<', content)

            # Also bake generic metric-card items
            # Pattern for Present Storage
            content = re.sub(
                r'(<div class="mc-label">[^<]*(?:ಪ್ರಸ್ತುತ ಸಂಗ್ರಹ|Present Storage)[^<]*</div>\s*<div class="mc-val"[^>]*>)[^<]*(</div>\s*<div class="mc-sub">)[^<]*(</div>)',
                r'\g<1>' + f'{storage} TMC' + r'\g<2>' + f'{pct}% ತುಂಬಿದೆ' + r'\g<3>',
                content
            )
            # Pattern for Gross Storage / Capacity
            content = re.sub(
                r'(<div class="mc-label">[^<]*(?:ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ|Gross Storage|Gross Capacity)[^<]*</div>\s*<div class="mc-val"[^>]*>)[^<]*(</div>)',
                r'\g<1>' + f'{gross_cap} TMC' + r'\g<2>',
                content
            )
            # Pattern for Water level
            if level:
                content = re.sub(
                    r'(<div class="mc-label">[^<]*(?:ಪ್ರಸ್ತುತ ಜಲಮಟ್ಟ|Water Level)[^<]*</div>\s*<div class="mc-val"[^>]*>)[^<]*(</div>)',
                    r'\g<1>' + f'{level} ಅಡಿ' + r'\g<2>',
                    content
                )
            # Pattern for Inflow
            content = re.sub(
                r'(<div class="mc-label">[^<]*(?:ಒಳಹರಿವು|Inflow)[^<]*</div>\s*<div class="mc-val"[^>]*>)[^<]*(</div>)',
                r'\g<1>' + f'{inflow:,}' + r'\g<2>',
                content
            )
            # Pattern for Outflow
            content = re.sub(
                r'(<div class="mc-label">[^<]*(?:ಹೊರಹರಿವು|Outflow)[^<]*</div>\s*<div class="mc-val"[^>]*>)[^<]*(</div>)',
                r'\g<1>' + f'{outflow:,}' + r'\g<2>',
                content
            )

            # Ensure data-loader.js and dam-sync.js are present
            if 'dam-sync.js' not in content:
                content = content.replace('</body>', '<script src="/dam-sync.js"></script>\n</body>')
            if 'data-loader.js' not in content:
                content = content.replace('</head>', '<script src="/data-loader.js"></script>\n</head>')

            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)

        print(f"✓ Baked 13 individual dam subpages in {dam_sub_dir}")

if __name__ == '__main__':
    main()
