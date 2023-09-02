import os
import random
import datetime
from pygame import mixer # 导入pygame的mixer模块

# 定义一个函数，用于播放语音内容
messages = []
bgm_file="nnnnfn6qt-onoej.mp3"
def speak(text):
    # 使用pyttsx3库来生成语音
    import pyttsx3
    # 初始化语音引擎
    engine = pyttsx3.init()
    # 设置语音参数
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    mixer.music.load(bgm_file)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    # 播放语音内容
    engine.say(text)
    engine.runAndWait()
    mixer.music.stop()
# 定义一个函数，用于播放音乐文件
def play_music(file):
    # 使用pygame的mixer模块来播放音乐文件
    try:
        # 加载音乐文件，根据文件后缀名自动判断格式
        mixer.music.load(file)
        # 播放音乐文件
        mixer.music.play()
        # 等待音乐文件播放完毕
        while mixer.music.get_busy():
            continue
    except Exception as e:
        # 如果出现异常，打印错误信息并提示用户
        print(e)
        speak(f"对不起，无法播放{file}，请检查文件是否存在或格式是否正确。")
# 定义一个函数，用于判断是否是整点
def is_hour():
    # 获取当前时间的分钟数
    minute = datetime.datetime.now().minute
    # 如果分钟数为0，返回True，否则返回False
    return minute == 0
# 定义一个函数，用于播放整点报时语音内容
def report_time():
    # 获取当前时间的小时数
    hour = datetime.datetime.now().hour
    # 如果小时数为0，表示是午夜12点
    if hour == 0:
        speak("现在是午夜12点，祝你有个好梦。")
    # 如果小时数为12，表示是中午12点
    elif hour == 12:
        speak("现在是中午12点，祝你用餐愉快。")
    # 如果小时数小于12，表示是上午
    elif hour < 12:
        speak(f"现在是上午{hour}点，祝你工作顺利。")
    elif hour < 20:
        speak(f"现在是下午{hour-12}点，祝你工作顺利。")
    # 如果小时数大于12，表示是下午
    else:
        speak(f"现在是下午{hour-12}点，祝你生活愉快。")
# 获取指定目录及其子目录下的所有mp3文件
# 定义一个空列表，用于存储找到的mp3文件
mp3_files = []
# 定义一个变量，用于指定要遍历的目录
directory = "D:\新建文件夹\新建文件夹"
# 使用os.walk函数，遍历指定目录及其子目录下的所有文件
for root, dirs, files in os.walk(directory):
    # 对于每个文件，判断是否是mp3文件，如果是，则添加到列表中
    for file in files:
        if file.endswith('.mp3'):
            # 使用os.path.join函数，拼接文件的完整路径
            file_path = os.path.join(root, file)
            mp3_files.append(file_path)
# 如果没有找到任何mp3文件，提示用户并退出程序
if not mp3_files:
    speak("对不起，没有找到任何mp3文件，请确保你的目录下有音乐文件。")
    exit()
# 随机打乱mp3文件的顺序
random.shuffle(mp3_files)
# 初始化mixer模块
mixer.init()
# 播放欢迎语

speak("您正在收听的是xueFM，我是你的主持人学习学什么。接下来，我将为您播放一些精彩的音乐，希望你喜欢。")
# 循环播放每个mp3文件，并在每个文件之间播放一些语音内容
for i, file in enumerate(mp3_files):
    # 判断是否是整点
    if is_hour():
        # 播放整点报时语音内容
        report_time()
    # 播放当前的音乐文件
    speak(f"您正在收听的是第{i+1}首歌曲。")
    name = os.path.basename(file)
    name = os.path.splitext(name)[0]
    song , singer =name.split('-')
    speak(f"{singer}演唱的{song}")
    play_music(file)
    if is_hour():
        # 播放整点报时语音内容
        report_time()
    # 播放一些语音内容
    speak(f"您刚刚收听的是：{singer}演唱的{song}，如果您喜欢，请给我们留言和评价。")

    # 获取用户留言
    print("请说出您的留言,或按Enter跳过:")
    message = input()

    # 判断留言是否为空
    if message:
        # 将非空留言添加到列表
        messages.append(message)
    else:
        # 留言为空,不添加
        pass

    # 随机读取一条留言
    if messages:
        msg = random.choice(messages)
        speak(f"收到留言:{msg}")
 

    speak(f"休息一下，我们将为您介绍一些音乐圈有趣的事情。")
    # 随机生成一些有趣的事情，并播放语音内容
    facts = [
        "你知道吗?酷玩乐队的歌曲《Viva La Vida》使用了超过40种不同的乐器录制。",
        "你知道吗?披头士乐队的专辑中共有27首歌曲登上了公告牌百强单曲榜冠军。",
        "你知道吗?周杰伦的专辑《叶惠美》创下台湾史上最快销量纪录,发行首日就卖出了10万张。",
        "你知道吗?蔡依林凭借专辑《Ugly Beauty》一举获得第29届金曲奖年度专辑奖,这是史上第一个华语女歌手获得这个大奖。",
        "你知道吗?陈奕迅的演唱会最高票价达到了88800港币,刷新了华语乐坛的纪录。",
        "你知道吗?日本男子组合岚的总销量高达3600万张,是日本史上销量最高的艺人之一。",
        "你知道吗?韩红是中国内地销量最高的女歌手,她的专辑销量合计超过1.3亿张。",
        "你知道吗?世界顶级DJ艾维西的单曲《Wake Me Up》在全球范围内狂销超过800万份。",
        "你知道吗?荷兰DJ马汀·盖里克斯是第一位进入DJ MAG百大DJ排名前十的非英语歌手。",
        "你知道吗?世界上第一台音乐广播电台KDKA诞生于1920年的美国。"
    ]
    fact = random.choice(facts)
    speak(fact)
# 播放结束语
speak("感谢您收听xueFm，我是你的主持人学习学什么。希望你喜欢我们的节目，下次再见。")