"""
Run with:
pip install pytest pytest_mock
python -m pytest .\test_day_01_2021.py
"""
from adventofcode.year_2021.day_01_2021 import part_one, part_two

def test_integer_comparison():
    test_data = ['9' , '10']
    assert 1 == part_one(test_data)

def test_part_one():
    test_data = ['199', '200', '208', '210', '200','207','240','269','260','263']
    assert 7 == part_one(test_data)

def test_part_two():
    test_data = ['199', '200', '208', '210', '200','207','240','269','260','263']
    assert 5 == part_two(test_data)

