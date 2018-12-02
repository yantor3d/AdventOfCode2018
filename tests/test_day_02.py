import itertools
import pytest

import aoc.day_02

TEST_INPUT_01_DATA = (
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
)

TEST_INPUT_01_RESULTS_2 = (0, 1, 1, 0, 1, 1, 0)
TEST_INPUT_01_RESULTS_3 = (0, 1, 0, 1, 0, 0, 1)


@pytest.mark.parametrize("input_,expected", zip(TEST_INPUT_01_DATA, TEST_INPUT_01_RESULTS_2))
def test_01_label_has_exactly_two_letters(input_, expected):
    """Test that a labels with exactly two of any letter return True."""

    actual = aoc.day_02.has_exactly_n_letters(input_, 2)

    assert actual == bool(expected)


@pytest.mark.parametrize("input_,expected", zip(TEST_INPUT_01_DATA, TEST_INPUT_01_RESULTS_3))
def test_01_label_has_exactly_three_letters(input_, expected):
    """Test that a labels with exactly three of any letter return True."""

    actual = aoc.day_02.has_exactly_n_letters(input_, 3)

    assert actual == bool(expected)


def test_01_label_checksum():
    """Test that the checksum of the labels is 12."""

    checksum = aoc.day_02.calculate_labels_checksum(TEST_INPUT_01_DATA)

    assert checksum == 12


TEST_INPUT_02_DATA = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]

TEST_INPUT_02_RESULTS = {
    ('abcde', 'axcye'): 2,
    ('fghij', 'fguij'): 1
}


@pytest.mark.parametrize("input_", itertools.combinations(TEST_INPUT_02_DATA, 2))
def test_02_count_number_of_different_letters(input_):
    a, b = input_

    try:
        expected = TEST_INPUT_02_RESULTS[(a, b)]
    except KeyError:
        pass
    else:
        actual = aoc.day_02.number_of_different_letters(a, b)
        assert actual == expected


def test_02_find_letters_in_common():
    expected = 'fgij'
    actual = aoc.day_02.find_letters_in_common('fghij', 'fguij')

    assert actual == expected
