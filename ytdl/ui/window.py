import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
from tkinter import scrolledtext
import tkinter.font as tkFont
from .about import About
from .pipe import Pipe
import webbrowser
import subprocess
import threading
import os
from .settings import Settings

class Window:
    def __init__(self,args):

        # initial setup of window
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        _y=int((self.screen_height-640)/2)
        _x=int((self.screen_width-1000)/2)
        self.root.geometry('%dx%d+%d+%d' % (1030, 580, _x, _y))
        self.root.title('YouTube-dl GUI')
        self.root.iconbitmap('./ytdl/images/logo.ico')
        
        self.root.resizable(False,False)

        # style
        self.root.configure(bg='#303135')
        self.style= ttk.Style()
        self.style.configure('TCombobox', fieldbackground= '#525252', background= '#525252',foreground='black')
        self.style.configure('TButton',background='#525252')
        self.style.configure('TScrollbar',background='#525252',activebackground='#525252')
        self.style.configure('TNotebook', background='#424242',borderwidth=0)
        self.style.configure('TCheckbutton', background='#525252',foreground='white',activebackground='#525252',borderwidth=0)
        self.style.layout("TNotebook", [])


        # frame1 newer
        self.md=PhotoImage(file = './ytdl/images/Frame 1newer.png')
        self.canvas1 = Canvas( self.root, width = 560,height = 1000)
        background_label = Label(image=self.md,anchor='n')
        background_label.place(x=0, y=-2, relwidth=1, relheight=1)
        self.canvas1.pack()

        # tab control
        self.tabControl = ttk.Notebook(self.root,height=236,width=624)
        self.tab1 = Frame(self.tabControl,background='#525252')
        self.tab2 = Frame(self.tabControl,background='#525252')
        self.tab3 = Frame(self.tabControl,background='#525252')
        self.tab4 = Frame(self.tabControl,background='#525252')
        self.tab5 = Frame(self.tabControl,background='#525252')
        self.tab6 = Frame(self.tabControl,background='#525252')
        self.tab7 = Frame(self.tabControl,background='#525252')

        self.tabControl.add(self.tab1, text ='  Basic  ')
        self.tabControl.add(self.tab2, text ='  Advanced ')
        self.tabControl.add(self.tab3, text ='  Playlist  ')
        self.tabControl.add(self.tab4, text =' Multi video ')
        self.tabControl.add(self.tab5, text ='  Converter ')
        self.tabControl.add(self.tab6, text ='  Custom command ')
        self.tabControl.add(self.tab7, text =' History ')
        self.tabControl.place(x=35,y=215)#275


        Label(self.root, text = 'Youtube-dl GUI',bg='#303135',font=('Arial', 18),fg='white').place(x = 230,y = 10)
        _logo_image =  Image.open('./ytdl/images/logo.png')
        _resize_image = _logo_image.resize((25, 25))
        _img = ImageTk.PhotoImage(_resize_image)
        _label1 = Label(self.root, image=_img,bg='#303135')
        _label1.image = _img
        _label1.place(x=410,y=10)

        _explore = Label(self.root, text = 'Explore  ytdl  Unlocked',fg='yellow',cursor='hand2',bg='#303135')
        _explore.place(x = 530,y = 20)
        _explore.bind('<Button-1>', lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/blob/main/README.md#ytdl-unlocked-pro'))


        # statusbar
        self.status = StringVar()
        self.status.set('')
        self.statusbar = tk.Label(self.root, textvariable=self.status ,width=150, bd=2,fg='white', relief=tk.SUNKEN, anchor=tk.W,bg='#202125')
        self.statusbar.place(x=-1,y=560)

        # url textfield
        self.url_box = Entry(self.root,bg='#A1A1A1',width=80,bd=0,fg='black')
        if len(args)>=2:
            temp_args = args[1:]
            self.url_box.insert(END," ".join(temp_args))
        self.url_box.place(x=60,y=103)

        # URL text
        self._URL_text_var = StringVar()
        self._URL_text_var.set("URL")
        self._url_label = Label(self.root, textvariable = self._URL_text_var ,bg="#424242",fg="white")
        self._url_label.place(x = 55,y = 76)

        # Output text
        self._output_text_var = StringVar()
        self._output_text_var.set("Output")
        self._output_label = Label(self.root, textvariable = self._output_text_var,bg="#424242",fg="white",cursor='hand2')
        self._output_label.bind('<Enter>',lambda a: self._output_label.config(fg="#0574FF"))
        self._output_label.bind('<Leave>',lambda a: self._output_label.config(fg="white"))
        self._output_label.bind("<Button-1>", lambda e: self.open_dir())
        self._output_label.place(x = 55,y = 148)

        # location field
        self.location_box = Entry(self.root,bg='#A1A1A1',width=80,bd=0,fg='black')
        with open('./ytdl/config/loc.txt') as file:
            self.download_Directory = file.readlines()[0]
        self.location_box.insert(0,self.download_Directory)
        self.location_box.place(x=60,y=179)

        # go button
        self.go_button_image = PhotoImage(file = './ytdl/images/go.png')
        self.go_button_red_image = PhotoImage(file = './ytdl/images/gored.png')
        self.go_button = Button(self.root,text='GO',bd=0,image=self.go_button_image,command=lambda: self.on_change(),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.go_button.bind('<Enter>',lambda a:self.color_changer(self.go_button, self.go_button_red_image))
        self.go_button.bind('<Leave>',lambda a:self.color_changer(self.go_button, self.go_button_image))
        self.go_button.place(x=570,y=96)

        # paste button
        self.paste_button_image = PhotoImage(file = './ytdl/images/paste.png')
        self.paste_button_red_image = PhotoImage(file = './ytdl/images/pastered.png')
        self.paste_button = Button(self.root,text='Paste',bd=0,image=self.paste_button_image,command=lambda: self.paste_on_text(),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.paste_button.bind('<Enter>',lambda a:self.color_changer(self.paste_button, self.paste_button_red_image))
        self.paste_button.bind('<Leave>',lambda a:self.color_changer(self.paste_button, self.paste_button_image))
        self.paste_button.place(x=200,y=134)

        # clear button
        self.clear_button_image = PhotoImage(file = './ytdl/images/clear.png')
        self.clear_button_red_image = PhotoImage(file = './ytdl/images/clearred.png')
        self.clear_button = Button(self.root,text='clear',bd=0,image=self.clear_button_image,command=lambda: self.url_box.delete(0,END),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.clear_button.bind('<Enter>',lambda a:self.color_changer(self.clear_button, self.clear_button_red_image))
        self.clear_button.bind('<Leave>',lambda a:self.color_changer(self.clear_button, self.clear_button_image))
        self.clear_button.place(x=300,y=134)

        # browse button
        self.browse_button_image = PhotoImage(file = './ytdl/images/browse.png')
        self.browse_button_red_image = PhotoImage(file = './ytdl/images/browred.png')
        self.browse_button = Button(self.root,text='browse',bd=0,image=self.browse_button_image,command=lambda: self.browse_location(),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.browse_button.bind('<Enter>',lambda a:self.color_changer(self.browse_button, self.browse_button_red_image))
        self.browse_button.bind('<Leave>',lambda a:self.color_changer(self.browse_button, self.browse_button_image))
        self.browse_button.place(x=570,y=174)

        # About button
        self.about_button_image = PhotoImage(file = './ytdl/images/img3.png')
        self.about_button_red_image = PhotoImage(file = './ytdl/images/aboutdark.png')
        self.about_button = Button(self.root,text='about',bd=0,image=self.about_button_image,command=lambda: self.about_project(),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.about_button.bind('<Enter>',lambda a:self.color_changer(self.about_button, self.about_button_red_image))
        self.about_button.bind('<Leave>',lambda a:self.color_changer(self.about_button, self.about_button_image))
        self.about_button.place(x=28,y=510)

        # update button
        self.update_button_image = PhotoImage(file = './ytdl/images/img4.png')
        self.update_button_red_image = PhotoImage(file = './ytdl/images/updatedark.png')
        self.update_button = Button(self.root,text='update',bd=0,image=self.update_button_image,command=lambda: self.update_project(),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.update_button.bind('<Enter>',lambda a:self.color_changer(self.update_button, self.update_button_red_image))
        self.update_button.bind('<Leave>',lambda a:self.color_changer(self.update_button, self.update_button_image))
        self.update_button.place(x=120,y=510)

        # donate button
        self.donate_button_image = PhotoImage(file = './ytdl/images/donatelight.png')
        self.donate_button_red_image = PhotoImage(file = './ytdl/images/donatedark.png')
        self.donate_button = Button(self.root,text='donate',bd=0,image=self.donate_button_image,command=lambda: webbrowser.open("https://github.com/sourabhkv/ytdl#support-us"),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.donate_button.bind('<Enter>',lambda a:self.color_changer(self.donate_button, self.donate_button_red_image))
        self.donate_button.bind('<Leave>',lambda a:self.color_changer(self.donate_button, self.donate_button_image))
        self.donate_button.place(x=216,y=510)

        # GitHub button
        self.Github_button_image = PhotoImage(file = './ytdl/images/img6.png')
        self.Github_button_red_image = PhotoImage(file = './ytdl/images/Githubdark.png')
        self.Github_button = Button(self.root,text='Github',bd=0,image=self.Github_button_image,command=lambda: webbrowser.open("https://github.com/sourabhkv/ytdl"),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.Github_button.bind('<Enter>',lambda a:self.color_changer(self.Github_button, self.Github_button_red_image))
        self.Github_button.bind('<Leave>',lambda a:self.color_changer(self.Github_button, self.Github_button_image))
        self.Github_button.place(x=324,y=510)

        # Supported websites button
        self.supported_web_button_image = PhotoImage(file = './ytdl/images/img7.png')
        self.supported_web_button_red_image = PhotoImage(file = './ytdl/images/supportedwebsitesdark.png')
        self.supported_web_button = Button(self.root,text='supported_web',bd=0,image=self.supported_web_button_image,command=lambda: webbrowser.open("https://supported_web.com/yt-dlp/yt-dlp/blob/master/supportedsites.md"),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.supported_web_button.bind('<Enter>',lambda a:self.color_changer(self.supported_web_button, self.supported_web_button_red_image))
        self.supported_web_button.bind('<Leave>',lambda a:self.color_changer(self.supported_web_button, self.supported_web_button_image))
        self.supported_web_button.place(x=420,y=510)

        # settings button
        self.settings_button_image = PhotoImage(file = './ytdl/images/settings.png')
        self.settings_button_red_image = PhotoImage(file = './ytdl/images/settingsdark.png')
        self.settings_button = Button(self.root,text='settings',bd=0,image=self.settings_button_image,command=lambda: self.settings_class.Settings_page(self.screen_height,self.screen_width),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.settings_button.bind('<Enter>',lambda a:self.color_changer(self.settings_button, self.settings_button_red_image))
        self.settings_button.bind('<Leave>',lambda a:self.color_changer(self.settings_button, self.settings_button_image))
        self.settings_button.place(x=585,y=510)

        # download thumbnail button
        self.download_thumbnail_button_image = PhotoImage(file = './ytdl/images/img13.png')
        self.download_thumbnail_button_red_image = PhotoImage(file = './ytdl/images/thred.png')
        self.download_thumbnail_button = Button(self.root,text='download thumbnail',bd=0,image=self.download_thumbnail_button_image,command=lambda: self.settings_class.Settings_page(self.screen_height,self.screen_width),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.download_thumbnail_button.bind('<Enter>',lambda a:self.color_changer(self.download_thumbnail_button, self.download_thumbnail_button_red_image))
        self.download_thumbnail_button.bind('<Leave>',lambda a:self.color_changer(self.download_thumbnail_button, self.download_thumbnail_button_image))
        self.download_thumbnail_button.place(x=765,y=229)

        # download button
        self.download_button_image = PhotoImage(file = './ytdl/images/img9.png')
        self.download_button_red_image = PhotoImage(file = './ytdl/images/dwred.png')
        self.download_button = Button(self.root,text='download thumbnail',bd=0,image=self.download_button_image,command=lambda: self.settings_class.Settings_page(self.screen_height,self.screen_width),bg='#424242',activebackground='#424242',highlightthickness = 0)
        self.download_button.bind('<Enter>',lambda a:self.color_changer(self.download_button, self.download_button_red_image))
        self.download_button.bind('<Leave>',lambda a:self.color_changer(self.download_button, self.download_button_image))
        self.download_button.place(x=805,y=506)


        # description box
        self.frame1=Frame(self.root,bg = "#303135",width=280,height=200)
        self.frame1.place(x=708,y=275)
        self.sb_ver= ttk.Scrollbar(self.frame1)
        self.description_box = Text(self.frame1,height=13,width=41,highlightthickness=0,relief=FLAT,yscrollcommand=self.sb_ver.set)
        self.description_box.config(font= tkFont.Font(family="Arial", size=10),state= NORMAL,background="#404040",fg="grey")#404040
        self.sb_ver.config(command=self.description_box.yview)
        self.sb_ver.pack(side=RIGHT, fill=Y)
        self.description_box.config(state=DISABLED)
        self.description_box.pack(side=LEFT)

        # Custom command page
        Label(self.tab6, text="yt-dlp ARGS",fg="white",bg="#525252").place(x=8,y=10)
        Label(self.tab6, text = "eg. -F <URL>",fg="white",bg="#525252").place(x = 535,y = 210)

        self.custom_cmd=Entry(self.tab6,bg='#303135',width=55,bd=0,fg='white',font=('Microsoft Sans Serif',10))
        self.custom_cmd.place(x=82,y=10)

        self.text_area = scrolledtext.ScrolledText(self.tab6, wrap=tk.WORD,width=83, height=11,font=('Microsoft Sans Serif',9),background="#404040",fg="white",highlightthickness=0,relief=FLAT)
        self.text_area.grid(column=0, row=2, pady=40, padx=10)

        _terminal_label = Label(self.tab6, text = "Terminal",fg="cyan",cursor="hand2",bg="#525252")
        _terminal_label.bind("<Button-1>", lambda e : subprocess.Popen('start terminal.bat',shell=True) )
        _terminal_label.place(x = 290,y = 210)

        _help_label = Label(self.tab6, text = "How to use ?",fg="orange",cursor="hand2",bg="#525252")
        _help_label.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/yt-dlp/yt-dlp#usage-and-options'))
        _help_label.place(x = 10,y = 210)

        _run_button = ttk.Button(self.tab6, text = "RUN",command=lambda : self.custom())
        _run_button.config(width=8)
        _run_button.place(x=553,y=10)

        self.imgpst = PhotoImage(file = "./ytdl/images/paste2.png")
        self.paste_custom = Button(self.tab6, text = "Paste",fg="blue",bd=0,bg="#525252",image=self.imgpst,command=lambda : self.paste2_on_text() ,activebackground='#525252',highlightthickness = 0)
        self.paste_custom.place(x=480,y=10)

        self.imgclr = PhotoImage(file = "./ytdl/images/clr2.png")
        self.clear_custom = Button(self.tab6, text = "Clear",fg="blue",bd=0,bg="#525252",image=self.imgclr,command=lambda : self.clear_custom_cmd_box() ,activebackground='#525252',highlightthickness = 0)
        self.clear_custom.place(x=515,y=10)

        # other class declaration
        self.custom_class = Pipe()
        self.settings_class = Settings()

        # list declaration
        self.basic_formats: list = []
        self.audio_formats: list = ["Mp3 64 kbps","Mp3 128 kbps","Mp3 320 kbps","M4A high","Wav Lossless","Flac Lossless"]
        self.video_streams: list = []
        self.audio_streams: list = []
        self.captions     : list = []
        self.playlist_format: list =[]


        # tab elements area
        
        # tab1
        self.video_quality_var = StringVar()
        self.video_quality_var.set("Select video Quality")
        Label(self.tab1, textvariable = self.video_quality_var,bg="#525252",fg="white").place(x = 20,y = 20)

        self.basic_combobox = ttk.Combobox(self.tab1, width="90", values=self.basic_formats,state="readonly")
        self.basic_combobox.place(x=20,y=47)

        self.ischecked_music = BooleanVar()
        self.ischecked_music.set(False)
        self.check_music=ttk.Checkbutton(self.tab1,text = "Convert to music", var=self.ischecked_music, onvalue=True, offvalue=False, command=self.isChecked)
        self.check_music.place(x=3,y=85)

        self.music_combobox =  ttk.Combobox(self.tab1, width="45", values=self.audio_formats,state="readonly")
        self.music_combobox.place(x=20,y=110)

        #tab2
        self.video_streams_var = StringVar()
        self.video_streams_var.set("Video  Streams")
        Label(self.tab2, textvariable = self.video_streams_var ,bg="#525252",fg="white").place(x = 20,y = 10)

        self.video_streams_combobox = ttk.Combobox(self.tab2, width="95", values=self.video_streams,state="readonly")
        self.video_streams_combobox.place(x=15,y=32)

        self.audio_streams_var = StringVar()
        self.audio_streams_var.set("Audio  Streams")
        Label(self.tab2, textvariable = self.audio_streams_var ,bg="#525252",fg="white").place(x = 20,y = 55)

        self.audio_streams_combobox = ttk.Combobox(self.tab2, width="95", values=self.audio_streams,state="readonly")
        self.audio_streams_combobox.place(x=15,y=77)

        self.captions_var = StringVar()
        self.captions_var.set("Subtitles")
        Label(self.tab2, textvariable = self.captions_var ,bg="#525252",fg="white").place(x = 20,y = 100)

        self.captions_combobox = ttk.Combobox(self.tab2, width="37", values=self.captions ,state="readonly")
        self.captions_combobox.place(x=15,y=122)

        self.format_var = StringVar()
        self.format_var.set("Format")
        Label(self.tab2, textvariable = self.format_var,bg="#525252",fg="white").place(x = 280,y = 100)

        self.format_checkbox=ttk.Combobox(self.tab2, width="20", values=["auto-detect","mp4","mkv","webm"],state="readonly")
        self.format_checkbox.set("auto-detect")
        self.format_checkbox.place(x=327-50,y=122)

        self.ratelim_var = StringVar()
        self.ratelim_var.set("Rate limit(eg. 50K or 4.2M)")
        Label(self.tab2, textvariable = self.ratelim_var ,bg="#525252",fg="white").place(x = 442,y = 100)

        self.ratelim_entry=ttk.Entry(self.tab2,width=27)
        self.ratelim_entry.place(x=437,y=122)

        self.custom_filename_var = StringVar()
        self.custom_filename_var.set("Custom Filename")
        Label(self.tab2, textvariable = self.custom_filename_var,bg="#525252",fg="white").place(x = 20,y = 146)

        self.customfile_entry = ttk.Entry(self.tab2,width=46)
        self.customfile_entry.place(x=17,y=169)

        self.proxy_var = StringVar()
        self.proxy_var.set("Proxy URL")
        Label(self.tab2, textvariable = self.proxy_var,bg="#525252",fg="white").place(x = 330,y = 146)

        self.proxy_entry = ttk.Entry(self.tab2,width=46)
        self.proxy_entry.place(x=323,y=169)

        self.embdth_var = BooleanVar()
        self.embdth_var.set(False)
        self.embdth=ttk.Checkbutton(self.tab2,text="Embed thumbnail", var=self.embdth_var, onvalue=True, offvalue=False)
        self.embdth.place(x=17,y=199)

        #tab3
        self.playlist_format_var = StringVar()
        self.playlist_format_var.set("Select format")
        Label(self.tab3, textvariable = self.playlist_format_var,bg="#525252",fg="white").place(x = 170,y = 20)

        self.playlist_format = ttk.Combobox(self.tab3, width="45", values=self.playlist_format,state="readonly")
        self.playlist_format.place(x=170,y=45)

        self.playlist_items_var = StringVar()
        self.playlist_items_var.set("Select items")
        Label(self.tab3, textvariable = self.playlist_items_var,bg="#525252",fg="white").place(x = 170,y = 70)

        self.playlist_items = ttk.Entry(self.tab3,width=47)
        self.playlist_items.place(x=170,y=95)



    
    def color_changer(self,b,a):
        b.config(image=a)
    
    def on_change(self):
        _text = self.url_box.get()
        if not len(_text):
            messagebox.showerror('Youtube-dl GUI','Enter URL')

    def isChecked(self):
        print("hello")
    
    def paste_on_text(self):
        try:
            _AnnoyingWindow=Tk()
            _ClipBoard = _AnnoyingWindow.clipboard_get()
            _AnnoyingWindow.destroy()
            _ele=_ClipBoard
            self.url_box.insert(END, ' '+_ele )

        except:
            _AnnoyingWindow.destroy()
            messagebox.showerror('Youtube-dl GUI','URL should be in text')
    
    def paste2_on_text(self):
        try:
            _AnnoyingWindow=Tk()
            _ClipBoard = _AnnoyingWindow.clipboard_get()
            _AnnoyingWindow.destroy()
            _ele=_ClipBoard
            self.custom_cmd.insert(END, ' '+_ele )
            print(self.custom_cmd.get())

        except:
            _AnnoyingWindow.destroy()
            messagebox.showerror('Youtube-dl GUI','URL should be in text')
    
    def clear_custom_cmd_box(self):
        self.custom_cmd.delete(0,END)
        self.text_area.delete(0.0,END)
    
    def browse_location(self):
        self.download_Directory = filedialog.askdirectory(initialdir='YOUR DIRECTORY PATH')
        if self.download_Directory=='':
            with open('./ytdl/config/loc.txt','r') as file:
                self.download_Directory=file.readlines()[0]

        self.location_box.delete(0,END)
        self.location_box.insert(0,self.download_Directory)
        with open('./ytdl/config/loc.txt','w+') as file:
            file.write(self.download_Directory)
    
    def about_project(self):
        About(self.screen_height, self.screen_width)
    
    def open_dir(self):
        if os.path.exists(self.location_box.get()):
            subprocess.Popen(r'explorer /open, '+self.location_box.get().replace("/","\\"))
        else:
            messagebox.showerror("Youtube-dl GUI","Path doesn't exist\nPath might be deleted or moved")
    
    def custom(self):
        if len(self.custom_cmd.get()) > 0:
            _cmd="yt-dlp "+self.custom_cmd.get()
            t2 = threading.Thread(target=self.custom_class.run_commandcustom, args=(self.root,self.text_area,_cmd,))
            t2.start()
        else:
            messagebox.showerror("Youtube-dl GUI","Enter command")