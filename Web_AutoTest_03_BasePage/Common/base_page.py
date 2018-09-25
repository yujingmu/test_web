#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 22:16
# @Author  : yimi
# @File    : base_page.py
# basepage
# 常用的方法函数封装起来
# 加入日志，截图功能

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logger
import dir_config
import logging
import random
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, by=By.XPATH, model="model", wait=30, requence=0.5):
        # 等待元素可见
        try:
            start = time.localtime()
            WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_all_elements_located(locator))
            end = time.localtime()
            wait_time = end - start
            logging.info("等待元素可见：｛0｝, 起始时间为：｛1｝, 等待时长：｛2｝".format(locator, start, wait_time))
        except:
            # 日志
            logging.exception("等待元素可见异常")
            # 截图   存放地址，图片名字
            self._save_screenshot(model)
            raise

    def click_element(self, locator, by=By.XPATH, model="model",index=None):
        """
        :param locator: 查找元素的方法值，属性值
        :param by: 查找元素的方法
        :param model: 执行测试用例的模块
        :param index: 多个元素中选择某个元素的下标
        :return: 返回查找到的某个元素
        """
        logging.info("开始执行点击操作")
        element = self._select_one_from_elements(locator,by,model, index)
        logging.info("点击元素：{0}={1}".format(by, locator))
        try:
            element.click()
        except:
            logging.exception("点击操作失败")
            self._save_screenshot(model)
            raise


    def input_text(self, value, locator, by=By.XPATH, model="model", index=None):
        """
        :param locator: 
        :param by: 
        :param value: 
        :param index: 
        :param model: 
        :return: 
        """
        logging.info("开始执行文本输入操作")
        element = self._select_one_from_elements(locator, by, model, index)
        logging.info("输入文本框元素：{0}={1}".format(by, locator))
        try:
            element.send_keys(value)
        except:
            logging.exception("输入文本{0}失败".format(value))
            self._save_screenshot(model)
            raise

    def get_element_attribute(self, attribute_name, locator, by=By.XPATH, model="model", index=None):
        logging.info("开始获取元素属性")
        element = self._select_one_from_elements(locator, by, model, index)
        logging.info("获取元素{0}的属性值".format(element))
        try:
            element.get_attribute(attribute_name)
        except:
            logging.exception("获取元素{0}的属性值失败".format(element))
            self._save_screenshot(model)
            raise

    def get_text(self, locator, by=By.XPATH, model="model", index=None):
        logging.info("开始获取元素文本内容")
        element = self._select_one_from_elements(locator, by, model, index)
        logging.info("获取元素{0}的文本内容".format(element))
        try:
            element.text
        except:
            logging.exception("获取元素{0}的文本内容失败".format(element))
            self._save_screenshot(model)
            raise

    def scroll_element_into_view(self, locator, by=By.XPATH, model="model", index=None):
        logging.info("开始获取元素文本内容")
        element = self._select_one_from_elements(locator, by, model, index)
        logging.info("拖动滚动条滚动元素{0}到视野可见区域".format(element))
        try:
            self.driver.execute_javascript("arguments[0].scrollIntoView()", element)
        except:
            logging.exception("拖动滚动条滚动元素{0}到视野可见区域失败".format(element))
            self._save_screenshot(model)
            raise

    def _select_one_from_elements(self, locator, by=By.XPATH, model="model", index=None):
        logging.info("查找元素：{0}={1}".format(by, locator))
        if index != None:     # 多个元素中选择一个
            try:
                element = self.driver.find_elements(by=By.XPATH, value=locator)
            except:
                logging.exception("查找多个元素失败")
                self._save_screenshot(model)
                raise
            if index == -1 or index < 0:     #随机选择一个
                random_index = random.randint(0, len(element)-1)
                element = element[random_index]
            else:
                element = element[index]
        else:
            try:
                element = self.driver.find_element(by=By.XPATH, value=locator)
            except:
                logging.exception("查找单个元素失败")
                self._save_screenshot(model)
                raise

    def _save_screenshot(self, model_name="model"):     # 函数名添加下划线表示该函数只在内部使用
            # 根据功能和时间点生成截图
            # 文件格式：功能名称_年月日-时分秒.png
            file_path =  dir_config.screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) )
            self.driver.save_screenshot(file_path)
            logging.info("截图成功，路径为: {0}".format(file_path))


