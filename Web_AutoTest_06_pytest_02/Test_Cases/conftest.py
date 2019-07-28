# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 11:08
# @Author  : yimi
# @File    : conftest.py

import pytest
import logging
from selenium import webdriver
from Page_Object.login_page import LoginPage
from Page_Object.home_page import HomePage
from Page_Object.bid_page import BidPage
from Page_Object.user_page import UserPage
from Test_Data import login_data
from Common import Logger

# 定义pytest的fixture

# 定义一个函数，并在这个函数当中，实现用例的准备工作和清理工作
# 在函数的前面加上@pytest.fixture, fixture可以设置作用域范围
# fixture指定的class 为unittest的setUpClass，tearDownClass

@pytest.fixture()
def web_login():
    logging.info("***用例前置：初始化浏览器会话，登录前程贷系统***")
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(login_data.login_url)
    login_page = LoginPage(driver)
    bid_page = BidPage(driver)
    home_page = HomePage(driver)
    user_page = UserPage(driver)
    login_page.login(login_data.success_data["username"],login_data.success_data["password"])
    yield driver, login_page, bid_page, home_page, user_page
    logging.info("***用例后置：关闭浏览器会话***")
    driver.quit()

@pytest.fixture()
def web_init():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    yield driver, login_page, home_page
    driver.quit()
# @pytest.fixture()
