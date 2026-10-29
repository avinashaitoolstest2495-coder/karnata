import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.js', '.html', '.py')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    c = fp.read()
                    if 'petrol_rates' in c or 'historical_petrol' in c:
                        print(f"Found in: {path}")
            except Exception:
                pass
