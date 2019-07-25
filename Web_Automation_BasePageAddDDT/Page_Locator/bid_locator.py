# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:21
# @Author  : yimi
# @File    : bid_locator.py

from selenium.webdriver.common.by import By
# 标详情页面
class BidLocator:

    bid_input = (By.XPATH, "//input[@class= 'form-control invest-unit-investinput']")

    bid_button = (By.XPATH, "//button[@class='btn btn-special height_style']")

    no10_popup_msg = (By.XPATH, "//button[text()='请输入10的整数倍']")
    no100_popup_msg = (By.XPATH,"//div[@class='text-center']")

    financing_bidding = (By.XPATH, "//div[text()='融资投标']")

    bid_popup_locator = (By.CSS_SELECTOR, '.layui-layer-content .capital_font1')
    bid_active_locator = (By.CSS_SELECTOR, '.layui-layer-content .capital_btn>button')

    # bid_by_id = "15182"
    # submit_by_xpath = "//button[text()='投标']"
    # popup_msg_success = "//div[text()='投标成功！']"
    # check_active_xpath = "//div[@class='layui-layer-content']//button[text()='查看并激活']"




