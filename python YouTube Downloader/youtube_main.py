from pytube import YouTube
import sys 



#link = "https://www.youtube.com/watch?v=ut-RE4QsJnc"

link = str(input("Input Your Youtube Video Link :- "))
path = input("Input Your Download path :- ")


try:
    yt = YouTube(link)
    print(f"Channal Title  :- {yt.author}")
    print(f"Video title :- {yt.title}")
    #print(f"Video description :- {yt.description}")
    print(f"Video views :- {yt.views}")

except:
    print("wrong link")





def youtube_downloader_highest_resolution(self):
    download = yt.streams.get_highest_resolution()
    download.download(path)
    return "please wait..."

def youtube_downloader_highest_resolution(self):
    download = yt.streams.get_lowest_resolutione()
    download.download(path)
    return "please wait..."

def youtube_audio_downloader(self):
    download = yt.streams.get_audio_only()
    download.download(path)
    return "please wait..."


if "__main__" == "__name__":
    pass
