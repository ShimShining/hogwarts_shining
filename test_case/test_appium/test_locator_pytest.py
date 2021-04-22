# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/20
Describe:
"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestLocatorPytest:

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

        self.driver.quit()

    def test_search(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        cur_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        # assert cur_price > 200
        assert_that(cur_price, close_to(229, 229 * 0.05))
        # self.driver.back()
        # self.driver.back()

    def test_get_attr(self):
        elem_search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_status = elem_search.is_enabled()
        print(search_status)
        if search_status:
            print(elem_search.text)
            print(elem_search.location)
            print(elem_search.size)
            elem_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            sleep(3)
            alibaba = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            alibaba_visible = alibaba.get_attribute("displayed")
            if alibaba_visible == "true":
                print("搜索成功")
            else:
                print('搜索失败')

    def test_touchaction(self):

        action = TouchAction(self.driver)
        rect = self.driver.get_window_rect()
        width = rect['width']
        height = rect['height']
        x = int(width/2)
        y = int(height * 4/5)
        to_y = int(height * 1/5)
        sleep(3)
        action.press(x=x, y=y).wait(200).move_to(x=x, y=to_y).release().perform()
        sleep(3)

    def test_get_cur_price(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        cur_price_elem = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        cur_price = float(cur_price_elem.text)
        print(cur_price)

    def test_automator(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        sleep(3)
        name_elem = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")')
        pwd_elem = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")')
        login_btn = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")')
        name_elem.send_keys('13400010002')
        pwd_elem.send_keys('3563284567')
        login_btn.click()
        sleep(5)

    def test_scroll(self):

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("清水").instance(0));' )

    def test_wait(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # cur_price_elem = self.driver.find_element_by_xpath(
        #    "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        #WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        elem = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # cur_price_elem = self.driver.find_element(*locator)
        # cur_price = float(cur_price_elem.text)
        cur_price = float(elem.text)
        print(cur_price)

    def test_get_attr(self):

        search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search.get_attribute("content-desc"))
        print(search.get_attribute("resource-id"))
        print(search.get_attribute("bounds"))
        print(search.get_attribute("clickable"))

    def test_hamcrest(self):

        assert_that(10, close_to(9, 2))
        assert_that("string with ts", contains_string("with"))

if __name__ == "__main__":

    pytest.main()

