import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
import os,time
from io import BytesIO
import requests
import subprocess,threading,time
root = Tk()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
y=int((sh-320)/2)
x=int((sw-900)/2)
root.geometry('%dx%d+%d+%d' % (900, 320, x, y))


root.resizable(False, False)
audlst=[]
vidlst=[]
subs=[]

name1 = Label(root, text = "YouTube-dl GUI",font=('Arial', 18)).place(x = 350,y = 10) 
name = Label(root, text = "URL").place(x = 440,y = 35)#440
name = Label(root, text = "saving file                                                                                                                                                                     ").place(x = 240,y = 145)
userloc=(os.environ['USERPROFILE'])+"\\Downloads"
name7 = Label(root, text = userloc,fg="blue",cursor="hand2")
name7.place(x = 300,y = 145)
name7.bind("<Button-1>", lambda e: explorer(userloc))
#^ Length and width window :D
url=""

def explorer(a):
    os.startfile(a)
    
def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()


def repo():
    import webbrowser
    webbrowser.open('https://github.com/sourabhkv/ytdl/')

def update():
    t1 = threading.Thread(target=run_command2, args=("youtube-dl -U",))
    t1.start()
    
def browse():
    global download_Directory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
    if download_Directory=="":
        download_Directory=userloc
    name7 = Label(root, text = download_Directory,fg="blue",cursor="hand2")
    name7.place(x = 300,y = 145)
    name7.bind("<Button-1>", lambda e: explr(download_Directory))

def cmder():
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM youtube-dl.exe"
    try:
        st=popens(a)
        sts=popens(b)
        btn['state'] = NORMAL
        messagebox.showinfo("YouTube-dl GUI","download cancelled")
    except:
        pass

def cmderx():
    b="taskkill /F /IM youtube-dl.exe"
    sts=popens(b)
    c="taskkill /F /IM youtube-dl.exe"
    stb=popens(c)

def viewer(img):
    img.show()


def thumbnail(url):
    global img,image2,vid,thurl,r,picbtn
    if "youtube" in url and "music" not in url:
        d=url.find("=")
        vid=url[d+1:]
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((230, 135), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        panel = Label(root, image=image2)
        picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=0,y=0)
        dwth()
    else:
        u='youtube-dl --get-thumbnail '+url
        u=popens(u)
        url=u
        url=str(url)
        thurl=url[:-1]
        try:
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            width, height = img.size
            i=1
            while (i)>0:
                if (i*height)<=135 and (i*width)<=230:
                    break
                else:
                    i=i-0.001
            nw=int(i*width)
            nh=int(i*height)
            sp=int((230-nw)/2)
            print(nw,nh)
            image = img.resize(((nw),(nh)), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(root, image=image2)
            picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            picbtn.place(x=sp,y=0)
            dwth()
        except:
            name = Label(root, text = "Thumbnail not available").place(x = 40,y = 53)
            

def dwth():
    global viewbtn
    viewbtn=ttk.Button(root,text="Download thumbnail",command=thdlr)
    viewbtn.place(x=60,y=143)

def run_command2(cmd):
    global line,name2x
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading update...]")
        name2x = Label(root, text = line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10)).place(x =100,y = 290)
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    root.title("YouTube-dl GUI")
    name2x = Label(root, text = "Updated                                                                                                                                                                                                         ",font=('Arial', 10)).place(x = 100,y = 290)
    messagebox.showinfo("YouTube-dl GUI","Youtube-dl \nUpdate completed!")

def run_command(cmd):
    btn['state'] = DISABLED
    global line,name2x,pro
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading...]")
        name2x = Label(root, text = line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10)).place(x =100,y = 290)
        if str(line)=="":
            break
    btn['state'] = NORMAL
    p.stdout.close()
    p.wait()
    root.title("YouTube-dl GUI")
    name2x = Label(root, text = "Download complete                                                                                                                                                                                                         ",font=('Arial', 10)).place(x = 100,y = 290)
    try:
        messagebox.showinfo("YouTube-dl GUI",(result1)+"\nDownload completed!")
    except:
        pass

def title(url):
    global result1,view,length,result1,lengthx
    if "youtube" in url or "youtu" in url:
        global yt
        from pytube import YouTube
        yt=YouTube(url)
        result1=yt.title
        lengthx=time.strftime("%H:%M:%S", time.gmtime(yt.length))
    else:
        stream=popens('youtube-dl --get-title --get-duration '+url)
        result1 = stream.split("\n")
        lengthx=str(result1[1])
        result1=str(result1[0])
    name2 = Label(root, text = "  Title                                                    ").place(x = 430,y = 106)
    bl=Label(root,text="Duration:  "+str(lengthx)+"                    ").place(x=760,y=106)
    name = Label(root, text = (result1)+"                                                                                                   ").place(x = 240,y = 125)
    
