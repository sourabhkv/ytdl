import urllib.request
import json
link = "https://api.github.com/repos/sourabhkv/ytdl/releases/latest"
#https://api.github.com/repos/sourabhkv/ytdl/releases

data = urllib.request.urlopen(link)
jx = data.read().decode()
data.close()
final = json.loads(jx)
print(final['tag_name'],final['published_at'])