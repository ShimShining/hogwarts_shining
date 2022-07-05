# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/24
Describe:添加成员API case
"""
import pytest
import allure
from service.business.contact.member_api import MemberApi


@allure.feature("添加成员模块")
class TestMemberApi:

    def setup_class(self):

        self.member_api = MemberApi()
        self.token = self.member_api.get_token()
        self.member_api.clear_data()
        self.member_api.plan_data()

    def teardown_class(self):

        pass

    @allure.story("添加接口")
    @pytest.mark.run(order=1)
    def test_add_member_success(self, get_member_data):

        r = self.member_api.add_member(get_member_data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = self.member_api.search_member(get_member_data["userid"])
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        assert get_member_data["name"] == r.json()["name"]
        assert get_member_data["mobile"] == r.json()["mobile"]

    @allure.story("添加接口")
    def test_add_member_mobile_miss_email_exist(self):
        data = {
            "userid": "email_exist",
            "name": "重复",
            "email": "email_exist@test.com",
            "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = self.member_api.search_member(data["userid"])
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        assert data["name"] == r.json()["name"]
        assert data["email"] == r.json()["email"]
        assert r.json()["mobile"] is ""

    @allure.story("添加接口")
    @pytest.mark.run(order=2)
    # todo 异常场景用例可以使用数据驱动
    def test_add_member_name_repeat(self):
        data = {
                "userid": "repeat001",
                "name": "重复",
                "mobile": "13944021401",
                "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60102

    @allure.story("添加接口")
    def test_add_member_userid_miss(self):

        data = {
            "name": "用户id缺失",
            "mobile": "13940021401",
            "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 41009

    @allure.story("添加接口")
    def test_add_member_name_miss(self):
        data = {
                "userid": "name_miss001",
                "mobile": "13940021401",
                "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60112

    @allure.story("添加接口")
    def test_add_member_mobile_miss(self):
        data = {
                "userid": "mobile_miss",
                "name": "momiss",
                "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60129

    @allure.story("添加接口")
    def test_add_member_depart_miss(self):
        data = {
                "userid": "mobile_miss",
                "name": "departmiss",
                "mobile": "13500401414"
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 40066

    def test_add_member_all_miss(self):
        data = {}

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60112

    @allure.story("添加接口")
    def test_add_member_all_empty(self):
        data = {
                "userid": "",
                "name": "",
                "mobile": "",
                "department": [],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 40058

    @allure.story("添加接口")
    def test_add_member_name_empty(self):
        data = {
                "userid": "user_id",
                "name": "",
                "mobile": "13825844404",
                "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 40058


    @allure.story("添加接口")
    def test_add_member_mobile_empty(self):
        data = {
                "userid": "user_id",
                "name": "myshiy",
                "mobile": "",
                "department": [1, 2],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60129

    @allure.story("添加接口")
    def test_add_member_depart_empty(self):
        data = {
                "userid": "user_id001",
                "name": "user001",
                "mobile": "13525854404",
                "department": [],
        }

        r = self.member_api.add_member(data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 40066

    @pytest.mark.parametrize("user_id", [
        "delete001"
    ])
    @allure.story("删除接口")
    def test_del_member(self, user_id):

        r = self.member_api.del_member(user_id)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = self.member_api.search_member(user_id)
        assert r.status_code == 200
        assert r.json()["errcode"] == 60111











