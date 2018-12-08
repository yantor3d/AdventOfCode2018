import pytest 

import aoc.day_06 

P = aoc.day_06.Point 

TEST_DATA = [
    P(1, 1),
    P(1, 6),
    P(8, 3),
    P(3, 4),
    P(5, 5),
    P(8, 9),
]

TEST_AREA_AROUND = [
    {P(1, 1), (2, 1), P(0, 1), P(1, 2), P(1, 0)},
    {P(1, 6), (2, 6), P(0, 6), P(1, 7), P(1, 5)},
    {P(8, 3), (7, 3), P(9, 3), P(8, 4), P(8, 2)},
    {P(3, 4), (4, 4), P(2, 4), P(3, 5), P(3, 3)},
    {P(5, 5), (6, 5), P(4, 5), P(5, 6), P(5, 4)},
    {P(8, 9), (9, 9), P(7, 9), P(8, 10), P(8, 8)},
]

TEST_OUTPUT = [
    -1,
    -1,
    -1,
    9,
    17,
    -1
]


def test_bounding_box_min():
    bb = aoc.day_06.get_bounding_box(TEST_DATA)
    assert bb.min == P(1, 1)


def test_bounding_box_max():
    bb = aoc.day_06.get_bounding_box(TEST_DATA)
    assert bb.max == P(8, 9)


@pytest.mark.parametrize('input_,expected', zip(TEST_DATA, TEST_AREA_AROUND))
def test_area_around(input_, expected):
    actual = aoc.day_06.area_around(input_)
    assert set(actual) == expected


@pytest.mark.parametrize('input_,expected', zip(TEST_DATA, TEST_AREA_AROUND))
def test_grow_area(input_, expected):
    actual = aoc.day_06.grow_area({input_})
    assert actual == expected


@pytest.mark.parametrize('input_,expected', zip(TEST_DATA, TEST_OUTPUT))
def test_non_infinite_area(input_, expected):
    areas = aoc.day_06.get_area_around_points(TEST_DATA)
    
    assert areas[input_] == expected


if __name__ == '__main__':
    aoc.day_06.get_area_around_points(TEST_DATA)