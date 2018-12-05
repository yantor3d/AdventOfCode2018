import pytest 

import aoc.day_05


TEST_01_REACTIONS = [
    ('dabAcCaCBAcCcaDA', 'cC', 'dabAaCBAcCcaDA'),
    ('dabAaCBAcCcaDA', 'Aa', 'dabCBAcCcaDA'),
    ('dabCBAcCcaDA', 'cC', 'dabCBAcaDA'),
    ('dabCBAcCcaDA', 'Cc', 'dabCBAcaDA')
]


TEST_02_REMOVE_ = [
    ('aA', 'dbcCCBcCcD'),
    ('bB', 'daAcCaCAcCcaDA'),
    ('cC', 'dabAaBAaDA'),
    ('dD', 'abAcCaCBAcCcaA'),
]


TEST_02_SOLVES = [
    ('dbcCCBcCcD', 'dbCBcD'),
    ('daCAcaDA', 'daCAcaDA'),
    ('dabAaBAaDA', 'daDA'),
    ('abAcCaCBAcCcaA', 'abCBAc'),
]


@pytest.mark.parametrize('input_,arg,expected', TEST_01_REACTIONS)
def test_01_polymer_reactions(input_, arg, expected):
    assert aoc.day_05.react_with(arg, input_) == expected


def test_01_solve_polymer():
    assert aoc.day_05.solve('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'


@pytest.mark.parametrize('input_,expected', TEST_02_REMOVE_)
def test_02_remove_units(input_, expected):   
    assert aoc.day_05.remove(input_, 'dabAcCaCBAcCcaDA') == expected


@pytest.mark.parametrize('input_,expected', TEST_02_SOLVES)
def test_02_solve_polmer(input_, expected):   
    assert aoc.day_05.solve(input_) == expected
