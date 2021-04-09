#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""

import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Switch模块")
class TestSwitch:

    def test_switch_right(self):
        print("Switch:  == Right")

    def test_switch_left(self):
        print("Switch:  == Left")


@allure.feature("Login 模块")
class TestLogin:

    @allure.title("用户名密码正确-登录成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("Loop1:=="):
            print("Login:  == 1")
        with allure.step("Loop2:=="):
            print("Login:  == 2")
        with allure.step("Loop3:=="):
            print("Login:  == Success")

    @allure.title("用户名密码错误-登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录失败")
    def test_login_fail(self):
        print("Login:  == Fail")

    @allure.story("用户名为空")
    def test_login_username_empty(self):
        print("Login:  == Username Empty")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("登录密码错误")
    def test_login_pwd_wrong(self):
        print("Login:  == Pwd Wrong")

    @allure.story("登录验证码错误")
    def test_login_verity_code_wrong(self):
        print("Login:  == Verity Code Wrong")


if __name__ == "__main__":
    pytest.main()
