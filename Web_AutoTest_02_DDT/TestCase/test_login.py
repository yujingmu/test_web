#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:46
# @Author  : yimi
# @File    : test_login.py

import unittest
from selenium import webdriver
from login_page import LoginPage
from index_page import IndexPage
import public_data as public
import login_data as LD
import public_data as PD
from ddt import ddt,data,unpack
from selenium.webdriver.chrome.options import Options

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 设置无头浏览器
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # 登录
        self.driver = webdriver.Chrome(
            executable_path=(PD.driver_path),
            chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(public.login_url)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # 步骤
        self.login_page.login(LD.success_data["username"], LD.success_data["password"])
        # 验证-检查点
        # self.assertEqual(self.driver.current_url, "http://120.79.176.157:8012/Index/index")
        self.assertEqual(IndexPage(self.driver).get_nickName(), LD.success_data["check_nickname"])

    @data(*LD.no_data)
    def test_login_noData(self, data):
        self.login_page.login(data["username"], data["password"])
        self.assertEqual(self.login_page.no_data_error(), data["check"])
