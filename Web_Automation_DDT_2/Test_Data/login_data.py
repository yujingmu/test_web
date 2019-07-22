# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 21:22
# @Author  : yimi
# @File    : login_data.py

# from login_page import LoginPage
login_url = "http://120.78.128.25:8765/Index/login.html"

success_data = {"username":"18684720553", "password":"python", "check_nickname":"我的帐户[python10]"}

# 没有填写用户名或密码的数据
# 同种类型的数据，使用相同的代码，可以使用
error_data = [{"username":" ", "password":"python", "check":"请输入手机号"},
           {"username":"18684720553", "password":"  ", "check":"请输入密码"}]

username_passwd_mismatch = [("18684720553","adfafadsfafd","帐号或密码错误!"),
                            ("18684726574","python","此账号没有经过授权，请联系管理员!")]