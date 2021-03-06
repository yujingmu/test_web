#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 22:53
# @Author  : yimi
# @File    : task_switch_windows_0903.py

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
ele = driver.find_element_by_xpath("//input[@id='kw']")
ele.send_keys("柠檬班")
driver.find_element_by_id('su').click()
# 等待元素出现
ele_locator = (By.XPATH, '//h3/a[contains(text(),"软件测试")]')
WebDriverWait(driver, 30, 1).until(EC.visibility_of_all_elements_located(ele_locator))
# 获取为操作之前的窗口数量
windows = driver.window_handles
# 点击操作 带来窗口数量的变化
driver.find_element_by_xpath('//h3/a[contains(text(),"软件测试")]').click()

WebDriverWait(driver,20).until(EC.new_window_is_opened(windows))
# # 重新获取一下窗口列表
windows = driver.window_handles
# 切换到最新的窗口
driver.switch_to.window(windows[-1])

windows = driver.window_handles
# 等到元素出现再切换
local_product = (By.XPATH,"//a[text()='知识分享']")
WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located(local_product))
driver.find_element_by_xpath("//a[text()='知识分享']").click()
time.sleep(2)
# 关闭‘知识分享’页面
driver.close()

time.sleep(10)
driver.quit()
