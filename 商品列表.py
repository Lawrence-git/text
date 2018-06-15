# 提示充值
balance = 0
shoppingCart = []
print("余额为0,请充值后再购买商品")
balance = int(input("请输入充值金额(元): "))
print('+++++++++++++++++++++++++++')
print("现余额为 %s 元" %balance)
print('+++++++++++++++++++++++++++')

# 循环购买
# 设置跳出标签
exit_flag = False
while not exit_flag:

    # 商品列表
    products = [
        ['Mac Book Pro',17800],
        ['iphone X',8500],
        ['ipad Pro',17800],
        ['iMac',17800],
        ['Mac Pro',27800]
    ]
    print("------------ 商 品 列 表 ------------")
    for index,product in enumerate(products):
        print("{:3}.  {:12}  {:10}".format(index,product[0],product[1]))
    print("-------------- E N D --------------")

    # 选择商品,添加到购物车
    count = 0
    choice = (input("输入编号购买商品: "))
    if choice.isdigit():
        shoppingCart.append(products[eval(choice)])
        print("\n")
        print("┏━━━━━━━━━━━ 购物车 ━━━━━━━━━━┓")
        for product in shoppingCart:
            count += 1
            print("{:3}.  {:12}  {:10}".format(count, product[0], product[1]))
            balance-=product[1]
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("余额剩余 %s 元"%(balance))

    elif choice == 'q':

        exit_flag = True








# for index, product in shoppingCart:
#     print("\n")
#     print("┏━━━━━━━━━━━ 购物车 ━━━━━━━━━━┓")
#     print(" %s.  %s   %s" % (index, product[0], product[1]))
#     print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")