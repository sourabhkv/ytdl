@echo off
taskkill /F /IM updater.exe
del /f updater.exe
rename updater2.exe updater.exe
PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Updated')"
exit /b