# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/21
Describe:
"""
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "browserName": 'Browser',
            "noReset": True,
            # "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            # "chromedriverExecutable": "D:/softinstall/chrome/chromedriver220/"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):

        self.driver.quit()

    def test_browser(self):

        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element_by_id("index-bn").click()
