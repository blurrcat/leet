#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/validate-ip-address/description/

Write a function to check whether an input string is a valid IPv4 address or
IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which
consists of four decimal numbers, each ranging from 0 to 255, separated by
dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address
172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits,
each group representing 16 bits. The groups are separated by colons (":").
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
one. Also, we could omit some leading zeros among four hexadecimal digits
and some low-case characters in the address to upper-case ones, so
2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading
zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single
empty group using two consecutive colons (::) to pursue simplicity. For
example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the
address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the
input string.

IPv4::

    >>> s = Solution()
    >>> s.validIPAddress('172.16.254.1')
    'IPv4'
    >>> s.validIPAddress('172.0.254.1')
    'IPv4'
    >>> s.validIPAddress('172.16.254.-0')
    'Neither'
    >>> s.validIPAddress('172.16.254.0001')
    'Neither'
    >>> s.validIPAddress('256.256.256.256')  # must be in [0, 255]
    'Neither'
    >>> s.validIPAddress('01.001.200.1') # leading zeros are invalid
    'Neither'
    >>> s.validIPAddress('1.1.1') # must be 4 parts
    'Neither'
    >>> s.validIPAddress('1.1..1') # cannot omit entirely
    'Neither'

IPv6::

    >>> s.validIPAddress('2001:0db8:85a3:0000:0000:8A2E:0370:7334')
    'IPv6'
    >>> s.validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334')
    'IPv6'
    >>> s.validIPAddress('2001:0db8')  # too few parts
    'Neither'
    >>> # extra leading zero
    >>> s.validIPAddress('02001:0db8:85a3:0000:0000:8A2E:0370:7334')
    'Neither'
    >>> # invalid digit
    >>> s.validIPAddress('200n:0db8:85a3:0000:0000:8A2E:0370:7334')
    'Neither'
    >>> # cannot omit all if a part is '0000'
    >>> s.validIPAddress('2001:0db8:85a3::0000:8A2E:0370:7334')
    'Neither'
    >>> # omit leading zeros is ok
    >>> s.validIPAddress('2001:db8:85a3:000:00:8A2E:0370:7334')
    'IPv6'

    >>> s.validIPAddress('123')
    'Neither'

"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        no = 'Neither'
        hex = '0123456789abcdefABCDEF'
        if '.' in IP:  # maybe v4
            parts = IP.split('.')
            if len(parts) != 4:
                return no
            for p in parts:
                if p == '0':
                    continue
                if p.startswith('0') or p.startswith('-'):
                    return no
                try:
                    p = int(p)
                except ValueError:
                    return no
                if p < 0 or p > 255:
                    return no
            return 'IPv4'
        elif ':' in IP:  # maybe v6
            parts = IP.split(':')
            if len(parts) != 8:
                return no
            for p in parts:
                if not p or len(p) > 4:
                    return no
                if p == '0':
                    continue
                for digit in p:
                    if digit not in hex:
                        return no
            return 'IPv6'
        return no
