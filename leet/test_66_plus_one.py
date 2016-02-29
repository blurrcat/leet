#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits
        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                return digits
        return [1] + digits


@pytest.mark.parametrize('number', (
    0,
    1,
    9,
    19,
    199,
    1929,
    99999999999999,
))
def test_66_plus_one(number):
    digits = [int(d) for d in str(number)]
    result = [int(d) for d in str(number + 1)]
    s = Solution()
    assert s.plusOne(digits) == result
