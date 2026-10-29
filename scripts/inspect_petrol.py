import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ["30", "31", "ಬೆಂಗಳೂರು", "₹", "price-val", "districtTable"]):
        print(f"{i+1}: {line.strip()[:120]}")
