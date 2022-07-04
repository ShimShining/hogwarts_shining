#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""
import allure

TEST_CASE_LINK = 'https://github.com/.../...'


@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass