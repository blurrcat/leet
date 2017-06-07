#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
149. Max Points on a Line
DescriptionHintsSubmissionsSolutions
Total Accepted: 78038
Total Submissions: 507756
Difficulty: Hard
Contributor: LeetCode
Given n points on a 2D plane, find the maximum number of points that lie on
the same straight line.
"""
import pytest
from collections import defaultdict


class Point(object):

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    __repr__ = __str__


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lines = defaultdict(set)
        if not points:
            return 0
        if len(points) == 1:
            return 1
        for i, p1 in enumerate(points):
            for p2 in points[i:]:
                if p2.x - p1.x == 0:
                    b = p1.x
                    k = 'inf'
                else:
                    b = (p2.x * p1.y - p2.y * p1.x) / (p2.x - p1.x)
                    k = (p2.y - b) / float(p2.x)
                line = lines[(k, b)]
                line.add(p1)
                line.add(p2)
        return max(len(l) for l in lines.itervalues())


TESTCASES = [
    [[], 0],
    [[[0, 0]], 1],
    [[[0, 0], [0, 1]], 2],
    [[[0, 0], [0, 1], [0, 2], [1, 0]], 3],
    [[[0, i] for i in range(1000)], 1000]
]


@pytest.mark.parametrize('points,expected', TESTCASES)
def test_max_points(points, expected):
    points = [Point(x, y) for x, y in points]
    actual = Solution().maxPoints(points)
    assert actual == expected
