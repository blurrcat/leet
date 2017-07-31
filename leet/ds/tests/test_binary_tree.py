import random
from leet.ds.binary_tree import BinaryTree

items = (2, 9, 3, 6, 5, 8, 7)


def test_init_and_add():
    t = BinaryTree(items)
    assert 6 in t
    assert 4 not in t
    # tree structure
    root = t._root
    assert root.key == 2
    assert root.right.key == 9
    assert root.right.left.key == 3
    assert root.right.left.right.key == 6
    assert root.right.left.right.left.key == 5
    assert root.right.left.right.right.key == 8
    assert root.right.left.right.right.left.key == 7

    assert tuple(t) == items


def test_remove():
    t = BinaryTree(items)

    t.remove(9)
    assert 9 not in t
    t.remove(6)
    assert 6 not in t
    t.remove(3)
    assert 3 not in t

    for item in items:
        if item not in (3, 6, 9):
            assert item in t


def test_bench_add(benchmark):
    size = 512
    items = range(size)

    def setup():
        random.shuffle(items)

    def bench_add():
        BinaryTree(items)

    benchmark.pedantic(bench_add, setup=setup, rounds=size)


def test_bench_contains(benchmark):
    size = 512
    items = range(size)

    def setup():
        random.shuffle(items)
        tree = BinaryTree(items)
        return (tree,), {}

    def bench_contains(tree):
        for item in items:
            assert item in tree

    benchmark.pedantic(bench_contains, setup=setup, rounds=size)


def test_bench_delete(benchmark):
    size = 512
    items = range(size)

    def setup():
        random.shuffle(items)
        tree = BinaryTree(items)
        return (tree,), {}

    def bench_remove(tree):
        for item in items:
            tree.remove(item)

    benchmark.pedantic(bench_remove, setup=setup, rounds=size)