def captn(url):
    global cmb3,subs
    rut=popens('youtube-dl --list-subs '+url)
    ot=rut
    b=ot.split("\n")
    print(b)
    r=0
    for i in range(-1,-1-len(b),-1):
        if 'Available subtitles' in b[i]:
            r=i
            break
    b=b[r:]
    if "no subtitles" not in b[-2]:
        for i in range(0,len(b)):
            if "vtt" in b[i] and "srv" in b[i]:
                subs.append(b[i])

    streams = Label(root, text = "captions").place(x = 20,y = 230) 
    if len(subs)==0:
        subs.append("no captions available")
        cmb3 = ttk.Combobox(root, width="125", values=subs,state="readonly")
        cmb3.place(x=105,y=230)
        cmb3.current(0)
    else:
        cmb3 = ttk.Combobox(root, width="125", values=subs,state="readonly")
        cmb3.place(x=105,y=230)

def paste():
    try:
        AnnoyingWindow=Tk()
        ClipBoard = AnnoyingWindow.clipboard_get()
        AnnoyingWindow.destroy()
        ele=ClipBoard
        e1.insert(0, ele )
    except:
        AnnoyingWindow.destroy()
        messagebox.showerror("YouTube-dl GUI","URL should be in text")

def terminal():
    t1s = threading.Thread(target=popens, args=("start.bat",))
    t1s.start()

def clr():
    e1.delete(0,END)

def srch(url):
    global cmb,cmb2,cmb3,audlst,vidlst,subs,rest,btn
    stream = popens('youtube-dl -F '+url)
    output = stream
    if audlst!=[]:
        audlst=[]
    if vidlst!=[]:
        vidlst=[]
    if subs!=[]:
        subs=[]
    if True:
        a=(output.split("\n"))

        for i in range(0,len(a)):
            if "vp9" in a[i] or "video" in a[i] and "[info]" not in "[download]" not in a[i] and "[generic]" not in a[i] or "fps" in a[i] or "avc1" in a[i]  or "mp4" in a[i] and "mp4a" not in a[i] and "audio" not in a[i]:
                vidlst.append(a[i])
                
        for i in range(0,len(a)):
            if "audio" in a[i] or "mp3" in a[i] or "m4a" in a[i]:
                audlst.append(a[i])
        if (len(audlst))==0 and (len(vidlst))==0:
            cmb2 = ttk.Combobox(root, width="125", values=audlst,state="readonly")
            cmb2.place(x=105,y=200)
            if yt.age_restricted:
                messagebox.showwarning("YouTube-dl GUI","Age-resticted content")
            else:
                messagebox.showerror("YouTube-dl GUI","URL/Website not supported or Stream might be DRM protected \nStream might be age-restricted \nTry using VPN \nIf you see this error again with VPN Website is not supported :( \n Go to About->Supported websites")

        if len(audlst)==0 and len(vidlst)!=0:
            audlst.append("no separate audio streams available audio included in video stream")
            cmb2 = ttk.Combobox(root, width="125", values=audlst,state="readonly")
            cmb2.place(x=105,y=200)
            streamsaud = Label(root, text = "audio streams").place(x = 20,y = 200)
            cmb2.current(0)
        if "no separate audio streams available audio included in video stream" not in audlst:
            audlst.append("mp3_low music 64K_only music")
            audlst.append("mp3_high music 320K_only music")
            audlst.append("m4a_high music only_music")
            audlst.append("wav music only_music")
            audlst.append("flac music studio_quality_music 24 bit audio")
            cmb2 = ttk.Combobox(root, width="125", values=audlst,state="readonly")
            streamsaud = Label(root, text = "audio streams").place(x = 20,y = 200)
            cmb2.place(x=105,y=200)

        
        cmb = ttk.Combobox(root, width="125", values=vidlst,state="readonly")
        cmb.place(x=105,y=170)
        streamsvid = Label(root, text = "video streams").place(x = 20,y = 170)
        global btn
        btn = ttk.Button(root, text="Download",state=NORMAL,command=checkcmbo)
        btn.place(x=95,y=260)
        root.title("YouTube-dl GUI")


def link(n):
    import webbrowser
    webbrowser.open(n)

