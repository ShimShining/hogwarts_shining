# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/17
Describe:
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_get_crypto():

    driver = webdriver.Chrome()
    s_url = "https://www.baidu.com"
    kw = "https://www.crypto.com"
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(s_url)
    driver.find_element(By.ID, "kw").send_keys(kw)
    driver.find_element(By.ID, "su").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@class='result c-container new-pmd'][1]//*[@class='t c-title-en']").click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    print(windows)
    time.sleep(20)

    elem = driver.find_element(By.XPATH, "//*[@class='css-123aog3']")

    assert elem is not None

