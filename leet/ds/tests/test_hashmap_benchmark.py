import random
from leet.ds.hashmap import HashMap
ROUNDS = 128
SIZE = 512
N = 100


def test_bench_set(benchmark):
    keys = list(range(SIZE))
    values = list(keys)
    kvs = list(zip(keys, values))
    m = HashMap()

    def setup():
        global m
        m = HashMap(kvs)

    def bench_set():
        for k, v in kvs[:N]:
            m.set(k, v)

    benchmark.pedantic(bench_set, setup=setup, rounds=ROUNDS)


def test_bench_get(benchmark):
    keys = list(range(SIZE))
    values = list(keys)
    random.shuffle(values)
    m = HashMap(zip(keys, values))

    def bench_get():
        for k in keys[:N]:
            m.get(k, None)

    benchmark.pedantic(bench_get, rounds=ROUNDS)


def test_bench_pop(benchmark):
    keys = list(range(SIZE))
    values = list(keys)
    m = HashMap()

    def setup():
        global m
        m = HashMap(zip(keys, values))

    def bench_pop():
        for k in keys[:N]:
            m.pop(k, None)

    benchmark.pedantic(bench_pop, setup=setup, rounds=ROUNDS)
