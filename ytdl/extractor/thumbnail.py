import requests
from io import BytesIO
from PIL import ImageTk,Image
from tkinter import ttk, Label, StringVar
from threading import Thread
class Search_thumbnail:
    def search_thumbnail(self,x):
        info = x.info
        url = x.URL
        if "youtube" in url and "music" not in url and "shorts" not in url or "youtu.be" in url and "music" not in url and "shorts" not in url:
            if "youtube" in url:
                d=url.find("=")
                vid=url[d+1:]
            elif "youtu.be" in url:
                vid=url[url.rfind("/")+1:]
            thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            img.mode = 'RGB'
            image = img.resize((270, 160), Image.LANCZOS)
            x.thimg = ImageTk.PhotoImage(image)
            Label(x.root, image=x.thimg)
            picbtn=ttk.Button(x.root, text = 'thumbnail', image = x.thimg,command=lambda : self.viewer(img))
            picbtn.place(x=710,y=40)
    
        elif "youtube" in url and "music" in url:
            if url.find("&")==-1:
                vid=url[1+url.find("="):]
            else:
                vid=url[1+url.find("="):url.find("&")]
            #print(vid)
            thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            img.mode = 'RGB'
            image = img.resize((270, 160), Image.LANCZOS)
            x.thimg = ImageTk.PhotoImage(image)#https://www.youtube.com/shorts/WSFe3Rp7arQ
            Label(x.root, image=x.thimg)
            picbtn=ttk.Button(x.root, text = 'thumbnail', image = x.thimg,command=lambda : self.viewer(img))
            picbtn.place(x=710,y=40)

        elif "youtube" in url and "shorts" in url:
            #print("ghfghgfhf")
            vid=url.rstrip("?feature=share")[url.rstrip("?feature=share").rfind("/")+1:]
            #print(vid)
            #print(vid,url)
            thurl = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vid)
            r = requests.get(thurl)
            img = Image.open(BytesIO(r.content))
            img.mode = 'RGB'
            image = img.resize((270, 160), Image.LANCZOS)
            x.thimg = ImageTk.PhotoImage(image)#https://www.youtube.com/shorts/WSFe3Rp7arQ
            Label(x.root, image=x.thimg)
            picbtn=ttk.Button(x.root, text = 'thumbnail', image = x.thimg,command=lambda : self.viewer(img))#work left in viewer image not showing up
            picbtn.place(x=710,y=40)
    
        else:
            if 'thumbnail' in info:
                thurl=info['thumbnail']
            try:
                r = requests.get(thurl)
                img = Image.open(BytesIO(r.content))
                width, height = img.size
                i=2
                while (i)>0:
                    if (i*height)<=170 and (i*width)<=270:
                        break
                    else:
                        i=i-0.02
                nw=int(i*width)
                nh=int(i*height)
                sp=int((230-nw)/2)
                #print(nw,nh)
                image = img.resize(((nw),(nh)), Image.Resampling.LANCZOS)
                x.thimg = ImageTk.PhotoImage(image)
                Label(x.root, image=x.thimg)
                picbtn=ttk.Button(x.root, text = 'thumbnail', image = x.thimg,command=lambda : self.viewer(img))
                picbtn.place(x=sp+730,y=40)
            
            except:
                x.na = StringVar()
                x.na.set("Thumbnail unavailable")
                x.thumbnail_unavailable_label = Label(x.root, textvariable = x.na,bg="#525252",fg="white")
                x.thumbnail_unavailable_label.place(x = 780,y = 70)
    
    def viewer(self,img):
        t1w = Thread(target=self.viewers, args=(img,))
        t1w.start()
    
    def viewers(self,img):
        img.show()