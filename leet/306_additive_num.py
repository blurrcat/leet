"""
306. Additive Number
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for
the first two numbers, each subsequent number in the sequence must be the sum
of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive
sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100,
199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence
1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine
if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""
import pytest
import random


def _check(num, start, la, lb):
    ia = start + la
    ib = ia + lb
    a = int(num[start: ia])
    b = int(num[ia: ib])
    expected = str(a + b)
    lc = len(expected)
    ic = ib + lc
    if ic > len(num):
        return False
    if num[ib:ic] == expected:
        if ic == len(num):
            return True
        return _check(num, start=ia, la=lb, lb=lc)
    else:
        return False


class Solution(object):

    def isAdditiveNumber(self, num):
        l = len(num)
        if l < 3:
            return False
        for la in range(1, l - 2 + 1):
            for lb in range(1, l - la + 1):
                if _check(num, 0, la, lb):
                    return True
        return False


def generate_large_num(n=1000):
    parts = [random.randint(1, 10000), random.randint(1, 10000)]
    while n > 0:
        num = sum(parts[-2:])
        n -= len(str(num))
        parts.append(num)
    return ''.join(str(p) for p in parts), parts


TESTCASES = [
    ['1', False],
    ['11', False],
    ['112', True],
    ['111', False],
    ['112358', True],
    ['199100199', True],
    ['11213', True],
    [generate_large_num(2)[0], True],
    [generate_large_num(1600)[0], True],
]


def test_generate():
    num = generate_large_num(n=2)
    print(num)
    assert num


@pytest.mark.parametrize('num,expected', TESTCASES)
def test_additive_num(num, expected):
    actual = Solution().isAdditiveNumber(num)
    assert actual == expected
