#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def get_edit_dist(x, y):
    xl = len(x)
    yl = len(y)
    distances = [[0 for _ in range(yl + 1)] for _ in range(xl + 1)]
    distances[0][0] = 0
    for i in range(1, xl + 1):
        distances[i][0] = i
    for j in range(1, yl + 1):
        distances[0][j] = j

    for i in range(1, xl + 1):
        for j in range(1, yl + 1):
            dist = [
                distances[i - 1][j] + 1,  # delete
                distances[i][j - 1] + 1,  # insert
            ]
            if x[i - 1] == y[j - 1]:
                dist.append(distances[i - 1][j - 1])  # match
            else:
                dist.append(distances[i - 1][j - 1] + 1)  # replace
            distances[i][j] = min(dist)

    return distances[xl][yl]


TESTCASES = [
    ['hi', 'hi', 0],
    ['ho', 'hoi', 1],
    ['hi', 'ho', 1],
    ['h', '', 1],
    ['h', 'hh', 1],
    ['', '', 0],
    ['the longest', 'longest day', 8],
    ['GCGTATGCGGCTAACGC', 'GCTATGCGGCTATACGC', 2],
]


@pytest.mark.parametrize('x,y,expected', TESTCASES)
def test(x, y, expected):
    dist = get_edit_dist(x, y)
    assert dist == expected
