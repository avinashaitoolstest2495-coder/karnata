import sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('namma-karnataka/wrangler.toml', 'r', encoding='utf-8') as f:
    print(f.read())
