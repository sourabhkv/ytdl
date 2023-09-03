import os
from .ui import window
from .update._update_checker import check_for_update
from threading import Thread
from tkinter import *
from tkinter import ttk
import requests
import zipfile

__license__ = 'Public Domain'

class maker:
    
    'This class is to check if all files exist, if not create it'

    def __init__(self) -> None:
        global _dependency_status
        _dependency_status = False
        if  os.path.exists("./config"):
            pass
        else:
            os.makedirs("./config",exist_ok=False)
            with  open("./config/loc.txt",'w+') as file:
                file.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
            
            with open("./config/history.txt",'w+') as file1:
                with  open("./config/log.txt",'w+') as file2:
                    with  open("./config/cookies.txt",'w+') as file3:
                        with  open("./config/args.txt",'w+') as file4:
                            with open("./config/loc.txt",'w+') as file5:
                                file5.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
            
            with  open("./config/output_temp_vid.txt",'w+') as file:
                file.write("%(title)s.%(ext)s")
            
            with  open("./config/output_temp_plst.txt",'w+') as file:
                file.write("%(playlist_title)s %(playlist_index)s %(title)s.%(ext)s")
    
    def download_dependency(self):
        global _dependency_status
        _files_list = os.listdir()
        if "yt-dlp_86.exe" not in _files_list and "ffmpeg.exe" not in _files_list and "AtomicParsley.exe" not in _files_list:
            self.dependency_status = False
            self._root = Tk()
            self.screen_width = self._root.winfo_screenwidth()
            self.screen_height = self._root.winfo_screenheight()
            _y=int((self.screen_height-340)/2)
            _x=int((self.screen_width-500)/2)
            self._root.geometry('%dx%d+%d+%d' % (500, 300, _x, _y))
            self._root.title('YouTube-dl GUI Dependency installer')
            Label(self._root,text="Youtube-dl GUI needs to install the following dependency\n\n1.yt-dlp\n\n2.ffmpeg\n\n3.AtomicParsley").place(x=100,y=10)
            self._download_status = StringVar()
            self._download_status.set('Installation will take approx 30 Mb internet and 43 Mb of disk space')
            Label(self._root,textvariable=self._download_status).place(x=20,y=210)
            self.install_btn = ttk.Button(self._root,text='Install dependency',command=self.disable_btn)
            self.install_btn.place(x=200,y=160)
            self.progress = ttk.Progressbar(self._root, orient="horizontal", length=450, mode="determinate")
            self.progress.place(x=20,y=250)
            self._root.iconbitmap('./images/logo.ico')
            self._root.mainloop()
        
        else:
            _dependency_status = True
    
    def disable_btn(self):
        self.install_btn.config(state=DISABLED)
        download_thread = Thread(target=self.download_file)
        download_thread.start()
    
    def download_file(self):
        global _dependency_status
        url1 = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_x86.exe'
        response = requests.get(url1, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        self._download_status.set('[downloading yt-dlp . . .]')
        with open('yt-dlp_x86.exe', 'wb') as file:
            for data in response.iter_content(block_size):
                file.write(data)
                self.progress["value"] += len(data)
        
        url2 = 'https://github.com/ForeverAggregrate/ytdl_dependency/releases/latest/download/Dependency.zip'
        response = requests.get(url2, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        self._download_status.set('[downloading ffmpeg,AtomicParsley . . .]')
        with open('Dependency.zip', 'wb') as file:
            for data in response.iter_content(block_size):
                file.write(data)
                self.progress["value"] += len(data)
        
        self.progress["value"] = 0
        
        self._download_status.set('[extracting files . . .]')
        with zipfile.ZipFile('Dependency.zip', 'r') as zip:
            zip.extractall('./')
        
        os.remove('Dependency.zip')
        self._download_status.set('[Done] All dependency is installed ,Restart the program')
        _dependency_status = True


cleaner = maker()
cleaner.download_dependency()


#mythread = Thread(target=check_for_update,args=("https://api.github.com/repos/sourabhkv/ytdl/releases/latest",))
#mythread.start()

def main(args=None):
    if _dependency_status:
        window.Window(args).root.mainloop()