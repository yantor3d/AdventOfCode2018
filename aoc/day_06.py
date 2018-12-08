import collections
import functools
import itertools
import math
import operator 
import sys
import string
import time

import aoc.util 

Point = collections.namedtuple('Point', 'x y')
BoundingBox = collections.namedtuple('BoundingBox', 'min max')


def parse_input(line):
    """Return the point declared in the line.

    Returns:
        Point

    """

    x, y = map(int, line.strip().split(','))

    return Point(x, y)


def get_bounding_box(points):
    """Return a bounding box that contains each point.

    Args:
        points (iterable)

    Returns:
        BoundingBox    
        
    """

    points = list(points)

    min_x = min(points, key=operator.attrgetter('x')).x
    min_y = min(points, key=operator.attrgetter('y')).y

    max_x = max(points, key=operator.attrgetter('x')).x
    max_y = max(points, key=operator.attrgetter('y')).y

    return BoundingBox(
        Point(min_x, min_y),
        Point(max_x, max_y),
    )


def get_points_in_bounding_box(bounding_box):
    """Return all points contained by the bounding box.

    Args:
        bounding_box (BoundingBox)

    Returns:
        list of Points

    """

    x_range = range(bounding_box.min.x, bounding_box.max.x + 1)
    y_range = range(bounding_box.min.y, bounding_box.max.y + 1)

    result = set(itertools.starmap(Point, itertools.product(x_range, y_range)))

    return result


def expand_bounding_box(bounding_box, amount):
    """Return a bounding box grown by ``amount``.

    Args:
        bounding_box (BoundingBox)
        amount (float): Amount of to grow the bounding box by.

    Returns:
        BoundingBox    

    """

    mn, mx = bounding_box

    amount = int(amount)

    mnx, mny = mn.x - amount, mn.y - amount
    mxx, mxy = mx.x + amount, mx.y + amount

    return BoundingBox(
        Point(int(mnx), int(mny)),
        Point(int(mxx), int(mxy)),
    )


def distance_between(a, b):
    """Return the distance between two points.

    Args:
        a (Point)
        b (Point)

    Returns:
        int

    """

    return abs(a.x - b.x) + abs(a.y - b.y)


def area_around(p):
    """Yield the point and the orthogonally adjacent points."""

    yield Point(p.x + 0, p.y + 0)
    yield Point(p.x + 1, p.y + 0)
    yield Point(p.x - 1, p.y + 0)
    yield Point(p.x + 0, p.y + 1)
    yield Point(p.x + 0, p.y - 1)


def grow_area(area):
    """Return the area grown by one unit orthogononally."""

    return set(itertools.chain.from_iterable(map(area_around, area)))


def is_on_boundary(point, bounding_box):
    """Return True if the point is on the edge of the bounding box.

    Args:
        point (Point)
        bounding_box (BoundingBox)

    Returns:       
        bool

    """

    bb = bounding_box
    p = point

    result = any(
        [
            p.x == bb.min.x and p.y in range(bb.min.y, bb.max.y),
            p.x == bb.max.x and p.y in range(bb.min.y, bb.max.y),
            p.y == bb.min.y and p.x in range(bb.min.x, bb.max.x),
            p.y == bb.max.y and p.x in range(bb.min.x, bb.max.x),
        ]
    )

    return result


def is_infinite(area, bounding_box):
    """Return True if an area is infinite. An infinite area has at least one 
    point on the boundary of the bounding box.

    Args:
        area (set of Point)
        bounding_box (BoundingBox)

    Returns:
        bool

    """

    return any([is_on_boundary(pnt, bounding_box) for pnt in area])


def get_closest_points(to_this_point, points):
    """Return the points that are closest to the given point.

    Args:
        to_this_point (Point)
        points (iterable of Point)

    Returns:
        set of Point
    """

    distances = {pnt: distance_between(pnt, to_this_point) for pnt in points}

    closest_distance = min(distances.values())

    result = {p for p in distances if distances[p] == closest_distance}

    return result 


def get_area_around_points(points):
    """Return the areas around each point. 

    Args:
        points (iterable)
        
    Returns:
        dict: Point -> int 
            A value of -1 means the area is infinite.

    """

    bb = get_bounding_box(points)
    bb = expand_bounding_box(bb, 1)

    whole_area = get_points_in_bounding_box(bb)

    result = {pnt: set() for pnt in points}

    for pnt in whole_area:
        closest_points = get_closest_points(pnt, points)

        if len(closest_points) == 1:
            cp = next(iter(closest_points))

            result[cp].add(pnt)

    for pnt, area in result.items():
        if is_infinite(area, bb):
            result[pnt] = -1
        else:
            result[pnt] = len(area)

    return result


def answer_part_01():
    lines = aoc.util.get_puzzle_input(6)
    points = list(map(parse_input, lines))

    area = get_area_around_points(points)
    answer_01 = max(area.values())

    print(f"Part One: {answer_01}")


def main():
    answer_part_01()


if __name__ == "__main__":
    main()