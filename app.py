# -*- encoding = UTF-8
import subprocess
import imageio_ffmpeg
from os import listdir
from os import path
from os import makedirs
from tqdm import tqdm

def audioConversion(inputMedia="media.wav",outputMedia="media.out.wav",auioChannel="1", audioRate="16000", audioBitRate="256k", logLevel="quiet"):
    """
    使用imageio_ffmpeg将音频转换为wav格式。
    :param inputMedia: 输入的音频文件路径。
    :param outputMedia: 输出的音频文件路径。
    :param auioChannel: 音频通道数，默认为1。
    :param audioRate: 音频采样率，默认为16000Hz。
    :param audioBitRate: 音频比特率，默认为256k。
    :param logLevel: 日志级别，默认为"quiet"。
    :return: 返回转换命令字符串
    """
    return f"{imageio_ffmpeg.get_ffmpeg_exe()} -loglevel {logLevel} -y -i {inputMedia} -ac {auioChannel} -ar {audioRate} -b:a {audioBitRate} {outputMedia}"

def renameFileName(inputFileName,outputFileType="wav"):
    """
    修改文件后缀名。
    :param inputFileName: 输入的文件名。
    :param outputFileType: 输出的文件类型。
    :return: 修改后的文件名。
    """
    root, ext = path.splitext(inputFileName)
    return root + "." + outputFileType

def cmdPause(pauseType = "p"):
    """
    暂停命令行窗口，等待用户输入。
    :param pauseType: "p"表示暂停，"e"表示退出。
    :return: 无返回值。
    """
    if pauseType == "p":
        input("按回车键继续...")
    elif pauseType == "e":
        input("按回车键退出...")
        exit(0)

if __name__ == '__main__':
    # 路径设置
    inputAudioPath = "./input"
    outputAudioPath = "./output"
    # 自动创建 input 和 output 文件夹（如不存在）
    makedirs(inputAudioPath, exist_ok=True)
    makedirs(outputAudioPath, exist_ok=True)
    # 支持的音频后缀
    audio_exts = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'}
    # 获取所有文件
    all_files = listdir(inputAudioPath)
    # 筛选音频文件和非音频文件
    audio_files = []
    pass_list = []
    for x in all_files:
        ext = path.splitext(x)[1].lower()
        if ext in audio_exts:
            audio_files.append(x)
        else:
            pass_list.append(x)
    if not audio_files:
        print("input 文件夹无音频文件，程序停止。")
        cmdPause("e")
        exit(0)
    for x in tqdm(audio_files, desc="处理进度"):
        full_path = (inputAudioPath + r'/' + x)
        output_path = (outputAudioPath + r'/' + renameFileName(x))
        subprocess.Popen(audioConversion(full_path,output_path))
    if pass_list:
        print("已跳过以下文件:")
        for x in pass_list:
            print(x)