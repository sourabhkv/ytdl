import tkinter as tk
from tkinter import *
import os,re ,requests,subprocess,threading,shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
global status
my_dir=os.getcwd()
def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()

def checker(a):
    req=requests.get(a)
    res=req.text
    req.close()
    s=0
    d=""
    f=res.split("\n")
    for i in range(30,len(f)):
        if "Version in support" in f[i]:
            s=i
    for j in range(0,len(f[s])):
        if f[s][j].isnumeric() or f[s][j]==",":
            d=d+f[s][j]
    global versions,curver,streams4,streams5,stream6
    all_ver=""
    versions=d.split(",")
    print(versions)
    r=open("version.txt","r")
    curver=r.readlines()[0]
    r.close()
    streams4 = Label(root2, text = "Current version : "+str(curver),bg="#303135",fg="white").place(x = 110,y = 70)
    for i in range(0,len(versions)):
        all_ver=all_ver+"  "+str(versions[i])
    streams5 = Label(root2, text = "Supported versions : "+all_ver,bg="#303135",fg="white").place(x = 40,y = 100)
    if str(curver)==versions[-1]:
        status.set(" You are using latest version")
    elif str(curver)!=versions[-1] and str(curver) in versions:
        status.set(" Updating...")
        t2 = threading.Thread(target=popens, args=("yt-dlp_x86 -U",))
        t2.start()
        CREATE_NO_WINDOW = 0x08000000
        #popens('del /f "script.bat"')
        try:
            subprocess.call("taskkill /F /IM yt-dlp_x86.exe",creationflags=CREATE_NO_WINDOW)
        except:
            pass
        try:
            subprocess.call('taskkill /F /IM "Youtube-dl GUI.exe"',creationflags=CREATE_NO_WINDOW)
        except:
            pass
        status.set(" Downloading update")
        url2='https://github.com/sourabhkv/ytdl/releases/latest/download/update.zip'
        with urlopen(url2) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                for member in zfile.namelist():
                    filename = os.path.basename(member)
                    source = zfile.open(member)
                    target = open(os.path.join(my_dir, filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
        lst=os.listdir()
        if "script.bat" in lst:
            subprocess.call('script.bat',creationflags=CREATE_NO_WINDOW)
        else:
            os.startfile("Youtube-dl GUI.exe")
        t=open("version.txt","w")
        t.write(str(versions[-1]))
        t.close()
        status.set(" Update complete")
        

root2 = tk.Tk()
sw = root2.winfo_screenwidth()
sh = root2.winfo_screenheight()
root2.focus_force()
y=int((sh-450)/2)
x=int((sw-350)/2)
root2.geometry('%dx%d+%d+%d' % (350, 400, x, y))
root2.title('Youtube-dl GUI updater')
root2.configure(bg='#303135')
streams = Label(root2, text = "Youtube-dl GUI",bg="#303135",font=('Arial', 16),fg="white").place(x = 105,y = 8)
streams2 = Label(root2, text = "This is project is based on yt-dlp , ffmpeg , atomic parsley",bg="#303135",fg="white").place(x = 15,y = 40)
t2 = threading.Thread(target=checker, args=("https://sourabhkv.github.io/ytdl",))
t2.start()
status= StringVar()
status.set("")
statusbar = tk.Label(root2, textvariable=status ,width=150, bd=2,fg="white", relief=tk.SUNKEN, anchor=tk.W,bg='#202125').place(x=-2,y=380)
root2.resizable(False, False)
root2.iconbitmap(r'logo.ico')
root2.mainloop()
