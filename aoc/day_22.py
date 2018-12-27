"""Advent of Code 2018 day 21 - https://adventofcode.com/2018/day/21"""

import aoc.util 

TILES = ['.', '=', '|']


def print_it(tiles, target):
    lines = []

    for row in tiles:
        lines.append([])

        for tile in row:
            i = tile % 3
            lines[-1].append(TILES[i])

    lines[0][0] = 'M'
    tx, ty = target 
    lines[ty][tx] = 'T' 

    lines = [''.join(line) for line in lines]
    text = '\n'.join(lines)

    print('')
    print(text)


def get_cave_tiles(cave_depth, target_coordinates, extend=2):
    ox, oy = 0, 0

    tx, ty = target_coordinates
    mx = int(tx * max(1.0, extend))
    my = int(ty * max(1.0, extend))

    M = 20183 

    tiles = [[-1 for _ in range(mx + 1)] for _ in range(my + 1)]

    for x in range(mx + 1):
        tiles[0][x] = ((x * 16807) + cave_depth) % M

    for y in range(my + 1):
        tiles[y][0] = ((y * 48271) + cave_depth) % M

    tiles[0][0] = (0 + cave_depth) % M
    tiles[ty][tx] = (0 + cave_depth) % M

    result = 0

    for y in range(1, my + 1):
        for x in range(1, mx + 1):
            if (x, y) == (tx, ty):
                continue 
            
            a = tiles[y][x - 1]
            b = tiles[y - 1][x]

            tiles[y][x] = ((a * b) + cave_depth) % M
            
    return tiles 


def calculate_risk(cave_depth, target_coordinates):
    ox, oy = 0, 0
    tx, ty = target_coordinates

    tiles = get_cave_tiles(cave_depth, target_coordinates, extend=1)

    result = 0 

    for row in tiles[:ty + 1]:
        for tile in row[:tx + 1]:
            result += (tile % 3)
    
    return result 


def answer_part_01():
    depth = 4848
    target = (15, 700)

    answer = calculate_risk(depth, target)

    print(f'Part one: {answer}')

def main():
    answer_part_01()


if __name__ == "__main__":
    main()