# Implementing-a-music-radio-station-based-on-Python
本项目使用Python语言实现了一个简单的命令行音乐广播电台功能,具有随机播放本地音乐、整点报时、留言功能。
This project uses the Python language to implement a simple command-line music player , with random playback of local music , the whole point of the clock , message function .
# 一、主要功能:
1.播放指定目录下的音乐文件（仅支持MP3格式）
2.随机播放
3.整点报时
4.留言                                                                                                                   
5.播放时随机选择音乐趣闻进行播报
# I. Main functions.
1. Play music files in the specified directory (only support MP3 format)
2. Random playback
3. Whole point chime
4. Message                                                                                                                   
5. Randomly select music anecdotes to broadcast when playing
# 二、运用的主要模块和库:
os  文件遍历
pygame  音频播放
random  随机打乱歌曲
datetime 获取当前的日期和时间
# II,The main modules and libraries used.
os file traversal
pygame audio playback
random randomize songs
datetime Getting the current date and time
# bgm
本项目bgm使用项目musicgen生成：https://huggingface.co/spaces/facebook/MusicGen
