"""Advent of Code 2018 day 07 - https://adventofcode.com/2018/day/7"""

import collections
import itertools
import re 
import string

import aoc.util 

instructions_regex = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

Instruction = collections.namedtuple('Instruction', 'prev this')
Task = collections.namedtuple('Task', 'node elapsed_time run_time')


def parse_input(line):
    [[prev, this]] = instructions_regex.findall(line)

    return Instruction(prev, this)


def get_nodes(steps):
    """Return the nodes in the graph.
    
    Args:
        steps (iterable of Instruction)

    Returns:
        set
    """

    return set(itertools.chain.from_iterable(steps))


def get_graph(steps):
    """Return a map of the node graph.
    
    Returns:
        dict: str -> set, set
            The node and its upstream and downstream dependencies.

    """

    nodes = get_nodes(steps)

    dependencies = {
        node: (
            {step.prev for step in steps if step.this == node},
            {step.this for step in steps if step.prev == node}
        )
        for node in nodes
    }

    return dependencies


def get_roots(graph):
    """Yield each node in the graph with no upstream dependencies."""

    for node in graph:
        up, dn = graph[node] 

        if not up:
            yield node


def get_parallel_build_order(steps, number_of_worker, minimum_time):  # noqa C901
    """Return the order of the steps when executed in parallel.

    Args:
        steps (iterable of Instruction)
        number_of_works (int)
        minimum_time (int)

    Returns:
        int, str 
            - Time to complete all tasks
            - Order in which tasks were completed
    """

    graph = get_graph(steps)

    evaluated = collections.defaultdict(bool)

    schedule_pool = list(set(get_roots(graph)))
    
    def get_evaluation_time(x):
        return minimum_time + string.ascii_uppercase.index(x) + 1 

    workers = {i: None for i in range(number_of_worker)}
    
    elapsed_time = 0

    result = [] 

    while True:        
        schedule_pool.sort(reverse=True)
        elapsed_time += 1

        # Schedule task for idle workers
        for worker, task in workers.items():
            if task is not None:
                continue

            if not schedule_pool:
                continue 

            node = schedule_pool.pop(-1)

            if not evaluated[node]:
                workers[worker] = Task(node, 0, get_evaluation_time(node)) 
                evaluated[node] = True

        finished_tasks = []

        # Do work on active tasks
        for worker, task in workers.items():
            if task is None:
                continue 
            
            task = task._replace(elapsed_time=task.elapsed_time + 1)

            if task.elapsed_time >= task.run_time:
                finished_tasks.append(task)
                task = None 
            
            workers[worker] = task

        for task in finished_tasks:           
            result.append(task.node)

            # Schedule dependent tasks
            _, downstream = graph[task.node]

            for node in downstream:
                upstream, _ = graph[node]

                upstream_nodes_are_evaluated = all([n in result for n in upstream])

                if upstream_nodes_are_evaluated:
                    schedule_pool.append(node)

        if not schedule_pool:
            for worker, task in workers.items():
                if task is not None:
                    break
            else:
                break

    return elapsed_time, ''.join(result)


def answer_part_01():
    input_ = aoc.util.get_puzzle_input(7)
    steps = list(map(parse_input, input_))
    
    elapsed_time, answer = get_parallel_build_order(steps, 1, 60)
    print(f'Part One: {elapsed_time:<4d} {answer}')


def answer_part_02():
    input_ = aoc.util.get_puzzle_input(7)
    steps = list(map(parse_input, input_))
    
    elapsed_time, answer = get_parallel_build_order(steps, 5, 60)
    print(f'Part Two: {elapsed_time:<4d} {answer}')


def main():
    answer_part_01() 
    answer_part_02() 


if __name__ == "__main__":
    main()
