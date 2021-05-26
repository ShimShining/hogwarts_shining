# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/24
Describe:客户标签API po封装
"""
from jsonpath import jsonpath
from homework_test.test_wework_api_2th_work.api.wework_api import WeworkApi
import allure


class TagApi(WeworkApi):

    __add_path = "/externalcontact/add_corp_tag"
    __edit_path = "/externalcontact/edit_corp_tag"
    __search_path = "/externalcontact/get_corp_tag_list"
    __delete_path = "/externalcontact/del_corp_tag"

    def search(self):

        data = {
            "method": "post",
            "url": self.base_url + self.__search_path,
            "params": {
                "access_token": self.token
            },
            "json": {}
        }
        allure.attach(f"查询接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"查询接口响应结果为<={r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def get_tag_id(self, group_name, tag_name):

        r = self.search()
        fliter = f'$..*[?(@.group_name=="{group_name}")].tag[?(@.name=="{tag_name}")].id'
        self.logger.info(f"fliter={fliter}")
        tag_id = jsonpath(r.json(), fliter)
        self.logger.info("+++++++++++++++++++++")
        return tag_id[0]

    def get_tag_id_by_dict(self, group_name, tag_name):

        # 获取所有的tags
        r = self.search()
        # r.json()的数据类型已经是dict
        groups = r.json()["tag_group"]
        # 遍历groups列表
        for group in groups:

            if group["group_name"] == group_name:
                # 如果group_name相等,则进入遍历该group下的所有tags
                for tag in group["tag"]:
                    # tag的name=要查找的tag,返回其id
                    if tag["name"] == tag_name:
                        return tag["id"]
                else:
                    # 指定的组下无指定的tag,返回None
                    return None
        else:
            # groups下无指定的group,返回None
            return None

    def get_tags_order(self):

        # 获取所有的tags
        r = self.search()
        # r.json()的数据类型已经是dict
        groups = r.json()["tag_group"]

        orders = [(group["group_name"], tag["name"], tag["order"])for group in groups for tag in group["tag"]]
        self.logger.info(orders)
        return orders

    def add_tag(self, group_name, tag_name):

        data = {
            "method": "post",
            "url":  self.base_url + self.__add_path,
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": group_name,
                "tag": [
                    {
                        "name": tag_name
                    }
                ]
            }
        }
        allure.attach(f"添加接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"添加接口响应结果为<={r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def add_tags(self, group_name, tag_list=None):
        """
        添加标签组
        :param group_name: 可能是json==>{"group_name": "ngname","tag": [
        {"name": "tag_name", "oreder": 1}]};也可能是group_name
        :param tag_list:
        :return: 添加标签组后的response
        """
        if tag_list is None:

            data = {
                "method": "post",
                "url": self.base_url + self.__add_path,
                "params": {
                    "access_token": self.token
                },
                "json": group_name
            }
        else:
            data = {
                "method": "post",
                "url": self.base_url + self.__add_path,
                "params": {
                    "access_token": self.token
                },
                "json": {
                    "group_name": group_name,
                    "tag": tag_list
                }
            }
        self.logger.info(f"请求data={data}")
        allure.attach(f"添加接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"添加接口响应结果为<={r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def edit_tag(self, group_name, tag_name, new_tag_name):

        tag_id = self.get_tag_id(group_name, tag_name)
        if tag_id:
            data = {
                "method": "post",
                "url": self.base_url + self.__edit_path,
                "params": {
                    "access_token": self.token
                },
                "json": {
                    "id": tag_id,
                    "name": new_tag_name
                }
            }
            allure.attach(f"修改接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
            r = self.request(data)
            allure.attach(f"添加接口响应结果为<={r.json()}", attachment_type=allure.attachment_type.JSON)
            return r
        allure.attach(f"添加接口响应结果为<=None", attachment_type=allure.attachment_type.JSON)
        return None

    def del_tag(self, group_name, tag_name):

        tag_id = self.get_tag_id_by_dict(group_name, tag_name)
        self.logger.info(f"准备删除的标签tag_id={tag_id}")
        if tag_id is None:
            self.logger.info(f"准备删除的标签tag_id=None,抛出异常")
            raise Exception(f"group_name={group_name},tag_name={tag_name}的tag_id={tag_id},删除失败")
        data = {
            "method": "post",
            "url": self.base_url + self.__delete_path,
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        allure.attach(f"删除接口请求数据为=>{data}", attachment_type=allure.attachment_type.JSON)
        r = self.request(data)
        allure.attach(f"删除接口响应结果为<={r.json()}", attachment_type=allure.attachment_type.JSON)
        return r

    def get_all_added_tags(self):
        """
        返回所有标签组名和tag名
        :return: (group_name, tag_name)
        """
        r = self.search()
        tags = []
        groups = r.json()["tag_group"]
        # 遍历groups列表
        # return [ (group["group_name"], tag["name"]) for group in groups
        # if group["group_name"] != "客户等级" for tag in group["tag"]]
        for group in groups:
            if group["group_name"] != "客户等级":
                # 遍历除客户等级的所有标签组
                for tag in group["tag"]:
                    tags.append((group["group_name"], tag["name"]))
        allure.attach(f"获取所有的添加标签为<={tags}", attachment_type=allure.attachment_type.TEXT)
        return tags

    def del_all_added_tags(self):

        added_tags = self.get_all_added_tags()
        self.logger.info('--------------初始化----------------')
        self.logger.info(added_tags)
        if added_tags:
            for tag in added_tags:
                self.del_tag(*tag)

    def prepare_data(self):

        self.add_tag("删除标签组", "你删除我试试")
        self.add_tag("编辑标签组", "编辑tag1")

    def clear_data(self):

        self.logger.info("----------开始清理数据----------")
        self.del_all_added_tags()
        self.logger.info("----------删除成功--------------")

    def clear(self):

        r = self.search()

        tag_id_list = [tag["id"] for group in r.json()["tag_group"] for tag in group["tag"]]
        r = self.del_tags(tag_id_list)
        allure.attach(f"clear环境后的响应结果为<={r.json()}", attachment_type=allure.attachment_type.TEXT)
        return r

