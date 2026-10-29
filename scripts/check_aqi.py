import re
c = open('weather.html', 'r', encoding='utf-8').read()
matches = [line.strip() for line in c.splitlines() if 'aqi' in line.lower() and 'href' in line.lower()]
print('aqi href lines in weather.html:', matches)
