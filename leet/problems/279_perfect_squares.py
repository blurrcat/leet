#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/perfect-squares/description/

Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.
"""
import pytest
import math


class Solution(object):

    def numSquares(self, num):
        # results[n] means the least number of perfect square numbers which
        # add up to n
        # the sub-problem is defined as:
        # n can be the sum of some square number s and another number m.
        # so results[n] = min(results[n - s] + 1, for each square number < n)
        results = [0]
        for i in xrange(1, num + 1):
            r = min(
                results[i - j * j] + 1
                for j in xrange(1, int(math.sqrt(i)) + 1)
            )
            results.append(r)
        return results[num]


TESTCASES = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 1],
    [5, 2],
    [6, 3],
    [7, 4],
    [8, 2],
    [9, 1],
    [10, 2],
    [11, 3],
    [12, 3],
    [13, 2],
    [14, 3],
    [15, 4],
    [6665, 3],
]


@pytest.mark.parametrize('args,expected', TESTCASES)
def test_perfect_squares(args, expected):
    actual = Solution().numSquares(args)
    assert actual == expected
