#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
73. Set Matrix Zeroes
Total Accepted: 61115 Total Submissions: 184690
Difficulty: Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
import pytest


class Solution(object):
    """
    To use constant space solution only, we need to mark locations to be set
    to zero, while preserving the original zeros in the matrix.
    """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        if not matrix[0]:
            return
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for ii in range(rows):
                        if matrix[ii][j] != 0:  # only mark if it's not 0
                            matrix[ii][j] = None  # mark as to be set
                    for jj in range(cols):
                        if matrix[i][jj] != 0:
                            matrix[i][jj] = None
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


TESTCASES = [
    (
        [],
        [],
    ),
    (
        [[]],
        [[]],
    ),
    (
        [
            [1],
        ],
        [
            [1],
        ],
    ),
    (
        [
            [0],
        ],
        [
            [0],
        ],
    ),
    (
        [
            [1, 0],
        ],
        [
            [0, 0],
        ],
    ),
    (
        [
            [1],
            [0],
        ],
        [
            [0],
            [0]
        ],
    ),
    (
        [
            [1, 1],
            [0, 1],
        ],
        [
            [0, 1],
            [0, 0]
        ],
    ),
    (
        [
            [1, 0, 1],
            [1, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 0, 1],
        ],
    ),
    (
        [
            [1, 0, 0],
            [1, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 0, 0],
        ],
    ),
]


@pytest.mark.parametrize('matrix,result', TESTCASES)
def test(matrix, result):
    s = Solution()
    s.setZeroes(matrix)
    assert matrix == result
