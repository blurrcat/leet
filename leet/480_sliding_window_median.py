#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
480. Sliding Window Median Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 5470
Total Submissions: 17571
Difficulty: Hard
Contributors:
YutingLiu
Median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value. So the median is the mean of the two
middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k
numbers in the window. Each time the sliding window moves right by one
position. Your job is to output the median array for each window in the
original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for
non-empty array.
"""
import pytest
import bisect


class Solution(object):

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k == 1:
            return [float(n) for n in nums]
        if k == 2:
            return [
                (n + nums[i + 1]) / 2.0 for i, n in enumerate(nums[:-1])]
        if k % 2 == 0:
            def get_mid(sorted_list):
                n = len(sorted_list)
                i = (n - 1) // 2
                return (sorted_list[i] + sorted_list[i + 1]) / 2.0
        else:
            def get_mid(sorted_list):
                return float(sorted_list[(len(sorted_list) - 1) // 2])

        group = sorted(nums[:k])
        result = [get_mid(group)]
        n = len(nums)
        for i in range(1, n - k + 1):
            # print 'prev group: {}'.format(group),
            # remove last item from group
            del_idx = bisect.bisect_left(group, nums[i - 1])
            del group[del_idx]
            # insert new item
            bisect.insort_left(group, nums[i + k - 1])

            # print 'nums: {}; group: {}'.format(nums[i:i + k], group),
            result.append(get_mid(group))
            # print 'result: ', result
        return result


TESTCASES = [
    [[1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]],
    [[1, 2, 3, 4, 5, ], 2, [1.5, 2.5, 3.5, 4.5]],
    [[1, 2, 3, 4, 5], 3, [2, 3, 4]],
    [[1, 2, 3, 4, 5], 4, [2.5, 3.5]],
    [[1, 2, 3, 4, 5], 5, [3]],
    [[1, 3, -1, -3, 5, 3, 6, 7], 3, [1, -1, -1, 3, 5, 6]],
]


@pytest.mark.parametrize('nums, k, expected', TESTCASES)
def test(nums, k, expected):
    actual = Solution().medianSlidingWindow(nums, k)
    assert actual == expected
