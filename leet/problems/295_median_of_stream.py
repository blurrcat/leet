#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.

    >>> finder = MedianFinder()
    >>> finder.findMedian()
    >>> finder.addNum(1)
    >>> finder.findMedian()
    1
    >>> finder.addNum(2)
    >>> finder.findMedian()
    1.5
    >>> finder.addNum(3)
    >>> finder.findMedian()
    2

    >>> finder = MedianFinder()
    >>> finder.findMedian()
    >>> finder.addNum(2)
    >>> finder.findMedian()
    2
    >>> finder.addNum(1)
    >>> finder.findMedian()
    1.5
    >>> finder.addNum(3)
    >>> finder.findMedian()
    2
"""
import bisect


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._nums = []
        self._median = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        i = bisect.bisect(self._nums, num)
        self._nums.insert(i, num)
        length = len(self._nums)
        mid = int(length / 2)
        if length % 2 == 1:
            self._median = self._nums[mid]
        else:
            self._median = sum(self._nums[mid - 1: mid + 1]) / 2.0

    def findMedian(self):
        """
        :rtype: float
        """
        return self._median
