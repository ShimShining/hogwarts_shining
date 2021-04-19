# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:企业微信添加成员case
"""
import logging
import pytest
from test_case.wework_po_test.page_obj.home_page import HomePage
from time import sleep


class TestWeworkAddMember:

    def setup(self):

        self.home = HomePage()

    # 测试数据与页面操作抽离
    @pytest.mark.parametrize("name,accid,phone", [('ez', '0090', '13144440000')])
    def test_add_member(self, name, accid, phone):

        member = self.home.goto_add_member_page().add_member(name, accid, phone).get_contacts_list()
        assert name in member
        sleep(10)

    @pytest.mark.parametrize("name,accid,phone", [('ez', '0092', '13144440000')])
    def test_add_member_fail(self, name, accid, phone):

        error = self.home.goto_add_member_page().add_member_fail(name, accid, phone)
        assert '该手机号已被“ez”占有' in error


