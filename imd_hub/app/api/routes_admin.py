"""
routes_admin.py
Protected Admin APIs for Manual Triggering & Scraper Telemetry
"""

import os
from fastapi import APIRouter, Depends, HTTPException, Header, Security
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.database.database import get_db
from app.database.models import ScrapeRun, ScrapeError
from app.scraper.imd_scraper import run_imd_scrape_job

router = APIRouter(prefix="/api/admin", tags=["Admin APIs"])

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "nk_admin_secret_2026")

def verify_admin_key(x_api_key: str = Header(None, alias="X-API-Key")):
    if not x_api_key or x_api_key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid ADMIN_API_KEY")
    return True

@router.post("/scrape")
def trigger_manual_scrape(db: Session = Depends(get_db), authorized: bool = Depends(verify_admin_key)):
    """Triggers immediate manual execution of IMD Karnataka scraper."""
    summary = run_imd_scrape_job()
    return summary

@router.get("/scrape-status")
def get_scrape_status(db: Session = Depends(get_db)):
    """Returns telemetry of last scraper run, errors, and next scheduled run."""
    last_run = db.query(ScrapeRun).order_by(desc(ScrapeRun.started_at)).first()
    recent_errors = db.query(ScrapeError).order_by(desc(ScrapeError.created_at)).limit(10).all()

    error_list = []
    for err in recent_errors:
        error_list.append({
            "id": err.id,
            "url": err.url,
            "type": err.error_type,
            "message": err.error_message,
            "created_at": err.created_at.isoformat()
        })

    return {
        "last_run": last_run.started_at.isoformat() if last_run else None,
        "completed_at": last_run.completed_at.isoformat() if (last_run and last_run.completed_at) else None,
        "status": last_run.status if last_run else "NEVER_RUN",
        "locations_found": last_run.locations_found if last_run else 0,
        "locations_success": last_run.locations_success if last_run else 0,
        "locations_failed": last_run.locations_failed if last_run else 0,
        "last_error": last_run.error_message if last_run else None,
        "recent_errors": error_list
    }
