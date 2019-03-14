"""
    name : resource
    usage : from resource import Screens, loadImgs, loadCache, saveCache, existsCache, initialize, updateCache
    
"""

#公用库
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import json
from subprocess import run

#加载配置文件
from config import Screens, CachePath

#全局变量
Path = CachePath
print("Path: ", Path)
NpyDir = "/npy"
NpyPath = Path + NpyDir

if not os.path.exists(Path) :
    os.makedirs(Path)
if not os.path.exists(NpyPath) :
    os.makedirs(NpyPath)

#加载资源文件
def loadImgs() :
    print("loading files.")
    #迭代屏幕
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        #加载屏幕图像
        if "refer" in screen.keys() :
            print("loading",screenKey)
            url = screen["refer"]
            screen["img"]=np.array(Image.open(url))
        #迭代元素
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                #加载元素图像
                if "refer" in element.keys() :
                    url = element["refer"]
                    img = np.array(Image.open(url))
                elif "img" in screen.keys() :
                    img = screen["img"]
                else :
                    assert "img" in locals().keys()
                if ( "location" in element.keys() ) and ( "img" in locals().keys() ) :
                    print("loading",screenKey,sProKey)
                    location = element["location"]
                    offset = location["offset"]
                    length = location["length"]
                    x1 = offset["x"]
                    x2 = x1 + length["x"]
                    y1 = offset["y"]
                    y2 = y1 + length["y"]
                    element["img"] = img[x1:x2,y1:y2,:]
    return Screens
#loadImgs()

#把Screens里的nparray分别保存为文件
def saveNpys() :
    path = NpyPath
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            np.save( path + "/" + screenKey + ".npy" , screen['img'] )
            for screenKey in Screens.keys() :
                screen = Screens[screenKey]
                for sProKey in screen.keys() :
                    if isinstance(screen[sProKey],dict) :    
                        element = screen[sProKey]
                        if "img" in element.keys() :
                            np.save( path + "/" + screenKey + "_" + sProKey + ".npy" , element['img'] )
    return Screens
#把Screens里的np.array移除
def removeNpas() :
    path = NpyDir
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            screen['img'] = path + "/" + screenKey + ".npy"
            for screenKey in Screens.keys() :
                screen = Screens[screenKey]
                for sProKey in screen.keys() :
                    if isinstance(screen[sProKey],dict) :    
                        element = screen[sProKey]
                        if "img" in element.keys() :
                            element['img'] = path + "/" + screenKey + "_" + sProKey + ".npy"
    return Screens
#把np.array文件加载到Screens
def loadNpys() : 
    path = NpyPath
    print("loading cache: ", Path)
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        npyFile = path + "/" + screenKey + ".npy"
        if os.path.exists(npyFile) :
            screen['img'] = np.load(npyFile)
        for screenKey in Screens.keys() :
            screen = Screens[screenKey]
            for sProKey in screen.keys() :
                if isinstance(screen[sProKey],dict) :
                    element = screen[sProKey]
                    npyFile = path + "/" + screenKey + "_" + sProKey + ".npy"
                    if os.path.exists(npyFile) :
                        element['img'] = np.load(npyFile)
    return Screens

#保存为json文件
def saveConfig() :
    with open("./config.json", 'w', encoding='utf-8') as json_file:
        json.dump(Screens, json_file, ensure_ascii=False)
#从json文件加载
def loadConfig() :
    with open("./config.json", 'r', encoding='utf-8') as json_file:
        Screens = json.load(json_file)
        return Screens


#打印img
def printImgs() :
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            print(screenKey + ":", screen["img"])
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                if "img" in element.keys() :
                    print(screenKey + "_" + sProKey + ":", element["img"])

#显示图像

#显示第一层图像
def showFirstLevelImgs() :
    #统计个数
    n = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            n += 1
    #计算行列数
    cols = 6
    rows = round(n/cols) + 1
    plt.figure(figsize=[20,40], dpi=400)
    #加载
    i = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            i += 1
            plt.subplot(rows,cols,i)
            plt.imshow(screen["img"])
            plt.title(screenKey)
            plt.axis("off")
    plt.show()

#显示第二层图像
def showSecondLevelImgs() :
    #统计个数
    n = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                if "img" in element.keys() :
                    n += 1
    #计算行列数
    cols = 6
    rows = round(n/cols) + 1
    plt.figure(figsize=[20,40], dpi=200)
    #加载
    i = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                if "img" in element.keys() :
                    i += 1
                    plt.subplot(rows,cols,i)
                    plt.imshow(element["img"])
                    plt.title(sProKey, fontsize=8)
                    plt.axis("off")
    plt.show()

#显示全部图像
def showImgs() :
    #统计个数
    n = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            n += 1
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                if "img" in element.keys() :
                    n += 1
    #计算行列数
    cols = 6
    rows = round(n/cols) + 1
    plt.figure(figsize=[20,40], dpi=200)
    #加载
    i = 0
    for screenKey in Screens.keys() :
        screen = Screens[screenKey]
        if "img" in screen.keys() :
            i += 1
            plt.subplot(rows,cols,i)
            plt.imshow(screen["img"])
            plt.title(sProKey, fontsize=8)
            plt.axis("off")
        for sProKey in screen.keys() :
            if isinstance(screen[sProKey],dict) :    
                element = screen[sProKey]
                if "img" in element.keys() :
                    i += 1
                    plt.subplot(rows,cols,i)
                    plt.imshow(element["img"])
                    plt.title(sProKey, fontsize=8)
                    plt.axis("off")
    plt.show()


#对外接口

#判断缓存文件是否存在
def existsCache() :
    return ( os.path.exists("./config.json") and os.path.exists(NpyPath) )

#保存缓存
def saveCache() :
    saveNpys()
    removeNpas()
    saveConfig()

#加载缓存
def loadCache() :
    removeNpas()
    saveConfig()
    loadNpys()

#更新缓存
def updateCache() :
    loadResource()
    saveCache()
    loadCache()

#清理缓存
def clearCache() :
    pass

#从图片资源加载
def loadResource() :
    loadImgs()

#初始化
def initialize() :
    print("initialize.")
    if existsCache() :
        loadCache()
    else :
        loadResource()
        loadCache()
#updateCache()
#print(Screens)
