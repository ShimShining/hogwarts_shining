# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/19
Describe:PO基类封装
"""
import time

import yaml

from selenium import webdriver


class BasePage:

    def __init__(self, base_driver=None):

        if base_driver is None:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
            with open('../datas/cookie.yml', encoding='utf-8') as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            print('cookie登录成功')
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        else:
            self.driver = base_driver

    def find(self, by, elem=None):

        if elem:
            return self.driver.find_element(by, elem)

        return self.driver.find_element(*by)

    def finds(self, by, elem=None):

        if elem:
            return self.driver.find_elements(by, elem)

        return self.driver.find_elements(*by)

    def kill_env(self):

        time.sleep(3)
        self.driver.quit()



