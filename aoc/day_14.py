"""Advent of Code 2018 day 14 - https://adventofcode.com/2018/day/14""

import aoc.util 
import time 


def make_recipes():
    """Yields the list of recipe scores after each individual recipe is added.

    Yields;
        int, list: Number of recipes, list of recipes. The list is pre-sized to 
            avoid repeated re-allocations.

    """

    max_size = 10000
    recipes = [None] * (max_size + 1)
    recipes[0] = 3
    recipes[1] = 7

    elf_a = 0
    elf_b = 1

    n = 2

    while True:
        new_score = recipes[elf_a] + recipes[elf_b]

        if new_score >= 10:
            b = new_score % 10 
            a = int((new_score - b) / 10)

            recipes[n] = a; n += 1
            yield n, recipes

            recipes[n] = b; n += 1
            yield n, recipes 
        else:      
            recipes[n] = new_score; n += 1
            yield n, recipes 

        elf_a = (elf_a + (1 + recipes[elf_a])) % n
        elf_b = (elf_b + (1 + recipes[elf_b])) % n 

        if n >= max_size:
            recipes.extend([None] * max_size)
            max_size *= 2


def answer_part_01(puzzle_input=None):
    """What are the scores of the ten recipes immediately after the number of 
    recipes in your puzzle input?
    
    """

    if puzzle_input is None:
        puzzle_input = aoc.util.get_puzzle_input(14)[0]
       
    n = int(puzzle_input)

    answer = ''

    for number_of_recipes, recipes in make_recipes():
        if number_of_recipes < n + 10:
            continue 

        answer = ''.join(map(str, recipes[n:n + 10]))
        break 

    return answer 


def answer_part_02(puzzle_input=None):
    """How many recipes appear on the scoreboard to the left of the score 
    sequence in your puzzle input?
    
    """

    if puzzle_input is None:
        puzzle_input = aoc.util.get_puzzle_input(14)[0]
       
    answer = -1

    puzzle_input = [int(p) for p in puzzle_input]
    n = len(puzzle_input)
    
    for number_of_recipes, recipes in make_recipes():       
        tail = recipes[number_of_recipes - n:number_of_recipes]

        if tail == puzzle_input:            
            answer = number_of_recipes - n
            break 

    return answer 


def main():
    start_time = time.time()
    answer_01 = answer_part_01()
    elapsed_time = time.time() - start_time
    print(f'Part one: {answer_01} took {elapsed_time:.2f} seconds')

    start_time = time.time()
    answer_02 = answer_part_02()    
    elapsed_time = time.time() - start_time
    print(f'Part two: {answer_02} took {elapsed_time:.2f} seconds')
    

if __name__ == "__main__":
    main()
