import time
import random
import os
import json

from resource import Screens, loadImgs, loadCache, saveCache, existsCache, initialize
from image import getWechat, getWPS, getMe, getAlbum, getMyFriendsCircle, getDetail, \
    getRelay, isRelay, getCopyPoint, getCopyMenu, getSkip, getDocPoint, \
    getKeyboard, getKeyboard_closed, getEnter, getPastePoint, getPasteMenu, \
    getSave, getBack_photo, getBack_detail, \
    isHome, isWechat, isMe, isAlbum, isList, isIndex, isPhoto, isDetail, \
    isWPS, isWPSAd, isWPSEdit, isOther, currentScreen, cutImg, showIcon, showRegion
from adb import tap, press, swipe, getScreen, gotoHome, gotoBack
from interact import tapLocation, pressLocation, tapPoint, pressPoint

#记录已经处理的总长度
TotalLength = 0

#当前屏幕
CurrentScreen = getScreen()
#刷新当前屏幕
def refreshCurrentScreen() :
    global CurrentScreen
    time.sleep(random.randint(1,2))
    CurrentScreen = getScreen()
"""
refreshCurrentScreen()
img = CurrentScreen
plt.figure(figsize=[20,40], dpi=400)
plt.subplot(1,1,1)
plt.imshow(img)
plt.title("")
plt.axis("off")
plt.show()
"""

#切至左屏
def toLeftScreen() :
    width = Screens["size"]["ScreenWidth"]
    height = Screens["size"]["ScreenHeight"]
    x1 = width / 4 * 1
    x2 = width / 4 * 3
    y1 = height / 2
    y2 = y1
    swipe(x1,y1,x2,y2,500)
    refreshCurrentScreen()

#切至右屏
def toRightScreen() :
    width = Screens["size"]["ScreenWidth"]
    height = Screens["size"]["ScreenHeight"]
    x1 = width / 4 * 1
    x2 = width / 4 * 3
    y1 = height / 2
    y2 = y1
    swipe(x2,y2,x1,y1,500)
    refreshCurrentScreen()

#去桌面
def goHome() :
    print("go home")
    try: 
        gotoHome()
        refreshCurrentScreen()
        return True
    except:
        return False
#goHome()

#去左桌面
def toLeft() :
    print("to left")
    toLeftScreen()
    refreshCurrentScreen()
#去右桌面
def toRight() :
    print("to right")
    toRightScreen()
    refreshCurrentScreen()
#回退
def goBack(n) :    
    print("go back",n)
    try :
        for i in range(0,n) :
            gotoHome()
        refreshCurrentScreen()
    except:
        return False
#goBack(2)

