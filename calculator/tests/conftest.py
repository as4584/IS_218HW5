import pytest
from faker import Faker
from calculator.calculator import Calculator

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate for testing")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture(scope="session")
def generated_records(num_records):
    records = []
    for _ in range(num_records):
        a = fake.random_number()
        b = fake.random_number()
        operation = fake.random_element(elements=('add', 'subtract', 'divide'))
        
        if operation == 'add':
            result = Calculator.add(a, b)
        elif operation == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation == 'divide':
            b = b or 1  # Avoid division by zero
            result = Calculator.divide(a, b)
        
        records.append((a, b, operation, result))
    
    return records

@pytest.mark.parametrize("a, b, operation, expected", [])
def test_generated_records(a, b, operation, expected):
    if operation == "add":
        assert Calculator.add(a, b) == expected
    elif operation == "subtract":
        assert Calculator.subtract(a, b) == expected
    elif operation == "divide":
        assert Calculator.divide(a, b) == expected