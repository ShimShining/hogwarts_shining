# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:基础页面封装
"""


from selenium import webdriver
import yaml


def singleton(cls):

    _instance = {}

    def _singleton(*args, **kwargs):

        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]


class SingleDriver:
    """
    单例实例化driver
    """
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            cls.driver = webdriver.Chrome(options=option)
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            login_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?"
            cls.driver.get(login_url)
            with open('../../../datas/cookie.yml', encoding='utf-8') as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    cls.driver.add_cookie(cookie)
            print("cookie登录成功")
            cls.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        return cls.driver


class BasePage:

    def __init__(self):

        self.driver = SingleDriver().get_driver()


class BasePage1:

    def __init__(self, origin_driver=None):

        if origin_driver is None:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            login_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?"
            self.driver.get(login_url)
            with open('../../../datas/cookie.yml', encoding='utf-8') as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            print("cookie登录成功")
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = origin_driver

    def find(self, by, elem=None):

        if elem:
            return self.driver.find_element(by, elem)

        return self.driver.find_element(*by)

    def finds(self, by, elem=None):

        if elem:
            return self.driver.find_elements(by, elem)

        return self.driver.find_elements(*by)


