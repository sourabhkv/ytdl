url2='https://github.com/sourabhkv/ytdl/releases/latest/download/ytdl.zip'
import requests, zipfile,io
import os,sys,re ,requests,subprocess,threading
def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()

t2 = threading.Thread(target=popens, args=("yt-dlp_x86 -U",))
t2.start()
os.system('del /f "script.bat"')
ver=""
url='https://github.com/sourabhkv/ytdl/releases/latest'
r = requests.get(url)
if r.status_code == 200:
    title_re=re.compile(r'<title>(.*?)</title>', re.UNICODE )
    match = title_re.search(r.text)
    title=str(match.group(1))
    for i in title:
        if i.isdigit():
            ver=ver+i
    ver=int(ver)
s=open("version.txt","r")
curver=int(s.readlines()[0])
s.close()
if curver==ver or curver>ver:
    os.system('PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Up to date\')"')
elif ver>curver:
    try:
        popens("taskkill /F /IM yt-dlp_x86.exe")
    except:
        pass
    os.system('taskkill /F /IM "Youtube-dl GUI.exe"')
    #popens("del /f D:\\vx\\v3\\files\\dist\\Youtube-dl GUIYoutube-dl GUI.exe")
    os.system('del /f "Youtube-dl GUI.exe"')
    print("downloading update")
    r = requests.get(url2)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(os.getcwd())
    t=open("version.txt","w")
    t.write(str(ver))
    t.close()
    lst=os.listdir()
    if "script.bat" in lst:
        os.system('powershell.exe powershell start script.bat -v runas')
    else:
        print("UPDATED")
        os.startfile("Youtube-dl GUI.exe")
        
