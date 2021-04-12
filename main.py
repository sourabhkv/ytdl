import win32gui, win32con
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox, filedialog
import os,subprocess,webbrowser,time,pygame,threading,multiprocessing
root = Tk()
root.geometry("900x250")
c=[]
final=[]
audlst=[]
vidlst=[]
subs=[]
#sroot.geometry("400x400")
name1 = Label(root, text = "YouTube-dl GUI").place(x = 170,y = 0) 
name = Label(root, text = "URL").place(x = 40,y = 20)

#^ Length and width window :D
url=""

def repo():
    webbrowser.open('https://github.com/sourabhkv')

def update():
    t1 = threading.Thread(target=run_command, args=("youtube-dl -U",))
    t1.start()

def browse():
    global download_Directory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

def cmder():
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM youtube-dl.exe"
    try:
        st=subprocess.Popen(a,shell=True)
        sts=subprocess.Popen(b,shell=True)
        messagebox.showinfo("youtube-dl","download cancelled")
    except:
        pass

def dlwin(line):
    pygame.init()
    (width, height) = (800, 30)
    sur_obj = pygame.display.set_mode((width, height))
    font_color=(0,0,0)
    font_obj=pygame.font.Font("C:\Windows\Fonts\calibri.ttf",15)
    pygame.display.set_caption('Downloading')
    programIcon = pygame.image.load('logo.png')
    pygame.display.set_icon(programIcon)
    text_obj=font_obj.render(str(line),True,font_color)
    sur_obj.fill((255,255,255))
    sur_obj.blit(text_obj,(0,0))
    pygame.display.update()

def run_command(command):
    global line
    p = subprocess.Popen((command), stdout=subprocess.PIPE,universal_newlines=True, bufsize=1,shell=True)
    for line in iter(p.stdout.readline, b''):
        dlwin(line)
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    pygame.quit()
    try:
        messagebox.showinfo("youtube-dl",(result1)+"download completed!")
    except:
        pass

def title(url):
    global result1
    stream=subprocess.Popen('youtube-dl -e '+url,stdout=subprocess.PIPE,shell=True)
    result1 = stream.communicate()[0]
    print(result1)
    result1=u'{}'.format((result1))
    print(result1)
    result1=result1[2:-3]
    name = Label(root, text = (result1)+"                                                                                                   ").place(x = 180,y = 50)

def captn(url):
    global cmb3,subs
    rut=os.popen('youtube-dl --list-subs '+url)
    ot=rut.read()
    b=ot.split("\n")
    if "no subtitles" not in b[-2]:
        for i in range(0,len(b)):
            if "vtt" in b[i]:
                subs.append(b[i])

    streams = Label(root, text = "captions").place(x = 20,y = 160)
    cmb3 = ttk.Combobox(root, width="125", values=subs)
    cmb3.place(x=105,y=160)

def srch(url):
    global cmb,cmb2,cmb3,audlst,vidlst,subs
    stream = os.popen('youtube-dl -F '+url)
    output = stream.read()
    a=(output.split("\n"))
    if audlst!=[]:
        audlst=[]
    if vidlst!=[]:
        vidlst=[]
    if subs!=[]:
        subs=[]
    

    for i in range(0,len(a)):
        if "audio" in a[i] and "tiny" in a[i] or "only" in a[i] and "audio" in a[i]:
            audlst.append(a[i])
    if len(audlst)==0:
        pass
    else:
        audlst.append("mp3_low music 64K")
        audlst.append("mp3_high music 320K")
        audlst.append("m4a_high music")

    for i in range(0,len(a)):
        if "video" in a[i] and "only" in a[i]:
            vidlst.append(a[i])

    cmb = ttk.Combobox(root, width="125", values=vidlst)
    cmb.place(x=105,y=100)
    cmb2 = ttk.Combobox(root, width="125", values=audlst)
    cmb2.place(x=105,y=130)
    streams = Label(root, text = "video streams").place(x = 20,y = 100)
    btn = ttk.Button(root, text="Download",command=checkcmbo)
    btn.place(x=100,y=200)
    streams = Label(root, text = "audio streams").place(x = 20,y = 130)
    t1 = threading.Thread(target=title, args=(url,))
    t1.start()
    t2 = threading.Thread(target=captn, args=(url,))
    t2.start()
    
