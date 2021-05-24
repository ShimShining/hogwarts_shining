# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/23
Describe:api 自动化基类
"""
import requests


class BaseApi:

    def request(self, request: dict):

        if request.get("protocol") == "rpc":
            return self.rpc_request(**request)

        if request.get("protocol") == "tcp":
            return self.tcp_request(**request)

        return self.http_request(**request)

    def http_request(self, request):

        return requests.request(**request)

    def rpc_request(self, request):

        pass

    def tcp_request(self, request):

        pass

