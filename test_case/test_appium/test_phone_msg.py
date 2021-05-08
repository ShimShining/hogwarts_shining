# -*- coding:utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/6
Describe:
"""
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestPhoneMsg:

    def setup(self):

        caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "mumu",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".Main",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "avd": "Nexus_5X_API_30_x86"   # 自动启动android sdk中的虚拟设备
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):

        self.driver.quit()

    def test_mobile_apis(self):

        self.driver.make_gsm_call('13345677891', GsmCallActions.CALL)
        self.driver.send_sms('13812349871', 'appium sms test')
        self.driver.set_network_connection(1)   # 0,1,2,4,6
        sleep(3)
        self.driver.set_network_connection(6)
        sleep(3)
        self.driver.get_screenshot_as_file('./img.png')

        self.driver.start_recording_screen()

        self.driver.stop_recording_screen()
