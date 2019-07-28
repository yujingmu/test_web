# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 22:22
# @Author  : yimi
# @File    : user_page.py


from Page_Object.Base_Page import BasePage
from Page_Locator.user_locator import UserLoctor

class UserPage(BasePage):

    def __init__(self, driver):
        super(UserPage, self).__init__(driver)
        self.user_locator = UserLoctor
        # self.login_locator = LoginLocator()

    def get_element_balance(self):
        name = "用户个人页面定位用户余额的元素"
        return self.wait_element_presence(self.user_locator.balance_locator, model=name)

    def get_balance_amount(self):
        name="用户个人页面获取用户余额"
        balance_str = self.get_element_balance().text
        balance = balance_str[0:-1]
        return float(balance)

