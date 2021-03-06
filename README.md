# yt-clipboard-downloader

Automatically downloads content from youtube URLs as they're copied to the computer's clipboard

DEPENDANCIES:
    
    pip package  :  youtube-dl
    apt packages :  ffmpeg python3-tk

    youtube-dl   - An open source youtube downloader project that keeps up to date as changes are made to youtube
    ffmpeg       - An audio/video conversion package, needed to convert webm to mp3 in this project
    python3-tk   - Adds the standard python GUI library tkinter, if you don't have it installed already.
                   Used in this project for its access to the clipboard
    
NOTE: 

It only semi-works in windows due to tkinter's clipboard selection behaving differently in a windows environment, and ffmpeg having a different installation process in windows (the package for converting from the default format of webm, to mp3). It does work fantastic in Ubuntu 18/20 though. This script uses the packages 'tkinter' to read the computer's clipboard, and 'yotube-dl' to perform download actions on youtube URLs

USAGE:

    ./ytdownload.py [PATH] [-v]

    PATH = Directory to download files into
    -v   = 'download entire video' flag (audio only by default)

FUNCTIONALITY:

After the script is started, it watches the computer's clipboard, and detects any youtube URLs with regex; automatically starting the download with the settings specified in the command line arguments. On successful download, the audio/video is stored in the specified folder, and its ID is stored in a .csv file; to avoid duplicate downloads

TROUBLESHOOT:

If unexpected errors occur, make sure youtube_dl is up to date with:
    
    pip install --upgrade youtube-dl
