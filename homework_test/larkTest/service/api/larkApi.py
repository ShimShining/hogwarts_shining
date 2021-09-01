# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe: 飞书基础API
"""
from homework_test.larkTest.read_config import ReadConfig
from homework_test.larkTest.service.api.api import Api


class LarkApi(Api):

    _base_url = ReadConfig.get_lark_api_base_url()
    __token_path = "/auth/v3/tenant_access_token/internal"

    def __init__(self):

        super().__init__()
        self.token = None
        self.app_id = "cli_a1a5914d54f99013"
        self.app_secret = "anOniQndOyvmODm3FRN3jd17wfIUOOPx"

    def get_token(self):

        if self.token:
            self.logger.info(f"使用已有token={self.token}")
            return self.token

        data = {
            "method": "POST",
            "url": self._base_url + self.__token_path,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": {
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }

        }
        j = self.request(data)
        assert j["code"] == 0
        self.logger.info(f"第一次获取token成功,token={j['tenant_access_token']}")
        return j["tenant_access_token"]

    def lark_request(self, request):

        if not request.get('headers'):
            request["headers"] = {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {self.get_token()}"
            }
            self.logger.info(f"headers添加成功")

        j = self.request(request)
        return j

