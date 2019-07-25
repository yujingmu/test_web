# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 19:43
# @Author  : yimi
# @File    : web_homework_03_upload.py

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('C:\D\PycharmProjects\Review\python_base\web_homework_03_uploadfile.html')
driver.maximize_window()
# 方法一：
# driver.find_element_by_id("file").send_keys("C:\\Users\yujing\Downloads\get_excel_data.py")
# time.sleep(5)
# driver.quit()
# 方法二：
import web_5_window_upload_file
driver.find_element_by_id("file").click()
time.sleep(2)
web_5_window_upload_file.upload_file("C:\\Users\\yujing\\Downloads\\get_excel_data.py")
time.sleep(5)
driver.quit()


