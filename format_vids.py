#!/usr/bin/python3
import json
import sys

assert len(sys.argv) == 2

lines = []
name = sys.argv[-1]
with open(name, "r") as f:
    lines = f.readlines()

videos=[]

for line in lines:
    line=json.loads(line)
    videos.append(line["url"])

with open(name, "w") as f:
    for vid in videos:
        f.write(vid)
        f.write("\n")

