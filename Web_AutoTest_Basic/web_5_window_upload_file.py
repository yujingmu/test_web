# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 15:03
# @Author  : yimi
# @File    : web_window_upload_file.py

import time
import win32con
import win32gui

# 上传文件
# PC端自动化使用模块 AutoIt
# 1. 如果是input可以直接输入路径，直接调用send_keys输入路径
# 2. 非input标签的上传，需要借助第三方工具（a. AutoIt   b. Python pywin32库）
# 工具安装 pywin32 spy++  windows控件

def upload_file(file_path):
#     一级顶层窗口---第二个参数Title会因为浏览器不同而不同
    dialog = win32gui.FindWindow("#32770", "打开")
#      二级窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)   # 0 表示遍历所有的后代
#       三级窗口
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
#       四级窗口
    edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)

#       二级窗口---打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button", None)
    time.sleep(2)
    # 输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    time.sleep(5)
    # 点击打卡按钮
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)







