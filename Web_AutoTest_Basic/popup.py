#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 20:42
# @Author  : yimi
# @File    : popup.py

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
# 点击登录按钮
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# 弹出框处理
# 1.触发  2.等待元素可见  3.再处理
local_username = (By.ID, "TANGRAM__PSP_10__footerULoginBtn")
WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located(local_username))
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()

time.sleep(10)
driver.quit()


