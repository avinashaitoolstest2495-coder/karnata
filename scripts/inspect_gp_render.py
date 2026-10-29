import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- LINES 530-560 ---")
for i in range(530, 560):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')

print("\n--- LINES 704-760 ---")
for i in range(704, 760):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
