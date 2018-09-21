#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 22:11
# @Author  : yimi
# @File    : open_special_website.py

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
# ele = driver.find_element_by_id('kw')
ele = driver.find_element_by_xpath("//input[@id='kw']")
ele.send_keys("柠檬班")
driver.find_element_by_id('su').click()
# 等待元素出现
xpath_ele = '//h3/a[contains(text(),"软件测试")]'
ele_locator = (By.XPATH, xpath_ele)
WebDriverWait(driver, 30, 1).until(EC.visibility_of_all_elements_located(ele_locator))
driver.find_element_by_xpath(xpath_ele).click()

time.sleep(100)
driver.quit()

