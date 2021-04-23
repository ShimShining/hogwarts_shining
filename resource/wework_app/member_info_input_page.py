# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/23
Describe:
"""
from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.add_member_page import AddMemberPage
from resource.wework_app.base_app_page import BaseAppPage


class MemberInfoInputPage(BaseAppPage):

    __user_name = (MobileBy.ID, "com.tencent.wework:id/ays")
    __phone_number = (MobileBy.ID, "com.tencent.wework:id/f4m")
    __save_btn = (MobileBy.ID, "com.tencent.wework:id/ac9")

    def add_member_and_save(self, name, phone, toast):

        self.wait_for_visible(self.__user_name)
        self.find(self.__user_name).send_keys(name)
        self.find(self.__phone_number).send_keys(phone)
        self.find(self.__save_btn).click()
        self.check_toast_info(toast)
        return AddMemberPage(self.driver)
