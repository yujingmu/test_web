# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 20:45
# @Author  : yimi
# @File    : homework_11_class.py


# 一、必做题
# 1.什么是类？什么是对象？
# 类是对一群具有相同特征或行为的事物的一个总称，不能直接使用

# 2.类由哪几部分构成？
# 类名, 属性， 方法

# 3.类的设计原则
# 请从类的命名、类中属性和方法来阐述
# 类名：大驼峰命名法
#类函数可调用同一个类里面的其他函数， self.函数名

# 4.类中实例方法的特性？__init__方法的作用？
# 初始化函数

# 5.列举几个生活中类和对象的例子
# 类是图纸，对象是房子
# 类是模型， 对象是产品

# 6.编写如下程序
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{0}岁的{1}吃着美味的食物".format(self.age, self.name))

    def drink(self):
        print("{0}岁的{1}喝着可口的饮料".format(self.age, self.name))

    def joy(self):
        print("很享受")

tom = Cat("Tom", 1)
tom.eat()
tom.drink()
tom.joy()





