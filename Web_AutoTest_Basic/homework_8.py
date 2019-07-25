# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 22:15
# @Author  : yimi
# @File    : homework_8.py
# 1.什么是模块？有什么作用？
# 把相关的代码分配到一个模块里能让代码更好用，更易懂。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。

# 2.模块中的哪些资源可以被调用处使用？
# 函数，变量

# 3.模块的命名规范
# 以数字，字母，下划线构成
# 不能以数字开头
# 不要以下划线开头
# 不要与关键字重名
# 不要与系统内置的模块，函数重名
# 不建议使用中文

# 4.模块的导入方式有哪几种？
# import 模块名
# import 模块名 as 模块重命名
# from 模块名 import *
# __all__ = ["模块名"]
# from 包名.模块名 import 类名/函数名

# 5. __name__属性的特性？
# 每个python文件运行都有
# 直接运行py文件，__name__ == "__main__"
# 导入python文件，__name__ == "路径.模块名"

# 6.os模块中有哪些常用的方法？用什么作用？
# os.getcwd()               获取当前的工作路径
# os.path.join(a，b)        连接两个部分路径，组成一个完整路径
# os.mkdir(路径名)          某个目录下创建一个新目录
# os.mkdirs(路径名)         创建多层目录
# os.rmdir(路径名)          删除一个目录
# os.rmdirs(路径名)         删除多层目录
# os.listdir()              获取当前路径下的目录列表
# os.path.isdir(文件路径)   判断当前路径是否是目录
# os.path.isfile(文件名)    判断当前文件是否是文件

# 7.编写如下程序
# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# b.每个模块中需要添加测试代码
# import python_base.homework_8_module as area_rectangle
#
# print(area_rectangle.circle_area(4))
# print(area_rectangle.circle_perimeter(4))
# print(area_rectangle.rectangle_area(4, 2))
# print(area_rectangle.rectangle_perimeter(4, 2))

# 9.编写如下程序
# 裴伯拉切数列，从第三个元素开始，
# 每个元素为前两个元素之和，用户输入某个大于0的正整数，
# 求出小于等于这个正整数的所有裴伯拉切元素
# a.裴伯拉切数列为：0  1  1  2  3  5  8  13  21  34  55  89  144  ...
# b.例如，用户输入50，那么小于等于50的裴伯拉切元素为：0  1  1  2  3  5  8  13  21  34
# c.要求在一个模块中定义，在另一个程序中调用
# F(n+2) = F(n+1)+ F(n)
# n= 0
# F(0) = 0
# F(1) = 1