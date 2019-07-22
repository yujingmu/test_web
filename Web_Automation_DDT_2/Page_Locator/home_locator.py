# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:21
# @Author  : yimi
# @File    : home_locator.py

from selenium.webdriver.common.by import By

class HomeLocator:
    # 登录成功后进入到主页， 主页的元素定位
    nickname_locator = (By.XPATH, "//a[@href='/Member/index.html']")

    bid1_locator = (By.XPATH, "//div[@class='b-unit'][1]//span[@class='fs-22']")
    bid2_locator = (By.XPATH, "//div[@class='b-unit'][2]//span[@class='fs-22']")
    bid3_locator = (By.XPATH, "//div[@class='b-unit'][3]//span[@class='fs-22']")

    bid_button1_xpath = (By.XPATH, "//div[@class='b-unit'][1]//a[text()='抢投标']")
    bid_button2_xpath = (By.XPATH, "//div[@class='b-unit'][2]//a[text()='抢投标']")
    bid_button3_xpath = (By.XPATH, "//div[@class='b-unit'][3]//a[text()='抢投标']")






