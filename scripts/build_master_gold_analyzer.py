# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_master_gold_analyzer.py
Comprehensive Gold & Commodity Price Intelligence, Buy/Sell Analyzer,
Jewellery Bill Calculator, Gold-to-Silver Ratio (GSR), and Investment Strategy Center.
"""

import json

# Read current gold rates data
with open("data/gold_rates.json", "r", encoding="utf-8") as f:
    gold_data = json.load(f)

gold_json_str = json.dumps(gold_data, ensure_ascii=False)

print("Loaded gold rates JSON successfully!")
