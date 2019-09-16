#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
139. Word Break My Submissions Question
Total Accepted: 79250 Total Submissions: 321614 Difficulty: Medium

Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
import pytest


class Solution(object):
    """
    Define a(i) as accept(a for accept) s[0:i-1]. The problem becomes getting
    a(n), where n = len(s).

    a(0) = True
    a(i) = (
        (a(0) & s[0:i] in dict) or
        (a(1) & s[1:i] in dict) or
         ...
        (a(i-1) & s[i-1:i] in dict)
    ), for n >= i > 0
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not (s and wordDict):
            return False
        n = len(s)
        a = [False] * (n + 1)
        a[0] = True
        wordDict = set(wordDict)
        for i in range(1, n+1):
            for j in range(0, i):
                if a[j] and s[j:i] in wordDict:
                    a[i] = True
                    break
        return a[-1]


@pytest.mark.parametrize('s,words,result', (
    (
        'leetcode',
        ['leet', 'code'],
        True,
    ),
    (
        '',
        ['leet'],
        False,
    ),
    (
        'leetcode',
        ['lee', 'leet', 'code'],
        True,
    ),
    (
        'leet',
        ['e'],
        False,
    ),
    (
        'x',
        ['x'],
        True,
    ),
    (
        'xyx',
        ['xy'],
        False,
    ),
    (
        'bb',
        ['a', 'b', 'bbb', 'bbbb'],
        True,
    ),
    (
        'abcd',
        ['a', 'abc', 'b', 'cd'],
        True,
    ),
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaab",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa",
         "aaaaaaaaa", "aaaaaaaaaa"],
        False,
    ),
    (
        "dcacbcadcad",
        ["cbd", "dca", "bcdc", "dcac", "ad"],
        False,
    ),
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaaa",
        ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa",
         "aaaaaaaaa", "aaaaaaaaaa", "ba"],
        False,
    ),
    (
        'aaabaaba',
        ['aa', 'aaa', 'ba'],
        False,
    ),
))
def test_139_word_break(s, words, result):
    solution = Solution()
    assert solution.wordBreak(s, words) == result
