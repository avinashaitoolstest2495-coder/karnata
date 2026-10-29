# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
import json

ROOT_DIR = Path(".")
p = ROOT_DIR / "data" / "gold_rates.json"
d = json.load(open(p, "r", encoding="utf-8"))

bg = d.get("baseGold", {})
yg = d.get("yesterdayGold", {})
bs = d.get("baseSilver", {})

g24 = int(bg.get("24", 15671))
g22 = int(bg.get("22", 14360))
g18 = int(bg.get("18", 11750))
sil = float(bs.get("999", 260.0))
gsr = round(g24 / sil, 1)

print("Target values:")
print(f"24K: ₹{g24:,}")
print(f"22K: ₹{g22:,}")
print(f"18K: ₹{g18:,}")
print(f"Silver: ₹{sil:.2f}")
print(f"GSR: {gsr}")
