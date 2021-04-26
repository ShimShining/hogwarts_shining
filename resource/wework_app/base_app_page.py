# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:app PO 基类
"""
import time
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from resource.utils.log import *
import sys
import os

# path.abspath(sys.modules['__main__'].__file__)
log_filename = os.path.realpath(sys.argv[1]).split("\\")[-1]. \
    replace(".py::", "py_").replace("::", ".") \
    if sys.argv[1] else None
# log_filename = os.path.basename(__file__)
print(f"日志主文件路径={log_filename}")
print(f"Sys.argv参数列表={sys.argv}")
logger = Logger(log_filename).logger


class BaseAppPage:

    def __init__(self, driver: WebDriver = None):

        self.driver = driver

    def wait_for_visible(self, loc, timeout=20, frequency=0.5):

        try:
            self.log_info(f"等待元素{loc}可见")
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

        try:
            self.driver.find_element(MobileBy.XPATH,
                                     f"//*[@class='android.widget.Toast' and @text='{info}']")
            self.log_info(f"查找定位文本信息=[{info}]成功.")
        except NoSuchElementException as e:
            self.log_error(f"查找定位文本信息=[{info}]失败!!!")

    def log_info(self, msg):

        logger.info(msg)

    def log_error(self, err_msg):

        logger.error(err_msg)

    def kill_env(self):

        time.sleep(2)
        self.driver.quit()

    def swipe_find(self, text, limit=5):

        for i in range(limit):
            try:
                elemment = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(30)
                return elemment
            except NoSuchElementException:
                self.log_info(f"未找到{text}文本,继续滑动查找")
                size = self.driver.get_window_size()
                wid = size['width']
                height = size['height']
                start_x = wid / 2
                start_y = height * 0.8
                to_x = wid / 2 + wid * 1 / 9
                to_y = height * 0.3
                duration = 2000     # 单位毫秒
                self.driver.swipe(start_x, start_y, to_x, to_y, duration)

            if i == limit - 1:
                self.driver.implicitly_wait(30)
                raise NoSuchElementException(f"查找文本{text}{i}次后,未找到!!!")




