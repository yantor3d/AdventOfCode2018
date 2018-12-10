"""Advent of Code 2018 day 05 - https://adventofcode.com/2018/day/5"""

import string
import time 

import aoc.util 


REACTS_WITH = {}
REACTS_WITH.update(zip(string.ascii_lowercase, string.ascii_uppercase))
REACTS_WITH.update(zip(string.ascii_uppercase, string.ascii_lowercase))

REACTIONS_UNITS = [''.join(each) for each in REACTS_WITH.items()]


def react_with(unit, polymer):
    """Return the polymer after removing one adjacent reactive unit."""

    return polymer.replace(unit, '', 1)


def react(polymer):
    """Return the polymer after removing adjacent reactive units."""

    for unit in REACTIONS_UNITS:
        polymer = react_with(unit, polymer)

    return polymer


def remove(units, polymer):
    """Remove all instances of ``units`` from polymer."""
    
    return ''.join([u for u in polymer if u not in units])


def solve(polymer):
    """Return the stable polymer after removing all adjacent reactive units."""

    while True:
        old_polymer, polymer = polymer, react(polymer)

        if old_polymer == polymer:
            break 

    return polymer 


def anmswer_part_01(polymer):
    """Calculate the polymer after all unstable units react with each other."""

    return solve(polymer)


def answer_part_02(polymer):
    """Calculate the shortest polymer that can be achieved by removing exactly
    one type of unit.

    """

    polymers = []

    for u, L in zip(string.ascii_uppercase, string.ascii_lowercase):
        units = u + L 
        sliced_polymer = remove(units, polymer)
        solved_polymer = solve(sliced_polymer)

        polymers.append(solved_polymer)

    polymers.sort(key=len)
    shortest_polymer = next(iter(polymers))

    return shortest_polymer


def main():
    input_ = aoc.util.get_puzzle_input(5)[0]

    start_time = time.time()
    answer_01 = len(anmswer_part_01(input_))
    elapsed_time = time.time() - start_time

    print(f"Part one: {answer_01} - solved in {elapsed_time:0.2f} seconds")

    start_time = time.time()
    answer_02 = len(answer_part_02(input_))
    elapsed_time = time.time() - start_time

    print(f"Part two: {answer_02} - solved in {elapsed_time:0.2f} seconds")


if __name__ == "__main__":
    main()
