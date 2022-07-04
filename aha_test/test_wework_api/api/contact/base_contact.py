# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/26
Describe:通讯录基础封装
"""
import allure
from aha_test.test_wework_api.api.wework_api import WeworkApi


class CommonContact(WeworkApi):

    def get_token(self):
        data = {
            "method": "get",
            "url": self.token_url,
            "params": {
                "corpid": "ww47f671844340af6d",
                "corpsecret": "eNQQ7BRH5K05NlB6vl55gTg_T5ZqC4IgM9OSRR2Z99Q"
            }

        }

        r = self.request(data)
        assert r.status_code == 200
        allure.attach(f"获取token接口响应结果为=>{r.json()}", attachment_type=allure.attachment_type.TEXT)
        self.token = r.json()["access_token"]
        allure.attach(f"获取token值为=>{self.token}", attachment_type=allure.attachment_type.TEXT)
        self.logger.info(f"获取token成功,token={self.token}")

