# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/16
Describe:使用chrome复用浏览器获取cookies信息
"""
from selenium import webdriver
import yaml


class TestGetCookies:

    def test_get_cookie(self):

        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9777"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("menu_contacts").click()

        cookie = self.driver.get_cookies()
        with open('../datas/cookie.yml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)

