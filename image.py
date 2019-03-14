"""
    name : resource
    usage : 
    from image import getWechat, getWPS, getMe, getAlbum, getMyFriendsCircle, getDetail, \
        getRelay, isRelay, getCopyPoint, getCopyMenu, getSkip, getDocPoint, \
        getKeyboard, getKeyboard_closed, getEnter, getPastePoint, getPasteMenu, \
        getSave, getBack_photo, getBack_detail, \
        isHome, isWechat, isMe, isAlbum, isList, isIndex, isPhoto, isDetail, \
        isWPS, isWPSAd, isWPSEdit, isOther, currentScreen, cutImg, showIcon, showRegion
    
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from resource import Screens, initialize, showImgs
from adb import getScreen

initialize()

#切图
def cutImg(img, location) :
    offset = location["offset"]
    length = location["length"]
    x1 = offset["x"]
    x2 = x1 + length["x"]
    y1 = offset["y"]
    y2 = y1 + length["y"]
    print(x1,x2,y1,y2)
    return img[x1:x2,y1:y2,:]

#显示图标
def showIcon(img, screenName, iconName) :    
    location = Screens[screenName][iconName]["location"]
    icon = Screens[screenName][iconName]["img"]
    newicon = cutImg(img, location)
    plt.figure(figsize=[20,40], dpi=400)
    plt.subplot(1,3,1)
    plt.imshow(img)
    plt.title("img")
    plt.axis("off")
    plt.subplot(1,3,2)
    plt.imshow(newicon)
    plt.title("newicon")
    plt.axis("off")
    plt.subplot(1,3,3)
    plt.imshow(icon)
    plt.title("icon")
    plt.axis("off")
    plt.show()
#img = getScreen()
#showIcon(img, "wpsedit", "enter_9keys")

def showRegion(img, screenName, location) :
    newicon = cutImg(img, location)
    plt.figure(figsize=[20,40], dpi=400)
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title("img")
    plt.axis("off")
    plt.subplot(1,2,1)
    plt.imshow(newicon)
    plt.title("img")
    plt.axis("off")
    plt.show()
def showImg(img) :
    plt.figure(figsize=[20,40], dpi=400)
    plt.subplot(1,1,1)
    plt.imshow(img)
    plt.title("img")
    plt.axis("off")
    plt.show()

#匹配2张图
def matchImage( img1, img2) :
    return ( img1  == img2 ).all()
"""
img1 = Screens["home"]["img"]
img2 = Screens["home"]["img"]
print(matchImage( img1, img2))
"""

#按位置匹配大图和小图
def matchImageIcon( img, icon, point ) :
    x1 = point["x"]
    x2 = x1 + icon.shape[0]
    y1 = point["y"]
    y2 = y1 + icon.shape[1]
    if x1 >  img.shape[0] or y1 > img.shape[1] :
        return False
    img_temp = img [ x1 : x2, y1 : y2, : ]
    result = matchImage( img_temp, icon )
    if result :
        return {"x":0.5*(x1+x2),"y":0.5*(y1+y2)}
    else :
        return False
"""
img = Screens["home"]["img"]
icon = Screens["home"]["wechaticon"]["img"]
location = Screens["home"]["wechaticon"]["location"]
x = location["offset"]["x"] 
y = location["offset"]["y"]
point = {"x":x, "y":y}
temp = matchImageIcon( img, icon, point )
print(temp)
"""

#按位置匹配来图和资源
def matchScreenIcon( img, screenName, iconName ) :
    screen = Screens[screenName]
    icon = screen[iconName]
    iconImg = icon["img"]
    point = { "x":icon["location"]["offset"]["x"], "y":icon["location"]["offset"]["y"] }
    result = matchImageIcon( img, iconImg, point )
    return result
"""
img = Screens["home"]["img"]
temp = matchScreenIcon( img, "home", "wechaticon" )
print(temp)
"""

#在大图内搜索小图
def searchIconInImage( img, icon ) :
    for i in range( 0, img.shape[0]-icon.shape[0] ) :
        for j in range( 0, img.shape[1]-icon.shape[1] ) :
            icon_temp = img[ i:i+icon.shape[0], j:j+icon.shape[1] , : ]
            if matchImage( icon_temp, icon ) :
                return {"x":i, "y":j}
    return False
"""
img = getScreen()
icon= Screens["detail"]["copy"]["img"]
temp = searchIconInImage( img, icon )
print(temp)
"""

def searchEnlarge( img, screenName, iconName, locationName ) :
    screen = Screens[screenName]
    icon = screen[iconName]
    iconImg = icon["img"]
    enlarge = icon["enlarge"]
    location = icon[locationName]

    x1 = location["offset"]["x"]
    x2 = x1 + location["length"]["x"]
    y1 = location["offset"]["y"]
    y2 = y1 + location["length"]["y"]

    x1 = max(0, x1 - enlarge["x"])
    x2 = min(Screens["size"]["ScreenWidth"], x2 + enlarge["x"])
    y1 = max(0, y1 - enlarge["y"])
    y2 = min(Screens["size"]["ScreenHeight"], y2 + enlarge["y"])

    img_temp = img [ x1 : x2, y1 : y2, : ]
    result = searchIconInImage( img_temp, iconImg )
    if result :
        result["x"] = result["x"] + x1 + 0.5 * location["length"]["x"]
        result["y"] = result["y"] + y1 + 0.5 * location["length"]["y"]
    return result
"""
img = getScreen()
temp = searchEnlarge( img, "detail", "copy", "location" )
print(temp)
"""

def searchRegions( img, screenName, iconName ) :
    screen = Screens[screenName]
    icon = screen[iconName]
    iconImg = icon["img"]
    regions = icon["regions"]
    location = icon["location"]
    for region in regions :
        x1 = region["offset"]["x"]
        x2 = x1 + region["length"]["x"]
        y1 = region["offset"]["y"]
        y2 = y1 + region["length"]["y"]

        x1 = max(0, x1)
        x2 = min(Screens["size"]["ScreenWidth"], x2)
        y1 = max(0, y1)
        y2 = min(Screens["size"]["ScreenHeight"], y2)

        img_temp = img [ x1 : x2, y1 : y2, : ]
        result = searchIconInImage( img_temp, iconImg )
        if result :
            result["x"] = result["x"] + x1 + 0.5 * location["length"]["x"]
            result["y"] = result["y"] + y1 + 0.5 * location["length"]["y"]
        return result
"""
img = getScreen()
temp = searchRegions( img, "wpsedit", "paste" )
print(temp)

