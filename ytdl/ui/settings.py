import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import messagebox

class Settings:
    def Settings_page(self,sh,sw):
        self.root = tk.Tk()
        self.root.configure(bg='#303135')
        self.root.focus_force()
        y=int((sh-500)/2)-30
        x=int((sw-500)/2)
        self.root.geometry('%dx%d+%d+%d' % (500, 500, x, y))
        self.root.title('Youtube-dl GUI  Settings')
        Label(self.root, text = "Settings",font=('Arial', 16),bg="#303135",fg="white").place(relx=0.5, rely=0.05,anchor= CENTER)
        Label(self.root, text = "Default Download Options",bg="#303135",fg="white").place(relx=0.5, rely=0.12,anchor= CENTER)
        Label(self.root, text = "Path to Cookie file",bg="#303135",fg="white").place(relx=0.5, rely=0.28,anchor= CENTER)
        Label(self.root, text = "Output template for video",bg="#303135",fg="white").place(relx=0.5, rely=0.44,anchor= CENTER)
        Label(self.root, text = "Output template for playlist",bg="#303135",fg="white").place(relx=0.5, rely=0.56,anchor= CENTER)
        dd=Label(self.root, text = "Update  yt-dlp",fg="#0574FF",cursor="hand2",bg="#303135")
        dd.place(x = 390,y = 460)
        #dd.bind("<Button-1>", lambda e: updateback())
        name75 = Label(self.root, text = "Report issue",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 15,y = 460)
        name75.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/issues'))

        self.optnentry=ttk.Entry(self.root,width=74)
        self.cookiepath=ttk.Entry(self.root,width=71)
        self.out_vid=ttk.Entry(self.root,width=74)
        self.out_plst=ttk.Entry(self.root,width=74)
        
        #self.x = ttk.Button(self.root, text ="Save", command = self.save())
        #self.x.place(relx=0.5, rely=0.8,anchor= CENTER)
        file2=open("./config/cookies.txt",'r')
        data1=file2.readlines()
        file2.close()
        file3=open("./config/args.txt",'r')
        data2=file3.readlines()
        file3.close()
        file4=open("./config/output_temp_vid.txt",'r')
        out_temp_vid=file4.readlines()
        file4.close()
        file5=open("./config/output_temp_playlist.txt",'r')
        out_temp_plst=file5.readlines()
        file5.close()
        
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
        Button(self.root, text =".", command = self.cookieselect()).place(x=455,y=156)
        self.root.resizable(False, False)
        self.root.iconbitmap(r'./images/logo.ico')
        self.root.mainloop()
    
    def save(self):
        c1=self.optnentry.get()
        c2=self.cookiepath.get()
        c3=self.out_vid.get()
        c4=self.out_plst.get()
        with open("./config/cookies.txt",'w+') as file:
            file.write(c2)

        with open("./config/args.txt",'w+') as file:
            file.write(c1)

        with open("./config/output_temp_vid.txt",'w+') as file:
            file.write(c3)
        
        with open("./config/output_temp_playlist.txt",'w+') as file:
            file.write(c4)
        
        #root4.destroy()
        self.root.destroy()
        messagebox.showinfo("Youtube-dl GUI", "Settings saved!")