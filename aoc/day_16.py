"""Advent of Code 2018 day 16 - https://adventofcode.com/2018/day/16"""

import aoc.util 


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


OPCODES = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]


def parse_input_01(lines):
    """Parse the opcode samples from the puzzle input.

    Each sample is three lines followed by a blank line.
        Before: [#, #, #, #]
        # # # #
        After:  [#, #, #, #]

    """

    lines = iter(lines)

    while True:
        try:
            before = next(lines).strip().split(':')[-1].strip()[1: -1].split(', ')
            args = next(lines).strip().split()
            after = next(lines).strip().split(':')[-1].strip()[1: -1].split(', ')
        except StopIteration:
            break 

        before = list(map(int, before))
        args = list(map(int, args))
        after = list(map(int, after))

        yield before, args, after 

        try:
            next(lines)
        except StopIteration:
            break


def parse_input_02(lines):
    """Parse the program instructions from the puzzle input.

    Each line is four numbers.
    
    """
    
    for line in lines:
        yield list(map(int, line.split()))


def possible_opcodes(before, args, after):
    """Return the names of the opcodes that could affect the registry as given."""

    result = []

    __, a, b, c = args

    for op in OPCODES:
        reg = before[:]

        op(reg, a, b, c)

        if reg == after:
            result.append(op.__name__)

    return set(result)


def answer_part_01():
    """How many samples in your puzzle input behave like three or more opcodes?"""

    puzzle_input = aoc.util.get_puzzle_input(16, suffix='part_01')

    samples = list(parse_input_01(puzzle_input))

    answer = 0
    
    for before, args, after in samples:
        opcodes = possible_opcodes(before, args, after)

        if len(opcodes) >= 3:
            answer += 1

    print(f'Part one: {answer}')


def answer_part_02():
    """What value is contained in register 0 after executing the test program?"""
    
    puzzle_input_01 = aoc.util.get_puzzle_input(16, suffix='part_01')
    puzzle_input_02 = aoc.util.get_puzzle_input(16, suffix='part_02')

    samples = list(parse_input_01(puzzle_input_01))
    program = list(parse_input_02(puzzle_input_02))
    
    opcode_names = {op.__name__: op for op in OPCODES}
    opcode_ids = {}
    opcodes_seen = set()

    for before, args, after in samples:
        opcodes = possible_opcodes(before, args, after)

        opcodes -= opcodes_seen

        if len(opcodes) == 1:
            opcode = next(iter(opcodes))
            opcodes_seen.add(opcode)
            opcode_ids[args[0]] = opcode_names[opcode]

    reg = [0, 0, 0, 0]

    for (opcode, a, b, c) in program:
        op = opcode_ids[opcode]

        op(reg, a, b, c)

    answer = reg[0]
    print(f'Part two: {answer}')


def main():
    # answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()
