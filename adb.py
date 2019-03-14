"""
    name ： adb
    usage : from adb import getScreen, gotoHome, gotoBack, tap, press, swipe

"""

from subprocess import run
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import random

from config import ADB
prefix = ADB["commandpPefix"]
cachePath = ADB["cachePath"]
myshell = True

#拉取屏幕截屏
def pullScreen( url ) :
    command = prefix + "adb shell screencap /sdcard/temp/screen.png"
    run(command,shell=myshell)
    command = prefix + "adb pull /sdcard/temp/screen.png " + url
    run(command,shell=myshell)
    return url
"""
temp = pullScreen( "C:/WechatFriendCircleCrawler/temp/1.png" )
print(temp)
"""
ScreenSerial = 0
#获取屏幕数据
def getScreen() :
    global ScreenSerial
    ScreenSerial += 1
    url = cachePath + "/screen" + str(ScreenSerial) + ".png"
    pullScreen( url )
    img=np.array(Image.open(url))
    return img
"""
from image import currentPage
from loadResource import loadImgs, Screens
img = getScreen()
print(currentPage(img))
plt.figure(figsize=[20,40], dpi=400)
plt.subplot(1,1,1)
plt.imshow(img)
plt.axis("off")
plt.show()
"""

#去手机桌面
def gotoHome() :
    command = prefix + "adb shell input keyevent 3" 
    run(command,shell=myshell)
#gotoHome()

#返回上一个屏幕
def gotoBack() :
    command = prefix + "adb shell input keyevent 4"
    run(command,shell=myshell)
#gotoBack()

#触摸
def tap(x, y) :
    print("tap:", x, y)
    xx = x + random.randint(0,3)
    yy = y + random.randint(0,3)
    print(xx,yy)
    command = prefix + "adb shell input tap " + str(xx) + " " + str(yy)
    run(command,shell=myshell)
#tap(100,200)

#长按
def press(x,y) :
    print("press:", x, y)
    timelen = 800 #+ random.randint(1,3)
    xx = x + random.randint(0,3)
    yy = y + random.randint(0,3)
    command = prefix + "adb shell input swipe " + str(xx) + " " + str(yy) + " " + str(xx) + " " + str(yy) + " " + str(timelen)
    run(command,shell=myshell)
#press(100,200)

#滑动
def swipe(x1,y1,x2,y2,timelen) :
    print("swipe:", x1,y1,x2,y2,timelen)
    xx1 = x1 + random.randint(0,3)
    yy1 = y1 + random.randint(0,3)
    xx2 = x2 + random.randint(0,3)
    yy2 = y2 + random.randint(0,3)
    timelenr = timelen + random.randint(0,3)
    command = prefix + "adb shell input swipe " + str(xx1) + " " + str(yy1) + " " + str(xx2) + " " + str(yy2) + " " + str(timelenr) 
    run(command,shell=myshell)
#swipe(224,373,224,1373,800)

