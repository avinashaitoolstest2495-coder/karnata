import sys, json, os

sys.stdout.reconfigure(encoding='utf-8')

print("--- 1. petrol-price.html ---")
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if "30" in line or "31" in line or "nearest" in line.lower() or "price-card" in line.lower() or "tbody" in line.lower() or "bengaluru" in line.lower() or "ಬೆಂಗಳೂರು" in line:
        if len(line.strip()) < 150:
            print("PETROL:", line.strip())

print("\n--- 2. dam-levels.html ---")
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    dtext = f.read()

for line in dtext.splitlines():
    if "bhadra" in line.lower() or "ಭದ್ರಾ" in line or "krs" in line.lower() or "ಕೆಆರ್‌ಎಸ್" in line or "malaprabha" in line.lower() or "ಮಲಪ್ರಭಾ" in line:
        if len(line.strip()) < 150:
            print("DAM:", line.strip())

print("\n--- 3. gold-rate.html 10-year table ---")
with open('gold-rate.html', 'r', encoding='utf-8') as f:
    gtext = f.read()

for line in gtext.splitlines():
    if "10" in line and ("year" in line.lower() or "ವರ್ಷ" in line or "table" in line.lower() or "tbody" in line.lower()):
        print("GOLD 10Y:", line.strip()[:150])

print("\n--- 4. apmc-prices.html 10-year table ---")
with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    atext = f.read()

for line in atext.splitlines():
    if ("10" in line or "ವರ್ಷ" in line or "hist" in line.lower()) and ("table" in line.lower() or "tbody" in line.lower() or "tr" in line.lower()):
        print("APMC 10Y:", line.strip()[:150])

print("\n--- 5. gba.html ward & bwssb ---")
with open('gba.html', 'r', encoding='utf-8') as f:
    gbtext = f.read()

for line in gbtext.splitlines():
    if "wardtable" in line.lower() or "bwssb" in line.lower() or 'id="res' in line.lower():
        print("GBA:", line.strip()[:150])

print("\n--- 6. nanna-sthala.html ---")
with open('nanna-sthala.html', 'r', encoding='utf-8') as f:
    nstext = f.read()

for line in nstext.splitlines():
    if 'id="res' in line.lower() or "ಸ್ಥಳವನ್ನು" in line:
        print("NANNA-STHALA:", line.strip()[:150])

