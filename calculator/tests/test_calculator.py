import pytest
from calculator.calculator import Calculator
from faker import Faker
fake = Faker()

@pytest.fixture
def calculator():
    """Fixture to reset history before each test."""
    Calculator.clear_history()
    return Calculator

class TestCalculator:

    def test_add(self, calculator):
        a = fake.random_number()
        b = fake.random_number()
        expected = a + b
        assert calculator.add(a, b) == expected

    def test_subtract(self, calculator):
        a = fake.random_number()
        b = fake.random_number()
        expected = a - b
        assert calculator.subtract(a, b) == expected

    def test_divide(self, calculator):
        a = fake.random_number()
        b = fake.random_number() or 1  # Ensure no zero division
        expected = a / b
        assert calculator.divide(a, b) == expected

    def test_divide_by_zero(self, calculator):
        a = fake.random_number()
        with pytest.raises(ZeroDivisionError):
            calculator.divide(a, 0)