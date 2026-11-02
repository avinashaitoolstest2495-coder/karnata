import re, json

txt = open('gold-rate.html', encoding='utf-8').read()
m = re.search(r'const GOLD_HIST_FULL = (\[[\s\S]*?\]);', txt)
hist = json.loads(m.group(1))
print('Total history items:', len(hist))
print('Latest date:', hist[-1]['date'])
rev = list(reversed(hist))
print('7-day slice dates:', [x['date'] for x in rev[:7]])
print('Chart container in HTML:', 'id="hist-chart-wrapper"' in txt)
print('Chart canvas in HTML:', 'id="histCreativeChart"' in txt)
print('renderHistoricalInteractiveChart in HTML:', 'function renderHistoricalInteractiveChart' in txt)
