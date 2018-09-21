#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 16:53
# @Author  : yimi
# @File    : http_request_testcase.py

import unittest
from task_0810_database.common.http_request import HttpRequest
from task_0810_database.common.read_config_data import ReadConfigDate
from task_0810_database.common.excel_get_data import GetDataFromExcel
from task_0810_database.config_file import read_path
from task_0810_database.common.api_log import LogDisplay

logger = LogDisplay('API_Test_Logger', 'DEBUG', 'DEBUG')
mode = ReadConfigDate(read_path.config_path, 'FLAG', 'mode').read_config()
# print(mode)
case_id_list= ReadConfigDate(read_path.config_path, 'FLAG', 'case_id').read_config()
# print(case_id_list)
class HttpRequestTestCase(unittest.TestCase):
    def __init__(self, methodName, url, params, method, expected, case_id):
        super(HttpRequestTestCase, self).__init__(methodName)
        self.url = url
        self.params = params
        self.method = method
        self.expected = expected
        self.case_id = case_id

    def setUp(self):       #初始化工作
        self.object = HttpRequest(self.url, self.params, self.method)     #创建一个实例
        self.save = GetDataFromExcel(read_path.test_data_path, 'test_data', mode, case_id_list)

    def test_api(self):
        res = self.object.http_request()
        self.save.write_data(self.case_id+1, 9, str(res))
        try:
            self.assertEqual(self.expected, str(res))
            test_result = "Pass"
        except AssertionError as e:
            logger.error("执行用例时报错：{0}".format(e))
            test_result = "Fail"
            raise e
        finally:
            self.save.write_data(self.case_id+1, 10, test_result)

    def tearDown(self):
        pass