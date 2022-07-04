# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestFormOpt:

    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.ID, 'user_login').send_keys("123")
        self.driver.find_element(By.ID, 'user_password').send_keys('password')
        self.driver.find_element(By.CSS_SELECTOR, '[for=user_remember_me]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name=commit]').click()
        sleep(5)


