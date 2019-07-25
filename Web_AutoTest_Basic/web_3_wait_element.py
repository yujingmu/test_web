# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 20:56
# @Author  : yimi
# @File    : web_wait.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("url")


# 等待操作
# 1. 强制等待
import time
time.sleep(5)

# 2.隐性等待
driver.implicitly_wait(30)

# 3. 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 元素等待
WebDriverWait(driver, 5, 0.3).until(EC.visibility_of_element_located((By.ID, " ")))

# iframe 等待
WebDriverWait(driver, 5, 0.3).until(EC.frame_to_be_available_and_switch_to_it("frame_name"))

# 新开窗口等待
WebDriverWait(driver, 5, 0.3).until(EC.new_window_is_opened(driver.window_handles))


# 窗口切换
# 窗口等待
WebDriverWait(driver, 5, 0.3).until(EC.new_window_is_opened(driver.window_handles))
#  获取当前窗口
windows = driver.window_handles            # 返回列表
#  切换到最新打开的窗口
driver.switch_to_window(driver.window_handles[-1])
driver.close()
print(driver.current_window_handle)

#   切回到原来的窗口
driver.switch_to_window(driver.window_handles[0])
#   获取当前窗口的句柄
driver.current_window_handle()



# iframe 切换（嵌套页面）
# iframe name
driver.switch_to_frame("frame_name")
# web对象
driver.switch_to_frame("WebElement")
# 索引
driver.switch_to_frame(1)
#  退出iframe，回到默认的页面
driver.switch_to_default_content()









