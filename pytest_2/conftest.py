import os

import pytest
import yaml
from calculator_demo import Calculator


@pytest.fixture(scope="module")
def get_calc():
    print("【开始计算】")
    calc = Calculator()
    yield calc
    print("【结束计算】")


def get_testdata(method_name):
    data_path = os.getcwd() + '/data1.yml'
    with open(data_path, encoding='utf-8') as f:
        testdata = yaml.safe_load(f)
        data = testdata[method_name]["data"]
        idss = testdata[method_name]["ids"]
    return [data, idss]


@pytest.fixture(params=get_testdata("plus")[0], ids=get_testdata("plus")[1])
def get_data0(request):
    return request.param
