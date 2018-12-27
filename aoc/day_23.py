"""Advent of Code day 23 - https://adventofcode.com/2018/day/23"""

import collections
import itertools 
import re 

import aoc.util

Point = collections.namedtuple('Point', 'x y z')
Nanbot = collections.namedtuple('Nanbot', 'position signal_range')

INPUT_REGEX = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')


def parse_input(lines):
    result = [] 

    for line in lines:
        x, y, z, r = map(int, INPUT_REGEX.findall(line)[0])

        p = Point(x, y, z)
        result.append(Nanbot(p, r))

    return result 


def most_nanobots_in_range(bots):
    highest_signal = -1
    result = 0

    for a in bots:
        if a.signal_range > highest_signal:
            highest_signal = a.signal_range
            result = 0
        else:
            continue 

        for b in bots:
            d = manhatten_distance(a.position, b.position)

            if d <= a.signal_range:
                result += 1

    return result


def manhatten_distance(a, b):
    return abs(b.x - a.x) + abs(b.y - a.y) + abs(b.z - a.z)


def answer_part_01():
    """Find the nanobot with the largest signal radius. How many nanobots are in range of its signals?"""

    puzzle_input = aoc.util.get_puzzle_input(23)
    bots = parse_input(puzzle_input)

    answer = most_nanobots_in_range(bots)

    print(f'Part one: {answer}')


def answer_part_02():
    pass


def main():
    answer_part_01()
    answer_part_02() 


if __name__ == "__main__":
    main()