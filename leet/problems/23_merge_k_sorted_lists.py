#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
import pytest
from leet.ds.linked_list import ListNode


class Solution(object):
    """
    In the simple case where there are 2 sorted lists to be merged,
    it is trivial to merge them in O(n), where n is the total number of
    elements in the 2 lists. We denote this operation as `merge2(l1, l2)`.

    Consider there are more than 2 sorted lists. One plausible solution is to
    reduce the lists with `merge2`, like `reduce(merge2, lists)`, or more
    specifically:

        merged = []
        for list in lists:
            merged = merge2(merged, list)

    The time complexity is O(n * k), where k is the number of lists. Note
    that in each iteration, `list` is processed with all elements merged so
    far, which is a waste. Observe that merging k lists can be broken into
    k/2 `merge2` subproblems. By applying this recursively, we come to a
    divide and conquer solution:

        while len(lists) > 1:
            lists = [merge2(*every_2_lists) for every_2_lists in lists]
        return lists[0]

    In each iteration of the while loop, it takes O(n) for all the `merge2`
    operations. Each loop reduce the number of lists roughly by 1/2. Summing
    this up, the time complexity of the solution is O(n * log(k, 2)).
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # filter empty lists
        lists = [l for l in lists if l]
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in xrange(0, len(lists), 2):
                if i + 1 < len(lists):
                    # merge 2 lists
                    a = lists[i]
                    b = lists[i + 1]
                    # insert values from b to a, where a is the list whose
                    # head is smaller
                    if b.val < a.val:
                        a, b = b, a
                    head = prev = a
                    a = a.next
                    while a and b:
                        if a.val < b.val:
                            prev = a
                            a = a.next
                        else:
                            # insert b between prev and a
                            tmp = b
                            b = b.next
                            prev.next = tmp
                            tmp.next = a
                            prev = tmp
                    if b:
                        prev.next = b
                    merged.append(head)
                else:  # one single list left
                    merged.append(lists[i])
            lists = merged
        return lists[0]


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
        [[1, 3], [2, 4]], [1, 2, 3, 4],
    ],
    [
        [[2, 4], [1, 3]], [1, 2, 3, 4],
    ],
    [
        [[1, 3], [2, 4, 5, 6]], [1, 2, 3, 4, 5, 6],
    ],
    [
        [[1, 3, 5, 6], [2, 4]], [1, 2, 3, 4, 5, 6],
    ],
    [
        [[1, 2, 2], [1, 1, 2]], [1, 1, 1, 2, 2, 2],
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
