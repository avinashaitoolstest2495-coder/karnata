import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

for dam in ['ಭದ್ರಾ', 'ಮಲಪ್ರಭಾ', 'ಕೃಷ್ಣರಾಜ']:
    idx = 0
    while True:
        idx = text.find(dam, idx)
        if idx == -1: break
        snippet = text[max(0, idx-100):min(len(text), idx+300)]
        if 'dam-card' in snippet or 'dam-storage-stat' in snippet or 'tbl-storage-cell' in snippet:
            print(f"=== {dam} ===")
            print(snippet)
        idx += len(dam)
