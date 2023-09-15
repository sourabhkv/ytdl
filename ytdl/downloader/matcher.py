from tkinter import messagebox
from .downloader import Downloader
from threading import Thread
class Match_case:
    def __init__(self) -> None:
        self.my_opts = [
            '--no-mtime',
            '--no-restrict-filenames',
            '--add-metadata',
            '--color','no_color',
        ]
    
    def checking(self, x):
        #tab1 check
        if x.basic_combobox.get() or x.music_combobox.get():
            if x.basic_combobox.get():
                print(x.basic_combobox.get())
                __temp = [
                    '-f '+ x.basic_combobox.get().split()[0],
                ]
                self.my_opts.extend(__temp)
            else:
                print(x.music_combobox.get())
                
                __temp = [
                    '--embed-thumbnail',
                    '--parse-metadata','description:(?s)(?P<meta_comment>.+)',
                    '--parse-metadata','album:(?s)(?P<meta_album>.+)',
                    '--parse-metadata','genre:(?s)(?P<meta_genre>.+)',
                    '--parse-metadata','uploader:(?s)(?P<meta_album_artist>.+)',
                    '--parse-metadata','%(upload_date,release_year).4s:(?P<meta_date>.+)',
                ]
                if "Mp3" in x.music_combobox.get():
                    if '64' in x.music_combobox.get():
                        __temp.extend(['-x','--audio-format','mp3','--audio-quality','64K','-f wa'])
                    if '128' in x.music_combobox.get():
                        __temp.extend(['-x','--audio-format','mp3','--audio-quality','128K','-f ba'])
                    if '320' in x.music_combobox.get():
                        __temp.extend(['-x','--audio-format','mp3','--audio-quality','320K','-f ba'])
                elif "M4a" in x.music_combobox.get():
                    __temp.extend(['-x','--audio-format','m4a','--audio-quality','0','-f ba'])
                elif "Wav" in x.music_combobox.get():
                    __temp.extend(['-x','--audio-format','wav','--audio-quality','0','-f ba'])
                elif "Flac" in x.music_combobox.get():
                    __temp.extend(['-x','--audio-format','flac','--audio-quality','0','-f ba'])

                self.my_opts.extend(__temp)
                

        #tab2 check
        elif x.video_streams_combobox.get() or x.audio_streams_combobox.get() or x.captions_combobox.get():
            print(x.video_streams_combobox.get() , x.audio_streams_combobox.get() , x.captions_combobox.get())
            if x.video_streams_combobox.get() and x.audio_streams_combobox.get():
                __temp = [ 
                    '-f ' + x.audio_streams_combobox.get().split()[0] + "+" + x.video_streams_combobox.get().split()[0],
                    ]
                self.my_opts.extend(__temp)
            elif x.video_streams_combobox.get() and x.audio_streams_combobox.get() and x.captions_combobox.get():
                __temp = [
                    '-f ' + x.audio_streams_combobox.get().split()[0] + "+" + x.video_streams_combobox.get().split()[0],'--write-srt --sub-lang {}'.format(x.captions_combobox.get().split()[0]),
                    ]
                self.my_opts.extend(__temp)
            elif x.video_streams_combobox.get():
                __temp = [ 
                    '-f ' + x.audio_streams_combobox.get().split()[0] + "+" + x.video_streams_combobox.get().split()[0],
                    ]
                self.my_opts.extend(__temp)
        
        else:
            messagebox.showerror("Youtube-dl GUI","Select valid combination")
            return
        
        if x.embdth_var.get():
            self.my_opts.append('--embed-thumbnail')
        if x.ratelim_entry.get():
            self.my_opts.append('-r '+x.ratelim_entry.get())

        if x.customfile_entry.get():
            self.my_opts.append('-o '+x.customfile_entry.get()+'.%(ext)s')
        else:
            self.my_opts.append('-o '+'%(title)s.%(ext)s')
        
        if x.proxy_entry.get():
            self.my_opts.append('--proxy '+x.proxy_entry.get())
        if x.format_checkbox.get()!='auto-detect':
            self.my_opts.append('--merge-output-format '+x.format_checkbox.get())
        
        dl = Downloader(x)
        print(self.my_opts)
        self.my_opts = tuple(self.my_opts)
        _res = dl.cli_to_api(self.my_opts)
        print(_res)
        _mythread = Thread(target=dl.start_download , args=(_res,))
        _mythread.start()