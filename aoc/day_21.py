"""Advent of Code 2018 day 21 - https://adventofcode.com/2018/day/21"""

import collections
import sys
import time 

import aoc.util 

Instruction = collections.namedtuple('Instruction', 'op a b c')


def addr(reg, a, b, c):
    """Stores into register C the result of adding register A and register B."""

    reg[c] = reg[a] + reg[b] 


def addi(reg, a, b, c):
    """Stores into register C the result of adding register A and value B."""

    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    """Stores into register C the result of multiplying register A and register B."""

    reg[c] = reg[a] * reg[b] 


def muli(reg, a, b, c):    
    """Stores into register C the result of multiplying register A and value B."""

    reg[c] = reg[a] * b 


def banr(reg, a, b, c):
    """Stores into register C the result of the bitwise AND of register A and register B."""

    reg[c] = reg[a] & reg[b] 


def bani(reg, a, b, c):
    """Stores into register C the result of the bitwise AND of register A and value B."""

    reg[c] = reg[a] & b 


def borr(reg, a, b, c):
    """Stores into register C the result of the bitwise OR of register A and register B."""

    reg[c] = reg[a] | reg[b] 


def bori(reg, a, b, c):
    """Stores into register C the result of the bitwise OR of register A and value B."""

    reg[c] = reg[a] | b 


def setr(reg, a, b, c):
    """Copies the contents of register A into register C. (Input B is ignored.)"""

    reg[c] = reg[a] 


def seti(reg, a, b, c):
    """Stores value A into register C. (Input B is ignored.)"""

    reg[c] = a 


def gtir(reg, a, b, c):
    """Sets register C to 1 if value A is greater than register B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(a > reg[b])
    

def gtri(reg, a, b, c):
    """Sets register C to 1 if register A is greater than value B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(reg[a] > b)


def gtrr(reg, a, b, c):
    """Sets register C to 1 if register A is greater than register B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(reg[a] > reg[b])


def eqir(reg, a, b, c):
    """Sets register C to 1 if value A is equal to register B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(a == reg[b])


def eqri(reg, a, b, c):
    """Sets register C to 1 if register A is equal to value B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(reg[a] == b)


def eqrr(reg, a, b, c):    
    """Sets register C to 1 if register A is equal to register B. 
    Otherwise, register C is set to 0.
    
    """

    reg[c] = int(reg[a] == reg[b])


OPCODES = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


def parse_input(lines):
    lines = iter(lines)

    __, instruction_pointer = next(lines).split()
    instructions = []

    for line in lines:
        opcode, *args = line.split() 
        a, b, c = map(int, args)
        inst = Instruction(OPCODES[opcode], a, b, c)
        instructions.append(inst)

    return int(instruction_pointer), instructions


def regfmt(register):
    regstr = ', '.join(['{:>16d}'.format(r) for r in register])
    return f'[{regstr}]'
    

def dump(register, instruction):
    before = regfmt(register)
    ptr = register[1]
    op, a, b, c = instruction
    op(register, a, b, c)
    after = regfmt(register)

    print(f'{before} ({ptr} {op.__name__} {a:>8d} {b:>8d} {c:>8d}) {after}')


def run_program(instruction_pointer, instructions):
    """Run the instructions until the process terminates.

    Args:
        instruction_pointer (int): Register index of the instruction pointer.
        instructions (list of Instruction): Program instructions

    Returns:
        int: Number of instructions executed

    """

    answer = 1e9 

    register = [0] * 6

    idx = instruction_pointer
    ptr = register[idx]

    n = len(instructions)

    while True:
        register[idx] = ptr 

        if ptr >= n or ptr < 0:
            break  

        op, a, b, c = instructions[ptr]
        
        if ptr == 24:  # Short circuit the inner loop
            register[4] = register[2] - (register[2] % 256)
            register[4] = int(register[4] / 256)
        else:
            op(register, a, b, c)

        if instructions[ptr].op.__name__ == 'eqrr':
            if register[5] < 0:
                break 

            yield register[5]
         
        ptr = register[idx]
        ptr += 1


def answer_part_01():
    """What is the lowest non-negative integer value for register 0 that causes 
    the program to halt after executing the fewest instructions?
    
    """

    puzzle_input = aoc.util.get_puzzle_input(21)
    instruction_pointer, instructions = parse_input(puzzle_input)

    answer = next(run_program(instruction_pointer, instructions))
    print(f'Part one: {answer}')


def answer_part_02():
    """What is the lowest non-negative integer value for register 0 that causes 
    the program to halt after executing the most instructions?

    """

    puzzle_input = aoc.util.get_puzzle_input(21)
    instruction_pointer, instructions = parse_input(puzzle_input)

    p = 1e9

    seen = collections.Counter()

    for v in run_program(instruction_pointer, instructions):
        seen[v] += 1

        if seen[v] == 2:
            print(f'Part two: {p:>8d}')
            break
        
        p = v


def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()