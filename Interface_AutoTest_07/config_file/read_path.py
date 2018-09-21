#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 9:06
# @Author  : yimi
# @File    : read_path.py

import os
from Task.task_0810_database.common.read_config_data import ReadConfigDate
project_config_path = os.path.realpath(__file__)
# print(project_config_path)
# 配置文件的路径
config_path = os.path.join(os.path.split(project_config_path)[0], 'config_file.conf')
# print(config_path)
# # 读取顶级目录
project_path = ReadConfigDate(config_path, 'PROJECT_PATH', 'project_path').read_config()
# print(project_path)# # 读取测试数据的目录
test_data_path = os.path.join(project_path, 'test_data', 'excel_test_data.xlsx')
# print(test_data_path)
# # 测试日志的存储路径
test_log_path = os.path.join(project_path, 'test_result', 'log_file')
# print(test_log_path)
# # 测试html报告的存储路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report')
# print(test_report_path)
# 测试报告类型为txt的文件的存储路径



