#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Input:
       Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7

Output:

             3
            / \
           4   5
          / \   \
         5   4   7

Note: The merging process must start from the root nodes of both trees.
"""
from leet.ds.binary_tree import BinaryTreeNode as TreeNode


def flatten(t, idx, result):
    result[idx] = t.val
    if t.left is not None:
        flatten(t.left, idx * 2 + 1, result)
    if t.right is not None:
        flatten(t.right, idx * 2 + 2, result)
    return result


def unflatten(f, idx):
    node = TreeNode(f[idx])
    l_idx = idx * 2 + 1
    r_idx = l_idx + 1
    if l_idx in f:
        node.left = unflatten(f, l_idx)
    if r_idx in f:
        node.right = unflatten(f, r_idx)
    return node


class Solution(object):

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        f1, f2 = {}, {}
        flatten(t1, 0, f1)
        flatten(t2, 0, f2)
        for k, v in f2.items():
            if k in f1:
                f1[k] += v
            else:
                f1[k] = v
        return unflatten(f1, 0)


def test_merge_2_btrees():
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    s = Solution()
    merged = s.mergeTrees(t1, t2)
    assert merged.val == 3
    assert merged.left.val == 4
    assert merged.right.val == 5
    assert merged.left.left.val == 5
    assert merged.left.right.val == 4
    assert merged.right.right.val == 7


def test_edge_cases():
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(3)
    merged = s.mergeTrees(t1, t2)
    assert merged.val == 4
    assert merged.left is None and merged.right is None

    merged = s.mergeTrees(t1, None)
    assert merged.val == 1
    assert merged.left is None and merged.right is None

    assert s.mergeTrees(None, None) is None
