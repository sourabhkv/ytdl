mkdir Build_env
cd Build_env
virtualenv venv
venv\Scripts\activate
pip install Pillow
pip install Pyinstaller
pip install requests
pip install psutil
pip install --upgrade yt_dlp
pip install pytube
Copy-Item "..\class2.81.py" -Destination ".\"
Copy-Item "..\logo.ico" -Destination ".\"
pyinstaller --icon=logo.ico -w --hidden-import yt_dlp.compat._legacy ".\class2.81.py"
New-Item -Path ".\dist\class2.81\images" -ItemType Directory
Copy-Item "..\images\*.*" -Destination ".\dist\class2.81\images"
Copy-Item "..\logo.ico" -Destination ".\dist\class2.81"
Copy-Item "..\yt-dlp_x86.exe" -Destination ".\dist\class2.81"
.\yt-dlp.exe -U
Copy-Item "..\ffmpeg.exe" -Destination ".\dist\class2.81"
Copy-Item "..\AtomicParsley.exe" -Destination ".\dist\class2.81"
Remove-Item ".\dist\class2.81\websockets-10.4.dist-info"
read-host “`r`nPress ENTER to continue...”
