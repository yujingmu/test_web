# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:58
# @Author  : yimi
# @File    : bid_page.py

from Base_Page import BasePage
from Page_Locator.bid_locator import BidLocator

class BidPage(BasePage):

    def __init__(self, driver):
        super(BidPage, self).__init__(driver)
        self.bid_locator = BidLocator()

    @property
    def get_bid_input(self):
        return self.wait_element_presence(self.bid_locator.bid_input)

    def enter_amount(self, money):
        self.scroll_to_view(self.bid_locator.financing_bidding)
        element = self.get_bid_input
        element.send_keys(money)
        return element.get_attribute("data-amount")

    def submit_bid_button(self):
        return self.wait_element_presence(self.bid_locator.bid_button)

    @property
    def get_no_10_message(self):
        return self.wait_element_presence(self.bid_locator.no10_popup_msg)

    def click_bid_button(self):
        self.wait_element_click(self.bid_locator.bid_button).click()


    @property
    def get_popup_info(self):
        return self.wait_element_presence(self.bid_locator.bid_popup_locator)

    def active_bid(self):
        self.wait_element_click(self.bid_locator.bid_active_locator).click()

    # def get_element_finance_bidding(self):
    #     return self.wait_element_presence(self.bid_locator.financing_bidding)

