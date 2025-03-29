from pytubefix import YouTube
from pytubefix.cli import on_progress

def yt_downloader(location, url, type):    
    yt = YouTube(url, on_progress_callback=on_progress)
    if type == 'A':   
        resolution = yt.streams.get_audio_only()  
    elif type == 'V':
        resolution = yt.streams.get_highest_resolution()
    else:
        print("❌ Entered a wrong command. Type 'A' or 'V'.")
        
    try:
        print(f"Downloading {yt.title} ...")
        resolution.download(output_path=location)
        print(f"{'🎵 Audio' if type=='A' else '🎥 Video'} Downloaded Successfully!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = input('Enter the YT URL : ').strip()
    type = input('Enter the YT Source Required Type (Audio: A / Video: V) : ').strip().upper()
    location = 'ytDownloader'
    yt_downloader(location, url, type)