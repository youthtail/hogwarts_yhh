'''
测试用例的类别：
1、测试函数：def test_*(),位于测试类外
2、测试方法：def test_*(self),位于测试类中
3、测试类：Class Test*，位于测试模块中
4、测试模块：test_*.py，等同于测试文件
setup和teardown:
1、setup_function()/teardown_function():作用于测试函数，，每个函数执行一次
2、setup()/teardown():作用于测试方法,每个方法执行一次
3、setup_class()/teardown_class():作用于测试类，每个类执行一次
4、setup_module()/teardown_module():作用于测试模块，即测试文件，每个模块执行一次
'''

import pytest

# 被测代码
import yaml


def plus(a, b):
    return a + b


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def get_data():
    with open("./data1.yml", encoding='utf-8') as f:
        data = yaml.load(f)
        data_list = data["add"]["data"]
        ids = data["add"]["ids"]
    return [data_list, ids]


# 测试方法
# 装饰器，传参
@pytest.mark.test_add
@pytest.mark.parametrize('a,b,c', [(1, 2, 3), (1, 3, 4)], ids=["aaa", "bbb"])
def test_fun1(a, b, c):
    assert plus(a, b) == c


@pytest.mark.parametrize('a,b,c', get_data()[0], ids=get_data()[1])
def test_fun1_1(a, b, c):
    assert plus(a, b) == c


# 装饰器（装饰器是加在函数上的，调用函数的时候，会自动执行装饰器里的方法）
@pytest.fixture()
def loggin():
    return "我是登录方法"


class TestDemo:

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print('teardown_class')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')


    @pytest.mark.parametrize('a,b,c', get_data()[0],ids=get_data()[1])
    def test_fun2(self, a, b, c):
        print('测试方法：fun2')
        assert plus(a, b) == c

    def test_fun3(self, loggin):
        print(f'测试类的测试方法3')
        assert plus(1, 2) == 4
        print(f'user={loggin}')
