#!/usr/bin/python37
# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/12
Describe:
"""
import pytest


@pytest.fixture(params=["tom",'jerry','lili'],ids=[
    "唐门",
    "杰瑞",
    "丽丽"
])
def login(request):
    return request.param
    print("login")


def test_login(login):

    print(login)