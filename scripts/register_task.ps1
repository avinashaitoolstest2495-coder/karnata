
$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c "C:\Users\avina\Downloads\karnata-site-with-cms\scripts\run_30min_auto_updater.bat"'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration ([TimeSpan]::MaxValue)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "KarnataAutoUpdater30Min" -Action $action -Trigger $trigger -Settings $settings -Force
