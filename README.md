# ytdl
A GUI program that runs on top of youtube-dl and ffmpeg to download videos and audio.This project is only for educational purpose.
![startup](https://user-images.githubusercontent.com/55890376/115924152-fcea5080-a49c-11eb-8b71-a1e475ef69a2.JPG)

paste url and hit enter to view streams
![streams](https://user-images.githubusercontent.com/55890376/115923749-5605b480-a49c-11eb-8a8f-c412729a84ad.JPG)

select audio ,video and caption stream(s).

watch demo here-https://user-images.githubusercontent.com/55890376/114445050-398c9100-9bed-11eb-9b17-aea0be0704d8.mp4

#Insatllation

Download youtube-dl GUI installer here https://github.com/sourabhkv/ytdl/releases
Click the download button
![installer_startup](https://user-images.githubusercontent.com/55890376/115924610-99acee00-a49d-11eb-99c5-86e2b1a281b4.JPG)

Click Launch button after downloading.
You are ready to go.

#Working

youtube-dl searches streams available in website and displays streams.
*sometimes there may only be only video stream(s) available or no streams at all*.
User selects streams and browse location *default location in downloads*.
ffmpeg converts it into videos/audios.
if m4a is selected audio format ffmpeg uses AtomicParsley.
Pygame window displays live download progress.
Supported Websites -http://ytdl-org.github.io/youtube-dl/supportedsites.html
youtube-dl         -https://github.com/ytdl-org/youtube-dl
ffmpeg             -https://ffmpeg.org/ffmpeg.html
AtomicParsley      -http://atomicparsley.sourceforge.net/
Pygame             -https://www.pygame.org/wiki/about
