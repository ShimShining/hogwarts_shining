# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/12
Describe:
"""

import pytest
import yaml
from test_case.Calculator import *

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