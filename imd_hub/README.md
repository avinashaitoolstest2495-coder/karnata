# IMD Karnataka Weather Data Hub

Production-ready automated IMD weather scraper, REST APIs, database persistence, Kannada translations, and admin control dashboard.

## 🚀 Quick Start Commands

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Live Scraper
```bash
python run_scraper.py
```

### 3. Run FastAPI Application & Web Server
```bash
uvicorn app.api.main:app --reload --port 8000
```
- Public Karnataka Weather Dashboard: `http://localhost:8000/weather/karnataka`
- City Weather Details: `http://localhost:8000/weather/karnataka/bengaluru`
- Admin Dashboard: `http://localhost:8000/admin/weather`
- OpenAPI Docs: `http://localhost:8000/docs`

### 4. Run Unit Tests
```bash
pytest tests/
```

### 5. Run with Docker Compose
```bash
docker compose up -d
```

### 6. Run Hourly Cron (Linux Server)
```bash
0 * * * * cd /app && /usr/local/bin/python run_scraper.py >> /var/log/imd_scraper.log 2>&1
```

## 📡 REST API Endpoints

- `GET /api/weather/karnataka` - Latest weather for all 29+ Karnataka locations.
- `GET /api/weather/{city}` - Detailed latest observation & 7-day forecast.
- `GET /api/weather/{city}/forecast` - 7-day forecast array.
- `GET /api/weather/{city}/history?days=7` - Historical telemetry.
- `POST /api/admin/scrape` - Manually trigger scrape job (Requires `X-API-Key` header).
- `GET /api/admin/scrape-status` - Telemetry of scraper runs and recent error logs.
