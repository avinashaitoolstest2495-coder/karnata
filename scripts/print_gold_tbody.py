import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gold-rate.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(945, 985):
    print(f"{i+1}: {lines[i]}", end='')
