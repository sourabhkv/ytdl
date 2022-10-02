pyinstaller --icon=logo.ico -w --hidden-import yt_dlp.compat._legacy "Youtube-dl GUI.py"
mkdir ".\dist\Youtube-dl GUI\images"
robocopy images ".\dist\Youtube-dl GUI\images"
copy logo.ico ".\dist\Youtube-dl GUI"
copy yt-dlp_x86.exe ".\dist\Youtube-dl GUI"
copy version.txt ".\dist\Youtube-dl GUI"
copy ffmpeg.exe ".\dist\Youtube-dl GUI"
copy update_starter.bat ".\dist\Youtube-dl GUI"
rd /s /q ".\dist\Youtube-dl GUI\websockets-10.3.dist-info"
echo wait
pause
