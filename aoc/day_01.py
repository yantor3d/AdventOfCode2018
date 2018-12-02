"""Advent of Code 2018 day 01 - https://adventofcode.com/2018/day/1"""

import collections
import itertools
import os
import sys

import aoc.util


def parse_input(input_):
    """Parse the puzzle input.

    Args:
        input_ (str): A string of positive or negative frequency changes.

    Returns:
        :obj:`list` of :obj:`int`: A list of positive of negative frequency change values.

    """

    return list(map(int, input_.split()))


def incrimental_sum(values, start_at=0):
    """Calculate the sum of 'start' value (default: 0) plus an iterable of numbers.

    Yields:
        The sum after each number is added.

    """

    value = start_at

    while True:
        yield value 
        value += next(values)


def get_frequency(deltas):
    """Get the new frequency.

    Args:
        deltas (:obj:`list` of :obj:`int`): Frequency changes to apply

    Returns:
        int

    """

    return sum(deltas, 0)


def get_first_frequency_reached_twice(deltas):
    """Get the first frequency that is reached twice when repeating the same
    frequency changes over and over.

    Args:
        deltas (:obj:`list` of :obj:`int`): Frequency changes to apply

    Returns:
        int

    """

    result = None

    occurances = collections.Counter()

    frequency = incrimental_sum(itertools.cycle(deltas), start_at=0)

    while True:
        result = next(frequency)
        occurances[result] += 1 

        if occurances[result] == 2:
            break
    
    return result


def main(*argv):
    input_ = aoc.util.get_puzzle_input(1)

    deltas = parse_input(input_)

    answer_01 = get_frequency(deltas)
    print(f"Part One: {answer_01}")

    answer_02 = get_first_frequency_reached_twice(deltas)
    print(f"Part Two: {answer_02}")

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
