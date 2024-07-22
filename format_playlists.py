#!/usr/bin/python3

import json

lines = []
with open("/home/mac/youtube-backup/LEDGER/playlists.txt", "r") as f:
    lines = f.readlines()

playlists=[]
playlist_names=[]

for line in lines:
    line=json.loads(line)
    playlists.append(line["url"])
    playlist_names.append(line["title"])


with open("/home/mac/youtube-backup/LEDGER/playlists.txt", "w") as f:
    for i, playlist in enumerate(playlists):
        name = playlist_names[i]
        f.write(playlist + " " + name + "\n")



