# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:企业微信首页PO封装
"""
from selenium.webdriver.common.by import By

from test_case.wework_po_test.page_obj.add_member_page import AddMemberPage
from test_case.wework_po_test.page_obj.base_page import BasePage, BasePage1
from test_case.wework_po_test.page_obj.contacts_page import ContactsPage


class HomePage(BasePage1):

    def goto_contacts_page(self):
        print("进入Contacts页面")

        return ContactsPage(self.driver)

    def goto_add_member_page(self):

        # self.driver.find_element_by_id()
        self.find(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)


