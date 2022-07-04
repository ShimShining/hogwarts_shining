# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/23
Describe:
"""
from aha_test.test_wework_api.api.base_api import BaseApi
import allure


class WeworkApi(BaseApi):

    token = None
    base_url = "https://qyapi.weixin.qq.com/cgi-bin"
    token_url = base_url + "/gettoken"

    def get_token(self):

        data = {
            "method": "get",
            "url": self.token_url,
            "params": {
                "corpid": "ww47f671844340af6d",
                "corpsecret": "WuusLzIWVr2lqE5umfLZB6wVCk0NsdQReBBV6ONl-hA"
            }

        }

        r = self.request(data)
        assert r.status_code == 200
        allure.attach(f"获取token接口响应结果为=>{r.json()}", attachment_type=allure.attachment_type.TEXT)
        self.token = r.json()["access_token"]
        allure.attach(f"获取token值为=>{self.token}", attachment_type=allure.attachment_type.TEXT)
        self.logger.info(f"获取token成功,token={self.token}")

