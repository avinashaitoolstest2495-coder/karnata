# ============================================================
# Karnata Daily Data Scraper + Cloudflare Pages Auto-Deploy
# ============================================================

$SITE_DIR    = "c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka"
$SCRAPER_DIR = "$SITE_DIR\scraper"
$LOG_FILE    = "$SCRAPER_DIR\auto_deploy.log"

function Write-Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts $msg" | Tee-Object -FilePath $LOG_FILE -Append
}

Write-Log "========================================="
Write-Log "🚀 Karnata Daily Data Scrape + Deploy Started"
Write-Log "========================================="

Set-Location "$SITE_DIR"

# 1. Run Live Data Scrapers via Smart Scheduler (Gold, Dam, Weather, Petrol, APMC, News)
Write-Log "⚙️ Executing live data scrapers..."
try {
    $out = & python "$SCRAPER_DIR\smart_scheduler.py" --all 2>&1
    Write-Log "✅ Live data scrapers completed successfully."
} catch {
    Write-Log "❌ Scraper error: $_"
}

# 2. Deploy updated website & data to Cloudflare Pages (non-interactive)
Write-Log "☁️ Deploying updated live data to Cloudflare Pages..."
try {
    $out = & npx --yes wrangler pages deploy . --project-name=karnata --commit-dirty=true 2>&1
    Write-Log "✅ Cloudflare Pages Deployment complete!"
} catch {
    Write-Log "❌ Deployment error: $_"
}

Write-Log "========================================="
Write-Log "✅ All done! Live site updated."
Write-Log "========================================="

