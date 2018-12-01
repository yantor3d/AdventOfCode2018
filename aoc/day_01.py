"""Advent of Code 2018 day 01 - https://adventofcode.com/2018/day/1"""

import os 
import sys 


def parse_input(input_):
    """Parse the puzzle input.

    Args:
        input_ (str): A string of positive or negative frequency changes.

    Returns:
        :obj:`list` of :obj:`int`: A list of positive of negative frequency change values.
        
    """

    return map(int, input_.split())


def get_frequency(deltas, starting_frequency=0):
    """Get the new frequency.

    Args:
        deltas (:obj:`list` of :obj:`int`): Frequency changes to apply
        starting_frequency (int): Frequency to start at

    Returns:
        int

    """

    return sum(deltas, starting_frequency)


def main(*argv):
    file_path = os.path.join(os.path.dirname(__file__), 'day_01.dat')

    with open(file_path, 'r') as fp:
        input_ = fp.read()
        
    deltas = parse_input(input_)

    new_frequency = get_frequency(deltas, starting_frequency=0)

    print(new_frequency)

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
