import aoc.day_16 


def test_example_01():
    before = [3, 2, 1, 1]
    args = [9, 2, 1, 2]
    after = [3, 2, 2, 1]

    ops = aoc.day_16.possible_opcodes(before, args, after)

    assert 'mulr' in ops 
    assert 'addi' in ops 
    assert 'seti' in ops 
    assert len(ops) == 3 
