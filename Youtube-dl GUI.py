import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
import os
from yt_dlp import YoutubeDL
import subprocess,threading,time
import tkinter.font as tkFont
import json, urllib,sys,pyperclip
import urllib.request
import requests,datetime
from datetime import datetime
from urllib.request import urlopen
import shutil,time,psutil
from io import BytesIO
from zipfile import ZipFile
from tkinter import scrolledtext
import webbrowser
rloc=str(__file__)
print(rloc)
print(rloc[:rloc.rfind("\\")])
os.chdir(rloc[:rloc.rfind("\\")])
class App(tk.Tk):
    def __init__(self,*args):
        super().__init__()
        self.title('YouTube-dl GUI')
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        self.y=int((self.sh-700)/2)
        self.x=int((self.sw-1050)/2)
        self.resizable(False, False)
        #self.maxsize(1300,732)
        self.geometry('%dx%d+%d+%d' % (1050, 620, self.x, self.y))
        self.configure(bg='#303135')
        self.iconbitmap("./images/logo.ico")

        #self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.style= ttk.Style()
        self.style.configure("TCombobox", fieldbackground= "#525252", background= "#525252",foreground="black")
        self.style.configure("TButton",background="#525252")
        self.style.configure("TScrollbar",background="#525252",activebackground="#525252")
        self.style.configure("TNotebook", background='#424242',borderwidth=0)
        self.style.configure("TCheckbutton", background='#525252',foreground="white",activebackground="#525252",borderwidth=0)
        self.style.layout("TNotebook", [])

        self.image=Image.open("./images/Frame 1newer.png")
        self.canvas1 = Canvas( self)
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(image=self.background_image,anchor="n")
        self.background.pack(fill="both",expand=True)
        self.canvas1.pack(fill="both",expand=True)

        self.tabControl = ttk.Notebook(self,height=236,width=640)
        self.tab1 = Frame(self.tabControl,background="#525252")
        self.tab2 = Frame(self.tabControl,background="#525252")
        self.tab3 = Frame(self.tabControl,background="#525252")
        self.tab4 = Frame(self.tabControl,background="#525252")
        self.tab5 = Frame(self.tabControl,background="#525252")
        self.tab6 = Frame(self.tabControl,background="#525252")
        self.tab7 = Frame(self.tabControl,background="#525252")


        self.tabControl.add(self.tab1, text ='  Basic  ')
        self.tabControl.add(self.tab2, text ='  Advanced ')
        self.tabControl.add(self.tab3, text ='  Playlist  ')
        self.tabControl.add(self.tab4, text =' Multi video ')
        self.tabControl.add(self.tab5, text ='  Converter ')
        self.tabControl.add(self.tab6, text ='  Custom Exec ')
        self.tabControl.add(self.tab7, text =' History ')
        self.tabControl.place(relx=.331,rely=.617,anchor=CENTER)
        
        #self.status= StringVar()
        #self.statusbar = Label(self, textvariable=self.status ,width=1500, bd=2,fg="white", relief=tk.SUNKEN, anchor=tk.W,bg='#202125')
        #self.statusbar.place(relx=0.5,rely=1.001,anchor=S)

        self.large_font = tkFont.Font(family='Microsoft Sans Serif',size=9)
        #self.statusbar = tk.Label(s1, textvariable=self.status ,width=150, bd=2,fg="white", relief=tk.SUNKEN, anchor=tk.W,bg='#202125').place(x=-2,y=560)

        self.frame1=Frame(self,bg = "#303135",width=290,height=205)
        self.frame1.place(x=720,y=293)
        self.frame2=Frame(self,bg = "#A1A1A1",width=490,height=60)
        self.frame2.place(relx=0.286,rely=0.215,anchor=CENTER)

        self.frame3=Frame(self.tab4,bg = "#A1A1A1",width=910,height=170)
        self.frame3.place(relx=0.4,rely=0.212,anchor=CENTER)

        

        self.sb_ver= ttk.Scrollbar(self.frame1)
        self.sb_ver2= ttk.Scrollbar(self.frame2)
        self.sb_ver3= ttk.Scrollbar(self.frame3)
        
        self.text_box = Text(self.frame1,height=15,width=41,highlightthickness=0,relief=FLAT,yscrollcommand=self.sb_ver.set)
        self.fonte = tkFont.Font(family="Arial", size=10)
        self.text_box.config(font=self.large_font,state= NORMAL,background="#404040",fg="grey")#404040
        self.sb_ver.config(command=self.text_box.yview)
        self.sb_ver.pack(side=RIGHT, fill=Y)
        self.text_box.pack(side=LEFT)
        self.text_box.configure(state='disabled')

        self.url_box = Text(self.frame2,height=4,width=67,highlightthickness=0,relief=FLAT,yscrollcommand=self.sb_ver2.set)
        self.url_box.config(font=self.large_font,state= NORMAL,background="#A1A1A1",fg="black")#404040
        self.sb_ver2.config(command=self.url_box.yview)
        self.sb_ver2.pack(side=RIGHT, fill=Y)
        self.url_box.pack(side=LEFT)

        self.multi_box = Text(self.frame3,height=7,width=67,highlightthickness=0,relief=FLAT,yscrollcommand=self.sb_ver3.set)
        self.multi_box.config(font=self.large_font,state= NORMAL,background="#A1A1A1",fg="black")#404040
        self.sb_ver3.config(command=self.multi_box.yview)
        self.sb_ver3.pack(side=RIGHT, fill=Y)
        self.multi_box.pack(side=LEFT)

        self.tb7ref = Label(self.tab7, text="Refresh",bg="#525252",fg="orange",cursor='hand2')
        self.tb7ref.bind("<Button-1>", lambda e: self.refresh())
        self.tb7ref.place(x=525,y=210)

        self.tb7clr = Label(self.tab7, text="Clear history",bg="#525252",fg="yellow",cursor='hand2')
        self.tb7clr.bind("<Button-1>", lambda e: self.clearhistory())
        self.tb7clr.place(x=5,y=210)

        Label(self.tab7, text="Double click to launch files  ,  Right click to open files in explorer",bg="#525252",fg="white").place(x=125,y=210)

        #self.e1 = Entry(self,width=82,bg="#A1A1A1",bd=0)#A1A1A1
        #self.e1.place(relx=0.292,rely=0.195,anchor=CENTER)
        #self.e1.bind("<Return>", self.on_change)

        self.output_loc()

        self.pastebtn=PhotoImage(file = "./images/paste.png")
        self.pastebtnred = PhotoImage(file="./images/pastered.png")
        self.pasteurl=Button(self,bd=0,image=self.pastebtn,text="Paste",command= lambda: self.paste(self.url_box),relief="flat",bg="#424242",activebackground='#424242')
        self.pasteurl.bind('<Enter>',lambda a: self.changer_red(self.pasteurl,self.pastebtnred))
        self.pasteurl.bind('<Leave>',lambda a: self.changer_blue(self.pasteurl,self.pastebtn))
        self.pasteurl.place(x=200,y=174)

        self.clearbtn = PhotoImage(file = "./images/clear.png")
        self.clearbtnred = PhotoImage(file="./images/clearred.png")
        self.clearurl=Button(self,text="Clear",bd=0,image=self.clearbtn,command=lambda : self.clr(self.url_box),relief="flat",bg="#424242",activebackground='#424242')
        self.clearurl.bind('<Enter>',lambda a : self.changer_red(self.clearurl,self.clearbtnred))
        self.clearurl.bind('<Leave>',lambda a : self.changer_blue(self.clearurl,self.clearbtn))
        self.clearurl.place(x=300,y=174)

        self.gobtn = PhotoImage(file = "./images/go.png")
        self.gobtnred = PhotoImage(file="./images/gored.png")
        self.go=Button(self,text="GO",bd=0,image=self.gobtn,command= lambda : self.on_change(self.url_box),bg="#424242",activebackground='#424242')
        self.go.bind('<Enter>',lambda a: self.changer_red(self.go,self.gobtnred))
        self.go.bind('<Leave>',lambda a: self.changer_blue(self.go,self.gobtn))
        self.go.place(x=570,y=96)

        self.browsebtn = PhotoImage(file = "./images/browse.png")
        self.browsebtnred = PhotoImage(file = "./images/browred.png")
        self.browse = Button(self,image=self.browsebtn,bd=0, text="Browse", command=lambda : self.browse_file(),relief="flat",bg="#424242",activebackground='#424242')
        self.browse.bind('<Enter>',lambda a:self.changer_red(self.browse,self.browsebtnred))
        self.browse.bind('<Leave>',lambda a:self.changer_blue(self.browse,self.browsebtn))
        self.browse.place(x=575,y=212)

        self.aboutpic = PhotoImage(file = "./images/img3.png")
        self.aboutpicdark=PhotoImage(file="./images/aboutdark.png")
        self.about = Button(self, text = "About",fg="blue",bd=0,bg="#383838",image=self.aboutpic,command=lambda : self.open_window(),activebackground='#383838')
        self.about.bind('<Enter>',lambda a : self.changer_red(self.about,self.aboutpicdark))
        self.about.bind('<Leave>',lambda a : self.changer_blue(self.about,self.aboutpic))
        self.about.place(x = 28,y = 548)

        self.updatepic = PhotoImage(file = "./images/img4.png")
        self.updatedark=PhotoImage(file="./images/updatedark.png")
        self.update = Button(self, text = "Update",fg="blue",bd=0,bg="#383838",image=self.updatepic,command=lambda : self.update,activebackground='#383838')
        self.update.bind('<Enter>',lambda a: self.changer_red(self.update,self.updatedark))
        self.update.bind('<Leave>',lambda a: self.changer_blue(self.update,self.updatepic))
        self.update.place(x = 120,y = 548)

        self.donatepic = PhotoImage(file = "./images/donatedark.png")
        self.donatepicdark=PhotoImage(file="./images/donatelight.png")
        self.donate = Button(self, text = "Terminal",fg="blue",bd=0,bg="#383838",image=self.donatepic,command=lambda : webbrowser.open("https://github.com/sourabhkv/ytdl#support-us"),activebackground='#383838')
        self.donate.bind('<Enter>',lambda a: self.changer_red(self.donate,self.donatepicdark))
        self.donate.bind('<Leave>',lambda a: self.changer_blue(self.donate,self.donatepic))
        self.donate.place(x = 216,y = 548)

        self.githubpic = PhotoImage(file = "./images/img6.png")
        self.githubpicdark=PhotoImage(file="./images/githubdark.png")
        self.github = Button(self, text = "Github",fg="blue",bd=0,bg="#383838",image=self.githubpic,command=lambda : webbrowser.open('https://github.com/sourabhkv/ytdl/'),activebackground='#383838')
        self.github.bind('<Enter>',lambda a: self.changer_red(self.github,self.githubpicdark))
        self.github.bind('<Leave>',lambda a: self.changer_blue(self.github,self.githubpic))
        self.github.place(x = 324,y = 548)

        self.dwpic = PhotoImage(file = "./images/img9.png")
        self.dwpicdark = PhotoImage(file = "./images/dwred.png")
        self.thpic = PhotoImage(file = "./images/"+"img13.png")
        self.thpicdark =  PhotoImage(file = "./images/thred.png")
        self.cancelpic =  PhotoImage(file = "./images/img12.png")
        self.resumepic =  PhotoImage(file = "./images/img11.png")
        self.pausepic =  PhotoImage(file = "./images/img10.png")

        self.cancelbtn=Button(image=self.cancelpic, command=lambda: self.cancel() ,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")
        self.pausebtn=Button(image=self.pausepic, command=lambda: self.pause(self.cmd) ,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")

        self.supwpic = PhotoImage(file = "./images/img7.png")
        self.supwpicdark=PhotoImage(file="./images/supportedwebsitesdark.png")
        self.supw = Button(self, text = "Supported  Websites",bd=0,fg="blue",bg="#383838",image=self.supwpic,command=lambda : webbrowser.open('https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'),activebackground='#383838')
        self.supw.bind('<Enter>',lambda a: self.changer_red(self.supw,self.supwpicdark))
        self.supw.bind('<Leave>',lambda a: self.changer_blue(self.supw,self.supwpic))
        self.supw.place(x = 420,y = 548)

        self.oppic = PhotoImage(file = "./images/settings.png")
        self.oppicdark=PhotoImage(file="./images/settingsdark.png")
        self.option = Button(self, text = "Options",fg="blue",bd=0,bg="#383838",image=self.oppic,command=lambda : self.open_settings(),activebackground='#383838')
        self.option.bind('<Enter>',lambda a: self.changer_red(self.option,self.oppicdark))
        self.option.bind('<Leave>',lambda a: self.changer_blue(self.option,self.oppic))
        self.option.place(x = 585,y = 548)
        
        self.status=StringVar()
        self.status.set(' ')
        self.statusbar = Label(self, textvariable=self.status ,width=150, bd=2,fg="white",bg='#202125',relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.place(x=-2,y=600)

        self.mulstatus=StringVar()
        self.mulstatus.set("ddf")
        self.mulstatusbar = Label(self.tab4, textvariable=self.mulstatus ,width=150, bd=2,fg="white",bg='#202125',relief=tk.SUNKEN, anchor=tk.W)
        self.mulstatusbar.place(x=-2,y=216)

        self.static_url=StringVar()
        self.static_url.set("URL")
        Label(self, textvariable=self.static_url ,fg="white",bg='#424242').place(x=60,y=73)

        self.static_out=StringVar()
        self.static_out.set("Output")
        self.output_label=Label(self, textvariable=self.static_out ,fg="white",bg='#424242')
        self.output_label.bind('<Button-1>',self.openloc)
        self.output_label.bind('<Enter>', lambda e : self.output_label.configure(fg="#0574FF"))
        self.output_label.bind('<Leave>', lambda e : self.output_label.configure(fg="white"))
        self.output_label.place(x=60,y=189)


        #tab6
        Label(self.tab6, text="yt-dlp ARGS",fg="white",bg="#525252").place(x=8,y=10)
        self.text_area = scrolledtext.ScrolledText(self.tab6, wrap=tk.WORD,width=83, height=11,font=('Microsoft Sans Serif',9),background="#404040",fg="white",highlightthickness=0,relief=FLAT)
        self.text_area.grid(column=0, row=2, pady=40, padx=10)
        self.ex=Entry(self.tab6,bg="#303135",width=55,bd=0,fg="white",font=('Microsoft Sans Serif',10))
        self.ex.bind('<Return>',self.custom)
        self.ex.place(x=82,y=10)
        self.imgpst = PhotoImage(file = "./images/paste2.png")
        self.namepst = Button(self.tab6, text = "Paste",fg="blue",bd=0,bg="#525252",image=self.imgpst,command=lambda : self.paste2(),activebackground='#525252')
        self.namepst.place(x=480,y=10)
        self.imgclr = PhotoImage(file = "./images/clr2.png")
        self.nameclr = Button(self.tab6, text = "Clear",fg="blue",bd=0,bg="#525252",image=self.imgclr,command=lambda : self.clr2(),activebackground='#525252')
        self.nameclr.place(x=515,y=10)
        self.run6 = ttk.Button(self.tab6, text = "RUN",command=lambda : self.custom())
        self.run6.config(width=8)
        self.run6.place(x=553,y=10)

        #predef
        self.vidlabel=StringVar()
        self.vidlabel.set('')
        Label(self.tab2, textvariable=self.vidlabel,fg="white",bg='#525252').place(x=30,y=8)

        self.audlabel=StringVar()
        self.audlabel.set('')
        Label(self.tab2, textvariable=self.audlabel,fg="white",bg='#525252').place(x=30,y=56)

        self.caplabel=StringVar()
        self.caplabel.set('')
        Label(self.tab2, textvariable=self.caplabel,fg="white",bg='#525252').place(x=30,y=102)

        self.frmtlabel=StringVar()
        self.frmtlabel.set('')
        Label(self.tab2, textvariable=self.frmtlabel,fg="white",bg='#525252').place(x=305,y=104)

        self.rlimlabel=StringVar()
        self.rlimlabel.set('')
        Label(self.tab2, textvariable=self.rlimlabel,fg="white",bg='#525252').place(x=465,y=104)

        self.custlabel=StringVar()
        self.custlabel.set('')
        Label(self.tab2, textvariable=self.custlabel,fg="white",bg='#525252').place(x=30,y=152)

        self.pxylabel=StringVar()
        self.pxylabel.set('')
        Label(self.tab2, textvariable=self.pxylabel,fg="white",bg='#525252').place(x=340,y=152)

        self.mrglabel=StringVar()
        self.mrglabel.set('')
        Label(self.tab1, textvariable=self.mrglabel,fg="white",bg='#525252').place(x=30,y=15)

        self.stlabel=StringVar()
        self.stlabel.set('')
        Label(self.tab1, textvariable=self.stlabel,fg="white",bg='#525252').place(x=180,y=65)

        self.etlabel=StringVar()
        self.etlabel.set('')
        Label(self.tab1, textvariable=self.etlabel,fg="white",bg='#525252').place(x=380,y=65)

        self.plfrmtlabel=StringVar()
        self.plfrmtlabel.set('')
        Label(self.tab3, textvariable=self.plfrmtlabel,fg="white",bg='#525252').place(x=210,y=100)

        self.plsilabel=StringVar()
        self.plsilabel.set('')
        Label(self.tab3, textvariable=self.plsilabel,fg="white",bg='#525252').place(x=210,y=30)

        self.how_to_use = Label(self.tab6, text = "How to use ?",fg="yellow",cursor="hand2",bg="#525252")
        self.how_to_use.bind('<Button-1>',lambda e: webbrowser.open("https://github.com/yt-dlp/yt-dlp#usage-and-options"))
        self.how_to_use.place(x=20,y=210)

        Label(self.tab6, text = "eg. -F <URL>",fg="white",bg="#525252").place(x=530,y=210)

        self.terminal = Label(self.tab6 , text="Terminal" , fg="cyan", bg="#525252", cursor="hand2")
        self.terminal.bind('<Button-1>',lambda e: subprocess.Popen('start terminal.bat',shell=True))
        self.terminal.place(x=290,y=210)

        self.clr2label=Label(self.tab2, text = "",bg="#525252",fg="#0090FF")
        self.clr2label.bind('<Button-1>',lambda e: self.clrtab2())
        self.clr2label.place(x=530,y=205)

        self.clr1label=Label(self.tab1, text = "",bg="#525252",fg="#0090FF")
        self.clr1label.bind('<Button-1>',lambda e: self.clrtab1())
        self.clr1label.place(x=530,y=205)

        self.clr3label=Label(self.tab3, text = "",bg="#525252",fg="#0090FF")
        self.clr3label.bind('<Button-1>',lambda e: self.clrtab3())
        self.clr3label.place(x=530,y=205)

        Label(self, text = "Youtube-dl GUI",bg="#303135",font=('Arial', 18),fg="white").place(x = 230,y = 12)
        self.ytdlimg = Image.open("./images/logo.png")
        self.ytdlresize = self.ytdlimg.resize((25, 25))
        self.imgytdl = ImageTk.PhotoImage(self.ytdlresize)
        Label(image=self.imgytdl,bg="#303135").place(x=410,y=12)

        self.cb = BooleanVar()
        self.ebdth = BooleanVar()
        self.sp = BooleanVar()
        

        self.info={}
        self.vidlst=[]
        self.audlst=[]
        self.caplst=[]
        self.mergedlst=[]
        self.plformat=['144p','240p','360p','480p','720p','1080p','best','Mp3 128K','Mp3 320K','M4a High','Wav',"Flac 24 bit Lossless"]
        self.refresh()

        if (len(args)>0):
            print(args)
            self.paste_args(self.url_box,args)


        
    def on_change(self,e1):
        inp = e1.get(1.0, "end-1c")
        s = inp.split('\n')
        print(len(s),s)
        self.plfrmtlabel.set('')
        self.plsilabel.set('')
        self.info={}
        self.vidlst=[]
        self.audlst=[]
        self.caplst=[]
        self.mergedlst=[]
        try:
            self.vid.destroy()
            self.aud.destroy()
            self.cap.destroy()
            self.mus.destroy()
            self.vidmerged.destroy()
            self.text_box.configure(state='normal')
            self.text_box.delete(1.0,"end")
            self.text_box.configure(state='disabled')
            self.clr1label.configure(cursor="",text="")
            self.clr2label.configure(cursor="",text="")
            self.clr3label.configure(cursor="",text="")
            self.out_conf.destroy()
            self.proxy.destroy()
            self.custom_name.destroy()
            self.starttime.destroy()
            self.endtime.destroy()
            self.ratelim.destroy()
            self.picbtn.destroy()
        except:
            pass
        try:
            self.check.destroy()
            self.th.destroy()
            self.spblock.destroy()
        except:
            pass
        self.vidlabel.set('')
        self.audlabel.set('')
        self.caplabel.set('')
        self.frmtlabel.set('')
        self.rlimlabel.set('')
        self.custlabel.set('')
        self.pxylabel.set('')
        self.mrglabel.set('')
        self.stlabel.set("")
        self.etlabel.set("")
        self.out_conf=ttk.Combobox(self.tab2, width="20", values=["auto-detect","mp4","mkv","webm"],state="readonly")
        self.out_conf.set("auto-detect")
        self.picbtn=ttk.Button(self, text = 'thumbnail')
        self.ratelim=ttk.Entry(self.tab2,width=26)
        self.custom_name=ttk.Entry(self.tab2,width=47)
        self.proxy=ttk.Entry(self.tab2,width=47)
        self.starttime=ttk.Entry(self.tab1,width=20)
        self.endtime=ttk.Entry(self.tab1,width=20)
        try:
            self.playselect.destroy()
            self.plitems.destroy()
        except:
            pass
        try:
            s.remove("")
        except:
            pass
        if s==[]:
            messagebox.showerror("Youtube-dl GUI","  Enter Valid URL  ")
        else:
            if len(s)==1:
                if "youtu" in s[0] and "playlist" not in s[0]:
                    tv2 = threading.Thread(target=self.srch, args=(s[0],))
                    tv2.start()
                elif "youtu" not in s[0]:
                    tv2 = threading.Thread(target=self.srch, args=(s[0],))
                    tv2.start()
                elif "youtu" in s[0] and "playlist" in s[0]:
                    self.tabControl.select(2)
                    tv2 = threading.Thread(target=self.plsrch, args=(s[0],))
                    tv2.start()
                    

    def paste2(self):
        try:
            AnnoyingWindow=Tk()
            ClipBoard = AnnoyingWindow.clipboard_get()
            AnnoyingWindow.destroy()
            self.ex.insert(END, " "+ClipBoard )
        except:
            AnnoyingWindow.destroy()
            messagebox.showerror("Youtube-dl GUI","URL should be in text")

    def clr2(self):
        self.ex.delete(0,END)
        self.text_area.delete(0.0,END)

    def openloc(self,event=None):
        if os.path.exists(self.e2.get().replace("/","\\")):
            subprocess.Popen(r'explorer /open, '+self.e2.get().replace("/","\\"))
        else:
            messagebox.showerror("Youtube-dl GUI","Path doesn't exist\nPath might be deleted or moved")

    def runcmd(self,cmd):
        startupinfo = subprocess.STARTUPINFO()
        self.text_area.delete(0.0,END)
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            self.tabControl.tab(self.tab6, text = '* Custom Exec')
            self.text_area.insert(END,line[0:-1]+"\n")
            self.text_area.see(END)
            if str(line)=="":
                break
        p.stdout.close()
        p.wait()
        self.tabControl.tab(self.tab6, text = ' Custom Exec ')
        messagebox.showinfo("Youtube-dl GUI","\nCommand Executed!")

    def custom(self,a=None):
        if len(self.ex.get())>0:
            t1w = threading.Thread(target=self.runcmd, args=(self.ex.get(),))
            t1w.start()
            
                
        elif len(self.ex.get())==0:
            messagebox.showerror("Youtube-dl GUI","Enter command")

    def clrtab3(self,event=None):
        self.playselect.set('')

    def clrtab2(self,event=None):
        self.ebdth.set(0)
        self.aud.set("")
        self.vid.set("")
        if self.cap.get()!='no captions available':
            self.cap.set("")
        self.proxy.delete(0,END)
        self.custom_name.delete(0,END)
        self.ratelim.delete(0,END)

    def clrtab1(self,event=None):
        self.vidmerged.set('')
        self.mus.set('')
        self.starttime.delete(0,END)
        self.endtime.delete(0,END)      
            
    def popenz(self,cmd):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        p = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            self.title("Youtube-dl GUI  [Downloading...]")
            self.status.set(line[0:-1])
            if str(line)=="":
                break
        p.stdout.close()
        p.wait()
        self.title("done")

    def popens(self,cmd):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
        return process.stdout.read()

    def viewer(self,img):
        t1w = threading.Thread(target=self.viewers, args=(img,))
        t1w.start()
        
    def viewers(self,img):
        img.show()

    def output_loc(self):
        self.e2 = Entry(self,bg="#A1A1A1",width=82,bd=0)
        file = open("./database/loc.txt",'r')
        a=file.readlines()
        print(a,len(a))
        if os.path.exists(a[0]):
            self.e2.insert(0,a[0])
            file.close()
        else:
            file.close()
            file=open("./database/loc.txt","w")
            print((os.environ['USERPROFILE']+"\\Downloads").replace("\\","/"))
            file.write((os.environ['USERPROFILE']+"\\Downloads").replace("\\","/"))#adding downloads path
            file.close()
            file = open("./database/loc.txt",'r')
            self.e2.insert(0,file.readlines()[0])
            file.close()
        
        self.loc()
        self.e2.place(relx=.292,rely=0.368,anchor=CENTER)
    

    def titlefind(self,infos):
        url=self.info['original_url']
        if "youtube" in url or "youtu." in url and "playlist" not in url:
            date=str(self.info['upload_date'])
            data=self.info['title']+"\n\nDuration: "+self.info['duration_string']+"  |  Channel: "+self.info['uploader']+"\n\nPublished on: "+date[:4]+"-"+date[4:6]+"-"+date[6:]+"  |  Views: "+str(self.info['view_count'])+"\n\nCategory : "+str(self.info['categories'][0])+"\n\nDescription\n"+self.info['description']
            self.text_box.configure(state='normal')
            self.text_box.delete(1.0,"end")
            self.text_box.insert(1.0, data)
            self.text_box.configure(state='disabled')
        else:
            try:
                data=self.info['title']+"\n\nDuration: "+self.info['duration_string']+"\n\nDescription\n"+self.info['description']
            except:
                data=self.info['title']+"\n\nDescription\n"+self.info['description']
            self.text_box.configure(state='normal')
            self.text_box.delete(1.0,"end")
            self.text_box.insert(1.0, data)
            self.text_box.configure(state='disabled')

    def thumbnail(self,url):
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
            image = img.resize((270, 160), Image.Resampling.LANCZOS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(self, image=image2)
            #picbtn=ttk.Button(root, text = 'thumbnail', image = image2,command=lambda : viewer(img))
            #self.picbtn.configure(image=image2)
            self.picbtn.configure(image=image2,command=lambda : self.viewer(img))
            self.picbtn.image=image2
            self.picbtn.place(x=724,y=55)
            
        elif "youtube" in url and "music" in url:
            if url.find("&")==-1:
                vid=url[1+url.find("="):]
            else:
                vid=url[1+url.find("="):url.find("&")]
            thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            image = img.resize((270, 160), Image.Resampling.LANCZOS)
            image2 = ImageTk.PhotoImage(image)
            panel = Label(self, image=image2)
            self.picbtn.configure(image=image2,command=lambda : self.viewer(img))
            self.picbtn.image=image2
            self.picbtn.place(x=724,y=55)
        elif "youtube" in url and "shorts" in url:
            vid=url.rstrip("?feature=share")[url.rstrip("?feature=share").rfind("/")+1:]
            thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            img.mode = 'RGB'
            image = img.resize((270, 160), Image.Resampling.LANCZOS)
            image2 = ImageTk.PhotoImage(image)#https://www.youtube.com/shorts/WSFe3Rp7arQ
            panel = Label(self, image=image2)
            self.picbtn.configure(image=image2,command=lambda : self.viewer(img))
            self.picbtn.image=image2
            self.picbtn.place(x=724,y=55)
        else:
            if 'thumbnail' in self.info:
                thurl=self.info['thumbnail']
            
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
                image = img.resize(((nw),(nh)), Image.Resampling.LANCZOS)
                image2 = ImageTk.PhotoImage(image)
                self.picbtn.configure(image=image2)
                self.picbtn.configure(command=lambda : self.viewer(img))
                self.picbtn.image=image2
                self.picbtn.place(x=sp+745,y=55)

    def size(self,n):
        if n//1024**2>=1 and n//1024**2<1024:
            a=str(round((n/1024**2),2))+" MB"
            return a
        elif n>=1024**3:
            a=str((round((n/1024**3),2)))+" GB"
            return a
        elif n//1024>=1 and n//1024<1024:
            a=str(round(n/1024,2))+" KB"
            return a

    def size2(self,n):
        if n<1024.00:
            a=str(n)+" Kb/s"
            return a
        elif n>1024.00:
            a=str(round(n/1024,2))+" Mb/s"
            return a

    def fps(self,r):
        #print("fps")
        if 'fps' in r and r['fps']!=None:
            return " |  FPS : "+str(r['fps'])+"  | "
        else:
            return ""

    def size_add(self,x):
        #print("size")
        if 'filesize' in x and x['filesize']!=None:
            sz=self.size(x['filesize'])
            return " |  Size : "+str(sz)+" "
        elif 'filesize_approx' in x and x['filesize_approx']!=None:
            sz=self.size(x['filesize_approx'])
            return " |  Size : "+str(sz)+" "
        else:
            return ""

    def btr(self,x):
        #print("btr")
        if 'tbr' in x and x['tbr']!=None:
            return " |  Bitrate : "+self.size2(x['tbr'])+" "
        else:
            return ""

    def format_note(self,x):
        #print("note")
        if 'format_note' in x:
            return " "+x['format_note']+" "
        else:
            return ""

    def ext(self,x):
        #print("ext")
        if 'ext' in x and x['ext']!=None:
            return " |  Ext : "+x['ext']+" "
        else:
            return ""

    def acodec(self,x):
        #print("acodec")
        if 'acodec' in x and x['acodec']!=None:
            return "  "+x['acodec']+" "
        else:
            return ""

    def vcodec(self,x):
        #print("vcodec")
        if 'vcodec' in x and x['vcodec']!=None:
            return "  "+x['vcodec']+" "
        else:
            return ""

    def fid(self,x):
        if 'format_id' in x:
            return "  "+x['format_id']
        else:
            return ""

    def plsrch(self,url):
        self.status.set(' Loading . . .')
        from pytube import Playlist
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

        data=str(title)+"\n"+"\nTotal no. of videos : "+str(p.length)+"\nViews : "+str(views)+"\n"+"\n\nDescription "+"\n"+str(desc)
        self.text_box.configure(state='normal')
        self.text_box.delete(1.0,"end")
        self.text_box.insert(1.0, data)
        self.text_box.configure(state='disabled')

        self.playselect = ttk.Combobox(self.tab3, width="30", values=self.plformat,state="readonly")
        self.playselect.place(x=200,y=60)

        self.plitems=ttk.Entry(self.tab3,width=33)
        self.plitems.place(x=200,y=130)
        self.plitems.insert(0,"1"+"-"+str(len(a)))
        self.plfrmtlabel.set('Select format')
        self.plsilabel.set('Select items')
        self.clr3label.configure(cursor="hand2",text="Clear selection")
        self.status.set('')

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
            image = img.resize((270, 160), Image.Resampling.LANCZOS)
            image2 = ImageTk.PhotoImage(image)
            self.picbtn.configure(image=image2)
            self.picbtn.configure(command=lambda : self.viewer(img))
            self.picbtn.image=image2
            self.picbtn.place(x=724,y=55)
        elif "music" in url and "youtube" in url:
            full=p.sidebar_info
            thurl=full[0]['playlistSidebarPrimaryInfoRenderer']['thumbnailRenderer']['playlistCustomThumbnailRenderer']['thumbnail']['thumbnails'][0]['url']
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            img.mode = 'RGB'
            image = img.resize((160, 160), Image.Resampling.LANCZOS)
            image2 = ImageTk.PhotoImage(image)
            self.picbtn.configure(image=image2)
            self.picbtn.configure(command=lambda : self.viewer(img))
            self.picbtn.image=image2
            self.picbtn.place(x=780,y=55)

    def isChecked(self):
        if self.cb.get()==1:
            self.mus['state']=NORMAL
            self.mus.configure(state="readonly")
            self.mus.focus_force()
            self.vidmerged['state']=DISABLED
            self.starttime['state']=DISABLED
            self.endtime['state']=DISABLED
        elif self.cb.get()==0:
            self.vidmerged['state']=NORMAL
            self.vidmerged.configure(state="readonly")
            self.starttime['state']=NORMAL
            self.endtime['state']=NORMAL
            self.vidmerged.focus_force()
            self.mus['state']=DISABLED

    def browse_file(self):
        self.dir=filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        if self.dir=="":
            file = open("./database/loc.txt",'r')
            self.dir=file.readlines()[0]
            file.close()
        self.e2.delete(0,END)
        self.e2.insert(0,self.dir)
        file = open("./database/loc.txt",'w+')
        file.write(self.dir)
        file.close()
        self.loc()

    def loc(self):
        self.output_dir=self.e2.get()
        user=os.environ['USERPROFILE']
        user =user.replace("\\","/")
        self.output_dir=self.output_dir.replace("\\","/")
        if user in self.output_dir:
            self.output_dir="/"+self.output_dir.lstrip(user)
            #print(self.output_dir)
            return self.output_dir
        else:
            #print(self.output_dir)
            return self.output_dir
        

    def srch(self,url):
        ydl_opts = {}
        d=""
        cur=""

        self.status.set(' Loading . . .')
        try:
            with YoutubeDL(ydl_opts) as ydl:
                self.info = ydl.extract_info(url, download=False)
            tv1 = threading.Thread(target=self.thumbnail, args=(url,))
            tv1.start()
            tv2 = threading.Thread(target=self.titlefind, args=(self.info,))
            tv2.start()
        except:
            self.status.set(" Website not supported")
        if self.info!={}:
            self.status.set("")
            try:
                r=self.info['formats']
                print(len(r))
                for i in range(0,len(r)):
                    if r[i]['resolution']!="audio only" and r[i]['audio_ext']!='none' and (r[i]['ext']=='m4a' or r[i]['ext']=='webm') or r[i]['audio_ext']!='none':
                        cur="  "+self.format_note(r[i])+self.size_add(r[i])+self.ext(r[i])+self.acodec(r[i])+self.btr(r[i])+self.fid(r[i])
                        self.audlst.append(cur)
                    elif  r[i]['ext']=="mp4" or r[i]['ext']=="webm" or r[i]['ext']=='3gp':
                        cur="  "+self.format_note(r[i])+self.size_add(r[i])+self.ext(r[i])+self.vcodec(r[i])+self.btr(r[i])+self.fps(r[i])+self.fid(r[i])
                        #cur="  "+r[i]['format_note']+"  |  Size "+sz+" |  Ext : "+r[i]['ext']+"  "+r[i]['vcodec']+"  | "+r[i]['resolution']+self.fps(r[i])+" |  Bitrate : "+sz2+"  |  " +r[i]['format_id']
                        self.vidlst.append(cur)
                    if r[i]['acodec']!='none' and r[i]['vcodec']!='none':
                        self.mergedlst.append("  "+self.format_note(r[i])+self.size_add(r[i])+self.ext(r[i])+self.fps(r[i])+"   Resolution  "+r[i]['resolution']+"  |  id "+r[i]['format_id'])
            except:
                try:
                    t=self.info['entries'][0]['formats']
                    print(len(t))
                    for i in range(0,len(t)):
                        if t[i]['resolution']=='audio only':
                            cur=self.format_note(t[i])+self.size_add(t[i])+self.ext(t[i])+self.acodec(t[i])+self.btr(t[i])+"  | "+t[i]['protocol']+" "+self.fid(t[i])
                            #cur=(t[i]['format_id']+" "+t[i]['ext']+" "+t[i]['protocol'])
                            self.audlst.append(cur)
                        elif t[i]['resolution']!='audio only':
                            cur=self.format_note(t[i])+self.size_add(t[i])+self.ext(t[i])+self.vcodec(t[i])+self.btr(t[i])+"  | "+t[i]['protocol']+" "+self.fid(t[i])
                            self.vidlst.append(cur)
                except:
                    r=self.info['formats']
                    for i in range(0,len(r)):
                        if 'vcodec' in r[i] and (r[i]['vcodec']=='none' or r[i]['vcodec']==None):
                            cur="  "+self.format_note(r[i])+self.size_add(r[i])+self.ext(r[i])+self.vcodec(r[i])+self.btr(r[i])+self.fps(r[i])+self.fid(r[i])
                            self.vidlst.append(cur)
                        elif 'acodec' in r[i] and (r[i]['acodec']=='none' or r[i]['acodec']==None):
                            cur="  "+self.format_note(r[i])+self.size_add(r[i])+self.ext(r[i])+self.acodec(r[i])+self.btr(r[i])+self.fid(r[i])
                            self.audlst.append(cur)

            if 'subtitles' in self.info and "youtu" in url:
                for i in self.info['subtitles']:
                    if 'name' in self.info['subtitles'][i][0]:
                        self.caplst.append("  "+str(i)+"    "+str(self.info['subtitles'][i][0]['name']))

                            
                #print(self.info['entries'][0]['formats'][1]['format_id'])
            if len(self.caplst)==0:
                self.caplst.append("no captions available")

        #print(len(self.vidlst),len(self.audlst))
        self.vid = ttk.Combobox(self.tab2, width="95", values=self.vidlst,state="readonly")
        self.vid.place(x=20,y=32)
        self.aud = ttk.Combobox(self.tab2, width="95", values=self.audlst,state="readonly")
        self.aud.place(x=20,y=79)
        self.cap = ttk.Combobox(self.tab2, width="40", values=self.caplst,state="readonly")
        self.cap.place(x=20,y=127)
        self.mus = ttk.Combobox(self.tab1, width="40", values=['Mp3 64K','Mp3 128K','Mp3 320K','M4a High','Wav Lossless','Flac Lossless'],state="readonly")
        self.mus['state']=DISABLED
        self.mus.place(x=200,y=150)
        self.cb.set(0)
        self.check=ttk.Checkbutton(self.tab1,text="Convert to music", var=self.cb, onvalue=True, offvalue=False, command=self.isChecked)
        self.check.place(x=195,y=125)
        self.th=ttk.Checkbutton(self.tab2,text="Embed thumbnail", var=self.ebdth, onvalue=True, offvalue=False)
        self.th.place(x=20,y=205)
        self.spblock=ttk.Checkbutton(self.tab2,text="Sponserblock", var=self.sp, onvalue=True, offvalue=False)
        self.spblock.place(x=250,y=205)
        if self.caplst[0]=='no captions available':
            self.cap.set(self.caplst[0])

        if len(self.mergedlst)!=0:
            self.mergedlst.append("best available")

        

        self.vidmerged=ttk.Combobox(self.tab1, width="95", values=self.mergedlst,state="readonly")
        if len(self.mergedlst)==0:
            self.mergedlst.append(" Check advanced option")
            self.vidmerged.set(" Check advanced option")
        self.vidmerged.place(x=20,y=40)
        
            
        self.out_conf.place(x=295,y=127)
        self.proxy.place(x=325,y=176)
        self.custom_name.place(x=20,y=176)
        self.ratelim.place(x=452,y=127)
        self.starttime.place(x=170,y=90)
        self.endtime.place(x=370,y=90)

        self.vidlabel.set('Video Streams')
        self.audlabel.set('Audio Streams')
        self.caplabel.set('Captions')
        self.frmtlabel.set('Format')
        self.rlimlabel.set('Rate limit (eg. 40K/4.2M)')
        self.custlabel.set('Custom filename')
        self.pxylabel.set('Proxy URL')
        self.mrglabel.set('Select video quality')
        self.stlabel.set("Start time")
        self.etlabel.set("End time")
        self.clr1label.configure(cursor="hand2",text="Clear selection")
        self.clr2label.configure(cursor="hand2",text="Clear selection")
        self.dwbtn=Button(image=self.dwpic, command=lambda: self.download_1(url) ,bd=0,relief="flat",bg="#202020",activebackground="#202020",highlightthickness = 0,cursor="hand2")
        self.dwbtn.bind('<Enter>',lambda a: self.changer_red(self.dwbtn,self.dwpicdark))
        self.dwbtn.bind('<Leave>',lambda a: self.changer_blue(self.dwbtn,self.dwpic))
        self.dwbtn.place(x = 820,y = 543)
        

    def paste(self,e1):
        #print(self,e1)
        try:
            Clipper=Tk()
            ClipBoard = Clipper.clipboard_get()
            Clipper.destroy()
            r=len(e1.get(1.0, "end-1c"))
            if r==0:
                ele=ClipBoard
                #e1.insert(0, ele )
                e1.insert(1.0, ele)
            else:
                ele="\n"+ClipBoard
                e1.insert(float(r), ele )
        except:
            AnnoyingWindow.destroy()
            messagebox.showerror("Youtube-dl GUI","URL should be in text")

    def on_closing(self):
        if messagebox.askokcancel("Youtube-dl GUI", "Do you want to quit?"):
            self.destroy()

    def download_1(self,url):
        
        tb1mus = self.mus.get()
        tb1stime = self.starttime.get()#starttime
        tb1etime = self.endtime.get()#endtime
        tb1merged = self.vidmerged.get()
        tb2vid = self.vid.get()
        tb2cap = self.cap.get()
        tb2aud = self.aud.get()
        tb2prxy = self.proxy.get()
        tb2rtlim = self.ratelim.get()
        tb2embdth = self.cb.get()
        tb2cust = self.custom_name.get()
        tb2frmt = self.out_conf.get()

        if self.cap.get()=='no captions available':
            tb2cap = ""
        if tb1merged==" Check advanced option":
            tb1merged=""

        if tb2cust!="":
            tb2cust=tb2cust.replace("?","_")
            tb2cust=tb2cust.replace("<","_")
            tb2cust=tb2cust.replace(">","_")
            tb2cust=tb2cust.replace("|","_")
            tb2cust=tb2cust.replace(":","_")
            tb2cust=tb2cust.replace("*","_")
            tb2cust=tb2cust.replace("/","_")
            tb2cust=tb2cust.replace("\\","_")
            dir_ = "~"+self.output_dir+"/"+tb2cust+".%(ext)s"

        else:
            dir_ = "~"+self.output_dir+"/"+"%(title)s.%(ext)s"
        b=0

        print(tb2vid,tb2aud,tb1mus,tb2cap,tb1merged)

        if tb2vid=="" and tb2aud=="" and tb1mus=="" and tb2cap=="" and tb1merged=="":
            messagebox.showerror("Youtube-dl GUI","Select Audio/Video/Music stream")

        elif tb2vid=="" and tb2aud=="" and tb1mus!="" and tb2cap=="" and tb1merged=="":#['Mp3 64K','Mp3 128K','Mp3 320K','M4a High','Wav Lossless','Flac Lossless']
            if tb1mus=="Mp3 64K":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime -f ba -x --audio-format mp3 --audio-quality 64K -o \"{}\" '+url).format(dir_)
            elif tb1mus=="Mp3 128 kbps":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format mp3 --audio-quality 128K -o \"{}\" '+url).format(dir_)
            elif tb1mus=="Mp3 320K":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format mp3 --audio-quality 320K -o \"{}\" '+url).format(dir_)
            elif tb1mus=="M4a High":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format m4a --audio-quality 0  -o \"{}\" '+url).format(dir_)
            elif tb1mus=="Wav Lossless":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format wav --audio-quality 0 -o \"{}\" '+url).format(dir_)
            elif tb1mus=="Flac 24 bit Lossless":
                b=('yt-dlp_x86  --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --embed-thumbnail --no-mtime -f ba -x --audio-format flac --audio-quality 0 -o \"{}\" '+url).format(dir_)

        elif tb2vid!="" and tb2aud!="" and tb1mus=="" and tb2cap=="" and tb1merged=="" and tb1stime=="" and tb1etime=="" :
            print("ET$^TEFD")
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\"  --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {}+{} -o \"{}\" "+url).format(tb2vid.split()[-1],tb2aud.split()[-1],dir_)

        elif tb2vid!="" and tb2aud=="" and tb1mus=="" and tb2cap=="" and tb1merged=="" and tb1stime=="" and tb1etime=="":
            print("#$%TEFD")
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {} -o \"{}\" "+url).format(tb2vid.split()[-1],dir_)

        elif tb2vid!="" and tb2aud!="" and tb1mus=="" and tb2cap!="" and tb1merged=="" and tb1stime=="" and tb1etime=="":
            print("Fhfgffz")
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --write-srt --sub-lang {} --add-metadata --no-mtime --embed-metadata -f {}+{} -o \"{}\" "+url).format(tb2cap.split()[0],tb2vid.split()[-1],tb2aud.split()[-1],dir_)
            
        elif tb2vid=="" and tb2aud=="" and tb1mus=="" and tb2cap=="" and tb1merged!="" and tb1merged!='best available' and tb1stime=="" and tb1etime=="":
            print("hfdghdfghdg")
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {} -o \"{}\" "+url).format(tb1merged.split()[-1],dir_)
            
        elif tb2vid=="" and tb2aud=="" and tb1mus=="" and tb2cap=="" and tb1merged!="" and tb1merged=='best available':
            print("fghfdg")
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f bv+ba -o \"{}\" "+url).format(dir_)

        elif tb1stime!="" and tb1etime!="" and tb1merged!="" and tb2cap=="" and tb1mus=="" and tb2vid=="" and tb2aud=="":
            b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {} -o \"{}\" --download-sections \"{}\" "+url).format(tb1merged.split()[-1],dir_,"*"+str(tb1stime)+"-"+str(tb1etime))
            print(b,"ece")

        #elif tb1stime!="" and tb1etime!="" and tb1merged=="" and tb2cap=="" and tb1mus=="" and tb2vid!="" and tb2aud!="":
            #b=("yt-dlp_x86 --parse-metadata \"description:(?s)(?P<meta_comment>.+)\" --parse-metadata \"uploader:(?s)(?P<meta_album_artist>.+)\" --parse-metadata \"%(upload_date,release_year).4s:(?P<meta_date>.+)\" --add-metadata --no-mtime --embed-metadata -f {}+{} -o \"{}\" --download-sections \"{}\" "+url).format(tb2vid.split()[-1],tb2aud.split()[-1],dir_,"*"+str(tb1stime)+"-"+str(tb1etime))
            #print(b,"ece2")  ___________________________________________________separate video ,audio not working_________________________________________________
            
        if b:
            self.cmd=b
            self.dwstate="Downloading"
            tv2w = threading.Thread(target=self.run_command1, args=(b,))
            tv2w.start()

    def run_command1(self,cmd):
        self.status.set("")
        if self.dwstate=="Paused":
            self.dwstate="Downloading"
            self.pausebtn.config(image=self.pausepic, command = lambda: self.pause(self.cmd))
            self.status.set(" Resuming download")
        self.pausebtn.config(image=self.pausepic, command = lambda: self.pause(self.cmd))
        file2=open(os.getcwd()+"\\database\\cookies.txt",'r')
        if len(file2.readlines())!=0:
            cmd=cmd+" --cookies "+file2.readlines()[0]
        file2.close()
        file3=open(os.getcwd()+"\\database\\args.txt",'r')
        if len(file3.readlines())!=0:
            cmd=cmd+" "+file3.readlines()[0]
        file3.close()
        self.dwbtn['state']=DISABLED

        self.cancelbtn.place(x = 915,y = 543)
        self.pausebtn.place(x = 730,y = 543)

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True, bufsize=1)
        print(p.pid)
        for line in iter(p.stdout.readline, b''):
            self.title("Youtube-dl GUI  [Downloading...]")
            self.status.set(" "+line[0:-1]+"                                                                                                                                                                                                           ")
            if str(line)=="":
                break
        p.stdout.close()
        p.wait()
        if self.dwstate=="Downloading":
            self.status.set(" Download Complete")
            self.title("Youtube-dl GUI")
            self.dwbtn['state']=NORMAL
            self.cancelbtn.place(x = 1915,y = 1543)
            self.pausebtn.place(x = 1915,y = 1543)
            self.history()
            if len(self.custom_name.get())!=0:
                messagebox.showinfo("Youtube-dl GUI", self.custom_name.get()+"\nDownload complete")
            else:
                messagebox.showinfo("Youtube-dl GUI", self.info['title']+"\nDownload complete")
            
        elif self.dwstate=="Cancelled":
            self.title("Youtube-dl GUI")
            self.status.set(" Download Cancelled")
        elif self.dwstate=="Paused":
            self.title("Youtube-dl GUI")
            self.status.set(" Download Paused")


    def cancel(self):
        self.dwstate="Cancelled"
        current_process = psutil.Process()
        children = current_process.children(recursive=True)
        for child in children:
            print('Child pid is {}'.format(child.pid))
            subprocess.Popen("taskkill /F /PID "+str(child.pid),shell=True)
        t=time.time()
        if len(self.custom_name.get())!=0:
            name=self.custom_name.get()
        else:
            name=self.info['title']
            name=name.replace("|","｜")
            name=name.replace("?","？")
        count=0
        print(os.listdir(self.e2.get()))
        for i in range(0,len(os.listdir(self.e2.get()))):
            if ".part" in os.listdir(self.e2.get())[i]:
                print(os.listdir(self.e2.get())[i])
                if ( t - os.path.getmtime(self.e2.get()+"/"+os.listdir(self.e2.get())[i])<=5 ) and name in os.listdir(self.e2.get())[i] and count<=3:
                    if os.path.exists(os.listdir(self.e2.get())[i]):
                        os.remove(self.e2.get()+"/"+os.listdir(self.e2.get())[i])
                        count+=1
        self.status.set(" Download Cancelled")
        self.dwbtn['state']=NORMAL
        self.cancelbtn.place(x = 1915,y = 1543)
        self.pausebtn.place(x = 1915,y = 1543)

    def pause(self,cmd):
        self.dwstate="Paused"
        current_process = psutil.Process()
        children = current_process.children(recursive=True)
        self.pausebtn.config(image=self.resumepic, command = lambda: self.run_command1(self.cmd))
        for child in children:
            print('Child pid is {}'.format(child.pid))
            subprocess.Popen("taskkill /F /PID "+str(child.pid),shell=True)
        self.status.set(" Download Paused")

    def history(self):
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        url=self.url_box.get(1.0, "end-1c")
        try:
            title=self.info['title']
        except:
            if len(self.custom_name.get())!=0:
                title=self.custom_name.get()
            else:
                title=""
        file4=open(".\\database\\history.txt",'a')
        location=self.e2.get()
        log=title+"^"+url+"^"+dt_string+"^"+location+"^"+"\n"
        try:
            file4.write(log)
        except:
            pass
        file4.close()
        self.refresh()

    def clearhistory(self):
        answer = messagebox.askquestion('Youtube-dl GUI','Are you sure that you want to clear history?')
        if answer=="yes":
            file4=open("./database/history.txt",'w+')
            file4.write("")
            file4.close()
            self.refresh()

    def sel(self,a):
        selected=self.my_game.focus()
        val=self.my_game.item(selected,'values')
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

    def cl2(self,a):
        selected=self.my_game.focus()
        val=self.my_game.item(selected,'values')
        print(val)
        files=os.listdir(val[3])
        for i in range(0,len(files)):
            if val[0] in files[i]:
                print(val[-1]+"/"+files[i])
                try:#bug : work for ascii filenames
                    if ".vtt" not in files[i]:
                        d=val[-1]+"/"+files[i]
                        d=d.replace("/","\\")
                        s=r'explorer /select, "{}" '.format(d)
                        print(s)
                        subprocess.Popen(s)
                        break
                except:
                    messagebox.showerror("Youtube-dl GUI","File not found")
                    break

    def refresh(self):
        try:
            self.my_game.destroy()
            self.verscrlbar.destroy()
        except:
            pass
        self.my_game = ttk.Treeview(self.tab7,height=9)
        self.my_game.bind("<Double-Button-1>", lambda g: self.sel(self.my_game))
        self.my_game.bind('<Button-3>', lambda g: self.cl2(self.my_game))
        self.verscrlbar = ttk.Scrollbar(self.tab7,orient ="vertical",command = self.my_game.yview)
        self.verscrlbar.pack(side ='right', fill ='x')
        self.my_game.configure(xscrollcommand = self.verscrlbar.set)
        self.my_game['columns'] = ('Title', 'URL', 'Date time', 'Location')
        self.my_game.column("#0", width=0,  stretch=NO)
        self.my_game.column("Title",anchor=CENTER, width=210)
        self.my_game.column("URL",anchor=CENTER,width=150)
        self.my_game.column("Date time",anchor=CENTER,width=130)
        self.my_game.column("Location",anchor=W,width=130)
        self.my_game.heading("#0",text="",anchor=CENTER)
        self.my_game.heading("Title",text="Title",anchor=CENTER)
        self.my_game.heading("URL",text="URL",anchor=CENTER)
        self.my_game.heading("Date time",text="Date time",anchor=CENTER)
        self.my_game.heading("Location",text="Location",anchor=CENTER)
        file4=open("./database/history.txt",'r')
        log=file4.readlines()
        file4.close()
        self.my_game.pack()
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
                self.my_game.insert(parent='',index='end',iid=i,text='',values=(zc,zv,zb,zn))
        

    def paste_args(self,e1,s):
        p=""
        if ".txt" in s[0][1]:
            r=open(s[0][1],"r")
            t=r.readlines()
            r.close()
            for i in range(0,len(t)):
                if "https" in t[i]:
                    p=p+t[i]
        else:
            for i in range(1,len(s[0])):
                if len(s[0][i])!=0:
                    p=p+s[0][i]+'\n'
        #e1.insert(0, ele )
        if p!="":
            e1.insert(1.0, p)
            self.on_change(self.url_box)

    def clr(self,e1):
        e1.delete(1.0,"end")

    def changer_red(self,b,a):
        b.config(image=a)
        
    def changer_blue(self,b,a):
        b.config(image=a)

    def open_window(self):
        window = Window(self)
        window.grab_set()

    def open_settings(self):
        window = Settings(self)
        window.grab_set()


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.focus_force()
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        y=int((self.sh-500)/2)-30
        x=int((self.sw-600)/2)
        self.geometry('%dx%d+%d+%d' % (600, 500, x, y))
        self.title('About Youtube-dl GUI')
        self.configure(bg='#303135')
        self.image = Image.open("./images/logo.png")
        self.resize_image = self.image.resize((200, 200))
        self.img = ImageTk.PhotoImage(self.resize_image)
        streams = tk.Label(master=self, text = "",image=self.img,bg="#303135",font=('Arial', 16),fg="white").place(relx=0.5, rely=0.25,anchor= CENTER)
        streams2 = Label(self, text = "Youtube-dl GUI  v22.1002.19",bg="#303135",font=('Arial', 12),fg="white").place(relx=.5, rely=.5,anchor= CENTER)
        streams2 = Label(self, text = "Released under MIT License",bg="#303135",fg="white").place(relx=.5, rely=.56,anchor= CENTER)
        streams2 = Label(self, text = "This is project is based on yt-dlp , ffmpeg , atomic parsley",bg="#303135",fg="white").place(relx=.5, rely=.69,anchor= CENTER)
        streams3 = Label(self, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 9,'bold'),fg="red",bg="#303135").place(relx=.5, rely=.75,anchor= CENTER)
        name74 = Label(self, text = "CREDITS :",bg="#303135",fg="white").place(x=40+70,y=290)
        name74 = Label(self, text = "yt-dlp",bg="#303135",fg="#0574FF",cursor="hand2")
        name74.place(x = 135+85,y = 290)
        name74.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/yt-dlp/yt-dlp'))
        name73 = Label(self, text = "ffmpeg",fg="#0574FF",cursor="hand2",bg="#303135")
        name73.place(x = 210+95,y = 290)
        name73.bind("<Button-1>", lambda e: webbrowser.open('https://www.ffmpeg.org/'))
        name75 = Label(self, text = "AtomicParsley",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 290+105,y = 290)
        name75.bind("<Button-1>", lambda e: webbrowser.open('http://atomicparsley.sourceforge.net/'))
        name76 = Label(self, text = "TELEGRAM",fg="orange",cursor="hand2",bg="#303135")
        name76.place(x = 190+145,y = 390)
        name76.bind("<Button-1>", lambda e: webbrowser.open('https://t.me/ytdlgui'))
        name77 = Label(self, text = "DONATE",fg="yellow",cursor="hand2",bg="#303135")
        name77.place(x = 190,y = 390)
        name77.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl#support-us'))
        name7e = Label(self, text = "Changelog",fg="#0574FF",cursor="hand2",bg="#303135")
        name7e.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/releases/tag/v22.0808.19'))
        name7e.place(x = 195,y = 315)
        name8e = Label(self, text = "Check for updates",fg="#0574FF",cursor="hand2",bg="#303135")
        name8e.bind("<Button-1>", lambda e: os.startfile("updater.exe"))
        name8e.place(x = 295,y = 315)
        streams2 = Label(self, text = "https://github.com/sourabhkv/ytdl",bg="#303135",fg="white").place(relx=.5, rely=.87,anchor= CENTER)
        streams2 = Label(self, text = "Developed by sourabhkv",bg="#303135",fg="green").place(relx=.5, rely=.93,anchor= CENTER)
        self.resizable(False, False)
        self.iconbitmap(r'logo.ico')

