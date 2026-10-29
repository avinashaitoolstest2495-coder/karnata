import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('petrol-price.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero prices
content = content.replace(
    '<div class="pbc-price" id="hero-petrol">₹102.86</div>',
    '<div class="pbc-price" id="hero-petrol">₹110.89</div>'
)
content = content.replace(
    '<div class="pbc-price" id="hero-diesel">₹88.94</div>',
    '<div class="pbc-price" id="hero-diesel">₹98.80</div>'
)
content = content.replace(
    '<div class="pbc-price" id="hero-power">₹110.36</div>',
    '<div class="pbc-price" id="hero-power">₹118.39</div>'
)

# 2. Update district count label "30 ಜಿಲ್ಲೆಗಳು" -> "31 ಜಿಲ್ಲೆಗಳು"
content = content.replace(
    '<option value="all">📍 ಎಲ್ಲಾ 30 ಜಿಲ್ಲೆಗಳು (All Districts)</option>',
    '<option value="all">📍 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು (All Districts)</option>'
)
content = content.replace(
    "distSelect.innerHTML = '<option value=\"all\">📍 ಎಲ್ಲಾ 30 ಜಿಲ್ಲೆಗಳು (All Districts)</option>';",
    "distSelect.innerHTML = '<option value=\"all\">📍 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು (All Districts)</option>';"
)
content = content.replace(
    "// MASTER DISTRICT & CITIES DATASET (30 Districts, 189 Cities)",
    "// MASTER DISTRICT & CITIES DATASET (31 Districts, 196 Cities)"
)

# 3. Add Dharwad to DISTRICTS_DATA
dharwad_data = """  dharwad: { name_en: "Dharwad", name_kn: "ಧಾರವಾಡ", taluks: { hubballi: { name_en: "Hubballi", name_kn: "ಹುಬ್ಬಳ್ಳಿ", latitude: 15.3647, longitude: 75.124, petrol: 111.2, diesel: 99.12 }, dharwad: { name_en: "Dharwad", name_kn: "ಧಾರವಾಡ", latitude: 15.4589, longitude: 75.0078, petrol: 111.2, diesel: 99.12 }, kalghatgi: { name_en: "Kalghatgi", name_kn: "ಕಲಘಟಗಿ", latitude: 15.1822, longitude: 74.9744, petrol: 111.2, diesel: 99.12 }, kundgol: { name_en: "Kundgol", name_kn: "ಕುಂದಗೋಳ", latitude: 15.257, longitude: 75.253, petrol: 111.2, diesel: 99.12 }, navalgund: { name_en: "Navalgund", name_kn: "ನವಲಗುಂದ", latitude: 15.566, longitude: 75.365, petrol: 111.2, diesel: 99.12 }, alnavar: { name_en: "Alnavar", name_kn: "ಅಳ್ನಾವರ", latitude: 15.433, longitude: 74.733, petrol: 111.2, diesel: 99.12 }, annigeri: { name_en: "Annigeri", name_kn: "ಅಣ್ಣಿಗೇರಿ", latitude: 15.435, longitude: 75.432, petrol: 111.2, diesel: 99.12 } } },"""

# We can insert dharwad right after belagavi in DISTRICTS_DATA
if "dharwad:" not in content:
    content = content.replace(
        '  belagavi: { name_en: "Belagavi"',
        dharwad_data + '\n  belagavi: { name_en: "Belagavi"'
    )

# 4. Pre-render Dharwad in #fuel-tbody
dharwad_row = """    <tr class="dist-row" onclick="toggleDistrict('dharwad')">
      <td><span class="acc-arrow" id="arr-dharwad">▶</span><span class="d-kn">ಧಾರವಾಡ</span></td>
      <td>₹111.20</td>
      <td>₹99.12</td>
    </tr>"""

if "toggleDistrict('dharwad')" not in content:
    # insert after belagavi row in tbody
    content = re.sub(
        r'(<tr class="dist-row" onclick="toggleDistrict\(\'belagavi\'\)">[\s\S]*?</tr>)',
        r'\1\n' + dharwad_row,
        content
    )

with open('petrol-price.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("petrol-price.html updated successfully.")
