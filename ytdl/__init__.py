import os
from .ui import window
from .update._update_checker import check_for_update
from threading import Thread

__license__ = 'Public Domain'


class maker:
    
    'This class is to check if all files exist, if not create it'

    def __init__(self) -> None:
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
    
cleaner = maker()

mythread = Thread(target=check_for_update,args=("https://api.github.com/repos/sourabhkv/ytdl/releases/latest",))
mythread.start()

def main(args=None):
    window.Window(args).root.mainloop()