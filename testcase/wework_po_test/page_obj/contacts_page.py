# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:企业微信通讯录界面封装
"""
from selenium.webdriver.common.by import By

from testcase.wework_po_test.page_obj.base_page import BasePage, BasePage1


class ContactsPage(BasePage1):

    def goto_add_member_page(self):
        from testcase.wework_po_test.page_obj.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_contacts_list(self):
        member_list = []
        element_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        print(element_list)
        for elem in element_list:
            member_list.append(elem.text)
        print(member_list)
        return member_list

