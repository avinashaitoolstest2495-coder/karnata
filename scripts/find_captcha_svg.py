import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.js', '.html', '.py', '.json')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    if 'captchasvg' in fp.read().lower():
                        print(f"Found captchaSvg in: {path}")
            except Exception:
                pass
