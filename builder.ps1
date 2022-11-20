pyinstaller --icon=logo.ico -w --hidden-import yt_dlp.compat._legacy "Youtube-dl GUI.py"
New-Item -Path ".\dist\Youtube-dl GUI\images" -ItemType Directory
Copy-Item ".\images\*.*" -Destination ".\dist\Youtube-dl GUI\images"
Copy-Item logo.ico -Destination ".\dist\Youtube-dl GUI"
.\yt-dlp_x86.exe -U
Copy-Item yt-dlp_x86.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item version.txt -Destination ".\dist\Youtube-dl GUI"
Copy-Item ffmpeg.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item AtomicParsley.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item update_starter.bat -Destination ".\dist\Youtube-dl GUI"
Remove-Item ".\dist\Youtube-dl GUI\websockets-10.3.dist-info"
read-host “`r`nPress ENTER to continue...”
