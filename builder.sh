mkdir Build_env
cd Build_env
virtualenv venv
venv\Scripts\activate
pip install Pillow
pip install pyinstaller==5.6.2
pip install requests
pip install --upgrade yt_dlp
pip install pytube
pyinstaller --icon=../logo.ico -w --hidden-import yt_dlp.compat._legacy "../Youtube-dl GUI.py"
mkdir "./dist/Youtube-dl GUI/images/"
cp ../images/* "./dist/Youtube-dl GUI/images/"
cp ../logo.ico "./dist/Youtube-dl GUI/"
cp ../yt-dlp "./dist/Youtube-dl GUI/"
rm -r "./dist/Youtube-dl GUI/websockets-10.4.dist-info"
echo "Press enter to exit"
read varname
