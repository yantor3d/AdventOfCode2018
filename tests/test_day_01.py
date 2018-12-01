import pytest 

import aoc.day_01 

TEST_DATA = [
    ('+1 -2 +3 +1', 3),
    ('+1 +1 +1', 3),
    ('+1 +1 -2', 0),
    ('-1 -2 -3', -6)
]

@pytest.mark.parametrize("input_,expected", TEST_DATA)
def test_frequency_changes(input_, expected):
    deltas = aoc.day_01.parse_input(input_)

    assert aoc.day_01.get_frequency(deltas) == expected