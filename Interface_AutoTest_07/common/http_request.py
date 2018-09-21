#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 16:30
# @Author  : yimi
# @File    : http_request.py
import requests
from api_log import LogDisplay
# from common.function import HttpRequestTestCase
COOKIES = None
logger = LogDisplay('API_Test_Logger', 'DEBUG', 'DEBUG')

class HttpRequest:
    def __init__(self, url, param, method):
        self.url = url
        self.param = param
        self.method = method

    def http_request(self):
        global COOKIES
        if self.method.upper() == "GET":
            logger.info("使用get方法")
            try:
                res = requests.get(self.url, params=self.param, cookies=COOKIES)
            except Exception as e:
                logger.error("get请求错误：{0}".format(e))
                raise e
        elif self.method.upper() == "POST":
            try:
                res = requests.post(self.url, params=self.param, cookies=COOKIES)
            except Exception as e:
                logger.error("post请求错误：{0}".format(e))
                raise e
        else:
            logger.error("请求方法不正确！")
        if  res.cookies != {}:
            COOKIES = res.cookies
        return res.json()

if __name__ == "__main__":
    register = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
    register_data = {'mobilephone':'18093192866','pwd':'123456','regname':'tester1'}
    login = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone':'13548773642','pwd':'123456'}
    recharge = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    recharge_data = {"mobilephone": "13548773642", "amount": "100"}
    res_login = HttpRequest(login, login_data, 'get').http_request()
    res_register = HttpRequest(register, register_data, 'post').http_request()
    res_recharge = HttpRequest(recharge, recharge_data, 'post').http_request()
    print(res_login)
    print(res_register)
    print(res_recharge)