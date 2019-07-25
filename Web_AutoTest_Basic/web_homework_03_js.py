# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 21:25
# @Author  : yimi
# @File    : web_homework_03_js.py

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("C:\D\PycharmProjects\Review\python_base\web_homework_03_uploadfile.html")
driver.maximize_window()

element = driver.find_element_by_id("file")
js_code = "arguments[0].readOnly = false"
driver.execute_script(js_code, element)

time.sleep(3)
driver.quit()