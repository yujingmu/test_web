#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 22:56
# @Author  : yimi
# @File    : task_mouse_action_0903.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")

element = driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")
ActionChains(driver).move_to_element(element).click(element).perform()

from selenium.webdriver.support.ui import Select
driver.find_element_by_xpath("//a[text()='高级搜索']").click()
time.sleep(2)
object = driver.find_element_by_xpath("//select[@name='ft']")
# 初始化
select = Select(object)
time.sleep(2)

# 根据下标选值，下标从0开始
select.select_by_index(2)
time.sleep(2)
# 根据value属性选值
select.select_by_value("xls")
time.sleep(2)
# 根据文本内容选值
select.select_by_visible_text("RTF 文件 （.rtf)")

time.sleep(5)
driver.quit()
