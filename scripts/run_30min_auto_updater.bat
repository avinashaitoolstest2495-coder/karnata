@echo off
cd /d "C:\Users\avina\Downloads\karnata-site-with-cms"
for %%A in ("C:\Users\avina\Downloads\karnata-site-with-cms\scripts\updater.log") do if %%~zA GTR 2097152 type nul > "C:\Users\avina\Downloads\karnata-site-with-cms\scripts\updater.log"
python "C:\Users\avina\Downloads\karnata-site-with-cms\scripts\auto_updater_30min.py" >> "C:\Users\avina\Downloads\karnata-site-with-cms\scripts\updater.log" 2>&1
