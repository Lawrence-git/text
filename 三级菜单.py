# 数据结构：
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
# 设置一级菜单变量
firstLayer = menu
# 设置初始上级菜单变量
lastLayer = []

for k in menu:
    print(k)
while True:
    choice = input('go to -->: ')
    # 判断 choice 是否在 firstLayer 中
    if choice in firstLayer:
        # 添加 firstLayer 到上级菜单列表中
        lastLayer.append(firstLayer)
        # 一级菜单变为 firstLayer[choice] 例如: 北京---->北京[海淀]----->北京[海淀][五道口]
        firstLayer = firstLayer[choice]
        for k in firstLayer:
            print(k)
    elif choice == 'b':
        # 删除并获取 lastLayer 列表中最后一级菜单
        for k in lastLayer.pop():
            print(k)
    elif choice == 'q':
        exit()



