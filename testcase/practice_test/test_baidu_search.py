#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2021-04-09
Describe:demo practice
"""

import allure
from selenium import webdriver
import time
import pytest

driver_path = "D:\softinstall\chrome\chromedriver.exe"
test_url = "https://www.baidu.com"


@allure.testcase("https://www.github.com")
@pytest.mark.parametrize("search_text", ['pytest', 'allure', 'unittest'])
@allure.feature("百度搜索模块")
class TestBaiduSearch:

    def test_baidu_search_content(self, search_text):
        with allure.step("步骤1: 打开浏览器输入百度网址"):
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get(test_url)

        with allure.step(f"步骤2:在搜索栏输入{search_text},并点击百度一下"):
            driver.find_element_by_id("kw").send_keys(search_text)
            time.sleep(2)
            driver.find_element_by_id('su').click()
            time.sleep(5)

        with allure.step("步骤3: 截图保存在项目中"):
            driver.save_screenshot(f"./result/{search_text}.png")
            allure.attach.file(f"./result/{search_text}.png", name=search_text,
                               attachment_type=allure.attachment_type.PNG)
            allure.attach('<head></head><body>百度搜索测试</body>',
                          'Attach Html Type', allure.attachment_type.HTML)

        with allure.step("步骤4: 关闭浏览器,结束测试"):
            driver.quit()


if __name__ == "__main__":
    pytest.main()
