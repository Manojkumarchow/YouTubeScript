import pytube
video_link = "https://www.youtube.com/watch?v=eB4SpD4B0Og"
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download('D://Manoj')