#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""
import pytest

# content of test_sample.py
def inc(x):
    return x + 1

@pytest.mark.login
def test_answer():
    assert inc(3) == 4