"""Advent of Code 2018 day 10 - https://adventofcode.com/2018/day/10"""

import collections
import sys 

import aoc.util

Point = collections.namedtuple('Point', 'x y')


def cell_power_level(x, y, grid_serial_number):
    """Return the power level of the cell.

    Args:
        x (int): X coordinate of the power cell
        y (int): Y coordinate of the power cell
        grid_serial_number (int)

    Returns:
        int 

    """

    rack_id = x + 10

    power = rack_id * y
    power += grid_serial_number
    power = power * rack_id 

    try:
        power = int(str(power)[-3])
    except IndexError:
        power = 0

    power -= 5

    return power 


def grid_power_level(grid, x, y):
    """Get the power level of the 3x3 square within the grid.

    Args:
        grid (dict): (x, y) -> power level
        x (int): X coordinate of the top left of the square.
        y (int): Y coordinate of the top left of the square.

    Returns:
        int 

    """

    result = 0

    for a in range(3):
        for b in range(3):
            result += grid[x + a, y + b]

    return result     


def make_grid(grid_serial_number):
    """Make a 300x300 grid of power cells.

    Args:
        grid_serial_number (int)

    Returns:
        dict: (x, y) -> power level

    """

    result = {}

    for x in range(1, 301):
        for y in range(1, 301):
                result[x, y] = cell_power_level(x, y, grid_serial_number)
            
    return result 


def find_highest_power_level(grid):
    """Find the 3x3 square with the highest power level.

    Args:
        grid (dict): (x, y) -> power level

    Returns:
        (int, int) - Top left coordinate of the square

    """

    result = (-1, -1)
    max_power = -sys.maxsize

    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            power_level = grid_power_level(grid, x, y)

            if power_level > max_power:
                max_power = power_level
                result = (x, y)

    return result    


def answer_part_01():
    """What is the X,Y coordinate of the top-left fuel cell of the 3x3 square 
    with the largest total power?
    
    """

    puzzle_input = int(aoc.util.get_puzzle_input(11)[0])

    grid = make_grid(puzzle_input)
    x, y = find_highest_power_level(grid)

    print(f'Part one: {x},{y}')


def main():
    answer_part_01()


if __name__ == "__main__":
    main()
