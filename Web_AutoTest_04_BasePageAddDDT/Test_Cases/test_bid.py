# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 21:02
# @Author  : yimi
# @File    : test_bid.py

import unittest
from selenium import webdriver
from Page_Object.home_page import HomePage
from Page_Object.bid_page import BidPage
from Page_Object.login_page import LoginPage
from Page_Object.user_page import UserPage
from Page_Locator.bid_locator import BidLocator
from Test_Data import login_data, bid_data

class TestBid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.home_page = HomePage(cls.driver)
        cls.bid_page = BidPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.user_page = UserPage(cls.driver)
        cls.bid_locator = BidLocator()
        # cls.
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def test_1_bid_error(self):
        self.login_page.login(login_data.success_data["username"], login_data.success_data["password"])
        self.home_page.click_bid()
        # self.scrow_to_view(self.bid_locator.financing_bidding)
        self.bid_page.enter_amount(bid_data.error_data["investment_amount"])
        self.assertEqual(self.bid_page.get_no_10_message.text, bid_data.error_data["check"])

    def test_2_bid_sccess(self):
        old_balance = self.bid_page.enter_amount(bid_data.correct_data["investment_amount"])
        self.bid_page.click_bid_button()
        self.assertEqual(self.bid_page.get_popup_info.text, bid_data.correct_data["check"])
        self.bid_page.active_bid()
        new_balance = self.user_page.get_balance_amount()
        expected = int(float(old_balance) * 100) - int(float(bid_data.correct_data["investment_amount"]) * 100)
        actual = int(self.user_page.get_balance_amount()*100)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()


