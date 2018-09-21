#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 21:32
# @Author  : yimi
# @File    : mouse_action.py
# 完整版
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")

element = driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")
# 方法一：
# element.click()
# 方法二：
# 能不用鼠标就不用鼠标
# 实例化ActionChains类
# 调用鼠标操作
# 调用perform()去执行所有的鼠标动作
ActionChains(driver).move_to_element(element).click(element).perform()
# 鼠标悬浮的下拉列表元素定位：ctrl + shift + c
# 等待
# WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(By.XPATH, "//a[text()='高级搜索']"))
# driver.find_element_by_xpath("//a[text()='高级搜索']").click()

# # -------------------------------------------------------------------------------------

# # select 元素处理
# # 引入select类
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
