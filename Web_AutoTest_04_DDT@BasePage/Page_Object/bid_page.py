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
        name = "标详情页面获取的投标输入框"
        return self.wait_element_presence(self.bid_locator.bid_input, model=name)

    def enter_amount(self, money):
        name = "标详情页面输入投标金额"
        self.scroll_to_view(self.bid_locator.financing_bidding, model=name)
        element = self.get_bid_input
        element.send_keys(money)
        return element.get_attribute("data-amount")

    def submit_bid_button(self):
        name="标详情页面提交投标金额"
        return self.wait_element_presence(self.bid_locator.bid_button, model=name)

    @property
    def get_no_10_message(self):
        name="标详情页面输入不是10的整数倍金额，提交按钮提示相关信息"
        return self.wait_element_presence(self.bid_locator.no10_popup_msg, model=name)

    def click_bid_button(self):
        name="标详情页面点击提交按钮"
        self.wait_element_click(self.bid_locator.bid_button, model=name).click()

    @property
    def get_popup_info(self):
        name="标详情页面弹出投资成功提示"
        return self.wait_element_presence(self.bid_locator.bid_popup_locator, model=name)

    def active_bid(self):
        name="标详情页面投资成功，点击激活按钮"
        self.wait_element_click(self.bid_locator.bid_active_locator, model=name).click()

    # def get_element_finance_bidding(self):
    #     return self.wait_element_presence(self.bid_locator.financing_bidding)

