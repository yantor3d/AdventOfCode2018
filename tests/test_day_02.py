import pytest

import aoc.day_02

TEST_INPUT_DATA = (
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
)

TEST_INPUT_RESULTS_2 = (0, 1, 1, 0, 1, 1, 0)
TEST_INPUT_RESULTS_3 = (0, 1, 0, 1, 0, 0, 1)


@pytest.mark.parametrize("input_,expected", zip(TEST_INPUT_DATA, TEST_INPUT_RESULTS_2))
def test_label_has_exactly_two_letters(input_, expected):
    """Test that a labels with exactly two of any letter return True."""

    actual = aoc.day_02.has_exactly_n_letters(input_, 2)

    assert actual == bool(expected)


@pytest.mark.parametrize("input_,expected", zip(TEST_INPUT_DATA, TEST_INPUT_RESULTS_3))
def test_label_has_exactly_three_letters(input_, expected):
    """Test that a labels with exactly three of any letter return True."""

    actual = aoc.day_02.has_exactly_n_letters(input_, 3)

    assert actual == bool(expected)


def test_label_checksum():
    """Test that the checksum of the labels is 12."""

    checksum = aoc.day_02.calculate_labels_checksum(TEST_INPUT_DATA)

    assert checksum == 12
