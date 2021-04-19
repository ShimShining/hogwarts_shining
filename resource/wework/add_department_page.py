# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/19
Describe:
"""
from selenium.webdriver.common.by import By
from time import sleep
from resource.wework.BasePage import BasePage
from resource.wework.contact_page import ContactPage


class AddDepartmentPage(BasePage):

    __department_name = (By.CSS_SELECTOR, '.ww_inputText[name="name"]')
    __belong_department = (By.CSS_SELECTOR, '.js_toggle_party_list')
    # __select_depart = (By.CSS_SELECTOR, '.inputDlg_item .jstree-container-ul a.jstree-clicked')
    # __submit = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot a:contains("确定")')
    __submit = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot a.ww_btn_Blue')
    __cancel = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot a.ww_btn_Blue~a')
    __close = (By.CSS_SELECTOR, '.qui_dialog_head.ww_dialog_head .ww_commonImg_CloseDialog')

    def add_department(self, department_name, belong_department):

        self.find(self.__department_name).send_keys(department_name)
        self.find(self.__belong_department).click()
        # path0 = f'.inputDlg_item .jstree-container-ul a:contains("{belong_department}")'
        # path1 ='.inputDlg_item .jstree-container-ul a[id=1688852046068944_anchor]'
        path = '.qui_dialog_body.ww_dialog_body a[id="1688852046068944_anchor"]'
        print(path)
        select_department = (By.CSS_SELECTOR, path)
        print(select_department)
        sleep(3)
        self.find(select_department).click()
        self.find(self.__submit).click()
        sleep(2)
        return ContactPage(self.driver)

    def cancel_add_department(self):

        self.find(self.__cancel).click()
        return ContactPage(self.driver)

    def close_add_department(self):

        self.find(self.__close).click()
        return ContactPage(self.driver)
