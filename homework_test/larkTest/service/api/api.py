# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe:接口测试基类
"""
import json
import os
import sys
import requests
from resource.utils.log import Logger

log_filename = os.path.realpath(sys.argv[1]).split("\\")[-1]. \
    replace(".py::", "py_").replace("::", ".") \
    if sys.argv[1] else None
# log_filename = os.path.basename(__file__)
print(f"日志主文件路径={log_filename}")
print(f"Sys.argv参数列表={sys.argv}")
logger = Logger(log_filename).logger


class Api:

    def __init__(self):

        self.logger = logger

    def request(self, request: dict):

        if request.get("protocol") == "rpc":
            return self.rpc_request(**request)

        if request.get("protocol") == "tcp":
            return self.tcp_request(**request)

        if request.get("protocol") == "dubbo":
            return self.dubbo_request(**request)

        return self.http_request(request)

    def http_request(self, request):

        self.logger.info(f"请求参数为==> {json.dumps(request, indent=2, ensure_ascii=False)}")
        r = requests.request(**request)
        self.logger.info(f"响应参数为==> {json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r.json()

    def rpc_request(self, request):

        pass

    def tcp_request(self, request):

        pass

    def dubbo_request(self, request):

        pass
