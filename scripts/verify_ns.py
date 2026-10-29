import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('nanna-sthala.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Title populated:", "ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು" in text)
print("MLA Name:", 'id="resMlaName">ದಿನೇಶ್ ಗುಂಡೂರಾವ್</div>' in text)
print("MP Name:", 'id="resMpName">ಪಿ. ಸಿ. ಮೋಹನ್</div>' in text)
print("Local Body:", 'id="resLocalBody">ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ' in text)
print("Any '-' in res elements?:")
for elem in ['resMlaName', 'resMlaConst', 'resMlaParty', 'resMpName', 'resMpConst', 'resMpParty', 'resLocalBody', 'resWard', 'resZone', 'resDistrict']:
    match = re.search(r'id="' + elem + r'">-</', text)
    if match:
        print(f"  Found '-' in {elem}")
    else:
        print(f"  OK: {elem} populated")
