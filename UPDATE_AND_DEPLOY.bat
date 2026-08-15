@echo off
title Karnata.in — 1-Click Master Scrape & Live Deploy
echo =======================================================
echo 🌟 KARNATA 1-CLICK MASTER AUTO-PILOT UPDATE & DEPLOY 🌟
echo =======================================================
cd /d "%~dp0"
python scripts\run_all_and_deploy.py
echo.
echo =======================================================
echo ✅ Master Pipeline Finished! Press any key to exit.
echo =======================================================
pause
