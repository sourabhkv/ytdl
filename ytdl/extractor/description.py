from tkinter import NORMAL, DISABLED
class Description:
    def __init__(self,x) -> None:
        self.info = x.info
        pass

    def description_adder(self,x):
        if "youtube" in x.URL or "youtu.be" in x.URL:
            try:
                _length = str(self.info['duration_string'])
            except:
                _length = ''
            
            _desc = str(self.info['description'])
            _title = str(self.info['title'])
            _channel = str(self.info['uploader'])
            _categories = str(self.info['categories'][0])
            _views = str(self.info['view_count'])
            _pbdate = str(self.info['upload_date'])
            _pbdate=_pbdate[0:4]+"-"+_pbdate[4:6]+"-"+_pbdate[6:]
            _thumbnail = str(self.info['thumbnail'])
            try:
                self._data = _title + "\n\nDuration: " + _length + " |  Channel: " +_channel + "\n\nPublished on: "+_pbdate + " |  Views: "+_views + "\n\nCategory : " + _categories + "\n\nDescription\n"+_desc + "\n\nThumbnail\n"+_thumbnail

            except:
                pass
        
        else:
            try:
                _title = self.info['title']
                _length = self.info['duration_string']
                _desc = self.info['description_string']
            except:
                pass

        x.description_box.config(state=NORMAL)
        x.description_box.delete(1.0,"end")
        x.description_box.insert(1.0, self._data)
        x.description_box.configure(state=DISABLED)
        x.status.set('')