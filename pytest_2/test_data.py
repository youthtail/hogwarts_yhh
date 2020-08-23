import pytest


def plus(a, b):
    return a+b


class TestData:
    @pytest.mark.parametrize(['a', 'b', 'c'], [(1, 2, 3), (2, 3, 4)])
    def test_data(self, a, b, c):
        assert plus(a, b) == c