def about():
    root2 = tk.Tk()
    y=int((sh-350)/2)
    x=int((sw-350)/2)
    root2.geometry('%dx%d+%d+%d' % (350, 350, x, y))
    root2.title('YouTube-dl GUI')
    streams = Label(root2, text = "YouTube-dl GUI",font=('Arial', 16)).place(x = 105,y = 0)
    streams2 = Label(root2, text = "This is project is based on youtube-dl, ffmpeg, atomic parsley").place(x = 10,y = 30)
    streams3 = Label(root2, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 10,'bold'),fg="red").place(x = 30,y = 50)
    streams4 = Label(root2, text = "HOW TO USE").place(x = 140,y = 70)
    streams5 = Label(root2, text = "paste URL hit go you will see available streams").place(x = 50,y = 85)
    streams6 = Label(root2, text = "browse to save location of file").place(x = 110,y = 110)
    streams7 = Label(root2, text = "*some websites may support video streams only or no streams").place(x = 5,y = 130)
    streams6 = Label(root2, text = "Youtube-dl GUI VERISION 21.068.02").place(x = 80,y = 170)
    streams6 = Label(root2, text = "Changelog- fixed app not responding after opening terminal").place(x = 15,y = 185)
    streams8 = Label(root2, text = "Age restricted content may not work, title in UTF-8 character").place(x = 10,y = 202)
    streams8 = Label(root2, text = "Faster app launch, missing dll fixed, bugs fixes").place(x=45,y=220)
    ext13=ttk.Button(root2,text="supported websites",command= lambda: link('http://ytdl-org.github.io/youtube-dl/supportedsites.html'))
    ext13.place(x=120,y=280)
    name74 = Label(root2, text = "CREDITS:").place(x=40,y=315)
    name74 = Label(root2, text = "YouTube-dl",fg="blue",cursor="hand2")
    name74.place(x = 95,y = 315)
    name74.bind("<Button-1>", lambda e: link('https://youtube-dl.org/'))
    name73 = Label(root2, text = "ffmpeg",fg="blue",cursor="hand2")
    name73.place(x = 170,y = 315)
    name73.bind("<Button-1>", lambda e: link('https://www.ffmpeg.org/'))
    name75 = Label(root2, text = "AtomicParsley",fg="blue",cursor="hand2")
    name75.place(x = 220,y = 315)
    name75.bind("<Button-1>", lambda e: link('http://atomicparsley.sourceforge.net/'))
    root2.resizable(False, False)
    root2.iconbitmap(r'logo.ico')
    root2.mainloop()
    
def explr(lc):
    os.startfile(lc)
    
def on_change(e1):
    global url,nameloading
    try:
        url=e1.widget.get()
    except:
        url=e1.get()
    try:
        cmb.destroy()
        cmb2.destroy()
        cmb3.destroy()
        viewbtn.destroy()
        btn.destroy()
        picbtn.destroy()
        nd=Label(root, text="                        ").place(x=20,y=170)
        nd=Label(root, text="                        ").place(x=20,y=200)
        nd=Label(root, text="                        ").place(x=20,y=230)
        name2 = Label(root, text = "                                              ").place(x=100,y=290)
    except:
        pass
    #print(url)
    if url=="":
        messagebox.showerror("YouTube-dl GUI","  Enter URL  ")
    else:
        t1w = threading.Thread(target=title, args=(url,))
        t1w.start()
        t2 = threading.Thread(target=captn, args=(url,))
        t2.start()
        name3 = Label(root, text = "                                                                                                                                                                                                                                                                                                ").place(x = 240,y = 125)
        nameloading = Label(root, text = "Loading...                                                                                                                                                                                                                     ").place(x =430,y = 106)
        root.title("YouTube-dl GUI  [Loading...]")
        tv1 = threading.Thread(target=srch, args=(url,))
        tv1.start()
        tv2 = threading.Thread(target=thumbnail, args=(url,))
        tv2.start()

e1 = ttk.Entry(root,width=70)
e1.place(x=240,y=55)
e1.bind("<Return>", on_change)

