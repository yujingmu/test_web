#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 21:43
# @Author  : yimi
# @File    : homework_2.py

# 如果a = 15，b = 9，则a == b 、a != b 、a > b 、(a - 5) < b 、a >= b ** 2 、
# (a + 13 - 10 * 2) <= (b // 2 * 5 + 35 % 4)

a = 15
b = 9
print(a == b)       # False
print(a != b)       # True
print(a > b)        # True
print((a - 5) < b)      # False
print(a >= b ** 2)      # False
print((a + 13 - 10 * 2) <= (b // 2 * 5 + 35 % 4))       # True

# 3.定义字符串I'm Lemon, I love Python automated testing！
# 提示：使用双引号还是单引号呢？

print("I'm Lemon, I love Python automated testing！")

# 4.把website = 'http://www.python.org'中的python字符串取出来
# 提示：可以使用字符串切片

website = 'http://www.python.org'
print("顺序索引:", website[-10:-4])
print("倒序索引:", website[11:17])

# 5.将给定字符串前后的空格除去，把PHP替换为Python

best_language = "     PHP is the best programming language in the world!      "
print(best_language)
print(best_language.strip())
new_language = best_language.strip().replace("PHP", "Python")
print(new_language)

# # 6.演练字符串操作
my_hobby = "Never stop learning!"
# N e v e r  s t o p  l e a r n i n g !
# 截取从 2 ~ 6位置 的字符串
print("截取从 2 ~ 6位置 的字符串: ", my_hobby[1:6])
# 截取从 2 ~ 末尾的字符串
print("截取从 2 ~ 末尾的字符串: ", my_hobby[1:])
# 截取从 开始~ 6 位置 的字符串
print("截取从 开始~ 6 位置 的字符串: ", my_hobby[:6])
# 截取完整的字符串
print("截取完整的字符串: ", my_hobby[:])
# 从开始位置，每隔一个字符截取字符串
print("从开始位置，每隔一个字符截取字符串: ", my_hobby[::2])
# 从索引 3 开始，每隔2个取一个
print("从索引 3 开始，每隔2个取一个: ", my_hobby[3::3])
# 截取从 2 ~ 末尾-1的字符串
print("截取从 2 ~ 末尾-1的字符串: ", my_hobby[1:-1])
# 截取字符串末尾两个字符
print("截取字符串末尾两个字符: ", my_hobby[-3:-1])
# 字符串的逆序（拓展）
print("字符串的逆序: ", my_hobby[::-1])

# 7.去生鲜超市买橘子
# 收银员输入橘子的价格，单位：元／斤
# 收银员输入用户购买橘子的重量，单位：斤
# 计算并且 输出 付款金额
# 思考：如果输入的不是一个数字，执行程序会怎样？如何解决呢？
while(1):
    try:
        weight = float(input("请输入橘子的重量："))
        price = weight * 4.5
        print("应付款：", price)
        break
    except BaseException:
        print("输入数据类型不正确，请重新输入橘子的重量")


