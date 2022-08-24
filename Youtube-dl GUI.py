import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
import os
from yt_dlp import YoutubeDL
import subprocess,threading
import tkinter.font as tkFont
import json, urllib
import urllib.request
import requests,datetime
from datetime import datetime

def check_for_update(a):
    rs=open(os.getcwd()+"\\database\\log.txt","r")
    if float(time.time())-float(rs.readlines()[0])>=86400*2:
        r = requests.get(a)
        if r.status_code == 200:
            f=open("version.txt","r")
            curver=int(f.readlines()[0])
            f.close()
            result=r.text
            s=0
            d=""
            f=result.split("\n")
            for i in range(30,len(f)):
                if "Version in support" in f[i]:
                    s=i
            for j in range(0,len(f[s])):
                if f[s][j].isnumeric() or f[s][j]==",":
                    d=d+f[s][j]
            supported=d.split(",")
            version=[]
            for k in range(0,len(supported)):
                version.append(int(supported[k]))
            print(version)
            rs.close()
            rs=open(os.getcwd()+"\\database\\log.txt","w")
            rs.write(str(time.time()))
            rs.close()
            if curver==version[-2]:
                res=messagebox.askquestion("Youtube-dl GUI","Updates available! \nCurrent : "+str(curver)[0:2]+"."+str(curver)[2:7]+"."+str(curver)[6:]+"\nLatest    : "+str(version[-1])[0:2]+"."+str(version[-1])[2:7]+"."+str(version[-1])[6:]+"\n\nDownload update?")
                if res=="yes":
                    os.startfile("updater.exe")
            elif curver==version[-3]:
                res=messagebox.askquestion("Youtube-dl GUI","Updates available! \nCurrent : "+str(curver)[0:2]+"."+str(curver)[2:7]+"."+str(curver)[6:]+"\nLatest    : "+str(version[-1])[0:2]+"."+str(version[-1])[2:7]+"."+str(version[-1])[6:]+"\n\nUpdate now otherwise this version will not get updates in future\n\nDownload update?")
                if res=="yes":
                    os.startfile("updater.exe")
            elif curver==version[-1]:
                messagebox.showinfo("Youtube-dl GUI","Up to date")
            elif curver not in version:
                messagebox.showwarning("Youtube-dl GUI","This version is not supported\nVisit : https://github.com/sourabhkv/ytdl#installation")
    else:
        rs.close()

if  os.path.exists(os.getcwd()+"\\database\\):
    pass
else:
    os.makedirs(os.getcwd()+"\\database", exist_ok=False)
    file = open(os.getcwd()+"\\database\\loc.txt",'w+')
    file.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
    file.close()
    file2=open(os.getcwd()+"\\database\\cookies.txt",'w+')
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'w+')
    file3.close()
    file4=open(os.getcwd()+"\\database\\history.txt",'w+')
    file4.close()
    file5=open(os.getcwd()+"\\database\\log.txt",'w+')
    file5.write(str(time.time()))
    file5.close()

t1xz = threading.Thread(target=check_for_update, args=("https://github.com/sourabhkv/ytdl/releases/latest",))
t1xz.start()
    
def popens(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    return process.stdout.read()


def kill(cmd):
    t1s = threading.Thread(target=popens, args=(cmd,))
    t1s.start()
    namewa.destroy()

def browse():
    global download_Directory,ext12fx,ext11
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    if download_Directory=="":
        file = open(os.getcwd()+"\\database\\loc.txt",'r')
        download_Directory=file.readlines()[0]
        file.close()
    e2.delete(0,END)
    e2.insert(0,download_Directory)
    file = open(os.getcwd()+"\\database\\loc.txt",'w+')
    file.write(download_Directory)
    file.close()

def Resume():
    global ext12fx,ext11,btn
    ext12fx=Button(text="Pause",command=pause,image=img10)
    checkcmbo()

def pause():
    global ext12fx,ext11,btn
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM yt-dlp_x86.exe"
    ps.append("paused")
    st=popens(a)
    sts=popens(b)
    #btn['state'] = DISABLED
    ext12fx.configure(command=Resume,image=img11,text="resume")
    #ext12fx.place(x=650,y=502)
    messagebox.showinfo("Youtube-dl GUI","Download Paused")

def cmder(ext11,ext12fx):
    ext11.destroy()
    ext12fx.destroy()
    t1 = threading.Thread(target=cmderx)
    t1.start()

def cmderx():
    global btn
    a="taskkill /F /IM ffmpeg.exe"
    b="taskkill /F /IM yt-dlp_x86.exe"
    ps.append('cancelled')
    st=popens(a)
    sts=popens(b)
    btn['state'] = NORMAL
    title=result1.replace("|","_")#title org
    loc=e2.get()

    basicdata=cmbbsc.get()
    advvid=cmb.get()
    advaud=cmb2.get()
    customname=e3.get()
    if basicdata=="":
        codec1=advvid.split()[1]
        codec2=advaud.split()[1]
        vid=advvid.split()[0]
        aud=advaud.split()[0]

            
        if customname!="":
            title=customname
            
        if os.path.exists(loc+"/"+title+".f"+vid+"."+codec1+".part"):
            os.remove(loc+"/"+title+".f"+vid+"."+codec1+".part")
            #print("removed")
        if os.path.exists(loc+"/"+title+".f"+aud+"."+codec2+".part"):
            os.remove(loc+"/"+title+".f"+aud+"."+codec2+".part")
            #print("removed2")

        messagebox.showinfo("Youtube-dl GUI","Download Cancelled")
        
    elif basicdata!="":
        if customname!="":
            title=customname
        #print(loc+"/"+title+".mp4.part")
        if os.path.exists(loc+"/"+title+".mp4.part"):
            os.remove(loc+"/"+title+".mp4.part")
            #print("removed")
        messagebox.showinfo("Youtube-dl GUI","Download Cancelled")


def link(url):
    import webbrowser
    webbrowser.open(url)

def terminal():
    t1s = threading.Thread(target=popens, args=("start.bat",))
    t1s.start()

def remove_emoji(string):
    import re
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def title(url):
    global result1,length

    if "youtube" in url or "youtu.be" in url:
        '''from pytube import YouTube
        yt=YouTube(url)
        lengthx=yt.length
        lengthx=str(datetime.timedelta(seconds = lengthx))
        result1=yt.title
        channel=yt.author
        desc=yt.description
        pbdate=yt.publish_date.date()
        views=yt.views'''
        try:
            lengthx=info['duration_string']
        except:
            lengthx=""
        desc=info['description']
        result1=info['title']
        channel=info['uploader']
        views=info['view_count']
        categories=str(info['categories'][0])
        pbdate=str(info['upload_date'])
        pbdate=pbdate[0:4]+"-"+pbdate[4:6]+"-"+pbdate[6:]
        
        try:
            data=str(result1)+"\n"+"\nDuration: "+str(lengthx)+" | Channel: "+str(channel)+"\n\nPublished on: "+str(pbdate)+" | Views : "+str(views)+"\n\nCategory : "+categories+"\n\nDescription \n"+str(desc)+"\n\nThumbnail \n"+str(info['thumbnail'])
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)
            text_box.configure(state='disabled')
        except:
            #print("emoji")
            data=str(result1)+"\n"+"\nDuration: "+str(lengthx)+" | Channel: "+str(channel)+"\n\nUploaded on: "+str(pbdate)+" | Views : "+str(views)+"\n\nCategory : "+categories+"\n\nDescription \n"+"\n\nDescription \n"+str(desc)+"\n\nThumbnail \n"+str(info['thumbnail'])
            
            data=remove_emoji(data)
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)
            text_box.configure(state='disabled')
        

    else:
        try:
            lengthx=info['duration_string']
        except:
            lengthx=""
        try:
            desc=info['description']
        except:
            pass
        result1=info['title']
        try:
            data=str(result1)+"\n"+"\nDuration: "+lengthx+"\n"+"\nDescription \n"+str(desc)
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)
            text_box.configure(state='disabled')
        except:
            #print("emoji")
            data=str(result1)+"\n"+"\nDuration: "+lengthx
            
            data=remove_emoji(data)
            text_box.delete(1.0,"end")
            text_box.insert(1.0, data)
            text_box.configure(state='disabled')

