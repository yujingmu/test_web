#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 20:39
# @Author  : yimi
# @File    : bid_locator.py

class BidLocator:
    bid_balance_path = "//input[@data-url='/Invest/invest']"
    submit_bid_xpath = "//button[text()='投标']"
    popup_msg_success = "//div[text()='投标成功！']"
    check_active_xpath = "//div[@class='layui-layer-content']//button[text()='查看并激活']"
    no100_popup_msg = "//div[@class='text-center']"
    no10_popup_msg = "//button[@class='btn btn-special height_style']"