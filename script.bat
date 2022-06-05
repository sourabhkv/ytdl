@echo off
del /f "Frame 1newer.png"
rename "Frame 1newer2.png" "Frame 1newer.png"
PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Updated')"
"Youtube-dl GUI.exe"
exit /b
