# yt-clipboard-downloader

Automatically downloads content from youtube URLs as they're copied to the computer's clipboard

NOTE: It only semi-works in windows. Tkinter's clipboard selection behaves differently in a windows environment, and the dependencies of youtube_dl work differently as well; not including the codecs to output to MP3. It does work fantastic in Ubuntu 18.04 though

Uses the packages 'tkinter' and 'youtube_dl' to read the computer's clipboard, and automatically perform download
actions on youtube URLs

USAGE:

    ./ytdownload.py [PATH] [-v]

    PATH = Directory to download files into
    -v   = 'download entire video' flag (audio only by default)

FUNCTIONALITY:
  On successful download, the audio/video is stored in the specified folder, and its ID is stored in a .csv file;
  to avoid duplicate downloads

TROUBLESHOOT:
	If unexpected errors occur, make sure youtube_dl is up to date with:
	"pip install --upgrade youtube_dl"
