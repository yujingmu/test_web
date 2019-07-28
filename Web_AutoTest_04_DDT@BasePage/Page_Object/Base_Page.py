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

    def _screen_shot(self, model = "model"):                         # 函数名添加下划线表示该函数只在内部使用
        # 根据功能和时间点生成截图
        # 文件格式：功能名称_年月日-时分秒.png
        file_path = config_dir.IMG_PATH + "/{0}_{1}.png"\
            .format(model, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        self.driver.save_screenshot(file_path)
        logging.info("{0}错误截图成功，路径为: {0}".format(model, file_path))

    def wait_element_click(self, locator, wait=30, requence=0.2, model ="model"):
        try:
            element = WebDriverWait(self.driver, wait, requence).until(EC.element_to_be_clickable(locator))
            logging.info("等待{0}元素可见".format(locator))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("元素定位超时，错误信息为：{0}".format(e))
            self._screen_shot(model)
            raise

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
        logging.info("点击元素：{0}".format(locator))
        try:
            element.click()
        except:
            logging.error("点击操作失败")
            self._screen_shot(model)
            raise


    def input_text(self, value, locator, model="model"):
        """
        :param locator: 
        :param by: 
        :param value: 
        :param index: 
        :param model: 
        :return: 
        """
        try:
            logging.info("开始执行文本输入操作")
            self.find_element(locator, model).send_keys(value)
            logging.info("输入文本框元素：{0}".format(locator))
        except:
            logging.error("输入框{0}输入文本{1}失败".format(locator, value))
            self._screen_shot(model)
            raise


    def wait_element_presence(self, locator, model="model", wait=30, requence=0.5):
        try:
            element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            logging.info("等待{0}元素存在".format(locator))
            return element
        except (TimeoutException, NoSuchElementException) as e:
        # 日志
            logging.error("等待元素存在异常{0}".format(e))
        # 截图   存放地址，图片名字
            self._screen_shot(model)
            raise

    def wait_element_quick_presence(self, locator, wait=5, requence=0.2, model="model"):
        try:
            element = WebDriverWait(self.driver, wait, requence)
            return element.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("等待元素存在异常{0}".format(e))
            self._screen_shot(model)
            raise

    def wait_element_visibility(self, locator, model="model", wait=30, requence=0.5):
        try:
            element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            logging.info("等待{0}元素可见".format(locator))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("等待元素存在异常{0}".format(e))
            self._screen_shot(model)
            raise

    def find_element(self, locator, model='model'):
        try:
            self.wait_element_presence(locator)
            return self.driver.find_element(*locator)
        except (TimeoutException, NoSuchElementException) as e:
            logging.error("等待元素存在异常{0}".format(e))
            self._screen_shot(model)
            raise

    def scroll_to_view(self, locator, model="model"):
        element = self.find_element(locator)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            logging.error("指定元素执行滚动操作失败")
            self._screen_shot(model)
            raise

    def wait_iframe_available_and_switch_to_it(self, locator, wait=30, requence=0.5, model="model"):
        try:
            element = WebDriverWait(self.driver, wait, requence)
            return element.until(EC.frame_to_be_available_and_switch_to_it(locator))
        except:
            logging.error("等待iframe出现并切换失败")
            self._screen_shot(model)
            raise


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




