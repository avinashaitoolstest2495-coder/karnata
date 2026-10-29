import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('gba.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<tbody id="wardTableBody">([\s\S]*?)</tbody>', text)
if m:
    rows = re.findall(r'<tr id="ward_row_Central_\d+"', m.group(1))
    print("Total ward rows in wardTableBody:", len(rows))
    print("Active row in wardTableBody:", 'ward_row_Central_4" class="active"' in m.group(1))

print("BWSSB Div name:", 'id="resBwssbDivName"' in text and 'ಕೇಂದ್ರ 1 ವಿಭಾಗ' in text)
print("BWSSB EE name:", 'id="resBwssbEeName">ನಾಗೇಂದ್ರ ಬಿ.</div>' in text)
print("BWSSB AEE name:", 'id="resBwssbAeeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>' in text)
print("BWSSB AE name:", 'id="resBwssbAeName">ಮಹೇಶ್ ಕುಮಾರ್ ಕೆ.ಎಸ್.</div>' in text)
print("Any '-' in BWSSB elements?:")
for elem in ['resBwssbDivName', 'resBwssbEeName', 'resBwssbEeOffice', 'resBwssbSubdivName', 'resBwssbAeeName', 'resBwssbAeeOffice', 'resBwssbStationName', 'resBwssbAeName', 'resBwssbStationAddress']:
    match = re.search(r'id="' + elem + r'">(?:📍 (?:ಕಚೇರಿ|ಠಾಣೆ): )?-<', text)
    if match:
        print(f"  Found '-' in {elem}")
    else:
        print(f"  OK: {elem} populated")
