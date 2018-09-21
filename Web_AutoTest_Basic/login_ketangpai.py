#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 21:03
# @Author  : yimi
# @File    : login_ketangpai.py

from selenium import webdriver
import time
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
# 隐形等待（全局性质的） find.element都会使用到
driver.implicitly_wait(30)

driver.get('https://www.ketangpai.com/User/login.html')
driver.find_element_by_xpath("//a[text()='微信登录']").click()
# driver.switch_to_frame(1)
driver.find_element_by_class_name("wechatlogin-return").click()

# WebDriverWait(driver.)

# 回到最外层的html页面
# driver.switch_to_default_content()



# # 选择qq登录的方式
# driver.find_element_by_xpath("//a[contains(@class,'xxxx')]").click()
# time.sleep(20)

# 切换iframe
# driver.switch_to_frame("login_frame_qq")
# driver.switch_to_frame(driver.find_element_by_name("login_frame_qq"))
# driver.switch_to_frame(3)
# WebDriverWait(driver, )
# # 切换之后的操作，换一个html页面
# driver.find_element_by_id("switch_plogin").click()
#
# # 退出iframe的方法, 返回最初的页面
# driver.switch_to_default_content()

# ------------------------------------------------------------------------
# 百度
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# # 隐形等待
# driver.implicitly_wait(30)
# driver.get("http://www.baidu.com")









