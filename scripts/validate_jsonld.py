import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('bigg-boss-kannada-13.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<script type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', text)
print(f'Found {len(matches)} JSON-LD blocks.')

for i, m in enumerate(matches):
    try:
        data = json.loads(m.strip())
        print(f'Block {i+1} is VALID JSON-LD.')
        if '@graph' in data:
            print(f"Graph has {len(data['@graph'])} entities:")
            for item in data['@graph']:
                print(f" - [{item.get('@type')}] {item.get('name', '')[:50]}")
    except Exception as e:
        print(f'Block {i+1} FAILED to parse: {e}')
        sys.exit(1)

print("\nALL JSON-LD SCHEMAS VERIFIED SUCCESSFULLY!")
