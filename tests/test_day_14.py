import pytest 

import aoc.day_14


EXAMPLES_01 = [
    (9, '5158916779'),
    (5, '0124515891'),
    (18, '9251071085'),
    (2018, '5941429882'),
]

EXAMPLES_02 = [
    ('51589', 9),
    ('01245', 5),
    ('92510', 18),
    ('59414', 2018)
]


@pytest.mark.parametrize('number_of_recipes,expected_score', EXAMPLES_01)
def test_example_01(number_of_recipes, expected_score):
    actual_score = aoc.day_14.answer_part_01(number_of_recipes)

    assert actual_score == expected_score
    

@pytest.mark.parametrize('input_,expected', EXAMPLES_02)
def test_example_02(input_, expected):
    actual = aoc.day_14.answer_part_02(input_)

    assert actual == expected
