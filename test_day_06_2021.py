from adventofcode.year_2021.day_06_2021 import part_one, part_two

def test_part_one():
    test_data = ['3,4,3,1,2']
    assert 26 == part_one(18, test_data)
    assert 5934 == part_one(80, test_data)

def test_part_two():
     test_data = ['3,4,3,1,2']
     assert 26984457539 == part_two(256, test_data)
