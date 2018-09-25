#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 20:40
# @Author  : yimi
# @File    : bid_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bid_locator import BidLocator

class BidPage:
    def __init__(self, driver):
        self.driver = driver
        self.bid_locator = BidLocator

    def get_avalible_balance(self):
        bid_balance_locator = (By.XPATH, self.bid_locator.bid_balance_path)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(bid_balance_locator))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.bid_locator.bid_balance_path)
        return (element.get_attribute("data-amount")).strip("元")

    # 在投资金额输入框中填写投资金额
    def input_invest_balance(self, money):
        # 等待元素可见
        bid_balance_locator = (By.XPATH, self.bid_locator.bid_balance_path)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(bid_balance_locator))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.bid_locator.bid_balance_path)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # 填写投资金额
        self.driver.find_element_by_xpath(self.bid_locator.bid_balance_path).send_keys(money)
    # 填写投资金额后，点击提交按钮
    def click_submit_button(self):
        submit_bid_locator = (By.XPATH, self.bid_locator.submit_bid_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(submit_bid_locator))
        # 滚动到视野可见区域
        element = self.driver.find_element_by_xpath(self.bid_locator.submit_bid_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        self.driver.find_element_by_xpath(self.bid_locator.submit_bid_xpath).click()
    # 投资成功后点击查看并激活按钮
    def click_active_button(self):
        check_active_locator = (By.XPATH, self.bid_locator.check_active_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(check_active_locator))
        self.driver.find_element_by_xpath(self.bid_locator.check_active_xpath).click()
    # 投资成功后，读取弹出的提示信息
    def success_invest_msg(self):
        msg_invest_success = (By.XPATH, self.bid_locator.popup_msg_success)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(msg_invest_success))
        return self.driver.find_element_by_xpath(self.bid_locator.popup_msg_success).text
    # 投资金额不是100的倍数，读取弹出的提示信息
    def fail_invest_by_no100(self):
        msg_no100_locator = (By.XPATH, self.bid_locator.no100_popup_msg)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(msg_no100_locator))
        return self.driver.find_element_by_xpath(self.bid_locator.no100_popup_msg).text
    # 投资金额不是10的倍数，读取弹出的提示信息
    def fail_invest_by_no10(self):
        msg_no10_locator = (By.XPATH, self.bid_locator.no10_popup_msg)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(msg_no10_locator))
        return self.driver.find_element_by_xpath(self.bid_locator.no10_popup_msg).text



