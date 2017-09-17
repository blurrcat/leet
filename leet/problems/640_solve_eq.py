#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Solve a given equation and return the value of x in the form of string
"x=#value". The equation contains only '+', '-' operation, the variable x and
its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value
of x is an integer.


    >>> s = Solution()
    >>> s.solveEquation('10x+3x+13=-13')
    'x=-2'
    >>> s.solveEquation('x+5-3+x=6+x-2')
    'x=2'
    >>> s.solveEquation('x=x')
    'Infinite solutions'
    >>> s.solveEquation('2x=x')
    'x=0'
    >>> s.solveEquation('2x+3x-6x=x+2')
    'x=-1'
    >>> s.solveEquation('x=x+2')
    'No solution'
    >>> s.solveEquation('10x+20x=30')
    'x=1'
    >>> s.solveEquation('10x+20x=-30')
    'x=-1'
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        x = 0
        d = 0
        sign = 1
        word = ''

        def process_word(w, x, d):
            if not w:
                return x, d
            # print 'process "{}"'.format(w), x, d,
            if w.startswith('-'):
                word_sign = -1
                w = w[1:]
            else:
                word_sign = 1

            if w.endswith('x'):
                w = w[:-1]
                x += sign * word_sign * (int(w) if w else 1)
            else:
                d += sign * word_sign * (int(w) if w else 1)
            # print x, d
            return x, d

        for i, letter in enumerate(equation):
            if letter == '-':
                x, d = process_word(word, x, d)
                word = '-'
            elif letter == '+':
                x, d = process_word(word, x, d)
                word = ''
            elif letter == 'x':
                x, d = process_word(word + 'x', x, d)
                word = ''
            elif letter == '=':
                x, d = process_word(word, x, d)
                word = ''
                sign = -1
            else:  # digits
                word += letter
        x, d = process_word(word, x, d)

        if x == 0:
            if d == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x={}'.format(-d/x)
