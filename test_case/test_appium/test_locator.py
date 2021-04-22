# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/20
Describe:
"""
from time import sleep
from appium import webdriver

desire_cap = {
    "platformName": "android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True,
    "dontStopAppOnReset": True,
    "skipDeviceInitialization": True
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
# driver的生命周期生效,全局性
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
sleep(5)
driver.back()
driver.back()
driver.quit()
