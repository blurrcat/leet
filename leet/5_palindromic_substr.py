#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
5. Longest Palindromic Substring
DescriptionHintsSubmissionsSolutions
Total Accepted: 200626
Total Submissions: 798920
Difficulty: Medium
Contributor: LeetCode
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.
"""
import pytest


class Solution(object):

    def longestPalindrome(self, s):
        ls = len(s)
        if ls == 1:
            return s
        longest = s[0]
        for i in range(0, ls):
            # without a centroid: "baab"
            l = 1
            candidate_l = 0
            while i + 1 - l >= 0 and i + l < ls:
                if s[i + 1 - l] == s[i + l]:
                    candidate_l = l
                    l += 1
                else:  # mismatch
                    break
            if 2 * candidate_l > len(longest):
                longest = s[i + 1 - candidate_l:i + candidate_l + 1]
            # with a centroid: "bab"
            l = 1
            candidate_l = 0
            while i - l >= 0 and i + l < ls:
                if s[i - l] == s[i + l]:
                    candidate_l = l
                    l += 1
                else:  # mismatch
                    break
            if 1 + 2 * candidate_l > len(longest):
                longest = s[i - candidate_l:i + candidate_l + 1]
        return longest


TESTCASES = [
    ['a', 'a'],
    ['aa', 'aa'],
    ['aaa', 'aaa'],
    ['abbac', 'abba'],
    ['caba', 'aba'],
    ['babad', 'bab'],
    ['cbbd', 'bb'],
    ['a' * 499 + 'bb' + 'a' * 499, 'a' * 499 + 'bb' + 'a' * 499],
    ['a' * 499 + 'bcb' + 'a' * 499, 'a' * 499 + 'bcb' + 'a' * 499],
]


@pytest.mark.parametrize('s,expected', TESTCASES)
def test(s, expected):
    actual = Solution().longestPalindrome(s)
    assert actual == expected
