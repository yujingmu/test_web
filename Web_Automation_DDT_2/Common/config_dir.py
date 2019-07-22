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
    os.mkdir(LOG_PATH)

IMG_PATH = os.path.join(LOG_PATH,"IMG")
if not os.path.exists(IMG_PATH):
    os.mkdir(IMG_PATH)


