"""Advent of Code 2018 day 02 - https://adventofcode.com/2018/day/2"""

import collections
import functools
import itertools
import operator

import aoc.util 


def has_exactly_n_letters(label, n):
    """Return True if ``label`` has exactly ``n`` of any letter. Other, return False.

    Args:
        label (str): The string to scan.

    Returns:
        bool

    """

    letters = collections.Counter(label) 

    return n in letters.values()


def calculate_labels_checksum(labels):
    """Calculate the checksum of the labels.

    Args:
        labels (:obj:`list` of :obj:`str`): A list of label IDs

    Returns:
        int 

    """

    has_exactly_2_letters = functools.partial(has_exactly_n_letters, n=2)
    has_exactly_3_letters = functools.partial(has_exactly_n_letters, n=3)

    n2 = map(int, map(has_exactly_2_letters, labels))
    n3 = map(int, map(has_exactly_3_letters, labels))

    checksum = sum(n2) * sum(n3)

    return checksum 


def number_of_different_letters(a, b):
    """Return the number of difference between letters in the same position.
    
    Args:
        a (str): A string of letters
        b (str0: A string of letters

    Returns:
        int 

    """

    return sum(map(int, itertools.starmap(operator.ne, zip(a, b))))


def find_letters_in_common(a, b):
    """Return the letters in common between the two strings.
    
    Args:
        a (str): A string of letters
        b (str0: A string of letters

    Returns:
        str 

    """

    letters = [x for x, y in zip(a, b) if x == y]
    return ''.join(letters)


def main():
    input_ = aoc.util.get_puzzle_input(2)

    answer_01 = calculate_labels_checksum(input_)
    print(f"Part One: {answer_01}")

    pairs_of_labels = itertools.combinations(input_, 2)
    
    differs_by_exactly_one_letter = lambda x: number_of_different_letters(*x) == 1
    labels_that_differ_by_one_letter = filter(differs_by_exactly_one_letter, pairs_of_labels)
    letters_in_common = itertools.starmap(find_letters_in_common, labels_that_differ_by_one_letter)
    answer_02 = next(letters_in_common)
    print(f"Part Two: {answer_02}")


if __name__ == '__main__':
    main()
