# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from testcase.base import Base


class TestFrame(Base):

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(3)
    #     self.driver.maximize_window()
    #
    # # def teardown(self):
    # #     self.driver.quit()

    def test_window(self):

        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        # self.driver.switch_to_window(windows[-1])
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("user_name")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("13800010001")
        sleep(3)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys("username")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('11111')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

    def test_frame(self):

        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'droppable').text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)