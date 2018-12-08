import collections
import itertools
import re 
import queue

import aoc.util 

instructions_regex = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

Instruction = collections.namedtuple('Instruction', 'prev this')


def parse_input(line):
    [[prev, this]] = instructions_regex.findall(line)

    return Instruction(prev, this)


def get_nodes(steps):
    return set(itertools.chain.from_iterable(steps))


def get_graph(steps):
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
    for node in graph:
        up, dn = graph[node] 

        if not up:
            yield node


def get_build_order(steps):
    """Return the order in which the steps have to be complete.
    
    Args:
        steps (iterable of Instruction)

    Returns:
        str
        
    """

    graph = get_graph(steps)

    evaluation_graph = queue.Queue()

    roots = list(get_roots(graph))
    evaluation_graph.put(roots)

    result = []

    while True:
        if evaluation_graph.empty():
            break 

        nodes = evaluation_graph.get()
        next_nodes = set(nodes)

        for node in sorted(nodes):

            if node in result:
                continue 

            upstream, downstream = graph[node]
            upstream_nodes_are_evaluated = all([n in result for n in upstream])

            if not upstream_nodes_are_evaluated:
                continue 
                
            result.append(node)

            next_nodes.remove(node)            
            next_nodes.update(set(downstream))
            break

        if next_nodes:
            next_nodes = sorted(next_nodes, reverse=True)            
            evaluation_graph.put(next_nodes)

    return ''.join(result)


def answer_part_01():
    input_ = aoc.util.get_puzzle_input(7)
    steps = list(map(parse_input, input_))
    
    answer = get_build_order(steps)
    print(f'Part One: {answer}')


def main():
   answer_part_01() 


if __name__ == "__main__":
    main()