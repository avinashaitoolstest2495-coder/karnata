import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

for k in ['sum-avg', 'sum-full', 'sum-low', 'sum-present-tmc', 'sum-gross-cap', 'update-time']:
    start = text.find(f'id="{k}"')
    if start != -1:
        print(text[max(0, start-20):min(len(text), start+80)])
