# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:

windows: adb logcat ActivityManager:I | findstr "cmp" 后启动目标应用
Windows: aapt dump badging wework.apk  | findstr launchable-activity
adb shell am start -W -n <package-name>/<activity-name> -S
com.tencent.wework/.launch.LaunchSplashActivity

self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
'new UiScrollable(new UiSelector().scrollable(true).instance(0)).
scrollIntoView(new UiSelector().text("添加成员").instance(0));')
课后作业
使用 Appium 实现自动化添加联系人
"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from resource.wework_app.home_tab_page import HomeTabPage


class TestAddContactMember:

    def setup(self):

        caps = {
            "platformName": "android",
            "deviceName": "mumu",   # 无udid默认使用adb devices列表的而第一个
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "skipServerInstallation": True,
            "skipDeviceInitialization": True,
            # "dontStopAppOnReset": True
            # "settings": {
            #     "waitForIdleTimeout": 0  # 动态页面等待加载时间默认10秒
            # }
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(35)

    def teardown(self):

        sleep(5)
        self.driver.quit()

    def test_add_contact_member(self):

        # 进入通讯录页面
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']").click()
        # 滑动查找添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).'
                                 'instance(0)).scrollIntoView(new UiSelector().text("添加成员").'
                                 'instance(0));').click()
        # 进入添加成员输入信息页
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入成员信息并点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys('王五')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys('131244014402')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        # 查找 toast信息
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast' and @text='添加成功']")
        # 返回上一级查找刚刚添加的成员是否在列表中
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h86").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='王五']")


# PO
class TestAddContactMemberPO:

    def setup(self):

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
        self.home = HomeTabPage(self.driver)

    def teardown(self):

        self.home.kill_env()

    @pytest.mark.parametrize("info,username,phone,toast", [
       ["添加成员", "木子李", "13444014405", "添加成功"]
    ])
    def test_add_contact_member(self, info, username, phone, toast):

        member_list = self.home.enter_contact_tab().goto_add_member_page(info).\
            goto_member_info_input_page().add_member_and_save(username, phone, toast).\
            back_conctact_tab_page().get_contact_member_list()
        assert username in member_list








































