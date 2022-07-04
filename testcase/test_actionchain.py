# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionchain:

    def setup(self):
        self.driver = webdriver.Chrome()
        # self.url = "http://sahitest.com/demo/clicks.htm"
        # self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_actionchain(self):

        self.driver.get("http://sahitest.com/demo/clicks.htm")
        click_element = self.driver.find_element(By.CSS_SELECTOR, '[value="click me"]')
        double_element = self.driver.find_element(By.CSS_SELECTOR, '[value="dbl click me"]')
        right_element = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(click_element)
        action.double_click(double_element)
        action.context_click(right_element)
        sleep(3)
        action.perform()
        sleep(3)

    def test_moveto(self):

        self.driver.get("https://www.baidu.com")
        sleep(3)
        elem = self.driver.find_element(By.ID, "s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(elem)
        action.perform()
        sleep(5)

    def test_dragdrop(self):

        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_elem = self.driver.find_element(By.ID, 'dragger')
        drop_elem = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_elem, drop_elem).perform()
        # action.click_and_hold(drag_elem).release(drop_elem).perform()
        action.click_and_hold(drag_elem).move_to_element(drop_elem).release().perform()
        sleep(4)

    def test_keys(self):

        self.driver.get("http://sahitest.com/demo/label.htm")
        elem = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        elem.click()
        action = ActionChains(self.driver)

        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("Shining").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


