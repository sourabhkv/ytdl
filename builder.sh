virtualenv venv
source venv/bin/activate
pip install Pillow
pip install pyinstaller
pip install requests
pip install --upgrade yt_dlp
pyinstaller --icon=./images/logo.ico -w --hidden-import yt_dlp.compat._legacy --name="Youtube-dl GUI" ./ytdl/__main__.py
mkdir "./dist/Youtube-dl GUI/images/"
cp ../images/* "./dist/Youtube-dl GUI/images/"
cp ../logo.ico "./dist/Youtube-dl GUI/"
cp ../yt-dlp "./dist/Youtube-dl GUI/"
echo "Press enter to exit"
read varname
