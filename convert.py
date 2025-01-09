from moviepy.editor import AudioFileClip
import os

class AudioConvert:
    """
    Convert audio files of different formats to wav files

    Attributes:
        input_path (str): The path to the audio file.
        output_path (str): The path to save the converted audio file.

    Methods:
        change_extension_to_wav(input_file_path): Change the file extension to wav.
        convert_to_wav(): Convert the audio file to a wav file.
    """


    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    # Change the file extension to wav
    # input_file_path: The path to the audio file
    # return: The path to the wav file,like "C:/Users/xxx/xxx.wav"
    def change_extension_to_wav(self,input_file_path):
        base = os.path.splitext(input_file_path)[0]
        new_file_path = base + '.wav'
        return new_file_path

    # Convert the audio file to a wav file
    # return: The path to the wav file,like "C:/Users/xxx/xxx.wav"
    def convert_to_wav(self):
        # Check if the file is already a wav file
        if self.input_path[-3:] == 'wav':
            return "已經是wav檔案"
        #final_output_path means the path of the converted wav file
        self.final_output_path = self.change_extension_to_wav(self.input_path)
        audio = AudioFileClip(self.input_path)
        audio.write_audiofile(self.final_output_path)
        return self.final_output_path
    
