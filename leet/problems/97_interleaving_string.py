#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/interleaving-string/description/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Tests::

    >>> s = Solution()
    >>> s.isInterleave('', 'a', 'a')
    True
    >>> s.isInterleave('a', '', 'a')
    True
    >>> s.isInterleave('a', '', 'b')
    False
    >>> s.isInterleave('a', 'b', 'a')
    False
    >>> s.isInterleave('a', 'b', 'ab')
    True
    >>> s.isInterleave('a', 'b', 'ba')
    True
    >>> s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    True
    >>> s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
    False

"""


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3

        is_ok = [[False] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                is_ok[i][j] = (
                    i > 0 and is_ok[i-1][j] and s3[i+j-1] == s1[i-1]
                ) or (
                    j > 0 and is_ok[i][j-1] and s3[i+j-1] == s2[j-1]
                ) or (
                    i == j == 0
                )
        return is_ok[l1][l2]
