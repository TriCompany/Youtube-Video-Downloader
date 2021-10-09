
from pytube import YouTube
SAVE_PATH = "E:/" #to_do
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception
mp4files = yt.filter('mp4')


yt.set_filename('GeeksforGeeks Video')


d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
