# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe:日历接口
"""
from homework_test.larkTest.service.api.larkApi import LarkApi


class Calendar(LarkApi):

    # 创建,更新,获取列表和单个,删除的基础path均是同一个,请求的method和参数不同
    __base_path = "/calendar/v4/calendars"
    __subscribe_path = ""
    __unsubscribe_path = ""
    __search_path = ""

    def create(self):
        data = {
            "method": "POST",
            "url": self._base_url + self.__base_path,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": {
                "app_id": "cli_slkdjalasdkjasd",
                "app_secret": "dskLLdkasdjlasdKK"
            }

        }

    def get_lists(self):

        data = {
            "method": "GET",
            "url": self._base_url + self.__base_path
        }
        j = self.lark_request(data)
        return j["data"]["calendar_list"]

    def update(self):

        pass

    def delete(self):

        pass

    def get(self, *args):

        pass

    def subscribe(self):

        pass

    def unsubscribe(self):

        pass

    def delete_all(self):

        pass

