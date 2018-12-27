import aoc.day_23 

EXAMPLE = [
    'pos=<0,0,0>, r=4',
    'pos=<1,0,0>, r=1',
    'pos=<4,0,0>, r=3',
    'pos=<0,2,0>, r=1',
    'pos=<0,5,0>, r=3',
    'pos=<0,0,3>, r=1',
    'pos=<1,1,1>, r=1',
    'pos=<1,1,2>, r=1',
    'pos=<1,3,1>, r=1',
]

def test_example_01():
    data = aoc.day_23.parse_input(EXAMPLE)

    actual = aoc.day_23.most_nanobots_in_range(data)

    assert actual == 7