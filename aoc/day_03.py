"""Advent of Code 2018 day 03 - https://adventofcode.com/2018/day/3"""

import collections
import itertools
import re 

import aoc.util


Rectangle = collections.namedtuple('Rectangle', 'id left top width height')

rectangle_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def parse_rectangle(rect_desc):
    """Parses an rectangle description.

    Args:
        rect_desc (str): Description of a rectangle consisting.

    Returns:
        Rectangle

    """

    rect = rectangle_regex.split(rect_desc)[1:-1]

    return Rectangle(*map(int, rect))


def rectangle_coverage(rect):
    """Return the coordinates of each square inch covered by ``rect``.

    Args:
        rect (Rectangle)

    Returns:
        :obj:`set` of :obj:`tuple`(int, int)

    """

    return set(
        itertools.product(
            range(rect.left, rect.left + rect.width),
            range(rect.top, rect.top + rect.height)
        )
    )


def count_squares_coverage(rectangles):
    """Return a map of the number of rectangles covering each square.

    Args:
        rectangles (:obj:`list` of :obj:`Rectangle`)

    Returns:
        dict: ((int, int): int)
            The coordinates of each square inch covered by at least one rectangle,
            and the number of rectangles covering that square.

    """

    covered_squares = map(rectangle_coverage, rectangles)
    covered_squares = itertools.chain.from_iterable(covered_squares)

    number_of_times_a_square_is_covered = collections.Counter(covered_squares)

    return number_of_times_a_square_is_covered


# Part One solution
def shared_coverage(rectangles):
    """Return the coordinates of each square inch covered by two or more rectangles.

    Args:
        rectangles (:obj:`list` of :obj:`Rectangle`)

    Returns:
        list of (int, int)

    """

    number_of_times_a_square_is_covered = count_squares_coverage(rectangles)

    squares_covered_by_two_or_more_rectangles = (
        s for s, n 
        in number_of_times_a_square_is_covered.items()
        if n >= 2
    )

    return list(squares_covered_by_two_or_more_rectangles)


# Part Two solution
def rectangle_without_overlap(rectangles):
    """Return the rectangle that is not overlapped by any other rectangle.

    Args:
        rectangles (:obj:`list` of :obj:`Rectangle`)

    Returns:
        Rectangle

    """
    
    squares_coverage = count_squares_coverage(rectangles)
    number_of_times_a_square_is_covered = squares_coverage.__getitem__

    def is_overlapped(rect):
        squares = rectangle_coverage(rect)
        coverage = sum(map(number_of_times_a_square_is_covered, squares))
        return len(squares) != coverage

    return next(itertools.filterfalse(is_overlapped, rectangles), None)


def main():
    input_ = aoc.util.get_puzzle_input(3)

    rectangles = list(map(parse_rectangle, input_))

    answer_01 = len(shared_coverage(rectangles))
    print(f"Part one: {answer_01}")

    answer_02 = rectangle_without_overlap(rectangles)
    print(f"Part one: {answer_02}")


if __name__ == "__main__":
    main()
