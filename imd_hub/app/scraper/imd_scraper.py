"""
imd_scraper.py
Main Hourly IMD Karnataka Weather Scraper & Database Ingestion Engine
"""

import os
import time
import datetime
import logging
import asyncio
import httpx
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import IMDLocation, WeatherObservation, WeatherForecast, ScrapeRun, ScrapeError
from app.scraper.imd_parser import parse_karnataka_index, parse_city_forecast_page
from app.scraper.validator import validate_observation, parse_float

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

IMD_SOURCE_URL = os.getenv("IMD_SOURCE_URL", "https://internal.imd.gov.in/power/SRLDC/Karnatak.html")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

async def fetch_url_with_retry(client: httpx.AsyncClient, url: str, max_retries: int = 3) -> str:
    delay = 2
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            res = await client.get(url, headers=HEADERS, timeout=20.0)
            res.raise_for_status()
            return res.text
        except Exception as e:
            last_exc = e
            logger.warning(f"[IMDScraper] Attempt {attempt}/{max_retries} failed for {url}: {e}")
            if attempt < max_retries:
                await asyncio.sleep(delay)
                delay *= 2.5
    raise last_exc

async def scrape_location_task(client: httpx.AsyncClient, semaphore: asyncio.Semaphore, loc_info: dict, run_id: int) -> dict:
    async with semaphore:
        url = loc_info["forecast_url"]
        loc_name = loc_info["location_name"]
        logger.info(f"Scraping {loc_name} ({url})...")
        
        try:
            html = await fetch_url_with_retry(client, url)
            parsed = parse_city_forecast_page(html, url)
            logger.info(f"{loc_name} SUCCESS")
            return {
                "success": True,
                "location_info": loc_info,
                "parsed": parsed,
                "error": None
            }
        except Exception as e:
            err_msg = str(e)
            logger.error(f"{loc_name} FAILED: {err_msg}")
            return {
                "success": False,
                "location_info": loc_info,
                "parsed": None,
                "error": err_msg
            }

