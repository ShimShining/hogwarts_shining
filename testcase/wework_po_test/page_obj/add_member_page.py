# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:企业微信添加成员页面PO
"""
from selenium.webdriver.common.by import By

from testcase.wework_po_test.page_obj.base_page import BasePage, BasePage1


class AddMemberPage(BasePage1):

    # 页面元素不需要暴露给业务用例侧
    __username = (By.ID, "username")
    __accid = (By.ID, "memberAdd_acctid")
    __phone = (By.ID, "memberAdd_phone")
    __save_btn = (By.CSS_SELECTOR, '.js_btn_save')
    # phone_wrong_tips = (By.CSS_SELECTOR, ".ww_inputWithTips_tips:contains('该手机已被')")
    __wrong_tips = (By.CSS_SELECTOR, ".ww_inputWithTips_tips")

    def add_member(self, name, accid, phone):

        self.find(*self.__username).send_keys(name)
        self.find(*self.__accid).send_keys(accid)
        self.find(*self.__phone).send_keys(phone)
        self.find(*self.__save_btn).click()
        # 解决相互导入导致的importerror
        from testcase.wework_po_test.page_obj.contacts_page import ContactsPage
        return ContactsPage(self.driver)

    def add_member_fail(self, name, accid, phone):
        self.find(*self.__username).send_keys(name)
        self.find(*self.__accid).send_keys(accid)
        self.find(*self.__phone).send_keys(phone)
        self.find(*self.__save_btn).click()
        elems = self.finds(*self.__wrong_tips)
        error_list = [ele.text for ele in elems if ele.text]
        # for ele in elems:
        #     error_list.append(ele.text)
        print(error_list)
        return error_list