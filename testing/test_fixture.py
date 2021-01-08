import time

import pytest


# @pytest.fixture(autouse=True, scope="module")
# def login():
#     print("login")
#     yield ['tom', '123456']  # 相当于return
#     print('logout')
#
#
# # 相当于 setup tear down
# @pytest.fixture
# def conn_db():
#     print('conn db')

# 默认读取conftest.py的fixture conftest不能更换
# --setup-show 回溯fixture的执行国臣
# @pytest.mark.usefixtures("login")
def test_case1(login):
    print("print case 1")
    print(login)


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_case2():
    print("print case 2")


# 如果要用到fixure的返回值 需要以参数的形式传入 不能使用装饰器
def test_case3(login, conn_db):
    print("print case 3")
    print(login)


def test_case4():
    assert True
    # assert False
    # assert 1 == 2


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)],ids=["用例1","用例2","用例三"])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)


# @pytest.mark.parametrize('a', [1, 2, 3, 4])
# def test_case5(a):
#     time.sleep(3)
#     assert True
