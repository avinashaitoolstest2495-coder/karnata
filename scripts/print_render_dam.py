import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('function renderDam(')
if start != -1:
    end = text.find('function renderAllDams', start)
    print(text[start:end])
