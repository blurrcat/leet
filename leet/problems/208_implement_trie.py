"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

    >>> t = Trie()
    >>> t.insert('hi')
    >>> t.search('hi')
    True
    >>> t.search('ho')
    False
    >>> t.search('h')
    False
    >>> t.insert('h')
    >>> t.search('h')
    True
    >>> t.startsWith('h')
    True
    >>> t.startsWith('o')
    False
    >>> t.search('')
    False

"""


class Node(object):
    def __init__(self, v=None, ends=False):
        self.val = v
        self.ends = ends  # wether this is the end of a word
        self.children = []

    def get_child_by_val(self, val):
        for c in self.children:
            if c.val == val:
                return c

    def insert_branch(self, vals):
        node = self
        for val in vals:
            child = Node(val)
            node.children.append(child)
            node = child
        node.ends = True

    def __repr__(self):
        return 'Node[{}]'.format(self.val)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = Node()

    def _match_prefix(self, vals):
        node = self._root
        rest = ''
        for i, val in enumerate(vals):
            child = node.get_child_by_val(val)
            if child:
                node = child
            else:
                rest = vals[i:]
                break
        return node, rest

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node, rest = self._match_prefix(word)
        if rest:
            node.insert_branch(rest)
        else:
            node.ends = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node, rest = self._match_prefix(word)
        return not rest and node.ends

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        :type prefix: str
        :rtype: bool
        """
        _, rest = self._match_prefix(prefix)
        return not rest
