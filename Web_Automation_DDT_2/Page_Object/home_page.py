# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : home_page.py

from Base_Page import BasePage
from Page_Locator.home_locator import HomeLocator

class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.home_locator = HomeLocator()

    def get_nickName(self):
        # self.wait_element_visibility(self.home_locator.nickname_locator)
        # 滚动到视野可见区域
        # element = self.driver.find_element(self.home_locator.nickname_locator)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.wait_element_presence(self.home_locator.nickname_locator).text

    def get_current_url(self):
        self.wait_element_visibility(self.home_locator.nickname_locator)
        return self.driver.current_url