import collections

import aoc.util

Point = collections.namedtuple('Point', 'x y')

OPEN_GROUND = '.'
TREES = '|'
LUMBERYARD = '#' 


def parse_input(lines):
    result = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            result[Point(x, y)] = char 

    return result 


def adjacent_tiles(point):
    """Get the tiles adjacent to this point.

    Args:
        point (Point)

    Returns:
        list of Point 

    """

    p = point 

    return {
        Point(p.x - 1, p.y + 1),
        Point(p.x - 0, p.y + 1),
        Point(p.x + 1, p.y + 1),
        Point(p.x - 1, p.y + 0),
        Point(p.x + 1, p.y + 0),
        Point(p.x - 1, p.y - 1),
        Point(p.x - 0, p.y - 1),
        Point(p.x + 1, p.y - 1),
    }


def tick(woods):
    """Get the next state of the woods.

    Args:
        woods (dict)

    Returns:
        dict 

    """

    tiles = set(woods.keys())

    new_woods = dict(woods)

    for tile, state in woods.items():
        count = collections.Counter([woods[adj] for adj in adjacent_tiles(tile) & tiles])

        if state == OPEN_GROUND:
            new_state = TREES if count[TREES] >= 3 else OPEN_GROUND
        elif state == TREES:
            new_state = LUMBERYARD if count[LUMBERYARD] >= 3 else TREES
        elif state == LUMBERYARD:
            new_state = (
                LUMBERYARD 
                if (count[LUMBERYARD] >= 1 and count[TREES] >= 1) 
                else OPEN_GROUND
            )
        else:
            new_state = state 

        new_woods[tile] = new_state

    return new_woods


def score_it(woods):
    """Return the score of the wooded area.

    Args:
        woods (dict)

    Returns:
        int 
    """

    count = collections.Counter(woods.values())
    num_trees = count[TREES]
    num_yards = count[LUMBERYARD]

    return num_trees * num_yards


def solve(woods, iterations):
    for _ in range(iterations):
        woods = tick(woods)

    return score_it(woods)


def iter_solve(woods, iterations):
    score_iteration = {}
    scores = []

    pattern_count = collections.Counter()
    pattern_period = {}

    for i in range(iterations):
        woods = tick(woods)

        count = collections.Counter(woods.values())
        num_trees = count[TREES]
        num_yards = count[LUMBERYARD]

        score = num_trees * num_yards

        scores.append(score) 

        if score in score_iteration:            
            start = score_iteration[score]
            end = i

            score_pattern = scores[start:end + 1]
            
            for i_, score_ in enumerate(score_pattern):
                if score_ != scores[start + i_]:
                    break 
            else:
                score_pattern = tuple(score_pattern)

                pattern_count[score_pattern] += 1
                pattern_period[score_pattern] = (start, end)

                if pattern_count[score_pattern] > 5:
                    break

        score_iteration[score] = i

    repeated_pattern = sorted(pattern_count, key=pattern_count.__getitem__)[-1]
    
    start, end = pattern_period[repeated_pattern]
    period = end - start 

    n = start 

    while n <= iterations: 
        n += period

    n = iterations - (n - period) - 1

    return repeated_pattern[n]


def answer_part_01():
    """What will the total resource value of the lumber collection area be after 10 minutes?"""

    puzzle_input = aoc.util.get_puzzle_input(18)

    in_woods = parse_input(puzzle_input)
    answer = solve(in_woods, 10)
    
    print(f"Part one: {answer}")


def answer_part_02():
    """What will the total resource value of the lumber collection area be 
    after 1000000000 minutes?
    
    """

    puzzle_input = aoc.util.get_puzzle_input(18)

    in_woods = parse_input(puzzle_input)
    answer = iter_solve(in_woods, 1000000000)

    print(f"Part two: {answer}")
    
    
def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()
