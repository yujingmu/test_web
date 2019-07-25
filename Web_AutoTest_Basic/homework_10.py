# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 22:07
# @Author  : yimi
# @File    : homework_10.py
# 一、必做题
# 1.什么是异常？为什么要捕获异常？
# 程序运行时，提示的错误信息为异常
# 捕获异常，程序可在抛出错误的信息后不终止程序运行

# 2.异常的完整语法格式
# try:
    # 尝试执行的代码
    # pass
# except 错误类型1：
    # pass
# except 错误类型2：
    # pass
# except (错误类型3，错误类型4)：
    # pass
# except Exception as e:
    # raise e    # 抛出错误信息
# else:
    # pass     # 没有异常才会执行的代码
# finally:
    # print("无论是否有异常，都会执行")

# 3.在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？
# 如果try的块语句中没有异常，执行else的块语句和finally块语句都会被执行，except的块语句不会被执行
# 如果try的块语句中有异常，执行except的块语句和finally的块语句， else的块语句不被执行
#
# 4.编写如下程序

# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
while True:
    try:
        weight = float(input("请输入橘子的重量："))
        price = weight * 4.5
        print("应付款：", price)
        break
    except BaseException:
        print("输入数据类型不正确，请重新输入橘子的重量")

# 5.编写如下程序

# 优化剪刀石头布游戏程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
# h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能（选做）

import random
while(1):
    try:
        num_1 = int(input("请输入要出的拳 _石头（1）／剪刀（2）／布（3）:"))

        if num_1 > 3 or num_1 < 1:
            print("输入数据不正确，请重新输入")
            continue

        num_2 = random.randint(1, 3)
        if num_2 == 1:
            print("我出石头")
        elif num_2 == 2:
            print("我出剪刀")
        else:
            print("我出布")

        if (num_1 == 1 and num_2 == 2) or (num_1 == 2 and num_2 == 3) or (num_1 == 3 and num_2 ==1):
            print("恭喜你，你赢了")
        elif (num_1 == num_2) or (num_1 == num_2) or (num_1 == num_2):
            print("平局")
        else:
            print("Oh, my god, 我赢了")

        break
    except BaseException:
        print("输入数据类型不正确，请重新输入")

