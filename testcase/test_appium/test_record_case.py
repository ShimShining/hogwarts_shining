# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/20
Describe:
"""
from appium import webdriver

desire_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("淘宝")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
el3.click()

