# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 21:05
# @Author  : yimi
# @File    : web_homework_02.py

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ketangpai.com/")

driver.maximize_window()

driver.find_element_by_class_name("login").click()
driver.find_element_by_xpath('//input[@name="account"]').send_keys("xxxxxx")
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("xxxxxxx")
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]/child::a[@class="btn-btn"]').click()
time.sleep(6)

print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)

driver.get("http://taobao.com")

driver.back()
time.sleep(4)

driver.forward()
time.sleep(4)

driver.refresh()

driver.close()
driver.quit()