# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 19:33
# @Author  : yimi
# @File    : web_homework_03_tecentclass.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element_click(driver, locator):
    wait = WebDriverWait(driver, 30)
    return wait.until(EC.element_to_be_clickable(locator))

browser = webdriver.Chrome()
browser.get("https://ke.qq.com/")
browser.maximize_window()

wait_element_click(browser, (By.XPATH, "//div[@id='js-mod-entry-index']//a[text()='登录']"))
submit_element = browser.find_element_by_xpath("//div[@id='js-mod-entry-index']//a[text()='登录']")
submit_element.click()

wait_element_click(browser, (By.CLASS_NAME, 'i-qq'))
qq_login = browser.find_element_by_class_name('i-qq')
qq_login.click()

WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
time.sleep(3)
wait_element_click(browser, (By.XPATH, '//a[text()="帐号密码登录"]'))
swither = browser.find_element_by_xpath('//a[text()="帐号密码登录"]')
swither.click()

wait_element_click(browser, (By.ID, "login_button"))
browser.find_element_by_id("u").send_keys("xxxxxxxx")
browser.find_element_by_id("p").send_keys("xxxxxxxx")
browser.find_element_by_id("login_button").click()

time.sleep(5)
browser.quit()