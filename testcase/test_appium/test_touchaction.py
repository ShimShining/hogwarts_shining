# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/20
Describe:
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            # "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        # driver的生命周期生效,全局性
        self.driver.implicitly_wait(15)

    def teardown(self):

        pass

    def test_touch_action(self):

        action = TouchAction(self.driver)
        # 手势解锁
        action.press().wait(200).move_to().move_to().move_to().move_to().release().perform()



