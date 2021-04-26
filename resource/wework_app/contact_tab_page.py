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

    def goto_add_member_page(self, info="添加成员"):

        # self.find(self.__hand_add_member).click()
        self.scroll_to_text(info).click()
        from resource.wework_app.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_contact_member_list(self):

        member_elems = self.finds(self.__member)
        return [member.text for member in member_elems]

    def goto_person_info_page_by_name(self, name):

        # member = (MobileBy.XPATH, f"//*[contains(@text,'{name}')]")
        self.scroll_to_text(name).click()
        self.log_info(f"进入{name}的个人信息页")
        # self.wait_for_visible(member)
        # self.find(member).click()
        from resource.wework_app.person_info_page import PersonInfoPage
        return PersonInfoPage(self.driver)

