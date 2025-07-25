import pytest
from app.calc import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 16, 4) != 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 1) == 9

    def test_adding_success(self):
        assert self.calc.adding(self,5, 5) == 10

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print("Выполнение метода Teardown")
       
