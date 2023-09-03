virtualenv venv
venv\Scripts\activate
pip install Pillow
pip install Pyinstaller
pip install requests
pip install --upgrade yt_dlp
pyinstaller --icon=images/logo.ico -w --hidden-import yt_dlp.compat._legacy --name="Youtube-dl GUI" ytdl/__main__.py
New-Item -Path ".\dist\Youtube-dl GUI\images" -ItemType Directory
Copy-Item ".\images\*.*" -Destination ".\dist\Youtube-dl GUI\images"
read-host “`r`nPress ENTER to continue...”