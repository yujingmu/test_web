#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:14
# @Author  : yimi
# @File    : login_locator.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginLocator:
    # user_put = (By.XPATH,"")
    # 元素定位
    # 用户名输入框
    user_input_xpath = "//input[@name='phone']"
    # 密码输入框
    passwd_input_xpath = "//input[@name='password']"
    # 登录按钮
    button_xpath = "//button"
    # 未输入用户名的弹出信息
    no_data_xpath = "//div[@class='form-error-info']"
    # 用户名或密码错误的弹出信息
    user_passwd_error_xpath = "//div[@class='layui-layer-content']"

