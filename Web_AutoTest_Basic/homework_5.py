#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 20:18
# @Author  : yimi
# @File    : homework_5.py

# 1.break和continue的区别
# continue:某一条件满足时，不执行后续重复的代码，开始下一次循环
# break:某一条件满足时，退出循环，不再执行后续重复的代码

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
#
        if (num_1 == 1 and num_2 == 2) or (num_1 == 2 and num_2 == 3) or (num_1 == 3 and num_2 ==1):
            print("恭喜你，你赢了")
        elif (num_1 == num_2) or (num_1 == num_2) or (num_1 == num_2):
            print("平局")
        else:
            print("Oh, my god, 我赢了")

        break
    except BaseException:
        print("输入数据类型不正确，请重新输入")

# 2.while和for循环的异同点
# 相同点: 都能循环做一件重复的事情；
# 不同点: for循环是在序列穷尽时停止，while循环是在条件不成立时停止.


# 3.函数有哪些特性
# 封装,一个类就是一个封装了数据以及操作这些数据的代码的逻辑实体
# 继承,让某个类型的对象获得另一个类型的对象的属性的方法
# 多态,一个类实例的相同方法在不同情形有不同表现形式


# 4.Pycharm中Debug调试的Step Over(F8)、Step Into(F7)区别
# Step Over(F8): 单步执行代码，会把函数条用看做是一行代码直接执行
# Step Into(F7): 单步执行代码，如果是函数，会进入函数内部


# 5.写出将列表翻转的所有方法
# 将列表[13, 20, 42, 85, 9, 45]翻转之后为[45, 9, 85, 42, 20, 13]

list_1 = [13, 20, 42, 85, 9, 45]
list_1.reverse()
print(list_1)
#
list_2 = [13, 20, 42, 85, 9, 45]
list_3 = list_2[::-1]
print(list_3)


# 6.取出列表中最大的值
# 将列表[13, 20, 42, 85, 9, 45]中的最大值为85
# 提示：使用多种方法

list_1 = [13, 20, 42, 85, 9, 45]
#
def find_max_num(list_1):
    num = list_1[0]       # 最大
    for i in range(0,len(list_1)): # 从第二个元素开始对比
        if list_1[i] > num:
            num = list_1[i]
    return {"max":num}
#
max = find_max_num(list_1)
print(max)


list_1 = [13, 20, 42, 85, 9, 45]
for i in range(0, len(list_1)):
    for j in range(i, len(list_1)):
        if list_1[i] > list_1[j]:
            list_1[i], list_1[j] = list_1[j], list_1[i]
print(list_1[-1])


# 7.编写如下程序
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确

while(True):
    try:
        tuple_1= ("周一","周二","周三","周四","周五","周末","周末")
        num = int(input("请输入数字（用户输入1-7七个数字，分别代表周一到周日）"))
        if num < 0 and num > 7:
            print("输入有误，请重新输入！")
            continue
        if num == 0:
            break
        print(tuple_1[num-1])
    except BaseException:
        print("输入有误，请重新输入！")


# 8.编写如下程序
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
#
# 低于18.5： 过轻
# 18.5-25：   正常
# 25-28：      过重
# 28-32：      肥胖
# 高于32：   严重肥胖

height = float(input("请输入体重(公斤)："))
weight = float(input("请输入身高(米)："))
BMI = height/weight**2

if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI < 25:
    print("正常")
elif 25 <= BMI < 28:
    print("过重")
elif 28 <= BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")

# 9.编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best

def login(username, password):
    if username == "lemon" and password == "best":
        print("登录系统成功")
    else:
        print("用户名或密码错误")

username = input("username: ")
passwd = input("password: ")
login(username, passwd)

# 11.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
list_1 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
list_2 = []

for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)


# 12.编写如下程序
# 打印出1-100之间除了含7和7的倍数之外的所有数字

for i in range(0, 101):

    if i%7 == 0:
        print("\n")
        continue

    print(i, end="\t")


# 13.编写如下程序
# 输入键盘数字键(0~9)，返回数字键上方字符
# a.定义如下字典num_str_dic = {'1': '!', '2': '@', # '3': '#',
# '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
# b.例如：键盘输入5，程序输出%
# c.键盘输入0~9，正常输出字符之后，退出程序，否则继续提示输入

num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
while(True):
    try:
        num = int(input("请输入数字(0~9)："))
        if 0 <= num <= 9:
            print(num_str_dic[str(num)])
            break
        else:
            print("请重新输入")
    except Exception:
        print("请重新输入")





