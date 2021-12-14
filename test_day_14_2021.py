from adventofcode.year_2021.day_14_2021 import part_one, part_two

TESTDATA1 = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

expected = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

def test_part_one():
    test_data = TESTDATA1.splitlines()
    assert (len(expected), expected, 18) == part_one(test_data, 4) 
    assert 97 == part_one(test_data, 5)[0]
    assert 3073 == part_one(test_data, 10)[0]
    assert 1588 == part_one(test_data, 10)[2]

def test_part_two():
     test_data = TESTDATA1.splitlines()
     assert 2188189693529 == part_two(test_data, 40)
