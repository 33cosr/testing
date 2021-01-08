import pytest
import yaml

from pythoncode.calculator import Calculator


def test_a():
    print("test case ")


def get_datas(function_name):
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    add_datas = datas[function_name]['datas']
    add_ids = datas[function_name]['ids']
    print(add_datas)
    print(add_ids)
    return [add_datas, add_ids]


def get_steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile, encoding="utf-8") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'add' == step:
            print("step add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step add1")
            result = calc.add1(a, b)
        assert expect == result


class TestCalc:
    # def setup_class(self):
    #     print("caculator start")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("caculator end")

    def test_add_steps(self, get_calc):
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add1(1, 2)
        a = 1
        b = 1
        expect = 2

        get_steps("./steps/add_steps.yml", get_calc, a, b, expect)

    @pytest.mark.parametrize('a,b,expect', get_datas('add')[0],
                             ids=get_datas('add')[1])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.3, 0.4], [0.1, 0.1, 0.2], [0.5, 0.5, 1]])
    def test_add_float(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[10, 2, 8], [30, 40, -10], [3, 1, 2], [-1, -2, 1]],
                             ids=['sub case 1', 'sub case 2', 'sub case 3', 'sub case 4'])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[10.2, 10, 0.2], [0.3, 0.2, 0.1], [-1, -2, 1]],
                             ids=['sub case 1', 'sub case 2', 'sub case 3'])
    def test_sub_float(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[10, 2, 20], [30, 40, 1200], [0.3, 0.2, 0.06], [-1, -2, 2]],
                             ids=['mul case 1', 'mul case 2', 'mul case 3', 'mul case 4'])
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.32, 2, 0.64], [30, 40, 1200], [0.3, 0.2, 0.06], [-1, -2, 2]],
                             ids=['mul case 1', 'mul case 2', 'mul case 3', 'mul case 4'])
    def test_mul_float(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', get_datas('div')[0],
                             ids=get_datas('div')[1])
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [[10, 0], [30, 0], [0.3, 0], [-1, 0]],
                             ids=['divide case 1', 'divide case 2', 'divide case 3', 'divide case 4'])
    def test_div_zero(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            result = get_calc.div(a, b)

    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
