#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 21:48
# @Author  : yimi
# @File    : login_data.py
from login_page import LoginPage

success_data = {"username":"18684720553", "password":"python", "check_nickname":"我的帐户[小蜜蜂96027]"}

# 没有填写用户名或密码的数据
# 同种类型的数据，使用相同的代码，可以使用
no_data = [{"username":" ", "password":"python", "check":"请输入手机号"},
           {"username":"18684720553", "password":"  ", "check":"请输入密码"}]