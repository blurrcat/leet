import pytest
from leet.ds.binary_tree import BinarySearchTree, BinaryTreeNode

items = (2, 9, 3, 6, 5, 8, 7)


def test_init_and_add():
    t = BinarySearchTree(items)
    assert 6 in t
    assert 4 not in t
    # tree structure
    root = t._root
    assert root.val == 2
    assert root.right.val == 9
    assert root.right.left.val == 3
    assert root.right.left.right.val == 6
    assert root.right.left.right.left.val == 5
    assert root.right.left.right.right.val == 8
    assert root.right.left.right.right.left.val == 7

    assert tuple(t) == items
    # duplicate items should be dropped
    l = len(t)
    t.add(2)
    assert len(t) == l
    assert root.val == 2


def test_min_max():
    t = BinarySearchTree(items)
    assert t.min == 2
    assert t.max == 9


def test_successor():
    t = BinarySearchTree(items)
    node_8 = t.find(8)
    assert node_8.successor.val == 9


def test_remove():
    t = BinarySearchTree(items)

    t.remove(9)
    assert 9 not in t
    t.remove(6)
    assert 6 not in t
    t.remove(3)
    assert 3 not in t

    for item in items:
        if item not in (3, 6, 9):
            assert item in t
            t.remove(item)
            assert item not in t


def test_bool():
    t = BinarySearchTree()
    assert not t
    t.add(1)
    assert t


def test_node_from_list():
    root = BinaryTreeNode.from_list([1])
    assert root.val == 1
    assert not root.left and not root.right

    root = BinaryTreeNode.from_list([1, 2, 3, None, None, None, 4])
    assert root.val == 1
    assert root.left.val == 2
    assert root.left.left is None and root.left.right is None
    assert root.right.val == 3
    assert root.right.left is None and root.right.right.val == 4


@pytest.mark.parametrize('nodes_list,expect_valid', [
    [[2, 1, 3], True],
    [[], True],
    [[1], True],
    [[1, 2, 3], False],
    [[10, 5, 15, None, None, 6, 20], False],
    [[3, 1, 5, 0, 2, 4, 6], True],
    [[3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False],
    [[5, None, 9, None, None, 4], False],
    [[5, 4, None, None, 6], False],
])
def test_validate_search_tree(nodes_list, expect_valid):
    root = BinaryTreeNode.from_list(nodes_list)
    tree = BinarySearchTree.from_root(root)
    if expect_valid:
        assert tree is not None
        vals = [v for v in nodes_list if v is not None]
        assert len(tree) == len(vals)
        for v in vals:
            if v:
                assert v in tree
    else:
        assert tree is None
