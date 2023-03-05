$url = "https://github.com/sourabhkv/ytdl/releases/latest/download/YouTube-dl.GUI.exe"
$outputPath = ".\Youtube-dl GUI.exe"
Write-Host "Install Youtube-dl GUI (ytdl)"
$res = Read-Host "(y/N)"
if ($res -eq "y"){
    Write-Host "Downloading. . . "
    Invoke-WebRequest $url -OutFile $outputPath
    Write-Host "Installing. . . "
    Start-Process $outputPath
}
else{
    Exit(0)
}