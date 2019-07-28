# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 21:32
# @Author  : yimi
# @File    : test_login.py

from Test_Data import home_data
from Test_Data import login_data
import pytest

class TestLogin():

    # pytestmark = [pytest.mark.success, pytest.mark.error, pytest.mark.smoke]

    @pytest.mark.parametrize("date", login_data.error_data)
    def test_1_fail_login(self, date, web_init):
        driver, login_page, home_page = web_init
        login_page.login(date["username"], date["password"])
        assert login_page.no_data_error() == date["check"]

    @pytest.mark.parametrize("info", login_data.username_passwd_mismatch)
    def test_2_username_passwd_mismatch(self, info, web_init):
        driver, login_page, home_page = web_init
        login_page.login(info[0], info[1])
        assert login_page.get_element_username_or_passwd_error.text == info[2]

    @pytest.mark.smoke
    def test_3_login_success(self, web_init):
        driver, login_page, home_page = web_init
        login_page.login(login_data.success_data["username"],login_data.success_data["password"])
        expect_result_1 = home_page.get_nickName()
        assert login_data.success_data["check_nickname"] == expect_result_1
        expect_result_2 = home_page.get_current_url()
        assert home_data.index_url == expect_result_2


if __name__ == "__main__":
    pytest.main()

