import random
from leet.ds.binary_tree import BinarySearchTree


def test_bench_add(benchmark):
    size = 512
    items = range(size)

    def setup():
        random.shuffle(items)

    def bench_add():
        BinarySearchTree(items)

    benchmark.pedantic(bench_add, setup=setup, rounds=size)


def test_bench_contains(benchmark):
    size = 512
    items = range(size)

    def setup():
        random.shuffle(items)
        tree = BinarySearchTree(items)
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
        tree = BinarySearchTree(items)
        return (tree,), {}

    def bench_remove(tree):
        for item in items:
            tree.remove(item)

    benchmark.pedantic(bench_remove, setup=setup, rounds=size)
