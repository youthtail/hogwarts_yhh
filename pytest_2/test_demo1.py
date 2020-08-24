import pytest


# 被测类
class Calculator:

    def plus(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def minus(self, a, b):
        return a - b

    def times(self, a, b):
        return a * b


# 测试方法
# 装饰器，传参
class TestClass1:
    calc = Calculator()

    @pytest.mark.parametrize('a,b,c', [(1, 2, 3), (2, 2, 4)])
    def test_fun1(self, a, b, c):
        assert self.calc.plus(a, b) == c

    def test_fun2(self, a, b, c):
        self.calc.plus(a,b) ==c


# 加上装饰器（装饰器是加在函数上的，调用函数的时候，会自动执行装饰器里的方法）
@pytest.fixture(params='abc')
def loggin():
    return "vvv"


class TestDemo:

    def test_fun2(self, loggin):
        a=loggin(1)
        print(f'user={a}')

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    print(f"{customer_1},{customer_2},{customer_3}")