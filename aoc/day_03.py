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


def shared_coverage(rectangles):
    """Return the coordinates of each square inch covered by two or more rectangles.


    Args:
        rectangles (:obj:`list` of :obj:`Rectangle`)

    Returns:
        :obj:`set` of `

    """

    covered_squares = map(rectangle_coverage, rectangles)
    covered_squares = itertools.chain.from_iterable(covered_squares)

    number_of_times_a_square_is_covered = collections.Counter(covered_squares)

    squares_covered_by_two_or_more_rectangles = (
        s for s, n 
        in number_of_times_a_square_is_covered.items()
        if n >= 2
    )

    return len(list(squares_covered_by_two_or_more_rectangles))


def main():
    input_ = aoc.util.get_puzzle_input(3)

    rectangles = list(map(parse_rectangle, input_))

    answer_01 = shared_coverage(rectangles)
    print(f"Part one: {answer_01}")


if __name__ == "__main__":
    main()
