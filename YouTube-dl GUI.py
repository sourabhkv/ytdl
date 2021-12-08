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
import urllib.request
import json, urllib
import tkinter.font as tkFont

music=[]
root = Tk()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
y=int((sh-420)/2)
x=int((sw-940)/2)
root.geometry('%dx%d+%d+%d' % (940, 420, x, y))

root.resizable(False, False)
audlst=[]
vidlst=[]
subs=[]
thn=[1]

name1 = Label(root, text = "YouTube-dl GUI",font=('Arial', 18)).place(x = 380,y = 10) 
name = Label(root, text = "URL").place(x = 45,y = 55)
name = Label(root, text = "Output").place(x = 40,y = 110)
name = Label(root, text = "Custom Filename").place(x = 17,y = 135)
userloc=(os.environ['USERPROFILE'])+"\\Downloads"

statusbar = tk.Label(root, text="",width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)

url=""

text_box = Text(root,height=8,width=38 )
fonte = tkFont.Font(family="Arial", size=10)

sb_ver = Scrollbar(root,orient=VERTICAL)
sb_ver.place(x=925,y=240)
text_box.config(yscrollcommand=sb_ver.set,font=fonte,state= NORMAL)
sb_ver.config(command=text_box.yview)

def explorer(a):
    os.startfile(a)

def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()

def terminal():
    t1s = threading.Thread(target=popens, args=("start.bat",))
    t1s.start()

def repo(url):
    import webbrowser
    webbrowser.open(url)

def browse():
    global download_Directory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    if download_Directory=="":
        download_Directory=userloc
    e2.delete(0,END)
    e2.insert(0,download_Directory)

def Resume():
    global statusbar
    ext12fx=ttk.Button(root,text="Pause",command=pause)
    ext12fx.place(x=650,y=360)
    checkcmbo()

def pause():
    global statusbar
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM yt-dlp_x86.exe"
    try:
        st=popens(a)
        sts=popens(b)
        btn['state'] = NORMAL
        ext12fx=ttk.Button(root,text="Resume",command=Resume)
        ext12fx.place(x=650,y=360)
        messagebox.showinfo("YouTube-dl GUI","Download Paused")
    except:
        pass


def cmder():
    ext11.destroy()
    ext12fx.destroy()
    t1 = threading.Thread(target=cmderx)
    t1.start()

def cmderx():
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM yt-dlp_x86.exe"
    try:
        st=popens(a)
        sts=popens(b)
        btn['state'] = NORMAL
        title=result1.replace("|","_")#title org
        #print(title)
        #print(customname)#given title
        #print(vid,aud)
        loc=e2.get()
        #print(loc)
        if customname=="":
            if os.path.exists(loc+"\\"+title+".f"+vid+"."+codec1+".part"):
                os.remove(loc+"\\"+title+".f"+vid+"."+codec1+".part")
            if os.path.exists(loc+"\\"+title+".f"+aud+"."+codec2+".part"):
                os.remove(loc+"\\"+title+".f"+aud+"."+codec2+".part")
            if os.path.exists(loc+"\\"+title+".f"+vid+"."+codec1):
                os.remove(loc+"\\"+title+".f"+vid+"."+codec1)
        elif customname!="":
            if os.path.exists(loc+"\\"+customname+".f"+vid+"."+codec1+".part"):
                os.remove(loc+"\\"+customname+".f"+vid+"."+codec1+".part")
            if os.path.exists(loc+"\\"+customname+".f"+aud+"."+codec2+".part"):
                os.remove(loc+"\\"+customname+".f"+aud+"."+codec2+".part")
            if os.path.exists(loc+"\\"+customname+".f"+vid+"."+codec1):
                os.remove(loc+"\\"+customname+".f"+vid+"."+codec1)
                
        messagebox.showinfo("YouTube-dl GUI","Download Cancelled")
    except:
        pass

def update():
    t1 = threading.Thread(target=run_command2, args=("yt-dlp_x86 -U",))
    t1.start()

