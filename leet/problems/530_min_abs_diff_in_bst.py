#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a binary search tree with non-negative values, find the minimum
absolute difference between values of any two nodes.
"""
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_min(n):
    while n.left:
        n = n.left
    return n


def tree_max(n):
    while n.right:
        n = n.right
    return n


def min_diff(n):
    diffs = []
    if n.left:
        diffs.append(n.val - tree_max(n.left).val)
    if n.right:
        diffs.append(tree_min(n.right).val - n.val)
    return min(diffs) if diffs else None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minimum = sys.maxsize
        to_visit = [root]
        while to_visit:
            current = to_visit.pop()
            _diff = min_diff(current)
            if _diff and _diff < minimum:
                minimum = _diff
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)
        return minimum


def test_min_abs_diff_bst():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.right = TreeNode(0.5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    assert s.getMinimumDifference(root) == 0.5
