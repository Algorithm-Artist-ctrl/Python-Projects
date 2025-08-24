from pytube import YouTube
def down_Youtube(url,save):
    try:
        yt=YouTube(url)
        print(yt.title)
        print(yt.length)
        vd720p=yt.streams.filter(progressive=True,file_extension="mp4").first()
        vedio=vd720p.steams.get_highest_resolution()
        vedio.download(save)
    except  Exception as e:
        print(e)
link=input("Enter the Url of Youtube video:\n")
path=input("Enter the path to save the vedio:\n")
down_Youtube(link,path)

