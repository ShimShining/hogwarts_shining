# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from test_case.base import Base


class TestFile(Base):

    def test_image_upload(self):
        """
        百度图片,点击本地上传后,上传本地图片
        :return:
        """
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, '.st_camera_off').click()
        self.driver.find_element(By.ID, 'stfile').send_keys("D:\personProc\hogwarts_shining\datas\微信图片_20210412191202.png")
        sleep(3)

    def test_alert(self):
        """
        弹框点击确定
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        elem1 = self.driver.find_element(By.ID, 'draggable')
        elem2 = self.driver.find_element(By.ID, 'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(elem1, elem2).perform()
        sleep(3)
        print('点击alert弹框确定')
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, 'submitBTN')
        sleep(5)