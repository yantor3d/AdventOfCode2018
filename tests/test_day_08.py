import pytest

import aoc.day_08 


TEST_INPUT = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

TEST_NUMBER_OF_CHILDREN = ((0, 2), (1, 0), (2, 1), (3, 0))
TEST_NUMBER_OF_METADATA = ((0, 3), (1, 3), (2, 1), (3, 1))


@pytest.mark.parametrize('node_id,number_of_children', TEST_NUMBER_OF_CHILDREN)
def test_nodes_have_correct_number_of_children(node_id, number_of_children):
    root = aoc.day_08.get_node(iter(TEST_INPUT.split()))

    node = aoc.day_08.find_node(root, node_id)
    assert len(node.children) == number_of_children


@pytest.mark.parametrize('node_id,number_of_metadata', TEST_NUMBER_OF_METADATA)
def test_nodes_have_correct_number_of_metadata(node_id, number_of_metadata):
    root = aoc.day_08.get_node(iter(TEST_INPUT.split()))
    
    node = aoc.day_08.find_node(root, node_id)
    assert len(node.metadata) == number_of_metadata


def test_node_metadata_checksum():
    root = aoc.day_08.get_node(iter(TEST_INPUT.split()))

    checksum = aoc.day_08.get_tree_checksum(root)

    assert checksum == 138
