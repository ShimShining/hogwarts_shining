# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/23
Describe:api 自动化基类
"""
import json
import requests
import os
import sys
from resource.utils.log import Logger

log_filename = os.path.realpath(sys.argv[1]).split("\\")[-1]. \
    replace(".py::", "py_").replace("::", ".") \
    if sys.argv[1] else None
# log_filename = os.path.basename(__file__)
print(f"日志主文件路径={log_filename}")
print(f"Sys.argv参数列表={sys.argv}")
logger = Logger(log_filename).logger


class BaseApi:

    def __init__(self):

        self.logger = logger

    def request(self, request: dict):

        if request.get("protocol") == "rpc":
            return self.rpc_request(**request)

        if request.get("protocol") == "tcp":
            return self.tcp_request(**request)

        return self.http_request(request)

    def http_request(self, request):

        r = requests.request(**request)

        self.logger.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self, request):

        pass

    def tcp_request(self, request):

        pass

    # @staticmethod
    # def log_info(msg):
    #
    #     logger.info(msg)
    #
    # @staticmethod
    # def log_error(err_msg):
    #
    #     logger.error(err_msg)

