$action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "`"c:\Users\avina\Downloads\karnata-site-with-cms\namma-karnataka\scripts\run_hidden.vbs`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval (New-TimeSpan -Minutes 30)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 20)

Register-ScheduledTask -TaskName "KarnataAutoScrapeDeploy" -Action $action -Trigger $trigger -Settings $settings -Force
Write-Host "KarnataAutoScrapeDeploy Scheduled Task registered and verified for every 30 minutes!"
