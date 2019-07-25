#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 22:52
# @Author  : yimi
# @File    : format_print.py

# print("字符串%s" % "sun")
# print("my name is %s, %d years old, I like %s" %("berry", 25, "reading"))
#
# print("I like {}".format("eating"))
# print("1, {0}, {0}, {1}".format(2, 5,))
#
# # 1.序列类型中支持的操作
# zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
# # 2.通过索引取值
# print(zodiac[3])                # 兔
# # 3.切片操作
# print(zodiac[1:-1])             # 牛虎兔龙蛇马羊猴鸡狗
# # 4.成员关系操作
# print("龙" in zodiac)           # True
# # 5.连接操作 +
# new_zodiac = zodiac + "猫"
# print(new_zodiac)               # 鼠牛虎兔龙蛇马羊猴鸡狗猪猫
# # 6.重复操作 *
# print(zodiac * 2)               # 鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪
# # 7.支持遍历
# for item in zodiac:
#     print(item)
# # 鼠 牛 虎 兔 龙 蛇 马 羊 猴 鸡 狗 猪
# #  8.求长度
# print(len(zodiac))              # 12


# 列表相关操作
# str1 = "hello world!"
# list1 = ["天气", 18, str1, True, None, ["python", "java", "PHP"]]
# print("原列表： \n",list1)
# #  1.修改列表
# list1[1] = 25
# print("修改后的列表为：\n", list1)
# #  ['天气', 25, 'hello world!', True, None, ['python', 'java', 'PHP']]
# # 通过切片来赋值
# list1[3:5] = [1, 0]
# print("修改后的列表为：\n", list1)
# #  ['天气', 25, 'hello world!', 1, 0, ['python', 'java', 'PHP']]
# # 2.插入元素
# list1.append(["apple", "lemon", "orange"])
# print("append函数修改后的列表为：\n", list1)
# #  ['天气', 25, 'hello world!', 1, 0, ['python', 'java', 'PHP'], ['apple', 'lemon', 'orange']]
# # extend将序列类型数据扩充到列表中
# list1.extend(["apple", "lemon", "orange"])
# print("extend 函数修改后的列表为：\n", list1)
# # ['天气', 25, 'hello world!', 1, 0, ['python', 'java', 'PHP'], ['apple', 'lemon', 'orange'], 'apple', 'lemon', 'orange']
# list1.extend("lemon")
# print("extend 函数修改后的列表为：\n", list1)
# #  ['天气', 25, 'hello world!', 1, 0, ['python', 'java', 'PHP'], ['apple', 'lemon', 'orange'], 'apple', 'lemon', 'orange', 'l', 'e', 'm', '
# # insert 在指定位置插入数据
# list1.insert(3, "apple")
# print("insert在指定位置插入数据：\n", list1)
# # 删除元素
# del list1[1]
# print("删除索引为1的数据：\n", list1)
# #  remove 删除第一个出现的元素
# list1.remove(0)
# print("remove删除指定数据：\n", list1)
# # pop
# print(list1.pop())    # 删除数组最后一个元素，并返回该元素
# print(list1)
# print(list1.pop(4))
# print(list1)
#
# # 查找列表中的某个数据
# print(list1.count("l"))
#
# # 清空列表
# print(list1.clear())

num = [1, 20, 6, 50, 62]
num.sort()        # 由小到大排列
print(num)
num.sort(reverse=True)
print(num)         # 由大到小排列






