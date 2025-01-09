# GenerateVideoSubtitles
This project allows converting audio from videos into text.
Features include:

1. Supports both online and local sources; currently, online sources are limited to YouTube.
2. Utilizes the faster-whisper model. You can select the model size. For accuracy, it is recommended to use large-v3-turbo. If your system lacks sufficient performance, you can choose small.
3. Outputs can be saved as srt or txt.
4. The supported video languages are virtually unlimited, but English provides the best results. For Chinese, the output will be in Traditional Chinese.
5. Local file support includes mp3, m4a, and wav formats.

Environment:
Driver Version: 566.03
CUDA Version: 12.7
CUDA Toolkit 12.6 Update 2
cuDNN v9.5


Requirements:
CUDA installation is required.
At least 3–4 GB of memory is recommended.
First, install the packages listed in requirement.txt.

Then, additionally install:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```


How to Download the Project:
Run the following command:
```bash
git clone https://github.com/JoeYang1412/GenerateVideoSubtitles.git
```
After downloading and setting up the environment, open cli.py to use the program.

Usage Instructions:
```
Main Menu:  
1. Analyze Video/Audio  
2. Exit  
Please choose (1 or 2): 1  

Welcome to the Speech-to-Text System  
Please enter a YouTube URL or a local file path: YT_url  

Please select the model size:  
1. tiny  
2. small  
3. medium  
4. large  
5. large-v2  
6. large-v3  
7. large-v3-turbo  
8. turbo  
Enter the option number (default is 5): 7  

Please select the language:  
1. Auto  
2. Chinese  
3. English  
4. Japanese  
Enter the option number (default is 1): 1  

Please select the output format:  
1. txt  
2. srt  
Enter the option number (default is 2):  

Downloading...  
Video length: 300 seconds  
Download progress: 100%  
Download complete: example.m4a  
Converting format...  
MoviePy - Writing audio in SRZcpVPS6wc.wav  
MoviePy - Done.  
Initializing...  
Loading model...  
Model loaded successfully.  
Processing...  
100%  
Generating output file...  
Processing complete.  
Returning to main menu.  
```

Current Issues:
There may be unknown issues.



本專案可以將影片中的聲音，轉換成文字  
功能有
1. 可選擇線上或是本地來源，線上目前僅支援Youtube
2. 模型為 faster-whisper，可以選擇模型大小，若要精準，建議 large-v3-turbo，若效能不足，可選擇small
3. 可選擇輸出成 srt 或是txt
4. 影片語言基本上不限，但英文效果最好，中文則會輸出成繁體中文
5. 本地檔案支援 mp3,m4a,wav

環境：
Driver Version: 566.03  
CUDA Version: 12.7  
CUDA Toolkit 12.6 Update 2  
cudnn v9.5  

需求：  
需要安裝cuda  
且記憶體最少需要3-4G會比較好  
另請先安裝 `requirement.txt` 中的套件  
安裝完後請額外安裝  
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

本專案下載方法：
 ```bash
 git clone https://github.com/JoeYang1412/GenerateVideoSubtitles.git
 ```
下載完成後且環境建立後
打開 cli.py 即可使用

使用方法及步驟：
```
主選單:
1. 分析影片/音訊
2. 離開
請選擇 (1 或 2): 1

歡迎使用語音轉文字系統
請輸入影片網址或本地檔案路徑: YT_url

請選擇模型大小:
1. tiny
2. small
3. medium
4. large
5. large-v2
6. large-v3
7. large-v3-turbo
8. turbo
輸入選項編號 (默認為 5): 7

請選擇語言:
1. Auto
2. Chinese
3. English
4. Japanese
輸入選項編號 (默認為 1):1

請選擇輸出格式:
1. txt
2. srt
輸入選項編號 (默認為 2):

下載中...
影音長度：300秒
下載進度：: 100%
下載完成：example.m4a
轉換格式中...
MoviePy - Writing audio in SRZcpVPS6wc.wav
MoviePy - Done.
初始化...
加載模型中...
模型加載完成。
處理中...
100%
輸出檔案中...
完成處理
處理完成，返回主選單
```

目前有以下幾個問題
1. 可能有未知的問題

