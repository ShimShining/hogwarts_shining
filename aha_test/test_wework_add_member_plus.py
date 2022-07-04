# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/24
Describe:
1、添加联系人测试用例 实现PO封装
2、删除联系人用例 实现PO封装
3、将日志 保存到日志文件中，打印输出日志时间
"""
import os
import time

import pytest

from resource.utils.log import Logger
from resource.wework_app.app import App


class TestAddMember:

    def setup_class(self):

        self.app = App()

    def setup(self):
        # 启动app
        self.home = self.app.start().goto_main()

    def teardown(self):
        # 单条case重启app
        self.app.restart()

    def teardown_class(self):
        # kill driver
        self.app.stop()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone", [
        ["lao tie06", '13444044424']
    ])
    def test_add_member_success(self, name, phone):

        merbers = self.home.enter_contact_tab().\
            goto_add_member_page().\
            goto_member_info_input_page().\
            add_member_and_save(name, phone).\
            back_conctact_tab_page().\
            get_contact_member_list()

        assert name in merbers

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone", [
        ["lao tie00", '13444044424']
    ])
    def test_add_member_fail(self, name, phone):

        after_members = self.home.enter_contact_tab().\
            goto_add_member_page().\
            goto_member_info_input_page().\
            add_member_phone_repeat(name, phone).\
            back_add_member_page().back_conctact_tab_page().\
            get_contact_member_list()

        assert name not in after_members

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("name", [
        "lao tie06"
    ])
    def test_delete_member_success(self, name):

        members = self.home.enter_contact_tab().\
            goto_person_info_page_by_name(name).\
            goto_person_info_setting_page().\
            goto_edit_member_page().delete_member().\
            get_contact_member_list()

        assert name not in members

