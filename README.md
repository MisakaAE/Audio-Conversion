# Audio-Conversion
在 Python 使用ffmpeg转换任意音频至指定码率指定比特率的指定文件，用于制作Edge TX系统的语音包

<https://misakaae.com/archives/rc-soundpack-re>

## 测试环境
系统：Windows 11 Pro 24H2

Python ： 3.13.5

## 用到的库
```txt
colorama==0.4.6
imageio-ffmpeg==0.6.0
pillow==11.3.0
tqdm==4.67.1
```

## 编译
+ 确保安装pyinstaller
  ```bash
  pip install pyinstaller
  ```
+ 开始编译
  ```bash
  python.exe -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  pyinstaller --onefile --console app.py
  ```
+ 若出现`在此系统禁止运行脚本`字样，使用管理员命令行输入如下指令：
  ```bash
  set-ExecutionPolicy RemoteSigned
  ```
