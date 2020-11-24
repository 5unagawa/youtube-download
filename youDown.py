#!/usr/bin/env python
import ffmpeg
import os

from pytube import YouTube

yt = YouTube(input())

#get video url from user
print(yt.title)
stream = yt.streams.filter(only_audio=True).first()
print(stream)
print("Downloading video...")
stream.download()
print("Video downloaded. Converting to MP3.")

#convert mp4 to mp3 using ffmpeg
myfile = ffmpeg.input(yt.title + ".mp4")
myfile = ffmpeg.output(myfile, yt.title + ".mp3")
ffmpeg.run(myfile)
#delete mp4 version
os.remove(yt.title + ".mp4")
print("Complete")
