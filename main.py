import time
from tkinter import *
import downloadfun

# create root window
root = Tk()

# root window title and dimension
root.title("youtube downloader")
root.geometry('350x200')

checkmessage = "please select if you would like a copy to be saved as an mp3"
checked = IntVar()

def download_vid():
    linksave = link.get()
    mp3option = checked.get()
    link.delete(0, END)
    checked.set(0)
    time.sleep(2)
    inputbut = Button(root, text="Download", command=download_vid, state=DISABLED)
    #downloadfun.downloadyt(linksave)


# adding a label to the root window
lbl = Label(root, text = "paste the link here")
link = Entry(root, width=50)
mp3_choice = Checkbutton(root, text=checkmessage, variable=checked)
inputbut = Button(root, text="Download", command=(download_vid, download_vid))

lbl.grid(column=0, row=0)
link.grid(column=1, row=0)
mp3_choice.grid(column=0, row=1, columnspan=5)
inputbut.grid(column=0, row=2)



# Execute Tkinter
root.mainloop()

