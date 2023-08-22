import os


class Checker:
    
    'This class is to check if all files exist, if not create it'

    def __init__(self) -> None:
        if  os.path.exists("./config"):
            pass
        else:
            os.makedirs("./config",exist_ok=False)
            with  open("./config/loc.txt",'w+') as file:
                file.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
            
            with open("./config/history.txt",'w+') as file1:
                with open("./config/loc.txt",'w+') as file2:
                    file2.write((os.path.expanduser('~')+"\\Downloads").replace("\\","/"))
                    with  open("./config/log.txt",'w+') as file3:
                        with  open("./config/cookies.txt",'w+') as file4:
                            pass
                        pass
                    pass
            
            with  open("./config/output_temp_vid.txt",'w+') as file:
                file.write("%(title)s.%(ext)s")
            
            with  open("./config/output_temp_vid.txt",'w+') as file:
                file.write("%(playlist_title)s %(playlist_index)s %(title)s.%(ext)s")