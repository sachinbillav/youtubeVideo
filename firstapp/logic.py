from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys

def viewLogic(link):
    try:
        url = link
        yt = YouTube(url)
        return [yt.title,yt.thumbnail_url]
    except:
        return "ERROR"

def downloadLogic(link):
    try:
        def progress_function(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            sys.stdout.write(f"\rDownload progress: {percentage_of_completion:.2f}%")
            sys.stdout.flush()

        # Get the URL from user input
        url = link

        # Create a YouTube object with a progress callback
        yt = YouTube(url, on_progress_callback=progress_function)

        # Print the title of the video
        print(yt.title)

        # Get the highest resolution stream
        ys = yt.streams.get_highest_resolution()

        # Download the video
        ys.download()

        print("\nDownload complete.")
    except:
        pass
#downloadLogic("https://youtu.be/I5x8lAVQ8QQ?si=Jkcw7H7vAT9BNUxF")