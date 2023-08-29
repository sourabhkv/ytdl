import os
from .ui import window

__license__ = 'Public Domain'

class maker:
    
    'This class is to check if all files exist, if not create it'

    def __init__(self) -> None:
        if  os.path.exists("./ytdl/config"):
            pass
        else:
            os.makedirs("./ytdl/config",exist_ok=False)
            with  open("./ytdl/config/loc.txt",'w+') as file:
                file.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
            
            with open("./ytdl/config/history.txt",'w+') as file1:
                with  open("./ytdl/config/log.txt",'w+') as file2:
                    with  open("./ytdl/config/cookies.txt",'w+') as file3:
                        with  open("./ytdl/config/args.txt",'w+') as file4:
                            with open("./ytdl/config/loc.txt",'w+') as file5:
                                file5.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
            
            with  open("./ytdl/config/output_temp_vid.txt",'w+') as file:
                file.write("%(title)s.%(ext)s")
            
            with  open("./ytdl/config/output_temp_plst.txt",'w+') as file:
                file.write("%(playlist_title)s %(playlist_index)s %(title)s.%(ext)s")
        
cleaner = maker()    


def main(args=None):
    x = window.Window()
    x.root.mainloop()