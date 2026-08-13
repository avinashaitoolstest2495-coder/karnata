"""
Karnata — main.py
Master scheduler — runs all scrapers on IST schedule
Run: python main.py
Or deploy to: Cloudflare Workers / Railway / VPS cron
"""

import schedule
import time
import threading
import sys
import os
from datetime import datetime, timedelta, timezone
from utils import log, telegram_alert

# ─── Import all scrapers ──────────────────────────────────────
from gold_scraper   import run as run_gold
from petrol_scraper import run as run_petrol
from dam_scraper    import run as run_dam
from apmc_scraper   import run as run_apmc
from weather_scraper import run as run_weather
from ai_news_publisher import run as run_ai_news

# Push notification triggers — run AFTER the matching scraper writes
# fresh data, so they're always checking the latest values, not stale ones
from notify_trigger import check_gold as notify_check_gold
from notify_trigger import check_dam as notify_check_dam
from notify_trigger import check_weather as notify_check_weather
from local_news_scraper import run as run_local_news

# ─── Safe runner with error handling ─────────────────────────
def safe_run(name: str, fn):
    """Run a scraper safely — catch errors, log, alert."""
    try:
        log.info(f"▶️  Starting: {name}")
        result = fn()
        log.info(f"✅ Done: {name}")
        return result
    except Exception as e:
        msg = f"❌ {name} crashed: {e}"
        log.error(msg)
        telegram_alert(f"🚨 Scraper Error\n{msg}")
        return None

def job_social_media_broadcast():
    try:
        from image_generator import create_gold_card, create_dam_card
        from social_publisher import publish_update

        log.info("📱 Starting Automated Social Media Broadcaster...")

        # 1. Gold Rate Social Broadcast
        gold_img = create_gold_card({"gold_22k": "68,500", "gold_24k": "74,720", "silver_1kg": "89,500"})
        gold_caption = "🟡 KARNATA LIVE: Today's Gold & Silver Rates in Karnataka\n22K (10g): ₹68,500 | 24K: ₹74,720\nSilver (1kg): ₹89,500\n\nLive: https://karnata.pages.dev/gold"
        publish_update("gold", gold_caption, gold_img)

        # 2. Dam Levels Social Broadcast
        dam_img = create_dam_card({})
        dam_caption = "🌊 KARNATAKA DAM WATER LEVELS REPORT\nKRS: 124.80 ft | Kabini: 2284.00 ft | Almatti: 519.60 m\n\nLive Telemetry: https://karnata.pages.dev/dams"
        publish_update("dams", dam_caption, dam_img)

    except Exception as e:
        log.error(f"❌ Social media broadcast failed: {e}")

# ─── Run all scrapers once ────────────────────────────────────
def run_all():
    log.info("=" * 50)
    log.info("🚀 Running ALL scrapers")
    log.info("=" * 50)
    safe_run("Gold & Silver",   run_gold)
    safe_run("Petrol & Diesel", run_petrol)
    safe_run("Dam Levels",      run_dam)
    safe_run("APMC Prices",     run_apmc)
    safe_run("Weather",         run_weather)
    safe_run("AI News Publisher", lambda: run_ai_news(max_articles=3))
    safe_run("Local News (RSS)",  run_local_news)
    safe_run("Social Media Broadcaster", job_social_media_broadcast)
    log.info("✅ All scrapers done\n")

# ─── Individual scrapers ──────────────────────────────────────
def job_gold():
    safe_run("Gold & Silver",   run_gold)
    safe_run("Gold push check", notify_check_gold)

def job_petrol():  safe_run("Petrol & Diesel", run_petrol)

def job_dam():
    safe_run("Dam Levels",      run_dam)
    safe_run("Dam push check",  notify_check_dam)

def job_apmc():    safe_run("APMC Prices",     run_apmc)

def job_weather():
    safe_run("Weather",         run_weather)
    safe_run("Weather push check", notify_check_weather)

def job_ai_news():   safe_run("AI News Publisher",  lambda: run_ai_news(max_articles=3))
def job_local_news(): safe_run("Local News (RSS)",   run_local_news)

