import pytest

import aoc.day_11


EXAMPLE_FUEL_CELLS = [
    (8, (3, 5), 4),
    (57, (122, 79), -5),
    (39, (217, 196), 0),
    (71, (101, 153), 4),
]

EXAMPLE_CORNERS = [
    (18, 33, 45, 29),
    (42, 21, 61, 30),
]


@pytest.mark.parametrize('input_,coordinate,expected', EXAMPLE_FUEL_CELLS)
def test_fuel_cell_examples(input_, coordinate, expected):
    x, y = coordinate 

    actual = aoc.day_11.cell_power_level(x, y, input_)

    assert actual == expected


@pytest.mark.parametrize('grid_serial_number,x,y,power_level', EXAMPLE_CORNERS)
def test_top_left_corner_examples(grid_serial_number, x, y, power_level):
    grid = aoc.day_11.make_grid(grid_serial_number)

    actual = aoc.day_11.grid_power_level(grid, x, y,)

    assert actual == power_level


@pytest.mark.parametrize('grid_serial_number,x,y,power_level', EXAMPLE_CORNERS)
def test_grid_power_level_examples(grid_serial_number, x, y, power_level):
    grid = aoc.day_11.make_grid(grid_serial_number)

    actual, __ = aoc.day_11.find_highest_power_level(grid)

    assert actual == (x, y)
