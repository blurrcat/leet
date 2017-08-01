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
from leet.ds.binary_tree import BinaryTreeNode as TreeNode


def validate(node, min_v=None, max_v=None):
    if node is None:
        return True
    if (min_v is not None and node.val <= min_v) or (
            max_v is not None and node.val >= max_v):
        return False
    return validate(node.left, min_v, node.val) and validate(
        node.right, node.val, max_v
    )


class Solution(object):

    def isValidBST(self, root):
        return validate(root)


@pytest.mark.parametrize('nodes_list,expected', [
    [[1], True],
    [[], True],
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
