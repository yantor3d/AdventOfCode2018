import aoc.day_18 

EXAMPLE = [
    '.#.#...|#.',
    '.....#|##|',
    '.|..|...#.',
    '..|#.....#',
    '#.#|||#|#|',
    '...#.||...',
    '.|....|...',
    '||...#|.#|',
    '|.||||..|.',
    '...#.|..|.',
]


def test_example_01():
    in_woods = aoc.day_18.parse_input(EXAMPLE)

    actual = aoc.day_18.solve(in_woods, 10)

    assert actual == 1147
