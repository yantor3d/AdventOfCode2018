import pytest

import aoc.day_03


TEST_01_INPUT = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2",
]

TEST_01_PARSED = [
    aoc.day_03.Rectangle(1, 1, 3, 4, 4),
    aoc.day_03.Rectangle(2, 3, 1, 4, 4),
    aoc.day_03.Rectangle(3, 5, 5, 2, 2),
]

TEST_01_AREA_COVERED = {
    1: {
        (1, 3), (2, 3), (3, 3), (4, 3),
        (1, 4), (2, 4), (3, 4), (4, 4),
        (1, 5), (2, 5), (3, 5), (4, 5),
        (1, 6), (2, 6), (3, 6), (4, 6),
    },
    2: {
        (3, 1), (4, 1), (5, 1), (6, 1),
        (3, 2), (4, 2), (5, 2), (6, 2),
        (3, 3), (4, 3), (5, 3), (6, 3),
        (3, 4), (4, 4), (5, 4), (6, 4),
    },
    3: {
        (5, 5), (6, 5), 
        (5, 6), (6, 6), 
    }
}

TEST_01_EXPECTED_OVERLAP = {
    (1, 2): {
        (3, 3), (4, 3),
        (3, 4), (4, 4)
    }
}


@pytest.mark.parametrize("input_,expected", zip(TEST_01_INPUT, TEST_01_PARSED))
def test_01_parse_retangles(input_, expected):
    actual = aoc.day_03.parse_rectangle(input_)

    assert actual == expected


@pytest.mark.parametrize("input_", TEST_01_INPUT)
def test_01_area_of_rectangle(input_):
    rect = aoc.day_03.parse_rectangle(input_)

    actual = aoc.day_03.rectangle_coverage(rect)
    expected = TEST_01_AREA_COVERED[rect.id]

    assert actual == expected


def test_01_overlap_of_rectangles():
    rectangles = map(aoc.day_03.parse_rectangle, TEST_01_INPUT)
    actual = aoc.day_03.shared_coverage(rectangles)

    assert actual == 4
