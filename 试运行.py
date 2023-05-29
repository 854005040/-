import time, os, random, threading #导入时间、操作系统、随机数和多线程模块
import cv2, numpy, pyautogui #导入OpenCV、NumPy和PyAutoGUI模块
from PIL import ImageGrab   
import sys
import re,socket
import paddlehub as hub
ocr = hub.Module(name="chinese_ocr_db_crnn_mobile", enable_mkldnn=True)

import paddlehub as hub
# class Player(object):
# 	def __init__(self,accuracy=0.7,abd_mode=False,abd_num=0)
# 	self.accuracy=accuracy
# 	self.adb_mode=abd_mode
# 	self.abd_num=abd_num
#   os.open("夜神模拟器.exe",)
#   os.system("D:/Nox/bin/Nox.exe -run:")
'封装命令到字典'
cmd_package={'连接夜神':"adb connect 127.0.0.1:62001",  #中文对应的cmd命令
             '连接':'adb connect',
              '查看':'adb devices',
              '输入':'adb shell input text',
              '按键':'adb shell input keyevent',
              '点击':'adb shell input tap',
              '终止服务器':'adb kill-server',
              '启动服务器':'adb start-server',
              '查看所有':'adb devices -l',
              '拖动':'adb shell input swipe',
              '按拖':'adb shell input touchscreen swipe',
              # '应用':'adb shell am start com.qnss.uctt',
              # '':'',
       }
cmd_aJM_package={
    '':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',

}
def lianjie_sb():
    '''连接设备的函数，无参数，返回布尔值'''
    fanhui=os.popen(cmd_package['查看']).read()  #通过获取cmd命令返回值，转换成字符串格式
    print(fanhui)
    if '0' in fanhui:      #判断
        print("设备已连接")
        return True
    else:
        os.system(cmd_package['终止服务器'])
        os.system(cmd_package['启动服务器'])
        if "0." in IP_list():
            os.system(cmd_package['连接' + IP_list()])  # 用cmd命令运行
            print("设备已连接2")
            return True
        else:
            print('连接函数无法获取设备IP与端口号')
            return False
def IP_list():
    '''获取设备IP和端口，返回一个字符串格式IP，端口值'''
    sj = os.popen(cmd_package['查看所有']).read() #通过获取cmd命令返回值，转换成字符串格式
    if "0." in sj:     #判断
        IP_list = re.findall("\d+", sj)   #正则式表达提取字符串里的数字，保存在列表里
        a = socket.inet_ntoa(bytes(int(x) for x in IP_list[:4])) #提取列表里的数字，组合成IP字符串
        IP = a + ':' +IP_list[4]           #IP与端口合并
        print(IP)
    else:
        print("IP函数没获取到设备信息")
        IP='没有设备'
    return IP
def cmd_keyevent(ma):
    """按键功能，4返回，3home"""
    os.system(cmd_package['按键']+' '+str(ma))
def cmd_text(text):
    os.system(cmd_package['输入']+' '+str(text))
def cmd_click(x,y):
    os.system(cmd_package['点击']+' '+str(x)+' '+str(y))
def cmd_drag(x,y,x1,y1,time):
    # time2=3000
    # os.system(cmd_package['拖动'] + ' ' + str(x) + " " + str(y) + " " + str(x+1) + " " + str(y+1) + " " + str(time2))
    os.system(cmd_package['拖动']+' '+str(x)+" "+str(y)+" "+str(x1)+" "+str(y1)+" "+str(time))
def cmd_tdong(x,y,x1,y1,time):
    '''按住拖动，不太好使'''
    os.system(cmd_package['按拖'] + ' ' + str(x) + " " + str(y) + " " + str(x1) + " " + str(y1) + " " + str(time))
def cmd_app():
    os.system(cmd_package['应用'])
# cmd_text("785")
# cmd_click(220,271)
# cmd_tdong(220,271,548,488,3500)
# lianjie_sb()






