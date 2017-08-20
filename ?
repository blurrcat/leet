#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/h-index/description/

Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h
if h of his/her N papers have at least h citations each, and the other N − h
papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher
has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations
respectively. Since the researcher has 3 papers with at least 3 citations
each and the remaining two with no more than 3 citations each, his h-index is
3.

Note: If there are several possible values for h, the maximum one is taken as
the h-index.

    >>> s = Solution()
    >>> s.hIndex([0])
    0
    >>> s.hIndex([1])
    1
    >>> s.hIndex([10])
    1
    >>> s.hIndex([5, 6])
    2
    >>> s.hIndex([1, 0, 3, 6, 5])
    3

"""


class Solution(object):

    def hIndex(self, citations):
        citations.sort(reverse=True)
        N = len(citations)
        for i, c in enumerate(citations):
            h = i + 1
            if h <= c:
                if i == N - 1 or citations[i+1] <= h:
                    return h
        return 0
