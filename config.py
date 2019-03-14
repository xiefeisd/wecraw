"""
    name : config
    usage : from config import ADB, ReferPath, CachePath, ScreenWidth, ScreenHeight, Screens

"""

#ADB
ADB = {
    "commandpPefix": "C:/Users/xiefe/AppData/Local/Android/Sdk/platform-tools/",
    "cachePath": "C:/wecraw/temp",
}

#文件路径
ReferPath = "C:/wecraw/refer"
CachePath = "C:/wecraw/cache"

#屏幕尺寸
ScreenWidth = 1080
ScreenHeight = 2248

#屏幕元素
Screens = {    
    "size":{
        "ScreenWidth": ScreenWidth,
        "ScreenHeight": ScreenHeight,
    },
    #手机主屏
    #微信、WPS放同一个屏不行，狗日的小米
    "home": {
        "refer": ReferPath + "/home.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":2070,"y":510},"length":{"x":65,"y":65}},
            "enlarge": {"x":100,"y":100},
            "regions": [
                {"offset":{"x":2055,"y":00},"length":{"x":90,"y":ScreenWidth}},
            ]
        },
        #微信图标
        "wechaticon": {
            "location": {"offset":{"x":200,"y":110},"length":{"x":60,"y":70}},
            "enlarge": {"x":100,"y":100},
            "regions": [
                {"offset":{"x":180,"y":100},"length":{"x":1700,"y":900}},
            ]
        },
        #WPS图标
        "wpsicon": {
            "location": {"offset":{"x":200,"y":366},"length":{"x":80,"y":100}},
            "enlarge": {"x":100,"y":100},
            "regions": [
                {"offset":{"x":180,"y":100},"length":{"x":1700,"y":900}},
            ]
        },
    },
    #手机左屏
    "left": {
        "refer": ReferPath + "/left.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":489,"y":107},"length":{"x":60,"y":70}},
            "enlarge": {"x":10,"y":10},
        },
        #微信图标
        "wechaticon": {
            "location": {"offset":{"x":489,"y":107},"length":{"x":60,"y":70}},
            "enlarge": {"x":10,"y":10},
        },
    },
    #手机右屏
    "right": {
        "refer": ReferPath + "/right.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":491,"y":112},"length":{"x":80,"y":95}},
            "enlarge": {"x":10,"y":10},
        },
        #WPS图标
        "wpsicon": {
            "location": {"offset":{"x":491,"y":112},"length":{"x":80,"y":95}},
            "enlarge": {"x":10,"y":10},
        },
    },
    #微信
    "wechat": {
        "refer": ReferPath + "/wechat.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":99}},
            "enlarge": {"x":100,"y":100},
        },
        #“我的”按钮
        "me": {
            "location": {"offset":{"x":2120,"y":910},"length":{"x":110,"y":70}},
            "enlarge": {"x":100,"y":100},
        }
    },
    #“我的”
    "me": {
        "refer":  ReferPath + "/me.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":2120,"y":910},"length":{"x":110,"y":70}},
            "enlarge": {"x":100,"y":100},
        },
        #相册按钮
        "album": {
            "location": {"offset":{"x":950,"y":45},"length":{"x":65,"y":200}},
            "enlarge": {"x":100,"y":100},
        }
    },
    #相册
    "album": {
        "refer": ReferPath + "/album.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":175}},
            "enlarge": {"x":100,"y":100},
        },
        #我的朋友圈
        "myfriendscircle": {
            "location": {"offset":{"x":400,"y":785},"length":{"x":50,"y":240}},
            "enlarge": {"x":100,"y":100},
        }
    },
    #朋友圈列表
    "list": {
        "refer": ReferPath + "/list.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":260}},
            "enlarge": {"x":100,"y":100},
        },
        "properties": {
            #资源（微信朋友圈内容列表）显示区域
            "top": 300,
            "bottom": 2248,
            "head": 1000,
            "totaloffset":1000,
            #显示区背景色与前景色
            "backgroundColor" : [255,255,255,255],
            "foregroundColors" : [[247,247,247,255],[239,239,239,255]],
            #竖直扫描屏幕的搜索线在水平方向的定位
            "searchLineLocation": 540
        }
    },
    #朋友圈列表首页
    "index": {
        "refer": ReferPath + "/index.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":40}},
            "enlarge": {"x":10,"y":10},
        },
    },
    #照片
    "photo": {
        "refer": ReferPath + "/photo.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":2124,"y":0},"length":{"x":124,"y":1080}},
            "enlarge": {"x":100,"y":100},
        },
        #详情按钮
        "detail": {
            "location": {"offset":{"x":2160,"y":923},"length":{"x":50,"y":127}},
            "enlarge": {"x":100,"y":100},
            "point": {"x":2185,"y":985}
        },
        #回退按钮
        "goback": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":40}},
            "enlarge": {"x":10,"y":10},
        }
    },
    #详情
    "detail": {
        "refer": ReferPath + "/detail.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":175}},
            "enlarge": {"x":100,"y":100},
            "offset": {"x":190, "y":80},
        },
        #复制菜单
        "copy": {
            "location": {"offset":{"x":485,"y":240},"length":{"x":50,"y":95}},
            "enlarge": {"x":100,"y":100},
            "regions": [
                {"offset":{"x":360,"y":180},"length":{"x":380,"y":270}},
            ]
        },
        #转发特征
        "relay": {
            "refer": ReferPath + "/detail_relay.png",
            "location": {"offset":{"x":366,"y":182},"length":{"x":14,"y":14}},
            "enlarge": {"x":10,"y":10},
        },
        #回退按钮
        "goback": {
            "location": {"offset":{"x":150,"y":35},"length":{"x":55,"y":40}},
            "enlarge": {"x":10,"y":10},
        }
    },
    #WPS主页面
    "wps": {
        "refer": ReferPath + "/wps.png",
        "identity": {
            "location": {"offset":{"x":150,"y":210},"length":{"x":50,"y":280}},
            "enlarge": {"x":100,"y":100},
        },
        "document": {
            "location": {"offset":{"x":920,"y":190},"length":{"x":45,"y":110}},
            "regions": [
                {"offset":{"x":430,"y":180},"length":{"x":1230,"y":130}},
            ]
        },  
    },
    #WPS启动广告页
    "wpsad": {
        "refer": ReferPath + "/wpsad.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":2050,"y":345},"length":{"x":120,"y":390}},
            "enlarge": {"x":100,"y":100},            
        },
        #“跳过”按钮
        "skip": {
            "location": {"offset":{"x":2010,"y":940},"length":{"x":40,"y":110}},
            "enlarge": {"x":100,"y":100},            
        }
    },
    #WPS编辑页
    "wpsedit": {
        "refer": ReferPath + "/wpsedit.png",
        #身份识别
        "identity": {
            "location": {"offset":{"x":145,"y":40},"length":{"x":55,"y":110}},
            "enlarge": {"x":100,"y":100}, 
        },
        #回车按钮
        "enter": {
            "location": {"offset":{"x":2135,"y":975},"length":{"x":35,"y":50}},
            "enlarge": {"x":100,"y":100},
        },
        #9键时的回车按钮
        "enter_9keys": {
            "refer": ReferPath + "/wpsedit_9keys.png",
            "location": {"offset":{"x":2132,"y":964},"length":{"x":35,"y":52}},
            "enlarge": {"x":100,"y":100}, 
        },
        #宽底回车按钮
        "enter_widebottom": {
            "refer": ReferPath + "/wpsedit_widebottom.png",
            "location": {"offset":{"x":2086,"y":976},"length":{"x":33,"y":49}},
            "enlarge": {"x":100,"y":100}, 
        },
        #宽底9keys回车按钮
        "enter_widebottom_9keys": {
            "refer": ReferPath + "/wpsedit_widebottom_9keys.png",
            "location": {"offset":{"x":2080,"y":962},"length":{"x":40,"y":57}},
            "enlarge": {"x":100,"y":100}, 
        },
        #统计标签
        "statistics": {
            "location": {"offset":{"x":1227,"y":59},"length":{"x":44,"y":80}},
            "enlarge": {"x":10,"y":10},
            "offset": {"x":-50,"y":0}, 
        }, 
        #键盘关闭状态的统计标签
        "statistics_closed": {
            "refer": ReferPath + "/wpsedit_statistics.png",
            "location": {"offset":{"x":2030,"y":59},"length":{"x":44,"y":80}},
            "enlarge": {"x":10,"y":10}, 
            "offset": {"x":-50,"y":0}, 
        },  
        #键盘按钮
        "keyboard": {
            "location": {"offset":{"x":1360,"y":150},"length":{"x":55,"y":60}},
            "enlarge": {"x":10,"y":10}, 
        },
        #键盘关闭时的按钮
        "keyboard_closed": {
            "refer": ReferPath + "/wpsedit_full.png",
            "location": {"offset":{"x":2163,"y":150},"length":{"x":55,"y":60}},
            "enlarge": {"x":10,"y":10}, 
        },
        #粘贴菜单
        "paste": {
            "location": {"offset":{"x":755,"y":390},"length":{"x":42,"y":83}},
            "enlarge": {"x":100,"y":10}, 
            "regions": [
                {"offset":{"x":230,"y":375},"length":{"x":1330,"y":100}},
                {"offset":{"x":230,"y":0},"length":{"x":1330,"y":1080}},
            ]
        },
        #选中粘贴菜单
        "multipaste": {
            "refer": ReferPath + "/wpsedit_multipaste.png",
            "location": {"offset":{"x":67,"y":740},"length":{"x":55,"y":40}},
            "regions": [
                {"offset":{"x":230,"y":0},"length":{"x":1330,"y":1080}},
            ]
        },
        #保存按钮
        "save": {
            "location": {"offset":{"x":144,"y":220},"length":{"x":55,"y":55}},
            "enlarge": {"x":10,"y":10}, 
        },
        #空行
        "emptyline": {
            "location": {"offset":{"x":305,"y":70},"length":{"x":82,"y":1010}},
        },
        #编辑区
        "editregion": {
            "region": {"offset":{"x":240,"y":0},"length":{"x":1110,"y":1080}},
            "left": 70,
            "lineHeight": 82,
        },
        #粘贴点
        "pastepoint": {"x":950,"y":980},
    },
}
