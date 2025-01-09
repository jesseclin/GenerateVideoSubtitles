import yt_dlp
import re
from tqdm import tqdm
class Download:
    """
    A class to download audio files from YouTube using yt-dlp.
    Attributes:
        url (str): The URL of the YouTube video.
        output_path (str): The path to save the downloaded audio file.
        fixed_filename (str): The filename of the downloaded audio file without special characters.
    
    Methods:
        remove_special_characters(filename): Remove special characters from the filename.The purpose is to use this name as the file name.
        download_m4a(): Download the m4a file from the YouTube video.
    """
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path
        self.fixed_filename = self.remove_special_characters(url.split('=')[-1])
    
    
    def remove_special_characters(self, filename):
        return re.sub(r'[^a-zA-Z0-9]', '', filename)
        
    
    def download_m4a(self):
        progress_bar = None

        # Progress hook for the progress bar
        # if the status is 'downloading', update the progress bar
        # if the status is 'finished', close the progress bar
        def progress_hook(d):
            nonlocal progress_bar
            if d['status'] == 'downloading':
                clean_percent_str = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', d['_percent_str'])
                percent = float(clean_percent_str.strip('%'))
                progress_bar.n = percent
                progress_bar.refresh()
            elif d['status'] == 'finished':
                progress_bar.n = 100
                progress_bar.close()
                print(f"下載完成：{d['filename']}")

        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/best[ext=m4a]',                       #downloading the best audio quality
            'progress_hooks': [progress_hook],                                  #progress bar
            'outtmpl': f'{self.output_path}/{self.fixed_filename}.%(ext)s',     #output path
            'postprocessors': [],                                               #no postprocessing
            'nooverwrites': False,                                              #overwrite existing files
            'quiet': True,                                                      #no logging                               
            'noprogress':True                                                   #no progress messages
        }

        # Display time information and show progress bar while downloading the file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            
            info = ydl.extract_info(self.url, download=False)
            print("影音長度："+str(info['duration'])+"秒")
            progress_bar = tqdm(total=100, desc="下載進度：", unit="%")
            ydl.download(self.url)
            filename = ydl.prepare_filename(info)
            # Return the file name, which refers to the path, for example: ./video_id.m4a
            return filename
