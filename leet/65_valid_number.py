#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.

Acceptance: 12.6%
"""
import pytest
import string

# once you figure out all possible cases, draw a FSM and there you go


SIGNS = {'+', '-'}
DIGITS = set(string.digits)


class FSM(object):

    absorb_states = {
        'integer',
        'float',
        'float_point',
        'sci',
    }

    def __init__(self):
        self.state = 'initial'

    def parse(self, stream):
        if not stream:
            return False
        for token in stream.strip():
            # old_state = self.state
            action = getattr(self, 'on_{}'.format(self.state))
            self.state = action(token)
            # print('{} - {} -> {}'.format(old_state, token, self.state))
            if not self.state:
                return False  # undefined state
        return self.state in self.absorb_states

    def on_initial(self, token):
        if token in SIGNS:
            return 'signed'
        if token in DIGITS:
            return 'integer'
        if token == '.':
            return 'single_dot'

    def on_signed(self, token):
        if token in DIGITS:
            return 'integer'
        if token == '.':
            return 'single_dot'

    def on_integer(self, token):
        if token in DIGITS:
            return 'integer'
        if token == 'e':
            return 'sci_e'
        if token == '.':
            return 'float_point'

    def on_single_dot(self, token):
        if token in DIGITS:
            return 'float'

    def on_sci_e(self, token):
        if token in DIGITS:
            return 'sci'
        if token in SIGNS:
            return 'sci_e_signed'

    def on_sci(self, token):
        if token in DIGITS:
            return 'sci'

    on_sci_e_signed = on_sci

    def on_float_point(self, token):
        if token in DIGITS:
            return 'float'
        if token == 'e':
            return 'sci_e'

    def on_float(self, token):
        if token in DIGITS:
            return 'float'
        if token == 'e':
            return 'sci_e'


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return FSM().parse(s)


TESTCASES = [
    ['', False],
    ['0', True],
    ['+1', True],
    ['-1', True],
    [' 0.1', True],
    ['0.1 ', True],
    ['.1', True],
    ['1.', True],
    ['.', False],
    ['abc', False],
    ['1 a', False],
    ['2e10', True],
    ['2e-10', True],
    ['0e0', True],
    ['1e', False],
    ['e1', False],
    ['+1e-02', True],
    ['46.e3', True],
    ['46.e-3', True],
    ['46.e+3', True],
    ['.2e4', True],
    ['1.2e-4', True],
]


@pytest.mark.parametrize('s,expected', TESTCASES)
def test_65_valid_number(s, expected):
    assert Solution().isNumber(s) == expected
