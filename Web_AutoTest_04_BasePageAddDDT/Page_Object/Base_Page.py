# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 21:03
# @Author  : yimi
# @File    : Base_Page.py

import time
import random
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Common import config_dir
from Common import Logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_click(self, locator, wait=30, requence=0.2):
        try:
            # start = time.localtime()
            # print(start)
            # print(type(start))
            element = WebDriverWait(self.driver, wait, requence).until(EC.element_to_be_clickable(locator))
            # end = time.localtime()
            # wait_time = "end - start"
            # logger.info("等待元素可见：｛0｝, 起始时间为：｛1｝, 等待时长：｛2｝".format(locator, start, wait_time))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("元素定位超时，detailed info is {0}".format(e))
            self._screen_shot()
            raise

    def _screen_shot(self, model_name = "model"):                         # 函数名添加下划线表示该函数只在内部使用
        # 根据功能和时间点生成截图
        # 文件格式：功能名称_年月日-时分秒.png
        file_path = config_dir.IMG_PATH + "/{0}_{1}.png"\
            .format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        self.driver.save_screenshot(file_path)
        logging.info("截图成功，路径为: {0}".format(file_path))

    def click_element(self, locator, model="model",index=None):
        """
        :param locator: 查找元素的方法值，属性值
        :param by: 查找元素的方法
        :param model: 执行测试用例的模块
        :param index: 多个元素中选择某个元素的下标
        :return: 返回查找到的某个元素
        """
        logging.info("开始执行点击操作")
        element = self._select_one_from_elements(locator,model, index)
        # logger.info("点击元素：{0}={1}".format(locator))
        try:
            element.click()
        except:
            logging.error("点击操作失败")
            self._screen_shot(model)
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
            logging.error("输入文本{0}失败".format(value))
            self._screen_shot(model)
            raise



    def wait_element_presence(self, locator, model="model", wait=30, requence=0.5):
        try:
            # start = time.localtime()
            element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            # end = time.localtime()
            # wait_time = end - start
            # logger.info("等待元素存在：｛0｝, 起始时间为：｛1｝, 等待时长：｛2｝".format(locator, start, end))
            return element
        except (TimeoutException, NoSuchElementException) as e:
        # 日志
            logging.error("等待元素存在异常{0}".format(e))
        # 截图   存放地址，图片名字
            self._screen_shot(model)
            raise


    def wait_element_visibility(self, locator, model="model", wait=30, requence=0.5):
        try:
            # start = time.localtime()
            element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            # end = time.localtime()
            # wait_time = end - start
            # logger.info("等待元素可见：｛0｝, 起始时间为：｛1｝, 等待时长：｛2｝".format(locator, start, end))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("等待元素存在异常{0}".format(e))
            self._screen_shot(model)


    def find_element(self, locator, model='model'):
        try:
            self.wait_element_presence(locator)
            return self.driver.find_element(locator)
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("等待元素存在异常{0}".format(e))
            self._screen_shot(model)


    def scroll_to_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_iframe_available_and_switch_to_it(self, locator, wait=30, requence=0.5):
        element = WebDriverWait(self.driver, wait, requence)
        return element.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def wait_element_quick_presence(self, locator, wait=5, requence=0.2):
        element = WebDriverWait(self.driver, wait, requence)
        return element.until(EC.presence_of_element_located(locator))

    def _select_one_from_elements(self, locator, by=By.XPATH, model="model", index=None):
        logging.info("查找元素：{0}={1}".format(by, locator))
        if index != None:  # 多个元素中选择一个
            try:
                element = self.driver.find_elements(by=By.XPATH, value=locator)
            except:
                logging.error("查找多个元素失败")
                self._screen_shot(model)
                raise
            if index == -1 or index < 0:  # 随机选择一个
                random_index = random.randint(0, len(element) - 1)
                element = element[random_index]
            else:
                element = element[index]
        else:
            try:
                element = self.driver.find_element(by=By.XPATH, value=locator)
            except:
                logging.error("查找单个元素失败")
                self._screen_shot(model)
                raise

    def switch_window(self, window_handles, wait, requence, name=None):
        WebDriverWait(self.driver, wait, requence).until(EC.new_window_is_opened(window_handles))
        if not name:
            return self.driver.switch_to.window(window_handles[-1])
        return self.driver.switch_to.window(name)




