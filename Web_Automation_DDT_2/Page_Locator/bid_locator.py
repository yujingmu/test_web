# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:21
# @Author  : yimi
# @File    : bid_locator.py

from selenium.webdriver.common.by import By

class BidLocator:

    bid_locator = (By.ID, "15182")
    submit_locator = (By.XPATH, "//button[text()='投标']")
    popup_msg_success_locator = (By.XPATH, "//div[text()='投标成功！']")
    check_active_locator = (By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']")

    no100_popup_msg_locator = (By.XPATH, "//div[@class='text-center']")
    no10_popup_msg_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")


