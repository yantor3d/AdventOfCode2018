import collections
import itertools
import queue
import time 
import sys 

import aoc.util 

Point = collections.namedtuple('Point', 'x y')
Drop = collections.namedtuple('Drop', 'position direction')

FLOW_DOWN = Point(0, 1)
FLOW_LEFT = Point(-1, 0)
FLOW_RIGHT = Point(1, 0)


def parse_scan(v):
    if '..' in v:
        mn, mx = v.split('..')

        for n in range(int(mn), int(mx) + 1):
            yield n 
    else:
        yield int(v)


def parse_line(line):
    a, b = line.split(', ')

    a, av = a.split('=')
    b, bv = b.split('=')

    xs = parse_scan(av if a == 'x' else bv)
    ys = parse_scan(av if a == 'y' else bv)

    for x, y in itertools.product(xs, ys):
        yield Point(x, y)


def parse_input(lines):
    result = set()

    for line in lines:
        result.update(parse_line(line))

    return result


def print_it(clay, damp_sand, the_water, water=None):
    xs = [p.x for p in clay]
    ys = [p.y for p in clay]

    nx, ny = min(xs), min(ys)
    mx, my = max(xs), max(ys) 

    lines = [['.' for _ in range(mx - nx + 10)] for _ in range(my + 1)]

    for p in clay:
        lines[p.y][p.x - nx + 1] = '#'

    for p in damp_sand:
        lines[p.y][p.x - nx + 1] = '|'

    for p in the_water:
        lines[p.y][p.x - nx + 1] = '~'

    lines[0][500 - nx + 1] = '+'

    if water is not None:
        lines[water.y - ny + 1][water.x - nx + 1] = 'X'

    text = '\n'.join([''.join(line) for line in lines])

    with open('out.txt', 'w') as fp:
        fp.write(text)
        
    # print('')
    # print(text)
           

