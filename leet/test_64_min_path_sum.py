#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        m * n grid;

        total(i, j) = min(
            total(i - 1, j) + g[i][j],
            total(i, j - 1) + g[i][j],
        )
        total(0, j) = total(0, j - 1) + g[0][j]
        total(i, 0) = total(i - 1, 0) + g[i][0]
        total(0, 0) = g[0][0]
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if m == n == 1:
            return grid[0][0]

        total = [[0 for _ in xrange(n)] for _ in xrange(m)]
        total[0][0] = grid[0][0]
        for i in xrange(m):
            for j in xrange(n):
                if i == j == 0:
                    continue
                if i == 0:
                    total[i][j] = total[i][j - 1] + grid[i][j]
                elif j == 0:
                    total[i][j] = total[i - 1][j] + grid[i][j]
                else:
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
            [1, 1, 1],
        ], 3
    ),

))
def test_64_min_path_sum(grid, result):
    s = Solution()
    assert s.minPathSum(grid) == result
