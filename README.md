# Universal Video Downloader

A simple command-line tool for downloading videos from hundreds of sites (YouTube, Vimeo, X/Twitter, and more), powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Works with every site yt-dlp supports
- Downloads the best available video and audio quality
- Saves files into a `downloads/` folder (created automatically) with the video title as the filename
- Downloads a single video at a time, even when the URL belongs to a playlist
- Prints progress to the console while downloading

## Requirements

- Python 3.x
- yt-dlp (installed via `requirements.txt`)
- ffmpeg, needed to merge the separate best-quality video and audio streams

## Installation

```bash
git clone https://github.com/Zezo998/vidgrab.git
cd vidgrab
pip install -r requirements.txt
```

## Usage

```bash
python3 downloader.py "VIDEO_URL"
```

Example:

```bash
python3 downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

The video is saved to `downloads/<video title>.<ext>` in the current directory.

## How it works

`downloader.py` takes a video URL as a command-line argument and passes it to yt-dlp with the format selector `bestvideo+bestaudio/best`, so it grabs the best separate video and audio streams and merges them, falling back to the best single file when merging is not possible. The `noplaylist` option keeps the download to one video even if the URL is part of a playlist.

## Disclaimer

This tool is for educational purposes only. Respect the terms of service of the platforms you download from, and only download content you have the right to download.
