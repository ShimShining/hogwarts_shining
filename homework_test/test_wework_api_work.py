# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/21
Describe:
完成客户标签管理，新增、删除、修改
数据清理
数据驱动用例
"""

import pytest
from test_case.test_http_auto.weworkapi import WeworkAPI


class TestWeworkAPIPO:

    def setup_class(self):

        self.wework = WeworkAPI()
        self.wework.get_token()
        self.wework.del_all_added_tags()

    def teardown_class(self):
        self.wework.del_all_added_tags()

    @pytest.mark.run(order=3)
    def test_search_tag(self):
        r = self.wework.search()

        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("tag_name,group_name", [
        ["tag_001", "shimmer"],
        ["tag_002", "shimmer"],
        ["tag_001", "盲仔"],
        ["优秀", "信用"],
        ["差", "信用"]
    ])
    def test_add_tags(self, tag_name, group_name):
        r = self.wework.add_tag(tag_name, group_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.wework.get_tag_id_by_dict(tag_name, group_name)
        assert tag_id is not None

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("tag_name,group_name", [
        ["modify_tag001", "shimmer"]
    ])
    def test_del_tag(self, tag_name, group_name):
        r = self.wework.del_tag(tag_name, group_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.wework.get_tag_id_by_dict(tag_name, group_name)
        tags = self.wework.get_all_added_tags()
        assert (tag_name, group_name) not in tags
        assert tag_id is None

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("tag_name,group_name,new_tag_name", [
        ['tag_001', "shimmer", "modify_tag001"]
    ])
    def test_edit_tag(self, tag_name, group_name, new_tag_name):
        r = self.wework.edit_tag(tag_name, group_name, new_tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.wework.get_tag_id_by_dict(new_tag_name, group_name)
        assert tag_id is not None


