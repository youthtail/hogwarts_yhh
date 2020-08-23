import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('./data')))
    def test_a(self, env):
        if 'test' in env:
            print(f"测试环境{env}")


def test_b():
    f = yaml.safe_load(open('./data'))
    print(f)