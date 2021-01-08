# setup , teardown

def setup_module():
    print("资源准备: setup module")


def teardown_module():
    print("资源准备: teardown module")


def test_case1():
    print("case1")


def setup_function():
    print("setup function")


def teardown_function():
    print("teardown function")


class TestDemo:
    # 类前后执行
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    def setup(self):
        print("TestDemo setup")

    # 每个测试用例前后执行
    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")


class TestDemo1:
    # 类前后执行
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    def setup(self):
        print("TestDemo setup")

    # 每个测试用例前后执行
    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
