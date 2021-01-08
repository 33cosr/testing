from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(autouse=False, scope="function", params=['tom', 'jerry'])
def login(request):
    print("login hhh")
    request.param
    yield request.param  # 相当于return
    print('logout hhhh')


# 相当于 setup tear down
@pytest.fixture(scope="session")
def conn_db():
    print('conn db')


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("*****hello***")
    print(config)
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
