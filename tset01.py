import time, os, random, threading #导入时间、操作系统、随机数和多线程模块
import cv2, numpy, pyautogui #导入OpenCV、NumPy和PyAutoGUI模块
from PIL import ImageGrab
import sys
import re,socket
"1，选择一个合适的开发环境，比如Python、Airtest、按键精灵等"
"2，选择一个合适的游戏模拟器，比如BlueStacks、MuMu、雷电等"
"3，分析游戏的逻辑和界面，确定需要实现的功能和流程"
"4，编写代码，使用图像识别、文字识别、鼠标键盘控制等技术来实现自动化操作"
"5，测试和调试代码，优化性能和稳定性"

wa=['192','168','0','1']
IP=socket.inet_ntoa(bytes(int(x) for x in wa))
print(IP)
