import json

with open('data/petrol_rates.json', 'r', encoding='utf-8') as f:
    rates = json.load(f)

print("data/petrol_rates.json keys:", list(rates.keys()) if isinstance(rates, dict) else len(rates))
if isinstance(rates, dict):
    for k, v in list(rates.items())[:5]:
        print(k, ":", v)
    if 'bengaluru' in rates or 'bengaluru_urban' in rates:
        print("Bengaluru in rates:", rates.get('bengaluru') or rates.get('bengaluru_urban'))

with open('data/historical_petrol.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)
print("historical_petrol keys/len:", len(hist) if isinstance(hist, list) else list(hist.keys())[:5])
