# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:手动添加成员页面
"""
from appium.webdriver.common.mobileby import MobileBy
from resource.wework_app.base_app_page import BaseAppPage
from resource.wework_app.contact_tab_page import ContactTabPage


class AddMemberPage(BaseAppPage):

    __hand_input_add_member = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    __back_contact = (MobileBy.ID, "com.tencent.wework:id/h86")

    def goto_member_info_input_page(self):

        self.wait_for_visible(self.__hand_input_add_member)
        self.find(self.__hand_input_add_member).click()
        self.log_info("进入添加成员信息输入页")
        from resource.wework_app.member_info_input_page import MemberInfoInputPage
        return MemberInfoInputPage(self.driver)

    def back_conctact_tab_page(self):

        self.wait_for_visible(self.__back_contact)
        self.find(self.__back_contact).click()
        self.log_info("添加成员页返回通讯录底tab")
        return ContactTabPage(self.driver)
