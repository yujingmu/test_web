#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 22:04
# @Author  : yimi
# @File    : data_0905.py

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://kyfw.12306.cn/otn/leftTicket/")
time.sleep(3)
# 输入出发地
driver.find_element_by_id("fromStationText").send_keys("南京",Keys.ENTER)   # Keys.ENTER 优先选择下拉列表中的第一个
# 输入目的地
driver.find_element_by_id("toStationText").send_keys("西安",Keys.ENTER)
js_pha = "var ele = document.getElementById('train_date'); ele.removeAttribute('readOnly');ele.value = '2018-09-21';"
# 执行js语句
driver.execute_script(js_pha)
time.sleep(3)
# 点击查询
driver.find_element_by_id("a_search_ticket").click()

time.sleep(100)
driver.quit()
