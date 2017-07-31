#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import pytest


class Solution(object):

    def run(self, *args):
        pass


TESTCASES = [
    [[None], None]
]


@pytest.mark.parametrize('args,expected', TESTCASES)
def test(args, expected):
    actual = Solution().run(*args)
    assert actual == expected
