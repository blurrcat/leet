#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
137. Single Number II
DescriptionHintsSubmissionsSolutions
Total Accepted: 114622
Total Submissions: 279554
Difficulty: Medium
Contributor: LeetCode
Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
"""
import pytest


class Solution(object):
    """
    A naive solution is to use a counter for each unique integer in the list.
    That means O(k) space is used, where k is the number of unique items in
    the list.

    I'm not sure where the idea of the "right" solution comes from, but here
    it is, shamelessly taken from Leetcode's solutions section.

    Observe integers' binary representation.
    For breivity, say our integers are represented with 4 bits. That is,
    1 is 0b0001, 4 is 0b0100, 6 is 0b0110. Now, assume our input is
    [4, 4, 4, 1]. Let's layout their binary repr vertically::

                4    4    4    1

          heigh 0    0    0    0
                1    1    1    0
                0    0    0    0
          low   0    0    0    1

    It seems we can "count" each row independently. We need a counter for each
    row. The counter should incr if we see a binary "1" coming, and go back
    to 0 if it's current value is 3. The genious of the solution is to
    represent the counter using 2 bits::

                4    4    4    1      2-bit-counter    base-10-counter

          heigh 0    0    0    0        0    0              0
                1    1    1    0        0    0              0
                0    0    0    0        0    0              0
          low   0    0    0    1        0    1              1

    We're using 2 bits because that's what it takes to represent a number
    up to 3. The task becomes manipulating the 2-bit counter for each incoming
    number. The counter initialize to 0b00. The following are possible changes
    depending on the current value of the counter and the incoming number::

        counter    incoming    new-counter    base-10-counter
        0    0        0         0    0              0
        0    1        0         0    1              1
        1    0        0         1    0              2
        0    0        1         0    1              1
        0    1        1         1    0              2
        1    0        1         1    1              3
    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for n in nums:
            next_a = (a & ~b & ~n) | (~a & b & n)
            b = (~a & b & ~n) | (~a & ~b & n)
            a = next_a
        return a | b


long = [-1]
for _ in range(3):
    for i in range(10000):
        long.append(i)


TESTCASES = [
    [[1, 1, 1, 2], 2],
    [[2, 1, 1, 1], 2],
    [[1, 2, 1, 2, 1, 2, 3], 3],
    [long, -1]
]


@pytest.mark.parametrize('nums,expected', TESTCASES)
def test_single_number_ii(nums, expected):
    actual = Solution().singleNumber(nums)
    assert actual == expected
