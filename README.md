# <br>ytdl ![output-onlinepngtools](https://user-images.githubusercontent.com/55890376/147201322-7cb830c8-9a47-4bbb-ad0b-d79d4c09b58a.png)
</br>


A GUI program that runs on top of yt-dlp and ffmpeg to download videos and audio.**This project is only for educational purpose DO NOT SELL . USE AT YOUR RISK .**<br />

![me at zoo](https://user-images.githubusercontent.com/55890376/158213036-ab4a1d93-6661-496e-aae4-27d58658d74e.png)








![new](https://user-images.githubusercontent.com/55890376/148672374-69d952c3-3cb8-4193-b537-dac05f2a74b2.png)





paste url and hit enter/GO to view streams and thumbnail<br />
TO download thumbnail click **Download thumbnail**<br />
![ytdlgui3](https://user-images.githubusercontent.com/55890376/146916497-d6422aaa-ea57-4bdc-bf44-e336a1034aba.jpg)

<br>Version 22.208.02 and above with dark theme and categorized data.</br>

![youtube-dl GUI new](https://user-images.githubusercontent.com/55890376/154851022-a187920a-cd3e-4b81-8d4d-b4d77b1095d6.jpg)









Select audio ,video and caption stream(s).<br />
Click **Browse** to browse the location where video/audio will be saved **if not clicked default browse location is downloads**<br />

<h2>Special features</h2>
Captions support (YouTube)<br />
Thumbnail download </br>
Advanced option to specifically select audio , video separately </br>
Convert video into music MP3(64,128,320 KB/S), M4A , WAV ,FLAC WITH METADATA</br>
Varirty of [supported websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)</br>
File converter</br>

<h2>Coming features</h2>
Better playlist support.
Multi video download.

<h2>Stream selection</h2>
If you have VLC not installed try using these combination.
Recommended combination of audio and video codecs<br />
MP4 -->   video: avc1 & audio: m4a <br />
WEBM -->  video: webm & audio :webm <br />
NOTE : Files are converted into MKV format since other combination are incompatible<br />

<h4>Music</h4>
mp3 64K, mp3 320K, m4a, wav, flac available<br />
m4a, mp3 320K, flac includes thumbnail and Metadata<br />
flac , wav formats takes more space than mp3 and m4a
<br />

<h4>Playlist</h4>
Currently supports Youtube playlist
Enter playlist url select format(144p,240p...,mp3,m4a) hit download


[New version demo](https://drive.google.com/file/d/1OaQTnjXC8wvLKSkWYx_8j8pEyUu7IYXq/view?usp=sharing)</br>

Older version [watch demo here](https://user-images.githubusercontent.com/55890376/114445050-398c9100-9bed-11eb-9b17-aea0be0704d8.mp4)</br>

<h2>INSTALLATION</h2>

Download youtube-dl GUI latest installer [here](https://github.com/sourabhkv/ytdl/releases/latest)<br />


![setup complete](https://user-images.githubusercontent.com/55890376/156933091-b3e380c3-0673-4baa-9c1d-4667d5a52f4d.png)





Click Launch button after downloading.<br />
You are ready to go 🤘.<br />

<h2>WORKING</h2>

yt-dlp (youtube-dl for older version) searches streams available in website and displays streams.
*sometimes there may only be only video stream(s) available or no streams at all.Using VPN might help.*
User selects streams and browse location *(default location in downloads could be changed)*.
ffmpeg converts it into videos/audios.
if m4a is selected audio format ffmpeg uses AtomicParsley to write metadata in m4a file.
Pygame window displays live download progress(for older version).<br />

<h2>How development started and was carried?</h2>
<br>This project development started with wish to download youtube physics video(Center of mass) at 240p in March,2021 because 240p quality was managable and took decent amount of mobile data compared to 360p.<br />
<br>Many people don't have technical knowledge of how to use youtube-dl/yt-dlp command line, to make things easier to use ,I thought of making GUI version of youtube-dl/yt-dlp for those having no knowledge about command line program.<br />
Initially it was a very basic program which lack many features as time passed encountered many bugs and fixed it ,specially giving the live download progress in main window statusbar took almost 2 months to fix this , removing black console window at startup  was also challenging to fix without using --noconsole option.
<br>
Threading helped execute many function at same time<br />
The function popens(cmd) never executed with object oriented programming (OOPs)</br>
Tkinter was easy to use and took less space compared to PySide2/PyQt5</br>
After june,2021 there was no update to youtube-dl. Development stopped for 3 months finally backend changed to yt-dlp</br>
During this development period many bugs were encountered and fixed , many features were added ,hope this project will be active in future...</br>
Need help to make this better so that anyone with poor internet connctivity can learn somthing.<br />



<br>[Supported Websites](http://ytdl-org.github.io/youtube-dl/supportedsites.html)</br>
[youtube-dl](https://github.com/ytdl-org/youtube-dl)<br />
[yt-dlp](https://github.com/yt-dlp/yt-dlp)<br />
[Pytube](https://pytube.io/en/latest/)<br />
[ffmpeg](https://ffmpeg.org/ffmpeg.html)<br />
[AtomicParsley](http://atomicparsley.sourceforge.net/)<br />
[Pygame](https://www.pygame.org/wiki/about)<br />
[Inno Setup](https://jrsoftware.org/isinfo.php)<br />
