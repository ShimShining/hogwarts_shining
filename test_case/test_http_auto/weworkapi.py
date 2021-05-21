# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/21
Describe:企业微信API封装
"""
import json
from jsonpath import jsonpath
import requests


class WeworkAPI:

    token = None

    def get_token(self):
        r = requests.get(
            " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": "ww47f671844340af6d",
                "corpsecret": "WuusLzIWVr2lqE5umfLZB6wVCk0NsdQReBBV6ONl-hA"
            }
        )
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        self.token = r.json()["access_token"]

    def search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            },
            json={}
        )

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        return r

    def get_tag_id(self, tag_name, group_name):

        r = self.search()
        fliter = f'$..*[?(@.group_name=="{group_name}")].tag[?(@.name=="{tag_name}")].id'
        print(fliter)
        tag_id = jsonpath(r.json(), fliter)
        print("+++++++++++++++++++++")
        return tag_id[0]

    def get_tag_id_by_dict(self, tag_name, group_name):

        # 获取所有的tags
        r = self.search()
        # print(type(r.json()))
        # data = json.loads(r.json(), encoding="utf-8")
        # # 取出所有的tags的group
        # groups = data["tag_group"]
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
                    continue

                else:
                    # 指定的组下无指定的tag,返回None
                    return None

            continue
        else:
            # groups下无指定的group,返回None
            return None

    def add_tag(self, tag_name, group_name):

        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={
                "access_token": self.token
            },
            json={
                "group_name": group_name,
                "tag": [
                    {
                        "name": tag_name
                    }
                ]
            }
        )
        return r

    def edit_tag(self, tag_name, group_name, new_tag_name):

        tag_id = self.get_tag_id(tag_name, group_name)
        if tag_id:
            r = requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                params={
                    "access_token": self.token
                },
                json={
                    "id": tag_id,
                    "name": new_tag_name
                }
            )
            return r
        return None

    def del_tag(self, tag_name, group_name):

        tag_id = self.get_tag_id_by_dict(tag_name, group_name)
        print(tag_id)
        if tag_id is None:
            raise Exception(f"tag_name={tag_name},group_name={group_name}的tag_id={tag_id},删除失败")
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={
                "access_token": self.token
            },
            json={
                "tag_id": [
                    tag_id
                ]
            }
        )
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
        for group in groups:

            if group["group_name"] != "客户等级":
                # 遍历除客户等级的所有标签组
                for tag in group["tag"]:
                    tags.append((tag["name"], group["group_name"]))

        return tags

    def del_all_added_tags(self):

        added_tags = self.get_all_added_tags()
        print('--------------初始化----------------')
        print(added_tags)
        if added_tags:
            for tag in added_tags:
                self.del_tag(*tag)

