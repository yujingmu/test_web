#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 23:01
# @Author  : yimi
# @File    : task_alert_file_0903.py

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(r'D:\python linmen\auto_test\class\web/basic_task.html')

username_locator = (By.XPATH, "//input[@id='uname']")
username = WebDriverWait(driver,timeout=10).until(EC.visibility_of_all_elements_located(username_locator),message=u'元素加载超时!')[0]
username.send_keys("15250560734")
password = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.ID,'passwd')),message=u'元素加载超时!')
password.send_keys("123456")

object = driver.find_element_by_xpath("//select[@name='select']")
object_city = driver.find_element_by_xpath("//select[@name='city']")
# 初始化
select = Select(object)
select_city = Select(object_city)
time.sleep(2)

# 根据下标选值，下标从0开始
select.select_by_index(2)
time.sleep(1)
select_city.select_by_index(2)
time.sleep(1)
# 根据value属性选值
select.select_by_value("ShanXi")
time.sleep(1)
select_city.select_by_value("Xi'an")
time.sleep(1)
# 根据文本内容选值
select.select_by_visible_text("JiangSu")
time.sleep(1)
select_city.select_by_visible_text("NanJing")
time.sleep(1)

# 标签名为input， 调用send_keys('图片路径')实现文件上传
driver.find_element_by_id('photo').send_keys('D:\Desktop\Citrix.png')

driver.find_element_by_id("login").click()

WebDriverWait(driver, 20).until(EC.alert_is_present())

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
print(alert.text)
time.sleep(2)
alert.accept()
print(alert.text)
time.sleep(2)
alert.accept()

time.sleep(5)
driver.quit()