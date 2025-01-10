from faster_whisper import WhisperModel
import os
class speechToTextOnWhisperModel:
    """
    Convert speech to text using the Whisper model.
    Attributes:
        model_size (str): The size of the model.
        device (str): choose GPU or CPU.
        compute_type (str): The compute type to run the model.
        current_model_size (str): The current model size.
    
    Methods:
        setModelSize(model_size_input): Set the model size.
        setDeviceSetting(device_setting): Set the device.
        setComputeTypeSetting(compute_type_setting): Set the compute type.
        run_analyze(filename, sel_lang_option, return_list): Run the model in the subprocess
    """
    def __init__(self):
        self.model_size = None
        self.device = None
        self.compute_type = None
        self.current_model_size = None

    def setModelSize(self, model_size_input):
        self.model_size = model_size_input

    def setDeviceSetting(self, device_setting):
        self.device = device_setting

    def setComputeTypeSetting(self, compute_type_setting):
        self.compute_type = compute_type_setting

    def run_analyze(self, filename, sel_lang_option, return_list):
        # use absolute path
        # if the file does not exist, raise an error
        filename = os.path.abspath(filename)
        if not os.path.exists(filename):
            raise FileNotFoundError(f"檔案 {filename} 不存在，請確認路徑是否正確。")
        
        print("加載模型中...")
        # Load the model
        try:
            model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
        except Exception as e:
            raise ValueError(f"模型加載失敗: {e}")
        print("模型加載完成。")
        print("處理中...")

        # Run the model
        # choose the language option
        # Auto: automatically detect the language
        # Chinese: Chinese
        # English: English
        # Japanese: Japanese
        # transcript the audio file
        try:

            if sel_lang_option == "Auto":
                segments,_ = model.transcribe(filename, beam_size=5,log_progress=True)
                return_list[:] = list(segments)
            elif sel_lang_option == "Chinese":
                segments, _ = model.transcribe(filename, beam_size=5, language="zh",log_progress=True)
                return_list[:] = list(segments)
            elif sel_lang_option == "English":
                segments, _ = model.transcribe(filename, beam_size=5, language="en",log_progress=True)
                return_list[:] = list(segments)
            elif sel_lang_option == "Japanese":
                segments, _ = model.transcribe(filename, beam_size=5, language="ja",log_progress=True)
                return_list[:] = list(segments)
        except Exception as e:
            raise ValueError(f"模型運行失敗: {e}")
    