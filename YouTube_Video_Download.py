'''Start
  ↓
Get URL input from user
  ↓
Ask user: Download (1) Video or (2) Audio?
  ↓
If Video:
  ↓
Ask user: Choose resolution (e.g. 720p, 480p, 360p)
  ↓
Set yt-dlp format option accordingly
Else if Audio:
  ↓
Set yt-dlp format for audio only
  ↓
Ask user for save path (default current folder if empty)
  ↓
Configure yt-dlp output template with path
  ↓
Call yt-dlp download function
  ↓
Download completes successfully
  ↓
End
'''
import yt_dlp

url = input("Enter the YouTube video URL:\n")
choice = input("Download (1) Video or (2) Audio? Enter 1 or 2:\n")
if choice == '1':
    resolution = input("Enter max resolution (like 720, 480, 360):\n")
else:
    resolution = None
save_path = input("Enter folder path to save (press Enter for current folder):\n")
if not save_path:
    save_path = '.'  # current directory
if choice == '1':
    # Video + audio, max resolution from user
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s'
    }
else:
    # Audio only, convert to mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download complete!")
except Exception as e:
    print("Oops! Something went wrong:", e)
