import yt_dlp
from datetime import timedelta
from pprint import pprint

class Downloader:
    def __init__(self) -> None:
        pass

    def cli_to_api(self,opts):
        default = yt_dlp.parse_options([]).ydl_opts
        diff = {k: v for k, v in yt_dlp.parse_options(opts).ydl_opts.items() if default[k] != v}
        if 'postprocessors' in diff:
            diff['postprocessors'] = [pp for pp in diff['postprocessors'] if pp not in default['postprocessors']]
        
        myopts_opts = {
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
        }
        ydl_opts = {**myopts_opts, **diff}
        return ydl_opts
    
    def my_hook(self,d):
        try:
            if d['status'] == 'finished':
                print('Done downloading, now post-processing ...')
                print(d['filename'])
            if d['status'] == 'downloading':
                if d['eta']:
                    print(str(timedelta(seconds=d['eta'])),"%0.2f" %(d['downloaded_bytes']/d['total_bytes']))
                else:
                    print('-:-:- ',"%0.2f" %(d['downloaded_bytes']/d['total_bytes']))
            else:
                print('Download complete')
        except:
            pass
    
    def start_download(self,ydl_opts,x):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([x.url_box.get()])

class MyLogger:
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
        print(msg)