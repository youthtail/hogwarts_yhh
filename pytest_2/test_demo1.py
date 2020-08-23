# 装饰器传参
import pytest


# 被测方法
def plus(a, b):
    return a + b


# 测试方法
# 装饰器，传参
@pytest.mark.parametrize('a,b,c', [(1, 2, 3), (2, 2, 4)])
def test_fun1(a, b, c):
    assert plus(a, b) == c


# 加上装饰器（装饰器是加在函数上的，调用函数的时候，会自动执行装饰器里的方法）
@pytest.fixture()
def loggin():
    print("登录方法")
    return "登录方法"


class TestDemo:

    def test_fun2(self, loggin):
        print(f'测试类的测试方法')
        assert plus(1, 2) == 3
        print(f'user={loggin}')
