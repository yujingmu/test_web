# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 21:02
# @Author  : yimi
# @File    : test_bid.py


import pytest
from Test_Data import login_data, bid_data

# conftest.py中fixture的使用
# 在测试用例/测试类前面加上
# @pytest.mark.usefixtures("fixture函数名")

# @pytest.mark.usefixture("web_login")
class TestBid():
    # pytestmark = [pytest.mark.success, pytest.mark.error, pytest.mark.smoke]
    # fixture修饰的函数的名称就是修饰函数的返回值
    def test_1_bid_error(self, web_login):
        driver, login_page, bid_page, home_page, user_page = web_login
        bid_page.enter_amount(bid_data.error_data["investment_amount"])
        assert bid_page.get_no_10_message.text == bid_data.error_data["check"]

    @pytest.mark.smoke
    def test_2_bid_sccess(self, web_login):
        driver, login_page, bid_page, home_page, user_page = web_login
        home_page.click_bid()
        old_balance = bid_page.enter_amount(bid_data.correct_data["investment_amount"])
        bid_page.click_bid_button()
        assert bid_page.get_popup_info.text == bid_data.correct_data["check"]
        bid_page.active_bid()
        new_balance = user_page.get_balance_amount()
        expected = int(float(old_balance) * 100) - int(float(bid_data.correct_data["investment_amount"]) * 100)
        actual = int(user_page.get_balance_amount()*100)
        assert expected == actual

if __name__ == "__main__":
    pytest.main()


