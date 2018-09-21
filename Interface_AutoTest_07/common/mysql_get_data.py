#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/2018 10:50 AM
# @Author  : yimi
# @File    : mysqp_get_data.py


import mysql.connector
from task_0810_database.common.read_config_data import ReadConfigDate
from task_0810_database.config_file import read_path

class MySQLGetData:

    def __init__(self):
        self.config = eval(ReadConfigDate(read_path.config_path, 'DB', 'config').read_config())

    def mysql_get_data(self, query, query_condition, state=0):
        cnn = mysql.connector.connect(**self.config)
        cursor = cnn.cursor()
        # cursor.execute(query, (query_condition,))
        cursor.execute(query, query_condition)
        if state == 1:
            result = cursor.fetchone()    # fetchone返回的数据类型为元组
        else:
            result = cursor.fetchall()      # fetchall 返回的数据类型为列表
        cursor.close()
        cnn.close()
        return result

if __name__ == "__main__":
    query = "select regtime from member where mobilephone=%s"
    # query_condition = '18093192866'
    query_condition =('18093192866',)
    state = 1
    result = MySQLGetData().mysql_get_data(query, query_condition, state)
    print(result[0])
    # print("LeaveAmount:", int(result[0]))
    # query = "select * from member where id in (%s, %s) "
    # query_condition = (120, 125)
    # state = 1
    # result = MySQLGetData().mysql_get_data(query, query_condition, state)
    # print(result)
