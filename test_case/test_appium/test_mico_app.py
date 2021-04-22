# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/21
Describe:
"""
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMicroApp:

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.mm",
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "chromedriverExecutable": "D:\\softinstall\\chrome\\chromedriver220\\chromedriver.exe",
            "chromeOptions": {
                "androidProcess": "com.tencent.mm:appbrand0"
            },
            "adbPort": 5038
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(30)

    def test_search(self):
        # native
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5,size['height'] * 0.4,size['width'] * 0.5,size['height']*0.8)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消"]')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, '//*[@text="自选"]')

        print(self.driver.contexts)

        # 计入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()

        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()

        # 点击
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.find_element(By.CSS_SELECTOR, '.stock__item')
        self.driver.find_element(By.CSS_SELECTOR, '.stock__item').click()

    def find_top_window(self, driver=None):

        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print('find')
                return True
            else:
                self.driver.switch_to.window(window)
        return False








































