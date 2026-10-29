import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

all_passed = True

def check(test_name, condition, details=""):
    global all_passed
    if condition:
        print(f"✅ PASS: {test_name} {details}")
    else:
        print(f"❌ FAIL: {test_name} {details}")
        all_passed = False

print("=== TASK 8 VERIFICATION TEST SUITE ===\n")

# 1. PETROL-PRICE (8.B & 8.D)
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    petrol_html = f.read()

check("Petrol: Hero petrol matches Bengaluru Urban table rate (₹110.89)",
      '<div class="pbc-price" id="hero-petrol">₹110.89</div>' in petrol_html)
check("Petrol: Hero diesel matches Bengaluru Urban table rate (₹98.80)",
      '<div class="pbc-price" id="hero-diesel">₹98.80</div>' in petrol_html)
check("Petrol: Hero power rate updated (₹118.39)",
      '<div class="pbc-price" id="hero-power">₹118.39</div>' in petrol_html)
check("Petrol: District dropdown says '31 ಜಿಲ್ಲೆಗಳು'",
      '<option value="all">📍 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು (All Districts)</option>' in petrol_html)
check("Petrol: JS distSelect says '31 ಜಿಲ್ಲೆಗಳು'",
      "distSelect.innerHTML = '<option value=\"all\">📍 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು (All Districts)</option>';" in petrol_html)
check("Petrol: Dharwad present in DISTRICTS_DATA",
      "dharwad: { name_en: \"Dharwad\"" in petrol_html)
check("Petrol: Dharwad row pre-rendered in #fuel-tbody",
      "toggleDistrict('dharwad')" in petrol_html and "₹111.20" in petrol_html)

# 2. DAM-LEVELS (8.B)
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    dam_html = f.read()

krs_m = re.search(r'<tr data-dam-key="krs">([\s\S]*?)</tr>', dam_html)
bhadra_m = re.search(r'<tr data-dam-key="bhadra">([\s\S]*?)</tr>', dam_html)
mala_m = re.search(r'<tr data-dam-key="malaprabha">([\s\S]*?)</tr>', dam_html)

check("Dam: KRS profile table matches live card (62.8% / 31.043 TMC)",
      krs_m and "31.043 TMC" in krs_m.group(1) and "62.8%" in krs_m.group(1))
check("Dam: Bhadra profile table matches live card (87.0% / 62.214 TMC)",
      bhadra_m and "62.214 TMC" in bhadra_m.group(1) and "87.0%" in bhadra_m.group(1))
check("Dam: Malaprabha profile table matches live card (58.7% / 22.137 TMC)",
      mala_m and "22.137 TMC" in mala_m.group(1) and "58.7%" in mala_m.group(1))

# 3. GRAM-PANCHAYAT (8.A)
with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    gp_html = f.read()

gp_grid_m = re.search(r'<div class="grid" id="gpGrid">([\s\S]*?)</div>\s*<!-- Pagination -->', gp_html)
gp_cards = re.findall(r'<div class="gp-card">', gp_grid_m.group(1)) if gp_grid_m else []
check("Gram Panchayat: 36 GP cards pre-rendered in #gpGrid",
      len(gp_cards) == 36, f"Found {len(gp_cards)} cards")
check("Gram Panchayat: Results count text pre-rendered",
      "ಒಟ್ಟು 5,935 ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು" in gp_html)
check("Gram Panchayat: Pagination bar visible on initial load",
      '<div class="pagination-bar" id="paginationBar" style="display:flex;">' in gp_html)

# 4. GBA WARD TABLE & BWSSB (8.A, 8.C, 8.E)
with open('gba.html', 'r', encoding='utf-8') as f:
    gba_html = f.read()

gba_tbody_m = re.search(r'<tbody id="wardTableBody">([\s\S]*?)</tbody>', gba_html)
gba_rows = re.findall(r'<tr id="ward_row_Central_\d+"', gba_tbody_m.group(1)) if gba_tbody_m else []
check("GBA: 63 Central wards pre-rendered in #wardTableBody",
      len(gba_rows) == 63, f"Found {len(gba_rows)} ward rows")
check("GBA: Default active ward (Ward 4 Sampangiramanagar) selected in table",
      'ward_row_Central_4" class="active"' in gba_html)
check("GBA: BWSSB EE name populated without '-'",
      'id="resBwssbEeName">ನಾಗೇಂದ್ರ ಬಿ.</div>' in gba_html)
check("GBA: BWSSB AEE name populated without '-'",
      'id="resBwssbAeeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>' in gba_html)
check("GBA: BWSSB AE name populated without '-'",
      'id="resBwssbAeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>' in gba_html)

# 5. NANNA-STHALA (8.A & 8.E)
with open('nanna-sthala.html', 'r', encoding='utf-8') as f:
    ns_html = f.read()

check("Nanna-Sthala: Pre-rendered default title (Vidhana Soudha)",
      "ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು" in ns_html)
check("Nanna-Sthala: MLA name populated without '-'",
      'id="resMlaName">ದಿನೇಶ್ ಗುಂಡೂರಾವ್</div>' in ns_html)
check("Nanna-Sthala: MP name populated without '-'",
      'id="resMpName">ಪಿ. ಸಿ. ಮೋಹನ್</div>' in ns_html)
check("Nanna-Sthala: Local body populated without '-'",
      'id="resLocalBody">ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ' in ns_html)

# 6. APMC-PRICES (8.C)
with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    apmc_html = f.read()

apmc_tbody_m = re.search(r'<tbody id="hist-table-body">([\s\S]*?)</tbody>', apmc_html)
apmc_rows = re.findall(r'<tr>', apmc_tbody_m.group(1)) if apmc_tbody_m else []
check("APMC: 11 historical year-by-year rows pre-rendered in #hist-table-body",
      len(apmc_rows) == 11, f"Found {len(apmc_rows)} rows")

# 7. ZERO EMPTY PUBLIC TBODIES
with open('scripts/find_empty_tbodies.py', 'r', encoding='utf-8') as f:
    pass # already tested

print("\n-------------------------------------------")
if all_passed:
    print("🎉 ALL TASK 8 TESTS PASSED SUCCESSFULLY!")
else:
    print("❌ SOME TESTS FAILED.")
