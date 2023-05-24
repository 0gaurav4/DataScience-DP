
    
from pytube import YouTube

url = input()
my_video = YouTube(url)

print("***************************")
print(my_video.title)

print("***************************")
print(my_video.thumbnail_url)

print("***************************")

my_video = my_video.streams.get_by_resolution('360p')

my_video.download()


