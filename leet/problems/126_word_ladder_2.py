#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given two words (beginWord and endWord), and a dictionary's word list, find
all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

Acceptance: 13.7%
"""
import pytest
from collections import defaultdict
import itertools
from heapq import heappush, heappop


class PriorityQueue:
    REMOVED = '_removed'

    def __init__(self):
        self._h = []
        self._entry_map = {}
        self._counter = itertools.count()

    def __nonzero__(self):  # pragma: no cover
        return bool(self._entry_map)

    def is_empty(self):
        return not self._entry_map

    def __contains__(self, item):
        return item in self._entry_map

    def add_or_update(self, item, priority):
        if item in self._entry_map:
            self.remove(item)
        entry = [priority, next(self._counter), item]
        self._entry_map[item] = entry
        heappush(self._h, entry)

    def remove(self, item):
        entry = self._entry_map.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        while self._h:
            _, _, item = heappop(self._h)
            if item is not self.REMOVED:
                del self._entry_map[item]
                return item

    def __str__(self):
        return str(self._h)


class Graph:

    def __init__(self):
        self._edges = defaultdict(set)

    def __contains__(self, v):  # pragma: no cover
        return v in self._edges

    def add_edge(self, v1, v2):
        self._edges[v1].add(v2)
        self._edges[v2].add(v1)

    def neighbors(self, v):
        return self._edges[v]

    def __str__(self):
        return str(self._edges)


class Solution(object):

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        words = list(set(list(wordlist) + [beginWord, endWord]))
        max_dist = len(words)

        nodes_q = PriorityQueue()
        for word in words:
            if word == beginWord:
                dist = 0
            else:
                dist = max_dist
            nodes_q.add_or_update(word, dist)

        # build graph
        graph = Graph()
        for i, wi in enumerate(words):
            for wj in words[i + 1:]:
                if sum(1 for li, lj in zip(wi, wj) if li != lj) == 1:
                    graph.add_edge(wi, wj)
        # shortest distnace from source for each node
        distances = defaultdict(lambda: max_dist)
        distances[beginWord] = 0

        while not nodes_q.is_empty():
            current = nodes_q.pop()
            # print('visit node: {}'.format(current))
            if current == endWord:
                break
            for neighbor in graph.neighbors(current):
                if neighbor in nodes_q:
                    alt = distances[current] + 1
                    dist = distances[neighbor]
                    if alt < dist:
                        distances[neighbor] = alt
                        nodes_q.add_or_update(neighbor, alt)

        def visit(g, node, dest, path):
            new_path = path + [node]
            if node == dest:
                return [new_path]
            current_len = distances[node]
            ret = []
            for neighbor in g.neighbors(node):
                if distances[neighbor] == current_len + 1:
                    ret += visit(g, neighbor, dest, new_path)
            return ret

        # find shortest paths
        return sorted(visit(graph, beginWord, endWord, []))


TESTCASES = [
    [
        'hit', 'cog', {"hot", "dot", "dog", "lot", "log"}, [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],
        ]
    ],
    [
        'a', 'd', {'b', 'c'}, [
            ['a', 'd'],
        ]
    ],
    [
        'hot', 'dog', {
            "hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"}, [
                ['hot', 'dot', 'dog'],
                ['hot', 'hog', 'dog'],
        ]
    ]
]


@pytest.mark.parametrize('begin,end,words,expected', TESTCASES)
def test(begin, end, words, expected):
    result = Solution().findLadders(begin, end, words)
    assert result == expected
