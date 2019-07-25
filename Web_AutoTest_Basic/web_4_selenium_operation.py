# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 21:33
# @Author  : yimi
# @File    : web_selenium_operation.py

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# 浏览器中cache信息记录路径查询：chrome://version/
options.add_argument("--user-data-dir=C:\\Users\\yujing\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(options=options)
driver.get("url")


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("url")

# 等待alert框出现
alert = WebDriverWait(driver, 30, 0.2).until(EC.alert_is_present())   # alert_is_present() 已经切换到了alert
# alert = driver.switch_to_alert()
print(alert.text)
time.sleep(2)
alert.accept()


# 定位select,点击select，定位option,点击option
# 下拉列表
from selenium.webdriver.support.ui import Select

sele = driver.find_element_by_xpath("select_property ")
# 初始化
select_obj = Select(sele)
# 根据下标选值
select_obj.select_by_index(2)
# 根据value属性选值
select_obj.select_by_value(" ")

# 根据文本内容选取
select_obj.select_by_visible_text(" ")



# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).move_to_element("webelement").click("element").perform()
ActionChains(driver).move_to_element("webelement").double_click("element").perform()
ActionChains(driver).drag_and_drop(" ", "  ").perform()
ActionChains(driver).context_click("  ").perform()
# 鼠标悬浮下拉列表元素定位： CTRL+Shift+C



# 键盘
from selenium.webdriver.common.keys import Keys

driver.find_element_by_id(" ").send_keys(Keys.ENTER)
driver.find_element_by_id(" ").send_keys(Keys.CONTROL, "a")       # 组合键 ctrl+a


#js处理滚动条
element = driver.find_element_by_name(" ")
# 窗口拖动到可视范围
# element.location_once_scrolled_into_view
driver.execute_script("arguments[0].scrollIntoView();", element)   # 默认与当前窗口顶部对齐
time.sleep(2)
element.click()

driver.execute_script("arguments[0].scrollIntoView(false);", element)   # 与当前窗口底部对齐
driver.execute_script("window.scrollInto(0,document.body.scrollHeight)")    # 滚动条移动到页面底部
driver.execute_script("window.scrollInto(document.body.scrollHeight)，0")   # 滚动条移动到页面顶部


element = driver.find_element_by_name("   ")
element.get_attribute("value")
#  set attribute需要使用JS实现
js_code = "arguments[0].readOnly = false"
driver.execute_script(js_code, element )
element.clear()
element.send_keys(" ")

# 第二种方式(不推荐)
js_code = "var element = document.getElementByID(' '); element.readonly=false; e.value='2019-01-02'"
driver.execute_script(js_code)



