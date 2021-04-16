# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/13
Describe:
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.url = "https://ceshiren.com/"
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):

        self.driver.find_element(By.XPATH, '//*[@id="ember37"]').click()
        print("wait")
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[text()="最新" and @class="table-heading"]')) >= 1

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))

        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        sleep(5)
        print("DONE")