def pltitle(url):
    from pytube import Playlist
    global items
    p = Playlist(url)
    a=p.video_urls
    try:
        views=p.views
    except:
        views="NA"
    title=p.title
    try:
        desc=p.description
    except:
        desc=""
    try:
        data=str(title)+"\n"+"\nTotal no. of videos : "+str(p.length)+"\nViews : "+str(views)+"\n"+"\n\nDescription "+"\n"+str(desc)
        text_box.delete(1.0,"end")
        text_box.insert(1.0, data)
        text_box.configure(state='disabled')
        items.insert(0,'1-'+str(p.length))
        items.place(x=170,y=95)
    except:
            #print("emoji")
        data=str(title)+"\n"+"\nTotal no. of videos : "+str(p.length)+"\nViews : "+str(views)+"\n"+"\n\nDescription "+"\n"+str(desc)
            
        data=remove_emoji(data)
        text_box.delete(1.0,"end")
        text_box.insert(1.0, data)
        text_box.configure(state='disabled')
        items.insert(0,'1-'+str(p.length))
        items.place(x=170,y=95)
    from io import BytesIO
    import requests
    global image2,vid,thurl,picbtn
    if "youtube" in url and "music" not in url:
        if "youtube" in a[0]:
            d=a[0].find("=")
            vid=a[0][d+1:]
        elif "youtu.be" in a[0]:
            vid=a[0][a[0].rfind("/")+1:]
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((270, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        panel = Label(root, image=image2)
        picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=710,y=40)
        status.set("")

    elif "music" in url and "youtube" in url:
        global full
        full=p.sidebar_info
        thurl=full[0]['playlistSidebarPrimaryInfoRenderer']['thumbnailRenderer']['playlistCustomThumbnailRenderer']['thumbnail']['thumbnails'][0]['url']
        print(thurl)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((160, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        panel = Label(root, image=image2)
        picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=710+55,y=40)
        status.set("")

def about():
    root2 = tk.Toplevel()
    root2.focus_force()
    y=int((sh-400)/2)
    x=int((sw-600)/2)
    root2.geometry('%dx%d+%d+%d' % (600, 400, x, y))
    root2.title('About Youtube-dl GUI')
    root2.configure(bg='#303135')
    image = Image.open("logo.png")
    resize_image = image.resize((200, 200))
    img = ImageTk.PhotoImage(resize_image)
    streams = tk.Label(master=root2, text = "",image=img,bg="#303135",font=('Arial', 16),fg="white").place(relx=0.5, rely=0.25,anchor= CENTER)
    streams2 = Label(root2, text = "Youtube-dl GUI  v22.0808.19",bg="#303135",font=('Arial', 11),fg="white").place(relx=.5, rely=.5,anchor= CENTER)
    streams2 = Label(root2, text = "Released under MIT License",bg="#303135",fg="white").place(relx=.5, rely=.56,anchor= CENTER)
    streams2 = Label(root2, text = "This is project is based on yt-dlp , ffmpeg , atomic parsley",bg="#303135",fg="white").place(relx=.5, rely=.62,anchor= CENTER)
    streams3 = Label(root2, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 9,'bold'),fg="red",bg="#303135").place(relx=.5, rely=.69,anchor= CENTER)
    name74 = Label(root2, text = "CREDITS :",bg="#303135",fg="white").place(x=40+65,y=290)
    name74 = Label(root2, text = "yt-dlp",bg="#303135",fg="#0574FF",cursor="hand2")
    name74.place(x = 135+85,y = 290)
    name74.bind("<Button-1>", lambda e: link('https://github.com/yt-dlp/yt-dlp'))
    name73 = Label(root2, text = "ffmpeg",fg="#0574FF",cursor="hand2",bg="#303135")
    name73.place(x = 210+95,y = 290)
    name73.bind("<Button-1>", lambda e: link('https://www.ffmpeg.org/'))
    name75 = Label(root2, text = "AtomicParsley",fg="#0574FF",cursor="hand2",bg="#303135")
    name75.place(x = 290+105,y = 290)
    name75.bind("<Button-1>", lambda e: link('http://atomicparsley.sourceforge.net/'))
    name7e = Label(root2, text = "Changelog",fg="#0574FF",cursor="hand2",bg="#303135")
    name7e.bind("<Button-1>", lambda e: link('https://github.com/sourabhkv/ytdl/releases/tag/v22.0808.19'))
    name7e.place(x = 195,y = 315)
    name8e = Label(root2, text = "Check for updates",fg="#0574FF",cursor="hand2",bg="#303135")
    name8e.bind("<Button-1>", lambda e: os.startfile("updater.exe"))
    name8e.place(x = 295,y = 315)
    streams2 = Label(root2, text = "https://github.com/sourabhkv/ytdl",bg="#303135",fg="white").place(relx=.5, rely=.87,anchor= CENTER)
    streams2 = Label(root2, text = "Developed by sourabhkv",bg="#303135",fg="green").place(relx=.5, rely=.93,anchor= CENTER)
    root2.resizable(False, False)
    root2.iconbitmap(r'logo.ico')
    root2.mainloop()

def updateback():
    t1 = threading.Thread(target=run_command2, args=("yt-dlp_x86 -U",))
    t1.start()

def cookieselect():
    r = filedialog.askopenfilename()
    cookiepath.delete(0,END)
    cookiepath.insert(0,r)
    root3.focus_force()
    
def save():
    c1=optnentry.get()
    c2=cookiepath.get()
    file2=open(os.getcwd()+"\\database\\cookies.txt",'w+')
    file2.write(c2)
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'w+')
    file3.write(c1)
    file3.close()
    root3.destroy()
    messagebox.showinfo("Youtube-dl GUI", "Settings saved!")
    
def reco():
    global root3
    root3 = tk.Tk()
    root3.configure(bg='#303135')
    root3.focus_force()
    y=int((sh-500)/2)-30
    x=int((sw-500)/2)
    root3.geometry('%dx%d+%d+%d' % (500, 500, x, y))
    root3.title('Youtube-dl GUI')
    Label(root3, text = "Settings",font=('Arial', 16),bg="#303135",fg="white").place(x = 210,y = 10)
    Label(root3, text = "Default Download Options",bg="#303135",fg="white").place(x = 175,y = 50)
    dd=Label(root3, text = "Update backend",fg="#0574FF",cursor="hand2",bg="#303135")
    dd.place(x = 390,y = 355)
    dd.bind("<Button-1>", lambda e: updateback())
    ttk.Button(root3, text ="Save", command = save).place(x=215,y=256)
    global cookiepath,optnentry
    file2=open(os.getcwd()+"\\database\\cookies.txt",'r')
    data1=file2.readlines()
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'r')
    data2=file3.readlines()
    file3.close()
    optnentry=ttk.Entry(root3,width=74)
    cookiepath=ttk.Entry(root3,width=71)
    if len(data2)!=0:
        optnentry.insert(0,data2[0])
    elif len(data1)!=0:
        cookiepath.insert(0,data1[0])
    optnentry.place(x=20,y=78)
    #cookiepath.insert(0,data3)
    cookiepath.place(x=20,y=158)
    Button(root3, text =".", command = cookieselect).place(x=455,y=156)
    Label(root3, text = "Path to Cookie file",bg="#303135",fg="white").place(x = 195,y = 130)
    name75 = Label(root3, text = "Report issue",fg="#0574FF",cursor="hand2",bg="#303135")
    name75.place(x = 15,y = 355)
    name75.bind("<Button-1>", lambda e: link('https://github.com/sourabhkv/ytdl/issues'))
    root3.resizable(False, False)
    root3.iconbitmap(r'logo.ico')
    root3.mainloop()

def viewer(img):
    t1w = threading.Thread(target=viewers, args=(img,))
    t1w.start()

def viewers(img):
    img.show()

