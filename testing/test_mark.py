import pytest


@pytest.mark.login
def test_login1():
    print("login1 case")


@pytest.mark.login
def test_login2():
    print("login2 case")


@pytest.mark.search
def test_search1():
    print("search 1 case")


@pytest.mark.search
def test_search2():
    print("search 2 case")
