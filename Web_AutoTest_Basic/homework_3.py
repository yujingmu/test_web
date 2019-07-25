#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 22:38
# @Author  : yimi
# @File    : homework_3.py

# 1.个人信息展示
#
# 在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
# 按照以下格式输出：
# **************************************************
# 个人信息展示
# 姓名（网名）
# 年龄：年龄
# 性别：性别
# 爱好：爱好
# 座右铭：座右铭
# **************************************************
# 提示：可以使用%或者format来格式化显示

# print("*"*50)
# print("个人信息展示")
# print("\n")
# name = input("姓名：")
# age = int(input("年龄："))
# gender = input("性别：")
# hobby = input("爱好：")
# motto = input("座右铭：")
# print("姓名（网名）: {}".format(name) )
# print("年龄：{0}".format(age))
# print("性别：{}".format(gender))
# print("爱好：%s"%(hobby))
# print("座右铭：%s"%(motto))
# print("*"*50)

# 2.Python中的序列类型有哪些？支持哪些操作？
# 序列类型： 字符串， 列表， 元素，字典
# 支持操作：通过索引获取指定位置的元素
#           切片操作
#           成员关系操作符（in 或not in）
#           连接操作符 +
#           重复操作符 *
#           支持遍历
#           能求长度


# 3.编写代码，用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，打印输出“周末”
#
# 提示：可以使用序列中的任何一种类型
while(1):
    tuple_1 = ("周一", "周二", "周三", "周四", "周五", "周末", "周末")
    try:
        number = int(input("请输入星期："))

        if number >= 1 and number <= 7:
            print(tuple_1[number-1])
            break
        else:
            print("输入数据不正确，请重新输入")
    except BaseException:
        print("输入数据类型不正确，请重新输入")

# 4.列表中append和extend方法的区别，请举例说明
# list_1 = ["apple", 20, "s"]
# print("原列表为：\n", list_1)
#
# list_1.append(["lemon", "orange"])
# print("append函数修改后的列表为：\n", list_1)
#
# list_2 = ["apple", 20, "s"]
# list_2.extend(["lemon", "orange"])
# print("extend 函数修改后的列表为：\n", list_2)

# 5.删除如下列表中的"矮穷丑"，写出能想到的所有方法
#
# keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# keyou_info.pop(3)
# print(keyou_info)
#
# keyou_info_1 = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# del keyou_info_1[-5]
# print(keyou_info_1)
#
# keyou_info_2 = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# keyou_info_2.remove("矮穷丑")
# print(keyou_info_2)
#
# keyou_info_3 = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# keyou_info_3[3:4] = []
# print(keyou_info_3)

# 6.元组和列表有什么区别？分别应用于哪些场景？
#  相同点：都是序列类型
#  不同点：元组中的数据不能修改， 列表中的数据可修改
#  使用场景， 元组：归档，原数据保存
#             列表：列表存储相同类型的数据

# 7.创建元组有哪些方式？
# print(type(tuple('20')))
# print(type(('apple',)))
# print(type((1, 2, 3, 4)))
# print(type(tuple([1, 2, 3, 4])))
# tuple_1 = "lemon","apple"
# print(type(tuple_1))

# 8.定义两个字典用于表述你的个人信息
#
# 第一个字典存放你的这些信息：姓名、性别、年龄、身高
#
# 第二个字典存放你的其他信息：性格、爱好、座右铭
#
# a.将两个字典合并为第三个字典之后，打印出来
# b.觉得自己很年轻的，可以去整个容（修改年龄），然后露个脸（打印出来）
# c.对你的座右铭很感兴趣，请将其取出来
# d.如果你觉得自己精力充沛，又好折腾，可以尝试一下，字典支持序列类型的哪些操作？
