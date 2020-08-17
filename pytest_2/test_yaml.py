import pytest
import yaml


def get_data():
    with open('./data1.yml',encoding='utf-8') as f:
        datas = yaml.load(f)
        a = datas['add']['data']
        b = datas['add']['ids']
        print(f'\n{datas}')
    return [a, b]


@pytest.mark.parametrize('a', get_data()[0], ids=get_data()[1])
def test_func(a):
    b = a[0]+a[1]
    print(f'\n{b}')
