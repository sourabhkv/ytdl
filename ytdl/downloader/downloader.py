import yt_dlp
from datetime import timedelta
from pprint import pprint

class Downloader:
    def __init__(self,x) -> None:
        self.y = x

    def cli_to_api(self,opts):
        default = yt_dlp.parse_options([]).ydl_opts
        diff = {k: v for k, v in yt_dlp.parse_options(opts).ydl_opts.items() if default[k] != v}
        if 'postprocessors' in diff:
            diff['postprocessors'] = [pp for pp in diff['postprocessors'] if pp not in default['postprocessors']]
        
        myopts_opts = {
            'logger': MyLogger(self.y),
            'progress_hooks': [self.my_hook],
        }
        ydl_opts = {**myopts_opts, **diff}
        return ydl_opts
    
    def my_hook(self,d):
        try:
            if d['status'] == 'finished':
                self.y.status.set(' Done downloading, now post-processing ...')
                self.y.status.set(d['filename'])
            if d['status'] == 'downloading':
                self.y.status.set('[download] '+d['_default_template'])
            else:
                self.y.status.set(' Download complete')
        except:
            pass
    
    def start_download(self,ydl_opts):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.y.url_box.get()])

class MyLogger:
    def __init__(self,y) -> None:
        self.z = y
        
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        self.z.status.set(' '+msg)