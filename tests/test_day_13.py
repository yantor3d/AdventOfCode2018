import aoc.day_13 
import aoc.util


def test_example_01():
    puzzle_input = aoc.util.get_puzzle_input(13, raw=True, test_data='test_01')
    mine = aoc.day_13.parse_input(puzzle_input)

    actual = aoc.day_13.simulate(mine)
    
    assert actual == (7, 3)


def test_example_02():
    puzzle_input = aoc.util.get_puzzle_input(13, raw=True, test_data='test_02')
    mine = aoc.day_13.parse_input(puzzle_input)
    mine.remove_collisions = True

    actual = aoc.day_13.simulate(mine)
    
    assert actual == (6, 4)
