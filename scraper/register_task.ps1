# ============================================================
# Register Karnata Daily Update as Windows Scheduled Task
# Run this ONCE as Administrator:
#   Right-click PowerShell → "Run as administrator"
#   Then: powershell -ExecutionPolicy Bypass -File register_task.ps1
# ============================================================

$SCRIPT_PATH = "c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka\scraper\daily_update.ps1"
$TASK_NAME   = "Karnata Daily Data Update"

# Remove old task if exists
Unregister-ScheduledTask -TaskName $TASK_NAME -Confirm:$false -ErrorAction SilentlyContinue

# Create the task action
$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"$SCRIPT_PATH`"" `
    -WorkingDirectory "c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka"

# Run daily at 8:00 AM IST
$trigger = New-ScheduledTaskTrigger -Daily -At "08:00AM"

# Run whether user is logged in or not
$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable

# Register the task
Register-ScheduledTask `
    -TaskName $TASK_NAME `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -Force

Write-Host ""
Write-Host "✅ Task registered: '$TASK_NAME'"
Write-Host "   Runs daily at 8:00 AM"
Write-Host "   Script: $SCRIPT_PATH"
Write-Host ""
Write-Host "To test it right now, run:"
Write-Host "   Start-ScheduledTask -TaskName '$TASK_NAME'"
Write-Host ""
Write-Host "To view logs after it runs:"
Write-Host "   Get-Content 'c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka\scraper\auto_deploy.log'"
