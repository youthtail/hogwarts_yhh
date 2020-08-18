import pytest
import yaml


def plus(a, b):
    return a + b


def div(a, b):
    return a / b


class TestPractice:
    def setup_class(self):
        print("\n测试类开始")

    def teardown_class(self):
        print("\n测试类结束")

    def setup(self):
        print("测试方法开始")

    def teardown(self):
        print("\n测试方法结束")

    def get_testdata(method_name):
        with open('./data1.yml', encoding='utf-8') as f:
            testdata = yaml.safe_load(f)
            data = testdata[method_name]["data"]
            idss = testdata[method_name]["ids"]
        return [data, idss]

    @pytest.mark.plus
    @pytest.mark.parametrize("a,b,c", get_testdata("plus")[0], ids=get_testdata("plus")[1])
    def test_plus(self, a, b, c):
        if a == "a":
            try:
                plus(a, b)
            except Exception as e:
                assert e.__class__.__name__ == "TypeError"
            else:
                assert plus(a, b) == c

    @pytest.mark.div
    @pytest.mark.parametrize("a,b,c", get_testdata("div")[0], ids=get_testdata("div")[1])
    def test_div(self, a, b, c):
        if b == 0:
            try:
                div(a, b)
            except Exception as e:
                assert e.__class__.__name__ == "ZeroDivisionError"
        else:
            result = div(a, b)
            assert round(result, 2) == c
