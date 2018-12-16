import collections
import operator
import queue
import sys
import string 
import time 

import aoc.util

Point = collections.namedtuple('Point', 'x y')

ELF = 'E'
GOBLIN = 'G' 
WALL = '#'
FLOOR = '.'


class Actor(object):
    __slots__ = ['id', 'type', 'position', 'hit_points', 'attack_points']

    def __init__(self, id_, type_, position, hit_points, attack_points):
        self.id = id_ 
        self.type = type_
        self.position = position
        self.hit_points = hit_points
        self.attack_points = attack_points

    def __hash__(self):
        return self.id 

    def __str__(self):
        return '{}{}({:>3d}/{:>3d})'.format(self.type, self.name(), self.attack_points, self.hit_points)

    def name(self):
        id_ = (string.ascii_uppercase if self.type == ELF else string.ascii_lowercase)[self.id]
        return '({})'.format(id_) if self.type == ELF else '[{}]'.format(id_)


class Game(object):
    def __init__(self, x, y, tiles, walls, elves, goblins):
        self.x = x
        self.y = y
        self.tiles = tiles 
        self.walls = walls
        self.elves = elves 
        self.goblins = goblins

        self.debug = False
        self.draw = False

        self.elves_must_not_die = False

    def __iter__(self):
        actors = self.elves + self.goblins 
        actors.sort(key=lambda a: reading_order(a.position))

        for actor in actors:
            yield actor 

    def print_me(self, num_full_rounds):
        lines = [[' . ' for _ in range(self.x + 1)] for _ in range(self.y + 1)]

        for x, y in self.walls:            
            lines[y][x] = ' # ' 

        for x, y in self.tiles:            
            lines[y][x] = ' . ' 

        for each in self:
            x, y = each.position
            lines[y][x] = each.name()

        print('\nAfter {} rounds'.format(num_full_rounds))
        for i, line in enumerate(lines):
            actors = [a for a in self if a.position.y == i]
            actors = ', '.join([str(a) for a in actors])
            print(''.join(line), actors)

    def play(self, elf_power=3):
        num_full_rounds = 0

        running = True 

        for elf in self.elves:
            elf.attack_points = elf_power

        while running:
            if self.draw:
                self.print_me(num_full_rounds)

            for actor in self:
                if actor.hit_points <= 0:
                    continue 
                    
                if not self._take_turn(actor):
                    running = False
                    break
            else:
                num_full_rounds += 1

        if self.draw:
            self.print_me(num_full_rounds)

        survivors = self.elves or self.goblins
        hit_points = [each.hit_points for each in survivors]

        hit_points = sum(hit_points)

        return num_full_rounds, hit_points, num_full_rounds * hit_points

    def _take_turn(self, actor):     
        targets = self.elves if actor.type == GOBLIN else self.goblins

        if not targets:
            return False

        adjacent_targets = [
            target for target in targets 
            if actor.position in adjacent(target.position)
        ]

        if not adjacent_targets:
            paths_to_targets = {}

            for target in targets:
                try:
                    paths_to_targets[target] = self.find_path(actor.position, target.position)
                except LookupError:
                    pass                  

            if paths_to_targets:
                targets = sorted(paths_to_targets, key=lambda t: len(paths_to_targets[t]))
                closest_target = next(iter(targets), None)

                if closest_target is not None:
                    path_to_target = paths_to_targets[closest_target]
                    actor.position = path_to_target[1]

                    if self.debug:
                        print(str(actor), "moved to attack", str(closest_target))

        adjacent_targets = [
            target for target in targets 
            if actor.position in adjacent(target.position)
        ]

        if adjacent_targets:
            target_hit_points = collections.defaultdict(list)

            for target in adjacent_targets:
                target_hit_points[target.hit_points].append(target) 

            hp = min(target_hit_points)

            target = sorted(target_hit_points[hp], key=lambda t: reading_order(t.position))[0]

            self.make_attack(actor, target)

        return True 

    def make_attack(self, actor, target):
        target.hit_points -= actor.attack_points

        if target.hit_points <= 0:
            if target.type == ELF:
                if self.elves_must_not_die:
                    raise RuntimeError("An elf died.")

                self.elves.remove(target)
            elif target.type == GOBLIN:
                self.goblins.remove(target)

        if self.debug:
            print(str(actor), "attacked", str(target))

    def find_path(self, start, end):
        distances = {end: 0} 

        tiles = queue.Queue()
        tiles.put(end)

        occupied = set([actor.position for actor in self])
        occupied.remove(start)

        while not tiles.empty():
            this_tile = tiles.get()
            this_cost = distances[this_tile]

            for next_tile in adjacent(this_tile):
                if not next_tile in self.tiles:
                    continue 

                if next_tile in occupied:
                    continue
            
                try:
                    next_cost = distances[next_tile]

                    if this_cost + 1 >= next_cost:
                        continue 
                except KeyError:
                    pass

                distances[next_tile] = this_cost + 1

                tiles.put(next_tile)

            if start in distances:
                break
                
        path = [start]     

        cost = distances[start] 

        while True:            
            cost -= 1 
            this_tile = path[-1] 

            next_tiles = [
                n for n in adjacent(this_tile) 
                if distances.get(n, -10) == cost 
                and n not in path 
            ]

            next_tiles.sort(key=reading_order)

            if next_tiles:
                path.append(next_tiles[0])
            else:
                raise LookupError()

            if path[-1] == end:
                break  
        
        return path


