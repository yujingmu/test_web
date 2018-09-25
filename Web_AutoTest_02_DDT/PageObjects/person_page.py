#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 22:09
# @Author  : yimi
# @File    : person_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from person_locator import PersonLocator

class PersonPage:
    def __init__(self, driver):
        self.driver = driver
        self.person_locator = PersonLocator()

    def get_balance(self):
        balance_button = (By.XPATH, self.person_locator.person_balance_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(balance_button))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.person_locator.person_balance_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # return element.get_attribute("data-amount")
        return (self.driver.find_element_by_xpath(self.person_locator.person_balance_xpath).text).strip("元")
