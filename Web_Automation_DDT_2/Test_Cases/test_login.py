# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 21:32
# @Author  : yimi
# @File    : test_login.py

import unittest
from selenium import webdriver
from Test_Data import login_data
from ddt import ddt,data,unpack
from Page_Object.login_page import LoginPage
from Page_Object.home_page import HomePage
from Test_Data import home_data
from Test_Data import login_data


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def setUp(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    # def test_3_login_success(self):
    #     self.login_page.login(login_data.success_data["username"],login_data.success_data["password"])
    #     expect_result_1 = self.home_page.get_nickName()
    #     self.assertEqual(login_data.success_data["check_nickname"], expect_result_1)
    #     expect_result_2 = self.home_page.get_current_url()
    #     self.assertEqual(home_data.index_url, expect_result_2)

    # @data(*login_data.error_data)
    # def test_1_fail_login(self, date):
    #     self.login_page.login(date["username"], date["password"])
    #     self.assertEqual(self.login_page.no_data_error(), date["check"])

    @data(*login_data.username_passwd_mismatch)
    def test_2_username_passwd_mismatch(self, info):
        self.login_page.login(info[0], info[1])
        self.assertEqual(self.login_page.get_element_username_or_passwd_error.text,info[2])


    def tearDown(self):
        # self.login_page.get_element_username().clear()
        # self.login_page.get_element_passwd().clear()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

