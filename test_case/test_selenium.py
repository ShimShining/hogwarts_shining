# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/13
Describe:
"""
from selenium import webdriver
import time

def test_webdriver():

    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(5)

