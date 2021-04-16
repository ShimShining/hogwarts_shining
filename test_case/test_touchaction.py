# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from time import sleep


class TestTouchaction:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    def test_touch_action_scroll(self):

        self.driver.get("https://www.baidu.com")
        elem = self.driver.find_element(By.ID, 'kw')
        ele_search = self.driver.find_element(By.ID, 'su')
        elem.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(elem, 0,10000).perform()
        sleep(5)


