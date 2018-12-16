"""Advent of Code 2018 day 13 - https://adventofcode.com/2018/day/13"""

import itertools

import aoc.util 


TURN_RIGHT = +1 
STRAIGHT_AHEAD = 0
TURN_LEFT = -1

CART_TO_TRACK = {
    '<': '-',
    '>': '-',
    '^': '|',
    'v': '|',
}

DIRECTIONS = {
    '<': (-1, 0),
    '>': (+1, 0),
    '^': (0, -1),
    'v': (0, +1),
}

CORNERS = {
    ('^', ord('/')): '>',
    ('^', ord('\\')): '<',
    ('v', ord('/')): '<',
    ('v', ord('\\')): '>',
    ('>', ord('/')): '^',
    ('>', ord('\\')): 'v',
    ('<', ord('/')): 'v',
    ('<', ord('\\')): '^',
}

TURNS = {
    (TURN_LEFT, '>'): '^',
    (TURN_LEFT, '<'): 'v',
    (TURN_LEFT, 'v'): '>',
    (TURN_LEFT, '^'): '<',
    (TURN_RIGHT, '>'): 'v',
    (TURN_RIGHT, '<'): '^',
    (TURN_RIGHT, 'v'): '<',
    (TURN_RIGHT, '^'): '>',
}


class Mine(object):
    def __init__(self, size, tracks, carts, remove_collisions=False):
        self.tracks = tracks 
        self.carts = carts 
        self.size = size

        self.remove_collisions = remove_collisions

    def tick(self):
        collisions = set()

        carts = sorted(self.carts.values(), key=lambda c: (c.y, c.x))
        
        for cart in carts:
            if cart.id not in self.carts:
                continue 

            dx, dy = DIRECTIONS[cart.direction]
            nx, ny = cart.x + dx, cart.y + dy

            track = self.tracks[nx, ny]

            if track == ord('+'):
                move = next(cart)
            elif track in [ord('-'), ord('|')]:
                move = cart.direction
            else:
                move = CORNERS[cart.direction, track]

            cart.direction = move
            cart.x, cart.y = nx, ny

            for other in self.carts.values():
                if other.id == cart.id:
                    continue 

                if cart.x == other.x and cart.y == other.y: 
                    collisions.add((cart.x, cart.y))
                    self.carts.pop(cart.id)
                    self.carts.pop(other.id)
                    break
            
            if collisions and not self.remove_collisions:
                break

        return list(collisions)


class Cart(object):
    def __init__(self, direction, id_, x, y):
        self.direction = direction 
        self.id = id_
        self.x = x 
        self.y = y 

        self._turns = itertools.cycle([TURN_LEFT, STRAIGHT_AHEAD, TURN_RIGHT])

    def __next__(self):
        turn = next(self._turns)        
        return TURNS.get((turn, self.direction), self.direction)

        
def parse_input(lines):
    tracks = {}
    carts = {}

    sx, sy = -1, -1

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            sx = max(x, sx)
            sy = max(y, sy)

            if char == ' ':
                continue 

            if char in CART_TO_TRACK:
                cart = Cart(char, len(carts), x, y)
                carts[cart.id] = cart 

                char = CART_TO_TRACK[char]
            
            tracks[x, y] = ord(char)

    return Mine((sx, sy), tracks, carts)


def simulate(mine):
    result = None 

    while True:         
        collisions = mine.tick()

        if collisions and not mine.remove_collisions:
            result = collisions[0]
            break

        if len(mine.carts) == 1:
            last_cart = list(mine.carts.values())[0]
            result = (last_cart.x, last_cart.y)
            break

    return result


def answer_part_01():
    puzzle_input = aoc.util.get_puzzle_input(13, raw=True)
    mine = parse_input(puzzle_input)

    answer = simulate(mine)
    
    print(f'Part one: {answer}')


def answer_part_02():
    puzzle_input = aoc.util.get_puzzle_input(13, raw=True)
    mine = parse_input(puzzle_input)
    mine.remove_collisions = True 

    answer = simulate(mine)
    
    print(f'Part two: {answer}')


def main():
    answer_part_01()
    answer_part_02()


if __name__ == '__main__':
    main()
