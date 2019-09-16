#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
456. 132 Pattern
DescriptionHintsSubmissionsSolutions
Total Accepted: 9130
Total Submissions: 32242
Difficulty: Medium
Contributors:
love_Fawn
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence
ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that
takes a list of n numbers as input and checks whether there is a 132 pattern
in the list.

Note: n will be less than 15,000.
"""
import pytest
import random
import bisect


class Solution(object):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = len(nums)
        sorted_nums = sorted(nums)

        def remove_from_sorted(num):
            idx = bisect.bisect_left(sorted_nums, num)
            assert sorted_nums[idx] == num
            del sorted_nums[idx]

        if total < 3:
            return False
        i = 0
        while i < total - 2:
            ai = nums[i]
            remove_from_sorted(ai)
            if nums[i + 1] < ai:
                i += 1
                continue
            else:
                aj = nums[i + 1]
                remove_from_sorted(aj)
            for j in range(i + 2, total):
                if nums[j] >= aj:
                    aj = nums[j]
                    remove_from_sorted(aj)
                else:
                    break
            i = j
            if ai == aj:
                continue

            ai_idx = bisect.bisect_right(sorted_nums, ai)
            aj_idx = bisect.bisect_left(sorted_nums, aj)
            # some number in sorted_nums is between ai and aj
            if aj_idx != ai_idx:
                return True

        return False


TESTCASES = [
    [[1, 1, 0], False],
    [[1, 2, 3, 4], False],
    [[3, 1, 4, 2], True],
    [[-1, 3, 2, 0], True],
    # i, j, k may not be adjacent
    [[2, 5, 6, 4], True],  # [2, 5, 4], [2, 6, 4]
    [[2, 7, 6, 4], True],  # [2, 7, 4], [2, 6, 4]
    [[2, 6, -1, 3], True],  # [2, 6, 3]
    # too few arguments
    [[], False],
    [[1], False],
    [[1, 2], False],
    # performance
    [list(range(15000)) + [1], True],  # [0, 2, 1], ..., [0, 14999, 1]
    [[random.choice([0, 1]) for _ in range(15000)], False]
]


@pytest.mark.parametrize('nums, expected', TESTCASES)
def test_132_pattern(nums, expected):
    assert Solution().find132pattern(nums) == expected
