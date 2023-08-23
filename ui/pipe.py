import subprocess
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import END

class Pipe:
    
    def run_commandcustom(self,root,text_area,cmd):
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