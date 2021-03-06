import aoc.day_12 

TEST_INPUT = [
    'initial state: #..#.#..##......###...###',
    '',
    '...## => #',
    '..#.. => #',
    '.#... => #',
    '.#.#. => #',
    '.#.## => #',
    '.##.. => #',
    '.#### => #',
    '#.#.# => #',
    '#.### => #',
    '##.#. => #',
    '##.## => #',
    '###.. => #',
    '###.# => #',
    '####. => #',
]

GENERATIONS = [
    '...#..#.#..##......###...###...........',
    '...#...#....#.....#..#..#..#...........',
    '...##..##...##....#..#..#..##..........',
    '..#.#...#..#.#....#..#..#...#..........',
    '...#.#..#...#.#...#..#..##..##.........',
    '....#...##...#.#..#..#...#...#.........',
    '....##.#.#....#...#..##..##..##........',
    '...#..###.#...##..#...#...#...#........',
    '...#....##.#.#.#..##..##..##..##.......',
    '...##..#..#####....#...#...#...#.......',
    '..#.#..#...#.##....##..##..##..##......',
    '...#...##...#.#...#.#...#...#...#......',
    '...##.#.#....#.#...#.#..##..##..##.....',
    '..#..###.#....#.#...#....#...#...#.....',
    '..#....##.#....#.#..##...##..##..##....',
    '..##..#..#.#....#....#..#.#...#...#....',
    '.#.#..#...#.#...##...#...#.#..##..##...',
    '..#...##...#.#.#.#...##...#....#...#...',
    '..##.#.#....#####.#.#.#...##...##..##..',
    '.#..###.#..#.#.#######.#.#.#..#.#...#..',
    '.#....##....#####...#######....#.#..##.',
]


def test_example():
    state, rules = aoc.day_12.parse_input(TEST_INPUT)

    for i in range(0, 21):
        if i > 0:
            state = aoc.day_12.tick(state, rules)

        state_str = ''.join([state.get(k, '.') for k in range(-3, 36)])

        assert state_str == GENERATIONS[i]

    actual = aoc.day_12.evaluate(state)

    assert actual == 325