def about():
    root2 = tk.Tk()
    y=int((sh-350)/2)
    x=int((sw-350)/2)
    root2.geometry('%dx%d+%d+%d' % (350, 350, x, y))
    root2.title('YouTube-dl GUI')
    streams = Label(root2, text = "YouTube-dl GUI",font=('Arial', 16)).place(x = 105,y = 0)
    streams2 = Label(root2, text = "This is project is based on yt-dlp, ffmpeg, atomic parsley").place(x = 15,y = 30)
    streams3 = Label(root2, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 10,'bold'),fg="red").place(x = 30,y = 50)
    streams4 = Label(root2, text = "HOW TO USE").place(x = 140,y = 70)
    streams5 = Label(root2, text = "paste URL hit go you will see available streams").place(x = 50,y = 85)
    streams6 = Label(root2, text = "browse to save location of file").place(x = 110,y = 110)
    streams7 = Label(root2, text = "*some websites may support video streams only or no streams").place(x = 5,y = 130)
    streams6 = Label(root2, text = "YouTube-dl GUI VERISION 21.124.12").place(x = 80,y = 163)
    streams6 = Label(root2, text = "Changelog- Complete design change, Separate music section").place(x = 10,y = 180)
    streams8 = Label(root2, text = "Cancelling download deletes incompletely downloaded files").place(x = 10,y = 200)
    streams8 = Label(root2, text = "Better thumbnail preview, new option button added").place(x=35,y=220)
    ext13=ttk.Button(root2,text="supported websites",command= lambda: link('http://ytdl-org.github.io/youtube-dl/supportedsites.html'))
    ext13.place(x=120,y=280)
    name74 = Label(root2, text = "CREDITS:").place(x=40,y=315)
    name74 = Label(root2, text = "yt-dlp",fg="blue",cursor="hand2")
    name74.place(x = 95,y = 315)
    name74.bind("<Button-1>", lambda e: link('https://github.com/yt-dlp/yt-dlp'))
    name73 = Label(root2, text = "ffmpeg",fg="blue",cursor="hand2")
    name73.place(x = 155,y = 315)
    name73.bind("<Button-1>", lambda e: link('https://www.ffmpeg.org/'))
    name75 = Label(root2, text = "AtomicParsley",fg="blue",cursor="hand2")
    name75.place(x = 220,y = 315)
    name75.bind("<Button-1>", lambda e: link('http://atomicparsley.sourceforge.net/'))
    root2.resizable(False, False)
    root2.iconbitmap(r'logo.ico')
    root2.mainloop()

def reco():
    root3 = tk.Tk()
    y=int((sh-350)/2)
    x=int((sw-420)/2)
    root3.geometry('%dx%d+%d+%d' % (420, 350, x, y))
    root3.title('YouTube-dl GUI')
    streams = Label(root3, text = "YouTube-dl GUI",font=('Arial', 16)).place(x = 150,y = 0)
    streams3 = Label(root3, text = "Recommended Streams selection/combination").place(x = 90,y = 30)
    streams4 = Label(root3, text = "1. Video stream --> AVC1").place(x = 150,y = 50)
    streams5 = Label(root3, text = "   Audio stream --> M4a").place(x = 152,y = 65)
    streams6 = Label(root3, text = "2. Video stream -->  VP9").place(x = 150,y = 90)
    streams7 = Label(root3, text = "   Audio stream --> Opus").place(x = 152,y = 105)
    streams8 = Label(root3, text = "NOTE",font=('Arial', 12),fg="red").place(x = 200,y = 150)
    streams8 = Label(root3, text = "Choice 1 ONLY Supports subtitles and embeding metadata for video").place(x = 20,y = 170)
    streams8 = Label(root3, text = "Music with Flac does not support album art and will take more space").place(x = 20,y = 190)
    streams8 = Label(root3, text = "If custom filename is left blank default name of file will be title of video").place(x = 15,y = 210)
    root3.resizable(False, False)
    root3.iconbitmap(r'logo.ico')
    root3.mainloop()

