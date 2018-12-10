"""Advent of Code 2018 day 08 - https://adventofcode.com/2018/day/8"""

import collections

import aoc.util 

Node = collections.namedtuple('Node', 'id children metadata')


def find_node(root, node_id):
    """Find the node in the graph with the given ID."""
    
    return {
        node.id: node 
        for node in iter_tree(root)
    }.get(node_id)


def get_metadata(stream, n):
    """Return the next N metadata values from the stream of data."""

    return [int(next(stream)) for _ in range(n)]
        

def get_children(stream, n, node_id):
    """Return the next N child nodes constructed from the stream of data."""

    return [get_node(stream, node_id + i + 1) for i in range(n)]


def get_node(stream, node_id=0):
    """Return the node tree constructed from the stream of data."""    

    number_of_children = int(next(stream))
    number_of_metadata = int(next(stream))

    return Node(
        node_id,
        get_children(stream, number_of_children, node_id), 
        get_metadata(stream, number_of_metadata)
    )    


def iter_tree(root):
    """Yield each node in the tree, depth first."""

    yield root 

    for child in root.children:
        yield from iter_tree(child) 


def get_node_checksum(node):
    """Return the checksum for the node.

    The checksum is the sum of the metadata values.

    """

    return sum(node.metadata)


def get_tree_checksum(root):
    """Return the checksum for the tree.

    The checksum is the sum of the metadata values.

    """

    return sum(map(get_node_checksum, iter_tree(root)))


def get_node_value(node):
    """Return the value of a node.

    If a node has no children, it's value is the sum of its metadata entries.

    If a node has children, it's value is the sum of the values of the nodes
    at the indices referenced by the metadata entries.

    """

    if node is None:
        return 0 

    if node.children:
        children = dict(enumerate(node.children, 1))
        children = list(map(children.get, node.metadata))
        return sum(map(get_node_value, children))
    else:
        return get_node_checksum(node)


def answer_part_01():
    """What is the sum of all metadata entries?"""

    input_, = aoc.util.get_puzzle_input(8)  

    root = get_node(iter(input_.split()))
    answer = get_tree_checksum(root)

    print(f"Part one: {answer}")


def answer_part_02():
    """What is the value of the root node?"""

    input_, = aoc.util.get_puzzle_input(8)  

    root = get_node(iter(input_.split()))
    answer = get_node_value(root)

    print(f"Part two: {answer}")


def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()
