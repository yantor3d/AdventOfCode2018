import pytest 

import aoc.day_01 

TEST_DATA_01 = [
    ('+1 -2 +3 +1', 3),
    ('+1 +1 +1', 3),
    ('+1 +1 -2', 0),
    ('-1 -2 -3', -6)
]

TEST_DATA_02 = [
    ('+1 -2 +3 +1', 2),
    ('+1 -1', 0),
    ('+3 +3 +4 -2 -4', 10),
    ('-6 +3 +8 +5 -6', 5),
    ('+7 +7 -2 -7 -4', 14)
]


@pytest.mark.parametrize("input_,expected", TEST_DATA_01)
def test_part_01(input_, expected):
    deltas = aoc.day_01.parse_input(input_)

    assert aoc.day_01.get_frequency(deltas) == expected


@pytest.mark.parametrize("input_,expected", TEST_DATA_02)
def test_part_02(input_, expected):
    deltas = aoc.day_01.parse_input(input_)

    assert aoc.day_01.get_first_frequency_reached_twice(deltas) == expected