def title(url):
    global result1,view,length,lengthx,data
    if "youtube" not in url:
        stream=popens('yt-dlp_x86 --get-title --get-duration '+url)
        result1 = stream.split("\n")
        if len(result1[1])==0 and len(result1[0])==0:
            kl="taskkill /F /IM yt-dlp_x86.exe"
            try:
                popens(kl)
            except:
                pass
            messagebox.showerror("YouTube-dl GUI","Video unavailable \n These might be the cause\n Video is DRM protected \n Internet not available")
    
        lengthx=str(result1[1])#time
        result1=str(result1[0])#title
        text_box.place(x=650,y=220)
        data=result1+"\n"+"\nDuration : "+lengthx
        text_box.delete(1.0,"end")
        text_box.insert(1.0, data)

    else:
        stream=popens('yt-dlp_x86 --get-duration --get-description '+url)
        result1 = stream.split("\n")
        lengthx=str(result1.pop(-2))#time
        desc=""
        for i in range(0,len(result1)):
            desc=desc+result1[i]+"\n"

        VideoID=url[32:]
        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
        urlf = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        urlf = urlf + "?" + query_string
        with urllib.request.urlopen(urlf) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            result1.append(data['title'])

        result1=result1[-1]
        text_box.place(x=650,y=220)
        try:
            data=str(result1)+"\n"+"\nDuration : "+lengthx+"\n"+"\nDescription: "+str(desc)
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)
        except:
            data=str(result1)+"\n"+"\nDuration : "+lengthx+"\n"
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)

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