#启动微信
def launchWechat() :
    print("launch wechat:")    
    location = getWechat(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#refreshCurrentScreen()
#launchWechat()

#启动WPS
def launchWPS() :
    print("launch wps:")
    location = getWPS(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#refreshCurrentScreen()
#launchWPS()

#去Me
def toMe() :
    print("to me")
    location = getMe(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#refreshCurrentScreen()
#toMe()

#去Album
def toAlbum() :
    print("to album")
    location = getAlbum(CurrentScreen)
    print(location)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#toAlbum()

#去List
def toList() :
    print("to List:")
    location = getMyFriendsCircle(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#toList()

#从List进入Topic
def intoTopic(point) :
    print("into topic:")
    tapPoint(point)
    refreshCurrentScreen()

#去Detail
def toDetail() :
    print("to detail:")
    location = getDetail(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#toDetail()

#唤出copy菜单
def callCopyMenu() :
    print("call copy menu:")
    location = getCopyPoint(CurrentScreen)
    if location :
        pressPoint(location)
    refreshCurrentScreen()
    return location
#callCopyMenu()

#执行copy
def exeCopy() :
    print("exe copy:")
    location = getCopyMenu(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#exeCopy()

#去WPS
def toWPS() :
    print("to wps:")
    """
    location = getWPS(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    """
    #location = getWPS(CurrentScreen)
    time.sleep(1)
    refreshCurrentScreen()
    #return location
#toWPS()

#去WPSEdit
def toWPSEdit() :
    print("to wosedit:")
    location = getDocPoint(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#toWPSEdit()

#启用键盘
def callKeyboard() :
    print("call keyboard:")
    location = getKeyboard_closed(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location
#callKeyboard()

#插入空行
def insertEmptyLine(n) :
    print("insert a empty line:")
    location = getEnter(CurrentScreen)
    if location :
        for i in range(0,n) :
            tapPoint(location)
    return location


#唤出粘贴菜单
def callPasteMenuAtPoint(Point) :
    print("call paste menu at:", Point)
    try :
        pressPoint(Point)
        refreshCurrentScreen()
        return True
    except :
        return False        
def callPasteMenu() :
    print("call paste menu:")
    Point = getPastePoint(CurrentScreen)
    return callPasteMenuAtPoint(Point)


#执行粘贴
def exePaste() :
    print("exe paste:")
    location = getPasteMenu(CurrentScreen)
    if location :
        tapPoint(location)
    refreshCurrentScreen()
    return location

#保存WPS
def save() :
    print("save docment:")
    location = getSave(CurrentScreen)
    if location :
        tapPoint(location)
    return location

#从photo回退
def fromPhotoGoBack() :
    print("from photo go back.")
    point = getBack_photo(CurrentScreen)
    if point :
        tapPoint(point)
    refreshCurrentScreen()
    return point

#从detail回退
def fromDetailGoBack() :
    print("from detail go back.")
    point = getBack_detail(CurrentScreen)
    if point :
        tapPoint(point)
    refreshCurrentScreen()
    return point
#fromDetailGoBack()

#滑动列表首页，去掉头部
def swipeIndex() :
    top = 250
    length = Screens["list"]["properties"]["head"]
    bottom = top + length
    swipe(540, bottom, 540, top, 1000)
    refreshCurrentScreen()
#swipeIndex()

#滑动列表到指定位置
def swipeList(totalLength) :
    top = 250
    bottom = Screens["size"]["ScreenHeight"] -250
    stepmaxlength = bottom - top
    if stepmaxlength > totalLength :
        bottom = top + totalLength
        swipe(540, bottom, 540, top, 2000)
    else :
        steplength = stepmaxlength
        stepcount = int(totalLength / steplength)
        for i in range(0,stepcount) :
            swipe(540, bottom, 540, top, 2000)
        residue = totalLength - steplength * stepcount
        bottom = top + residue
        swipe(540, bottom, 540, top, 2000)        
    refreshCurrentScreen()
#swipeList(2000)

#从任何地方去朋友圈
def fromAnywhereGotoList() :    
    print("from anywhere goto List:")
    while not isList(CurrentScreen) :        
        screen = currentScreen(CurrentScreen)
        print("route: ",screen,".")
        if "left"==screen :
            launchWechat()
        elif "right"==screen :
            toLeftScreen()
        elif "wechat"==screen :
            toMe()
        elif "me"==screen :
            toAlbum()
        elif "album"==screen :
            toList()
        elif "index"==screen :
            swipeIndex()
            swipeList(TotalLength)
        elif "detail"==screen :
            if getCopyMenu(CurrentScreen) :
                print("quit from copy menu.")
                goBack(1)
            print("quit from detail.")
            fromDetailGoBack()
        elif "photo"==screen :
            print("quit from photo.")
            fromPhotoGoBack()
        elif "other"==screen :
            fromDetailGoBack()
        else :
            goHome()

#从任何地方去WPS
def fromAnywhereGotoWPSEdit() :
    print("from anywhere go to wps edit:")
    while not isWPSEdit(CurrentScreen) :        
        screen = currentScreen(CurrentScreen)
        print(screen)
        if "right"==screen :
            launchWPS()
        elif "left"==screen :
            toRightScreen()
        elif "wpsad"==screen :
            toWPS()
        elif "wps"==screen :
            toWPSEdit()
        else :
            goHome()
#fromAnywhereGotoWPSEdit()

#处理粘贴
def disposePaste() :
    print("dispose paste:")
    screenName = currentScreen(CurrentScreen)  
    if "wpsedit" == screenName :
        callKeyboard()
        while not getEnter(CurrentScreen) :
            callKeyboard()
        insertEmptyLine(25)
        callPasteMenu()
        while not getPasteMenu(CurrentScreen) :
            callPasteMenu()
        exePaste()
        save()
        insertEmptyLine(1)
        #os.system("pause")
        return True
    else :
        print("Error:",screenName)
        False
"""
for i in range(0,10) :
    while not isWPSEdit(CurrentScreen) :
        launchWPS()
    disposePaste()
    while not isHome(CurrentScreen) :
        goHome()
os.system("pause")
"""

#处理一条朋友圈详情
def disposeDetail(n) :
    print("dispose a detail:")
    screenName = currentScreen(CurrentScreen)    
    if "detail" == screenName :
        if not isRelay(CurrentScreen) :            
            callCopyMenu()
            while not getCopyMenu(CurrentScreen) :
                callCopyMenu()
            while getCopyMenu(CurrentScreen) :
                exeCopy()
            print("finish copy.")
            #回退到list
            if 1 == n :
                fromDetailGoBack()
            elif 2 == n :
                fromDetailGoBack()
                fromPhotoGoBack()
            #去粘贴
            fromAnywhereGotoWPSEdit()
            disposePaste()
            gotoHome()
            gotoHome()
            gotoHome()
            #gotoBack()
            #gotoBack()
            refreshCurrentScreen()
            fromAnywhereGotoList()
        else :
            #什么也不做
            print("it is a relay.")
            fromDetailGoBack()
            pass
        
    else :
        print("Error:", screenName)
        #页面不对，进行处理
#disposeDetail(1)

#处理一条朋友圈
def disposeTopic(point) :
    print("dispose a topic:")
    intoTopic(point)
    screenName = currentScreen(CurrentScreen)    
    if "detail" == screenName : 
        print("this is detail")
        disposeDetail(1)
        #fromDetailGoBack()
    elif "photo" == screenName :
        print("this is photo")
        toDetail()
        disposeDetail(2)        
    else :
        print("this is all no",screenName)
        pass
#disposeTopic()

#判断颜色在颜色列表中
def theColorInList(myColor, List) :
    for myList in List :
        if (myColor==myList).all() :
            return True
    return False

#对图片进行像素分析，获取topics列表
def getTopics( img ) :
    print("get topics:")
    prop = Screens["list"]["properties"]
    top = prop["top"]
    bottom = prop["bottom"]
    bgc = prop["backgroundColor"]
    fgcs = prop["foregroundColors"]
    sll = prop["searchLineLocation"]

    topics = []
    for i in range(top, bottom-1):
        current = img[i][sll]
        nextone = img[i+1][sll]
        if  (current==bgc).all() and theColorInList( nextone, fgcs ) :
            topic = {"begin": i+1, "end": 0}
            topics.append(topic)
            
        if  (nextone==bgc).all() and theColorInList( current, fgcs ) :
            if len(topics)>= 1 and topics[len(topics)-1]["end"]==0 :
                topic = {"begin": topics[len(topics)-1]["begin"], "end": i}
                del topics[len(topics)-1]
                topics.append(topic)
    print(len(topics))
    return topics
"""
img = getScreen()
temp = getTopics( img )
print(temp)
"""

#获取bottom
def getTopicsBottom(topics) :
    length = len(topics)
    last = topics[ max( 0, length - 1 ) ]
    penult = topics[ max( 0, length - 2 ) ]
    if last["end"] > 0 and last["end"] > last["begin"] :
        bottom = 0.5* ( last["begin"] + last["end"] )
    else :
        bottom = 0.5* ( penult["begin"] + penult["end"] )
    return bottom
"""
img = getScreen()
topics = getTopics( img )
bottom = getTopicsBottom(topics)
print(bottom)
"""

#处理topics列表
def disposeTopics(topics) :
    print("dispose topics:",len(topics))
    sll = Screens["list"]["properties"]["searchLineLocation"]
    for i in range( 0, len(topics) ) :
        #计算中心位置，调用处理函数
        topic = topics[i]
        if topic["end"] > topic["begin"] :
            center = ( topic["begin"] + topic["end"] ) / 2             
            point = {"x":center,"y":sll}            
            disposeTopic(point)
            #print(i, topic["begin"], topic["end"])
#img = getScreen()
#topics = getTopics( img )
#print(len(topics))
#disposeTopics(topics)

totalfile = "./totals.json"
#读写已经处理的总长度，下次从断点处开始
def loadTotalLength() :
    if os.path.exists(totalfile) :
        with open(totalfile, 'r', encoding='utf-8') as json_file:
            total = json.load(json_file)
            if "totallength" in total.keys() :
                totalLength = total["totallength"]
                return totalLength
    return 0
def saveTotalLength(length) :
    with open(totalfile, 'w', encoding='utf-8') as json_file:
        json.dump({"totallength":length}, json_file, ensure_ascii=False)

def wecraw() :
    global TotalLength
    TotalLength = loadTotalLength()
    #进入桌面，从桌面自动路由到List
    goHome()    
    if not isList(CurrentScreen) :
        fromAnywhereGotoList()
    top = Screens["list"]["properties"]["top"]
    
    #主循环
    while 1 :        
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if isList(CurrentScreen) :
            topics = getTopics(CurrentScreen)
            disposeTopics(topics)
            #os.system("pause")
            bottom = getTopicsBottom(topics)
            length = bottom - top
            TotalLength += length
            saveTotalLength(TotalLength)
            swipeList(length)
        else :                
            fromAnywhereGotoList()
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
wecraw()