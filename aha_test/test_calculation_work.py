# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/13
Describe:
1.上节课的作业，使用fixture 实现setup/teardown 功能
2.使用fixture 实现 参数化的功能
3.使用插件完成测试用例顺序的控制
4.改造测试用例的编码，支持中文编码格式（选做）
    1:pytest源码中的node.py文件的Node类中的name属性做一下编码解码操作
    # self.name = name
    self.name = name.encode("utf-8").decode("unicode_escape") # 支持中文
    2:hook函数pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
    ) -> None
    item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
5.添加命令行参数，使用hook插件实现（拔高，选做）
6.生成测试 报告截图
"""
import allure
import pytest


@allure.feature("计算器模块")
@pytest.mark.usefixtures("init_function")
class TestCalculator:

    @allure.story("计算器加法正向用例")
    @pytest.mark.run(order=2)
    def test_add_equal(self, init_class, get_add_equal_data):

        func = init_class.add
        a, b, expected_value = get_add_equal_data
        if type(a) == float or type(b) == float:
            assert round(func(a, b), 3) == expected_value
        else:
            assert func(a, b) == expected_value

    @allure.story("计算器加法正向用例")
    @pytest.mark.usefixtures("init_function")
    @pytest.mark.run(order=1)
    def test_add_unequal(self, init_class, get_add_unequal_data):

        func = init_class.add
        a, b, expected_value = get_add_unequal_data
        assert func(a, b) != expected_value

    @allure.story("计算器加法异常场景用例")
    @pytest.mark.run(order=6)
    def test_add_exception(self, init_class, get_add_exception_data):

        func = init_class.add
        a, b, exception, ex_pattern = get_add_exception_data
        with pytest.raises(eval(exception)) as exinfo:
            func(a, b)
        assert exinfo.type == eval(exception)
        assert ex_pattern in str(exinfo.value)

    @allure.story("计算器除法正向用例")
    @pytest.mark.run(order=4)
    def test_div_equal(self, init_class, get_div_equal_data):

        a, b, expected_value = get_div_equal_data
        assert init_class.div(a, b) == expected_value

    @allure.story("计算器除法正向用例")
    @pytest.mark.run(order=3)
    def test_div_unequal(self, init_class, get_div_unequal_data):

        a, b, expected_value = get_div_unequal_data
        assert init_class.div(a, b) != expected_value

    @allure.story("计算器除法异常场景用例")
    @pytest.mark.run(order=5)
    def test_div_exception(self, init_class, get_div_exception_data):

        a, b, exception, ex_pattern = get_div_exception_data
        with pytest.raises(eval(exception)) as exinfo:
            init_class.div(a, b)

        assert exinfo.type == eval(exception)
        assert ex_pattern in str(exinfo.value)


if __name__ == "__main__":

    pytest.main()
