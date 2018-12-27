import aoc.day_22


def test_example_01():
    depth = 510
    target = (10, 10)

    risk = aoc.day_22.calculate_risk(depth, target)

    assert risk == 114