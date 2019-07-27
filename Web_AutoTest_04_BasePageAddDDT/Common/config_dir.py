# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 20:36
# @Author  : yimi
# @File    : config_dir.py

import os

ROOT_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(ROOT_PATH)

LOG_PATH = os.path.join(ROOT_PATH, "LOG")
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

IMG_PATH = os.path.join(LOG_PATH,"IMG")
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)

CASE_PATH = os.path.join(ROOT_PATH, "Test_Cases")
if not os.path.exists(CASE_PATH):
    os.makedirs(CASE_PATH)

REPORT_PATH = os.path.join(ROOT_PATH, "HTML_REPORT")
if not os.path.exists(REPORT_PATH):
    os.makedirs(REPORT_PATH)
