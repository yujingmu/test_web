# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 18:28
# @Author  : yimi
# @File    : main.py

import pytest
import time
from Common import config_dir

if __name__ == '__main__':
    curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
    pytest.main(['-m', "smoke",
                 "--reruns", '2',
                 "--reruns-delay", '5',
                 "--html=" + config_dir.HTML_REPORT_PATH + "/pytest-result-" + curTime + ".html",
                 # HTML，通过网页展示测试报告
                 "--junitxml=" + config_dir.XML_REPORT_PATH + "/pytest-result-" + curTime + ".xml",
                 # XML格式，用于与jenkins集成
                 "--resultlog=" + config_dir.PYTEST_LOG_PATH + "/pytest-result-" + curTime + ".log"])


