import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('functions/api/voter-search.js', 'r', encoding='utf-8') as f:
    print(f.read())
