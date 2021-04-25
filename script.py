from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=6gTLL_wgRFk&ab_channel=011_NurMuhammadAinulYaqin").streams.first().download()