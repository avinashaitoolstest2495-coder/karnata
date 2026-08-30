# -*- coding: utf-8 -*-
"""
Karnata — scripts/connect_gold_frontend_to_llm_api.py
Fixes newline escaping in JS.
"""

with open("gold-rate.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the broken string split
html = html.replace("let formatted = resData.answer.split('\n').join('<br>');", "let formatted = resData.answer.split('\\n').join('<br>');")

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_ESCAPING_FIXED")
