#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""
import pytest


@pytest.mark.parametrize('key', ['a','b','c'],ids=['a','b','c'])
def test_inter(key):
    url = f"http://www.ceshiren.com/key={key}"
    print(url)