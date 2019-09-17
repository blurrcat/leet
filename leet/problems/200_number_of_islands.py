#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

Accepted
423,431
Submissions
988,271
"""
import pytest
from typing import List

ISLAND = '1'
WATER = '0'


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)

        if not grid[0]:
            return 0
        cols = len(grid[0])

        islands = 0

        for rowIndex, row in enumerate(grid):
            for colIndex, node in enumerate(row):
                if node == ISLAND:
                    islands += 1

                    connected = [(rowIndex, colIndex)]
                    while connected:
                        r, c = connected.pop()
                        grid[r][c] = WATER
                        if r - 1 > 0 and grid[r - 1][c] == ISLAND:
                            connected.append((r - 1, c))
                        if c - 1 > 0 and grid[r][c - 1] == ISLAND:
                            connected.append((r, c - 1))
                        if r + 1 < rows and grid[r + 1][c] == ISLAND:
                            connected.append((r + 1, c))
                        if c + 1 < cols and grid[r][c + 1] == ISLAND:
                            connected.append((r, c + 1))

        return islands


@pytest.mark.parametrize(
    'data,expected', [
        ['11110\n11010\n11000\n00000', 1],
        ['11000\n11000\n00100\n00011', 3],
    ]
)
def test_number_of_islands(data, expected):
    grid = [list(line) for line in data.split('\n')]
    assert Solution().numIslands(grid) == expected
