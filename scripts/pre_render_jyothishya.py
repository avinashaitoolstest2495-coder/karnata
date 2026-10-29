import sys

sys.stdout.reconfigure(encoding='utf-8')

planets = [
    {"symbol": "☀️", "name_kn": "ಸೂರ್ಯ (Sun)", "rashi": "ಸಿಂಹ", "degreeFormatted": "16° 42'", "nakshatra": "ಪುಬ್ಬಾ", "pada": "2", "house": "1"},
    {"symbol": "🌙", "name_kn": "ಚಂದ್ರ (Moon)", "rashi": "ವೃಷಭ", "degreeFormatted": "12° 18'", "nakshatra": "ರೋಹಿಣಿ", "pada": "1", "house": "2"},
    {"symbol": "♂️", "name_kn": "ಕುಜ (Mars)", "rashi": "ಮಿಥುನ", "degreeFormatted": "08° 35'", "nakshatra": "ಮೃಗಶಿರಾ", "pada": "3", "house": "3"},
    {"symbol": "☿️", "name_kn": "ಬುಧ (Mercury)", "rashi": "ಕನ್ಯಾ", "degreeFormatted": "14° 50'", "nakshatra": "ಹಸ್ತಾ", "pada": "2", "house": "4"},
    {"symbol": "♃", "name_kn": "ಗುರು (Jupiter)", "rashi": "ವೃಷಭ", "degreeFormatted": "20° 15'", "nakshatra": "ರೋಹಿಣಿ", "pada": "4", "house": "5"},
    {"symbol": "♀️", "name_kn": "ಶುಕ್ರ (Venus)", "rashi": "ತುಲಾ", "degreeFormatted": "05° 28'", "nakshatra": "ಚಿತ್ತಾ", "pada": "3", "house": "6"},
    {"symbol": "♄", "name_kn": "ಶನಿ (Saturn)", "rashi": "ಕುಂಭ", "degreeFormatted": "22° 40'", "nakshatra": "ಪೂರ್ವಾಭಾದ್ರಾ", "pada": "1", "house": "7"},
    {"symbol": "☊", "name_kn": "ರಾಹು (Rahu)", "rashi": "ಮೀನ", "degreeFormatted": "11° 12'", "nakshatra": "ಉತ್ತರಾಭಾದ್ರಾ", "pada": "2", "house": "8"},
    {"symbol": "☋", "name_kn": "ಕೇತು (Ketu)", "rashi": "ಕನ್ಯಾ", "degreeFormatted": "11° 12'", "nakshatra": "ಉತ್ತರಾಫಲ್ಗುಣಿ", "pada": "4", "house": "9"},
]

rows = []
for p in planets:
    row = f"""                  <tr>
                    <td style="font-weight:800; color:#0F172A;">{p['symbol']} {p['name_kn']}</td>
                    <td>{p['rashi']}</td>
                    <td style="font-family:var(--font-en); font-weight:700;">{p['degreeFormatted']}</td>
                    <td>{p['nakshatra']} ({p['pada']}ನೇ ಪಾದ)</td>
                    <td style="font-weight:900; color:var(--k-red);">{p['house']}ನೇ ಭಾವ</td>
                  </tr>"""
    rows.append(row)

rows_str = "\n".join(rows)

with open('ai-jyothishya.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_tbody = '<tbody id="planets-tbody"></tbody>'
new_tbody = f'<tbody id="planets-tbody">\n{rows_str}\n                </tbody>'

if old_tbody in html:
    html = html.replace(old_tbody, new_tbody)
    with open('ai-jyothishya.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Pre-rendered navagraha positions into ai-jyothishya.html successfully.")
else:
    print("old_tbody not found in ai-jyothishya.html")
