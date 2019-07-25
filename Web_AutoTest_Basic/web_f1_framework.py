# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 17:50
# @Author  : yimi
# @File    : web_f1_framework.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_element_click(driver, locator):
    element = WebDriverWait(driver, 30, 0.2)
    return element.until(EC.element_to_be_clickable(locator))

driver = webdriver.Chrome()
driver.get("http://120.78.128.25:8765/")
driver.maximize_window()

wait_element_click(driver,(By.XPATH, "//a[text()='登录']"))
driver.find_element_by_xpath("//a[text()='登录']").click()
wait_element_click(driver,(By.XPATH, "//button[text()='登录']"))
driver.find_element_by_name("phone").send_keys("18684720553")
driver.find_element_by_name("password").send_keys("python")
driver.find_element_by_xpath("//button[text()='登录']")
time.sleep(5)


driver.quit()



