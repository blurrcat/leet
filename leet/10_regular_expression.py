#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
]


@pytest.mark.parametrize('item, pattern, expected', TESTCASES)
def test(item, pattern, expected):
    s = Solution()
    assert s.isMatch(item, pattern) == expected
