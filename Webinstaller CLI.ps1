$url = "https://github.com/sourabhkv/ytdl/releases/latest/download/YouTube-dl.GUI.exe"
$outputPath = ".\Youtube-dl GUI.exe"
Invoke-WebRequest $url -OutFile $outputPath
Start-Process $outputPath
