from yt_dlp import YoutubeDL
from tkinter import messagebox
from .thumbnail import Search_thumbnail
from .description import Description
from threading import Thread

class extract_info:
    global x
    def __init__(self,x) -> None:
        if len(x.url_box.get())==0:
            messagebox.showerror("Youtube-dl GUI","  Enter Valid URL  ")
        else:
            self.url = x.url_box.get()
            x.URL = self.url
        self.merged_list = []
        self.audio_list = []
        self.video_list = []
        self.subs=[]

    def search(self,x):
        ydl_opts = {}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=False)
            x.info = info
            print(len(info['formats']))

            temp1 = Search_thumbnail()
            temp_thread1 = Thread(target= temp1.search_thumbnail ,args= ( x,))
            temp_thread1.start()

            temp2 = Description(x)
            temp_thread2 = Thread(target= temp2.description_adder , args= ( x,))
            temp_thread2.start()

            master = {
                'format_id':[],
                'format_note':[],
                'filesize':[],
                'ext':[],
                'acodec':[],
                'vcodec':[],
                'resolution':[],
                'tbr':[],
                'fps':[],
                'dynamic_range':[],
            }

            tasker = {
                'format_id':0,
                'format_note':1,
                'filesize':2,
                'ext':3,
                'acodec':4,
                'vcodec':5,
                'resolution':6,
                'tbr':7,
                'fps':8,
                'dynamic_range':9,
            }
            for i in range(len(info['formats'])):
                _x = info['formats'][i].keys()
                t = [None]*10
                for j in _x:
                    if str(j) in tasker:
                        t[tasker[j]] = info['formats'][i][j]
                    elif 'filesize_approx' in str(j):
                        print("apppp")
                        t[tasker['filesize']] = info['formats'][i][j]
                    elif not t[tasker['format_note']] and str(j)=='height':
                        t[tasker['format_note']] = str(info['formats'][i]['height']) + 'p'
                
                #print(t)
                counter = 0
                for k in master:
                    master[k].append(t[counter])
                    counter+=1
                _temp = ""
                
                if len(t)>0  and t[3]!='mhtml':
                    if t[4]=='none':
                        t[4]=None
                    if t[5]=='none':
                        t[5]=None
                    _temp=""
                    #print(t[4],t[5],type(t[4]),type(t[5]),"afeter",t[4] is None,t[5] is None)
                    if t[4] is None and t[5] is not None:#only video
                        if t[0] and t[0]!='none':
                            _temp = t[0]
                        if t[1] and t[1]!='none':
                            _temp +="  |  " +t[1]
                        if t[2] and t[2]!='none':
                            _temp += "  |  Size: " +self.size(t[2])
                        if t[3] and t[3]!='none':
                            _temp += "  |  Ext: "+t[3]
                        if t[5] and t[5]!='none':
                            _temp += "  |  "+t[5]
                        if t[6] and t[6]!='none':
                            _temp += "  |  "+t[6]
                        if t[7] and t[7]!='none':
                            _temp += "  |  Bitrate: "+str(round(t[7],2))+" K/s"
                        if t[8] and t[8]!='none':
                            _temp += "  |  FPS: "+str(t[8])
                        if t[9] and t[9]!='none':
                            _temp += "  |  "+t[9]
                        
                        self.video_list.append(_temp)
                    
                    if t[5] is None and t[4] is not None:# only audio
                        if t[0] and t[0]!='none':
                            _temp = t[0]
                        if t[1] and t[1]!='none':
                            _temp +="  |  " +t[1]
                        if t[2] and t[2]!='none':
                            _temp += "  |  Size: " +self.size(t[2])
                        if t[3] and t[3]!='none':
                            _temp += "  |  Ext: "+t[3]
                        if t[4] and t[4]!='none':
                            _temp += "  |  "+t[4]
                        if t[5] and t[5]!='none':
                            _temp += "  |  "+t[5]
                        if t[6] and t[6]!='none':
                            _temp += "  |  "+t[6]
                        if t[7] and t[7]!='none':
                            _temp += "  |  Bitrate: "+str(round(t[7],2))+" K/s"

                        self.audio_list.append(_temp)
                    
                    if t[5] is not None and t[4] is not None:
                        if t[0] and t[0]!='none':
                            _temp = t[0]
                        if t[1] and t[1]!='none':
                            _temp +="  |  " +t[1]
                        if t[2] and t[2]!='none':
                            _temp += "  |  Size: " +self.size(t[2])
                        if t[3] and t[3]!='none':
                            _temp += "  | Ext: "+t[3]
                        if t[4] and t[4]!='none':
                            _temp += "  |  "+t[4]
                        if t[5] and t[5]!='none':
                            _temp += "  |  "+t[5]
                        if t[6] and t[6]!='none':
                            _temp += "  |  "+t[6]
                        if t[7] and t[7]!='none':
                            _temp += "  |  Bitrate: "+str(round(t[7],2))+" K/s"
                        if t[8] and t[8]!='none':
                            _temp += "  |  FPS: "+str(t[8])
                        if t[9] and t[9]!='none':
                            _temp += "  |  "+t[9]

                        self.merged_list.append(_temp)
            
            if 'subtitles' in info:
                try:
                    for i in info['subtitles']:
                        self.subs.append(str(i)+"   "+str(info['subtitles'][i][0]['name']))
                except:
                    pass
        
        x.basic_formats = self.merged_list
        x.video_streams = self.video_list
        x.audio_streams = self.audio_list
        x.captions = self.subs
        x._init_tab1()
        x._init_tab2()
        x._init_download_button()
        x._init_download_image_button()



    def size(self,n):
        if n//1024**2>=1 and n//1024**2<1024:
            a=str(round((n/1024**2),2))+" MiB"
            return a
        elif n>=1024**3:
            a=str((round((n/1024**3),2)))+" GiB"
            return a
        elif n//1024>=1 and n//1024<1024:
            a=str(round(n/1024,2))+" KiB"
            return a