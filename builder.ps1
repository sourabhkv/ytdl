virtualenv venv
venv\Scripts\activate
pip install Pillow
pip install Pyinstaller=5.6.2
pip install requests
pip install psutil
pip install --upgrade yt_dlp
pip install pytube
pyinstaller --icon=logo.ico -w --hidden-import yt_dlp.compat._legacy "Youtube-dl GUI.py"
New-Item -Path ".\dist\Youtube-dl GUI\images" -ItemType Directory
Copy-Item ".\images\*.*" -Destination ".\dist\Youtube-dl GUI\images"
Copy-Item logo.ico -Destination ".\dist\Youtube-dl GUI"
Copy-Item yt-dlp_x86.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item version.txt -Destination ".\dist\Youtube-dl GUI"
Copy-Item ffmpeg.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item AtomicParsley.exe -Destination ".\dist\Youtube-dl GUI"
Copy-Item update_starter.bat -Destination ".\dist\Youtube-dl GUI"
Remove-Item ".\dist\Youtube-dl GUI\websockets-10.4.dist-info"
read-host “`r`nPress ENTER to continue...”