showIcon(img, "wpsedit", "paste")
location = Screens["wpsedit"]["paste"]["regions"][1]
showRegion(img, "wpsedit", location)
img = cutImg(img, location)
temp = searchRegions( img, "wpsedit", "paste" )
print(temp)
"""

#基于资源搜索Icon
def searchIcon( img, screenName, iconName ) :
    screen = Screens[screenName]
    icon = screen[iconName]
    result = matchScreenIcon( img, screenName, iconName )
    if result :
        return result
    if "enlarge" in icon.keys() :        
        result = searchEnlarge( img, screenName, iconName, "location" )
        if result :
            return result
    if "regions" in icon.keys() :
        result = searchRegions( img, screenName, iconName )
        if result :
            return result
    return False
"""
img = getScreen()
temp = searchIcon( img, "wpsedit", "paste" )
print(temp)
"""


#按位置截取图像数据
def getCharacter( img, location) :
    x1 = location["offset"]["x"]
    y1 = location["offset"]["y"]
    x2 = x1 + location["length"]["x"]
    y2 = y1 + location["length"]["y"]
    temp = img[x1:x2,y1:y2,:]
    return temp
"""
img = Screens["wechat"]["img"]
location = Screens["wechat"]["identity"]["location"]
icon = getCharacter( img, location)
plt.figure(figsize=[20,40], dpi=400)
plt.subplot(1,1,1)
plt.imshow(icon)
plt.axis("off")
plt.show()
"""

#取屏幕元素位置

#获取微信图标位置
def getWechat( img ) :
    screenName = "home"
    iconName = "wechaticon"
    return searchIcon( img, screenName, iconName )

#获取WPS图标位置
def getWPS( img ) :
    screenName = "home"
    iconName = "wpsicon"
    return searchIcon( img, screenName, iconName )

#获取“我的”图标位置
def getMe( img ) :
    screenName = "wechat"
    iconName = "me"
    return searchIcon( img, screenName, iconName )

#获取“相册”图标位置
def getAlbum( img ) :
    screenName = "me"
    iconName = "album"
    return searchIcon( img, screenName, iconName )

#获取“我的朋友圈”按钮的位置
def getMyFriendsCircle( img ) :
    screenName = "album"
    iconName = "myfriendscircle"
    return searchIcon( img, screenName, iconName )

#获取photo页面中detail按钮的位置
def getDetail( img ) :
    screenName = "photo"
    iconName = "detail"
    #return searchIcon( img, screenName, iconName )
    return( Screens["photo"]["detail"]["point"])

#获取relay标记的位置
def getRelay( img ) :
    screenName = "detail"
    iconName = "relay"
    return searchIcon( img, screenName, iconName )

#判断relay
def isRelay( img ) :
    return getRelay( img )

#获取复制菜单呼出点
def getCopyPoint( img ) :
    screenName = "detail"
    iconName = "identity"
    basic = searchIcon( img, screenName, iconName )
    offset = Screens["detail"]["identity"]["offset"]
    if basic :
        result = { "x": basic["x"] + offset["x"], "y": basic["y"] + offset["y"]}
        return result
    else :
        return False
"""
img = getScreen()
temp = getCopyPoint( img )
print(temp)
"""

#获取复制菜单的位置
def getCopyMenu( img ) :
    screenName = "detail"
    iconName = "copy"
    return searchIcon( img, screenName, iconName )
"""
img = getScreen()
icon = Screens["detail"]["copy"]["img"]
location = Screens["detail"]["copy"]["location"]
offset = location["offset"]
length = location["length"]
x1 = offset["x"]
x2 = x1+length["x"]
y1 = offset["y"]
y2 = y1+length["y"]
mark = img[x1:x2,y1:y2,:]
plt.figure(figsize=[20,40], dpi=400)
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("")
plt.axis("off")
plt.subplot(2,2,2)
plt.imshow(icon)
plt.title("")
plt.axis("off")
plt.subplot(2,2,3)
plt.imshow(mark)
plt.title("")
plt.axis("off")
plt.show()
temp = getCopyMenu(img)
print(temp)
"""

#获取wpsad页面“跳过的按钮位置
def getSkip( img ) :
    screenName = "wpsad"
    iconName = "skip"
    return searchIcon( img, screenName, iconName )

#获取wps页面document的位置
def getDocPoint( img ) :
    screenName = "wps"
    iconName = "document"
    return searchIcon( img, screenName, iconName )
#img = getScreen()
#print(getDocPoint( img ))

#获取键盘按钮的位置
def getKeyboard( img ) :
    screenName = "wpsedit"
    iconName = "keyboard"
    return searchIcon( img, screenName, iconName )
"""
img = getScreen()
screen = Screens["wpsedit"]
item = screen["keyboard"]
icon = item["img"]
location = item["location"]
offset = location["offset"]
length = location["length"]
x1 = offset["x"]
x2 = x1+length["x"]
y1 = offset["y"]
y2 = y1+length["y"]
mark = img[x1:x2,y1:y2,:]
plt.figure(figsize=[20,40], dpi=400)
plt.subplot(2,2,1)
plt.imshow(icon)
plt.title("")
plt.axis("off")
plt.subplot(2,2,2)
plt.imshow(mark)
plt.title("")
plt.axis("off")
plt.show()
temp = getCopyMenu(img)
print(temp)
"""

#获取键盘关闭时键盘按钮的位置
def getKeyboard_closed( img ) :
    screenName = "wpsedit"
    iconName = "keyboard_closed"
    return searchIcon( img, screenName, iconName )
"""
img = getScreen()
temp = getKeyboard_closed(img)
print(temp)
"""

#获取回车按钮的位置
def getEnter_26keys( img ) :
    screenName = "wpsedit"
    iconName = "enter"
    return searchIcon( img, screenName, iconName ) 
def getEnter_9keys( img ) :
    screenName = "wpsedit"
    iconName = "enter_9keys"
    return searchIcon( img, screenName, iconName ) 
def getEnter_widebottom_26keys( img ) :
    screenName = "wpsedit"
    iconName = "enter_widebottom"
    return searchIcon( img, screenName, iconName ) 
def getEnter_widebottom_9keys( img ) :
    screenName = "wpsedit"
    iconName = "enter_widebottom_9keys"
    return searchIcon( img, screenName, iconName ) 
def getEnter( img ) :
    widebottom = getEnter_widebottom_26keys( img )
    if widebottom :
        return widebottom
    else :
        widebottom_9keys = getEnter_widebottom_9keys( img )
        if widebottom_9keys :
            return widebottom_9keys
        else :
            key26 = getEnter_26keys( img )    
            if key26 :
                return key26
            else :
                key9 = getEnter_9keys( img )
                if key9 :
                    return key9
            return False
"""
img = getScreen()
temp = getEnter(img)
print(temp)
"""

#获取统计标签的位置
def getStatistics_opened( img ) :
    screenName = "wpsedit"
    iconName = "statistics"
    return searchIcon( img, screenName, iconName ) 
def getStatistics_closed( img ) :
    screenName = "wpsedit"
    iconName = "statistics_closed"
    return searchIcon( img, screenName, iconName ) 
def getStatistics( img ) :
    res1 = getStatistics_opened( img )    
    if res1 :
        return res1
    else :
        res2= getStatistics_closed( img )
        if res2 :
            return res2
    return False
"""
img = getScreen()
temp = getStatistics(img)
print(temp)
"""

#获取粘贴菜单呼出点
def getPastePoint( img ) :
    return Screens["wpsedit"]["pastepoint"]

#获取Paste菜单的位置
def getPasteMenu(img) :
    screenName = "wpsedit"
    iconName = "paste"
    return searchIcon( img, screenName, iconName ) 

#获取MultiPaste菜单的位置
def getMultiPaste(img) :
    screenName = "wpsedit"
    iconName = "multipaste"
    return searchIcon( img, screenName, iconName ) 
"""
img = getScreen()
temp = getMultiPaste(img)
print(temp)
"""

#获取保存按钮的位置
def getSave( img ) :
    screenName = "wpsedit"
    iconName = "save"
    return searchIcon( img, screenName, iconName ) 
"""
img = getScreen()
temp = getSave(img)
print(temp)
"""

#获取photo回退按钮的位置
def getBack_photo( img ) :
    screenName = "photo"
    iconName = "goback"
    return searchIcon( img, screenName, iconName ) 
#img = getScreen()
#print(getBack_photo(img))

#获取detail回退按钮的位置
def getBack_detail( img ) :
    screenName = "detail"
    iconName = "goback"
    return searchIcon( img, screenName, iconName )
#img = getScreen()
#print(getBack_detail(img))

#判断指定位置是否空行
def isEmptyLine( img, offset ) :
    emptyLine = Screens["wpsedit"]["emptyline"]["img"]
    left = Screens["wpsedit"]["emptyline"]["location"]["offset"]["y"]
    right = left + Screens["wpsedit"]["emptyline"]["location"]["length"]["y"]
    top = offset    
    lineHeight = Screens["wpsedit"]["emptyline"]["location"]["length"]["x"]
    bottom = top + lineHeight
    line = img[top:bottom,left:right,:]
    return matchImage( line, emptyLine )
"""
Screens = loadImgs()
img = Screens["wpsedit"]["img"]
temp = isEmptyLine( img, 500 )
print(temp)
"""
"""
from adb import getScreen
img = getScreen()
print(isHome(img))
"""

#判断screen身份

#判断图片是不是Home桌面
def isHome( img ) :
    screenName = "home"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )

#判断图片是不是left桌面
def isLeft( img ) :    
    screenName = "left"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )

#判断图片是不是right桌面
def isRight( img ) :
    screenName = "right"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )

#判断图片是不是Wechat主页
def isWechat( img ) :
    screenName = "wechat"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是WPS主页
def isWPS( img ) :
    screenName = "wps"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是Me页
def isMe( img ) :
    screenName = "me"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是Album页
def isAlbum( img ) :
    screenName = "album"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是List页
def isList( img ) :
    screenName = "list"
    iconName = "identity"
    return searchIcon( img, screenName, iconName ) 

#判断图片是不是Index页
def isIndex( img ) :
    screenName = "index"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是Photo页
def isPhoto( img ) :
    screenName = "photo"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是Detail页
def isDetail( img ) :
    screenName = "detail"
    iconName = "identity"
    return searchIcon( img, screenName, iconName ) 
""" 
img = getScreen()
temp = isList( img )
print(temp)
showIcon(img, "list", "identity")
"""

#判断图片是不是WPSAd页
def isWPSAd( img ) :
    screenName = "wpsad"
    iconName = "identity"
    return searchIcon( img, screenName, iconName )  

#判断图片是不是WPSEdit页
def isWPSEdit( img ) :
    screenName = "wpsedit"
    iconName = "identity"
    return searchIcon( img, screenName, iconName ) 

#判断图片是不是message页
def isOther( img ) :
    return getBack_detail(img) and (not isDetail(img))
#img = getScreen()
#print(isOther( img ))

#辨别当前页面
def currentScreen(img) :
    if isLeft(img) : return "left"
    elif isRight(img) : return "right"
    elif isWechat(img) : return "wechat"
    elif isWPS(img) : return "wps"
    elif isMe(img) : return "me"
    elif isAlbum(img) : return "album"
    elif isList(img) : return "list"
    elif isIndex(img) : return "index"
    elif isPhoto(img) : return "photo"
    elif isDetail(img) : return "detail"
    elif isWPSAd(img) : return "wpsad"
    elif isWPSEdit(img) : return "wpsedit"
    elif isOther(img) : return "other"
    else :return "all no"

#img = getScreen()
#print(currentScreen(img))
#showImgs()