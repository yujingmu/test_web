#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:25
# @Author  : yimi
# @File    : login_page.py

# pageobject封装页面的元素定位，元素操作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from login_locator import LoginLocator

class LoginPage:
    # 元素定位, 可放在类里面函数上面
    def __init__(self, driver):
        self.driver = driver
        self.login_locator = LoginLocator()

    # 登录
    def login(self, user, passwd):
        login_locator = (By.XPATH, self.login_locator.user_input_xpath)
        WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(login_locator))
        self.driver.find_element_by_xpath(self.login_locator.user_input_xpath).send_keys(user)
        self.driver.find_element_by_xpath(self.login_locator.passwd_input_xpath).send_keys(passwd)
        self.driver.find_element_by_xpath(self.login_locator.button_xpath).click()

    def no_user_prompt(self):
        no_user_locator = (By.XPATH, self.login_locator.noser_prompt_xpath)
        WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(no_user_locator))
        return self.driver.find_element_by_xpath(self.login_locator.noser_prompt_xpath).text

    def user_passwd_error(self):
        passwd_error_locator = (By.XPATH, self.login_locator.user_passwd_error_xpath)
        WebDriverWait(self.driver, 30, 0.2).until(
            EC.visibility_of_all_elements_located(passwd_error_locator))
        return self.driver.find_element_by_xpath(self.login_locator.user_passwd_error_xpath).text

    # 注册
    def register(self):
        pass

    # 忘记密码
    def forget_passwd(self):
        pass


