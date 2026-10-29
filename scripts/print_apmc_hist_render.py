import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(4268, 4320):
    print(f"{i+1}: {lines[i]}", end='')
