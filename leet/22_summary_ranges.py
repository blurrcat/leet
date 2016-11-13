#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
228. Summary Ranges   My Submissions QuestionEditorial Solution
Total Accepted: 45064 Total Submissions: 185561 Difficulty: Medium

Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
import pytest


class Solution(object):

    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        r = []

        def format_range(cur):
            return '{}->{}'.format(*cur) if cur[1] else str(cur[0])

        current = [nums[0], None]

        for i, num in enumerate(nums[1:]):
            if num == nums[i] + 1:
                current[1] = num
            else:
                r.append(format_range(current))
                current = [num, None]
        if current:
            r.append(format_range(current))
        return r


TESTCASES = [
    [[0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]],
    [[], []],
    [[0], ['0']],
    [[1, 3], ['1', '3']],
    [[1, 2], ['1->2']],
    [range(1, 10000), ['1->9999']]
]


@pytest.mark.parametrize('nums,ranges', TESTCASES)
def test(nums, ranges):
    s = Solution()
    assert s.summaryRanges(nums) == ranges
