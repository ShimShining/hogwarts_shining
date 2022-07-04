# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/16
Describe:login 封装
"""
from selenium import webdriver
import yaml
from resource.wework import WeWorkContactsPage
from testcase.base import Common, Base


class WeworkLogin:

    def get_locator(self):
        return {

        }

    def __init__(self):

        if Common.driver:
            self.driver = Common.driver
            print("24 Login init里无driver")
        else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            Common().set_driver(self.driver)
            print("30 Login init里实例化driver")

        self.login_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_login_page(self):
        self.driver.get(self.login_url)

    def login_by_cookie(self):

        with open('../datas/cookie.yml', encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def switch_to_contacts(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # return WeWorkContactsPage()

    def login_to_contacts(self):

        self.open_login_page()
        self.login_by_cookie()
        self.switch_to_contacts()
