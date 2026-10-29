import sys

sys.stdout.reconfigure(encoding='utf-8')

history = [
    {"year": "2016", "price": 28000, "min": 22000, "max": 31000, "event": "ನೋಟು ಅಮಾನ್ಯೀಕರಣದ ನಂತರ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ನಿಧಾನಗತಿಯ ವಹಿವಾಟು"},
    {"year": "2017", "price": 30500, "min": 24000, "max": 33500, "event": "ಗುಟ್ಕಾ ಮತ್ತು ಪಾನ್ ಮಸಾಲಾ ಉದ್ಯಮದಿಂದ ಹೊಸ ಬೇಡಿಕೆ ಆರಂಭ"},
    {"year": "2018", "price": 32500, "min": 26500, "max": 36000, "event": "ಮಲೆನಾಡಿನಲ್ಲಿ ಎಲೆಚುಕ್ಕಿ ರೋಗದ ಭೀತಿಯ ನಡುವೆಯೂ ಸ್ಥಿರ ದರ"},
    {"year": "2019", "price": 35000, "min": 29000, "max": 39500, "event": "ಉತ್ತರ ಭಾರತದ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಕರ್ನಾಟಕದ ರಾಶಿ ಅಡಿಕೆಗೆ ಭಾರಿ ಬೇಡಿಕೆ"},
    {"year": "2020", "price": 38000, "min": 31000, "max": 42000, "event": "ಕೋವಿಡ್ ಲಾಕ್‌ಡೌನ್ ಮಾರುಕಟ್ಟೆ ಪುನರಾರಂಭದ ನಂತರ ಭಾರಿ ಜಿಗಿತ"},
    {"year": "2021", "price": 44000, "min": 36000, "max": 48500, "event": "ಕ್ಯಾಂಪ್ಕೋ ವತಿಯಿಂದ ರೈತರಿಗೆ ದಾಖಲೆ ಮಟ್ಟದ ಧಾರಣೆ"},
    {"year": "2022", "price": 48500, "min": 41000, "max": 53000, "event": "ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹50,000 ಗಡಿ ದಾಟಿದ ರಾಶಿ ಅಡಿಕೆ"},
    {"year": "2023", "price": 50000, "min": 43000, "max": 54500, "event": "ಶಿವಮೊಗ್ಗ, ಸಾಗರ, ಶಿರಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ದೃಢ ಸ್ಥಿರತೆ"},
    {"year": "2024", "price": 52000, "min": 45000, "max": 57000, "event": "ರಫ್ತು ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಚಾಲಿ ಅಡಿಕೆಗೆ ಭಾರಿ ಪ್ರೀಮಿಯಂ ಬೆಲೆ"},
    {"year": "2025", "price": 54500, "min": 47000, "max": 59000, "event": "ಉತ್ತರ ಭಾರತದ ಕಂಪನಿಗಳ ಸ್ಪರ್ಧಾತ್ಮಕ ಬಿಡ್ಡಿಂಗ್"},
    {"year": "2026", "price": 56500, "min": 49000, "max": 62000, "event": "ಸಾರ್ವಕಾಲಿಕ ದಾಖಲೆ ಮಟ್ಟದಲ್ಲಿ ಅಡಿಕೆ ವಹಿವಾಟು"}
]

unit = "ಕ್ವಿಂಟಾಲ್"
prevPrice = None
rows = []
for item in history:
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

with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_tbody = '<tbody id="hist-table-body"></tbody>'
new_tbody = f'<tbody id="hist-table-body">\n{rows_str}\n        </tbody>'

if old_tbody in html:
    html = html.replace(old_tbody, new_tbody)
    with open('apmc-prices.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Pre-rendered 11 historical rows into apmc-prices.html successfully.")
else:
    print("Error: old_tbody not found in apmc-prices.html")
