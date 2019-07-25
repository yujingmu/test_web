# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 22:22
# @Author  : yimi
# @File    : user_page.py

import os
from Base_Page import BasePage
from Page_Locator.user_locator import UserLoctor
from Page_Locator.user_locator import UserLoctor
# from Test_Data import login_data

class UserPage(BasePage):

    def __init__(self, driver):
        super(UserPage, self).__init__(driver)
        self.user_locator = UserLoctor
        # self.login_locator = LoginLocator()

    def get_element_balance(self):
        return self.wait_element_presence(self.user_locator.balance_locator)

    def get_balance_amount(self):
        balance_str = self.get_element_balance().text
        return float(balance_str)

