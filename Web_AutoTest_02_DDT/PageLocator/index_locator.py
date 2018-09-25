#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:14
# @Author  : yimi
# @File    : index_locator.py

class IndexLocator:
    # 登录成功后首页的用户名
    user_name_xpath = "//a[@href='/Member/index.html']"
    bid_xpath = "//div[@class='b-unit']//span[@class='fs-22']"
    bid_button_xpath = "//div[@class='b-unit']//a[text()='抢投标']"