def run_imd_scrape_job() -> dict:
    db: Session = SessionLocal()
    start_time = datetime.datetime.now(datetime.timezone.utc)
    
    scrape_run = ScrapeRun(
        started_at=start_time,
        status="RUNNING"
    )
    db.add(scrape_run)
    db.commit()
    db.refresh(scrape_run)

    run_summary = {
        "status": "success",
        "started_at": start_time.isoformat(),
        "locations_found": 0,
        "locations_success": 0,
        "locations_failed": 0,
        "run_id": scrape_run.id
    }

    try:
        # Step 1: Discover locations from main page
        logger.info(f"Starting IMD Karnataka scraper from {IMD_SOURCE_URL}")
        with httpx.Client(timeout=20.0, headers=HEADERS) as sync_client:
            resp = sync_client.get(IMD_SOURCE_URL)
            resp.raise_for_status()
            discovered_locations = parse_karnataka_index(resp.text, IMD_SOURCE_URL)

        scrape_run.locations_found = len(discovered_locations)
        run_summary["locations_found"] = len(discovered_locations)
        db.commit()

        logger.info(f"Found {len(discovered_locations)} locations")

        # Step 2: Fetch forecast pages asynchronously with controlled concurrency (max 3)
        async def main_async_fetch():
            semaphore = asyncio.Semaphore(3)
            async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as async_client:
                tasks = [scrape_location_task(async_client, semaphore, loc, scrape_run.id) for loc in discovered_locations]
                return await asyncio.gather(*tasks)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(main_async_fetch())
        loop.close()

        success_count = 0
        failed_count = 0
        ingested_loc_ids = set()

        # Step 3: Ingest results into Database
        for res in results:
            loc_info = res["location_info"]
            norm_name = loc_info["normalized_name"]

            try:
                # Lookup or create IMDLocation
                db_loc = db.query(IMDLocation).filter(IMDLocation.normalized_name == norm_name).first()
                if not db_loc:
                    db_loc = IMDLocation(
                        location_name=loc_info["location_name"],
                        normalized_name=norm_name,
                        source_url=loc_info["source_url"],
                        forecast_url=loc_info["forecast_url"],
                        imd_city_id=loc_info["imd_city_id"],
                        active=True
                    )
                    db.add(db_loc)
                    db.commit()
                    db.refresh(db_loc)

                if not res["success"]:
                    failed_count += 1
                    scrape_err = ScrapeError(
                        scrape_run_id=scrape_run.id,
                        location_id=db_loc.id,
                        url=loc_info["forecast_url"],
                        error_type="Fetch/Parse Error",
                        error_message=res["error"]
                    )
                    db.add(scrape_err)
                    db.commit()
                    continue

                if db_loc.id in ingested_loc_ids:
                    logger.info(f"Skipping duplicate location ingestion for {norm_name}")
                    continue

                ingested_loc_ids.add(db_loc.id)
                success_count += 1
                parsed_data = res["parsed"]
                raw_obs = parsed_data.get("observation", {})
                norm_obs, errors = validate_observation(raw_obs)

                if errors:
                    for err in errors:
                        db.add(ScrapeError(
                            scrape_run_id=scrape_run.id,
                            location_id=db_loc.id,
                            url=loc_info["forecast_url"],
                            error_type="Validation Warning",
                            error_message=err
                        ))

                # Record Observation
                today_date = datetime.date.today()
                obs_model = WeatherObservation(
                    location_id=db_loc.id,
                    observation_date=today_date,
                    scraped_at=start_time,
                    max_temp=norm_obs.get("max_temp"),
                    max_temp_departure=norm_obs.get("max_temp_departure"),
                    min_temp=norm_obs.get("min_temp"),
                    min_temp_departure=norm_obs.get("min_temp_departure"),
                    rainfall_24h=norm_obs.get("rainfall_24h"),
                    rh_0830=norm_obs.get("rh_0830"),
                    rh_1730=norm_obs.get("rh_1730"),
                    sunset=norm_obs.get("sunset"),
                    sunrise_tomorrow=norm_obs.get("sunrise_tomorrow"),
                    moonset=norm_obs.get("moonset"),
                    moonrise=norm_obs.get("moonrise"),
                    source_url=loc_info["forecast_url"]
                )
                db.add(obs_model)

                # Record Forecasts
                for f in parsed_data.get("forecasts", []):
                    f_min = parse_float(f.get("min_temp"))
                    f_max = parse_float(f.get("max_temp"))
                    fc_model = WeatherForecast(
                        location_id=db_loc.id,
                        scraped_at=start_time,
                        forecast_date=today_date,
                        min_temp=f_min,
                        max_temp=f_max,
                        weather_description=f.get("weather"),
                        warning=f.get("warning"),
                        source_url=loc_info["forecast_url"]
                    )
                    db.add(fc_model)

                db.commit()
            except Exception as loc_err:
                db.rollback()
                failed_count += 1
                logger.error(f"Error ingesting location {norm_name}: {loc_err}")
                db.add(ScrapeError(
                    scrape_run_id=scrape_run.id,
                    location_id=db_loc.id if 'db_loc' in locals() and db_loc else None,
                    url=loc_info["forecast_url"],
                    error_type="Ingestion Exception",
                    error_message=str(loc_err)
                ))
                db.commit()

        # Update ScrapeRun completion
        end_time = datetime.datetime.now(datetime.timezone.utc)
        scrape_run.completed_at = end_time
        scrape_run.locations_success = success_count
        scrape_run.locations_failed = failed_count
        scrape_run.status = "SUCCESS" if failed_count == 0 else "PARTIAL_SUCCESS"
        db.commit()

        run_summary["locations_success"] = success_count
        run_summary["locations_failed"] = failed_count
        run_summary["completed_at"] = end_time.isoformat()
        logger.info(f"Scraper completed: {success_count} successful, {failed_count} failed")

    except Exception as exc:
        logger.error(f"Scraper fatal run failure: {exc}")
        db.rollback()
        scrape_run.status = "FAILED"
        scrape_run.error_message = str(exc)
        scrape_run.completed_at = datetime.datetime.now(datetime.timezone.utc)
        db.commit()
        run_summary["status"] = "failed"
        run_summary["error"] = str(exc)
    finally:
        db.close()

    return run_summary

if __name__ == "__main__":
    from app.database.database import init_db
    init_db()
    res = run_imd_scrape_job()
    print("Scraper Execution Result:", res)
