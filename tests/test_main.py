import pytest
from src.main import calculate_simple_interest

def test_calculate_simple_interest():
    assert calculate_simple_interest(1000, 5, 1) == 50.0
    assert calculate_simple_interest(2000, 3, 2) == 120.0
    assert calculate_simple_interest(500, 7, 3) == 105.0