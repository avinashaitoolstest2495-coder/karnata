import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ["bhadra", "ಭದ್ರಾ", "krs", "ಕೆಆರ್‌ಎಸ್", "malaprabha", "ಮಲಪ್ರಭಾ", "guide", "ಮಾರ್ಗದರ್ಶಿ", "ವಿವರವಾದ"]):
        print(f"{i+1}: {line.strip()[:140]}")
