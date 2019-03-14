"""
    name ： interact
    usage : from interact import tapPoint, pressPoint, tapLocation, pressLocation

"""

from adb import tap, press

"""
本节操作均以纵向为主轴
adb命令以横向为主轴
需要以横向为主轴时，应直接使用adb模块里的tap、press、swipe函数
"""

#位置转点
def location2Point(location) :
    x = location["offset"]["x"] + 0.5 * location["length"]["x"]
    y = location["offset"]["y"] + 0.5 * location["length"]["y"]
    return {"x":x,"y":y}


#xy互换
def exchangeXY(point) :
    return {"x":point["y"], "y":point["x"]}

#触摸点
def tapPoint(Point) :
    point = exchangeXY(Point)
    tap(point["x"],point["y"])
#tapPoint("x":30,"y":300)

#长按点
def pressPoint(Point) :
    point = exchangeXY(Point)
    press(point["x"],point["y"])
#pressPoint(DetailTarget1)

#触摸位置
def tapLocation(location) :    
    point = location2Point(location)
    tap(point["x"],point["y"])
#tapLocation({"offset":{"x":2070,"y":510},"length":{"x":65,"y":65}})

#长按位置
def pressLocation(location) :
    point = location2Point(location)
    press(point["x"],point["y"])
#pressLocation({"offset":{"x":2070,"y":510},"length":{"x":65,"y":65}})

