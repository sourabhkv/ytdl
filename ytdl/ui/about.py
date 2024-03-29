import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from ..version import __version__

class About:
    def __init__(self,sh,sw) -> None:
        root2 = tk.Toplevel()
        root2.focus_force()
        y=int((sh-500)/2)-30
        x=int((sw-600)/2)
        root2.geometry('%dx%d+%d+%d' % (600, 500, x, y))
        root2.title('About Youtube-dl GUI')
        root2.configure(bg='#303135')
        image = Image.open("./images/logo.png")
        resize_image = image.resize((200, 200))
        img = ImageTk.PhotoImage(resize_image)
        tk.Label(master=root2, text = "",image=img,bg="#303135",font=('Arial', 16),fg="white").place(relx=0.5, rely=0.25,anchor= CENTER)
        Label(root2, text = "Youtube-dl GUI  v"+__version__,bg="#303135",font=('Arial', 12),fg="white").place(relx=.5, rely=.5,anchor= CENTER)
        Label(root2, text = "Released under MIT License",bg="#303135",fg="white").place(relx=.5, rely=.56,anchor= CENTER)
        Label(root2, text = "This is project is based on yt-dlp , ffmpeg , atomic parsley",bg="#303135",fg="white").place(relx=.5, rely=.69,anchor= CENTER)
        Label(root2, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 9,'bold'),fg="red",bg="#303135").place(relx=.5, rely=.75,anchor= CENTER)
        name74 = Label(root2, text = "CREDITS :",bg="#303135",fg="white").place(x=40+70,y=290)
        name74 = Label(root2, text = "yt-dlp",bg="#303135",fg="#0574FF",cursor="hand2")
        name74.place(x = 135+85,y = 290)
        name74.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/yt-dlp/yt-dlp'))
        name73 = Label(root2, text = "ffmpeg",fg="#0574FF",cursor="hand2",bg="#303135")
        name73.place(x = 210+95,y = 290)
        name73.bind("<Button-1>", lambda e: webbrowser.open('https://www.ffmpeg.org/'))
        name75 = Label(root2, text = "AtomicParsley",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 290+105,y = 290)
        name75.bind("<Button-1>", lambda e: webbrowser.open('http://atomicparsley.sourceforge.net/'))
        name76 = Label(root2, text = "TELEGRAM",fg="orange",cursor="hand2",bg="#303135")
        name76.place(x = 190+145,y = 390)
        name76.bind("<Button-1>", lambda e: webbrowser.open('https://t.me/ytdlgui'))
        name77 = Label(root2, text = "DONATE",fg="yellow",cursor="hand2",bg="#303135")
        name77.place(x = 190,y = 390)
        name77.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl#support-us'))
        name7e = Label(root2, text = "Changelog",fg="#0574FF",cursor="hand2",bg="#303135")
        name7e.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/releases/tag/v23.0305.12'))
        name7e.place(x = 195,y = 315)
        name8e = Label(root2, text = "Check for updates",fg="#0574FF",cursor="hand2",bg="#303135")
        #name8e.bind("<Button-1>", lambda e: os.startfile("updater.exe"))
        name8e.place(x = 295,y = 315)
        streams2 = Label(root2, text = "https://github.com/sourabhkv/ytdl",bg="#303135",fg="white").place(relx=.5, rely=.87,anchor= CENTER)
        streams2 = Label(root2, text = "Developed by sourabhkv",bg="#303135",fg="green").place(relx=.5, rely=.93,anchor= CENTER)
        #webbrowser.open final2 https://drive.google.com/file/d/1CWW5YTK7MjIQ3ZyQdsN7TSNu_K-F3hxN/view?usp=sharing
        root2.resizable(False, False)
        root2.iconbitmap(r'./images/logo.ico')
        root2.mainloop()