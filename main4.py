import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from io import BytesIO
import requests
import subprocess,threading,time
root = Tk()
root.geometry("900x320")
root.resizable(False, False)
c=[]
final=[]
audlst=[]
vidlst=[]
subs=[]
#sroot.geometry("400x400")
name1 = Label(root, text = "YouTube-dl GUI",font=('Arial', 18)).place(x = 350,y = 10) 
name = Label(root, text = "URL").place(x = 440,y = 35)#440

#^ Length and width window :D
url=""

def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()


def repo():
    import webbrowser
    webbrowser.open('https://github.com/sourabhkv/ytdl/')

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
        st=popens(a)
        sts=popens(b)
        messagebox.showinfo("YouTube-dl GUI","download cancelled")
    except:
        pass

def viewer(img):
    img.show()

def thumbnail(url):
    global img,image2,vid,thurl,r
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
        #panel.pack(side="left", anchor=NW)
        #panel.place(x=0,y=0)
        picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=0,y=0)
    else:
        u='youtube-dl --get-thumbnail '+url
        u=popens(u)
        url=u
        url=str(url)
        thurl=url[:-1]
        #print(urlimger)
        print(thurl)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        width, height = img.size
        print(width,height)
        img.mode = 'RGB'
        if width==height:
            image = img.resize((135, 135), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(root, image=image2)
            picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            picbtn.place(x=50,y=0)
        else:
            image = img.resize((230, 135), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(root, image=image2)
            picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            picbtn.place(x=0,y=0)
    dwth()

def dwth():
    viewbtn=ttk.Button(root,text="Download thumbnail",command=thdlr)
    viewbtn.place(x=60,y=143)
    

def run_command(cmd):
    global line,name2x
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    #p = subprocess.Popen((command), stdout=subprocess.PIPE,universal_newlines=True, bufsize=1,shell=True)
    for line in iter(p.stdout.readline, b''):
        #root.title(line)
        root.title("Downloading...")
        name2x = Label(root, text = line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10)).place(x =100,y = 290)
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    #pygame.quit()
    root.title("YouTube-dl GUI")
    name2x = Label(root, text = "Download complete                                                                                                                                                                                                         ",font=('Arial', 10)).place(x = 100,y = 290)
    try:
        messagebox.showinfo("YouTube-dl GUI",(result1)+"\nDownload completed!")
    except:
        pass

def convert(s):
    return time.strftime("%H:%M:%S", time.gmtime(s))

def title(url):
    global result1,view,length
    if "youtube" in url:
        from pytube import YouTube
        yt=YouTube(url)
        result1=yt.title
        view=yt.views
        length=int(yt.length)
        length=convert(length)
    elif "youtube" not in url:
        try:
            stream=popens('youtube-dl --get-title --get-duration '+url)
            result1 = stream.split("\n")
            #print(result1,result1[0],result1[1])
            length=str(result1[1])
            result1=str(result1[0])
            print(result1)
        except:
            pass
        #print(result1)
    name = Label(root, text = (result1)+"                                                                                                   ").place(x = 240,y = 125)
    name2 = Label(root, text = "  Title                                                    ").place(x = 430,y = 106)
    if "youtube" in url:
        vl=Label(root,text="Views : "+str(view)+"                ").place(x=620,y=106)
        bl=Label(root,text="Length:  "+str(length)+"                    ").place(x=740,y=106)
    else:
        bl=Label(root,text="Length:  "+str(length)+"                    ").place(x=740,y=106)

def captn(url):
    global cmb3,subs
    rut=popens('youtube-dl --list-subs '+url)
    ot=rut
    b=ot.split("\n")
    if "no subtitles" not in b[-2]:
        for i in range(0,len(b)):
            if "vtt" in b[i]:
                subs.append(b[i])
    if len(subs)==0:
        subs.append("NO CAPTIONS AVAILABLE")
    streams = Label(root, text = "captions").place(x = 20,y = 230) 
    cmb3 = ttk.Combobox(root, width="125", values=subs,state="readonly")
    cmb3.place(x=105,y=230)
    cmb3.current(0)


def paste():
    AnnoyingWindow = Tk()
    ClipBoard = AnnoyingWindow.clipboard_get()
    AnnoyingWindow.destroy()
    ele=ClipBoard
    e1.insert(0, ele )

def clr():
    e1.delete(0,END)

def srch(url):
    global cmb,cmb2,cmb3,audlst,vidlst,subs
    stream = popens('youtube-dl -F '+url)
    output = stream
    #print(output)
    a=(output.split("\n"))
    if audlst!=[]:
        audlst=[]
    if vidlst!=[]:
        vidlst=[]
    if subs!=[]:
        subs=[]
    

    for i in range(0,len(a)):
        if "audio" in a[i] or "mp3" in a[i]:
            audlst.append(a[i])
    if len(audlst)==0:
        pass
    else:
        audlst.append("mp3_low music 64K_only music")
        audlst.append("mp3_high music 320K_only music")
        audlst.append("m4a_high music only_music")
        audlst.append("wav music only_music")
        audlst.append("flac music studio_quality_music 24 bit audio")

    for i in range(0,len(a)):
        if "video" in a[i]  or "mp4" in a[i] and "mp4a" not in a[i]:
            vidlst.append(a[i])

    cmb = ttk.Combobox(root, width="125", values=vidlst,state="readonly")
    cmb.place(x=105,y=170)
    cmb2 = ttk.Combobox(root, width="125", values=audlst,state="readonly")
    cmb2.place(x=105,y=200)
    streams = Label(root, text = "video streams").place(x = 20,y = 170)
    btn = ttk.Button(root, text="Download",command=checkcmbo)
    btn.place(x=95,y=260)
    streams = Label(root, text = "audio streams").place(x = 20,y = 200)
    name2 = Label(root, text = "                                              ").place(x=100,y=290)
    t1 = threading.Thread(target=title, args=(url,))
    t1.start()

def link(n):
    webbrowser.open(n)

def about():
    root2 = Tk()
    root2.geometry("350x350")
    root2.title('YouTube-dl GUI')
    streams = Label(root2, text = "YouTube-dl GUI",font=('Arial', 16)).place(x = 105,y = 0)
    streams2 = Label(root2, text = "This is project is based on youtube-dl, ffmpeg, atomic parsley").place(x = 10,y = 30)
    streams3 = Label(root2, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.").place(x = 70,y = 50)
    streams4 = Label(root2, text = "HOW TO USE").place(x = 140,y = 70)
    streams5 = Label(root2, text = "paste URL hit go you will see available streams").place(x = 50,y = 85)
    streams6 = Label(root2, text = "browse to save location of file").place(x = 110,y = 110)
    streams7 = Label(root2, text = "*some websites may support video streams only or no streams").place(x = 5,y = 130)
    streams6 = Label(root2, text = "Youtube-dl GUI VERISION 21.0511.10").place(x = 80,y = 170)
    streams6 = Label(root2, text = "Changelog- more audio formats added (flac,wav)").place(x = 30,y = 185)
    streams8 = Label(root2, text = "black screen at startup fixed , under the hood change").place(x = 40,y = 202)
    streams8 = Label(root2, text = "download progress output in same window").place(x=55,y=218)
    ext13=ttk.Button(root2,text="try VLC",command= lambda: link('https://www.videolan.org/'))
    ext13.place(x=140,y=250)
    ext13=ttk.Button(root2,text="supported websites",command= lambda: link('http://ytdl-org.github.io/youtube-dl/supportedsites.html'))
    ext13.place(x=120,y=280)
    ext13=ttk.Button(root2,text="YouTube-dl GUI",command= lambda: link('https://youtube-dl.org/'))
    ext13.place(x=30,y=315)
    ext13=ttk.Button(root2,text="ffmpeg",command= lambda: link('https://www.ffmpeg.org/'))
    ext13.place(x=138,y=315)
    ext13=ttk.Button(root2,text="Atomicparsley", command= lambda: link('http://atomicparsley.sourceforge.net/'))
    ext13.place(x=230,y=315)
    root2.resizable(False, False)
    root2.iconbitmap(r'logo.ico')
    root2.mainloop()

def kill():
    time.sleep(5)
    a="taskkill /F /IM powershell.exe"
    popens(a)
    
def explr(lc):
    tv1 = threading.Thread(target=kill)
    tv1.start()
    popens("powershell explorer "+lc)
    
def on_change(e1):
    global url
    try:
        url=e1.widget.get()
    except:
        url=e1.get()
    #print(url)
    if url=="":
        messagebox.showinfo("YouTube-dl GUI","  Enter URL  ")
    else:
        name3 = Label(root, text = "                                                                                                                                                                                                                                                                                                ").place(x = 240,y = 125)
        name = Label(root, text = "loading...                                                                                                                                                                                                                     ").place(x =430,y = 106)
        tv1 = threading.Thread(target=srch, args=(url,))
        tv1.start()
        tv2 = threading.Thread(target=thumbnail, args=(url,))
        tv2.start()
        t2 = threading.Thread(target=captn, args=(url,))
        t2.start()

e1 = Entry(root,width=70)
e1.place(x=240,y=55)
e1.bind("<Return>", on_change)

def thdlr():
    userloc=(os.environ['USERPROFILE'])
    loc=userloc.replace("\\","/")
    loc=loc+"/Downloads"
    #loc="/"+"Downloads"
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
            if i.isalpha() or i.isspace():
                propername=propername+i
        filename=loc+"/"+propername+"_Thumbnail"+".jpg"
        response = requests.get(url2)
        with open(filename, "wb") as f:
            f.write(response.content)
        messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
    else:
        propername=""
        for i in result1:
            if i.isalpha() or i.isspace():
                propername=propername+i
        filename=loc+"/"+propername+"_Thumbnail"+".jpg"
        with open(filename, "wb") as f:
            f.write(r.content)
        messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
    
    

#now we create simple function to check what user select value from checkbox

def checkcmbo():
    global tr,c,final,audlst,vidlst,subs
    st=(cmb.get())
    ad=(cmb2.get())
    try:
        rs=cmb3.get()
    except:
        rs=""
    if rs!="":
        cap=rs.split()
        cap=cap[0]
    elif rs=="" or rs=="NO CAPTIONS AVAILABLE":
        cap=""
    userloc=(os.environ['USERPROFILE'])
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
    print(loc)
    if st!="" and ad=="" and rs=="":
        vid_1=st.split()
        vid=(vid_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(vid,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                  ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))

    elif st=="" and ad!="" and "music" not in ad:
        aud_1=ad.split()
        aud=(aud_1[0])
        a=('youtube-dl -f "{}" -o "{}" '+url).format(aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                  ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))
        
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
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                   ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))

    elif st!="" and ad!="" and cap!="":
        vid_1=st.split()
        vid=(vid_1[0])
        vidf=vid_1[1]
        aud_1=ad.split()
        aud=(aud_1[0])
        audf=aud_1[1]
        if audf==vidf:
            a=('youtube-dl --write-srt --sub-lang {} --embed-subs -f "{}"+"{}" -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        else:
            a=('youtube-dl --write-srt --sub-lang {} --embed-subs -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt,fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))

    elif "mp3_low" in ad:
        a=('youtube-dl -x --audio-format mp3 --audio-quality 64K -o "{}" '+url).format("~"+loc+"/"+"%(title)s.%(ext)s")
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                     ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))

    elif "mp3_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format mp3 --audio-quality 320K --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
        t1 = threading.Thread(target=run_command, args=(a,))
        t1.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                     ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))

    elif "m4a_high" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format m4a --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
        #print(a)
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                      ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))
    elif "wav music only_music" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format wav --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
        #print(a)
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                      ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))
    elif "flac music studio_quality_music 24 bit audio" in ad:
        a=('youtube-dl -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format flac --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
        #print(a)
        p2 = threading.Thread(target=run_command ,args=(a, ))
        p2.start()
        name = Label(root, text = "saving file at                                                                                                                                                                  ").place(x = 240,y = 145)
        name7 = Label(root, text = cpt+"                                                      ",fg="blue",cursor="hand2")
        name7.place(x = 300,y = 145)
        name7.bind("<Button-1>", lambda e: explr(cpt))
        
    else:
        messagebox.showerror("YouTube-dl GUI","select stream")

    
    
    c=[]
    final=[]
    audlst=[]
    vidlst=[]
    subs=[]


image = Image.open("logo.png")
resize_image = image.resize((25, 25))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.place(x=535,y=10)
ext=ttk.Button(root,text="exit",command=root.destroy)
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
#labelimg.place(x=20,y=10)
root.mainloop()
