#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/integer-replacement/description/

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

    >>> s = Solution()
    >>> s.integerReplacement(1)
    0
    >>> s.integerReplacement(2)
    1
    >>> s.integerReplacement(3)
    2
    >>> s.integerReplacement(8)
    3
    >>> s.integerReplacement(7)
    4

"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n/2)
        return 1 + min(
            self.integerReplacement(n + 1),
            self.integerReplacement(n - 1),
        )
