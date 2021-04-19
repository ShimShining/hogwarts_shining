# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/19
Describe:使用po思想完成添加部门操作的自动化测试（注意组合定位）
"""
from time import sleep

from resource.wework.home_page import HomePage


class TestAddDepartment:

    def setup(self):

        self.home = HomePage()

    def test_add_department(self, get_depart):

        exist_departments = self.home.goto_catact_page().enter_add_department_page().\
            add_department(get_depart[0], get_depart[1]).get_department_list()

        assert get_depart[0] in exist_departments

    def test_cancel_add_department(self):

        contact = self.home.goto_catact_page()
        before_departments = contact.get_department_list()
        after_departments = contact.enter_add_department_page().\
            cancel_add_department().get_department_list()

        assert before_departments == after_departments

    def test_close_add_department(self):

        contact = self.home.goto_catact_page()
        before_departments = contact.get_department_list()
        after_departments = contact.enter_add_department_page().\
            close_add_department().get_department_list()

        assert before_departments == after_departments

    def teardown(self):

        self.home.kill_env()


