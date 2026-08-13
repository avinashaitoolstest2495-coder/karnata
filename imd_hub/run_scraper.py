#!/usr/bin/env python3
"""
run_scraper.py
CLI Command Line Entrypoint for IMD Karnataka Weather Scraper.
Usage:
    python run_scraper.py
"""

import sys
import os

# Ensure app package is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database.database import init_db
from app.scraper.imd_scraper import run_imd_scrape_job

if __name__ == "__main__":
    init_db()
    print("Starting IMD Karnataka Weather Scraper...")
    result = run_imd_scrape_job()
    print("\n================ SCRAPER RUN REPORT ================")
    print(f"Status:             {result.get('status')}")
    print(f"Started At:         {result.get('started_at')}")
    print(f"Completed At:       {result.get('completed_at')}")
    print(f"Locations Found:    {result.get('locations_found')}")
    print(f"Locations Success:  {result.get('locations_success')}")
    print(f"Locations Failed:   {result.get('locations_failed')}")
    print("====================================================")
