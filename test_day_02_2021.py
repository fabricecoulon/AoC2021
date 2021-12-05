"""
Run with:
pip install pytest pytest_mock
python -m pytest .\test_day_02_2021.py
"""
from adventofcode.year_2021.day_02_2021 import part_one, part_two

def test_part_one():
    test_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    assert 150 == part_one(test_data)

def test_part_two():
    test_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    assert 900 == part_two(test_data)
