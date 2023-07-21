import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
from tkinter import scrolledtext
import webbrowser

class Window:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("YouTube-dl GUI")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        _y=int((self.screen_height-640)/2)
        _x=int((self.screen_width-1000)/2)
        self.root.geometry('%dx%d+%d+%d' % (1030, 580, _x, _y))
        self.root.resizable(False,False)

        self.root.configure(bg='#303135')
        self.style= ttk.Style()
        self.style.configure("TCombobox", fieldbackground= "#525252", background= "#525252",foreground="black")
        self.style.configure("TButton",background="#525252")
        self.style.configure("TScrollbar",background="#525252",activebackground="#525252")
        self.style.configure("TNotebook", background='#424242',borderwidth=0)
        self.style.configure("TCheckbutton", background='#525252',foreground="white",activebackground="#525252",borderwidth=0)

        self.tabControl = ttk.Notebook(self.root,height=236,width=624)

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
        self.tabControl.add(self.tab6, text ='  Custom command ')
        self.tabControl.add(self.tab7, text =' History ')
        self.tabControl.place(x=35,y=215)#275




        


        Label(self.root, text = "Youtube-dl GUI",bg="#303135",font=('Arial', 18),fg="white").place(x = 230,y = 10) 

        self.ex=Entry(self.tab6,bg="#303135",width=55,bd=0,fg="white",font=('Microsoft Sans Serif',10))
        self.ex.place(x=82,y=10)

        name77 = Label(self.root, text = "Explore  ytdl  Unlocked",fg="yellow",cursor="hand2",bg="#303135")
        name77.place(x = 530,y = 20)
        name77.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/blob/main/README.md#ytdl-unlocked-pro'))

        imgpst = PhotoImage(file = "./images/paste2.png")
        namepst = Button(self.tab6, text = "Paste",fg="blue",bd=0,bg="#525252",image=imgpst,command=lambda : self.paste2(),activebackground='#525252',highlightthickness = 0)
        namepst.place(x=480,y=10)