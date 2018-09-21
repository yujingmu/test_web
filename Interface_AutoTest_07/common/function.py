#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 16:24
# @Author  : yimi
# @File    : ddt.py
import unittest
from ddt import ddt,data,unpack
from common.http_request import HttpRequest
from common.excel_get_data import GetDataFromExcel
from common.read_config_data import ReadConfigDate
from common.api_log import LogDisplay
from task_0810_database.config_file import read_path
from common.mysql_get_data import MySQLGetData

# 测试数据：
ip = ReadConfigDate(read_path.config_path,'IP', 'ip').read_config()
mode = ReadConfigDate(read_path.config_path, 'FLAG', 'mode').read_config()
case_id_list = ReadConfigDate(read_path.config_path, 'FLAG', 'case_id').read_config()
test_data = GetDataFromExcel(read_path.test_data_path, 'test_data', mode, case_id_list).get_data_from_excel()
# data_base = ReadConfigDate(read_path.config_path, 'DB', 'config').read_config()
# print(data_base)
logger = LogDisplay('API_Test_Logger', 'DEBUG', 'DEBUG')

# COOKIES = None
REGTIME = None
MEMBER_ID = None

# 写测试类
@ddt    # 装饰测试类，必须是继承unittest.TestCase的测试类
class HttpRequestTestCase(unittest.TestCase):
    def setUp(self):       #初始化工作
        logger.info("开始测试")
        self.save = GetDataFromExcel(read_path.test_data_path, 'test_data', mode, case_id_list)

    @data(*test_data)   #装饰测试方法,解析传递进来的测试数据
    def test_api(self, item):
        # global COOKIES
        global REGTIME
        global MEMBER_ID
        res = HttpRequest(ip+item['url'], eval(item['param']), item['method']).http_request()
        # 每次请求之后判断是否产生cookies, 如果产生就替换全局变量，如果不产生，就不替换
        # if  res.cookies != {}:
        #     COOKIES = res.cookies
        self.save.write_data(item['case_id']+1, 9, str(res))
        # 每次请求之后查询一次数据库   对全局变量进行替换
        # 替换regtime
        if REGTIME == None:
            query = "select regtime from member where mobilephone=%s"
            query_condition = eval(item['param'])['mobilephone']
            result = MySQLGetData().mysql_get_data(query, (query_condition,), 1)
            if result != None :
                REGTIME = str(result[0])+'.0'
        # 替换member_id
        if MEMBER_ID == None:
            query = "select id from member where mobilephone=%s"
            query_condition = eval(item['param'])['mobilephone']
            result = MySQLGetData().mysql_get_data(query, (query_condition,), 1)
            if result != None:
                MEMBER_ID = str(result[0])

        # 判断期望结果里面是否有这些字段
        if item['ExpectedResult'].find('${regtime}') != -1:
            new_param_str = item['ExpectedResult'].replace('${regtime}', REGTIME)
            if new_param_str.find('${member_id}') != -1:
                new_param = eval(new_param_str)
                #new_param = new_param.replace('${member_id}', MEMBER_ID)
                new_param["data"]["id"]= int(MEMBER_ID)
                new_param = str(new_param)
                if new_param_str.find('${no_reg_tel}') != -1:
                    new_param = new_param.replace('${no_reg_tel}', str(eval(item['param'])['mobilephone']))
        else:
            new_param = item['ExpectedResult']

        if item['CheckSQL'] != None:
            if item['CheckSQL'].find('${no_reg_tel}') != -1:
                sql_param = item['CheckSQL'].replace('${no_reg_tel}',str(eval(item['param'])['mobilephone']))
                query = eval(sql_param)['query']
                query_condition = eval(sql_param)['query_condition']
                result = MySQLGetData().mysql_get_data(query, (query_condition,), 1)
                try:
                    self.assertEqual(int(result[0]), int(eval(sql_param)['expected']))
                    sql_result = "Pass"
                except AssertionError as e:
                    logger.error("执行用例时报错：{0}".format(e))
                    sql_result = "Fail"
                    raise e
                finally:
                    self.save.write_data(item['case_id'] + 1, 11, sql_result)

        try:
            self.assertEqual(new_param, str(res))
            test_result = "Pass"
        except AssertionError as e:
            logger.error("执行用例时报错：{0}".format(e))
            test_result = "Fail"
            raise e
        finally:
            self.save.write_data(item['case_id']+1, 10, test_result)

    def tearDown(self):
        logger.info("测试结束")
