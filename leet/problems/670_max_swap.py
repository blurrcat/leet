#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a non-negative integer, you could swap two digits at most once to get
the maximum valued number. Return the maximum valued number you could get.

    >>> s = Solution()
    >>> s.maximumSwap(1)
    1
    >>> s.maximumSwap(10)
    10
    >>> s.maximumSwap(12)
    21
    >>> s.maximumSwap(2736)
    7236
    >>> s.maximumSwap(9973)
    9973
    >>> s.maximumSwap(9973)
    9973
    >>> s.maximumSwap(856)
    865
    >>> s.maximumSwap(88457)
    88754

"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        digits = []  # low -> high
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        # the index of the largest digit from digits[0] to digits[i]
        largests = [0]
        for i in range(1, len(digits)):
            idx = largests[-1]
            if digits[i] > digits[idx]:
                largests.append(i)
            else:
                largests.append(idx)
        for i in range(len(digits) - 1, -1, -1):
            idx = largests[i]
            if digits[idx] > digits[i]:
                digits[idx], digits[i] = digits[i], digits[idx]
                break
        return sum(10 ** i * digit for i, digit in enumerate(digits))
