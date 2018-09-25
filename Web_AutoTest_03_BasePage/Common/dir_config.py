#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:40
# @Author  : yimi
# @File    : dir_config.py.py

import os
#
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, 'TestDatas')

testcases_dir = os.path.join(base_dir, "TestCase")

logs_dir = os.path.join(base_dir, "Logs")

screenshot_dir = os.path.join(base_dir, "ScreenShot")






