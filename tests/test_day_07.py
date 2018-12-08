import pytest

import aoc.day_07

TEST_INPUT = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

TEST_OUTPUT_NODES = {'A', 'B', 'C', 'D', 'E', 'F'}

TEST_GRAPH = {
    'A': ({'C'}, {'B', 'D'}),
    'B': ({'A'}, {'E'}),
    'C': (set(), {'A', 'F'}),
    'D': ({'A'}, {'E'}),
    'E': ({'B', 'D', 'F'}, set()),
    'F': ({'C'}, {'E'}),
}


def test_nodes():
    steps = list(map(aoc.day_07.parse_input, TEST_INPUT))

    actual = aoc.day_07.get_nodes(steps)

    assert actual == TEST_OUTPUT_NODES


@pytest.mark.parametrize('input_,expected', TEST_GRAPH.items())
def test_graph(input_, expected):
    steps = list(map(aoc.day_07.parse_input, TEST_INPUT))
    graph = aoc.day_07.get_graph(steps)

    assert graph[input_] == expected


def test_root_node():
    steps = list(map(aoc.day_07.parse_input, TEST_INPUT))

    graph = aoc.day_07.get_graph(steps)
    actual = next(aoc.day_07.get_roots(graph))

    assert actual == 'C'


def test_build_order():
    steps = list(map(aoc.day_07.parse_input, TEST_INPUT))

    answer, order = aoc.day_07.get_parallel_build_order(steps, 1, 0)

    assert order == 'CABDFE'


def test_parallel_build_order():
    steps = list(map(aoc.day_07.parse_input, TEST_INPUT))

    answer, order = aoc.day_07.get_parallel_build_order(steps, 2, 0)

    assert answer == 15
    assert order == 'CABFDE'
