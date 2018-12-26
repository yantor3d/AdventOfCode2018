import collections
import itertools
import queue
import sys  
import time

import aoc.util 

TURNS = {'N': -1j, 'S': 1j, 'E': 1, 'W': -1} 
 

def route_lengths(route):
    distances = collections.defaultdict(int)
    positions = []

    x = 0
    p = x 

    for turn in route:
        if turn == '(':
            positions.append(p)
        elif turn == ')':
            x = positions.pop()
        elif turn == '|':
            x = positions[-1]
        else:
            d = TURNS[turn] 
            x += d 
        
            if distances[x]:
                distances[x] = min(distances[x], distances[p]+ 1)
            else:
                distances[x] = distances[p] + 1

        p = x 

    return distances.values()
    

def answer_part_01():
    route, = aoc.util.get_puzzle_input(20)

    start_time = time.time()
    answer = max(route_lengths(route[1:-1]))
    elapsed_time = time.time() - start_time 

    print(f'Part one: {answer} (took {elapsed_time:.2f} seconds')


def answer_part_02():
    route, = aoc.util.get_puzzle_input(20)

    start_time = time.time()
    answer = route_lengths(route[1:-1])
    answer = len([a for a in answer if a >= 1000])
    elapsed_time = time.time() - start_time 

    print(f'Part two: {answer} (took {elapsed_time:.2f} seconds')


def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()