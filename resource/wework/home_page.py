# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/19
Describe:
"""
from time import sleep

from selenium.webdriver.common.by import By

from resource.wework.BasePage import BasePage


class HomePage(BasePage):

    __contacts = (By.ID, 'menu_contacts')

    def goto_catact_page(self):

        self.find(self.__contacts).click()
        sleep(2)
        from resource.wework.contact_page import ContactPage
        return ContactPage(self.driver)
