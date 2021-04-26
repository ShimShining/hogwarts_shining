# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/26
Describe:编辑成员页
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.base_app_page import BaseAppPage
from resource.wework_app.contact_tab_page import ContactTabPage


class EditMemberPage(BaseAppPage):

    __delete_member_btn = (MobileBy.XPATH, "//*[@text='删除成员']")
    __del_tips = (MobileBy.XPATH, "//*[contains(@text,'记录将被完全清除')]")
    __del_confirm = (MobileBy.XPATH, "//*[contains(@text,'确定')]")

    def delete_member(self):

        self.scroll_to_text("删除成员").click()
        self.find(self.__del_tips)
        self.find(self.__del_confirm).click()
        self.log_info("删除成员->点击确定按钮")
        sleep(3)

        return ContactTabPage(self.driver)

