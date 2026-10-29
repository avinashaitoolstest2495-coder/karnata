import os

print("Wrangler files or cloudflare configs:")
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if 'wrangler' in f.lower() or 'cloudflare' in f.lower() or f.endswith('.toml'):
            print(os.path.join(root, f))
