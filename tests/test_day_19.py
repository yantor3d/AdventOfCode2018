import aoc.day_19

EXAMPLE_PROGRAM = [
    '#ip 0',
    'seti 5 0 1',
    'seti 6 0 2',
    'addi 0 1 0',
    'addr 1 2 3',
    'setr 1 0 0',
    'seti 8 0 4',
    'seti 9 0 5',
]


def test_example_program_01():
    ip, inst = aoc.day_19.parse_input(EXAMPLE_PROGRAM)

    reg = aoc.day_19.run_program(ip, inst)

    assert reg[ip] == 7