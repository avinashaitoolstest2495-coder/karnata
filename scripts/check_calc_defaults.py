import sys, re
sys.stdout.reconfigure(encoding='utf-8')

print("--- emi-calculator.html defaults ---")
with open('emi-calculator.html', 'r', encoding='utf-8') as f:
    emi_c = f.read()
for m in re.finditer(r'<input[^>]*value="([^"]*)"[^>]*id="([^"]*)"', emi_c):
    print(f"  id={m.group(2)}, val={m.group(1)}")

print("--- sip-calculator.html defaults ---")
with open('sip-calculator.html', 'r', encoding='utf-8') as f:
    sip_c = f.read()
for m in re.finditer(r'<input[^>]*value="([^"]*)"[^>]*id="([^"]*)"', sip_c):
    print(f"  id={m.group(2)}, val={m.group(1)}")
