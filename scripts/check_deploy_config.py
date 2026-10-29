import sys, os
sys.stdout.reconfigure(encoding='utf-8')

if os.path.exists('wrangler.toml'):
    with open('wrangler.toml', 'r', encoding='utf-8') as f:
        print("=== wrangler.toml ===")
        print(f.read())

if os.path.exists('package.json'):
    with open('package.json', 'r', encoding='utf-8') as f:
        print("=== package.json ===")
        print(f.read())
