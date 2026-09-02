#!/usr/bin/env python3
"""
Automated 24/7 Social Media Scheduler Runner for Karnata.in
Executes the exact 16 slots throughout the day based on IST time:

1.  07:15 AM — quote
2.  07:45 AM — petrol_diesel
3.  08:30 AM — weather_summary
4.  09:15 AM — apmc_rates
5.  09:45 AM — dam_levels
6.  10:15 AM — gold_rate
7.  10:45 AM — weather_nowcast_1
8.  11:30 AM — quiz_1
9.  12:30 PM — doyouknow_1
10. 01:45 PM — weather_nowcast_2
11. 02:30 PM — quiz_2
12. 04:00 PM — doyouknow_2
13. 04:45 PM — weather_nowcast_3
14. 05:45 PM — quiz_3
15. 07:15 PM — weather_nowcast_4
16. 08:00 PM — doyouknow_3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
HISTORY_FILE = ROOT_DIR / "data" / "social_publish_history.json"

SLOT_SCHEDULE = [
    ("quote", 7, 15),
    ("petrol_diesel", 7, 45),
    ("weather_summary", 8, 30),
    ("apmc_rates", 9, 15),
    ("dam_levels", 9, 45),
    ("gold_rate", 10, 15),
    ("weather_nowcast_1", 10, 45),
    ("quiz_1", 11, 30),
    ("doyouknow_1", 12, 30),
    ("weather_nowcast_2", 13, 45),
    ("quiz_2", 14, 30),
    ("doyouknow_2", 16, 0),
    ("weather_nowcast_3", 16, 45),
    ("quiz_3", 17, 45),
    ("weather_nowcast_4", 19, 15),
    ("doyouknow_3", 20, 0),
]

def load_history():
    today_str = datetime.now().strftime('%Y-%m-%d')
    if HISTORY_FILE.exists():
        try:
            d = json.load(open(HISTORY_FILE, 'r', encoding='utf-8'))
            if d.get("date") == today_str:
                return d
        except Exception:
            pass
    return {"date": today_str, "published_slots": []}

def save_history(history):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def check_and_publish_due_slots(dry_run=False):
    now = datetime.now()
    cur_mins = now.hour * 60 + now.minute
    history = load_history()
    published = history.get("published_slots", [])

    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] 🕒 Checking Social Publisher Due Slots (Current: {now.strftime('%I:%M %p')})...")
    print(f"  Already Published Today: {published}")

    due_slots = []
    for slot_key, h, m in SLOT_SCHEDULE:
        slot_mins = h * 60 + m
        # Trigger if within 30 minutes window and not published yet
        if cur_mins >= slot_mins and (cur_mins - slot_mins) <= 45:
            if slot_key not in published:
                due_slots.append((slot_key, h, m))

    if not due_slots:
        print("  [INFO] No slots currently due for publishing.")
        return

    for slot_key, h, m in due_slots:
        time_str = f"{h:02d}:{m:02d}"
        print(f"\n⚡ Slot Due: {slot_key} (Scheduled: {time_str})")

        # 1. Regenerate card if needed
        try:
            print(f"  [1/2] Regenerating graphic for {slot_key}...")
            from scripts.generate_daily_social_graphics import (
                render_quote_card, render_petrol_card, render_weather_morning_summary,
                render_apmc_carousel, render_dam_carousel_and_spotlights,
                render_gold_card, render_nowcast_map_card, render_quiz_interactive_card,
                render_doyouknow_card
            )

            fn_map = {
                "quote": render_quote_card,
                "petrol_diesel": render_petrol_card,
                "weather_summary": render_weather_morning_summary,
                "apmc_rates": render_apmc_carousel,
                "dam_levels": render_dam_carousel_and_spotlights,
                "gold_rate": render_gold_card,
                "weather_nowcast_1": render_nowcast_map_card,
                "quiz_1": lambda: render_quiz_interactive_card(1),
                "doyouknow_1": lambda: render_doyouknow_card(1),
                "weather_nowcast_2": render_nowcast_map_card,
                "quiz_2": lambda: render_quiz_interactive_card(2),
                "doyouknow_2": lambda: render_doyouknow_card(2),
                "weather_nowcast_3": render_nowcast_map_card,
                "quiz_3": lambda: render_quiz_interactive_card(3),
                "weather_nowcast_4": render_nowcast_map_card,
                "doyouknow_3": lambda: render_doyouknow_card(3),
            }

            if slot_key in fn_map:
                fn_map[slot_key]()
        except Exception as e:
            print(f"  [WARN] Graphic render exception for {slot_key}:", e)

        # 2. Publish to Meta (Facebook & Instagram)
        try:
            print(f"  [2/2] Publishing {slot_key} to Meta...")
            from scripts.auto_publish_social import publish_card
            ok = publish_card(slot_key, dry_run=dry_run)
            if ok:
                published.append(slot_key)
                history["published_slots"] = published
                save_history(history)
                print(f"  ✅ Successfully posted {slot_key}!")
        except Exception as e:
            print(f"  ❌ Publishing exception for {slot_key}:", e)

if __name__ == "__main__":
    is_dry = "--dry-run" in sys.argv
    check_and_publish_due_slots(dry_run=is_dry)
