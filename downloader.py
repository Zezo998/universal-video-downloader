import yt_dlp
import sys
import os

def download_video(url, output_path='downloads'):
    """
    Downloads a video from a given URL using yt-dlp.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for: {url}")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 downloader.py <video_url>")
        print("Example: python3 downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        video_url = sys.argv[1]
        download_video(video_url)
