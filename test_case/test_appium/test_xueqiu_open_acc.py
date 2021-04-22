# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/21
Describe:
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuOpenAcc:

    def setup(self):

        desire_caps ={
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'deviceName': '127.0.0.1:7555',
            'noReset': True,
            "skipDeviceInitialization": True,
            "chromedriverExecutableDir": "D:\\softinstall\\chrome\\chromedriver220"

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):

        pass

    def test_xueqiu_open_acc(self):
        """
        使用uiautomatorviewer定位app内的webview
        不同设备的渲染不同,不具有兼容性
        推荐:打开webview开关,使用chrome://inspect 来定位
        :return:
        """

        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        locator = (MobileBy.ACCESSIBILITY_ID, 'A股开户')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
        phone_loc = (MobileBy.ID, 'phone-number')
        get_verify_loc = (MobileBy.ACCESSIBILITY_ID, '获取验证码')
        vrify_loc = (MobileBy.ID, 'code')
        open_btn = (MobileBy.ACCESSIBILITY_ID, '立即开户')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(phone_loc))
        self.driver.find_element(*phone_loc).send_keys('13100010004')
        sleep(2)
        self.driver.find_element(*get_verify_loc).click()
        self.driver.find_element(*vrify_loc).send_keys('008976')
        self.driver.find_element(*open_btn)




























