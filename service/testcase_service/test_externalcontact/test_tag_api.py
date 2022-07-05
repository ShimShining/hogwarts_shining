# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/24
Describe:
"""


import pytest
import allure
from service.business.externalcontact.tag_api import TagApi


@allure.feature("客户管理-客户标签接口功能")
class TestTagApi:

    def setup_class(self):

        self.tag_api = TagApi()
        self.tag_api.get_token()
        # 清理环境数据
        self.tag_api.clear_data()
        # 准备环境数据
        self.tag_api.prepare_data()

    def teardown_class(self):
        # 清理环境数据
        self.tag_api.clear_data()

    @allure.story("查询接口")
    @pytest.mark.run(order=3)
    def test_search_tag(self):
        r = self.tag_api.search()

        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        assert len(r.json()["tag_group"]) > 0

    @allure.story("标签添加接口")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("group_name,tag_name", [
        ["shimmer", "tag_001"],
        ["shimmer", "tag_002"],
        ["盲仔", "tag_001"],
        ["信用", "优秀"],
        ["信用", "差"]
    ])
    def test_add_tag(self, group_name, tag_name):
        r = self.tag_api.add_tag(group_name, tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.tag_api.get_tag_id_by_dict(group_name, tag_name)
        assert tag_id is not None

    @allure.story("查询接口")
    def test_add_tags_json(self, get_tags_json):

        self.tag_api.logger.info(f"gettags={get_tags_json}")
        json_data = get_tags_json
        self.tag_api.logger.info(f"json_data={json_data}")
        r = self.tag_api.add_tags(json_data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group_tags = self.tag_api.get_all_added_tags()
        g_tags = [(json_data["group_name"], tag["name"]) for tag in json_data["tag"]]
        assert set(g_tags).issubset(set(group_tags))

    @allure.story("标签添加接口")
    def test_add_tags(self, get_tags):

        self.tag_api.logger.info(f"gettags={get_tags}")
        group_name, tag_list = get_tags
        self.tag_api.logger.info(f"group_name={group_name},tag_list={tag_list}")
        r = self.tag_api.add_tags(group_name, tag_list)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group_tags = self.tag_api.get_all_added_tags()
        g_tags = [(group_name, tag["name"]) for tag in tag_list]
        assert set(g_tags).issubset(set(group_tags))

    @allure.story("标签添加接口")
    def test_add_tags_order(self, get_tags_order):

        group_name, tag_list = get_tags_order
        r = self.tag_api.add_tags(group_name, tag_list)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        all_orders = self.tag_api.get_tags_order()
        tag_orders = [(group_name, tag["name"], tag["order"]) for tag in tag_list]
        assert set(tag_orders).issubset(set(all_orders))

    @allure.story("标签删除接口")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("group_name,tag_name", [
        ["删除标签组", "你删除我试试"]
    ])
    def test_del_tag(self, group_name, tag_name):

        r = self.tag_api.del_tag(group_name, tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.tag_api.get_tag_id_by_dict(group_name, tag_name)
        tags = self.tag_api.get_all_added_tags()
        assert (group_name, tag_name) not in tags
        assert tag_id is None

    @allure.story("标签修改接口")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("group_name,tag_name,new_tag_name", [
        ["编辑标签组", "编辑tag1", "modify_tag001"]
    ])
    def test_edit_tag(self, group_name, tag_name, new_tag_name):
        r = self.tag_api.edit_tag(group_name, tag_name, new_tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        tag_id = self.tag_api.get_tag_id_by_dict(group_name, new_tag_name)
        assert tag_id is not None

    @allure.story("接口全流程")
    @pytest.mark.parametrize("group_name,tag_name,new_tag_name", [
        ["flow", "flow_tags", "flow_modify"]
    ])
    def test_add_edit_del_flow(self, group_name, tag_name, new_tag_name):

        # 新增
        r = self.tag_api.add_tag(group_name, tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        # 修改
        r = self.tag_api.edit_tag(group_name, tag_name, new_tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        # 查询
        tag_id = self.tag_api.get_tag_id_by_dict(group_name, new_tag_name)
        assert tag_id is not None
        # 删除
        r = self.tag_api.del_tag(group_name, new_tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        tags = self.tag_api.get_all_added_tags()
        assert (group_name, new_tag_name) not in tags
        assert (group_name, tag_name) not in tags
