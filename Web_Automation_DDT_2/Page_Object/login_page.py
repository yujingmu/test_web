# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : login_page.py

from Test_Data import login_data
from Base_Page import BasePage as BP
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Locator.login_locator import LoginLocator
from Base_Page import BasePage
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(login_data.login_url)
        self.login_locator = LoginLocator()
        self.base_page = BasePage(self.driver)

    def login(self, user, passwd):
        login_locator = (By.XPATH, self.login_locator.login_by_xpath)
        self.base_page.wait_element_click(login_locator)
        # self.driver.find_element_by_name("phone").send_keys(user)
        # self.driver.find_element_by_name("password").send_keys(passwd)
        self.get_element_username().send_keys(user)
        self.get_element_passwd().send_keys(passwd)
        # self.driver.find_element_by_name(self.login_locator.username_by_name).send_keys(user)
        # self.driver.find_element_by_name(self.login_locator.password_by_name).send_keys(passwd)
        self.driver.find_element_by_xpath(self.login_locator.login_by_xpath).click()

    def registry(self):
        pass

    def forget_passwd(self):
        pass

    def no_data_error(self):
        no_user_locator = (By.XPATH, self.login_locator.no_data_error_by_xpath)
        self.base_page.wait_element_visibility(no_user_locator)
        return self.driver.find_element_by_xpath(self.login_locator.no_data_error_by_xpath).text

    def get_element_username(self):
        return self.base_page.wait_element_presence((By.NAME, self.login_locator.username_by_name))

    def get_element_passwd(self):
        return self.base_page.wait_element_presence((By.NAME,self.login_locator.password_by_name))

    @property
    def get_element_username_or_passwd_error(self):
       self.base_page.wait_element_quick_presence((By.NAME, self.login_locator.username_or_passwd_error_by_name))
       # time.sleep(0.02)
       return self.driver.find_element_by_class_name(self.login_locator.username_or_passwd_error_by_name)