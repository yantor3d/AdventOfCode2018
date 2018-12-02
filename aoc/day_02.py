import collections
import functools

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


def main():
    input_ = aoc.util.get_puzzle_input(2)

    answer_01 = calculate_labels_checksum(input_)
    print(f"Part One: {answer_01}")


if __name__ == '__main__':
    main()
