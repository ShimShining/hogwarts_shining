# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe:读取配置文件
"""
import configparser
import os


class ReadConfig:

    __root_dir = "D:\\personProc\\hogwarts_shining\\homework_test\\larkTest\\config\\config.ini"
    __cf = configparser.ConfigParser()

    @classmethod
    def get_lark_api_base_url(cls):
        cls.__cf.read(cls.__root_dir)
        print(cls.__root_dir)
        print(cls.__cf)
        print(cls.__cf.sections())
        return cls.__cf.get("lark-api", "base_url")