def on_change(e1):
    global url
    url=e1.widget.get()
    #print(url)
    name = Label(root, text = "loading...                                                                                                                                                                                                                     ").place(x = 180,y = 50)
    tv1 = threading.Thread(target=srch, args=(url,))
    tv1.start()
    #t1.join()
    #name1 = Label(root, text = "Saving file at "+loc).place(x = 160,y = 50)
    
    

e1 = Entry(root,width=70)
e1.place(x=100,y=20)
e1.bind("<Return>", on_change)


#now we create simple function to check what user select value from checkbox

def checkcmbo():
    global tr,c,final,audlst,vidlst,subs
    st=(cmb.get())
    ad=(cmb2.get())
    rs=cmb3.get()
    if rs!="":
        cap=rs.split()
        cap=cap[0]
    loc="\\"+"Downloads"
    try:
        loc=download_Directory
    except:
        pass
    if st!="" and ad=="" and rs=="":
        vid_1=st.split()
        vid=(vid_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(vid,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)

    elif st=="" and ad!="" and "music" not in ad:
        aud_1=ad.split()
        aud=(aud_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)
        
    elif st!="" and ad!="" and rs=="" and "music" not in ad:
        vid_1=st.split()
        vid=(vid_1[0])
        aud_1=ad.split()
        aud=(aud_1[0])
        a=('youtube-dl -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)

    elif st!="" and ad!="" and cap!="":
        vid_1=st.split()
        vid=(vid_1[0])
        aud_1=ad.split()
        aud=(aud_1[0])
        a=('youtube-dl --write-srt --sub-lang {} --embed-subs -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)

    elif "mp3_low" in ad:
        a=('youtube-dl -x --audio-format mp3 --audio-quality 64K -o "{}" '+url).format("~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)

    elif "mp3_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x --audio-format mp3 --audio-quality 320K --embed-thumbnail --add-metadata --metadata-from-title "%(artist)s - %(title)s" '+url+' --exec "ffmpeg -y -i {} -map 0 -c copy -metadata comment=\"\" -metadata description=\"\" -metadata purl=\"\" temp.mp3;cp -r temp.mp3 {};rm -rf temp.mp3"')
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)

    elif "m4a_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x --audio-format m4a --embed-thumbnail --add-metadata --metadata-from-title "%(artist)s - %(title)s" '+url+' --exec "ffmpeg -y -i {} -map 0 -c copy -metadata comment=\"\" -metadata description=\"\" -metadata purl=\"\" temp.m4a;cp -r temp.m4a {};rm -rf temp.m4a"')
        #print(a)
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        name = Label(root, text = "saving file at "+loc).place(x = 180,y = 75)
    else:
        name = Label(root, text = "select stream").place(x = 180,y = 75)

    
    
    c=[]
    final=[]
    audlst=[]
    vidlst=[]
    subs=[]


ext=ttk.Button(root,text="exit",command=root.destroy)
ext.place(x=190,y=200)
btn = ttk.Button(root, text="Github",command=repo)
btn.place(x=280,y=200)
browse_B = ttk.Button(root, text="Browse", command=browse)
browse_B.place(x=370,y=200)
ext11=ttk.Button(root,text="cancel",command=cmder)
ext11.place(x=465,y=200)
ext12=ttk.Button(root,text="update",command=update)
ext12.place(x=700,y=200)
root.iconbitmap(r'logo.ico')
root.title('YouTube-dl GUI')
root.mainloop()
