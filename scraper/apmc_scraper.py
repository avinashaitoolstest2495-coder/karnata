"""
Karnataka — apmc_scraper.py
Scrapes 100% genuine official APMC market rates directly from Karnataka Agricultural Marketing Board (krama.karnataka.gov.in).
Zero synthetic data. Zero mock generator.
"""

import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from scrape_full_krama_live_pure import run_pure_krama_scraper

def run() -> dict:
    print("🌾 Starting Karnataka APMC 100% pure live price scraper from KRAMA...")
    result = run_pure_krama_scraper()
    if isinstance(result, tuple):
        items, active_date = result
    else:
        items, active_date = result, datetime.now().strftime("%d/%m/%Y")

    iso_date = datetime.strptime(active_date, "%d/%m/%Y").strftime("%Y-%m-%d")
    
    output = {
        "date": iso_date,
        "market_date": active_date,
        "updated_at": datetime.now().isoformat(),
        "source": "Official KRAMA (krama.karnataka.gov.in)",
        "total_records": len(items),
        "items": items
    }
    
    target_json = ROOT_DIR / "data" / "apmc_prices.json"
    with open(target_json, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        
    print(f"✅ APMC: Published {len(items)} 100% genuine official KRAMA records for {iso_date}.")
    return output

if __name__ == "__main__":
    run()
