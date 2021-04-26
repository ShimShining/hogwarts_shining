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

    __back_btn = (MobileBy.XPATH, "// *[ @text = '添加成员'] /../../../../*[@class='android.widget.TextView']")
    # __user_name = (MobileBy.ID, "com.tencent.wework:id/ays")
    # __phone_number = (MobileBy.ID, "com.tencent.wework:id/f4m")
    __user_name = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[contains(@text,'必填')]")
    __phone_number = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[contains(@text,'必填')]")
    __save_btn = (MobileBy.ID, "com.tencent.wework:id/ac9")
    __phone_repeat = (MobileBy.XPATH, "//*[@text='手机已存在于通讯录，无法添加']")
    __pop_confirm = (MobileBy.XPATH, "//*[@text='确定']")

    def add_member_and_save(self, name, phone, toast="添加成功"):

        self.wait_for_visible(self.__user_name)
        self.find(self.__user_name).send_keys(name)
        self.find(self.__phone_number).send_keys(phone)
        self.find(self.__save_btn).click()
        self.check_toast_info(toast)
        return AddMemberPage(self.driver)

    def add_member_phone_repeat(self, name, phone):
        self.wait_for_visible(self.__user_name)
        self.find(self.__user_name).send_keys(name)
        self.find(self.__phone_number).send_keys(phone)
        self.find(self.__save_btn).click()
        self.wait_for_visible(self.__phone_repeat)
        self.find(self.__pop_confirm).click()
        return self

    def back_add_member_page(self):

        self.wait_for_visible(self.__back_btn)
        self.find(self.__back_btn).click()
        self.log_info("返回添加成员页")
        return AddMemberPage(self.driver)





