#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 17:37
# @Author  : yimi
# @File    : test_citrix_website.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https://ke.qq.com/')
# driver.find_element_by_xpath("//a[@class='h']").click()
# driver.find_element_by_id("J_Quick2Static").click()
#
# xpath_username = "//span[text()= '会员名/邮箱/手机号']"
# username_locator = (By.XPATH, xpath_username)
# username = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located(username_locator),message=u'元素加载超时!')
# username.send_keys("15250960734")
#
# password = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.ID,'TPL_password_1')),message=u'元素加载超时!')
# password.send_keys("123456")
# driver.find_element_by_id("J_SubmitStatic").click() #点击登录

# except NoSuchElementException as e:
#     print e.message