import time, os, random, threading #导入时间、操作系统、随机数和多线程模块
import cv2, numpy, pyautogui #导入OpenCV、NumPy和PyAutoGUI模块
from PIL import ImageGrab #从PIL模块导入ImageGrab类

#桌面模式下的鼠标操作延迟，程序已经设置随机延迟这里无需设置修改
pyautogui.PAUSE = 0.001 #设置PyAutoGUI的默认延迟为0.001秒
cwd = __file__.replace('auto_player.py', '')  #当前文件目录 #获取当前文件的目录，去掉文件名
wanted_path = f'{cwd}\\wanted'      #目标图片目录 #拼接目标图片的目录，用反斜杠分隔
#上面都不用改，下面是adb.exe文件所在路径要改，
#如果你已经加入系统PATH环境，就直接adb = 'adb',我的没加。 只用桌面模式话不用管
adb = 'd: && cd \\mysys\\Nox\\bin\\ && nox_adb.exe' #ADB文件路径 #设置ADB文件的路径，用空格分隔命令
nxfd = 'C:\\Users\\Administrator\\Nox_share\\ImageShare' #模拟器共享文件路径 #设置模拟器共享文件的路径

class Player(object): #定义一个类，叫做Player
    """docstring for Player""" #类的文档字符串，用来说明类的功能和用法
       # accuracy 匹配精准度 0~1 #adb_mode开启ADB模式  #adb_num连接第几台ADB设备
    def __init__(self, accuracy=0.8, adb_mode=False, adb_num=0): #定义类的初始化方法，接受三个参数：匹配精度、ADB模式和ADB设备编号，默认值分别为0.8、False和0
        super(Player, self).__init__() #调用父类的初始化方法，这里是object类，没有什么特别的作用
        self.accuracy = accuracy  #将匹配精度赋值给实例属性self.accuracy
        self.adb_mode = adb_mode  #将ADB模式赋值给实例属性self.adb_mode
        #self.load_target()  #调用实例方法self.load_target()，读取目标图片
        if self.adb_mode: #如果开启了ADB模式
            re = os.popen(f'{adb} devices').read() #执行ADB命令，获取连接的设备列表，并读取返回值，赋值给变量re
            print(re) #打印返回值re
            device_list = [e.split('\t')[0] for e in re.split('\n') if '\tdevice' in e] #将返回值re按换行符分割，过滤出包含'\tdevice'的元素，并取出每个元素的第一个字段（设备编号），组成一个列表，赋值给变量device_list
            assert len(device_list) >= 1, '未检测到ADB连接设备' #断言device_list的长度大于等于1，否则抛出异常，提示未检测到ADB连接设备
            self.device = device_list[adb_num]  #根据参数adb_num，从device_list中取出对应的设备编号，赋值给实例属性self.device
            re = os.popen(f'{adb} -s {self.device} shell wm size').read() #执行ADB命令，获取指定设备的屏幕尺寸，并读取返回值，赋值给变量re
            print(re) #打印返回值re
        else: #如果没有开启ADB模式
            w, h = pyautogui.size() #调用PyAutoGUI的size()方法，获取当前


aa=Player(adb_mode=True)
