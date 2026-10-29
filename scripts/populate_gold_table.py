import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('gold-rate.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'const HIST_125Y\s*=\s*(\[[\s\S]*?\]);', c)
if not m:
    print('Could not find HIST_125Y')
    sys.exit(1)

js_array_str = m.group(1)
clean_json = re.sub(r'(\w+):', r'"\1":', js_array_str)
clean_json = re.sub(r',\s*\]', ']', clean_json)
clean_json = re.sub(r',\s*\}', '}', clean_json)

data = json.loads(clean_json)
print(f'Successfully loaded {len(data)} historical records.')

rows = []
for h in data:
    g10 = f"{h['gold10g']:,}" if isinstance(h['gold10g'], int) or h['gold10g'].is_integer() else f"{h['gold10g']:,.2f}"
    g1 = f"{h['gold10g']/10:.2f}"
    s10 = f"{h['silver10g']:,}" if isinstance(h['silver10g'], int) or h['silver10g'].is_integer() else f"{h['silver10g']:,.2f}"
    event = h.get('event', '')
    row = f"""                <tr>
                  <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">{h['year']}</td>
                  <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹{g10}</td>
                  <td style="font-family:'Inter',sans-serif; color:#64748B;">₹{g1}</td>
                  <td style="font-family:'Inter',sans-serif; color:#475569;">₹{s10}</td>
                  <td style="font-size:13px; color:#334155;">{event}</td>
                </tr>"""
    rows.append(row)

table_body = '\n'.join(rows)
new_tbody = f'<tbody id="hist-125y-tbody">\n{table_body}\n              </tbody>'

old_tbody_pattern = r'<tbody id="hist-125y-tbody">[\s\S]*?</tbody>'
new_c = re.sub(old_tbody_pattern, new_tbody, c, count=1)

with open('gold-rate.html', 'w', encoding='utf-8') as f:
    f.write(new_c)

print(f'Pre-rendered {len(rows)} data rows into <tbody id="hist-125y-tbody"> in gold-rate.html')
