# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : home_page.py

from Page_Object.Base_Page import BasePage
from Page_Locator.home_locator import HomeLocator
from Test_Data import home_data
from selenium import webdriver

class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        # options = webdriver.ChromeOptions()
        # 浏览器中cache信息记录路径查询：chrome://version/
        # options.add_argument("--user-data-dir=C:\\Users\\yujing\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        # self.driver = webdriver.Chrome(options=options)
        self.home_locator = HomeLocator()

    # 无头浏览器
    # options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=C:\\Users\\yujing\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    # driver = webdriver.Chrome(options=options)
    # driver.get("url")


    def get_nickName(self):
        name="主页面获取昵称"
        return self.wait_element_presence(self.home_locator.nickname_locator, model=name).text

    def get_current_url(self):
        name="主页面获取URL"
        self.wait_element_visibility(self.home_locator.nickname_locator, model=name)
        return self.driver.current_url

    def click_bid(self):
        """选择并点击第一个标"""
        name="主页面点击第一个标"
        return self.wait_element_click(self.home_locator.changeable_bid1_locator, model=name).click()