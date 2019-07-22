# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : home_page.py

from selenium import webdriver
from Base_Page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Page_Locator.home_locator import HomeLocator
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_locator = HomeLocator()
        self.base_page = BasePage(self.driver)

    def get_nickName(self):

        nickname_locator = (By.XPATH, self.home_locator.user_name_xpath)
        self.base_page.wait_element_visibility(nickname_locator)
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.home_locator.user_name_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver.find_element_by_xpath(self.home_locator.user_name_xpath).text

    def get_current_url(self):
        nickname_locator = (By.XPATH, self.home_locator.user_name_xpath)
        self.base_page.wait_element_visibility(nickname_locator)
        return self.driver.current_url