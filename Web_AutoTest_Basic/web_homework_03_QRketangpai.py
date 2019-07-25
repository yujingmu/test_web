# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 19:36
# @Author  : yimi
# @File    : web_homework_03_QRketangpai.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element_click(driver, locator):
    wait = WebDriverWait(driver, 30)
    return wait.until(EC.element_to_be_clickable(locator))

browser = webdriver.Chrome()
browser.get("https://www.ketangpai.com")
browser.maximize_window()

wait_element_click(browser, (By.CLASS_NAME, "login"))
login = browser.find_element_by_class_name("login")
login.click()

wait_element_click(browser, (By.XPATH, '//a[text()="微信登录"]'))
wechat_login = browser.find_element_by_xpath('//a[text()="微信登录"]')
wechat_login.click()

time.sleep(3)
browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='login_container']/iframe"))

WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='qrcode lightBorder']")))
print(browser.find_element_by_xpath("//img[@class='qrcode lightBorder']").get_attribute("src"))

time.sleep(5)
browser.quit()