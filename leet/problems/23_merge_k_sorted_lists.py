#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
import pytest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_list(cls, l):
        if l:
            root = parent = ListNode(l[0])
            for v in l[1:]:
                parent.next = ListNode(v)
                parent = parent.next
            return root

    def to_list(self):
        node = self
        l = [node.val]
        while node.next:
            node = node.next
            l.append(node.val)
        return l

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # filter empty lists
        lists = [l for l in lists if l]
        if not lists:
            return None
        while True:
            merged = []
            for i in xrange(0, len(lists), 2):
                if i + 1 < len(lists):
                    # merge 2 lists
                    a = lists[i]
                    b = lists[i + 1]
                    # print 'merging %s and %s' % (a.to_list(), b.to_list())
                    if a.val < b.val:
                        root = ListNode(a.val)
                        a = a.next
                    else:
                        root = ListNode(b.val)
                        b = b.next
                    parent = root
                    while a and b:
                        if a.val < b.val:
                            parent.next = ListNode(a.val)
                            a = a.next
                        else:
                            parent.next = ListNode(b.val)
                            b = b.next
                        parent = parent.next
                    if a:
                        parent.next = a
                    elif b:
                        parent.next = b
                    merged.append(root)
                else:  # one single list left
                    merged.append(lists[i])

            if len(merged) == 1:
                return merged[0]
            lists = merged


@pytest.mark.parametrize('lists,expected', [
    [[], None],
    [
        [[1, 2]], [1, 2],
    ],
    [
        [[1, 2], []], [1, 2],
    ],
    # simple case: merge 2 lists
    [
        [[1, 3], [2, 4]], [1, 2, 3, 4]
    ],
    [
        [[1, 3], [2, 4, 5, 6]], [1, 2, 3, 4, 5, 6]
    ],
    [
        [[1, 3, 5, 6], [2, 4]], [1, 2, 3, 4, 5, 6]
    ],
    # merge more than 2 lists
    [
        [[1, 3], [2, 4], [3, 5]], [1, 2, 3, 3, 4, 5],
    ],
    [
        [[1, 3], [2, 4], [3, 5], [6, 7]], [1, 2, 3, 3, 4, 5, 6, 7],
    ],
])
def test_merge_k_lists(lists, expected):
    s = Solution()
    lists = [ListNode.from_list(l) for l in lists]
    merged = s.mergeKLists(lists)
    if merged:
        assert merged.to_list() == expected
    else:
        assert merged is None
