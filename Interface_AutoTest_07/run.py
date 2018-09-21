#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 17:01
# @Author  : yimi
# @File    : run.py

# ****************************调用http_request_test模块*******************************
import unittest
import os
import HTMLTestRunnerNew
# from task_0810_database.common.excel_get_data import GetDataFromExcel
# from task_0810_database.common.read_config_data import ReadConfigDate
# from task_0810_database.common.http_request_testcase import HttpRequestTestCase
# from task_0810_database.config_file import read_path
#
# ip = ReadConfigDate(read_path.config_path,'IP', 'ip').read_config()
# print(ip)
# mode = ReadConfigDate(read_path.config_path, 'FLAG', 'mode').read_config()
# # print(mode)
# case_id_list = ReadConfigDate(read_path.config_path, 'FLAG', 'case_id').read_config()
# print(case_id_list)
# test_data = GetDataFromExcel(read_path.test_data_path , 'test_data', mode, case_id_list).get_data_from_excel()
# print(read_path.test_data_path)
# suit = unittest.TestSuite()
# for item in test_data:
#     suit.addTest(HttpRequestTestCase("test_api",ip+item['url'], eval(item['param']), item['method'], item['ExpectedResult'],item['case_id']))
# path = os.path.join(read_path.test_report_path,'result_api_test.html')
# with open(path,"wb+") as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title="api_test",tester="yimi")
#     runner.run(suit)



# ****************************调用function模块（DDT）*******************************
# （必须通过加载模块添加测试用例）

import unittest
import os
import time
import HTMLTestRunnerNew
from common.function import HttpRequestTestCase
from common.send_email import SendEmail
from task_0810_database.config_file import read_path

suit = unittest.TestSuite()
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(HttpRequestTestCase))
# now_time = time.strftime('%Y-%m-%d')
path = os.path.join(read_path.test_report_path, 'api_test_result_xx.html')
print(path)
with open(path, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='api_test_result_xx.html', tester="yimi")
    runner.run(suit)
#  发送测试报告
# subject = "薏米的测试报告"
# sender = '1281018605@qq.com'
# receiver = '281417558@qq.com'
# # receiver = '1255811581@qq.com'
# mail_text = 'api test result'
# html_path = os.path.join(read_path.test_report_path,'api_test_result.html')
# mail_attach = html_path
# auth_code = 'pxqswpbzogoohahb'
# SendEmail(subject, sender, receiver, mail_text, mail_attach, auth_code).send_email()



