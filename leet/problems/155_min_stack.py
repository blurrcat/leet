#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
155. Min Stack
DescriptionHintsSubmissionsSolutions
Total Accepted: 127021
Total Submissions: 455047
Difficulty: Easy
Contributor: LeetCode
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

"""
from bisect import insort


class MinStack(object):

    def __init__(self):
        self._data = []
        self._ordered = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        insort(self._ordered, x)

    def pop(self):
        """
        :rtype: void
        """
        if self._data:
            x = self._data.pop()
            self._ordered.remove(x)

    def top(self):
        """
        :rtype: int
        """
        if self._data:
            return self._data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self._ordered:
            return self._ordered[0]


def test_min_stack():
    s = MinStack()
    assert not s.top()
    assert not s.getMin()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
