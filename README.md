# yt-clipboard-downloader
Automatically downloads content from youtube URLs as they're copied to the computer's clipboard

Uses the packages 'tkinter' and 'youtube_dl' to read the computer's clipboard, and automatically perform download
actions on youtube URLs

USAGE:
./ytdownload.py [PATH] [-v]

PATH specifies the directory to download audio/video into
	     ('downloads' by default)
-v   download the full video (Audio only by default)

FUNCTIONALITY:
  On successful download, the audio/video is stored in the specified folder, and its ID is stored in a .csv file;
  to prevent duplicate downloads

TROUBLESHOOT:
	If unexpected errors occur, make sure youtube_dl is up to date with:
	"pip install --upgrade youtube_dl"
