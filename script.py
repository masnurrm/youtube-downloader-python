# https://www.youtube.com/watch?v=BTvukP5Au5g&ab_channel=PCCSmada

import pytube
video_link = 'https://www.youtube.com/watch?v=BTvukP5Au5g&ab_channel=PCCSmada'
yt = pytube.YouTube(video_link)
video = yt.get('mpeg', '720p')
path = '/Users/ACER/Desktop'
video.download(path)