# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 21:02
# @Author  : yimi
# @File    : homework_7_smallTest.py

# 1.注释是用来做什么的？注释分几类？分别如何定义？
# 注释：解释说明代码的相关信息
#       提示，防遗忘
#       特殊注释  # !/usr/bin/env python
#                 # -*-coding:utf-8-*-

# 分类： 单行注释  #
#        多行注释  """                  """
#                  '''                  '''


# 2.变量的命名应当符合什么规则？
# 由数字，字母，下划线组成
# 不能以数字开头，不能使用中文
# 不能使用关键字
# 不与内置函数，模块命名重名
# 区分大小写
# 见名知意

# 3.Python中关键字有哪些？请至少写出10个
# print  if   else    elif     while  switch  case    range   in    not in   for
# join  list  dict    string   break

# 4.变量的类型有哪些？
# int  float  long  bool  string   list   tuple  dict

# 5.如何查看变量的内存地址、变量的类型以及如何比较两个变量值的大小？
# id(varible)    type(varible)
#      ==
#  max(varible_1, varible_2)

# 6.数字类型的字符串（如："123"）与数字类型之间如何相互转换？

# num = int("123")
# print(type(num))
# print(num)
# num_str = str(123)
# print(type(num_str))
# print(num_str)

# 7.字符串与列表之间如何相互转换？
# str_1 = "123abc"
# str_1.split("")
# print(list(str_1))
#
# list_1 = ['1', '2', '3', 'a', 'b', 'c']
# list_to_str = "".join(list_1)
# print(list_to_str)

# 8.布尔类型与数字类型之间如何相互转换？
# print(int(True))
# print(bool(1))

# 9.Python中的运算符有哪些种类？
#  算术运算符      赋值运算符          逻辑运算符      比较运算符

# 10.Python中逻辑运算符有哪些？它们之间有什么区别？
# and   一假必假， 两真为真
# or    一真必真，两假为假
# not   以假乱真

# 11.序列类型是Python中指定的类型吗？属于序列类型的数据类型有哪些？
# 序列类型不是Python中指定的类型， 序列类型： string, list, tuple, dict

# 12.序列类型支持哪些操作？
# 通过索引取值
# 切片操作       [start:stop:step]
# 成员关系操作   in    not in
# 连接操作  +   同类型之间
# 重复操作  *
# 支持遍历
# 可求长度  len()
# 支持内置函数   all, any, list, len, max, min, sum

# 13.字典支持序列中的哪些操作
# 成员运算  not in    in
# 支持遍历
# 能求长度
# 支持的内置函数   all, any, list, len

# 字典元素访问
# keys()方法返回一个包含所有键的列表
# has_key()检查字典是否存在某一键
# values()返回一个包含所有值的列表
# get()根据键的返回值，如果不存在输入的键，返回None
# items()返回一个列表，元素是由(key,value)组成的元祖
# 字典元素的删除
# del()按键从字典中删除元素
# clear()清除字典中的所有元素
# pop()删除按关键字删除元素并返回它的值
# update方法
# update类似合并，把一个字典的键值合并到另一个字典，覆盖相同键的值。
# in运算
# 字典里的in运算用于判断某键是否在字典里，对于value值不适用

# 14.range支持序列中的哪些操作
# 不可变序列类型
# 通过索引取值
# 切片操作       [start:stop:step]
# 支持遍历
# 成员关系操作   in    not in
# 可求长度  len()
# 支持内置函数    all, any, list, len, max, min, sum

# 15.有哪些方法可以修改列表中的某个元素呢？

# list_1 = ["apple", 20, "s"]
# list_1[0] = "banana"
# list_1[list_1.index(20)] = 50
# print(list_1)
# list_1[0:2] = "orange", 30
# print(list_1)

# 16.列表中的append和extend的区别

# list_1 = ["apple", 20, "s"]
# print("原列表为：\n", list_1)
#
# list_1.append(["lemon", "orange"])
# print("append函数修改后的列表为：\n", list_1)
#
# list_2 = ["apple", 20, "s"]
# list_2.extend(["lemon", "orange"])
# print("extend 函数修改后的列表为：\n", list_2)

# 17.元组和列表之间如何相互转换？
# list_1 = ["apple", 20, "s"]
# print(tuple(list_1))
# tuple_1 = ('apple', 20, 's')
# print(list(tuple_1))

# 18.获取字典中的某个值，有哪几种方法？有什么区别？
# dict_1 = {"name":"yimi", "age": 18, "gender": "female"}
# # dict[key] 可以从字典中取值，key不存在会报错
# print(dict_1["name"])
# # 字典.get(key) 可以从字典中取值，key不存在不会报错
# print(dict_1.get("age"))

# 19.如何将一个字典的键、值、键值对分别转化为元组？

# list_1 = []
# list_2 = []
# list_3 = []
# dict_1 = {"name":"yimi", "age":18, "gender":"female"}

# for i in dict_1.keys():
#     list_1.append(i)
# print(tuple(list_1))

# for i in dict_1.values():
#     list_2.append(i)
# print(tuple(list_2))

# for i in dict_1.items():
#     list_3.append(i)
# print(tuple(list_3))

# 20.我们学过的，不可变类型有哪些？可变类型有哪些？
# 不可变类型：数字，字符串，元组
# 可变类型（mutable）：列表，字典

# 21.Python中是用什么方法来进行输出操作的？它有哪些常用的参数呢？
#  print()
#  位置参数， 可变参数，关键字参数

# 22.程序执行的流程有哪几种？
#  顺序执行
#  判断       if
#  循环       while    for

# 23.for和while的区别？

# 如果一个需求明确循环的次数，那么使用for循环,for循环适用于已知循环次数
# 如果一个需求，不知道循环了多少次，但当i>=n的时候停止循环,使用while循环。

# 24.局部变量和全局变量有什么区别？
# 全局变量：外部作用域定义
# 局部变量: 内部作用域定义

# 1.编写如下程序
# 使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和
# i = 2
# result = 0
# while(i<= 100):
#     if i%2 != 0:
#         i = -i
#     result += i
#     if i > 0:
#         i += 1
#     else:
#         i = (-i) + 1
# print(result)

# i = 2
# result = 0
# while(i<= 100):
#     if i%2 != 0:
#         result -= i
#     else:
#         result += i
#     i += 1
# print(result)
# 2.编写如下程序
# 用户输入考试成绩，当分数高于90（包含90）时打印A；
# 否则如果分数高于80（包含80）时打印B；
# 否则如果当分数高于70（包含）时打印C；
# 否则如果当分数高于60（包含60）时打印D；
# 其他情况就打印E

# score = float(input("请输入分数: "))
# if score >= 90.0:
#     print("A")
# elif score >= 80.0:
#     print("B")
# elif score >= 70.0:
#     print("C")
# elif score >= 60.0:
#     print("D")
# else:
#     print("E")

# 3.编写如下程序
# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番
# （例如：需要几年10000才能变成20000）

# principal = 10000
# year = 0
# while principal < 20000:
#     principal = principal * 1.0352
#     year = year + 1
#
# print('需要%d年一万元的存款才能连本带息翻番' % year)

# 4.编写如下程序
# 从键盘获取一个数字，然后计算它的阶乘，
# 例如输入的是3，那么即计算3!的结果，并输出
# 提示：
# a. 1!等于 1
# b. 2!等于 1*2
# c. 3!等于 1*2*3
# d. n!等于 1*2*3*...*n

num = int(input("请输入数字: "))

result = 1
for i in range(1, num+1):
    result = result * i
print("{0}的阶乘是：{1}".format(num, result))
