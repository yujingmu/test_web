#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 21:34
# @Author  : yimi
# @File    : class1_0827.py
from selenium import webdriver
import time
# -------------------窗口相关操作--------------------
# 通过webdriver打开Chrome浏览器
driver = webdriver.Chrome()
# 全屏操作
driver.maximize_window()

driver.implicitly_wait(30)

# 设置窗口大小
# driver.set_window_size(800, 600)
# 访问一个网页
driver.get("http://www.baidu.com")
time.sleep(10)
driver.get("http://www.taobao.com")
time.sleep(10)

# 获取页面标题，url,窗口句柄
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)

# 在Chrome历史记录中回到上一个页面
driver.back()
time.sleep(5)
# 刷新
driver.refresh()
time.sleep(2)
# 在Chrome历史记录中回到下一个页面
# driver.forward()
# time.sleep(5)

#关闭当前窗口
# time.sleep(10)
# driver.close()

# 关闭chrome及Chromedriver
time.sleep(10)
driver.quit()

# --------------------查找页面元素---------------------
# F12 --> Elements

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# 1根据id
# driver.find_element_by_id("id")
ele_id= driver.find_element_by_id("kw")

# 2 根据name属性
# ele = driver.find_element_by_name("name")
ele_name = driver.find_element_by_name('wd')
# 找多个元素---列表
# ele_name = driver.find_elements_by_name('wd')
print(ele_name.tag_name)
print(ele_name.text)

# 3 根据class 属性 - 参数只能是一个参数值
ele_class = driver.find_element_by_class_name('wd')

# 4 根据标签名
ele_mark = driver.find_element_by_tag_name('wd')

# 5 根据链接  -a
ele_link_all = driver.find_element_by_link_text("新闻")
ele_link_part = driver.find_element_by_partial_link_text("产品")

print(ele_link_part.tag_name)
print(ele_link_part.text)

# 标签名为input的输入操作
ele_id.seng_keys("柠檬班")

time.sleep(10)
driver.quit()

