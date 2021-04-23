from google_drive_downloader import GoogleDriveDownloader as gdd
import os
a=os.getcwd()
from tkinter import *
from tkinter import ttk
import threading,shutil

def dler():
    try:
        gdd.download_file_from_google_drive(file_id='11aMEHLcYfjuBs-dX-YzU7g9RnjJ8sD_j',dest_path=a+'\\youtube_dl.zip')
        shutil.unpack_archive('youtube_dl.zip', a)
        ext=ttk.Button(root,text="Launch",command=launch)
        ext.place(x=100,y=45)
        name = Label(root, text = "   YouTube-dl GUI complete         ").place(x = 75,y = 75)
    except:
        name = Label(root, text = "   YouTube-dl GUI not complete    ").place(x = 75,y = 75)

def launch():
    os.startfile('youtube-dl GUI V21.04a21.exe')
    root.destroy()

def dlller():
    name = Label(root, text = "    YouTube-dl GUI downloading    ").place(x = 60,y = 75)
    t1 = threading.Thread(target=dler)
    t1.start()

root = Tk()
root.geometry("300x100")
root.resizable(False, False)
root.title('YouTube-dl GUI Installer')
ext=ttk.Button(root,text="Download",command=dlller)
ext.place(x=100,y=45)
root.mainloop()