class Scan(object):
    def __init__(self, clay):
        self.clay = clay

        self.damp_sand = set() 
        self.the_water = set()

        self.last_drop = set()

        self.states = collections.deque(maxlen=20)

        self.flowing_water = queue.Queue()
        self.stack = collections.deque()

        self.edge_of_the_map_x = max([p.x for p in self.clay]) + 1
        self.edge_of_the_map_y = max([p.y for p in self.clay])

    def fill_column(self, from_point):
        """Fill the water downward until it hits clay.
        
        Args:
            from_point (Point): Where the water is flowing from.

        Returns:
            set, set
                The water that is flowing, but hit clay
                The water that is flowing forever

        """

        falling = set()
        flowing = set([from_point]) 

        fill = queue.Queue()
        fill.put(from_point)

        while True:
            if fill.empty():
                break 

            p = fill.get()

            # Flow down
            f = Point(p.x, p.y + 1)

            if f in self.clay or f in self.the_water:
                break 
            else:
                if f.y > self.edge_of_the_map_y:
                    falling.add(f)
                else:
                    flowing.add(f)
                    fill.put(f)

        return flowing, falling

    def fill_row(self, from_point):
        """Fill the water outward until it hits clay, or is above sand
        
        Args:
            from_point (Point): Where the water is flowing from.

        Returns:
            set, set
                The water that resting on clay or other way
                The water that will continue to flow downward
        """

        pooled = set([from_point])
        flowing = set()

        fill = queue.Queue()
        fill.put((from_point, +1))
        fill.put((from_point, -1))
        
        while True:
            if fill.empty():
                break 

            p, d = fill.get() 

            f = Point(p.x + d, p.y)

            if f.x < 0 or f.x > self.edge_of_the_map_x:
                return set(), set()

            if f not in self.clay:
                b = Point(f.x, f.y + 1)

                if b in self.clay or b in self.the_water:
                    pooled.add(f)
                    fill.put((f, d))
                else:
                    flowing.add(f) 

        return pooled, flowing
                
    def is_finished(self):
        last_state = self.states[-1]

        for state in self.states:
            if state != last_state:
                return False
        else:
            max_y = max([p.y for p in self.damp_sand])

            return max_y >= self.edge_of_the_map_y - 1

    def back_track(self):
        while True:
            if not self.stack:
                break

            water = self.stack.pop()

            if water in self.the_water:
                continue 

            if water in self.last_drop:
                continue

            self.flowing_water.put(water)
            break 

    def simulate(self):
        self.flowing_water.put(Point(500, 1)) 

        p = -1

        start_time = time.time()
        elapsed_time = 0.0

        while True:
            state = len(self.damp_sand | self.the_water)
            self.states.append(state)

            if self.flowing_water.empty():
                self.damp_sand -= self.the_water
                
                if self.is_finished():
                    break
                else:
                    self.back_track()

            if self.flowing_water.empty():
                break 

            water = self.flowing_water.get()

            if water in self.the_water:
                continue 
            
            if water in self.last_drop:
                continue

            self.damp_sand.add(water)

            flow, fall = self.fill_column(water)

            self.damp_sand.update(flow)
                    
            if fall:  # water fell off the edge of the map
                fall = [f for f in fall if f.y < self.edge_of_the_map_y]
                self.damp_sand.update(fall)
                self.last_drop.add(water)
            else:  # water fell onto clay or pooled water
                self.stack.append(water)
                flow = sorted(flow, key=lambda p: p.y, reverse=True)    

                for f in flow:
                    if f in self.the_water:
                        continue 

                    fill, fall = self.fill_row(f)
                    
                    self.damp_sand.update(fill)
                    self.damp_sand.update(fall)

                    if fall:  # water has overflowed a container
                        for each in fall:
                            self.flowing_water.put(each)
                        break 
                    else:
                        self.the_water.update(fill)
                else:  
                    # Find where the water is pouring into the container from and resume the pour. 
                    up = Point(f.x, f.y - 1)

                    fill, fall = self.fill_row(up)

                    if fall:
                        self.damp_sand.update(fill)

                        for each in fall:
                            self.flowing_water.put(each)
                    else:
                        for f in fill:
                            if f in self.damp_sand:
                                self.flowing_water.put(f)
                                break

            max_y = max([p.y for p in self.the_water])
            percent = int((max_y / self.edge_of_the_map_y) * 100)

            if percent > p:
                elapsed_time = time.time() - start_time
                percent_str = f' {percent:>3d}% '
                progress_str = f'{percent_str:^100}'
                progress_bar = list(progress_str)

                for i, c in enumerate(progress_bar):
                    if c == ' ' and i < percent:
                        progress_bar[i] = '='

                progress_bar = ''.join(progress_bar)
                progress_bar = f'\r[{progress_bar}] {elapsed_time:8.2f}'
                sys.stdout.write(progress_bar)
                sys.stdout.flush()
                
            p = percent

        min_y = min([p.y for p in self.clay])
        max_y = max([p.y for p in self.clay])

        self.damp_sand = {
            w for w in self.damp_sand
            if (min_y <= w.y <= max_y)
        }

        return self.damp_sand, self.the_water


def main():
    """
    Part one: 
        How many tiles can the water reach within the range of y values in your scan?
    Part two: 
        How many water tiles are left after the water spring stops producing 
        water and all remaining water not at rest has drained?

    """

    puzzle_input = aoc.util.get_puzzle_input(17)
    clay = parse_input(puzzle_input)
    start_time = time.time()
    damp, wet = Scan(clay).simulate()
    elapsed_time = time.time() - start_time 

    answer_01 = len(damp | wet)
    answer_02 = len(wet)

    print('')
    print(f'Part one: {answer_01}')
    print(f'Part two: {answer_02}')
    print(f'Took {elapsed_time:.2f} seconds)')


if __name__ == "__main__":
    main()