def parse_input(lines):
    tiles = set()
    walls = set()
    goblins = []
    elves = []

    max_x = 0
    max_y = 0 

    for y, line in enumerate(lines):
        max_y = max([max_y, y])

        for x, char in enumerate(line):
            max_x = max([max_x, x])

            if char == WALL:
                walls.add(Point(x, y))  
            else:
                tiles.add(Point(x, y))

            if char == GOBLIN:
                goblins.append(Actor(len(goblins), GOBLIN, Point(x, y), 200, 3))
            elif char == ELF:
                elves.append(Actor(len(elves), ELF, Point(x, y), 200, 3))

    return Game(x, y, tiles, walls, elves, goblins)


def reading_order(point):
    """Return the reading order of the point (top to bottom, left to right).

    Args:
        point (Point): A tile in the dungeon

    Returns:
        (int, int)

    """

    return point.y, point.x


def distance_between(a, b):
    """Return the Manhatten Distance between two points.
    
    Returns:
        int 
    """

    return abs(a.x - b.x) + abs(a.y - b.y)


def get_closest_point(to_this_point, points):
    """Get the point that is closest to this point."""

    distances = collections.defaultdict(list)

    for point in points:
        d = distance_between(point, to_this_point)
        distances[d].append(point)

    closest_distance = min(distances)

    closest_points = distances[closest_distance]
    closest_points.sort(key=reading_order)

    return closest_points[0]


def adjacent(point):
    p = point 

    return {
        Point(p.x + 1, p.y + 0),
        Point(p.x - 1, p.y + 0),
        Point(p.x + 0, p.y + 1),
        Point(p.x + 0, p.y - 1),
    }


def part_01():
    start_time = time.time()
    puzzle_input = aoc.util.get_puzzle_input(15)

    game = parse_input(puzzle_input)
    __, __, score = game.play()
    elapsed_time = time.time() - start_time

    print (f'Part one: {score} took {elapsed_time:0.2f} seconds')


def part_02():
    start_time = time.time()
    puzzle_input = aoc.util.get_puzzle_input(15)

    # Do a manual binary search to find the minimum power levels 
    # so that none of the elves die.
    power = 14
    game = parse_input(puzzle_input)
    game.elves_must_not_die = True
    __, __, score = game.play(power)        
    elapsed_time = time.time() - start_time

    print (f'Part two: {score} took {elapsed_time:0.2f} seconds')


def main():
    # part_01()
    part_02()


if __name__ == "__main__":
    main()
