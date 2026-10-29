# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from scripts.generate_daily_social_graphics import get_live_weather

w = get_live_weather()
iw = w.get("imd_warnings", {})

for k, v in list(iw.items()):
    print(f"{k:20} -> {v.get('level')} ({v.get('district_kn')})")
