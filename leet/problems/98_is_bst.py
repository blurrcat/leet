#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/validate-binary-search-tree/#/description

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key. The right subtree of a node contains only nodes with keys greater than
the node's key. Both the left and right subtrees must also be binary search
trees.
Example 1:

    2
   / \
  1   3

Binary tree [2,1,3], return true.
Example 2:

    1
   / \
  2   3

Binary tree [1,2,3], return false.
"""
import pytest
from ds import TreeNode


def visit(node, parent_val=None, is_left=None):
    if not node:
        return True
    if node.val == 2:
        import pdb
        pdb.set_trace()
    if node.left:
        l_val = node.left.val
        if not l_val < node.val:
            return False
        if parent_val:
            if is_left and not l_val < parent_val:
                return False
            if not is_left and not l_val > parent_val:
                return False
    if node.right:
        l_val = node.right.val
        if not l_val > node.val:
            return False
        if parent_val:
            if is_left and not l_val < parent_val:
                return False
            if not is_left and not l_val > parent_val:
                return False
    return visit(
        node.left, node.val, True) and visit(node.right, node.val, False)


class Solution(object):

    def isValidBST(self, root):
        return visit(root)


@pytest.mark.parametrize('nodes_list,expected', [
    [[2, 1, 3], True],
    [[1, 2, 3], False],
    [[10, 5, 15, None, None, 6, 20], False],
    [[3, 1, 5, 0, 2, 4, 6], True],
    [[3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False]
])
def test_is_bst(nodes_list, expected):
    s = Solution()
    t = TreeNode.from_list(nodes_list)
    actual = s.isValidBST(t)
    assert actual == expected
