import sys

__license__ = 'Public Domain'

if __package__ is None:
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import ytdl

if __name__=="__main__":
    ytdl.main(sys.argv)