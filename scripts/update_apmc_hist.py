import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('"arecanut": {')
end = text.find('    "coconut": {', start)
areca_json_str = "{" + text[start:end].rstrip().rstrip(',') + "}"
areca_data = json.loads(areca_json_str)["arecanut"]

print("Arecanut name:", areca_data["name"])
print("History entries:", len(areca_data["history"]))

unit = areca_data["unit"]
prevPrice = None
rows = []
for item in areca_data["history"]:
    year = item["year"]
    price = item["price"]
    min_val = item.get("min")
    max_val = item.get("max")
    event = item.get("event", "ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ನಿರಂತರ ವಹಿವಾಟು")

    yoy_badge = '—'
    if prevPrice is not None:
        diff = ((price - prevPrice) / prevPrice) * 100
        is_pos = diff >= 0
        sign = '+' if is_pos else ''
        cls = 'pos' if is_pos else 'neg'
        yoy_badge = f'<span class="hist-growth-badge {cls}">{sign}{diff:.1f}%</span>'
    prevPrice = price

    min_max_str = f'₹{min_val:,} - ₹{max_val:,}' if min_val and max_val else '—'

    row = f"""          <tr>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#0A3E20;">{year}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#15803D;">₹{price:,} / {unit}</td>
            <td style="font-family:'Inter',sans-serif; color:#64748B;">{min_max_str}</td>
            <td>{yoy_badge}</td>
            <td style="font-size:13px; color:#334155;">{event}</td>
          </tr>"""
    rows.append(row)

rows_str = "\n".join(rows)

old_tbody = '<tbody id="hist-table-body"></tbody>'
new_tbody = f'<tbody id="hist-table-body">\n{rows_str}\n        </tbody>'

if old_tbody in text:
    text = text.replace(old_tbody, new_tbody)
    with open('apmc-prices.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully pre-rendered 11 historical rows in apmc-prices.html.")
else:
    print("old_tbody not found in apmc-prices.html")
