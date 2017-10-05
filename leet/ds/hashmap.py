_NOTSET = object()


class _Node(object):
    def __init__(self, value, next_=None):
        self.val = value
        self.next = next_


class _LinkedList(object):
    def __init__(self):
        self._head = _Node('head')

    def prepend(self, value):
        self._head.next = _Node(value, self._head.next)

    def remove(self, value):
        prev = self._head
        while prev:
            node = prev.next
            if node.val == value:
                prev.next, node.next = node.next, None
                return
        raise ValueError

    def __iter__(self):
        node = self._head
        while node.next:
            node = node.next
            yield node.val

    def __repr__(self):
        return 'LinkedList(%s)'.format(id(self))


class HashMap(object):
    GROW_THRESHHOLD = 2 / 3.0

    def __init__(self, data=()):
        self._init(8, data)

    def _init(self, size, data):
        self._size = size
        self._buckets = [_NOTSET for _ in xrange(size)]
        self._entries = 0
        for k, v in data:
            self.set(k, v)

    @property
    def load_factor(self):
        return self._entries / float(self._size)

    def _get_index(self, k):
        return hash(k) % self._size

    def _grow(self):
        buckets = self._buckets
        self._init(self._size * 4, ())
        for values in buckets:
            if values is not _NOTSET:
                for k, v in values:
                    self.set(k, v)

    def set(self, key, value):
        index = self._get_index(key)
        values = self._buckets[index]
        if values is _NOTSET:
            self._buckets[index] = values = _LinkedList()
        else:
            for k, v in values:
                # key value pair exists
                if k == key and v == value:
                    return
        values.prepend((key, value))
        self._entries += 1
        if self.load_factor > self.GROW_THRESHHOLD:
            self._grow()

    def get(self, key, default=_NOTSET):
        values = self._buckets[self._get_index(key)]
        if values is not _NOTSET:
            for k, v in values:
                if k == key:
                    return v
        if default is not _NOTSET:
            return default
        raise KeyError

    def pop(self, key, default=_NOTSET):
        values = self._buckets[self._get_index(key)]
        if values is not _NOTSET:
            for k, v in values:
                if k == key:
                    values.remove((k, v))
                    return v
        if default is not _NOTSET:
            return default
        raise KeyError
