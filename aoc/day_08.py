import collections

import aoc.util 

Node = collections.namedtuple('Node', 'node_id children metadata')


def find_node(root, node_id):
    return {
        node.node_id: node 
        for node in iter_tree(root)
    }.get(node_id)


def get_metadata(stream, n):
    return [int(next(stream)) for _ in range(n)]
        

def get_children(stream, n, node_id):
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


def print_tree(node, indent=0):
    if indent == 0:
        print('')

    print('-' * indent, node.node_id, node.metadata)

    for child in node.children:
        print_tree(child, indent + 1)


def answer_part_01():
    """What is the sum of all metadata entries?"""

    input_, = aoc.util.get_puzzle_input(8)  

    root = get_node(iter(input_.split()))
    answer = get_tree_checksum(root)

    print(f"Part one: {answer}")


def main():
    answer_part_01()


if __name__ == "__main__":
    main()
