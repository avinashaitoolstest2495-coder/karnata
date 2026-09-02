# Stop existing task if running
Stop-ScheduledTask -TaskName "KarnataGoldRateDailyUpdater" -ErrorAction SilentlyContinue

# Define Action
$pythonExe = "C:\Python313\python.exe"
if (-not (Test-Path $pythonExe)) {
    $pythonExe = (Get-Command python).Source
}
$scriptPath = "c:\Users\avina\Downloads\karnata-site-with-cms\scripts\gold_daily_updater.py"
$action = New-ScheduledTaskAction -Execute $pythonExe -Argument "`"$scriptPath`"" -WorkingDirectory "c:\Users\avina\Downloads\karnata-site-with-cms"

# Define 3 Daily Triggers strictly at 10:00 AM, 10:30 AM, and 11:00 AM
$trigger1 = New-ScheduledTaskTrigger -Daily -At "10:00"
$trigger2 = New-ScheduledTaskTrigger -Daily -At "10:30"
$trigger3 = New-ScheduledTaskTrigger -Daily -At "11:00"

# Define Settings (Allow on battery, wake computer, 15 min limit)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew

# Register Task
Register-ScheduledTask -TaskName "KarnataGoldRateDailyUpdater" -Action $action -Trigger @($trigger1, $trigger2, $trigger3) -Settings $settings -Force

Write-Host "SUCCESS: KarnataGoldRateDailyUpdater task successfully registered for 10:00 AM, 10:30 AM, and 11:00 AM!"
Get-ScheduledTask -TaskName "KarnataGoldRateDailyUpdater" | Select-Object TaskName, State
