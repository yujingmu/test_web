#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 17:02
# @Author  : yimi
# @File    : config.py

import configparser
from task_0810_database.config_file import read_path

class ReadConfigDate:
    def __init__(self, config_file, section_name, option_name):
        self.config_file = config_file
        self.section_name = section_name
        self.option_name = option_name
        self.cf = configparser.ConfigParser()

    def read_config(self):
        self.cf.read(self.config_file, encoding="UTF-8")
        value = self.cf.get(self.section_name, self.option_name)   # value的类型为 str
        return value                                               # eval(value)  返回原有的value类型

if __name__ == "__main__":
    url = ReadConfigDate(read_path.config_path, 'IP', 'ip').read_config()
    mode = ReadConfigDate(read_path.config_path, 'FLAG', 'mode').read_config()
    mode_data = ReadConfigDate(read_path.config_path, 'FLAG', 'case_id').read_config()
    data_base = ReadConfigDate(read_path.config_path, 'DB', 'config').read_config()
    print(url)
    print(mode)
    print(mode_data)
    print(data_base)
