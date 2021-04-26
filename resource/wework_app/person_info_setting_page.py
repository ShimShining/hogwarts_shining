# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/26
Describe:个人信息设置页面(点击右上角三个点进入)
"""
from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.base_app_page import BaseAppPage
from resource.wework_app.edit_member_page import EditMemberPage
from resource.wework_app.person_info_page import PersonInfoPage


class PersonInfoSettingPage(BaseAppPage):

    __edit_member = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def goto_edit_member_page(self):

        self.wait_for_visible(self.__edit_member)
        self.find(self.__edit_member).click()
        self.log_info("进入编辑成员页")
        return EditMemberPage(self.driver)

    def back_person_info_page(self):

        self.find().click()
        return PersonInfoPage(self.driver)

