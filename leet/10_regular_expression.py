#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

Total Accepted: 129950
Total Submissions: 543659
Difficulty: Hard
"""
import pytest
from collections import defaultdict


class Solution(object):

    def isMatch(self, stream, pattern):
        # build the fsm
        fsm = defaultdict(lambda: defaultdict(set))
        i = 0
        initial_state = 1
        state = initial_state
        # receive states: normal state, [repeat state...]
        # repeat state: has at least 1 action that transits to itself,
        # e.g., "a*"
        receive_states = [initial_state]

        pattern_l = len(pattern)
        while i < pattern_l:
            action = pattern[i]
            fsm[state][action].add(state + 1)
            state += 1
            for rs in receive_states[:-1]:
                fsm[rs][action].add(state)
            if i < pattern_l - 1 and pattern[i + 1] == '*':
                fsm[state][action].add(state)
                receive_states.append(state)
                i += 2
            else:
                receive_states = [state]
                i += 1

        stream_l = len(stream)

        def _match(i, state):
            for candidate in (stream[i], '.'):
                next_states = fsm[state].get(candidate, [])
                if i + 1 < stream_l:
                    for ns in next_states:
                        if _match(i + 1, ns):
                            return True
                else:
                    for ns in next_states:
                        if ns in receive_states:
                            return True
            return False

        if not stream:
            return initial_state in receive_states
        return _match(0, initial_state)


def memoize(f):
    cache = {}

    def wrapped(*args):
        if args not in cache:
            # print('cache miss: {}'.format(args))
            cache[args] = f(*args)
        # else:
        #     print('cache hit: {}'.format(args))
        return cache[args]

    return wrapped


class Solution2(object):

    def isMatch(self, stream, pattern):
        stream_l = len(stream)
        pattern_l = len(pattern)

        @memoize
        def _match(si, pi):
            # print('{} {}'.format(si, pi))
            # print('match "{}" with "{}"'.format(stream[si:], pattern[pi:]))
            if si == stream_l:  # stream empty
                # consume one star
                if pi + 1 < pattern_l and pattern[pi + 1] == '*':
                    return _match(si, pi + 2)
                # pattern empty
                elif pi == pattern_l:
                    return True
                else:
                    return False
            # pattern is empty but stream is not
            if pi == pattern_l:
                return False

            if pi + 1 < pattern_l:
                # current pattern is a star closure
                if pattern[pi + 1] == '*':
                    if pattern[pi] in (stream[si], '.'):
                        return (
                            # match and keep star
                            _match(si + 1, pi) or
                            # match and consume star
                            _match(si + 1, pi + 2) or
                            # match 0 and consume star
                            _match(si, pi + 2)
                        )
                    else:  # match 0; consume star
                        return _match(si, pi + 2)
            # try to match one literally
            if pattern[pi] in (stream[si], '.'):
                return _match(si + 1, pi + 1)
            else:
                return False

        return _match(0, 0)


TESTCASES = [
    # examples
    ('aa', 'a', False),
    ('aa', 'aa', True),
    ('aa', 'a*', True),
    ('aa', '.*', True),
    ('ab', '.*', True),
    ('aab', 'c*a*b*', True),
    # edge cases
    ('', 'a', False),
    ('', '.*', True),
    ('', 'a*', True),
    ('', 'a*a*', True),
    ('b', 'a*', False),
    ('a', '', False),
    ('', '', True),
    # greedy?
    ('ab', 'a*b', True),
    ('aa', 'a*b', False),
    # others
    ('acb', 'a.b', True),
    ('a', 'a.*', True),
    ('aa', 'a.*', True),
    ('', 'aa*', False),
    ('a', 'aa*', True),
    ('aa', 'aa*', True),
    ('aaa', 'a*a', True),
    ('aaa', 'a*a*', True),
    ('aaab', 'a*a*b', True),
    ('aaaa', 'a*a*b', False),
    ('aaba', 'ab*a*c*a', False),
    ('aaa', 'ab*ac*a', True),
    ('aaa', 'ab*a*c*a', True),
    ('ab', '.*..', True),
    ('abcdede', 'ab.*de', True),
    ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c', False),
]


@pytest.mark.parametrize('cls', [
    Solution,
    Solution2,
])
@pytest.mark.parametrize('item, pattern, expected', TESTCASES)
def test(cls, item, pattern, expected):
    s = cls()
    assert s.isMatch(item, pattern) == expected
