import aoc.day_17 

EXAMPLE_INPUT = [
    'x=495, y=2..7',
    'y=7, x=495..501',
    'x=501, y=3..7',
    'x=498, y=2..4',
    'x=506, y=1..2',
    'x=498, y=10..13',
    'x=504, y=10..13',
    'y=13, x=498..504',
]


def test_example_01():
    clay = aoc.day_17.parse_input(EXAMPLE_INPUT)

    damp, wet = aoc.day_17.Scan(clay).simulate()
    actual = len(damp | wet)

    assert actual == 57


def test_example_02():
    clay = aoc.day_17.parse_input(EXAMPLE_INPUT)

    damp, wet = aoc.day_17.Scan(clay).simulate()
    actual = len(wet)

    assert actual == 29
