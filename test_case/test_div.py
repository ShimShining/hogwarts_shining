#!/usr/bin/python37
# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/12
Describe:
"""

import pytest
import yaml



# 计算器
class Calculator:
    # 相加
    def add(self, a, b):
        return a + b

    # 相除
    def div(self, a, b):
        return a / b


@pytest.fixture()
def initcalc():
    calc = Calculator()
    return calc

def get_datas():

    with open("../datas/test_1th_work.yml") as f:
        datas = yaml.safe_load(f)
        return datas["div_equal"]

@pytest.fixture(params=get_datas())
def get_data(request):
    return request.param


class TestDiv:

    def test_div(self,initcalc, get_data):
        print(get_data)
        a, b, expect = get_data
        try:
            assert expect == initcalc.div(a, b)
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    pytest.main("-v -s")