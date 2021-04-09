#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""
import pytest
import yaml
class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print('测试环境')
            print(env)
            print(f"测试环境IP = {env['test']}")
        elif 'dev' in env:
            print('这是开发环境')