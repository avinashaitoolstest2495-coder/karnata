"""
main.py
FastAPI Application Entry Point for Karnataka IMD Weather Data Hub
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.database.database import init_db, get_db
from app.api.routes_weather import router as weather_router
from app.api.routes_admin import router as admin_router
from app.scheduler.scheduler import start_scheduler, shutdown_scheduler
from app.services.weather_service import get_all_karnataka_weather, get_city_weather_details

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize Database & Scheduler
    init_db()
    try:
        start_scheduler()
    except Exception as e:
        print(f"[Lifespan] Scheduler warning: {e}")
    yield
    # Shutdown: Stop Scheduler
    try:
        shutdown_scheduler()
    except Exception as e:
        print(f"[Lifespan] Shutdown warning: {e}")

app = FastAPI(
    title="Karnataka IMD Weather Data Hub API",
    description="Automated IMD Weather Scraper, REST APIs & Admin Dashboard for Karnataka",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(weather_router)
app.include_router(admin_router)

templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
@app.get("/weather/karnataka", response_class=HTMLResponse)
def public_karnataka_dashboard(request: Request, db: Session = Depends(get_db)):
    data = get_all_karnataka_weather(db)
    return templates.TemplateResponse("karnataka_dashboard.html", {"request": request, "data": data})

@app.get("/weather/karnataka/{city}", response_class=HTMLResponse)
def public_city_weather_page(city: str, request: Request, db: Session = Depends(get_db)):
    data = get_city_weather_details(db, city)
    return templates.TemplateResponse("city_weather.html", {"request": request, "data": data})

@app.get("/admin/weather", response_class=HTMLResponse)
def admin_dashboard_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
