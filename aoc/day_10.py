"""Advent of Code 2018 day 10 - https://adventofcode.com/2018/day/10"""

import collections
import operator
import re

import aoc.util

Vector = collections.namedtuple('Vector', 'x y')
Particle = collections.namedtuple('Particle', 'position velocity')
BoundingBox = collections.namedtuple('BoundingBox', 'min max')

INPUT_REGEX = re.compile(r'position=<([\d -]*),([\d -]*)> velocity=<([\d -]*),([\d -]*)>')


def parse_input(line):
    """Parse a line of the puzzle input.
    
    Args:
        line (str)

    Returns:
        Particle

    """

    px, py, vx, vy = map(int, INPUT_REGEX.findall(line)[0])

    return Particle(
        Vector(px, py),
        Vector(vx, vy)
    )


def print_output(particles):
    """Print the positions of each particle."""
    
    bb = get_bounding_box(particles)

    x = abs(bb.max.x - bb.min.x)
    y = abs(bb.max.y - bb.min.y)

    lines = [['.' for _ in range(x + 1)] for _ in range(y + 1)]

    points = [par.position for par in particles]

    for p in points:
        x = p.x - bb.min.x 
        y = p.y - bb.min.y 

        lines[y][x] = '#'

    for line in lines:
        print(''.join(line))


def get_bounding_box(particles):
    """Return a bounding box that contains all the particles.

    Args:
        particles (iterable)

    Returns:
        BoundingBox    
        
    """

    points = [p.position for p in particles]

    min_x = min(points, key=operator.attrgetter('x')).x
    min_y = min(points, key=operator.attrgetter('y')).y

    max_x = max(points, key=operator.attrgetter('x')).x
    max_y = max(points, key=operator.attrgetter('y')).y

    return BoundingBox(
        Vector(min_x, min_y),
        Vector(max_x, max_y),
    )


def area(bounding_box):    
    """Return the area of the bounding box.

    Args:
        bounding_box (BoundingBox)

    Returns:
        int 

    """

    bb = bounding_box
    x = abs(bb.max.x - bb.min.x)
    y = abs(bb.max.y - bb.min.y)

    return x * y 


def tick(particles):
    """Return the position of each particle in the next frame.

    Args:
        particles (list of Particle)

    Returns:
        list of Particle

    """

    def next_frame(particle):
        p = particle.position
        v = particle.velocity

        return Particle(
            Vector(p.x + v.x, p.y + v.y),
            particle.velocity
        )

    return list(map(next_frame, particles))


def answer_it(particles=None):
    """Find the image created by the particles when the are in alignment.
    
    Returns:
        int: Amount of time it took for the image to form.

    """

    if particles is None:
        puzzle_input = aoc.util.get_puzzle_input(10)
        particles = list(map(parse_input, puzzle_input))

    this_frame = particles

    elapsed_time = 0

    last_frame = this_frame
    smallest_area = area(get_bounding_box(this_frame))

    while True:
        last_frame = this_frame 
        this_frame = tick(this_frame)

        bb = get_bounding_box(this_frame)
        a = area(bb) 

        if a < smallest_area:
            smallest_area = a
        else:
            break

        elapsed_time += 1

    return elapsed_time, last_frame


def main():
    answer, image = answer_it()

    print(f"Part one:")
    print_output(image)
    print(f"Part two: {answer}")


if __name__ == "__main__":
    main()
