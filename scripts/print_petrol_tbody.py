import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(375, 400):
    print(f"{i+1}: {lines[i]}", end='')
