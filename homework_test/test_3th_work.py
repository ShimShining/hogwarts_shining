# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/16
Describe:使用序列化cookie的方式登录企业微信，完成添加成员操作
"""
from selenium import webdriver
import yaml
from resource.wework import WeworkLogin
from resource.wework import WeWorkContactsPage
from time import sleep

from test_case.base import Base


class TestGetCookies:
    """
    复用浏览器获取cookie
    """
    def test_get_cookie(self):

        opt = webdriver.ChromeOptions()
        # 设置debug地址,等于--remote-debugging-port设置的值
        opt.debugger_address = "127.0.0.1:9777"
        # 实例化Chrome并添加选项
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("menu_contacts").click()

        cookie = self.driver.get_cookies()
        with open('../datas/cookie.yml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)


class TestWeWorkAddMember(Base):

    def test_add_member(self, get_member_info):

        login = WeworkLogin()
        login.login_to_contacts()
        sleep(3)
        contact = WeWorkContactsPage(get_member_info)
        # 点击添加成员按钮
        contact.enter_add_member_page_by_top()
        sleep(3)
        # 输入基础信息
        contact.input_member_base_info()
        sleep(2)
        # 选择性别
        contact.select_gender()
        sleep(1)
        # 输入手机号,email
        contact.input_phone_and_email()
        sleep(2)
        # 向下滑动
        contact.scroll_down()
        # 修改或选择部门
        contact.modify_department()
        sleep(1)
        # 输入职务
        contact.input_job()
        sleep(3)
        #  选择身份
        contact.select_identity()

        # 选择对外信息
        contact.select_position()
        sleep(1)
        # 选择是否发送邀请
        contact.select_send_invitation()
        # 点击底部保存按钮
        contact.save_by_bottom()
        # sleep(1)
        contact.assert_save_tips_success()
        sleep(5)
        # 可以考虑校验[保存成功]的弹窗
        # 次数校验添加成功后的值
        contact.assert_save_success()




