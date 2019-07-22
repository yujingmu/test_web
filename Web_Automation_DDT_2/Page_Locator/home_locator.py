# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:21
# @Author  : yimi
# @File    : home_locator.py

from selenium.webdriver.common.by import By

class HomeLocator:
    user_name_locator = (By.XPATH, "//a[@href='/Member/index.html']")
    first_bid_locator = (By.XPATH, "//div[@class='b-unit'][1]//span[@class='fs-22']")
    second_bid_locator = (By.XPATH, "//div[@class='b-unit'][2]//span[@class='fs-22']")
    third_bid_locator = (By.XPATH, "//div[@class='b-unit'][3]//span[@class='fs-22']")
    


