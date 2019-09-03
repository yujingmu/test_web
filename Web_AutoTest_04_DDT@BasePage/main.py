# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 20:15
# @Author  : yimi
# @File    : main.py

import time
import unittest
from Common import config_dir
from HTMLTestRunnerNew import HTMLTestRunner
# 将HTMLTestRunnerNew.py file 放至到python 的lib路径下 D:\python37\Lib

# 实例化套件对象
s = unittest.TestSuite()
# TestLoader的用法
#   实例化TestLoader对象
# 使用discover取值一个目录下的所有测试用例
# 使用S
loader = unittest.TestLoader()
s.addTests(loader.discover(config_dir.CASE_PATH))

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

file = open(config_dir.REPORT_PATH+"/Web_AutoTest_{0}.html".format(curTime), "wb")
runner = HTMLTestRunner(
    stream=file,
    title='Web Test Report',
    description = "web 测试报告",
    tester="薏米",
)

runner.run(s)

