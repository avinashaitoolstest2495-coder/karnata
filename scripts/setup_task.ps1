# Stop existing task if running
Stop-ScheduledTask -TaskName "KarnataAutoScrapeDeploy" -ErrorAction SilentlyContinue

# Define Action
$scriptPath = "c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka\scripts\run_hidden.vbs"
$action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "`"$scriptPath`""

# Define Trigger (Runs every 30 minutes indefinitely)
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).ToString("HH:mm") -RepetitionInterval (New-TimeSpan -Minutes 30)

# Define Settings (15 min execution limit, ignore overlapping runs, run on battery)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew

# Register Task
Register-ScheduledTask -TaskName "KarnataAutoScrapeDeploy" -Action $action -Trigger $trigger -Settings $settings -Force

Write-Host "SUCCESS: KarnataAutoScrapeDeploy task successfully registered to run every 30 minutes!"
Get-ScheduledTask -TaskName "KarnataAutoScrapeDeploy" | Select-Object TaskName, State
