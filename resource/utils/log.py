# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/24
Describe:日志输出
"""
import datetime
import logging
import os
import time


class Logger:

    def __init__(self, loggername=__name__):
        # python官方文档中提供的一段示例，使用logging模块产生logger对象
        logging.basicConfig(datefmt='%Y-%m-%d%I:%M:%S %p')
        # 创建一个日志对象，这个参数可以随便填，这个参数唯一标识了这个日志对象
        self.logger = logging.getLogger(loggername)
        # 设置级别
        self.logger.setLevel(logging.INFO)

        # current_path = os.path.dirname(os.path.realpath(__file__))
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把log变成文件名的一部分了
        # log_path = current_path + "/log/"
        # 指定输出的日志文件名
        log_abs_path = "D:/personProc/hogwarts_shining/log/"
        dt = time.strftime("%Y_%m_%d_%H_%M", time.localtime(time.time()),)
        # 日志的文件名
        logname = log_abs_path + str(loggername) + '_' + str(dt) + '.log'
        # 创建一个handler，用于写入日志文件, 'a'表示追加
        file_handler = logging.FileHandler(logname, 'a')
        # 为logger添加的日志处理器
        self.logger.addHandler(file_handler)

        formatter = logging.Formatter('%(asctime)s => %(filename)s[line:%(lineno)d] * %(levelname)s : %(message)s')
        # 设置日志内容的格式
        file_handler.setFormatter(formatter)

    def fun(self):
        self.logger.error("这个一条错误日志")
        self.logger.info("这是一条info日志")
        self.logger.debug("这是一条debug日志")
        self.logger.warning("这是一条warning日志")


if '__main__' == __name__:
    testLogger = Logger("TestLogger")
    testLogger.fun()
