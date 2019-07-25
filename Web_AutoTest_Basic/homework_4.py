#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:15
# @Author  : yimi
# @File    : homework_4.py
# 1.定义两个字典用于表述你的个人信息
# 第一个字典存放你的这些信息：姓名、性别、年龄、身高
# 第二个字典存放你的其他信息：性格、爱好、座右铭
#     a.将两个字典合并为第三个字典之后，打印出来
#     b.觉得自己很年轻的，可以去整个容（修改年龄），然后露个脸（打印出来）
#     c.对你的座右铭很感兴趣，请将其取出来
#     d.如果你觉得自己精力充沛，又好折腾，可以尝试一下，字典支持序列类型的哪些操作？

dict_1 = {"name":"yimi", "gender":"female", "age": 26, "height":158}
dict_2 = dict({"Nature":"活泼", "hobby": "code", "motto":"生命不息，运动不止"})
dict_1.update(dict_2)
dict_3 = dict_1
print(dict_3)
dict_3["age"] = 18
print(dict_3)
print(dict_3["motto"])
print(dict_3.keys())
print(dict_3.values())
print(dict_3.items())


# 2.请写出if判断语句的格式
a = 4
b = 10
if a == 4:
    print("a=4")
    if b == 10:
        print("b=10")
    else:
        print("b！=10")
else:
    print("a!=4")


# 3.求三个整数中的最大值
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
num3 = float(input("请输入第三个数:"))
print("最大的数为：{}".format(max(num1, num2, num3)))

# 4.判断是否为闰年
# 输入一个有效的年份（如：2019），判断是否为闰年
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”

# 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）；
# 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）；

year = int(input("请输入一个年份："))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("{}年是闰年".format(year))
else:
    print("{}不是闰年".format(year))


# 5.分别使用for和while打印九九乘法表
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
i = 1
while(i<9):
    j = 1
    while(j<i+1):
        print("{} * {} = {}".format(i, j, i*j), end="\t")
        if i == j:
            print("\n")
        j += 1
    i += 1


for i in range(1, 10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(i, j, i*j), end="\t")
        if(j==i):
            print("\n")

#
# 7.使用if语句完成剪刀石头布游戏
# 提示：
# 提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 电脑随机出拳
# 比较胜负，显示用户胜、负还是平局
# 电脑随机出拳
# 使用随机数，首先需要导入随机数的模块 —— “工具包”
# import random
# 导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
# random.randint(a, b)，返回[a, b]之间的整数，包含a和b
# random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
# random.randint(4, 4)  # 结果永远是 4
# random.randint(25, 12)  # 该语句是错误的，下限必须小于上限

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

# 8.使用循环实现经典冒泡算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（小的数字排前面，大的排后面），
# 不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

