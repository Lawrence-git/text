# -*- coding:utf-8 -*-
# 打开并读取文件 login.txt, 如果是空文件, 则创建一个空列表. 否则 eval() 格式化列表
with open('login.txt') as f:
    ls = f.read().strip()
    if len(ls) == 0:
        ls = []
    else:
        ls = eval(ls)

# 默认可登录用户信息
users = [
    ['susan','123123'],
    ['ada','abc123'],
    ['admin','admin'],

]

# 设定初始登录次数, 如登录错误三次, 则退出程序
count = 0
while count < 3:
    login_name = input('Pleas input your username: ')
    # 检查 login_name 是否存在 login.txt 文件的 ls 列表中
    if login_name in ls:
        print('User Locked, Please contact administrator')
        break
    login_pwd = input('Please input your password: ')
    # 检查输入的 login_name 和 login_pwd 是否与默认登录用户信息一致
    if login_name == users[0][0] and login_pwd == users[0][1]:
        print('Success, Welcome \033[1;32m %s \033[0m' %login_name)
    elif login_name == users[1][0] and login_pwd == users[1][1]:
        print('Success, Welcome \033[1;32m %s \033[0m' %login_name)
    elif login_name == users[2][0] and login_pwd == users[2][1]:
        print('Success, Welcome \033[1;32m %s \033[0m' %login_name)

    else:
        # 登录信息不一致,则把登录名添加到 ls 列表并写入 login.txt 文件
        ls.append(login_name)
        with open('login.txt','w+') as f:
            f.write(str(ls))
            f.close()
        print('✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖')
        print('Username or password Error', '\n\033[1;31m%s\033[0m more chances left.'%(2-count))
        print('✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖')
        count += 1
