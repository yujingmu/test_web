# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 22:47
# @Author  : yimi
# @File    : homework_12.py
# 一、必做题
# 1.__str__的作用？

# def __str__(self):
#     return '<评论｛｝>'.format(self.id)

# 打印对象是会被调用
# 必须return字符串

# 2.is 与 == 的区别？
# is使用id查看内存地址，再判断地址是否一致, is为身份认证
# == 比较运算符， 判断值是否相等

# 3.类属性是什么？如何定义？在类外和类里如何调用？
# 类属性：给类定义的属性，是所有对象的公共特征
# 不会记录具体对象的特征
# 如何定义
# 在类的定义下方，使用类属性名=类属性值，这种形式来定义

# 类外
#   对象.类属性名
#   类.类属性名
#   类.类方法

# 类里
#   self.类属性名
#   类.类属性名
#   cls.类方法

# 4.类方法是什么？作用？如何定义？
# 针对类定义的方法
# 作用：修改，获取类属性
# 定义：
#   @classmethod
#   def 类方法名(cls):
#         pass

# 需要修饰器@classmethod
# 第一个参数应该是cls
# 在类方法类部， 可以使用cls访问类属性或调用方法

# 5.将类与对象相关内容，完成思维导图


# 6.编写如下程序

# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。

# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和
# 一个名为 open_restaurant()的方法（显示饭店正在营业）。

# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
# class Restaurant:
#
#     def __init__(self,restaurant_name,cooking_type):
#         self.restaurant_name = restaurant_name
#         self.cooking_type = cooking_type
#
#     def describe_restaurant(self):
#         print("*" * 50)
#         print("{:^50s}\n".format(self.restaurant_name))
#         for i in self.cooking_type:
#            print(i)
#         print("*" * 50)
#
#     def open_restaurant(self):
#         print("{}正在营业".format(self.restaurant_name))
#
# cooking = ['土豆丝', "地三鲜", "麻婆豆腐", "小龙虾"]
# Res = Restaurant("中餐厅",cooking)
# Res.describe_restaurant()
# Res.open_restaurant()

# 7.编写如下程序

# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。

# class Calculator:
#
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self):
#          return self.num1 + self.num2
#
#     def sub(self):
#         return self.num1 - self.num2
#
#     def mul(self):
#         return self.num1 * self.num2
#
#     def divide(self):
#         if self.num2 != 0:
#             print("两数相除为",self.num1 / self.num2)
#         else:
#             print("被除数不能为0，请重新输入被除数")
#
# Cal = Calculator(5, 1)
# print("两数相加为",Cal.add())
# print("两数相减为",Cal.sub())
# print("两数相乘为",Cal.mul())
# Cal.divide()


# 二、选作题
# 8.编写如下程序

# 编写一个工具箱类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。

class Tool:

    tool_count = 0

    def __init__(self, name, function, price):
        self.name = name
        self.function = function
        self.price = price  

    def add_tool(self):
        pass

    def remove_tool(self):
        pass

    def check_tool(self):
        pass

    @classmethod
    def get_tool_count(self):
        pass






