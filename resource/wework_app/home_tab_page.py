# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/22
Describe:首页底tab PO
"""
from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.base_app_page import BaseAppPage
from resource.wework_app.contact_tab_page import ContactTabPage


class HomeTabPage(BaseAppPage):

    __contact_tab = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']")

    def enter_contact_tab(self):

        self.find(self.__contact_tab).click()
        self.log_info("进入通讯录底tab")
        return ContactTabPage(self.driver)

