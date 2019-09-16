#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
import pytest
import functools
import operator
import math


class Solution(object):

    def rangeBitwiseAnd(self, min_, max_):
        if min_ == 0:
            return 0
        if min_ == max_:
            return min_
        bits = int(math.log(max_, 2))
        if min_ < 2 ** bits:
            return 0
        for shift in range(1, bits + 1):
            if (min_ >> shift) == (max_ >> shift):
                return min_ >> shift << shift


TESTCASES = [
    [0, 0],
    [0, 1],
    [1, 1],
    [2, 2],
    [5, 7],
    [34, 63],
    [34, 64],
    [1, 2],
    [1, 3],
    [2, 3],
    [2, 4],
    [2, 5],
    [2, 8],
    [5, 8],
    [7, 8],
    [512, 1023],
    [1000, 1023],
]


@pytest.mark.parametrize('m,n', TESTCASES)
def test_bit_and_range(m, n):
    actual = Solution().rangeBitwiseAnd(m, n)
    assert actual == functools.reduce(operator.and_, range(m, n + 1))
