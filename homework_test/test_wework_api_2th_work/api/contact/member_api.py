# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/23
Describe:通讯录接口封装
"""
import allure
from homework_test.test_wework_api_2th_work.api.contact.base_contact import CommonContact


class MemberApi(CommonContact):

    __add_path = "/user/create"
    __get_path = '/user/get'
    __update_path = "/user/update"
    __del_path = "/user/delete"

    def search_member(self, user_id):

        data = {
            "url": self.base_url + self.__get_path,
            "method": "get",
            "params": {
                "access_token": self.token,
                "userid": user_id
            },

        }
        allure.attach(f"读取成员接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"读取成员接口响应为=>{r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def add_member(self, member):
        """
        创建成员
        :return:
        """
        data = {
            "url": self.base_url + self.__add_path,
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": member
        }
        allure.attach(f"添加成员接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"添加成员接口响应为=>{r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def update_member(self, modify_member):

        data = {
            "url": self.base_url + self.__update_path,
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": modify_member
        }
        allure.attach(f"更新成员接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"更新成员接口响应为=>{r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def del_member(self, user_id):

        data = {
            "url": self.base_url + self.__del_path,
            "method": "get",
            "params": {
                "access_token": self.token,
                "userid": user_id
            },

        }
        allure.attach(f"删除成员接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"删除成员接口响应为=>{r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def plan_data(self):

        r = self.add_member({
            "userid": "delete001",
            "name": "删除",
            "mobile": "13944024404",
            "department": [1, 2],
        })
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = self.add_member({
            "userid": "repeat001",
            "name": "重复",
            "mobile": "13944021404",
            "department": [1, 2],
        })
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def clear(self):

        pass

    def clear_data(self):

        user_ids = ["email_exist", "delete001", "shim0526", "shim0527", "repeat001"]
        for user in user_ids:
            r = self.search_member(user)
            if r.json()["errcode"] == 0:
                self.del_member(user)
                self.logger.info(f"删除user_id={user}成功")