class Settings(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.focus_force()
        self.configure(bg='#303135')
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        y=int((self.sh-500)/2)-30
        x=int((self.sw-500)/2)
        self.geometry('%dx%d+%d+%d' % (500, 500, x, y))
        self.title('Youtube-dl GUI  Settings')
        Label(self, text = "Settings",font=('Arial', 16),bg="#303135",fg="white").place(relx=0.5, rely=0.05,anchor= CENTER)
        Label(self, text = "Default Download Options",bg="#303135",fg="white").place(relx=0.5, rely=0.12,anchor= CENTER)
        Label(self, text = "Path to Cookie file",bg="#303135",fg="white").place(relx=0.5, rely=0.28,anchor= CENTER)
        Label(self, text = "Output template for video",bg="#303135",fg="white").place(relx=0.5, rely=0.44,anchor= CENTER)
        Label(self, text = "Output template for playlist",bg="#303135",fg="white").place(relx=0.5, rely=0.56,anchor= CENTER)
        Label(self, text = "Multi video options",bg="#303135",fg="white").place(relx=0.5, rely=0.7,anchor= CENTER)
        dd=Label(self, text = "Update  yt-dlp",fg="#0574FF",cursor="hand2",bg="#303135")
        dd.place(x = 390,y = 460)
        #dd.bind("<Button-1>", lambda e: updateback())
        name75 = Label(self, text = "Report issue",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 15,y = 460)
        name75.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/issues'))
    
        ttk.Button(self, text ="Save", command = self.save).place(relx=0.5, rely=0.89,anchor= CENTER)
        file2=open("./database/cookies.txt",'r')
        data1=file2.readlines()
        file2.close()
        file3=open("./database/args.txt",'r')
        data2=file3.readlines()
        file3.close()
        file4=open("./database/output_temp_vid.txt",'r')
        out_temp_vid=file4.readlines()
        file4.close()
        file5=open("./database/output_temp_playlist.txt",'r')
        out_temp_plst=file5.readlines()
        file5.close()
        self.video=ttk.Combobox(self, width="20", values=["144p","240p","360p","480p","720","1080p"],state="readonly")
        file8=open("./database/multivideo.txt","r")
        
        r=file8.readlines()
        self.video.set(r[0][:-1])
        self.video.place(x=100,y=370)
        self.audio=ttk.Combobox(self, width="20", values=["ba","wa"],state="readonly")
        self.audio.set(r[-1])
        self.audio.place(x=270,y=370)
        file8.close()

        
        
        self.optnentry=ttk.Entry(self,width=74)
        self.cookiepath=ttk.Entry(self,width=71)
        self.out_vid=ttk.Entry(self,width=74)
        self.out_plst=ttk.Entry(self,width=74)
        
        if len(data2)!=0:
            self.optnentry.insert(0,data2[0])
        elif len(data1)!=0:
            self.cookiepath.insert(0,data1[0])
        
        self.out_plst.insert(0,out_temp_plst[0])
        self.out_plst.place(x=20,y=300)
        self.out_vid.insert(0,out_temp_vid[0])
        self.out_vid.place(x=20,y=240)
    
        self.optnentry.place(x=20,y=78)
    #cookiepath.insert(0,data3)
        self.cookiepath.place(x=20,y=158)
        Button(self, text =".", command = self.cookieselect).place(x=455,y=156)
        self.resizable(False, False)
        self.iconbitmap(r'logo.ico')
        
    def cookieselect(self):
        r = filedialog.askopenfilename()
        self.cookiepath.delete(0,END)
        self.cookiepath.insert(0,r)
        self.focus_force()

    def save(self):
        c1=self.optnentry.get()
        c2=self.cookiepath.get()
        c3=self.out_vid.get()
        c4=self.out_plst.get()
        file2=open("./database/cookies.txt",'w+')
        file2.write(c2)
        file2.close()
        file3=open("./database/args.txt",'w+')
        file3.write(c1)
        file3.close()
        file4=open("./database/output_temp_vid.txt",'w+')
        file4.write(c3)
        file4.close()
        file4=open("./database/output_temp_playlist.txt",'w+')
        file4.write(c4)
        file4.close()
        file8=open("./database/multivideo.txt","w+")
        file8.write(self.video.get()+"\n"+self.audio.get())
        file8.close()
        self.destroy()
        messagebox.showinfo("Youtube-dl GUI", "Settings saved!")

        

if __name__ == "__main__":
    s=__file__[:__file__.rfind("\\")]+"\\database"
    if os.path.exists(s):
        pass
    else:
        os.makedirs(s,exist_ok=False)
        os.makedirs(s+"\\update",exist_ok=False)
        file = open(s+"\\loc.txt",'w+')
        file.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
        file.close()
        file2=open(s+"\\cookies.txt",'w+')
        file2.close()
        file3=open(s+"\\args.txt",'w+')
        file3.close()
        file4=open(s+"\\history.txt",'w+')
        file4.close()
        file5=open(s+"\\log.txt",'w+')
        file5.write(str(time.time()))
        file5.close()
        file6=open(s+"\\output_temp_vid.txt",'w+')
        file6.write("%(title)s.%(ext)s")
        file6.close()
        file7=open(s+"\\output_temp_playlist.txt",'w+')
        file7.write("%(playlist_title)s %(playlist_index)s %(title)s.%(ext)s")
        file7.close()
        file8=open(s+"\\multivideo.txt","w+")
        file8.write("360p\nwa")
        file8.close()
        
    lst=sys.argv
    print(lst,type(lst))
    if len(lst)==2 and ".txt" in lst[1]:
        app = App(lst)
        app.mainloop()
    elif len(lst)>1:
        app = App(lst)
        app.mainloop()
    else:
        app = App()
        app.mainloop()
