#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:31
# @Author  : yimi
# @File    : index_page.py

import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from index_locator import IndexLocator
class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        self.index_locator = IndexLocator()

    def get_nickName(self):
        nickname_locator = (By.XPATH, self.index_locator.user_name_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(nickname_locator))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.index_locator.user_name_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver.find_element_by_xpath(self.index_locator.user_name_xpath).text

    def change_to_person_page(self):
        nickname_locator = (By.XPATH, self.index_locator.user_name_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(nickname_locator))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.index_locator.user_name_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element_by_xpath(self.index_locator.user_name_xpath).click()


    def click_firstbid(self):
        # 等待元素可见
        first_bid = (By.XPATH, self.index_locator.bid_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(first_bid))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.index_locator.bid_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # 点击元素
        self.driver.find_element_by_xpath(self.index_locator.bid_button_xpath).click()

    def random_bid(self):
        # 等待元素可见
        bid_locator = (By.XPATH, self.index_locator.bid_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(bid_locator))
        # 找到页面中的多个元素
        elements = self.driver.find_elements_by_xpath(self.index_locator.bid_xpath)
        # 滚动到视野可见区域
        self.driver.execute_script("arguments[0].scrollIntoView();", elements)
        # 在多个标中选择一个进行投标操作
        index = random.randint(0, len(elements)-1)           # 取左又取右
        # 点击
        elements[index].click()

















