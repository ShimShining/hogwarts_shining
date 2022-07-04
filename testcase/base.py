# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium import webdriver
from time import sleep
import os

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


# 全局变量 或者单例解决driver共享问题
class Common:

    driver = None

    def set_driver(self, dr):

        Common.driver = dr
        return Common.driver


class SingleDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
        return cls.driver

class Base:

    def setup(self):

        if Common.driver:
            print("Base 无driver实力")
            self.driver = Common.driver
        else:
            # browser = os.getenv("browser")
            # if browser == 'firefox':
            #     self.driver = webdriver.Firefox()
            # elif browser == 'headless':
            #     self.driver = webdriver.PhantomJS()
            # else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            print("Base 里实例化的driver")
            Common().set_driver(self.driver)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        sleep(5)
        self.driver.quit()


class MPath:

    def __init__(self, locator, method="XPATH"):

        self.locator = locator
        self.method = method
        if Common.driver:
            self.driver = Common.driver
        else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            Common().set_driver(self.driver)

    def get_element(self):

        if self.method == "XPATH":
            return self.driver.find_element(By.XPATH, self.locator)
        if self.method == "CSS_SELECTOR":
            return self.driver.find_element(By.CSS_SELECTOR, self.locator)
        if self.method == "ID":
            return self.driver.find_element(By.ID, self.locator)
        if self.method == "NAME":
            return self.driver.find_element(By.NAME, self.locator)

    def click(self):

        self.get_element().click()

    def input(self, input_text):

        self.get_element().send_keys(input_text)

    def scroll(self, to_y=2000):
        """
        滑动页面
        :return:
        """
        elem = self.get_element()
        action = TouchActions(self.driver)
        action.scroll_from_element(elem, 0, to_y)
        action.perform()
        sleep(2)

    @property
    def text(self):
        return self.get_element().text



