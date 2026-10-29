import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('data/petrol_rates.json', 'r', encoding='utf-8') as f:
    rates = json.load(f)
print(json.dumps(rates, indent=2, ensure_ascii=False)[:2000])
