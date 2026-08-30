import re

with open('weather.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for idx, line in enumerate(lines):
    # Count <div> and </div>
    open_divs = len(re.findall(r'<div[\s>]', line, re.IGNORECASE))
    close_divs = len(re.findall(r'</div>', line, re.IGNORECASE))
    
    depth += open_divs - close_divs
    if depth < 0:
        print(f"EXTRA CLOSE at line {idx+1}: {line.strip()} (Depth became {depth})")
        # Reset or track
        depth = 0

print(f"Final depth at end of file: {depth}")
