from pytube import YouTube
url = "https://youtu.be/kPRVtuicLBs"
vid = YouTube(url)

print(vid.title)

#print(vid.thumbnail_url)
vid = vid.streams.get_highest_resolution()
# for i in vid.streams:
#     print(i)
vid.download()
