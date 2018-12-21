"""Advent of Code 2018 day 19 - https://adventofcode.com/2018/day/19"""

import collections
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


def run_program(instruction_pointer, instructions, register=None, fast=False):
    """Run the instructions until the process terminates.

    Args:
        instruction_pointer (int): Register index of the instruction pointer.
        instructions (list of Instruction): Program instructions
        register (list of int): Optional intitial state of the registers
        fast (bool): If True, unroll the no good, very bad, horrible, terrible inner loop.
        
    Returns:
        list of int: Register values

    """

    register = register or [0] * 6

    idx = instruction_pointer
    ptr = register[idx]

    n = len(instructions)

    x = 0

    inner_loop = False

    while True:
        x += 1
        register[idx] = ptr
        
        if ptr >= n or ptr < 0:
            break 

        op, a, b, c = instructions[ptr]
        op(register, a, b, c)

        if inner_loop and fast:
            break

        inner_loop = ptr == 3

        ptr = register[idx]
        ptr += 1
   
    if fast:
        # Optimized inner loop
        R2 = register[2]
        for R4 in range(1, R2 + 1):
            register[0] += (R4 * (R2 % R4 == 0))

    return register 


def answer_part_01():
    """What value is left in register 0 when the background process halts?"""

    puzzle_input = aoc.util.get_puzzle_input(19)

    ip, inst = parse_input(puzzle_input)
    start_time = time.time()
    register = run_program(ip, inst)
    elapsed_time = time.time() - start_time
    answer = register[0]

    print(f'Part one: {answer} (took {elapsed_time:.2f} seconds)')


def answer_part_02():
    """What value is left in register 0 when the background process halts?"""

    puzzle_input = aoc.util.get_puzzle_input(19)

    ip, inst = parse_input(puzzle_input)
    start_time = time.time()
    register = [1, 0, 0, 0, 0, 0]
    register = run_program(ip, inst, register, fast=True)
    elapsed_time = time.time() - start_time

    answer = register[0]

    print(f'Part two: {answer} (took {elapsed_time:.2f} seconds)')


def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()
