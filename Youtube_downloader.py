from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

screen = Tk()

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_feild.get()

    user_path = path_label.cget("text")
    screen.title("Downloading......")

    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title("Download Completed! Download another file....")

title = screen.title("Youtube Downloader")
screen.iconbitmap("you.ico")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_image = PhotoImage(file="yt.png")
logo_image = logo_image.subsample(2,2)

canvas.create_image(250, 80, image=logo_image)

link_feild = Entry(screen, width=50)
link_label = Label(screen, text="Enter the YouTube link", font=('Roboto', 15))

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_feild)

path_label = Label(screen, text="Select the path for Download", font=('roboto', 15))
select_btn = Button(screen, text="Select", command=select_path)

canvas.create_window(240, 270, window=path_label)
canvas.create_window(400, 270, window=select_btn)

dwnd = PhotoImage(file="R.png")
download_btn = Button(screen, image=dwnd, borderwidth=0, command=download_file , text="Download", font=('roboto',15))
canvas.create_window(250,390, window=download_btn)




screen.mainloop()