def srch(url):
    global cmb,cmb2,cmb3,cmb4,audlst,vidlst,subs,rest,btn,music,streamsvid,streamsaud,btn
    stream = popens('yt-dlp_x86 -F '+url)
    output = stream
    if audlst!=[]:
        audlst=[]
    if vidlst!=[]:
        vidlst=[]
    if subs!=[]:
        subs=[]
    if music!=[]:
        music=[]
    if True:
        a=(output.split("\n"))

        for i in range(0,len(a)):
            if "3gp" in a[i] or "vp9" in a[i] or "video" in a[i] and "[info]" not in a[i] and "[download]" not in a[i] and "[generic]" not in a[i] or "fps" in a[i] or "avc1" in a[i]  or "mp4" in a[i] and "mp4a" not in a[i] and "audio" not in a[i]:
                vidlst.append(a[i])
                
        for i in range(0,len(a)):
            if "audio" in a[i] or "mp3" in a[i] or "m4a" in a[i]:
                audlst.append(a[i])
        if (len(audlst))==0 and (len(vidlst))==0:
            messagebox.showerror("YouTube-dl GUI","URL not supported or Stream might be DRM protected \nStream might be age-restricted \nTry using VPN \nIf you see this error again with VPN Website is not supported :( \n Go to About->Supported websites")

        if len(audlst)==0 and len(vidlst)!=0:
            audlst.append("no separate audio streams available audio included in video stream")
            music.append("Music not available")
            cmb2 = ttk.Combobox(root, width="95", values=audlst,state="readonly")
            cmb2.place(x=30,y=260)
            streamsaud = Label(root, text = "audio streams").place(x = 30,y = 230)
            cmb2.current(0)
            cmb4 = ttk.Combobox(root, width="41", values=music,state="readonly")
            cmb4.place(x=355,y=320)
            cmb4.current(0)  
        
        if "no separate audio streams available audio included in video stream" not in audlst:
            music.append("mp3_low music 64K_only music")
            music.append("mp3_high music 320K_only music")
            music.append("m4a_high music only_music")
            music.append("wav music only_music")
            music.append("flac music studio_quality_music 24 bit audio")
            cmb2 = ttk.Combobox(root, width="95", values=audlst,state="readonly")
            cmb2.place(x=30,y=260)
            streamsaud = Label(root, text = "Audio streams").place(x = 30,y = 230)
            cmb4 = ttk.Combobox(root, width="41", values=music,state="readonly")
            streamsaud = Label(root, text = "Convert to Music").place(x = 355,y = 290)
            cmb4.place(x=355,y=320)

        
        cmb = ttk.Combobox(root, width="95", values=vidlst,state="readonly")
        cmb.place(x=30,y=200)
        streamsvid = Label(root, text = "Video streams").place(x = 30,y = 170)
        btn = ttk.Button(root, text="Download",state=NORMAL,command=checkcmbo)
        btn.place(x=745,y=360)
        statusbar = tk.Label(root, text="                                                                                                                                                                                                        ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)

def thdlr():
    global customname
    customname=e3.get()
    loc=userloc.replace("\\","/")
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
        if len(customname)==0:
            url2 = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(vid)
            propername=""
            for i in result1:
                if i.isalpha() or i.isspace() or i.isnumeric():
                    propername=propername+i
            filename=loc+"/"+propername+"_Thumbnail"+".jpg"
            response = requests.get(url2)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
        else:
            url2 = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(vid)
            filename=loc+"/"+customname+".jpg"
            response = requests.get(url2)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
    else:
        if len(customname)==0:
            propername=""
            for i in result1:
                if i.isalpha() or i.isspace() or i.isnumeric():
                    propername=propername+i
            filename=loc+"/"+propername+"_Thumbnail"+".jpg"
            try:
                response = requests.get(thurl)
            except:
                pass
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")
        else:
            filename=loc+"/"+customname+".jpg"
            try:
                response = requests.get(thurl)
            except:
                pass
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            messagebox.showinfo("YouTube-dl GUI",(filename)+" \nDownload completed!")

def captn(url):
    global cmb3,subs,cationlb
    rut=popens('yt-dlp_x86 --list-subs '+url)
    ot=rut
    b=ot.split("\n")
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

    cationlb = Label(root, text = "Captions").place(x = 30,y = 290) 
    if len(subs)==0:
        subs.append("no captions available")
        cmb3 = ttk.Combobox(root, width="47", values=subs,state="readonly")
        cmb3.place(x=30,y=320)
        cmb3.current(0)
    else:
        cmb3 = ttk.Combobox(root, width="47", values=subs,state="readonly")
        cmb3.place(x=30,y=320)

def viewer(img):
    img.show()

def thdlrz():
    tv2 = threading.Thread(target=thdlr)
    tv2.start()

def thumbnail(url):
    global img,image2,vid,thurl,r,picbtn
    if "youtube" in url and "music" not in url:
        d=url.find("=")
        vid=url[d+1:]
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((270, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        panel = Label(root, image=image2)
        picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=645,y=20)
        dwth()
    else:
        u='yt-dlp_x86 --get-thumbnail '+url
        u=popens(u)
        url=u
        url=str(url)
        thurl=url[:-1]
        try:
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            width, height = img.size
            i=2
            while (i)>0:
                if (i*height)<=165 and (i*width)<=260:
                    break
                else:
                    i=i-0.1
            nw=int(i*width)
            nh=int(i*height)
            sp=int((230-nw)/2)
            #print(nw,nh)
            image = img.resize(((nw),(nh)), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(root, image=image2)
            picbtn=Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            picbtn.place(x=sp+665,y=20)
            dwth()
        except:
            name = Label(root, text = "Thumbnail not available").place(x = 700,y = 70)

def dwth():
    global viewbtn
    viewbtn=ttk.Button(root,text="Download thumbnail",command=thdlrz)
    viewbtn.place(x=730,y=188)

def run_command2(cmd):
    global line,name2x,ext11,ext12fx
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading update...]")
        statusbar = tk.Label(root, text=line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    root.title("YouTube-dl GUI")
    ext11.destroy()
    ext12fx.destroy()
    messagebox.showinfo("YouTube-dl GUI","YouTube-dl \nUpdate completed!")

def run_command(cmd):
    btn['state'] = DISABLED
    global line,name2x,pro,ext11,ext12fx
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading...]")
        statusbar = tk.Label(root, text=line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
        if "[Metadata]" in str(line):
            ext12fx.destroy()
            ext11.destroy()
            statusbar = tk.Label(root, text="Download Complete                                                                                                                                                                                                          ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
            messagebox.showinfo("YouTube-dl GUI",(result1)+"\nDownload completed!")
            break
        if str(line)=="":
            break
    btn['state'] = NORMAL
    p.stdout.close()
    p.wait()
    root.title("YouTube-dl GUI")

def run_command3(cmd):
    btn['state'] = DISABLED
    global line,name2x,pro,ext11,ext12fx
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading...]")
        statusbar = tk.Label(root, text=line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
        if str(line)=="":
            break
    btn['state'] = NORMAL
    p.stdout.close()
    p.wait()
    root.title("YouTube-dl GUI")
    ext12fx.destroy()
    ext11.destroy()
    statusbar = tk.Label(root, text="Download Complete                                                                                                                                                                                                          ",font=('Arial', 10), bd=1,width=1000, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
    try:
        messagebox.showinfo("YouTube-dl GUI",(result1)+"\nDownload completed!")
    except:
        pass
    
    
def run_command4(cmd):
    btn['state'] = DISABLED
    global line,name2x,pro,ext11,ext12fx
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("YouTube-dl GUI  [Downloading...]")
        statusbar = tk.Label(root, text=line[0:-1]+"                                                                                                                                                                                                           ",font=('Arial', 10), bd=1,width=1000, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
        if str(line)=="":
            break
    btn['state'] = NORMAL
    p.stdout.close()
    p.wait()
    statusbar = tk.Label(root, text="Download Complete                                                                                                                                                                                                          ",font=('Arial', 10), bd=1,width=1000, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
    ext11.destroy()
    ext12fx.destroy()
    root.title("YouTube-dl GUI")
    messagebox.showinfo("YouTube-dl GUI",(result1)+"\nDownload completed!")

def clr():
    e1.delete(0,END)

def clr2():
    e3.delete(0,END)

def on_change(e1):
    text_box.place(x=0,y=450)
    global url,nameloading,statusbar
    try:
        url=e1.widget.get()
    except:
        url=e1.get()
    
    nd1=Label(root, text="                        ").place(x=30,y=290)
    nd2=Label(root, text="                        ").place(x=30,y=170)
    nd3=Label(root, text="                        ").place(x=30,y=230)
    nd4=Label(root, text="                        ").place(x=20,y=200)
    nd5=Label(root, text="                        ").place(x=20,y=230)
    nd5=Label(root, text="                                         ").place(x=340,y=290)
    clr2()
    try:
        btn.destroy()
        text_box.delete(1.0,"end")
        viewbtn.destroy()
    except:
        pass
    
    try:
        cmb.destroy()
        cmb2.destroy()
        cmb3.destroy()
        cmb4.destroy()
        picbtn.destroy()
        ext11.destroy()
        ext12fx.destroy()
    except:
        pass
    
    if url=="":
        messagebox.showerror("YouTube-dl GUI","  Enter Valid URL  ")
    else:
        t1w = threading.Thread(target=title, args=(url,))
        t1w.start()
        t2 = threading.Thread(target=captn, args=(url,))
        t2.start()
        statusbar = tk.Label(root, text=" [Loading...]                                                                                                                                                                                                          ",font=('Arial', 10),width=1000, bd=1, relief=tk.SUNKEN, anchor=tk.W).place(x=0,y=400)
        tv1 = threading.Thread(target=srch, args=(url,))
        tv1.start()
        tv2 = threading.Thread(target=thumbnail, args=(url,))
        tv2.start()

e1 = ttk.Entry(root,width=70)
e1.place(x=120,y=55)
e1.bind("<Return>", on_change)

e2 = ttk.Entry(root,width=70)
e2.place(x=120,y=110)
e2.insert(0, userloc )

e3 = ttk.Entry(root,width=70)
e3.place(x=120,y=135)

def checkcmbo():
    global ext12fx,ext11,statusbar,customname
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
    global vid,aud,codec1,codec2

    vid=""
    aud=""
    codec1=""
    codec2=""
    st=(cmb.get())
    ad=(cmb2.get())
    rs=cmb3.get()
    ms=cmb4.get()
    customname=e3.get()
    if ad=="no separate audio streams available audio included in video stream":
        ad=""
    if rs=="no captions available":
        rs=""
    
    ext12fx=ttk.Button(root,text="Pause",command=pause)
    ext12fx.place(x=650,y=360)
    ext11=ttk.Button(root,text="Cancel",command=cmder)
    ext11.place(x=840,y=360)
    if ad=="" and rs=="" and st!="":
        vid_1=st.split()
        vid=(vid_1[0])
        codec1=vid_1[1]
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -f "{}" -o "{}" '+url).format(vid,"~"+loc+"/"+"%(title)s.%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("1 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -f "{}" -o "{}" '+url).format(vid,"~"+loc+"/"+customname+".%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("1 2")
            return
        
    if st=="" and ad=="" and ms=="":
        try:
            ext12fx.destroy()
            ext11.destroy()
        except:
            pass
        messagebox.showerror("yt-dlp_x86 GUI","Select audio/video stream")
    elif "mp3_low" in ms:
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -x --audio-format mp3 --audio-quality 64K -o "{}" '+url).format("~"+loc+"/"+"%(title)s.%(ext)s")
            t1 = threading.Thread(target=run_command3, args=(a,))
            t1.start()
            #print("5 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -x --audio-format mp3 --audio-quality 64K -o "{}" '+url).format("~"+loc+"/"+customname+".%(ext)s")
            t1 = threading.Thread(target=run_command3, args=(a,))
            t1.start()
            #print("5 2")
            return

    elif "mp3_high" in ms:
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format mp3 --audio-quality 320K --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
            t1 = threading.Thread(target=run_command3, args=(a,))
            t1.start()
            #print("6 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+customname+".%(ext)s"+' -x '+url+' --audio-format mp3 --audio-quality 320K --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
            t1 = threading.Thread(target=run_command3, args=(a,))
            t1.start()
            #print("6 2")
            return

    elif "m4a_high" in ms:
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format m4a --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("7 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+customname+".%(ext)s"+' -x '+url+' --audio-format m4a --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata --embed-thumbnail')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("7 2")
            return
        
    elif "wav music only_music" in ms:
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format wav --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("8 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+customname+".%(ext)s"+' -x '+url+' --audio-format wav --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("8 2")
            return
    elif "flac music studio_quality_music 24 bit audio" in ms:
        if len(customname)==0:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+"%(title)s.%(ext)s"+' -x '+url+' --audio-format flac --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("9 1")
            return
        else:
            a=('yt-dlp_x86 --no-mtime -o ' +"~"+loc+"/"+customname+".%(ext)s"+' -x '+url+' --audio-format flac --metadata-from-title "%(album_artist)s - %(title)s" --add-metadata')
            p2 = threading.Thread(target=run_command3 ,args=(a, ))
            p2.start()
            #print("9 2")
            return

    elif st=="" and ad!="":
        if len(customname)==0:
            aud_1=ad.split()
            aud=(aud_1[0])
            codec1=vid_1[1]
            a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}" -o "{}" '+url).format(aud,"~"+loc+"/"+"%(title)s.%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("2 1")
            return
        else:
            aud_1=ad.split()
            aud=(aud_1[0])
            codec1=vid_1[1]
            a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}" -o "{}" '+url).format(aud,"~"+loc+"/"+customname+".%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("2 2")
            return
        
    elif st!="" and ad!="" and rs=="" and "music" not in ms:
        if len(customname)==0:
            vid_1=st.split()
            vid=(vid_1[0])
            codec1=vid_1[1]
            aud_1=ad.split()
            aud=(aud_1[0])
            vidf=vid_1[1]
            audf=aud_1[1]
            codec2=audf
            if audf==vidf:
                a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}"+"{}" -o "{}" '+url).format(vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
            else:
                a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("3 1")
            return
        else:
            vid_1=st.split()
            vid=(vid_1[0])
            codec1=vid_1[1]
            aud_1=ad.split()
            aud=(aud_1[0])
            vidf=vid_1[1]
            audf=aud_1[1]
            codec2=audf
            if audf==vidf:
                a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}"+"{}" -o "{}" '+url).format(vid,aud,"~"+loc+"/"+customname+".%(ext)s")
            else:
                a=('yt-dlp_x86 --no-mtime --no-restrict-filenames --embed-metadata -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(vid,aud,"~"+loc+"/"+customname+".%(ext)s")
            t1 = threading.Thread(target=run_command, args=(a,))
            t1.start()
            #print("3 2")
            return

    elif st!="" and ad!="" and rs!="":
        if len(customname)==0:
            vid_1=st.split()
            vid=(vid_1[0])
            vidf=vid_1[1]
            codec1=vid_1[1]
            aud_1=ad.split()
            aud=(aud_1[0])
            audf=aud_1[1]
            codec2=audf
            cap=rs.split()
            cap=cap[0]
            if audf==vidf:
                a=('yt-dlp_x86 --write-srt --no-mtime --sub-lang {} --embed-subs --no-restrict-filenames --embed-metadata -f "{}"+"{}" -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
            else:
                a=('yt-dlp_x86 --write-srt --no-mtime --sub-lang {} --embed-subs --no-restrict-filenames --embed-metadata -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+"%(title)s.%(ext)s")
            t1 = threading.Thread(target=run_command4, args=(a,))
            t1.start()
            #print("4 1")
            return
        else:
            vid_1=st.split()
            vid=(vid_1[0])
            vidf=vid_1[1]
            codec1=vid_1[1]
            aud_1=ad.split()
            aud=(aud_1[0])
            audf=aud_1[1]
            codec2=audf
            cap=rs.split()
            cap=cap[0]
            if audf==vidf:
                a=('yt-dlp_x86 --no-mtime --write-srt --sub-lang {} --embed-subs --no-restrict-filenames --embed-metadata -f "{}"+"{}" -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+customname+".%(ext)s")
            else:
                a=('yt-dlp_x86 --no-mtime --write-srt --sub-lang {} --embed-subs --no-restrict-filenames --embed-metadata -f "{}"+"{}" --merge-output-format mp4 -o "{}" '+url).format(cap,vid,aud,"~"+loc+"/"+customname+".%(ext)s")
            t1 = threading.Thread(target=run_command4, args=(a,))
            t1.start()
            #print("4 2")
            return
    
    else:
        messagebox.showerror("YouTube-dl GUI","Select stream")


    audlst=[]
    vidlst=[]
    subs=[]
    music=[]

name7 = Label(root, text = "About",fg="blue",cursor="hand2")
name7.place(x = 30,y = 360)
name7.bind("<Button-1>", lambda e: about())

name8 = Label(root, text = "Update",fg="blue",cursor="hand2")
name8.place(x = 90,y = 360)
name8.bind("<Button-1>", lambda e: update())

name9 = Label(root, text = "Terminal",fg="blue",cursor="hand2")
name9.place(x = 160,y = 360)
name9.bind("<Button-1>", lambda e: terminal())

name10 = Label(root, text = "Github",fg="blue",cursor="hand2")
name10.place(x = 235,y = 360)
name10.bind("<Button-1>", lambda e: repo('https://github.com/sourabhkv/ytdl/'))

name11 = Label(root, text = "Supported  Websites",fg="blue",cursor="hand2")
name11.place(x = 300,y = 360)
name11.bind("<Button-1>", lambda e: repo('http://ytdl-org.github.io/youtube-dl/supportedsites.html'))

name7 = Label(root, text = "Options",fg="blue",cursor="hand2")
name7.place(x = 445,y = 360)
name7.bind("<Button-1>", lambda e: reco())

image = Image.open("logo.png")
resize_image = image.resize((25, 25))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.place(x=565,y=10)
browse_B = ttk.Button(root, text="Browse", command=browse)
browse_B.place(x=560,y=110)
ext15=ttk.Button(root,text="Paste",command=paste)
ext15.place(x=250,y=80)
ext16=ttk.Button(root,text="Clear",command=clr)
ext16.place(x=330,y=80)
ext17=ttk.Button(root,text="GO",command=lambda: on_change(e1))
ext17.place(x=560,y=53)
root.iconbitmap(r'logo.ico')
root.title('YouTube-dl GUI')
root.mainloop()
