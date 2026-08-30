@echo off
echo ========================================================
echo   Karnata.in - Panchatantra 15-Day Auto-Sync Scheduler
echo ========================================================
echo.
cd /d "c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka"

echo [%date% %time%] Starting Panchatantra 5,958 Gram Panchayat sync...
node "c:\Users\avina\.gemini\antigravity\brain\a5a7b6ab-2e2e-492f-a4ea-1bf58f4177f3\scratch\fast_karnataka_staff_scraper.js"

echo.
echo [%date% %time%] Syncing database files to root...
node "c:\Users\avina\.gemini\antigravity\brain\a5a7b6ab-2e2e-492f-a4ea-1bf58f4177f3\scratch\sync_panchatantra_data.js"

echo.
echo [%date% %time%] Panchatantra sync completed successfully!
echo ========================================================
