import tkinter
import customtkinter
from pytube import YouTube


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("YouTube Video Downloader")
app.geometry("720x480")


def download(format):
    try:
        yt_link = link.get()
        yt = YouTube(yt_link, on_progress_callback=on_progress)
        if (format == "video"):
            video = yt.streams.get_highest_resolution()
        else:
            video = yt.streams.get_audio_only()
        video.download()
        download_label.configure(text="Download finished!", text_color="white")
    except Exception as ex:
        download_label.configure(text=f"ERROR: {ex}", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    completion_percentage = bytes_downloaded / file_size * 100
    percentage = str(int(completion_percentage))
    progress.configure(text=f"{percentage}%")
    progress_bar.set(float(completion_percentage / 100))
    progress.update()


title = customtkinter.CTkLabel(app, text="Paste a YouTube link")
title.pack(padx=10, pady=15)

# URL input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download_label = customtkinter.CTkLabel(app, text="")
download_label.pack()

# download buttons
download_video_btn = customtkinter.CTkButton(
    app,
    fg_color="red",
    text="Dowload video",
    command=lambda: download("video"))
download_video_btn.pack(padx=10, pady=15)

download_mp4_btn = customtkinter.CTkButton(
    app,
    fg_color="red",
    text="Dowload as mp4",
    command=lambda: download("mp4"))
download_mp4_btn.pack(padx=10, pady=15)


# progress indicator
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progress_bar = customtkinter.CTkProgressBar(
    app, progress_color="red", width=450)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=15)

app.mainloop()
