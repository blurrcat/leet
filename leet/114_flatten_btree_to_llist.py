#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Difficulty: Medium
Total Accepted: 129.1K
Total Submissions: 370.3K
"""


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(node, result):
    result.append(node)
    if node.left:
        traverse(node.left, result)
    if node.right:
        traverse(node.right, result)


class Solution(object):

    def flatten(self, root):
        if not root:
            return
        result = []
        traverse(root, result)
        for i, n in enumerate(result[:-1]):
            n.left = None
            n.right = result[i + 1]
        result[-1].left = result[-1].right = None


def test_flatten_btree():
    nodes = [TreeNode(n) for n in range(6)]
    root = nodes[0]
    root.left, root.right = nodes[1], nodes[4]
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[4].right = nodes[5]
    s = Solution()
    s.flatten(root)
    for i, n in enumerate(nodes[:-1]):
        assert n.val == i
        assert n.left is None
        assert n.right is nodes[i + 1]


def test_edge_cases():
    s = Solution()
    root = TreeNode(0)
    s.flatten(root)
    assert root.right is None
    assert root.left is None
    assert s.flatten(None) is None


def test_left_branch():
    nodes = [TreeNode(n) for n in range(6)]
    for i, n in enumerate(nodes[:-1]):
        n.left = nodes[i + 1]
    s = Solution()
    s.flatten(nodes[0])
    for i, n in enumerate(nodes[:-1]):
        assert n.val == i
        assert n.left is None
        assert n.right is nodes[i + 1]
