import youtube_dl


def download(link, location):
    ydl = youtube_dl.YoutubeDL({'outtmpl': location + "%(title)s.%(ext)s"})
    with ydl:
        ydl.download([link])
        return "Finished"


download("https://www.youtube.com/watch?v=yDH5J0moTro", "Downloads/")
