import pytest

import aoc.day_09

TEST_DATA = [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
]


@pytest.mark.parametrize('num_players,last_marble_worth,expected', TEST_DATA)
def test_example_games(num_players, last_marble_worth, expected):
    actual = aoc.day_09.play_game(num_players, last_marble_worth)

    assert actual == expected
