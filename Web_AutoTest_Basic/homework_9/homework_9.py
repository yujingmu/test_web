# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 22:18
# @Author  : yimi
# @File    : homework_9.py

# 1.什么是文件？有哪些种类？
# 文件：长期存储设备上的一段数据
# 种类：硬盘，U盘，移动硬盘，光盘

# 2.文件的操作步骤
#  打开， 读写， 关闭

# 3.操作文件的常用函数/方法有哪些？
# file.read()              file.readline()        file.readlines()
# file.close()            file.write()

# 4.read、readline、readlines有什么区别？
# read 一次性读取文件内的所有内容，读取完内容后，指针在末尾     小文件复制
# readline 每次读取一行，按行读取，每读取一行，指针向下移动一行， 返回类型为字符串       大文件复制
# readlines  每次读取一行，按行读取，每读取一行，指针向下移动一行， 返回类型为列表       大文件复制

# 提示：请从返回的对象类型、文件指针位置、应用场景来阐述

# 5. 打开文件的方式有哪些？
#   r    w    a    r+   w+    a+    b

# 6.编写如下程序
# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制，并修改文件名
#
# music_origin = open("心如止水.mp3", mode='rb')        # 二进制类型文件
# music_copy = open("xinruzhishui.mp3", mode = "wb+")
#
# resource = music_origin.read()
# music_copy.write(resource)
#
# music_origin.close()
# music_copy.close()


# 7.编写如下程序
#
# 有两行数据，存放在txt文件里面：
#
# url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
#
# url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
#
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
#
# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
#
# {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
#
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！

file = open("test_date.txt")

list_data = []
data= file.readlines()

for line in data:
    dict_data = {}
    data_line = line.strip('\n').split('@')
    for item in data_line:
        dict_1 = item.split(':', 1)
        dict_data[dict_1[0]] = dict_1[1]
    list_data.append(dict_data)
print(list_data)

file.close()

# 8.使用思维导图总结本次课的内容
#
#
# 二、选作题
# 9.编写如下程序
#
# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
#
# a.第一行添加如下内容：
# name,age,gender,hobby,motto
#
# b.从第二行开始，每行添加具体信息，例如：
#
# 可优,17,男,臭美,Always Be Coding!
#
# 柠檬小姐姐,16,女,可优,Lemon is best!
#
# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
#
# person_info = [{"name": "可优",
#                "age": 17,
#                "gender": "男",
#                "hobby": "臭美",
#                "motto": "Always Be Coding!"},
#               {"name": "柠檬小姐姐",
#                "age": 16,
#                "gender": "女",
#                "hobby": "可优",
#                "motto": "Lemon is best!"},
#               ]
# d.将所有用户信息写入到txt文件中之后，然后再读出
#
# e.有精力的同学可以试试，多种方法来读取文件，比如csv模块（不作要求）

# 注意：csv格式的数据，是以英文逗号分隔的

# file = open('data.csv', 'w+')
# list_1 = ['name','age','gender','hobby','motto']
# for data in list_1:
#     file.write(data)
#     file.write(',')
#
# value = file.read()
# print(value)