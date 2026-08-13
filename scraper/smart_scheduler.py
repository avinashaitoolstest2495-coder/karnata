"""
Karnata — smart_scheduler.py
Online automated cloud scheduler adhering strictly to IST time windows.
Used by GitHub Actions, Windows Task Scheduler, and main.py daemon.

Schedule (IST - UTC+5:30):
- Petrol Price: Daily morning
- Gold Price: Daily morning & afternoon
- Dam Water Levels: 5x daily
- Weather Telemetry: Every hour
- APMC Prices: 4x daily
- Local News: Every 3 hours
- AI News Publisher: 3x daily
"""

import os
import sys
import time
from datetime import datetime, timezone, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gold_scraper import run as run_gold
from petrol_scraper import run as run_petrol
from dam_scraper import run as run_dam
from apmc_scraper import run as run_apmc
from weather_scraper import run as run_weather
from local_news_scraper import run as run_local_news
from ai_news_publisher import run as run_ai_news
from utils import log


def get_ist_now():
    return datetime.now(timezone(timedelta(hours=5, minutes=30)))


def run_all_scrapers():
    """Execute all scrapers in optimal order."""
    log.info("🚀 Running ALL Karnata scrapers...")
    try_run("Gold & Silver Scraper", run_gold)
    try_run("Petrol & Diesel Scraper", run_petrol)
    try_run("Dam Levels Scraper", run_dam)
    try_run("APMC Prices Scraper", run_apmc)
    try_run("Weather Scraper", run_weather)
    try_run("Local News RSS Scraper", run_local_news)
    try_run("AI News Publisher", lambda: run_ai_news(3))


def run_scheduled_scrapers(force_all=False):
    if force_all:
        run_all_scrapers()
        return

    ist_now = get_ist_now()
    hour = ist_now.hour
    minute = ist_now.minute

    log.info(f"🕒 Current IST Time: {ist_now.strftime('%Y-%m-%d %I:%M:%S %p')} (Hour: {hour}, Minute: {minute})")

    # Run weather every hour
    try_run("Weather Scraper (Hourly)", run_weather)
    try_run("Local News RSS Scraper", run_local_news)

    # Gold: morning (6-11 AM) and afternoon (3-6 PM)
    if (6 <= hour <= 11) or (15 <= hour <= 18):
        try_run("Gold Scraper", run_gold)

    # Petrol: morning (6-10 AM)
    if 6 <= hour <= 10:
        try_run("Petrol Scraper", run_petrol)

    # Dam Levels: 7 AM, 10 AM, 1 PM, 5 PM, 8 PM
    if hour in (7, 8, 10, 11, 13, 14, 17, 18, 20, 21):
        try_run("Dam Scraper", run_dam)

    # APMC: morning, afternoon, evening
    if hour in (6, 7, 9, 10, 13, 14, 18, 19):
        try_run("APMC Scraper", run_apmc)

    # AI News: Morning batch (6-9 AM IST) & Evening batch (5-9 PM IST) -> 2 Morning + 2 Evening stories daily
    if hour in (6, 7, 8, 17, 18, 19, 20):
        try_run("AI News Publisher (2 Morning + 2 Evening Batches)", lambda: run_ai_news(2))


def try_run(name, fn):
    try:
        log.info(f"▶️ Executing: {name}")
        fn()
        log.info(f"✅ Completed: {name}")
    except Exception as e:
        log.error(f"❌ Error in {name}: {e}")


if __name__ == "__main__":
    force_mode = "--all" in sys.argv or "once" in sys.argv or "-a" in sys.argv
    run_scheduled_scrapers(force_all=force_mode)
