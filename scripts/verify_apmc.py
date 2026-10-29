import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<tbody id="hist-table-body">([\s\S]*?)</tbody>', text)
if m:
    rows = re.findall(r'<tr>', m.group(1))
    print("Total rows in hist-table-body:", len(rows))
    print("Contains 2016:", "2016" in m.group(1))
    print("Contains 2026:", "2026" in m.group(1))
    print("Contains ₹56,500:", "₹56,500" in m.group(1))
else:
    print("hist-table-body not found")
