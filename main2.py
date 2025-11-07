from pytube import YouTube
import mp4tomp3
import time
print("welcome to Refael's YouTube download script")
while True:

    convert = mp4tomp3.downloadyt()
    if convert == "yes":
        print("this might take a moment please have patience")
        mp4tomp3.convert()


    keepgoing = input("would you like to download another video")

    if keepgoing != "yes":
        print("thanks for using this service")
        time.sleep(5)
        exit(7)