def thdlr():
    loc=userloc.replace("\\","/")
    loc=loc+"/Downloads"
    try:
        loc=download_Directory
        cpt=download_Directory
        cpt=cpt.replace("/","\\")
        if "C:" in loc:
            loc=loc.replace("/","\\")
            rloc=loc.lstrip(userloc)
            loc2="\\"+rloc
            loc=loc2
    except:
        pass
    if "youtube" in url:
        url2 = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(vid)
        propername=""
        for i in result1:
            if i.isalpha() or i.isspace() or i.isnumeric():
                propername=propername+i
        filename=loc+"/"+propername+"_Thumbnail"+".jpg"
        response = requests.get(url2)
        imgthd = Image.open(BytesIO(response.content))
        width2,height2=imgthd.size
        print(width2,height2)
        if width2==120 or height2==90:
            url2 = "https://i.ytimg.com/vi/{}/sddefault.jpg".format(vid)
            response = requests.get(url2)
        with open(filename, "wb") as f:
            f.write(response.content)
        messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
    else:
        propername=""
        for i in result1:
            if i.isalpha() or i.isspace() or i.isnumeric():
                propername=propername+i
        filename=loc+"/"+propername+"_Thumbnail"+".jpg"
        with open(filename, "wb") as f:
            f.write(r.content)
        messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")


def checkcmbo():
    loc="/"+"Downloads"
    cpt=userloc+"\\Downloads"
    try:
        loc=download_Directory
        cpt=download_Directory
        cpt=cpt.replace("/","\\")
        if "C:" in loc:
            loc=loc.replace("/","\\")
            rloc=loc.lstrip(userloc)
            loc2="\\"+rloc
            loc=loc2
    except:
        pass

    
    global tr,audlst,vidlst,subs
    st=(cmb.get())
    ad=(cmb2.get())
    rs=cmb3.get()
    if ad=="no separate audio streams available audio included in video stream":
        ad=""
    if rs=="no captions available":
        rs=""
    
    print(st,len(st))
    print(ad,len(ad))
    print(rs,len(rs))
    #print(loc)
    if ad=="" and rs=="" and st!="":
        vid_1=st.split()
        vid=(vid_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(vid,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("1")
        return 
        
    if st=="" and ad=="":
        messagebox.showerror("YouTube-dl GUI","select audio/video stream")
    elif "mp3_low" in ad:
        a=('youtube-dl -x --audio-format mp3 --audio-quality 64K -o "{}" '+url).format("~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("5")
        return

    elif "mp3_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format mp3 --audio-quality 320K --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("6")
        return

    elif "m4a_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format m4a --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        print("7")
        return
        
    elif "wav music only_music" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format wav --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        print("8")
        return
    elif "flac music studio_quality_music 24 bit audio" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format flac --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        print("9")
        return

    elif st=="" and ad!="":
        aud_1=ad.split()
        aud=(aud_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("2")
        return
        
    elif st!="" and ad!="" and rs=="" and "music" not in ad:
        vid_1=st.split()
        vid=(vid_1[0])
        aud_1=ad.split()
        aud=(aud_1[0])
        vidf=vid_1[1]
        audf=aud_1[1]
        if audf==vidf:
            a=('youtube-dl -f "{}"+"{}" -o "{}" '+url).format(vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        else:
            a=('youtube-dl -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("3")
        return

    elif st!="" and ad!="" and rs!="":
        vid_1=st.split()
        vid=(vid_1[0])
        vidf=vid_1[1]
        aud_1=ad.split()
        aud=(aud_1[0])
        audf=aud_1[1]
        cap=rs.split()
        cap=cap[0]
        if audf==vidf:
            a=('youtube-dl --write-srt --sub-lang {} --embed-subs -f "{}"+"{}" -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        else:
            a=('youtube-dl --write-srt --sub-lang {} --embed-subs -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        print("4")
        return
    
    else:
        messagebox.showerror("YouTube-dl GUI","Select stream")

    
    
    audlst=[]
    vidlst=[]
    subs=[]


image = Image.open("logo.png")
resize_image = image.resize((25, 25))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.place(x=535,y=10)
ext=ttk.Button(root,text="Terminal",command= terminal)
ext.place(x=370,y=260)
btn = ttk.Button(root, text="Github",command=repo)
btn.place(x=465,y=260)
browse_B = ttk.Button(root, text="Browse", command=browse)
browse_B.place(x=190,y=260)
ext11=ttk.Button(root,text="cancel",command=cmder)
ext11.place(x=280,y=260)
ext12=ttk.Button(root,text="Update",command=update)
ext12.place(x=650,y=260)
ext13=ttk.Button(root,text="About",command=about)
ext13.place(x=560,y=260)
ext15=ttk.Button(root,text="Paste",command=paste)
ext15.place(x=370,y=80)
ext16=ttk.Button(root,text="Clear",command=clr)
ext16.place(x=465,y=80)
ext17=ttk.Button(root,text="GO",command=lambda: on_change(e1))
ext17.place(x=680,y=53)
root.iconbitmap(r'logo.ico')
root.title('YouTube-dl GUI')
root.mainloop()
