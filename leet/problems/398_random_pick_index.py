#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/random-pick-index/#/description

Given an array of integers with possible duplicates, randomly output the
index of a given target number. You can assume that the given target number
must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space
will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should
// have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

"""
import pytest
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([
            i for i, n in enumerate(self.nums) if n == target])


TESTCASES = [
    [
        [3, 2, 1, 3, 3], [
            [3, [0, 3, 4]],
            [1, [2]],
        ]
    ],
    [
        [1], [
            [1, [0]]
        ],
    ],
]


@pytest.mark.parametrize('nums, cases', TESTCASES)
def test_random_pick_index(nums, cases):
    s = Solution(nums)
    for num, expected in cases:
        for _ in expected:
            actual = s.pick(num)
            assert actual in expected
