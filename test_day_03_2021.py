"""
Run with:
pip install pytest pytest_mock
python -m pytest .\test_day_03_2021.py
"""
from adventofcode.year_2021.day_03_2021 import part_one, part_two

# ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def test_part_one():
    test_data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    assert 198 == part_one(test_data)

def test_part_two():
     test_data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
     assert 230 == part_two(test_data)
