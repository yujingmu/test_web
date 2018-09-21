#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 21:21
# @Author  : yimi
# @File    : keyboard_0905.py

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
ele = driver.find_element_by_id('kw').send_keys("柠檬班", Keys.ENTER)
ele_local = (By.XPATH,"//div[@id='page']//span[text()=4]")
WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(ele_local))
element = driver.find_element_by_xpath("//div[@id='page']//span[text()=4]")
# 滚动条处理 — js代码 —
driver.execute_script("arguments[0].scrollIntoView()", element)
# 底部对齐
# driver.execute_script("arguments[0].scrollIntoView(false)", element)
time.sleep(2)
element.click()








