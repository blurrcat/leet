import pytest
from leet.ds.hashmap import HashMap


def test_init():
    m = HashMap((('a', 1), ('b', 2)))
    assert m.get('a') == 1
    assert m.get('b') == 2


def test_basic():
    m = HashMap()
    m.set('a', 10)
    assert m.get('a') == 10


def test_get_missing_key():
    m = HashMap()
    with pytest.raises(KeyError):
        m.get('a')


def test_pop():
    m = HashMap()
    m.set('a', 1)
    assert m.pop('a') == 1
    with pytest.raises(KeyError):
        m.pop('a')


def test_load_factory():
    m = HashMap()
    assert m.load_factor == 0
    m.set('a', 1)
    assert m.load_factor == 1 / float(m._size)
    m.set('a', 1)  # should be ignored
    assert m.load_factor == 1 / float(m._size)


def test_grow():
    m = HashMap()
    old_size = m._size
    for i in range(old_size + 1):
        m.set(i, i)
    assert m._size > old_size
