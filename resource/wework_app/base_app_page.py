# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:app PO 基类
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseAppPage:

    def __init__(self, driver: WebDriver):

        self.driver = driver

    def wait_for_visible(self, loc, timeout=20, frequency=0.5):

        try:
            WebDriverWait(self.driver, timeout, frequency).\
                            until(expected_conditions.visibility_of_all_elements_located(loc))
        except Exception as e:
            raise e

    def scroll_to_text(self, find_text):
        """
        滑动到指定文本,并返回该元素
        :param find_text:
        :return:
        """
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).'
                                 f'instance(0)).scrollIntoView(new UiSelector().text("{find_text}").'
                                 'instance(0));')

    def find(self, mobile_by, path=None):

        if path:
            return self.driver.find_element(mobile_by, path)
        return self.driver.find_element(*mobile_by)

    def finds(self, mobile_by, path=None):

        if path:
            return self.driver.find_elements(mobile_by, path)
        return self.driver.find_elements(*mobile_by)

    def check_toast_info(self, info):

        return self.driver.find_element(MobileBy.XPATH,
                                        f"//*[@class='android.widget.Toast' and @text='{info}']")

    def kill_env(self):

        sleep(2)
        self.driver.quit()