# ─── Schedule setup (IST times) ──────────────────────────────
def setup_schedule():
    """
    All times in IST (Indian Standard Time UTC+5:30)
    schedule library uses local time — set TZ=Asia/Kolkata on your server
    Or use UTC offsets below.
    """

    # Gold & Silver — daily at 7:00 AM IST (after IBJA publishes)
    schedule.every().day.at("07:00").do(job_gold)
    schedule.every().day.at("15:00").do(job_gold)  # afternoon update

    # Petrol & Diesel — daily at 6:30 AM IST (IOCL updates at 6am)
    schedule.every().day.at("06:30").do(job_petrol)

    # Dam levels — daily at 8:00 AM IST (KSNDMC publishes morning bulletin)
    schedule.every().day.at("08:00").do(job_dam)
    schedule.every().day.at("17:00").do(job_dam)  # evening update too

    # APMC prices — daily at 9:30 AM IST (markets open and post data)
    schedule.every().day.at("09:30").do(job_apmc)
    schedule.every().day.at("14:00").do(job_apmc)

    # Weather — every hour (Open-Meteo is free, no rate limit concern)
    schedule.every().hour.at(":05").do(job_weather)

    # AI News Publisher — 3x daily
    schedule.every().day.at("08:30").do(job_ai_news)
    schedule.every().day.at("13:30").do(job_ai_news)
    schedule.every().day.at("19:30").do(job_ai_news)

    # Local News RSS — every 3 hours (Vijay Karnataka, Prajavani, Udayavani etc.)
    schedule.every(3).hours.do(job_local_news)

    log.info("📅 Schedule set:")
    log.info("   🥇 Gold:    7:00 AM, 3:00 PM IST")
    log.info("   ⛽ Petrol:  6:30 AM IST")
    log.info("   💧 Dam:     8:00 AM, 5:00 PM IST")
    log.info("   🌾 APMC:    9:30 AM, 2:00 PM IST")
    log.info("   🌦️ Weather: Every hour")
    log.info("   🤖 AI News: 8:30 AM, 1:30 PM, 7:30 PM IST")
    log.info("   📰 Local News RSS: Every 3 hours")


# ─── Main entry points ────────────────────────────────────────
def run_daemon():
    """Run as a background daemon — continuous scheduling."""
    log.info("🤖 Karnata Scraper Daemon starting...")
    telegram_alert("🟢 Karnata scrapers started")

    # Run all once at startup
    run_all()

    # Set schedule
    setup_schedule()

    log.info("⏰ Scheduler running... Press Ctrl+C to stop")
    while True:
        schedule.run_pending()
        time.sleep(30)  # check every 30 seconds


def run_once_all():
    """One-time run — useful for testing or manual trigger."""
    run_all()


def run_specific(name: str):
    """Run a specific scraper by name."""
    runners = {
        "gold":    job_gold,
        "petrol":  job_petrol,
        "dam":     job_dam,
        "apmc":    job_apmc,
        "weather": job_weather,
        "ai_news": job_ai_news,
        "news":    job_ai_news,
    }
    fn = runners.get(name.lower())
    if fn:
        fn()
    else:
        log.error(f"Unknown scraper: {name}. Options: {list(runners.keys())}")


# ─── Cloudflare Worker compatible export ──────────────────────
def cloudflare_handler(event, context):
    """
    For Cloudflare Workers with Cron Triggers.
    Deploy as: wrangler deploy
    Add to wrangler.toml:
        [triggers]
        crons = ["0 1 * * *", "30 0 * * *", "0 2 * * *"]  # UTC = IST-5:30
    """
    import json
    cron = event.get("cron", "unknown")
    log.info(f"☁️  Cloudflare cron trigger: {cron}")

    # Route based on cron time
    hour_utc = datetime.now(timezone.utc).hour
    # 6:30 AM IST = 1:00 AM UTC
    if hour_utc == 1:   job_petrol()
    # 7:00 AM IST = 1:30 AM UTC
    elif hour_utc == 2: job_gold()
    # 8:00 AM IST = 2:30 AM UTC
    elif hour_utc == 3: job_dam()
    # 9:30 AM IST = 4:00 AM UTC
    elif hour_utc == 4: job_apmc()
    # Hourly weather
    else: job_weather()

    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}


# ─── CLI entry point ─────────────────────────────────────────
if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "daemon":
        run_daemon()
    elif args[0] == "once":
        run_once_all()
    elif args[0] in ("gold", "petrol", "dam", "apmc", "weather", "ai_news", "news"):
        run_specific(args[0])
    elif args[0] == "test":
        # Quick test — just weather (fastest, no scraping needed)
        log.info("🧪 Test mode — running weather only")
        safe_run("Weather", run_weather)
    else:
        print(f"""
Karnata Scraper

Usage:
  python main.py              # Run as daemon (scheduled)
  python main.py once         # Run all scrapers once
  python main.py gold         # Run only gold scraper
  python main.py petrol       # Run only petrol scraper
  python main.py dam          # Run only dam levels scraper
  python main.py apmc         # Run only APMC prices
  python main.py weather      # Run only weather
  python main.py news         # Run only AI news publisher (Gemini)
  python main.py test         # Quick test (weather only)
        """)
