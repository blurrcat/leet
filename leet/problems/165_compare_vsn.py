#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise
return 0.

You may assume that the version strings are non-empty and contain only digits
and the . character.
The . character does not represent a decimal point and is used to separate
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it
is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering: 0.1 < 1.1 < 1.2 < 13.37

    >>> s = Solution()
    >>> s.compareVersion('0.1', '0.1')
    0
    >>> s.compareVersion('1.1', '0.1')
    1
    >>> s.compareVersion('0.1', '1.1')
    -1
    >>> s.compareVersion('1.1', '1.2')
    -1
    >>> s.compareVersion('13.37', '1.2')
    1
    >>> s.compareVersion('1.0', '1')
    0
    >>> s.compareVersion('1', '1.0')
    0
    >>> s.compareVersion('1.2.3', '1.2')
    1
    >>> s.compareVersion('1.2', '1.2.3')
    -1

"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(n) for n in version1.split('.')]
        v2 = [int(n) for n in version2.split('.')]
        gt = 1
        # use the longer number as the base for comparison
        if len(v2) > len(v1):
            v1, v2 = v2, v1
            # since we swapped the numbers, the definition of "greater than"
            # should be negated too
            gt = -1
        for i, n in enumerate(v1):
            try:
                if n > v2[i]:
                    return gt
                elif n < v2[i]:
                    return -gt
            except IndexError:
                # v1 is longer than v2
                if v1[i] > 0:
                    return gt
        return 0
