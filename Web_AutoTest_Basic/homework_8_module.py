# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 22:06
# @Author  : yimi
# @File    : homework_8_module.py

import math

def circle_area(r):
    circle_area = math.pi * (r ** 2)
    return circle_area

def circle_perimeter(r):
    circle_perimeter = 2 * math.pi * r
    return circle_perimeter

def rectangle_area(long, width):
    rectangle_area = long * width
    return rectangle_area

def rectangle_perimeter(long, width):
    rectangle_perimeter = 2 * (long + width)
    return rectangle_perimeter

if __name__ == "__main__":
    print(circle_area(4))
    print(circle_perimeter(4))
    print(rectangle_area(4, 2))
    print(rectangle_perimeter(4, 2))