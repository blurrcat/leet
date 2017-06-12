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
from collections import Counter
from fractions import Fraction


class Point(object):

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return 'P({}, {})'.format(self.x, self.y)


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        def __hash__(self):
            return hash((self.x, self.y))

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        p = points[0]
        p.__class__.__hash__ = __hash__
        p.__class__.__eq__ = __eq__
        result = 0
        points_counter = Counter(points)
        uq_points = points_counter.keys()
        for i, p1 in enumerate(uq_points):
            # given p1, a line can be identified by its slope
            slopes = Counter()  # slope to count
            for p2 in uq_points[i + 1:]:
                if p2.x == p1.x:
                    slope = 'vertical'
                else:
                    slope = Fraction(p2.y - p1.y, p2.x - p1.x)
                slopes[slope] += points_counter[p2]
            if slopes:
                local_max = max(slopes.itervalues()) + points_counter[p1]
            else:  # only p1 left
                local_max = points_counter[p1]
            if local_max > result:
                result = local_max
        return result


TESTCASES = [
    [[], 0],
    [[[0, 0]], 1],
    [[[0, 0], [0, 1]], 2],
    [[[0, 0], [0, 0]], 2],
    [[[0, 0], [0, 0], [0, 0]], 3],
    [[[1, 1], [1, 1], [2, 2], [2, 2]], 4],
    [[[0, 0], [0, 0], [0, 1], [1, 1]], 3],
    [[[0, 0], [1, 1], [0, 0], [1, 1]], 4],
    [[[0, 0], [0, 1], [0, 2], [1, 0]], 3],
    [[[0, i] for i in range(1000)], 1000],
    # float precision.. noqa
    [[[0, 0], [94911151, 94911150], [94911152, 94911151]], 2],
    [[[-240, -657], [-27, -188], [-616, -247], [-264, -311], [-352, -393], [-270, -748], [3, 4], [-308, -87], [150, 526], [0, -13], [-7, -40], [-3, -10], [-531, -892], [-88, -147], [4, -3], [-873, -555], [-582, -360], [-539, -207], [-118, -206], [970, 680], [-231, -47], [352, 263], [510, 143], [295, 480], [-590, -990], [-236, -402], [308, 233], [-60, -111], [462, 313], [-270, -748], [-352, -393], [-35, -148], [-7, -40], [440, 345], [388, 290], [270, 890], [10, -7], [60, 253], [-531, -892], [388, 290], [-388, -230], [340, 85], [0, -13], [770, 473], [0, 73], [873, 615], [-42, -175], [-6, -8], [49, 176], [308, 222], [170, 27], [-485, -295], [170, 27], [510, 143], [-18, -156], [-63, -316], [-28, -121], [396, 304], [472, 774], [-14, -67], [-5, 7], [-485, -295], [118, 186], [-154, -7], [-7, -40], [-97, -35], [4, -9], [-18, -156], [0, -31], [-9, -124], [-300, -839], [-308, -352], [-425, -176], [-194, -100], [873, 615], [413, 676], [-90, -202], [220, 140], [77, 113], [-236, -402], [-9, -124], [63, 230], [-255, -118], [472, 774], [-56, -229], [90, 228], [3, -8], [81, 196], [970, 680], [485, 355], [-354, -598], [-385, -127], [-2, 7], [531, 872], [-680, -263], [-21, -94], [-118, -206], [616, 393], [291, 225], [-240, -657], [-5, -4], [1, -2], [485, 355], [231, 193], [-88, -147], [-291, -165], [-176, -229], [154, 153], [-970, -620], [-77, 33], [-60, -111], [30, 162], [-18, -156], [425, 114], [-177, -304], [-21, -94], [-10, 9], [-352, -393], [154, 153], [-220, -270], [44, -24], [-291, -165], [0, -31], [240, 799], [-5, -9], [-70, -283], [-176, -229], [3, 8], [-679, -425], [-385, -127], [396, 304], [-308, -352], [-595, -234], [42, 149], [-220, -270], [385, 273], [-308, -87], [-54, -284], [680, 201], [-154, -7], [-440, -475], [-531, -892], [-42, -175], [770, 473], [118, 186], [-385, -127], [154, 153], [56, 203], [-616, -247]], 24],  # noqa
]


@pytest.mark.parametrize('points,expected', TESTCASES)
def test_max_points(points, expected):
    points = [Point(x, y) for x, y in points]
    actual = Solution().maxPoints(points)
    assert actual == expected
