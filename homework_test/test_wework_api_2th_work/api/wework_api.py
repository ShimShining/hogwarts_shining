# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/23
Describe:
"""
from homework_test.test_wework_api_2th_work.api.base_api import BaseApi


class WeworkApi(BaseApi):

    token = None
    base_url = "https://qyapi.weixin.qq.com/cgi-bin"

    def get_token(self):

        data = {
            "method": "get",
            "url": self.base_url + "/gettoken",
            "params": {
                "corpid": "ww47f671844340af6d",
                "corpsecret": "WuusLzIWVr2lqE5umfLZB6wVCk0NsdQReBBV6ONl-hA"
            }

        }

        r = self.request(data)
        assert r.status_code == 200
        self.token = r.json()["access_token"]
        self.logger.info(f"获取token成功,token={self.token}")

