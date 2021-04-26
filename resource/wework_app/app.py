# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/24
Describe:app 基类
"""
from time import sleep

from appium import webdriver
from resource.wework_app.base_app_page import BaseAppPage
from resource.wework_app.home_tab_page import HomeTabPage


class App(BaseAppPage):

    def start(self):
        if not self.driver:
            self.log_info("App 类开始初始化driver")
            caps = {
                "platformName": "android",
                "deviceName": "mumu",  # 无udid默认使用adb devices列表的而第一个
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                "skipServerInstallation": True,
                "skipDeviceInitialization": True,
                "dontStopAppOnReset": True
                # "settings": {
                #     "waitForIdleTimeout": 0  # 动态页面等待加载时间默认10秒
                # }
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(35)
        else:
            self.log_info("复用已有driver")
            self.driver.launch_app()
        return self

    def restart(self):

        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):

        sleep(3)
        if self.driver:
            self.driver.quit()

    def goto_main(self):

        return HomeTabPage(self.driver)

