#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import pytest


class Solution(object):

    def run(self):
        pass


TESTCASES = [
]


@pytest.mark.parametrize('args,expected', TESTCASES)
def test(args, expected):
    actual = Solution().run(*args)
    assert actual == expected
