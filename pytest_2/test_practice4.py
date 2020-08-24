import allure
import pytest

from conftest import get_testdata


class TestPractice:

    def setup_class(self):
        print("\n测试类开始")

    def teardown_class(self):
        print("\n测试类结束")

    def setup(self):
        print("测试方法开始")

    def teardown(self):
        print("\n测试方法结束")

    @allure.story("加法测试")
    @allure.link("http:baidu.com", name="jira")
    @pytest.mark.run(order=1)
    def test_plus(self, get_calc, get_data0):
        data = get_data0
        print(data)
        a = data[0]
        b = data[1]
        c = data[2]
        if a == "a":
            try:
                get_calc.plus(a, b)
            except Exception as e:
                assert e.__class__.__name__ == "TypeError"
            else:
                assert get_calc.plus(a, b) == c

    @allure.story("除法测试")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,c", get_testdata("div")[0], ids=get_testdata("div")[1])
    def test_div(self, get_calc, a, b, c):
        if b == 0:
            try:
                get_calc.div(a, b)
            except Exception as e:
                assert e.__class__.__name__ == "ZeroDivisionError"
        else:
            result = get_calc.div(a, b)
            assert round(result, 2) == c

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, c', get_testdata("minus")[0], ids=get_testdata("minus")[1])
    def test_minus(self, a, b, c, get_calc):
        assert get_calc.minus(a, b) == c

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, c', get_testdata("times")[0], ids=get_testdata("times")[1])
    def test_times(self, a, b, c, get_calc):
        assert get_calc.times(a, b) == c
