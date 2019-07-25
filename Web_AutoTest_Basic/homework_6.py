#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:06
# @Author  : yimi
# @File    : homework_6.py


# 1.函数有哪几种参数类型，分别有什么特点？
# 位置参数：形参和实参一一对应
# 关键字参数：name = "ss"
# 默认参数： 放在其他参数类型之后
# 可变参数： 所传参数个数不确定


# 2.在函数调用时，位置参数和关键字参数的顺序
# 位置参数在前， 关键字参数在后

# 3.什么是拆包（unpack）和打包（pack）？
# 4.哪些类型可以拆包（unpack）？拆包时变量的个数要什么要求？
# 字典，元组，列表，字符串可以拆包
# unpack:
# dict_1 = {"name":"yimi", "age":26}
# (a, aa),(b, bb) = dict_1.items()        # 拆包时变量（字典对）的个数与字典中字典对的个数一样
# print((a, aa),(b, bb))
#
# list_1 = [1, 2]
# a, b = list_1             # 拆包时变量的个数与列表中元素的个数一样
# print(a, b)
#
# tuple_1 = (12, 56)
# x, y = tuple_1             # 拆包时变量的个数与元组中元素的个数一样
# print(x, y)
#
# str_1 = "da y"
# m,n, a, b= str_1            # 拆包时变量的个数与字符串中的字符个数一样
# print(m, n, a, b)


# 5.函数的可变参数是什么？有哪几种？为什么要使用可变参数？
# 函数中所传参数不确定， 两种， 位置参数， 关键字参数


# 6.将两个变量的值进行交换（a = 100, b = 200）
# a.交换之后，a = 200， b = 100
# b.使用你能想到的所有方法来实现
# a = 100
# b = 200
# a, b = b, a
# print("a={},b={}".format(a, b))

# a = 100
# b = 200
# tem = a
# a = b
# b =tem
# print("a = {}, b = {}".format(a, b))

# a = 100
# b = 200
# tem = a+b
# a = tem - a
# b = tem - b
# print("a = {}, b = {}".format(a, b))


# 7.编写如下程序
# 将用户输入的所有数字相乘之后对20取余数
# a.用户输入的数字个数不确定
# b.请使用函数来实现

# def caculator(*args):
#     result = 1
#     for i in args:
#         result *= i
#     remainder = result % 20
#     return remainder
#
# num = input("请输入数字,以逗号分隔：")
# num_list=num.split(",")
# print(num_list)
# list_1 = []
# for i in num_list:
#     a = int(i)
#     list_1.append(a)
# print(caculator(*list_1))

# 8.编写如下程序
# 求列表所有元素的和
# a.one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
# b.使用while循环来实现

# one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
# result = 0
# i = 0
# while(i<len(one_list)):
#     result += one_list[i]
#     i += 1
# print(result)

# 9.编写如下程序
# 求圆的面积
# a.传入一个圆的半径，将其面积返回
# b.函数中的Π，可以导入import math，通过math.pi来获取（也可以直接使用3.14）
# import math
#
# def area(r):
#     area = math.pi*r*r
#     return area
#
# R = float(input("请输入圆的半径："))
# print(area(R))


# 11.编写如下程序（必做题第7题拓展）
# 将用户输入的所有数字相乘之后对20取余数
# a.用户输入的数字个数不确定
# b.用户可能使用关键字参数来传递待相乘的数字，例如：num1=21,num2=45等等
# b.请使用函数来实现

def caculator(*args, **kwargs):
    result_1 = 1
    result_2 = 1
    for i in args:
        result_1 *= i

    for m, n in kwargs.items():
        result_2 *= n

    result = result_1 * result_2
    return result % 20


num = input("请输入数字,以逗号分隔：")
num_list=num.split(",")

list_1 = []
dict_1 = {}
for i in range(len(num_list)):
    if "=" in num_list[i]:
        dict_2 = {}
        x, y = num_list[i].split("=")
        value = int(y)
        dict_2[x] = value
        dict_1.update(dict_2)
    elif "=" not in num_list[i]:
        a = int(num_list[i])
        list_1.append(a)
    else:
        print("数据不正确")

result = caculator(*list_1, **dict_1)
print(result)

