#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:46
# @Author  : yimi
# @File    : test_login.py

import unittest
from selenium import webdriver
from login_page import LoginPage
from index_page import IndexPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://120.79.176.157:8012/Index/login.html")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # 步骤
        self.login_page.login("18684720553", "python")
        # 验证-检查点
        # self.assertEqual(self.driver.current_url, "http://120.79.176.157:8012/Index/index")
        self.assertEqual(IndexPage(self.driver).get_nickName(), "我的帐户[小蜜蜂96027]")

    def test_login_noUser(self):
        self.login_page.login("     ", "python")
        self.assertEqual(self.login_page.no_user_prompt(), '请输入手机号')

    def test_login_wrongPasswd(self):
        self.login_page.login("18684720553", "python1234")
        self.assertEqual(self.login_page.user_passwd_error(), "帐号或密码错误!")
