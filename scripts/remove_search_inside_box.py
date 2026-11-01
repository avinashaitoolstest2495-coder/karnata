# scripts/remove_search_inside_box.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ask.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the line:
# <div class="hero-sparkle">
#   <span>✨</span> ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ (Free AI 2.0)
# </div>
target_sparkle = """        <div class="hero-sparkle">
          <span>✨</span> ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ (Free AI 2.0)
        </div>"""

if target_sparkle in text:
    text = text.replace(target_sparkle, "")
    print("REMOVED: hero-sparkle HTML div")
else:
    print("WARNING: target_sparkle exact text not found, checking line-by-line")
    lines = text.splitlines(True)
    new_lines = []
    skip = False
    for l in lines:
        if 'hero-sparkle' in l and '<div' in l:
            skip = True
            continue
        if skip and '</div>' in l:
            skip = False
            continue
        if not skip:
            new_lines.append(l)
    text = "".join(new_lines)
    print("REMOVED: hero-sparkle lines via line filter")

# 2. Also remove .hero-sparkle from CSS
text = text.replace(""".hero-sparkle {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 999px;
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      color: #1D4ED8;
      font-size: 13.5px;
      font-weight: 800;
      margin-bottom: 16px;
    }""", "")

# 3. Aggressive CSS overrides to completely remove the inside box in the search box
old_query_css = """.query-input-elem {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #0F172A;
      font-size: 16px;
      font-weight: 600;
      font-family: inherit;
      line-height: 1.5;
    }"""

new_query_css = """.query-input-elem,
    input[type="text"].query-input-elem,
    .main-input-wrap input[type="text"],
    .docked-inner input[type="text"] {
      flex: 1 !important;
      background: transparent !important;
      background-color: transparent !important;
      border: none !important;
      border-width: 0 !important;
      outline: none !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      padding: 10px 0 !important;
      margin: 0 !important;
      color: #0F172A !important;
      font-size: 16px !important;
      font-weight: 600 !important;
      font-family: inherit !important;
      line-height: 1.5 !important;
    }
    .query-input-elem:focus,
    input[type="text"].query-input-elem:focus,
    .main-input-wrap input[type="text"]:focus,
    .docked-inner input[type="text"]:focus {
      background: transparent !important;
      background-color: transparent !important;
      border: none !important;
      border-width: 0 !important;
      outline: none !important;
      box-shadow: none !important;
    }"""

if old_query_css in text:
    text = text.replace(old_query_css, new_query_css)
    print("REPLACED: query-input-elem CSS with zero-border transparent styles")
else:
    print("WARNING: old_query_css exact match not found, injecting into <style>")
    idx = text.find('</style>')
    if idx != -1:
        text = text[:idx] + "\n" + new_query_css + "\n" + text[idx:]
        print("INJECTED: new_query_css into <style>")

with open('ask.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: ask.html updated cleanly.")
