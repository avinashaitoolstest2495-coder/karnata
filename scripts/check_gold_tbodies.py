import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('gold-rate.html', 'r', encoding='utf-8') as f:
    text = f.read()

tbodies = re.findall(r'<tbody[^>]*>([\s\S]*?)</tbody>', text)
print("Total tbodies in gold-rate.html:", len(tbodies))
for i, tb in enumerate(tbodies):
    rows = re.findall(r'<tr[^>]*>', tb)
    print(f"  tbody #{i+1}: {len(rows)} rows (empty: {len(rows) == 0})")
