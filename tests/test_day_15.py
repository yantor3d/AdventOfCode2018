import pytest 

import aoc.day_15 

INPUT_01 = (
    [
        '#######',
        '#.G...#',
        '#...EG#',
        '#.#.#G#',
        '#..G#E#',
        '#.....#',
        '#######',
    ]
)

OUTPUT_101 = (47, 590, 27730)
OUTPUT_201 = (29, 172, 4988)

INPUT_02 = (
    [
        '#######',
        '#G..#E#',
        '#E#E.E#',
        '#G.##.#',
        '#...#E#',
        '#...E.#',
        '#######',
    ]
)

OUTPUT_102 = (37, 982, 36334)

INPUT_03 = (
    [
        '#######',
        '#E..EG#',
        '#.#G.E#',
        '#E.##E#',
        '#G..#.#',
        '#..E#.#',
        '#######',
    ]
)

OUTPUT_103 = (46, 859, 39514)
OUTPUT_203 = (33, 948, 31284)

INPUT_04 = (
    [
        '#######',
        '#E.G#.#',
        '#.#G..#',
        '#G.#.G#',
        '#G..#.#',
        '#...E.#',
        '#######',
    ]
)

OUTPUT_104 = (35, 793, 27755)
OUTPUT_204 = (37, 94, 3478)

INPUT_05 = (
    [
        '#######',
        '#.E...#',
        '#.#..G#',
        '#.###.#',
        '#E#G#G#',
        '#...#G#',
        '#######',
    ]
)

OUTPUT_105 = (54, 536, 28944)
OUTPUT_205 = (39, 166, 6474)

INPUT_06 = (
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
    ]
)

OUTPUT_106 = (20, 937, 18740)
OUTPUT_206 = (30, 38, 1140)

EXAMPLES_1 = [
    (INPUT_01, OUTPUT_101),
    (INPUT_02, OUTPUT_102),
    (INPUT_03, OUTPUT_103),
    (INPUT_04, OUTPUT_104),
    (INPUT_05, OUTPUT_105),
    (INPUT_06, OUTPUT_106),
]

EXAMPLES_2 = [
    (INPUT_01, 15, OUTPUT_201),
    (INPUT_03, 4,  OUTPUT_203),
    (INPUT_04, 15, OUTPUT_204),
    (INPUT_05, 12, OUTPUT_205),
    (INPUT_06, 34, OUTPUT_206),
]

@pytest.mark.parametrize('input_,expected', EXAMPLES_1)
def test_example_01_games(input_, expected):
    game = aoc.day_15.parse_input(input_)

    actual = game.play()

    assert actual == expected


@pytest.mark.parametrize('input_,cheat,expected', EXAMPLES_2)
def test_example_02_games(input_, cheat, expected):
    game = aoc.day_15.parse_input(input_)
    actual = game.play(cheat)

    assert actual == expected
