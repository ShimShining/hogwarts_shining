#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date:2021-04-09
Describe:
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""
import pytest
import yaml
import allure


global data
data = yaml.safe_load(open("../datas/test_1th_work.yml"))


# 计算器
class Calculator:
    # 相加
    def add(self, a, b):
        return a + b

    # 相除
    def div(self, a, b):
        return a / b


add = Calculator().add


def insert_func(param_list, insert_item):
    for item in param_list:
        item.insert(0, insert_item)


insert_func(data["add_equal"], add)
insert_func(data["add_unequal"], add)
insert_func(data["add_exception"], add)


@allure.feature("计算器模块")
class TestCalculator:

    def setup_class(self):

        print("---- class setup ----")
        self.calc = Calculator()
        self.accuracy = 0.000001   # 浮点数精度误差
        # add = self.calc.add
        # self.insert_func(data["add_equal"], add)
        # self.insert_func(data["add_unequal"], add)
        # self.insert_func(data["add_exception"], add)

    def teardown_class(self):

        print("---- class teardown ----")

    def setup(self):

        print("---- 开始计算 ----")

    def teardown(self):

        print("---- 计算结束 ----")

    @allure.story("计算器加法正向用例")
    @pytest.mark.parametrize("func,a,b,expected_value", data["add_equal"])
    def test_add_equal(self, func, a, b, expected_value):

        if type(a) == float and type(b) == float:
            assert abs(func(a, b) - expected_value) < self.accuracy
        else:
            assert func(a, b) == expected_value

    @allure.story("计算器加法正向用例")
    @pytest.mark.parametrize("func,a,b,expected_value", data["add_unequal"])
    def test_add_unequal(self, func, a, b, expected_value):
        assert func(a, b) != expected_value

    @allure.story("计算器加法异常场景用例")
    @pytest.mark.parametrize("func,a,b,exception,ex_pattern", data["add_exception"])
    def test_add_exception(self, func, a, b, exception, ex_pattern):

        with pytest.raises(eval(exception)) as exinfo:
            func(a, b)
        assert exinfo.type == eval(exception)
        assert ex_pattern in str(exinfo.value)

    @allure.story("计算器除法正向用例")
    @pytest.mark.parametrize("a,b,expected_value", data["div_equal"])
    def test_div_equal(self, a, b, expected_value):

        assert self.calc.div(a, b) == expected_value

    @allure.story("计算器除法正向用例")
    @pytest.mark.parametrize("a,b,expected_value", data["div_unequal"])
    def test_div_unequal(self, a, b, expected_value):

        assert self.calc.div(a, b) != expected_value

    @allure.story("计算器除法异常场景用例")
    @pytest.mark.parametrize("a,b,exception,ex_pattern", data["div_exception"])
    def test_div_exception(self, a, b, exception, ex_pattern):
        # create_obj = compile('obj()', 'create_obj.py', 'eval')
        with pytest.raises(eval(exception)) as exinfo:
            self.calc.div(a, b)

        assert exinfo.type == eval(exception)
        assert ex_pattern in str(exinfo.value)


if __name__ == "__main__":

    pytest.main()

































