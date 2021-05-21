# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/21
Describe:企业微信API自动化测试
"""
import json

import requests


class TestWeworkAPI:

    def setup_class(self):

        r = requests.get(
            " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": "ww47f671844340af6d",
                "corpsecret": "WuusLzIWVr2lqE5umfLZB6wVCk0NsdQReBBV6ONl-hA"
            }
        )
        assert r.status_code == 200
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        self.token = r.json()["access_token"]

    def test_get_token(self):

        r = requests.get(
            " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": "ww47f671844340af6d",
                "corpsecret": "WuusLzIWVr2lqE5umfLZB6wVCk0NsdQReBBV6ONl-hA"
            }
        )
        assert r.status_code == 200
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        print(r.json()["access_token"])

    def test_search_tag(self):

        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            },
            json={}
        )

        assert r.status_code == 200

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.json()["errcode"] == 0

    def test_add_tags(self):

        # 测试数据的唯一性,1.提前清理数据;2.使用时间戳代表唯一性
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={
                "access_token": self.token
            },
            json={
                    "group_name": "shining",
                    "tag": [
                        {
                            "name": "tag_521001"
                        }
                    ]
            }
        )

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            },
            json={}
        )

        assert r.status_code == 200

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.json()["errcode"] == 0

    def test_del_tag(self):

        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={
                "access_token": self.token
            },
            json={
                "tag_id": [
                    "etkb_0EAAA9MVTioEybcu_853NCO8oKA"
                ]
            }
        )

        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            },
            json={}
        )

        assert r.status_code == 200

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.json()["errcode"] == 0




