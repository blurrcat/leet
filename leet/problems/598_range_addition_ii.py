#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given an m * n matrix M initialized with all 0's and several update
operations.

Operations are represented by a 2D array, and each operation is represented
by an array with two positive integers a and b, which means M[i][j] should be
added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix
after performing all the operations.

    >>> s = Solution()
    >>> s.maxCount(4, 4, [[1, 1]])
    1
    >>> s.maxCount(4, 4, [[5, 5]])
    16
    >>> s.maxCount(4, 4, [[3, 3], [2, 4], [4, 2]])
    4
    >>> s.maxCount(3, 3, [[2, 2], [3, 3]])
    4

"""


def merge(a, b):
    return (a[0] if a[0] < b[0] else b[0]), (a[1] if a[1] < b[1] else b[1])


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        ops.append((m, n))
        merged = reduce(merge, ops)
        return merged[0] * merged[1]
