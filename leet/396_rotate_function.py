#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
396. Rotate Function
DescriptionHintsSubmissionsSolutions
Total Accepted: 18304
Total Submissions: 57618
Difficulty: Medium
Contributor: LeetCode
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions
clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:
```
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
```
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""
import pytest


class Solution(object):

    def maxRotateFunction(self, A):
        """
        Notice F(k) - F(k-1) = sum(A) - n * Bk(0), where n = len(A)

        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        n = len(A)
        total = 0
        f = 0
        for i, a in enumerate(A):
            f += i * a
            total += a
        result = f
        for k in range(1, n):
            f2 = f + total - n * A[-k]
            if f2 > result:
                result = f2
            f = f2
        return result


TESTCASES = [
    [[], 0],
    [[4, 3, 2, 6], 26],
    [[0], 0],
    [[1, 2], 2],
    [[-1, 1], 1],
    [[-10, 10, 1], 12],
    [[1] * 9999, 49985001],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 330],
]


@pytest.mark.parametrize('A, expected', TESTCASES)
def test(A, expected):
    s = Solution()
    actual = s.maxRotateFunction(A)
    assert actual == expected
    A = A[-1:] + A[:-1]
    actual = s.maxRotateFunction(A)
    assert actual == expected
