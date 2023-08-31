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

    def search(self,x):
        ydl_opts = {}
        try:
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

            
            
            for i in range(0,len(info['formats'])):
                print("going")
                #a=info['formats'][i]
                try:
                    del info['formats'][i]['url']
                except:
                    pass
                try:
                    del info['formats'][i]['preferencefragments']
                except:
                    pass
                try:
                    del info['formats'][i]['http_headers']
                except:
                    pass
                try:
                    del info['formats'][i]['source_preference']
                except:
                    pass
                try:
                    del info['formats'][i]['downloader_options']
                except:
                    pass
                try:
                    del info['formats'][i]['fragments']
                except:
                    pass
                try:
                    del info['formats'][i]['language']
                    del info['formats'][i]['language_preference']
                except:
                    pass
                try:
                    info['formats'][i]['filesize']=self.size(info['formats'][i]['filesize'])
                    del info['formats'][i]['preference']
                except:
                    pass
                try:
                    del info['formats'][i]['format']
                    del info['formats'][i]['height']
                    del info['formats'][i]['width']
                except:
                    pass
                try:
                    #del info['formats'][i]['protocol']
                    del info['formats'][i]['quality']
                except:
                    pass
                try:
                    del info['formats'][i]['manifest_url']
                    del info['formats'][i]['fragment_base_url']
                except:
                    pass
                try:
                    del info['formats'][i]['manifest_stream_number']
                except:
                    pass
                b=info['formats'][i]
                #print(b)
                st={}
                for i in b:
                    if b[i]!=None and b[i]!='none' and b[i]!=False and b[i]!='SDR':
                        st[i]=b[i]
                if "format_id" in st:
                    d=d+st['format_id']
                if 'format_note' in st:
                    d=d+"  |  "+st['format_note']
                if 'filesize' in st:
                    d=d+"  |  Size : "+str(st['filesize'])
                if 'filesize_approx' in st:
                    st['filesize_approx']=self.size(st['filesize_approx'])
                    d=d+"  |  Size : "+str(st['filesize_approx'])
                if 'ext' in st:
                    d=d+"  | ext: "+st['ext']
                if 'vcodec' in st:
                    d=d+"  |  "+st['vcodec']
                if 'acodec' in st:
                    d=d+"  |  "+st['acodec']
                if 'resolution' in st:
                    d=d+"  |  "+st['resolution']
                if 'tbr' in st:
                    if st['tbr']>=1024:
                        st['tbr']=str(round(st['tbr']/1024,2))+" Mbps"
                        d=d+"  | Bitrate: "+st['tbr']
                    else:
                        d=d+"  | Bitrate: "+str(st['tbr'])+" Kbps"
                if 'fps' in st:
                    d=d+" | FPS "+str(st['fps'])
                if 'vcodec' in st and 'acodec' in st:
                    d=d+" #"
                d=d+"\n"
            print(d)
            #print(st)
        except:
            d=" "+"\n"+" "
        
    
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