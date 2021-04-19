# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/19
Describe:
"""
from selenium.webdriver.common.by import By
from resource.wework.BasePage import BasePage


class ContactPage(BasePage):

    __add_btn = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    __add_department = (By.CSS_SELECTOR, '.js_create_party')
    __departments = (By.CSS_SELECTOR, '.member_colLeft .jstree-default a')

    def enter_add_department_page(self):

        self.find(self.__add_btn).click()
        self.find(self.__add_department).click()
        from resource.wework.add_department_page import AddDepartmentPage
        return AddDepartmentPage(self.driver)

    def get_department_list(self):

        department_list = []
        elem_list = self.finds(*self.__departments)
        for elem in elem_list:
            department_list.append(elem.text)
        print(department_list)
        return department_list

