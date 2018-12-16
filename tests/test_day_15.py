import pytest 

import aoc.day_15 

EXAMPLE_01 = (
    [
        '#######',
        '#.G...#',
        '#...EG#',
        '#.#.#G#',
        '#..G#E#',
        '#.....#',
        '#######',
    ], (47, 590, 27730)
)

EXAMPLE_02 = (
    [
        '#######',
        '#G..#E#',
        '#E#E.E#',
        '#G.##.#',
        '#...#E#',
        '#...E.#',
        '#######',
    ], (37, 982, 36334)
)

EXAMPLE_03 = (
    [
        '#######',
        '#E..EG#',
        '#.#G.E#',
        '#E.##E#',
        '#G..#.#',
        '#..E#.#',
        '#######',
    ], (46, 859, 39514)
)

EXAMPLE_04 = (
    [
        '#######',
        '#E.G#.#',
        '#.#G..#',
        '#G.#.G#',
        '#G..#.#',
        '#...E.#',
        '#######',
    ], (35, 793, 27755)
)

EXAMPLE_05 = (
    [
        '#######',
        '#.E...#',
        '#.#..G#',
        '#.###.#',
        '#E#G#G#',
        '#...#G#',
        '#######',
    ], (54, 536, 28944)
)

EXAMPLE_06 = (
    [
        '#########',
        '#G......#',
        '#.E.#...#',
        '#..##..G#',
        '#...##..#',
        '#...#...#',
        '#.G...G.#',
        '#.....G.#',
        '#########',
    ], (20, 937, 18740)
)

EXAMPLES = [
    EXAMPLE_01,
    EXAMPLE_02,
    EXAMPLE_03,
    EXAMPLE_04,
    EXAMPLE_05,
    EXAMPLE_06,
]


@pytest.mark.parametrize('input_,expected', EXAMPLES)
def test_example_game(input_,expected):
    game = aoc.day_15.parse_input(input_)

    actual = game.play()

    assert actual == expected