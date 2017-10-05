_NOTSET = object()
_DUMMY = object()


class HashMap(object):
    GROW_THRESHHOLD = 2 / 3.0

    def __init__(self, data=()):
        self._init(8, data)

    def _init(self, size, data):
        self._size = size
        self._buckets = [None] * size
        self._entries = 0
        for k, v in data:
            self.set(k, v)

    @property
    def load_factor(self):
        return self._entries / float(self._size)

    def _grow(self):
        buckets = self._buckets
        self._init(self._size * 4, (item for item in buckets if item))

    def _get_item(self, key):
        index = hash(key) % self._size
        while True:
            item = self._buckets[index]
            if item:
                if item[0] == key:
                    return index, item
                else:  # collision; probe
                    index += 1
            else:
                return index, None

    def set(self, key, value):
        index, item = self._get_item(key)
        if item != (key, value):
            self._buckets[index] = (key, value)
            self._entries += 1
        if self.load_factor > self.GROW_THRESHHOLD:
            self._grow()

    def get(self, key, default=_NOTSET):
        index, item = self._get_item(key)
        if item:
            return item[1]
        if default is not _NOTSET:
            return default
        raise KeyError

    def pop(self, key, default=_NOTSET):
        index, item = self._get_item(key)
        if item:
            self._buckets[index] = None
            return item[1]
        if default is not _NOTSET:
            return default
        raise KeyError
