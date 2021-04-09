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

@pytest.mark.add
def test_answer_false():
    assert inc(3) == 5

def test_answer_true():
    assert inc(4) == 5