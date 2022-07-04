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
    if sys.argv[1] else "api.py兜底日志文件名"
# log_filename = os.path.basename(__file__)
logger = Logger(log_filename).logger
logger.info("<== logger 初始化完成,开始日志收集 ==>")
logger.info(f"Sys.argv参数列表={sys.argv}")
logger.info(f"日志主文件路径={log_filename}")


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
        self.logger.info(f"返回状态码为==> {r.status_code}")
        self.logger.info(f"返回响应为==> {json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r.json()

    def rpc_request(self, request):

        pass

    def tcp_request(self, request):

        pass

    def dubbo_request(self, request):

        pass
