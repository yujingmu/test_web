# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:08
# @Author  : yimi
# @File    : login_locator.py

from selenium.webdriver.common.by import By

class LoginLocator:
    username_locator = (By.NAME, "phone")
    password_locator = (By.NAME, "password")
    login_locator = (By.XPATH, "//button[@class='btn btn-special']")

    forget_passwd_locator = (By.XPATH, "//a[text()='忘记密码?']")
    register_locator = (By.XPATH, "//a[contains(text(), '免费注册')]")

    no_data_error_locator = (By.XPATH, "//div[@class='form-error-info']")

    username_or_passwd_error_locator = (By.NAME, "layui-layer-content")

