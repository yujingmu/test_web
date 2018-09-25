#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 21:07
# @Author  : yimi
# @File    : test_invest.py

# 用例分析 - 投资成功

# 前置： 登录成功  账户有余额--充值，查数据库，个人账号查看，事前手动准备金额
#   事先充钱
#   查数据库 -- 不够则充值     页面/接口充值
#
# 步骤：
# 1. 登录成功，进入首页
# 2. 选第一个标进行投资
# 3. 获取投资前的个人余额
# 4. 在投标详情页面，输入投资金额进行投标
# 5. 投标页面，弹出投资成功弹出框，点击查看并激活按钮
#
# 个人页面：
# 获取用户余额

# 验证：
# 1. 投资前获取一下，投资后在获取一下。 求差，等于投资金额
# 自动化测试独立账号
# 2.投资记录里失败
import time
import unittest
from selenium import webdriver
from bid_page import BidPage
from login_page import LoginPage
from index_page import IndexPage
from person_page import PersonPage
import public_data as PD
import invest_data as ID
from selenium.webdriver.chrome.options import Options

class TestInvest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # 登录
        self.driver = webdriver.Chrome(
            executable_path=(PD.driver_path),
            chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(PD.login_url)
        self.bid_page = BidPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.person_page = PersonPage(self.driver)
        self.login_page.login(PD.username, PD.password)

    def tearDown(self):
        self.driver.quit()

    def test_invest_success(self):
        # 进入个人详情页面，查看当前账户余额
        self.index_page.change_to_person_page()
        before_invest = self.person_page.get_balance()
        # 返回首页
        self.driver.back()
        time.sleep(5)
        # 首页选择一个标来进行投资
        self.index_page.click_firstbid()
        self.bid_page.input_invest_balance(ID.input_money)
        self.bid_page.click_submit_button()
    #     投资成功，读取提示信息
        self.assertEqual(self.bid_page.success_invest_msg(),ID.expect_success_invest_msg)
        # 投资成功，查看并激活
        self.bid_page.click_active_button()
    #     进入个人详情页面，读取投资后的个人账户余额
        # 刷新
        self.driver.refresh()
        time.sleep(2)
        after_invest = self.person_page.get_balance()
        self.assertEqual(int(float(before_invest)-float(after_invest)), ID.input_money)

    def test_invest_failed_by_No100(self):
        self.index_page.click_firstbid()
        self.bid_page.input_invest_balance(150)
        self.bid_page.click_submit_button()
        #     投资成功，读取提示信息
        self.assertEqual(self.bid_page.fail_invest_by_no100(), ID.expext_msg_by_no100)

    def test_invest_failed_by_No10(self):
        self.index_page.click_firstbid()
        self.bid_page.input_invest_balance(15)
        #     投资成功，读取提示信息
        self.assertEqual(self.bid_page.fail_invest_by_no10(), ID.expext_msg_by_no10)






