def thumbnail(url):
    from io import BytesIO
    import requests
    global image2,vid,thurl,picbtn
    if "youtube" in url and "music" not in url and "shorts" not in url or "youtu.be" in url and "music" not in url and "shorts" not in url:
        if "youtube" in url:
            d=url.find("=")
            vid=url[d+1:]
        elif "youtu.be" in url:
            vid=url[url.rfind("/")+1:]
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((270, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        panel = Label(root, image=image2)
        picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=710,y=40)
        dwth()
    elif "youtube" in url and "music" in url:
        if url.find("&")==-1:
            vid=url[1+url.find("="):]
        else:
            vid=url[1+url.find("="):url.find("&")]
        #print(vid)
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((270, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)#https://www.youtube.com/shorts/WSFe3Rp7arQ
        panel = Label(root, image=image2)
        picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=710,y=40)
        dwth()
    elif "youtube" in url and "shorts" in url:
        #print("ghfghgfhf")
        vid=url.rstrip("?feature=share")[url.rstrip("?feature=share").rfind("/")+1:]
        #print(vid)
        #print(vid,url)
        thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
        r = requests.get(thurl)
        img = Image.open(BytesIO(r.content))
        img.mode = 'RGB'
        image = img.resize((270, 160), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)#https://www.youtube.com/shorts/WSFe3Rp7arQ
        panel = Label(root, image=image2)
        picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
        picbtn.place(x=710,y=40)
        dwth()
    else:
        if 'thumbnail' in info:
            thurl=info['thumbnail']
        try:
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            width, height = img.size
            i=2
            while (i)>0:
                if (i*height)<=165 and (i*width)<=270:
                    break
                else:
                    i=i-0.02
            nw=int(i*width)
            nh=int(i*height)
            sp=int((230-nw)/2)
            #print(nw,nh)
            image = img.resize(((nw),(nh)), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(root, image=image2)
            picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            picbtn.place(x=sp+730,y=40)
            dwth()
        except:
            na= StringVar()
            na.set("Thumbnail not available")
            name = Label(root, textvariable = na,bg="#525252",fg="white").place(x = 780,y = 70)

def dwth():
    global viewbtn
    viewbtn=Button(root,text="Download thumbnail",image=img13,bd=0,command=thdlrz,activebackground="#202020",highlightthickness = 0)
    viewbtn.bind('<Enter>',lambda a:changer_red(viewbtn,imgthred))
    viewbtn.bind('<Leave>',lambda a:changer_blue(viewbtn,img13))
    viewbtn.place(x=765,y=229)

def thdlrz():
    tv2 = threading.Thread(target=thdlr)
    tv2.start()

def thdlr():
    global customname
    customname=e3.get()
    try:
        loc=download_Directory
    except:
        loc=userloc
    loc=loc.replace("\\","/")
    #print(loc)

    print(loc)
    
    if "youtube" in url or "youtu.be" in url:
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
                response.close()
                messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
            elif response.status_code != 200:
                url2 = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
                response = requests.get(url2)
                with open(filename, 'wb') as f:
                    f.write(response.content)
                response.close()
                messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
        else:
            url2 = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(vid)
            filename=loc+"/"+customname+".jpg"
            response = requests.get(url2)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                response.close()
                messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
            elif response.status_code != 200:
                url2 = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
                response = requests.get(url2)
                with open(filename, 'wb') as f:
                    f.write(response.content)
                response.close()
                messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
    else:
        if len(customname)==0:
            propername=""
            for i in result1:
                if i.isalpha() or i.isspace() or i.isnumeric():
                    propername=propername+i
            filename=loc+"/"+propername+"_Thumbnail"+".jpg"
            response = requests.get(thurl)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            response.close()
            messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
        else:
            filename=loc+"/"+customname+".jpg"
            response = requests.get(thurl)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            response.close()
            messagebox.showinfo("Youtube-dl GUI",(filename)+" \nDownload completed!")
    print(filename)


def clearentry():
    d=cmb.get()
    f=cmb2.get()
    r=cmb3.get()
    if "no captions available" not in r:
        cmb3.set("")
    if "Audio combined in video streams" not in f and 'Audio not available' not in f:
        cmb2.set("")
    if "Video not available" not in d:
        cmb.set("")
    if ftbox.get()!="auto-detect":
        ftbox.current(0)
    e3.delete(0, END)
    e4.delete(0, END)
    ratelim.delete(0, END)
    c6.set(False)
    

def bas():
    try:
        d=cmbbsc.get()
        if d=="Check Advanced option":
            cmbbsc.set("Check Advanced option")
        else:
            cmbbsc.set("")
            cmbmus.set('')
    except:
        pass

def captn(url):
    global cmb3,tab1clr,tab2clr,tb2cap
    subs=[]
    if 'subtitles' in info:
        try:
            for i in info['subtitles']:
                subs.append(str(i)+"   "+str(info['subtitles'][i][0]['name']))
        except:
            pass

    if len(subs)==0:
        subs.append("no captions available")
        cmb3 = ttk.Combobox(tab2, width="37", values=subs,state="readonly")
        cmb3.place(x=15,y=122)
        cmb3.current(0)
    else:
        cmb3 = ttk.Combobox(tab2, width="37", values=subs,state="readonly")
        cmb3.place(x=15,y=122)

    tb2cap.set("Captions")
        
    
    tab2clr = Label(tab2, text = "Clear selection",fg="#0090FF",cursor="hand2",bg="#525252")
    tab2clr.place(x = 515,y = 200)
    tab2clr.bind("<Button-1>", lambda g: clearentry())

    tab1clr = Label(tab1, text = "Clear selection",fg="#0090FF",cursor="hand2",bg="#525252")
    tab1clr.place(x = 515,y = 200)
    tab1clr.bind("<Button-1>", lambda g: bas())
    #print(music,len(music))
    
def size(n):
    if n//1024**2>=1 and n//1024**2<1024:
        a=str(round((n/1024**2),2))+" MiB"
        return a
    elif n>=1024**3:
        a=str((round((n/1024**3),2)))+" GiB"
        return a
    elif n//1024>=1 and n//1024<1024:
        a=str(round(n/1024,2))+" KiB"
        return a


def isChecked():
    global cmbmus,cmbbsc,cb
    if cb.get() == 1:
        if cmbbsc.get()!="Check Advanced option":
            cmbbsc.set("")
        cmbbsc['state']=DISABLED
        cmbmus['state']=NORMAL
        cmbmus.focus_force()
        cmbmus.config(state="readonly")
    elif cb.get()==0:
        cmbmus.set("")
        cmbmus['state']=DISABLED
        cmbbsc['state']=NORMAL
        cmbbsc.focus_force()
        cmbbsc.config(state="readonly")
    #print(cb.get())

def srch(url):
    global cmbbsc,cmb,cmb2,cmbmus,btn,audlst,vidlst,music,basic,check,cusvar
    ydl_opts = {}
    global info
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        #print(info)
        d=""
        tv2z = threading.Thread(target=title, args=(url,))
        tv2z.start()
        if "youtube" not in url and "youtu.be" not in url:
            tv2 = threading.Thread(target=thumbnail, args=(url,))
            tv2.start()
        for i in range(0,len(info['formats'])):
            #a=info['formats'][i]
            try:
                del info['formats'][i]['url']
            except:
                pass
            try:
                del info['formats'][i]['preferencefragments']
            except:
                pass
            try:
                del info['formats'][i]['http_headers']
            except:
                pass
            try:
                del info['formats'][i]['source_preference']
            except:
                pass
            try:
                del info['formats'][i]['downloader_options']
            except:
                pass
            try:
                del info['formats'][i]['fragments']
            except:
                pass
            try:
                del info['formats'][i]['language']
                del info['formats'][i]['language_preference']
            except:
                pass
            try:
                info['formats'][i]['filesize']=size(info['formats'][i]['filesize'])
                del info['formats'][i]['preference']
            except:
                pass
            try:
                del info['formats'][i]['format']
                del info['formats'][i]['height']
                del info['formats'][i]['width']
            except:
                pass
            try:
                #del info['formats'][i]['protocol']
                del info['formats'][i]['quality']
            except:
                pass
            try:
                del info['formats'][i]['manifest_url']
                del info['formats'][i]['fragment_base_url']
            except:
                pass
            try:
                del info['formats'][i]['manifest_stream_number']
            except:
                pass
            b=info['formats'][i]
            #print(b)
            st={}
            for i in b:
                if b[i]!=None and b[i]!='none' and b[i]!=False and b[i]!='SDR':
                    st[i]=b[i]
            if "format_id" in st:
                d=d+st['format_id']
            if 'format_note' in st:
                d=d+"  |  "+st['format_note']
            if 'filesize' in st:
                d=d+"  |  Size : "+str(st['filesize'])
            if 'filesize_approx' in st:
                st['filesize_approx']=size(st['filesize_approx'])
                d=d+"  |  Size : "+str(st['filesize_approx'])
            if 'ext' in st:
                d=d+"  | ext: "+st['ext']
            if 'vcodec' in st:
                d=d+"  |  "+st['vcodec']
            if 'acodec' in st:
                d=d+"  |  "+st['acodec']
            if 'resolution' in st:
                d=d+"  |  "+st['resolution']
            if 'tbr' in st:
                if st['tbr']>=1024:
                    st['tbr']=str(round(st['tbr']/1024,2))+" Mbps"
                    d=d+"  | Bitrate: "+st['tbr']
                else:
                    d=d+"  | Bitrate: "+str(st['tbr'])+" Kbps"
            if 'fps' in st:
                d=d+" | FPS "+str(st['fps'])
            if 'vcodec' in st and 'acodec' in st:
                d=d+" #"
            d=d+"\n"
        #print(d)'''
        #print(st)
    except:
        d=" "+"\n"+" "
        #print("ero")
    stream = d
    output = stream
    audlst=[]
    vidlst=[]
    music=[]
    basic=[]
    basic2=[]

    a=(output.split("\n"))
    for i in range(0,len(a)):
        if "3gp" in a[i] or "vp9" in a[i] or "video" in a[i] or "fps" in a[i] or "avc1" in a[i]  or "mp4" in a[i] and "mp4a" not in a[i] and "audio" not in a[i]:
            if "mp4a" in a[i]:
                s=a[i]
                basic.append(s)
            if "youtube" not in url and "youtu.be" not in url:
                t=""
                r=str(a[i]).split()
                for s in range(0,len(r)):
                    t=t+"  "+r[s]
                vidlst.append(t)
            elif "youtube" in url or "youtu.be" in url:
                vidlst.append(a[i])

        if "audio" in a[i] or "mp3" in a[i] or "m4a" in a[i]:
            if "youtube" not in url and "youtu.be" not in url:
                t=""
                r=str(a[i]).split()
                for v in range(0,len(r)):
                    t=t+"  "+r[v]
                audlst.append(t)
            elif "youtube" in url or "youtu.be" in url:
                audlst.append(a[i])

    frmt.set('Format')
    global ftbox,ratelim
    rtx.set("Rate limit (eg. 50K or 4.2M )")
    ftbox=ttk.Combobox(tab2, width="20", values=["auto-detect","mp4","mkv","webm"],state="readonly")
    ftbox.current(0)
    ftbox.place(x=327-50,y=122)

    ratelim=ttk.Entry(tab2,width=27)
    ratelim.place(x=437,y=122)
    cusvar.set("Custom Filename")
    global e3,e4,embdth
    e3 = ttk.Entry(tab2,width=47)
    e4 = ttk.Entry(tab2,width=46)
    e3.place(x=17,y=145+24)
    e4.place(x=323,y=145+24)
    prxy.set("Proxy URL")
    embdth=ttk.Checkbutton(tab2,text="Embed thumbnail", var=c6, onvalue=True, offvalue=False)
    embdth.place(x=17,y=145+24+30)
    
                
    t2 = threading.Thread(target=captn, args=(url,))
    t2.start()
    
    #print(basic)
    if "youtube" in url or "youtu.be" in url:
        for i in range(0,len(basic)):
            k=basic[i].split()
            data=k[2]+"     Size  :  "+k[6]+" "+k[7]+"   |    format  : "+k[10]+"    |    FPS:   "+k[-2]+"    |    Resolution  :    "+k[16]+"    |   id   "+k[0]
            basic2.append(data)
        if len(basic2)!=0:
            basic2.append("Best available")
            cmbbsc = ttk.Combobox(tab1, width="90", values=basic2,state="readonly")
            cmbbsc.place(x=20,y=47)
        elif len(basic2)==0 and len(vidlst)!=0 or len(basic2)==0 and len(audlst)!=0:
            basic2.append("Check Advanced option")
            cmbbsc = ttk.Combobox(tab1, width="90", values=basic2,state="readonly")
            cmbbsc.set(basic2[0])
            cmbbsc.place(x=20,y=47)
        
    if "youtube" not in url and "youtu.be" not in url:
        if len(basic)==0:
            basic.append("Check Advanced option")
            cmbbsc = ttk.Combobox(tab1, width="90", values=basic,state="readonly")
            cmbbsc.set(basic[0])
            cmbbsc.place(x=20,y=47)
        else:
            cmbbsc = ttk.Combobox(tab1, width="90", values=basic,state="readonly")
            cmbbsc.place(x=20,y=47)
    
    global cb
    check=ttk.Checkbutton(tab1, var=cb, onvalue=True, offvalue=False, command=isChecked)
    check.place(x=3,y=85)

    #print(len(vidlst))


    if len(audlst)==0 and len(vidlst)==0:
        status.set(" Website not supported")
        vidlst.append("Video not available")
        cmb = ttk.Combobox(tab2, width="95", values=vidlst,state="readonly")
        cmb.place(x=15,y=32)
        cmb.set(vidlst[0])
        audlst.append("Audio not available")
        cmb2 = ttk.Combobox(tab2, width="95", values=audlst,state="readonly")
        cmb2.place(x=15,y=77)
        cmb2.set(audlst[0])
        tb4select.set("No Music available")
        messagebox.showerror("YouTube-dl GUI","URL not supported or Stream might be DRM protected \nStream might be age-restricted \nTry using VPN \nIf you see this error again with VPN Website is not supported \nSee Supported websites")

    
    if len(audlst)==0 and len(vidlst)!=0:
        audlst.append("Audio combined in video streams")
        cmb2 = ttk.Combobox(tab2, width="95", values=audlst,state="readonly")
        cmb2.set(audlst[0])
        cmb2.place(x=15,y=77)
        tb4select.set("No Music available")
        
    if len(audlst)!=0:
        if audlst[0]!="Audio not available" and audlst[0]!="Audio combined in video streams":
            print("***")
            cmb2 = ttk.Combobox(tab2, width="95", values=audlst,state="readonly")
            cmb2.place(x=15,y=77)
            music=["Mp3 64 kbps","Mp3 128 kbps","Mp3 320 kbps","M4a High","Wav Lossless","Flac 24 bit Lossless"]
            cmbmus= ttk.Combobox(tab1, width="45", values=music,state="readonly")
            cmbmus['state']=DISABLED
            cmbmus.place(x=20,y=110)
            tb4select.set("Convert to music")

    #print(len(audlst))

    if len(vidlst)==0 and len(audlst)!=0:
        vidlst.append("Video not available")
        cmb = ttk.Combobox(tab2, width="95", values=vidlst,state="readonly")
        cmb.current(0)
        cmb.place(x=15,y=32)
        
    if len(vidlst)!=0:
        if vidlst[0]!="Video not available":
            cmb = ttk.Combobox(tab2, width="95", values=vidlst,state="readonly")
            cmb.place(x=15,y=32)

    #print(audlst)
    #print(vidlst)
    
    tb1quality.set("Select  video  quality")
    tb2vid.set("Video  Streams")
    tb2aud.set("Audio  Streams")
    

        
    
    status.set("")

        

    btn = Button(root,image=img9, text="Download",command=checkcmbo,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")
    btn.bind('<Enter>',lambda a:changer_red(btn,imgdwred))
    btn.bind('<Leave>',lambda a:changer_blue(btn,img9))
    btn.place(x=805,y=506)

def history():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    url=e1.get()
    try:
        title=str(result1)
    except:
        if len(e3.get())!=0:
            title=e3.get()
        else:
            title=""
    file4=open(os.getcwd()+"\\database\\history.txt",'a')
    fmt=cmbmus.get()
    location=download_Directory
    log=title+"^"+url+"^"+dt_string+"^"+location+"^"+"\n"
    try:
        file4.write(log)
    except:
        pass
    file4.close()
    
def run_command4(cmd):
    #print(cmd)
    file2=open(os.getcwd()+"\\database\\cookies.txt",'r')
    if len(file2.readlines())!=0:
        cmd=cmd+" --cookies "+file2.readlines()[0]
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'r')
    if len(file3.readlines())!=0:
        cmd=cmd+" "+file3.readlines()[0]

    file3.close()
    global ext11,ext12fx,ext17go
    ext12fx.place(x=690+20,y=506)
    ext11.place(x=885+20,y=506)
    btn['state'] = DISABLED
    ext17go['state']=DISABLED
    root.title("Youtube-dl GUI  [Downloading...]")
    zen=""
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    #print(p.pid)
    for line in iter(p.stdout.readline, b''):
        root.title("Youtube-dl GUI  [Downloading...]")
        status.set(" "+line[0:-1]+"                                                                                                                                                                                                           ")
        if str(line)=="":
            break
        elif str(line)!="":
            zen=line
            
    ext17go['state']=NORMAL
    p.stdout.close()
    p.wait()
    if "\n" in zen:
        status.set(" Download Complete")
        root.title("Youtube-dl GUI")
        history()
        refresh()
        btn['state'] = NORMAL
        #ext17go['state']=NORMAL
        ext12fx.destroy()
        ext11.destroy()
        if e3.get()=="":
            print(result1)
            messagebox.showinfo("Youtube-dl GUI",result1+"\n"+"Download complete")
        elif len(e3.get())!=0:
            messagebox.showinfo("Youtube-dl GUI",+e3.get()+"\n"+"Download complete")
                
            
    elif "\n" not in zen:
        if ps[-1]=='paused':
            status.set(" Download Paused")
            #ext11.destroy()
            #ext12fx.destroy()
        elif ps[-1]=='cancelled':
            status.set(" Download Cancelled")
            btn['state'] = NORMAL
            
    root.title("Youtube-dl GUI")
    #print(ps)
    
def run_command4pl(cmd):
    #print(cmd)
    file2=open(os.getcwd()+"\\database\\cookies.txt",'r')
    if len(file2.readlines())!=0:
        cmd=cmd+" --cookies "+file2.readlines()[0]
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'r')
    if len(file3.readlines())!=0:
        cmd=cmd+" "+file3.readlines()[0]
    file3.close()
    global ext11,ext12fx
    ext12fx.place(x=690+20,y=506)
    ext11.place(x=885+20,y=506)
    progress=""
    btn['state'] = DISABLED
    ext17go['state']=DISABLED
    root.title("Youtube-dl GUI  [Downloading...]")
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        status.set(" "+line[0:-1]+"                                                                                                                                                                                                           ")
        if "Downloading video" in line and "of" in line:
            progress="Youtube-dl GUI  "+line[10:-1]
        root.title(progress)
        if str(line)=="":
            break
    btn['state'] = NORMAL
    ext17go['state']=NORMAL
    p.stdout.close()
    p.wait()
    ext12fx.destroy()
    ext11.destroy()
    status.set(" Download Complete")
    root.title("Youtube-dl GUI")

def run_command4multi(cmd,gg):
    #print(cmd)
    file2=open(os.getcwd()+"\\database\\cookies.txt",'r')
    if len(file2.readlines())!=0:
        cmd=cmd+" --cookies "+file2.readlines()[0]
    file2.close()
    file3=open(os.getcwd()+"\\database\\args.txt",'r')
    if len(file3.readlines())!=0:
        cmd=cmd+" "+file3.readlines()[0]
    file3.close()
    btn['state'] = DISABLED
    ext17go['state']=DISABLED
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        gg.set(" "+line[0:-1]+"                                                                                                                                                                                                           ")
        if str(line)=="":
            break
    btn['state'] = NORMAL
    ext17go['state']=NORMAL
    p.stdout.close()
    p.wait()
    gg.set(" Download Complete")
    root.title("Youtube-dl GUI")


def multibuster(z,b,c):
    print("z",z,"b",b"c",c)
    loc="/"+"Downloads"
    cpt=userloc+"\\Downloads"
    user=(os.environ['USERPROFILE'])
    user=user.replace("\\","/")
    try:
        loc=download_Directory
        if "C:" in loc:
            cd=loc.lstrip(user)#bug removed of multi video
            loc=cd.replace("\\","/")
            loc="/"+loc
    except:
        pass
    if len(b)!=0:
        if "144p" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:144,vext:mp4,aext:m4a -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "240p" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:240,vext:mp4,aext:m4a -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "360p" in b:
            a=("yt-dlp --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:360,vext:mp4,aext:m4a -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "480p" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:480,vext:mp4,aext:m4a -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "720p" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:720,vext:mp4,aext:m4a -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "1080p" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -S height:1080,vext:mp4,aext:m4a "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "best" in b:
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --add-metadata --no-mtime -f bv+ba -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "Mp3 320 kbps" in b:
            a=("yt-dlp --ignore-errors --format bestaudio --audio-quality 0 --extract-audio --add-metadata --embed-thumbnail --audio-format mp3 --no-mtime --audio-quality 320K -o {} --yes-playlist "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "Mp3 64 kbps" in b:
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --add-metadata --audio-format mp3 --no-mtime --audio-quality 64K -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "M4a High" in b:
            a=("yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format m4a --audio-quality 0 -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "Wav Losless" in b:
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --audio-quality 0 --add-metadata --no-mtime --embed-thumbnail --audio-format wav  -o {} "+z).format("~"+loc+"/"+"%(title)s.%(ext)s")


        print(a)

        tv2w = threading.Thread(target=run_command4multi, args=(a,c,))
        tv2w.start()

def buster():
    #print(u)
    h=0
    for i in u:
        if len(i)!=0 and len(u[i][0].get())!=0:
            multibuster(i,u[i][0].get(),u[i][1])
            print(i,u[i][0].get(),u[i][1])
            h=h+1
    if h==0:
        messagebox.showerror("Youtube-dl GUI","Select quality")
    
def lolo(a,b,c,d):
    if b.get()==0:
        c.set("")
        c['state']=DISABLED
    elif b.get()==1:
        c['state']=NORMAL
        c.focus_force()
        c.config(state="readonly")
    #print(a,b)
    
def multi(url_lst):
    global qt1,qt2,qt3,qt4,qt5,url1,url2,url3,url4,url5,check1,check2,check3,check4,check5
    url1=""
    url2=""
    url3=""
    url4=""
    url5=""
    qt1=ttk.Combobox(tab4, width="10", values=playlist,state="readonly")
    qt2=ttk.Combobox(tab4, width="10", values=playlist,state="readonly")
    qt3=ttk.Combobox(tab4, width="10", values=playlist,state="readonly")
    qt4=ttk.Combobox(tab4, width="10", values=playlist,state="readonly")
    qt5=ttk.Combobox(tab4, width="10", values=playlist,state="readonly")
    #check=ttk.Checkbutton(tab1, var=cb, onvalue=True, offvalue=False, command=isChecked)
    url1=url_lst[0]
    try:
        url2=url_lst[1]
        url3=url_lst[2]
        url4=url_lst[3]
        url5=url_lst[4]
    except:
        try:
            url2=url_lst[1]
            url3=url_lst[2]
            url4=url_lst[3]
        except:
            try:
                url2=url_lst[1]
                url3=url_lst[2]
            except:
                try:
                    url2=url_lst[1]
                except:
                    url2=""
    #print(url1,url2,url3,url4,url5)
    #print(len(url1),len(url2),len(url3),len(url4),len(url5))
    from pytube import YouTube
    import time
    data=""

    if len(url1)!=0:
        yt=YouTube(url1)
        title=yt.title
        lengthx=yt.length
        lengthx=str(time.strftime('%H:%M:%S', time.gmtime(lengthx)))
        data="1. "+url1+"\n"+str(title)+"\nDuration : "+lengthx
        if len(title)>25:
            title=title[:23]+".."
        check1=ttk.Checkbutton(tab4,text=title, var=c1, onvalue=True, offvalue=False, command=lambda :lolo(check1,c1,qt1,url1))
        check1.place(x=10,y=10+10)
        qt1.place(x=200,y=10+10)
        qt1['state']=DISABLED
    if len(url2)!=0:
        yt=YouTube(url2)
        title=yt.title
        lengthx=yt.length
        lengthx=str(time.strftime('%H:%M:%S', time.gmtime(lengthx)))
        data=data+"\n\n2. "+url2+"\n"+str(title)+"\nDuration : "+lengthx
        if len(title)>25:
            title=title[:23]+".."
        check2=ttk.Checkbutton(tab4,text=title, var=c2, onvalue=True, offvalue=False, command=lambda :lolo(check2,c2,qt2,url2))
        check2.place(x=10,y=25+16)
        qt2.place(x=200,y=25+16)
        qt2['state']=DISABLED
    if len(url3)!=0:
        yt=YouTube(url3)
        title=yt.title
        lengthx=yt.length
        lengthx=str(time.strftime('%H:%M:%S', time.gmtime(lengthx)))
        data=data+"\n\n3. "+url3+"\n"+str(title)+"\nDuration : "+lengthx
        if len(title)>25:
            title=title[:23]+".."
        check3=ttk.Checkbutton(tab4,text=title, var=c3, onvalue=True, offvalue=False, command=lambda :lolo(check3,c3,qt3,url3))
        check3.place(x=10,y=40+22)
        qt3.place(x=200,y=40+22)
        qt3['state']=DISABLED
    if len(url4)!=0:
        yt=YouTube(url4)
        title=yt.title
        lengthx=yt.length
        lengthx=str(time.strftime('%H:%M:%S', time.gmtime(lengthx)))
        data=data+"\n\n4. "+url4+"\n"+str(title)+"\nDuration : "+lengthx
        if len(title)>25:
            title=title[:23]+".."
        check4=ttk.Checkbutton(tab4,text=title, var=c4, onvalue=True, offvalue=False, command=lambda :lolo(check4,c4,qt4,url4))
        check4.place(x=10,y=55+28)
        qt4.place(x=200,y=55+28)
        qt4['state']=DISABLED
    if len(url5)!=0:
        yt=YouTube(url5)
        title=yt.title
        lengthx=yt.length
        lengthx=str(time.strftime('%H:%M:%S', time.gmtime(lengthx)))
        data=data+"\n\n5. "+url5+"\n"+str(title)+"\nDuration : "+lengthx
        if len(title)>25:
            title=title[:23]+".."
        check5=ttk.Checkbutton(tab4,text=title, var=c5, onvalue=True, offvalue=False, command=lambda :lolo(check5,c5,qt5,url5))
        check5.place(x=10,y=70+34)
        qt5.place(x=200,y=70+34)
        qt5['state']=DISABLED

    try:
        text_box.delete(1.0,"end")
        text_box.insert(1.0, data)
        text_box.configure(state='disabled')
    except:
            #print("emoji")
            
        data=remove_emoji(data)
        text_box.delete(1.0,"end")
        text_box.insert(1.0, data)
        text_box.configure(state='disabled')

    global u,btn
        
    u={url1:[qt1,p1],url2:[qt2,p2],url3:[qt3,p3],url4:[qt4,p4],url5:[qt5,p5]}
    btn = Button(root,image=img9, text="Download",command=buster,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")
    btn.bind('<Enter>',lambda a:changer_red(btn,imgdwred))
    btn.bind('<Leave>',lambda a:changer_blue(btn,img9))
    btn.place(x=800,y=506)
    status.set('')

def clrt5():
    global play,items
    play.set("")
    items.delete(0,END)
    #items.insert(0,"")

def on_change(e1):
    global url,play,btn

    na= StringVar()
    na.set("                                                    ")
    name = Label(root, textvariable = na,bg="#525252").place(x = 760,y = 70)
    tb1quality.set("")
    tb2vid.set("")
    tb2aud.set("")
    tb4select.set("")
    tb2cap.set("")
    rtx.set("")
    text_box.configure(state='normal')
    text_box.delete(1.0,"end")
    ps=[]
    p1.set('')
    p2.set('')
    p3.set('')
    p4.set('')
    p5.set('')
    prxy.set("")
    cusvar.set("")
    frmt.set('')
    try:
        ratelim.destroy()
        e3.destroy()
        e4.destroy()
        embdth.destroy()
    except:
        pass
    try:
        qt1.destroy()
        qt2.destroy()
        qt3.destroy()
        qt4.destroy()
        qt5.destroy()
    except:
        pass
    try:
        ftbox.destroy()
    except:
        pass
    try:
        check1.destroy()
        check2.destroy()
        check3.destroy()
        check4.destroy()
        check5.destroy()
    except:
        try:
            check1.destroy()
            check2.destroy()
            check3.destroy()
            check4.destroy()
        except:
            try:
                check1.destroy()
                check2.destroy()
                check3.destroy()
            except:
                try:
                    check1.destroy()
                    check2.destroy()
                except:
                    try:
                        check1.destroy()
                    except:
                        pass
                
    try:
        cmb2.destroy()
        cmb.destroy()
        cmb3.destroy()
        check.destroy()
        cb.set(False)
        cmbmus.destroy()
        cmbbsc.destroy()
        tab1clr.destroy()
        tab2clr.destroy()
        btn.destroy()
    except:
        pass
    try:
        picbtn.destroy()
        viewbtn.destroy()
    except:
        pass

    
    try:
        url=e1.widget.get()
    except:
        url=e1.get()
        
    
    if url=="":
        messagebox.showerror("Youtube-dl GUI","  Enter Valid URL  ")
    else:
        if "list=" in url and "youtube" in url and " " not in url:
            playlistvar.set("Select format")
            playlistnum.set('Select items')
            global play,clearplay,items
            items=ttk.Entry(tab3,width=47)
            tabControl.select(2)
            items.place(x=170,y=95)
            play = ttk.Combobox(tab3, width="45", values=playlist,state="readonly")
            play.place(x=170,y=45)
            clearplay = Label(tab3, text = "Clear selection",fg="#0090FF",cursor="hand2",bg="#525252")
            clearplay.place(x = 515,y = 200)
            clearplay.bind("<Button-1>", lambda g: clrt5())
            btn = Button(root,image=img9, text="Download",command=playlister,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")
            btn.bind('<Enter>',lambda a:changer_red(btn,imgdwred))
            btn.bind('<Leave>',lambda a:changer_blue(btn,img9))
            btn.place(x=800,y=506)
            t2 = threading.Thread(target=pltitle, args=(url,))
            t2.start()
            status.set(" [Loading...]                                                                                                                                                                                                          ")
        elif " " not in url:
            try:
                play.destroy()
                clearplay.destroy()
            except:
                pass
            playlistvar.set("Provide playlist URL")
            try:
                items.destroy()
            except:
                pass
            playlistnum.set('')
            status.set(" [Loading...]                                                                                                                                                                                                          ")
            tv1 = threading.Thread(target=srch, args=(url,))
            tv1.start()
            if "youtube" in url or "youtu.be" in url:
                tv2 = threading.Thread(target=thumbnail, args=(url,))
                tv2.start()
        elif " " in url:
            many=url.split()
            global url_lst
            url_lst=[]
            if len(many)>5:
                messagebox.showwarning("YouTube-dl GUI",' Multi-video only supports 5 YouTube URL at max \nFirst 5 will be considered for downloading ')
                for i in range(0,5):
                    if "youtube"  in many[i] or "youtu.be"  in many[i]:
                        url_lst.append(many[i])
            elif len(many)>1 and len(many)<=5:
                for i in range(0,len(many)):
                    if "youtube" in many[i] or "youtu.be" in many[i]:
                        url_lst.append(many[i])

            url_lst=list(set(url_lst))
            tabControl.select(3)
            print(url_lst)
            tv2z = threading.Thread(target=multi, args=(url_lst,))
            status.set(" [Loading...]                                                                                                                                                                                                          ")
            tv2z.start()

    
def checkcmbo():
    global customname,loc
    loc="/"+"Downloads"
    cpt=userloc+"\\Downloads"
    user=(os.environ['USERPROFILE'])
    user=user.replace("\\","/")
    print(download_Directory)
    try:
        loc=download_Directory
        if "C:" in loc:
            c=loc.lstrip(user)
            loc=c.replace("\\","/")
            loc="/"+loc
    except:
        pass
    
    basicdata=cmbbsc.get()
    advvid=cmb.get()
    advaud=cmb2.get()
    if "Audio combined in video streams" in advaud or  'Audio not available' in advaud:
        advaud=""
    if "Video not available" in advvid:
        advvid=""
    advcap=cmb3.get()
    try:
        convertaud=cmbmus.get()
    except:
        convertaud=""
    customname=e3.get()
        
    if "available" in advcap:
        advcap=""
    if "Check Advanced option" in basicdata:
        basicdata=""
    try:
        playdata=play.get()
    except:
        pass
    otformat=ftbox.get()
    print(otformat)
    output="~"+loc+"/"+"%(title)s.%(ext)s"

    if len(customname)!=0:
        customname=customname.replace("?","_")
        customname=customname.replace("<","_")
        customname=customname.replace(">","_")
        customname=customname.replace("|","_")
        customname=customname.replace(":","_")
        customname=customname.replace("*","_")
        customname=customname.replace("/","_")
        customname=customname.replace("\\","_")
        output="~"+loc+"/"+customname+".%(ext)s"

    global ext12fx,ext11,a
    ext12fx=Button(root,text="Pause",bd=0,image=img10,command= pause,activebackground="#202020",highlightthickness = 0)
    ext11=Button(root,text="Cancel",bd=0,image=img12,command=lambda :cmder(ext11,ext12fx),activebackground="#202020",highlightthickness = 0)

    

    if len(basicdata)==0 and len(advvid)==0 and len(advaud)==0 and len(advcap)==0 and len(convertaud)==0:
        messagebox.showerror("Youtube-dl GUI","Select Audio/Video/Music stream")

    elif len(basicdata)!=0 and len(advvid)==0 and len(advaud)==0 and len(advcap)==0 and len(convertaud)==0:
        if basicdata=="Best available":
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --no-restrict-filenames --embed-metadata -f bv+ba -o {} "+url).format(output)
        else:
            w=basicdata.split()
            id1=w[-1]
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --no-restrict-filenames --embed-metadata -f {} -o {} "+url).format(id1,output)
        #print(a)
        

    elif len(basicdata)==0 and len(advvid)!=0 and len(advaud)!=0 and len(advcap)==0 and len(convertaud)==0:
        #print("adv 12")
        a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\"  --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {}+{} -o {} "+url).format(advvid.split()[0],advaud.split()[0],output)
        #a=a+" --download-sections *1:11-4:40 --newline"
        #print("download section")
        

    elif len(basicdata)==0 and len(advvid)!=0 and len(advaud)==0 and len(advcap)==0 and len(convertaud)==0:
        #print("adv 12")
        a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {} -o {} "+url).format(advvid.split()[0],output)
        

    elif len(basicdata)==0 and len(advvid)==0 and len(advaud)!=0 and len(advcap)==0 and len(convertaud)==0:
        #print("adv 12")
        a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --add-metadata --no-mtime --embed-metadata -f {} -o {} "+url).format(advaud.split()[0],output)
        

    elif len(basicdata)==0 and len(advvid)!=0 and len(advaud)!=0 and len(advcap)!=0 and len(convertaud)==0:
        #print("adv 123")
        u=advcap.split()[0]
        #print(u)
        a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --write-srt --sub-lang {} --add-metadata --no-mtime --embed-metadata -f {}+{} -o {} "+url).format(u,advvid.split()[0],advaud.split()[0],output)
        

    elif len(basicdata)==0 and len(advvid)==0 and len(advaud)==0 and len(advcap)==0 and len(convertaud)!=0:
        if "Mp3 64 kbps" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -f ba -x --audio-format mp3 --audio-quality 64K -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
            
        elif "Mp3 128 kbps" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format mp3 --audio-quality 128K -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
        elif "Mp3 320 kbps" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba  -x --audio-format mp3 --audio-quality 320K -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
        elif "M4a High" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format m4a --audio-quality 0  -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
        elif "Wav Lossless" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format wav --audio-quality 0 -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
        elif "Flac 24 bit Lossless" in convertaud:
            b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format flac --audio-quality 0 -o {} '+url).format(output)
            tv2w = threading.Thread(target=run_command4, args=(b,))
            tv2w.start()
    if a:
        print("Exe")
        if len(ratelim.get())!=0:
            a=a+" -r "+ratelim.get()
        if len(e4.get())!=0:
            a=a+" --proxy "+e4.get()
        if c6.get():
            a=a+" --embed-thumbnail "
            #print(c6.get())
        if otformat=="auto-detect":
            tv2w = threading.Thread(target=run_command4, args=(a,))
            tv2w.start()
        elif otformat=="mp4":
            a=a+" --merge-output-format mp4"
            tv2w = threading.Thread(target=run_command4, args=(a,))
            tv2w.start()
        elif otformat=="webm":
            a=a+" --merge-output-format webm"
            tv2w = threading.Thread(target=run_command4, args=(a,))
            tv2w.start()
        else:
            a=a+" --merge-output-format mkv"
            tv2w = threading.Thread(target=run_command4, args=(a,))
            tv2w.start()
        print(a)
    else:
        messagebox.showerror("Youtube-dl GUI","More than one option detected \nTry to Clear unnecessary option(s) \nSelect one option")
        cmbbsc.set("")
        cmbmus.set("")
        clearentry()
            
def playlister():
    loc="/"+"Downloads"
    cpt=userloc+"\\Downloads"
    user=(os.environ['USERPROFILE'])
    user=user.replace("\\","/")
    try:
        loc=download_Directory
        if "C:" in loc:
            c=loc.lstrip(user)
            loc=c.replace("\\","/")
            loc="/"+loc
    except:
        pass
    if len(play.get())==0:
        messagebox.showerror("Youtube-dl GUI","Select format")
    elif len(play.get())!=0:
        link=url[url.rfind("list=")+5:]
        if "144p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:144,vext:mp4,aext:m4a -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "240p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:240,vext:mp4,aext:m4a -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "360p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:360,vext:mp4,aext:m4a -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "480p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:480,vext:mp4,aext:m4a -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "720p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:720,vext:mp4,aext:m4a -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "1080p" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -S height:1080,vext:mp4,aext:m4a "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "best" in play.get():
            a=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -f bv+ba -o {} "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")    
        elif "Mp3 320 kbps" in play.get():
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --audio-format mp3 --no-mtime --audio-quality 320K -o {} --yes-playlist "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "Mp3 64 kbps" in play.get():
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --audio-format mp3 --no-mtime --audio-quality 64K -o {} --yes-playlist "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "M4a High" in play.get():
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime --audio-format m4a -o {} --yes-playlist "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        elif "Wav Losless" in play.get():
            a=("yt-dlp_x86 --ignore-errors --format bestaudio --extract-audio --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-thumbnail --audio-format wav  -o {} --yes-playlist "+link).format("~"+loc+"/"+"%(title)s.%(ext)s")
        if len(items.get())!=0:
            a=a+" --playlist-items "+str(items.get())

        #print(a)

        tv2w = threading.Thread(target=run_command4pl, args=(a,))
        global ext12fx,ext11
        ext12fx=Button(root,text="Pause",bd=0,image=img10,command= pause,activebackground="#202020",highlightthickness = 0)
        ext11=Button(root,text="Cancel",bd=0,image=img12,command=lambda :cmder(ext11,ext12fx),activebackground="#202020",highlightthickness = 0)
        tv2w.start()
        

def update():
    os.system('powershell.exe powershell start updater.exe -v runas')
    #os.startfile('updater.exe')

def run_command2(cmd):
    global ext11,ext12fx
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("Youtube-dl GUI  [Downloading update...]")
        status.set(" "+line[0:-1]+"                                                                                                                                                                                                           ")
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    root.title("Youtube-dl GUI")
    messagebox.showinfo("Youtube-dl GUI","yt-dlp \nUpdated!")
    root3.focus_force()

def run_command4conv(cmd,namez):
    global namewa
    onbtn['state'] = DISABLED
    namewa = Label(tab5, text = "Cancel conversion",fg="#0090FF",cursor="hand2",bg="#525252")
    namewa.place(x = 20,y = 120)
    namewa.bind("<Button-1>", lambda g: kill("taskkill /F /IM ffmpeg.exe"))
    tv2w = threading.Thread(target=popenszz, args=(cmd,namez,))
    tv2w.start()

def popenszz(cmd,namez):
    root.title("Youtube-dl GUI [Converting..]")
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call(cmd, startupinfo=si)
    onbtn['state'] = NORMAL
    namewa.destroy()
    messagebox.showinfo("Youtube-dl GUI","Conversion completed!\nFile "+namez+" Saved")
    root.title("Youtube-dl GUI")

def newconvert():
    a1=ccx.get()
    a2=ccx2.get()
    a3=e5x.get()#filename
    #print(a1,a2,a3,len(a3))
    if len(ccx.get())==0 or len(ccx2.get())==0 or len(e5x.get())==0:
        messagebox.showerror("Youtube-dl GUI","Select format or file")
    elif len(a1)!=0 and len(a2)!=0 and len(a3)!=0:
        x=a3.replace("\\","/")
        d=x[x.rfind("/")+1:]
        d=d.replace("/","\\")
        s=d.rfind(".")
        a3=d[:s]
        #print(a3)
        namez=e2.get()+"/"+a3+"_copy."+a2.lower()
        a=('ffmpeg -i "{}" "{}"').format(e5x.get(),namez)
        print(a)
        run_command4conv(a,namez)
        
        
    
def paste():
    #clr()
    try:
        AnnoyingWindow=Tk()
        ClipBoard = AnnoyingWindow.clipboard_get()
        AnnoyingWindow.destroy()
        r=len(e1.get())
        if r==0:
            ele=ClipBoard
            e1.insert(0, ele )
        else:
            ele=" "+ClipBoard
            e1.insert(r, ele )
    except:
        AnnoyingWindow.destroy()
        messagebox.showerror("Youtube-dl GUI","URL should be in text")
        
def clr():
    e1.delete(0,END)

def convert():
    global ccx2,onbtn
    a="Mp4"
    if ccx.get()=="Mkv":
        a="Mkv"
    elif ccx.get()=="Mp3":
        a="Mp3"
    elif ccx.get()=="M4a":
        a="M4a"
    ex='*.'+a.lower()
    filetypes = (
        (a, ex),
        )
    filenamex = filedialog.askopenfilename(title='Select a file...',filetypes=filetypes)
    #print(filenamex,len(filenamex))
    if len(filenamex)!=0:
        global tox
        tox=[]
        e5x.delete(0,END)
        e5x.insert(0,filenamex)
        convertvar.set("Convert to")
        if a=="Mp4" or a=="Mkv":
            for i in range(0,len(convertfrom)):
                if a!=convertfrom[i]:
                    tox.append(convertfrom[i])
        elif a=="M4a":
            tox=["Mp3"]
        elif a=="Mp3":
            tox=["M4a"]
        ccx2 = ttk.Combobox(tab5, width="12", values=tox,state="readonly")
        ccx2.place(x=485,y=35)
        onbtn = ttk.Button(tab5, text="Convert",command=newconvert)
        onbtn.place(x=250,y=80)

def clearconv():
    tox=[]
    ccx2.destroy()
    onbtn.destroy()
    e5x.delete(0,END)
    e5x.insert(0,"File not selected")
    convertvar.set("")

def changer_red(b,a):
    b.config(image=a)

def changer_blue(b,a):
    b.config(image=a)

def run_commandcustom(cmd):
    global text_area
    startupinfo = subprocess.STARTUPINFO()
    text_area.delete(0.0,END)
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    root.title("Youtube-dl GUI  [Executing command]")
    p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        root.title("Youtube-dl GUI  [Executing command]")
        text_area.insert(END,line[0:-1]+"\n")
        text_area.see(END)
        if str(line)=="":
            break
        
    p.stdout.close()
    p.wait()
    root.title("Youtube-dl GUI")
    messagebox.showinfo("Youtube-dl GUI","\nCommand Executed!")

def custom():
    if len(ex.get())>0:
        cmd="yt-dlp_x86 "+ex.get()
        t2 = threading.Thread(target=run_commandcustom, args=(cmd,))
        t2.start()
    elif len(ex.get())==0:
        messagebox.showerror("Youtube-dl GUI","Enter command")
        

#-------------------------------------------------------------------------------------------------------------------
music=[]
audlst=[]
vidlst=[]
basic=[]
basic2=[]
subs=[]
thn=[1]
ps=[]
playlist=["144p","240p","360p","480p","720p","1080p","best","Mp3 64 kbps","Mp3 320 kbps","M4a High","Wav Losless"]
convertfrom=["Mp4","Mkv","Mp3","M4a"]
root = tk.Tk()
root.configure(bg='#303135')
style= ttk.Style()
style.configure("TCombobox", fieldbackground= "#525252", background= "#525252",foreground="black")
style.configure("TButton",background="#525252")
style.configure("TScrollbar",background="#525252",activebackground="#525252")
style.configure("TNotebook", background='#424242',borderwidth=0)
style.configure("TCheckbutton", background='#525252',foreground="white",activebackground="#525252",borderwidth=0)

style.layout("TNotebook", [])

md=PhotoImage(file = "Frame 1newer.png")
canvas1 = Canvas( root, width = 560,height = 1000)
background_label = Label(image=md,anchor="n")
background_label.place(x=0, y=-2, relwidth=1, relheight=1)
canvas1.pack()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
y=int((sh-640)/2)
x=int((sw-1000)/2)
root.geometry('%dx%d+%d+%d' % (1030, 580, x, y))
root.resizable(False, False)

tabControl = ttk.Notebook(root,height=236,width=624)

tab1 = Frame(tabControl,background="#525252")
tab2 = Frame(tabControl,background="#525252")
tab3 = Frame(tabControl,background="#525252")
tab4 = Frame(tabControl,background="#525252")
tab5 = Frame(tabControl,background="#525252")
tab6 = Frame(tabControl,background="#525252")
tab7 = Frame(tabControl,background="#525252")
streamsvid = Label(tab5,text="Convert From",bg="#525252",fg="white").place(x = 15,y = 10)
btnz = ttk.Button(tab5, text="Browse File",command=convert)
btnz.place(x=135,y=33)

tabControl.add(tab1, text ='  Basic  ')
tabControl.add(tab2, text ='  Advanced ')
tabControl.add(tab3, text ='  Playlist  ')
tabControl.add(tab4, text =' Multi video ')
tabControl.add(tab5, text ='  Converter ')
tabControl.add(tab6, text ='  Custom command ')
tabControl.add(tab7, text =' History ')
tabControl.place(x=35,y=215)#275

ccx = ttk.Combobox(tab5, width="12", values=convertfrom,state="readonly")
ccx.place(x=15,y=35)
ccx.current(0)
e5x=ttk.Entry(tab5,width=40)
e5x.place(x=220,y=35)
e5x.insert(0,"File not selected")
name45za = Label(tab5, text = "Clear selection",fg="#0090FF",cursor="hand2",bg="#525252")
name45za.place(x = 515,y = 200)
name45za.bind("<Button-1>", lambda g: clearconv())

from tkinter import scrolledtext
s=Label(tab6, text="yt-dlp ARGS",fg="white",bg="#525252").place(x=8,y=10)
text_area = scrolledtext.ScrolledText(tab6, wrap=tk.WORD,width=83, height=11,font=('Microsoft Sans Serif',9),background="#404040",fg="white",highlightthickness=0,relief=FLAT)  
text_area.grid(column=0, row=2, pady=40, padx=10)
#history
def clearhistory():
    answer = messagebox.askquestion('Youtube-dl GUI','Are you sure that you want to clear history?')
    if answer=="yes":
        file4=open(os.getcwd()+"\\database\\history.txt",'w+')
        file4.write("")
        file4.close()
        refresh()
    
def sel(a):
    selected=my_game.focus()
    val=my_game.item(selected,'values')
    print(val)
    files=os.listdir(val[3])
    for i in range(0,len(files)):
        if val[0] in files[i]:
            print(val[-1]+"/"+files[i])
            try:#bug : work for ascii filenames
                if ".vtt" not in files[i]:
                    os.startfile(val[-1]+"/"+files[i])
                    break
            except:
                messagebox.showerror("Youtube-dl GUI","File not found")
                break

def cl(a):
    sel(a)

def refresh():
    global my_game,verscrlbar
    try:
        my_game.destroy()
        verscrlbar.destroy()
    except:
        pass
    my_game = ttk.Treeview(tab7,height=9)
    my_game.bind("<Double-Button-1>", lambda g: cl(my_game))
    verscrlbar = ttk.Scrollbar(tab7,orient ="vertical",command = my_game.yview)
    verscrlbar.pack(side ='right', fill ='x')
    my_game.configure(xscrollcommand = verscrlbar.set)
    my_game['columns'] = ('Title', 'URL', 'Date time', 'Location')
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Title",anchor=CENTER, width=180)
    my_game.column("URL",anchor=CENTER,width=120)
    my_game.column("Date time",anchor=CENTER,width=120)
    my_game.column("Location",anchor=CENTER,width=180)
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Title",text="Title",anchor=CENTER)
    my_game.heading("URL",text="URL",anchor=CENTER)
    my_game.heading("Date time",text="Date time",anchor=CENTER)
    my_game.heading("Location",text="Location",anchor=CENTER)
    file4=open(os.getcwd()+"\\database\\history.txt",'r')
    log=file4.readlines()
    file4.close()
    my_game.pack()
    if len(log)!=0:
        for i in range(-1,-1-len(log),-1):
            zc=log[i].split("^")[0]
            zc=zc.replace("?","")
            zc=zc.replace("<","")
            zc=zc.replace(">","")
            zc=zc.replace("|","")
            zc=zc.replace(":","")
            zc=zc.replace("*","")
            zc=zc.replace("/","")
            zc=zc.replace("\\","")
            zv=log[i].split("^")[1]
            zb=log[i].split("^")[2]
            zn=log[i].split("^")[-2]
            my_game.insert(parent='',index='end',iid=i,text='',values=(zc,zv,zb,zn))
            


refresh()
name3r = Label(tab7, text="Refresh",bg="#525252",fg="orange",cursor='hand2')
name3r.bind("<Button-1>", lambda e: refresh())
name3r.place(x=525,y=210)
name4r = Label(tab7, text="Clear history",bg="#525252",fg="yellow",cursor='hand2')
name4r.bind("<Button-1>", lambda e: clearhistory())
name4r.place(x=5,y=210)
Label(tab7, text="Double click to open files",bg="#525252",fg="white").place(x=230,y=210)
#--------------------------------------------------------------------------------------------------------------
p1=StringVar()
p2=StringVar()
p3=StringVar()
p4=StringVar()
p5=StringVar()
pcx=StringVar()
frmt=StringVar()
rtx=StringVar()
frmt.set('')
p1.set('')
p2.set('')
p3.set('')
p4.set('')
p5.set('')
rtx.set('')
streamsvid = Label(tab4, textvariable = p1,bg="#525252",fg="white").place(x = 290,y = 20)
streamsvid = Label(tab4, textvariable = p2,bg="#525252",fg="white").place(x = 290,y = 20+21)
streamsvid = Label(tab4, textvariable = p3,bg="#525252",fg="white").place(x = 290,y = 20+42)
streamsvid = Label(tab4, textvariable = p4,bg="#525252",fg="white").place(x = 290,y = 20+42+21)
streamsvid = Label(tab4, textvariable = p5,bg="#525252",fg="white").place(x = 290,y = 20+42+42)
ft = Label(tab2, textvariable = frmt,bg="#525252",fg="white").place(x = 330-50,y = 100)
rt = Label(tab2, textvariable = rtx,bg="#525252",fg="white").place(x = 442,y = 100)
#--------------------------------------------------------------------------------------------------------------
convertvar=StringVar()
convertvar.set("")
urlvar=StringVar()
playlistvar=StringVar()
playlistvar.set("")
playlistnum=StringVar()
playlistnum.set('')

tb1quality=StringVar()
tb2aud=StringVar()
tb2vid=StringVar()
tb4select=StringVar()
tb2cap=StringVar()
cb = BooleanVar()
c1=BooleanVar()
c2=BooleanVar()
c3=BooleanVar()
c4=BooleanVar()
c5=BooleanVar()
c6=BooleanVar()
prxy=StringVar()
prxy.set("")
tb1quality.set("")
tb2vid.set("")
tb2cap.set("")
tb2aud.set("")
tb4select.set("")

urlvar.set("URL")
outvar=StringVar()
outvar.set("Output")
cusvar=StringVar()
cusvar.set("")
name1 = Label(root, text = "Youtube-dl GUI",bg="#303135",font=('Arial', 18),fg="white").place(x = 230,y = 10) 
name = Label(root, textvariable = urlvar,bg="#424242",fg="white").place(x = 55,y = 76)
name3r = Label(root, textvariable = outvar,bg="#424242",fg="white",cursor='hand2')
name3r.bind("<Button-1>", lambda e: os.startfile(e2.get()))
name3r.bind('<Enter>',lambda a:name3r.config(fg="#0574FF"))
name3r.bind('<Leave>',lambda a:name3r.config(fg="white"))
name3r.place(x = 55,y = 148)
name = Label(tab2, textvariable = cusvar,bg="#525252",fg="white").place(x = 20,y = 146)
name = Label(tab2, textvariable = prxy,bg="#525252",fg="white").place(x = 330,y = 146)
streamsvidto = Label(tab5,textvariable=convertvar,bg="#525252",fg="white").place(x = 485,y = 10)
userloc=(os.environ['USERPROFILE'])+"\\Downloads"
userloc=userloc.replace("\\","/")
status= StringVar()
status.set("")
large_font = tkFont.Font(family='Microsoft Sans Serif',size=9)
statusbar = tk.Label(root, textvariable=status ,width=150, bd=2,fg="white", relief=tk.SUNKEN, anchor=tk.W,bg='#202125').place(x=-2,y=560)

url=""
streamsvid = Label(tab3, textvariable = playlistvar,bg="#525252",fg="white").place(x = 170,y = 20)
streamsvidz = Label(tab3, textvariable = playlistnum,bg="#525252",fg="white").place(x = 170,y = 70)
streamsvid = Label(tab1, textvariable = tb1quality,bg="#525252",fg="white").place(x = 20,y = 20)
streamsvid = Label(tab2, textvariable = tb2vid,bg="#525252",fg="white").place(x = 20,y = 10)
streamsvid = Label(tab2, textvariable = tb2aud,bg="#525252",fg="white").place(x = 20,y = 55)
streamsvid = Label(tab1, textvariable = tb4select,bg="#525252",fg="white").place(x = 26,y = 85)
streamsvid = Label(tab2, textvariable = tb2cap,bg="#525252",fg="white").place(x = 20,y = 100)

frame1=Frame(root,bg = "#303135",width=280,height=200)
frame1.place(x=708,y=275)
sb_ver= ttk.Scrollbar(frame1)
text_box = Text(frame1,height=14,width=41,highlightthickness=0,relief=FLAT,yscrollcommand=sb_ver.set)
fonte = tkFont.Font(family="Arial", size=10)


text_box.config(font=large_font,state= NORMAL,background="#404040",fg="grey")#404040
sb_ver.config(command=text_box.yview)
sb_ver.pack(side=RIGHT, fill=Y)
text_box.pack(side=LEFT)
text_box.configure(state='disabled')


e1 = Entry(root,width=82,bg="#A1A1A1",bd=0)
e1.place(x=52,y=104)
e1.bind("<Return>", on_change)

e2 = Entry(root,bg="#A1A1A1",width=82,bd=0)
e2.place(x=52,y=179)
zzz = open(os.getcwd()+"\\database\\loc.txt",'r')
download_Directory=str(zzz.readlines()[0])
e2.insert(0, download_Directory )
zzz.close()


ex=Entry(tab6,bg="#303135",width=55,bd=0,fg="white",font=('Microsoft Sans Serif',10))
ex.place(x=82,y=10)


def paste2():
    try:
        AnnoyingWindow=Tk()
        ClipBoard = AnnoyingWindow.clipboard_get()
        AnnoyingWindow.destroy()
        ele=ClipBoard
        ex.insert(END, " "+ele )
    except:
        AnnoyingWindow.destroy()
        messagebox.showerror("Youtube-dl GUI","URL should be in text")

def clr2():
    ex.delete(0,END)
    text_area.delete(0.0,END)

imgpst = PhotoImage(file = f"paste2.png")
namepst = Button(tab6, text = "Paste",fg="blue",bd=0,bg="#525252",image=imgpst,command=lambda : paste2(),activebackground='#525252')
namepst.place(x=480,y=10)

imgclr = PhotoImage(file = f"clr2.png")
nameclr = Button(tab6, text = "Clear",fg="blue",bd=0,bg="#525252",image=imgclr,command=lambda : clr2(),activebackground='#525252')
nameclr.place(x=515,y=10)

name7zax = ttk.Button(tab6, text = "RUN",command=lambda : custom())
name7zax.config(width=8)
name7zax.place(x=553,y=10)

name75 = Label(tab6, text = "How to use ?",fg="orange",cursor="hand2",bg="#525252")
name75.place(x = 10,y = 210)
name75.bind("<Button-1>", lambda e: link('https://github.com/yt-dlp/yt-dlp#usage-and-options'))

name75 = Label(tab6, text = "eg. -F <URL>",fg="white",bg="#525252")
name75.place(x = 535,y = 210)

name75 = Label(tab6, text = "Terminal",fg="cyan",cursor="hand2",bg="#525252")
name75.place(x = 290,y = 210)
name75.bind("<Button-1>", lambda e : terminal())

img3 = PhotoImage(file = f"img3.png")
name7z = Button(root, text = "About",fg="blue",bd=0,bg="#383838",image=img3,command=lambda : about(),activebackground='#383838')
name7z.bind('<Enter>',lambda a:changer_red(name7z,aboutd))
name7z.bind('<Leave>',lambda a:changer_blue(name7z,img3))
name7z.place(x = 28,y = 510)

img4 = PhotoImage(file = f"img4.png")
name8 = Button(root, text = "Update",fg="blue",bd=0,bg="#383838",image=img4,command=lambda : update(),activebackground='#383838')
name8.bind('<Enter>',lambda a:changer_red(name8,updated))
name8.bind('<Leave>',lambda a:changer_blue(name8,img4))
name8.place(x = 120,y = 510)

img5 = PhotoImage(file = f"img5.png")
name9 = Button(root, text = "Terminal",fg="blue",bd=0,bg="#383838",image=img5,command=lambda : terminal(),activebackground='#383838')
name9.bind('<Enter>',lambda a:changer_red(name9,terminald))
name9.bind('<Leave>',lambda a:changer_blue(name9,img5))
name9.place(x = 216,y = 510)

img6 = PhotoImage(file = f"img6.png")
name10 = Button(root, text = "Github",fg="blue",bd=0,bg="#383838",image=img6,command=lambda : link('https://github.com/sourabhkv/ytdl/'),activebackground='#383838')
name10.bind('<Enter>',lambda a:changer_red(name10,githubd))
name10.bind('<Leave>',lambda a:changer_blue(name10,img6))
name10.place(x = 324,y = 510)

img7 = PhotoImage(file = f"img7.png")
name11 = Button(root, text = "Supported  Websites",bd=0,fg="blue",bg="#383838",image=img7,command=lambda : link('https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'),activebackground='#383838')
name11.bind('<Enter>',lambda a:changer_red(name11,supd))
name11.bind('<Leave>',lambda a:changer_blue(name11,img7))
name11.place(x = 420,y = 510)

img14 = PhotoImage(file = f"settings.png")
name7 = Button(root, text = "Options",fg="blue",bd=0,bg="#383838",image=img14,command=lambda : reco(),activebackground='#383838')
name7.bind('<Enter>',lambda a:changer_red(name7,optionsd))
name7.bind('<Leave>',lambda a:changer_blue(name7,img14))
name7.place(x = 585,y = 510)

image = Image.open("logo.png")
img9 = PhotoImage(file = "img9.png")
img10 = PhotoImage(file = "img10.png")
img11 = PhotoImage(file = "img11.png")
img12 = PhotoImage(file = "img12.png")
img13 = PhotoImage(file = "img13.png")
imggored = PhotoImage(file="gored.png")
imgdwred = PhotoImage(file="dwred.png")
aboutd=PhotoImage(file="aboutdark.png")
updated=PhotoImage(file="updatedark.png")
githubd=PhotoImage(file="githubdark.png")
terminald=PhotoImage(file="terminaldark.png")
supd=PhotoImage(file="supportedwebsitesdark.png")
optionsd=PhotoImage(file="settingsdark.png")
imgclearred = PhotoImage(file="clearred.png")
imgpastered = PhotoImage(file="pastered.png")
imgbrowred = PhotoImage(file="browred.png")
imgthred = PhotoImage(file="thred.png")
resize_image = image.resize((25, 25))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img,bg="#303135")
label1.image = img
label1.place(x=410,y=10)
img8 = PhotoImage(file = f"browse.png")
browse_B = Button(root,image=img8,bd=0, text="Browse", command=browse,relief="flat",bg="#424242",activebackground='#424242')
browse_B.bind('<Enter>',lambda a:changer_red(browse_B,imgbrowred))
browse_B.bind('<Leave>',lambda a:changer_blue(browse_B,img8))
browse_B.place(x=570,y=170)
img0 = PhotoImage(file = f"paste.png")
ext15=Button(root,bd=0,image=img0,text="Paste",command=paste,relief="flat",bg="#424242",activebackground='#424242')
ext15.bind('<Enter>',lambda a:changer_red(ext15,imgpastered))
ext15.bind('<Leave>',lambda a:changer_blue(ext15,img0))
ext15.place(x=200,y=134)
img1 = PhotoImage(file = f"clear.png")
ext16=Button(root,text="Clear",bd=0,image=img1,command=clr,relief="flat",bg="#424242",activebackground='#424242')
ext16.bind('<Enter>',lambda a:changer_red(ext16,imgclearred))
ext16.bind('<Leave>',lambda a:changer_blue(ext16,img1))
ext16.place(x=300,y=134)
img2 = PhotoImage(file = f"go.png")
ext17go=Button(root,text="GO",bd=0,image=img2,command=lambda: on_change(e1),bg="#424242",activebackground='#424242')
ext17go.bind('<Enter>',lambda a:changer_red(ext17go,imggored))
ext17go.bind('<Leave>',lambda a:changer_blue(ext17go,img2))
ext17go.place(x=570,y=96)

root.iconbitmap(r'logo.ico')
root.title('Youtube-dl GUI')
messagebox.showinfo("Youtube-dl GUI","This version is out of support & will not get future updates.\nTo get latest version uninstall this version & Check on 8 August or later : https://sourabhkv.github.io/ytdl")
root.mainloop()
