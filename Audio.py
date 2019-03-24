import moviepy.editor as mp
video = mp.VideoFileClip("The Best Way to Prepare a Dataset Easily.mp4")
video.audio.write_audiofile("test.mp3")
