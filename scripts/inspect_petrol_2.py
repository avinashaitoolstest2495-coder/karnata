import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- LINES 350-400 ---")
for i in range(350, 400):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')

print("--- LINES 800-880 ---")
for i in range(800, 880):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
