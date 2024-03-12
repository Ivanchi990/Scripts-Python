from tkinter import *
from pytube import YouTube

window = Tk()

window.geometry('500x350')
window.resizable(0, 0)
window.title("Youtube video downloader")

Label(window, text="Download yourvideo").place(x=120, y=40)

link = StringVar()
Label(window, text="Paste the link here: ").place(x=32, y=120)
link_enter = Entry(window, width=70, textvariable=link).place(x=32, y=150)

def download():
    url = YouTube(str(link.get()))
    
    video = url.streams.get_highest_resolution()
    video.download("C:\\Users\\Monica Perez\\Downloads")
    
    Label(window, text="Downloaded").place(x=180, y=240)
    
Button(window, text="Download", command=download).place(x=180, y=180)

window.mainloop()