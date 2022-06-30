@echo off
del /f "img14.png"
del /f "optionsdark.png"
PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Updated')"
"Youtube-dl GUI.exe"
exit /b
