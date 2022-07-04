#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date:
Describe:
"""
import pytest
import allure


@allure.feature("这是登录模块测试用例")
class TestlLogin():
    @allure.story("用户名正确，登录成功")
    @allure.severity(allure.severity_level.BLOCKER)  # 阻塞
    def test_logina(self):
        allure.attach("这是一个纯文本", name="文本信息", attachment_type=allure.attachment_type.TEXT)  # 添加文本
        print("这是登录，用户名正确，登录成功")
        pass

    @allure.story("密码正确，登录成功")
    @allure.severity(allure.severity_level.CRITICAL)  # 严重
    def test_loginb(self):
        allure.attach("<body>这是一个网页</body>", name="HTML测试模块", attachment_type=allure.attachment_type.HTML)  # 添加网页

        print("这是登录，密码正确，登录成功")
        pass

    @allure.story("用户名错误，登录失败")
    # --allure-link-pattern=issue:https://blog.csdn.net/weixin_44275820/article/details/105169871/issue/{}
    @allure.issue("10086", "这是一个bug，需要修复")
    @allure.severity(allure.severity_level.NORMAL)  # 正常问题
    def test_loginc(self):
        allure.attach.file("./picture/微信头像.jpg", name="这是一个图片", attachment_type=allure.attachment_type.JPG)  # 添加图片
        print("这是登录，用户名错误，登录失败")
        pass

    @allure.story("密码错误，登录失败")
    @allure.link("https://blog.csdn.net/article/details/105169871", name="我的博客")
    @allure.severity(allure.severity_level.MINOR)  # 不太重要
    def test_logind(self):
        with allure.step("点击用户名输入框"):
            print("输入用户名")
        with allure.step("点击输入密码输入框"):
            print("输入密码")
        print("点击登录按钮")
        with allure.step("点击登录后登录失败"):
            assert "1" == 1
            print("这是登录，密码错误，登录失败")
        pass

    Testcase_link = "https://blog.csdn.net/weixin_44275820/article/details/105169871"

    @allure.story("用户不存在，登录失败")
    @allure.testcase(Testcase_link, "我的博客管理平台")
    @allure.severity(allure.severity_level.TRIVIAL)  # 不重要
    def test_logine(self):
        print("这是登录，用户不存在，请重新注册")
        pass

    @allure.story("密码已锁定，登录失败")
    def test_loginf(self):
        print("这是登录，密码已锁定，请重置密码")
        pass

    @allure.story("密码为空，登录失败")
    def test_loging(self):
        print("这是登录，密码为空，请输入密码")
        pass


if __name__ == '__main__':
    pytest.main("-v -s")
