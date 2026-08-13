"""
routes_weather.py
Public REST API Endpoints for Karnataka IMD Weather Data
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.weather_service import (
    get_all_karnataka_weather,
    get_city_weather_details,
    get_city_history
)

router = APIRouter(prefix="/api/weather", tags=["Public Weather APIs"])

@router.get("/karnataka")
def get_karnataka_weather(db: Session = Depends(get_db)):
    """Return latest weather observations for all locations in Karnataka."""
    return get_all_karnataka_weather(db)

@router.get("/{city}")
def get_city_weather(city: str, db: Session = Depends(get_db)):
    """Return latest observation and 7-day forecast for a specific city (e.g. bengaluru, mysuru, mangaluru)."""
    res = get_city_weather_details(db, city)
    if res.get("status") == "error":
        raise HTTPException(status_code=404, detail=res["message"])
    return res

@router.get("/{city}/forecast")
def get_city_forecast(city: str, db: Session = Depends(get_db)):
    """Return 7-day forecast for a specific city."""
    res = get_city_weather_details(db, city)
    if res.get("status") == "error":
        raise HTTPException(status_code=404, detail=res["message"])
    return {
        "city_en": res["name_en"],
        "city_kn": res["name_kn"],
        "updated_at": res["updated_at"],
        "forecast": res["forecast_7_days"]
    }

@router.get("/{city}/history")
def get_city_weather_history(city: str, days: int = Query(default=7, ge=1, le=90), db: Session = Depends(get_db)):
    """Return historical weather observations for a city (e.g. ?days=7 or ?days=30)."""
    res = get_city_history(db, city, days)
    if res.get("status") == "error":
        raise HTTPException(status_code=404, detail=res["message"])
    return res
