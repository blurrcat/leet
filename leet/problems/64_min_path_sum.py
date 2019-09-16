#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
64. Minimum Path Sum My Submissions Question
Total Accepted: 64258 Total Submissions: 187652 Difficulty: Medium

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
import pytest


class Solution(object):
    # @profile
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        m * n grid;

        total(i, j) = min(
            total(i - 1, j) + g[i][j],
            total(i, j - 1) + g[i][j],
        )
        total(0, j) = total(0, j - 1) + g[0][j], j > 1
        total(i, 0) = total(i - 1, 0) + g[i][0], i > 1
        total(0, 0) = g[0][0]
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        total = [[0 for _ in range(n)] for _ in range(m)]
        total[0][0] = grid[0][0]

        for i in range(1, m):
            total[i][0] = total[i - 1][0] + grid[i][0]
        for j in range(1, n):
            total[0][j] = total[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                total[i][j] = min(
                    total[i - 1][j], total[i][j - 1]) + grid[i][j]
        return total[m - 1][n - 1]


@pytest.mark.parametrize('grid,result', (
    (
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
        ], 0
    ),
    (
        [
            [0, 0, 1],
            [1, 2, 1],
            [0, 0, 0],
        ], 1
    ),
    (
        [
            [0, 1, 4],
            [0, 3, 0],
            [3, 1, 1],
        ], 4
    ),
    (
        [], 0
    ),
    (
        [
            [1],
            [1],
        ], 2
    ),
    (
        [
            [1, 1],
        ], 2
    ),
    (
        [[1] * 100] * 100,
        199
    )

))
def test_64_min_path_sum(grid, result):
    s = Solution()
    assert s.minPathSum(grid) == result
