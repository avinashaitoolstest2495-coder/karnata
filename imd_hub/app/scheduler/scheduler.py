"""
scheduler.py
APScheduler Hourly Automation Service (Asia/Kolkata Timezone)
"""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone

from app.scraper.imd_scraper import run_imd_scrape_job

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def start_scheduler():
    kolkata_tz = timezone("Asia/Kolkata")
    
    # Run at 00 minutes of every hour (06:00, 07:00, 08:00, etc.)
    trigger = CronTrigger(minute=0, timezone=kolkata_tz)
    
    scheduler.add_job(
        run_imd_scrape_job,
        trigger=trigger,
        id="hourly_imd_karnataka_scraper",
        replace_existing=True
    )
    
    scheduler.start()
    logger.info("APScheduler initialized: Hourly IMD Scraper scheduled at :00 IST")

def shutdown_scheduler():
    if scheduler.running:
        scheduler.shutdown()
        logger.info("APScheduler shutdown successfully")
