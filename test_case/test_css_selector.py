# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCssSelector:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
        self.driver.get(self.url)

    def teardown(self):
        self.driver.quit()

    def test_xpath(self):

        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹")
        # self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹")
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹")
        self.driver.find_element(By.ID, 'su').click()
        sleep(5)


