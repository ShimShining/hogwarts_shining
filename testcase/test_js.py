# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/14
Describe:
"""
from selenium.webdriver.common.by import By
from testcase.base import Base
from time import sleep


class TestJs(Base):

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, 'kw').send_keys("selenium测试")
        su_elem =self.driver.execute_script("return document.getElementById('su')")
        su_elem.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[text()="下一页 >"]').click()
        sleep(2)
        for code in [
            "return document.title",
            "return JSON.stringify(performance.timing)"
        ]:
            # code = "return document.title;return JSON.stringify(performance.timing)"
            print(self.driver.execute_script(code))

    def test_change_date(self):

        self.driver.get("https://www.12306.cn/index/")
        js_script = "d=document.getElementById('train_date');d.removeAttribute('readonly');"
        self.driver.execute_script(js_script)
        # 一定要注意设置等待时间,不然页面元素没有加载出来就赋值了,在页面上看页面的值看起来就没被改动
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(3)