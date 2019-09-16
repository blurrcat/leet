#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

    >>> s = Solution()
    >>> s.maximalSquare([['1', '1'], ['1', '1']])
    4
    >>> s.maximalSquare([])
    0
    >>> s.maximalSquare([[]])
    0
    >>> s.maximalSquare([['1']])
    1
    >>> s.maximalSquare([['0', '0']])
    0
    >>> s.maximalSquare([['1', '0']])
    1
    >>> s.maximalSquare([['1', '1']])
    1
    >>> s.maximalSquare([['0', '1'], ['1', '1']])
    1
    >>> matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]  # noqa
    >>> s.maximalSquare(matrix)
    4

"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_size = 0
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j] = min(
                            dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1],
                        ) + 1
                    else:  # on the edge of the matrix
                        dp[i][j] = 1
                    if dp[i][j] > max_size:
                        max_size = dp[i][j]
        return max_size * max_size
