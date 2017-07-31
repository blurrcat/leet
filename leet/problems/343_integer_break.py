#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
343. Integer Break
DescriptionHintsSubmissionsSolutions
Total Accepted: 41067
Total Submissions: 90147
Difficulty: Medium
Contributor: LeetCode
Given a positive integer n, break it into the sum of at least two positive
integers and maximize the product of those integers. Return the maximum
product you can get.

For example, given n = 2, return 1 (2 = 1 + 1);
given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
import pytest


class Solution(object):
    """
    Define f(n) as the max product given n.

    We have::

        f(n) = 1, when n = 2
        f(n) = max(g(1) * g(n - 1), ..., g(n//2) * g(n - n//2))), when n > 2

    where g(n) is defined as::

        g(1) = 1, when n = 1
        g(n) = max(n, f(n))

    Each item in the `max` clause of `f(n)` represents one way to divide n.
    For example, 9 can be divided as (3 + 6). 3 and 6 can both be further
    divided. The product of the final divided is biggest if when choose the
    best divide for both 3 and 6. There's another option, which is not to
    divide 3, that's what `g(n)` denotes.
    """

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        # let's pretend f and g are 1-based for convinience
        # 0 is not used
        f = [1] * (n + 1)
        g = [1] * (n + 1)
        g[2] = 2
        for i in range(3, n + 1):
            f[i] = max(g[j] * g[i - j] for j in range(1, (i // 2) + 1))
            g[i] = max(i, f[i])
        return f[n]


TESTCASES = [
    [2, 1],
    [3, 2],
    [4, 4],
    [5, 6],
    [6, 9],
    [7, 12],
    [10, 36],
]


@pytest.mark.parametrize('n,expected', TESTCASES)
def test_integer_break(n, expected):
    actual = Solution().integerBreak(n)
    assert actual == expected
