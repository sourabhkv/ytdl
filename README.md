# ytdl
A GUI program that runs on top of youtube-dl and ffmpeg to download videos and audio.**This project is only for educational purpose DO NOT SELL .**<br />
![window1](https://user-images.githubusercontent.com/55890376/118402205-8816ca80-b686-11eb-8c19-c4a15ec08f77.JPG)


paste url and hit enter to view streams and thumbnail<br />
TO download thumbnail click **Download thumbnail**<br />
![window2](https://user-images.githubusercontent.com/55890376/118402227-a67cc600-b686-11eb-9ea1-d52a33b617ba.JPG)


Select audio ,video and caption stream(s).<br />
Click **Browse** to browse the location where video/audio will be saved **if not clicked default browse location is downloads**<br />

<h1>Stream selection</h1>
If you have VLC not installed try selecting video with codec avc1 and audio with m4a it will work.
If audio and video codecs are webm then output is webm else it is mp4<br />

<h3>Music</h3>
mp3 64K, mp3 320K, m4a, wav, flac available<br />
m4a,mp3 320K includes thumbnail and Metadata<br />

[watch demo here](https://user-images.githubusercontent.com/55890376/114445050-398c9100-9bed-11eb-9b17-aea0be0704d8.mp4)

<h1>INSTALLATION</h1>

Download youtube-dl GUI installer [here](https://github.com/sourabhkv/ytdl/releases)<br />
![setup](https://user-images.githubusercontent.com/55890376/118402262-c57b5800-b686-11eb-9eed-61a32933748b.JPG)
![setup2](https://user-images.githubusercontent.com/55890376/118402273-d3c97400-b686-11eb-8aca-445a2d26cacc.JPG)
![start](https://user-images.githubusercontent.com/55890376/118402353-3884ce80-b687-11eb-91a6-d999a675d288.JPG)


Click Launch button after downloading.<br />
You are ready to go 🤘.<br />

<h1>WORKING</h1>

youtube-dl searches streams available in website and displays streams.
*sometimes there may only be only video stream(s) available or no streams at all.Using VPN might help.*
User selects streams and browse location *(default location in downloads)*.
ffmpeg converts it into videos/audios.
if m4a is selected audio format ffmpeg uses AtomicParsley to write metadata in m4a file.
Pygame window displays live download progress(for older version).<br />


[Supported Websites](http://ytdl-org.github.io/youtube-dl/supportedsites.html)<br />
[youtube-dl](https://github.com/ytdl-org/youtube-dl)<br />
[ffmpeg](https://ffmpeg.org/ffmpeg.html)<br />
[AtomicParsley](http://atomicparsley.sourceforge.net/)<br />
[Pygame](https://www.pygame.org/wiki/about)<br />
[try VLC for better playback](https://www.videolan.org/)<br />
