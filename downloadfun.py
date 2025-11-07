from moviepy.editor import *
import glob
import os
from pytube import YouTube


def newest():
    listfiles = glob.glob('C:\\Users\\katzr\\Downloads\\*.mp4')
    newestfile = max(listfiles, key = os.path.getctime)
    return newestfile

def convert():
    file = newest()
    filemp3 = file
    filemp3 = filemp3[:-3]
    mp3encode = ('mp3')
    filemp3save = filemp3 + mp3encode
    video = VideoFileClip(file)
    video.audio.write_audiofile(filemp3save)

def downloadyt(link):
    SAVE_PATH = "C:\\Users\\katzr\\Downloads"



    link = (link)
    print("please wait while we verify your link")
    yt = YouTube(link)

    try:
        mp4files = yt.streams.filter(progressive=True, file_extension='mp4')
        print("link accepted download starting")
    except:
        print("check your internet connection and try again")

    d_video = yt.streams.get_highest_resolution()

    try:
        d_video.download(SAVE_PATH)
    except:
        print("error 2")

    print("you're download is now complete and can be found under Downloads in File explorer")

    convert()

