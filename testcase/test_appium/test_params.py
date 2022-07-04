# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/21
Describe:
"""
from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParams:

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

        # self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
        self.driver.quit()

    @pytest.mark.parametrize('s_key,code,price', [
        ['alibaba', 'BABA', 220],
        ['xiaomi', '01810', 25]
    ])
    def test_search(self, s_key, code, price):
        """
        1. 打开雪球应用
        2. 点击搜索框
        3. 输入搜索词
        4. 点击第一个搜索联想词
        5. 判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(s_key)
        sleep(2)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        cur_p = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{code}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        cur_p = float(cur_p)
        # expect_price = 220
        assert_that(cur_p, close_to(price, price * 0.1))



























