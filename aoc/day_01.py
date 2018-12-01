"""Advent of Code 2018 day 01 - https://adventofcode.com/2018/day/1"""

import collections
import itertools
import os 
import sys 



def parse_input(input_):
    """Parse the puzzle input.

    Args:
        input_ (str): A string of positive or negative frequency changes.

    Returns:
        :obj:`list` of :obj:`int`: A list of positive of negative frequency change values.
        
    """

    return list(map(int, input_.split()))


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

    def frequency_occurances(f):
        """Yield the frequency after applying each change."""

        deltas_ = itertools.cycle(deltas)

        while True:
            yield f
            f += next(deltas_)

    def is_occurance(n):       
        """Return True if the frequency has been hit for the nth time."""

        occurances = collections.Counter()

        def count_occurance(f):
            occurances[f] += 1
            return occurances[f] == n
        
        return count_occurance

    return next(filter(is_occurance(2), frequency_occurances(0)))


def main(*argv):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'day_01.dat')

    with open(file_path, 'r') as fp:
        input_ = fp.read()
        
    deltas = parse_input(input_)

    answer_01 = get_frequency(deltas)
    print(f"Part One: {answer_01}")

    answer_02 = get_first_frequency_reached_twice(deltas)    
    print(f"Part Two: {answer_02}")

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
