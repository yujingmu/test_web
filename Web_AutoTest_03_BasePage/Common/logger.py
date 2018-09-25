#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 21:20
# @Author  : yimi
# @File    : logger.py

import os
import time
import logging
from Common import dir_config
from logging.handlers import RotatingFileHandler

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir + "/Web_AutoTest_{0}.log".format(curTime), backupCount=20,
                                encoding='utf-8')

# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

# logging.info("hehehe")
