#!/usr/bin/python3
from tkinter import Tk
from tkinter import TclError
from youtube_dl import YoutubeDL
import re
import sys
import os

#References
#Downloading audio track       https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
#Specifying download location  https://github.com/ytdl-org/youtube-dl/issues/13459

def main():
    #Default flags (saving audio)
    saveVideo = False
    dupeFile = 'saved-audio.csv'

    #Change default flags if saving video
    if '-v' in sys.argv:
        saveVideo = True
        dupeFile = 'saved-video.csv'
        sys.argv.remove('-v')

    #Get folder to store tracks in from command line arguments
    if len(sys.argv) > 1:
        folder = sys.argv[1]
        #Strip off trailing slash if it exists
        if folder[-1] == '/' or folder[-1] == '\\':
            folder = folder[:-1]
    else:
        folder = 'downloads'

    #Create directories and files if they don't exist
    if not os.path.isdir(folder):
        os.makedirs(folder)
    if not os.path.isfile('saved-audio.csv'):
        open('saved-audio.csv','a').close()
    if not os.path.isfile('saved-video.csv'):
        open('saved-video.csv','a').close()

    #youtube_dl download options for audio as mp3
    dl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{folder}/%(title)s-%(id)s.%(ext)s',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    #If video flag is specified, use default video download options (except for output path, and not breaking the script on error)
    if saveVideo:
        dl_opts = {
            'ignoreerrors': True,
            'outtmpl': f'{folder}/%(title)s-%(id)s.%(ext)s'
        }

    #Print landing message
    print(f"""{'-'*50}\nYoutube clipboard downloader - By chrispyth42\nUses the packages 'tkinter' and 'youtube_dl'\nListens to PC's clipboard, and downloads from any youtube URLs\n\nUSAGE:\n\t./ytdownload.py [PATH] [-v]\n\n\tPATH specifies the directory to download audio/video into\n\t     ('downloads' by default)\n\t-v   download the full video (Audio only by default)\n\nTROUBLESHOOT:\n\tIf unexpected errors occur, make sure youtube_dl is up to date with:\n\t"pip install --upgrade youtube_dl"\n\n{'-'*50}""")
    if not saveVideo:
        landing = f"Setting: Saving AUDIO into folder '{folder}'\nStatus:  Waiting for youtube links to be copied (ctrl-c to exit)..."
    else:
        landing = f"Setting: Saving VIDEO into folder '{folder}'\nStatus:  Waiting for youtube links to be copied (ctrl-c to exit)..."
    print(landing)

    #Create hidden tkinter root window for its access to the clipboard
    root = Tk()
    root.withdraw()

    #clipboard_get breaks when there's nothing in the clipboard. This ensures that it always at least starts with something
    try:
        current = root.clipboard_get()
    except TclError:
        root.clipboard_append(' ')
        current = ''

    #Outer try block for handling keyboard interrupt
    try:
        #Loop forever
        while True:
            #If the clipboard changed, test its contents
            clip = root.clipboard_get()

            if clip != current:
                current = clip
                
                #Extract all youtube links from the paste data
                vids = re.findall(r'(https?://www.youtube.com/watch\?v=[a-zA-Z0-9_\-]{11})|(https?://youtu.be/[a-zA-Z0-9_\-]{11})',clip)

                #If non-empty result, iterate through the list of lists to get each youtube video url
                if vids:
                    for match in vids:
                        for v in match:
                            if v:
                                #Extract just the video ID from either youtube url format
                                if '=' in v:
                                    id = v.split('=')[1]
                                else:
                                    id = v.split('/')[3]

                                #Check store of already saved audio/video to ensure no dupes
                                savedSongs = open(dupeFile,'r')
                                isSaved = False
                                for line in savedSongs:
                                    line = line.strip().split(',')
                                    if line[0] == id:
                                        isSaved = line[1]
                                        break
                                savedSongs.close()
                                
                                #If something isn't saved, download it, then update the csv 
                                if not isSaved:
                                    #Save track
                                    if saveVideo:
                                        print(f'{"-"*50}\nSaving video...')
                                    else:
                                        print(f'{"-"*50}\nSaving audio...')
                                        
                                    dl = YoutubeDL(dl_opts)
                                    res = dl.download([v])

                                    #If the download returns a good status code (0), update CSV and return success message
                                    if not res:
                                        #Update CSV
                                        savedSongs = open(dupeFile,'a')
                                        savedSongs.write(f"{id},{folder}\n")
                                        savedSongs.close()
                                        
                                        #Notify that it's done
                                        print(f'\nDownload Complete\n{"-"*50}')

                                    #Else don't do that
                                    else:
                                        print(f'\nA problem ocurred when loading the selected video.\n{"-"*50}')

                                #If something's already saved, notify the user of its recorded location
                                else:
                                    print(f"\n!! Already saved in folder '{isSaved}'\n{'-'*50}")

                    #Re-print landing message at end of for loop to indicate that it's ready again
                    print(landing)

    #Gently exit on keyboard interrupt
    except KeyboardInterrupt:
        print('\nSee you later!')

main()