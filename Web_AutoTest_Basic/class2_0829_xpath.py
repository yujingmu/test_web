#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 20:49
# @Author  : yimi
# @File    : xpath.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://120.78.128.25:8765/")
time.sleep(10)

# 统一使用相对路径定位
# //标签名[@属性名=属性值]
driver.find_element_by_xpath("//meta[@name='phone' and @type='text']")
driver.find_element_by_xpath("//span[text()='请输入手机号码']")


time.sleep(100)
driver.quit()