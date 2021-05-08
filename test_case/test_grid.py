# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/8
Describe:
"""
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote


class TestGrid:

    def test_grid(self):

        hub_url = 'http://127.0.0.1:4444/wd/hub'
        capability = DesiredCapabilities.CHROME.copy()
        # 使用多线程实现并发
        for i in range(1, 5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get("https://www.baidu.com")
