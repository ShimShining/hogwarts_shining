# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/26
Describe:个人信息页
"""
from appium.webdriver.common.mobileby import MobileBy

from resource.wework_app.base_app_page import BaseAppPage


class PersonInfoPage(BaseAppPage):

    __setting_btn = (MobileBy.XPATH, "//*[@resource-id='android:id/content']/*/*[1]/*[2]")

    def goto_person_info_setting_page(self):

        self.wait_for_visible(self.__setting_btn)
        self.find(self.__setting_btn).click()
        self.log_info("进入个人信息设置页面")
        from resource.wework_app.person_info_setting_page import PersonInfoSettingPage
        return PersonInfoSettingPage(self.driver)

    def back_cantact_tab_page(self):

        pass