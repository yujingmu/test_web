#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 19:31
# @Author  : yimi
# @File    : upload_file_0907.py

# 上传窗口 win32gui.FindWindow -> 子窗口（打开按钮） win32gui.FindWindowEx
# 上传窗口 win32gui.FindWindow -> 子窗口 ComboBoxEx32-> 子窗口 ComboBoxEx-> 子窗口 Edit

import win32gui
import win32con
import time

def upload_file(file_path):
    # 一级顶层窗口
    dialog = win32gui.FindWindow("#32770", "请选择文件/文件夹")
    # 二级窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # 二级窗口打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    # 三级窗口
    ComboBoxEx = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBoxEx', None)
    # 四级窗口--文件路径出入区域
    edit = win32gui.FindWindowEx(ComboBoxEx,0, 'Edit', None)
    # 1. 输入操作
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    time.sleep(2)
    # 2. 点击打开按钮
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1, button)
# 百度云盘自动上传文件
upload_file('C:\\D\\HTML\\Learning\\lesson1.html')

# ---------------------------------------------------------------
# 课堂派自动上传作业
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
# Chrome://version   个人资料路径
options.add_argument("--user-data-dir=C:\\Users\\yujing\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(options=options)
driver.get("")
driver.find_element_by_xpath("").click()
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR,""))
driver.find_element_by_css_selector("").click()
time.sleep(3)
upload_file("C:\\D\\HTML\\Learning\\lesson1.html")

