# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.getcwd()
sys.path.insert(0, ROOT_DIR)
from scripts.build_complete_125_years_dataset import full_126_years

print(f'Total historical records available: {len(full_126_years)}')

rows = []
for r in full_126_years:
    g10 = f"{r['gold_10g']:,.2f}" if r['gold_10g'] % 1 != 0 else f"{int(r['gold_10g']):,}"
    g1 = f"{r['gold_24k_per_gram']:,.2f}"
    s10 = f"{r['silver_10g']:,.2f}" if r['silver_10g'] % 1 != 0 else f"{int(r['silver_10g']):,}"
    event = r['milestone']
    
    row = f'''                <tr>
                  <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">{r['year']}</td>
                  <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹{g10}</td>
                  <td style="font-family:'Inter',sans-serif; color:#64748B;">₹{g1}</td>
                  <td style="font-family:'Inter',sans-serif; color:#475569;">₹{s10}</td>
                  <td style="font-size:13px; color:#334155;">{event}</td>
                </tr>'''
    rows.append(row)

table_body = '\n'.join(rows)
tbody_html = f'<tbody id="hist-125y-tbody">\n{table_body}\n              </tbody>'

for target_file in ['gold-rate.html', 'namma-karnataka/gold-rate.html']:
    if not os.path.exists(target_file): continue
    with open(target_file, 'r', encoding='utf-8') as f:
        html = f.read()

    import re
    new_html = re.sub(r'<tbody id="hist-125y-tbody">[\s\S]*?</tbody>', tbody_html, html, count=1)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'Successfully injected {len(rows)} pre-rendered rows into {target_file}')

