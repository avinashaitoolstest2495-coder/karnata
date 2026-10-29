import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data-loader.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("data-loader.js length:", len(text))
for line in text.splitlines()[:50]:
    print(line[:140])
