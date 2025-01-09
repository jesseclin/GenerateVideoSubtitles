class time_process:
    """
    A class to process the time in seconds to the correct format.
    Attributes:
        need_process (int): The time in seconds.
    
    Methods:
        process(): Convert the time in seconds to the correct format.
    """
    def __init__(self,need_process):
        self.secondsProcess = need_process
    def process(self):
        hours = self.secondsProcess // 3600
        minutes = (self.secondsProcess % 3600) // 60
        seconds = self.secondsProcess % 60
        milliseconds = (seconds - int(seconds)) * 1000
        # Return the time in the correct format, for example: 00:00:00,000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}"