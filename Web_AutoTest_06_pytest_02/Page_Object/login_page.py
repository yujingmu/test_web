# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : login_page.py

from Page_Object.Base_Page import BasePage
from Page_Locator.login_locator import LoginLocator
from Page_Locator.bid_locator import BidLocator
from Test_Data import login_data


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.login_locator = LoginLocator()
        self.bid_locator = BidLocator()

    def get_element_username(self):
        name="登录页面获取用户名输入框"
        return self.wait_element_presence(self.login_locator.username_locator, model=name)

    @property
    def get_element_passwd(self):
        name="登录页面获取密码输入框"
        return self.wait_element_presence(self.login_locator.password_locator, model=name)

    @property
    def get_login_button(self):
        name="登录页面获取登录按钮"
        return self.wait_element_click(self.login_locator.login_button_locator, model=name)

    def login(self, user, passwd):
        name="登录页面等待登录按钮出现"
        self.driver.get(login_data.login_url)
        self.wait_element_click(self.login_locator.login_button_locator)
        self.get_element_username().send_keys(user)
        self.get_element_passwd.send_keys(passwd)   # 方法被@property 修饰可以作为属性，引用时不用加括号
        self.get_login_button.click()

        # self.driver.find_element_by_name("phone").send_keys(user)
        # self.driver.find_element_by_name("password").send_keys(passwd)
        # self.driver.find_element_by_name(self.login_locator.username_by_name).send_keys(user)
        # self.driver.find_element_by_name(self.login_locator.password_by_name).send_keys(passwd)

    def no_data_error(self):
        name="登录页面没有输入用户名或密码获取错误提示信息"
        element = self.wait_element_visibility(self.login_locator.no_data_error_locator, model=name)
        return element.text

    @property
    def get_element_username_or_passwd_error(self):
        name = "登录页面获取弹出的错误信息"
        return self.wait_element_quick_presence(self.login_locator.username_or_passwd_error_locator)
        # return self.driver.find_element(self.login_locator.username_or_passwd_error_locator)

    def registry(self):
        pass

    def forget_passwd(self):
        pass


