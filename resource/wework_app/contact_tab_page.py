# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:通讯录页面封装
"""
from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.base_app_page import BaseAppPage


class ContactTabPage(BaseAppPage):

    __member = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b4l']/*[position()>1]//*[@class='android.widget.TextView']")

    def goto_add_member_page(self, info):

        # self.find(self.__hand_add_member).click()
        self.scroll_to_text(info).click()
        from resource.wework_app.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_contact_member_list(self):

        member_elems = self.finds(self.__member)
        return [member.text for member in member_elems]


